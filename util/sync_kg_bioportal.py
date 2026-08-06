#!/usr/bin/env python3
"""Sync script for KG-Bioportal ontology transforms.

KG-Bioportal (https://ncbo.github.io/kg-bioportal/graphs/) transforms BioPortal
ontologies to KGX TSV. It publishes ~1300 transform records, which is far too many
to carry as a product inventory on a single KG-Registry page, and most of those
records describe ontologies KG-Registry does not track at all.

So this sync does not mirror the manifest into the ``kg-bioportal`` resource page
the way ``sync_obo_foundry.py`` mirrors OBO Foundry. Instead it works like a
side-channel annotation pass: for every successfully transformed ontology that
*already* has a KG-Registry resource page, it adds (or refreshes) a single
GraphProduct on that page pointing at the KGX release asset. The ``kg-bioportal``
resource page itself just links to the graph browser.

Deliberate omissions:

* Failed and skipped transforms are never written. KG-Bioportal records those so
  its own site can explain the gap; there is no artifact for KG-Registry to list.
* New resources are never created. KG-Bioportal draws part of its graph listing
  from KG-Registry, so minting resources from its manifest would be a circular
  sync.
* The synced products do **not** name ``kg-bioportal`` in ``original_source`` or
  ``secondary_source``. ``propagate_products`` (util/extract-metadata.py) copies
  every product onto the page of each resource it cites as a source, so naming the
  aggregator there would rebuild the 1000-entry inventory this design exists to
  avoid. The KG-Bioportal provenance lives in the product name, description, and
  release URL instead.

Acronym-to-resource matching is deliberately conservative: see ``resolve_match``.
"""

from __future__ import annotations

import argparse
import copy
import csv
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import frontmatter  # type: ignore
import yaml

try:
    from util.common import CustomRuamelYAMLHandler, dump_frontmatter_text
    from util.source_associations import make_original_source_associations
except ModuleNotFoundError:
    from common import CustomRuamelYAMLHandler, dump_frontmatter_text
    from source_associations import make_original_source_associations


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


ONTO_STATS_URL = (
    "https://github.com/ncbo/kg-bioportal/releases/latest/download/onto_stats.yaml"
)
TOTAL_STATS_URL = (
    "https://github.com/ncbo/kg-bioportal/releases/latest/download/total_stats.yaml"
)
# Suffix appended to a resource id to form the id of its KG-Bioportal product.
PRODUCT_SUFFIX = "kg-bioportal"

# Fields on a synced product that this script owns. Anything else on an existing
# product (product_file_size from the size-retrieval pass, curator warnings, ...)
# is left alone.
MANAGED_PRODUCT_FIELDS = (
    "id",
    "name",
    "category",
    "description",
    "product_url",
    "format",
    "compression",
    "node_count",
    "edge_count",
    "latest_version",
    "original_source",
)

# Tokens that carry no discriminating signal when comparing two ontology names.
NAME_STOPWORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "classification",
        "controlled",
        "data",
        "database",
        "for",
        "in",
        "of",
        "ontologies",
        "ontology",
        "resource",
        "system",
        "taxonomy",
        "terminology",
        "the",
        "thesaurus",
        "to",
        "version",
        "vocabulary",
    }
)

# Minimum name similarity for an acronym match to be accepted without curation.
# Calibrated against the current manifest: every genuine acronym collision in it
# (RO/Radiomics vs. Relation Ontology, PSO/PatientSafety vs. Plant Stress, ...)
# scores 0.0, while the loosest genuine match scores 0.33.
MIN_NAME_SIMILARITY = 0.3

# Minimum per-token similarity for two name tokens to count as the same word.
# 0.85 accepts inflections like relations/relation and planarian/planaria while
# rejecting atom/atlas. It sits just above phenotypic/phenotype (0.84), which is
# why PATO needs an entry in the sync map.
MIN_TOKEN_SIMILARITY = 0.85


def name_tokens(name: str) -> List[str]:
    """Split an ontology name into lowercase content tokens."""
    return [
        token
        for token in re.split(r"[^a-z0-9]+", (name or "").lower())
        if token and token not in NAME_STOPWORDS
    ]


def name_similarity(first: str, second: str) -> float:
    """Score how much two ontology names overlap, from 0.0 to 1.0.

    Coverage is computed in both directions and the better one wins, so a name
    that is a subset of the other ("Uber Anatomy Ontology" against "Uberon
    multi-species anatomy ontology") still scores well.
    """
    first_tokens = name_tokens(first)
    second_tokens = name_tokens(second)
    if not first_tokens or not second_tokens:
        return 0.0

    def coverage(left: List[str], right: List[str]) -> float:
        matched = sum(
            1
            for token in left
            if any(
                SequenceMatcher(None, token, other).ratio() >= MIN_TOKEN_SIMILARITY
                for other in right
            )
        )
        return matched / len(left)

    return max(coverage(first_tokens, second_tokens), coverage(second_tokens, first_tokens))


def normalized_name(name: str) -> str:
    """Reduce a name to comparable alphanumerics."""
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


class KGBioportalSync:
    """Annotate KG-Registry resources with their KG-Bioportal KGX transforms."""

    def __init__(
        self,
        registry_root: Optional[str] = None,
        cache_ttl_hours: int = 24,
        map_path: Optional[str] = None,
        report_path: Optional[str] = None,
    ):
        script_dir = Path(__file__).resolve().parent
        self.repo_root = script_dir.parent
        self.registry_root = (
            Path(registry_root) if registry_root is not None else self.repo_root / "resource"
        )
        self.cache_ttl_hours = cache_ttl_hours
        self.cache_dir = self.repo_root / "cache"
        self.cache_file = self.cache_dir / "kg_bioportal_cache.yaml"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.map_path = (
            Path(map_path) if map_path is not None else script_dir / "kg_bioportal_sync_map.yaml"
        )
        self.report_path = (
            Path(report_path)
            if report_path is not None
            else self.repo_root / "reports" / "kg_bioportal_unmatched.tsv"
        )

        self.yaml_handler = CustomRuamelYAMLHandler()
        self.confirmed_matches, self.rejected_acronyms = self._load_sync_map()
        self.resource_names = self._load_resource_names()
        self.resources_by_name = self._index_resources_by_name()

    # ----------------------------------------------------------------- inputs

    def _load_sync_map(self) -> Tuple[Dict[str, str], set]:
        """Load curator decisions about which acronym belongs to which resource."""
        confirmed: Dict[str, str] = {}
        rejected: set = set()
        if not self.map_path.exists():
            logger.warning("No KG-Bioportal sync map at %s", self.map_path)
            return confirmed, rejected

        try:
            data = yaml.safe_load(self.map_path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            logger.warning("Failed to load KG-Bioportal sync map: %s", exc)
            return confirmed, rejected

        for acronym, resource_id in (data.get("confirmed") or {}).items():
            if isinstance(resource_id, str) and resource_id.strip():
                confirmed[str(acronym).upper()] = resource_id.strip()
        for acronym in data.get("rejected") or []:
            rejected.add(str(acronym).upper())

        overlap = set(confirmed) & rejected
        if overlap:
            logger.warning(
                "Acronyms listed as both confirmed and rejected are treated as rejected: %s",
                ", ".join(sorted(overlap)),
            )
            for acronym in overlap:
                confirmed.pop(acronym, None)

        logger.info(
            "Loaded KG-Bioportal sync map: %s confirmed, %s rejected",
            len(confirmed),
            len(rejected),
        )
        return confirmed, rejected

    def _load_resource_names(self) -> Dict[str, str]:
        """Map each existing resource id to its display name."""
        names: Dict[str, str] = {}
        if not self.registry_root.exists():
            return names

        for resource_dir in sorted(self.registry_root.iterdir()):
            if not resource_dir.is_dir():
                continue
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if not resource_file.exists():
                continue
            try:
                metadata = frontmatter.load(resource_file).metadata
            except Exception as exc:
                logger.warning("Failed to read %s: %s", resource_file, exc)
                continue
            name = metadata.get("name") if isinstance(metadata, dict) else None
            names[resource_dir.name] = str(name) if name else resource_dir.name
        return names

    def _index_resources_by_name(self) -> Dict[str, List[str]]:
        index: Dict[str, List[str]] = {}
        for resource_id, name in self.resource_names.items():
            index.setdefault(normalized_name(name), []).append(resource_id)
        return index

    def resource_file(self, resource_id: str) -> Path:
        return self.registry_root / resource_id / f"{resource_id}.md"

    # ------------------------------------------------------------ manifest IO

    def _is_cache_valid(self) -> bool:
        if not self.cache_file.exists():
            return False
        cache_age_hours = (time.time() - os.path.getmtime(self.cache_file)) / 3600
        if cache_age_hours < self.cache_ttl_hours:
            logger.info(
                "KG-Bioportal cache is valid (age: %.1f hours, TTL: %s hours)",
                cache_age_hours,
                self.cache_ttl_hours,
            )
            return True
        logger.info(
            "KG-Bioportal cache expired (age: %.1f hours, TTL: %s hours)",
            cache_age_hours,
            self.cache_ttl_hours,
        )
        return False

    def _load_from_cache(self) -> Optional[Dict[str, Any]]:
        try:
            data = yaml.safe_load(self.cache_file.read_text(encoding="utf-8"))
        except Exception as exc:
            logger.warning("Failed to load KG-Bioportal cache: %s", exc)
            return None
        if isinstance(data, dict) and isinstance(data.get("ontologies"), list):
            logger.info(
                "Loaded %s KG-Bioportal transform records from cache", len(data["ontologies"])
            )
            return data
        return None

    def _save_to_cache(self, data: Dict[str, Any]) -> None:
        try:
            self.cache_file.write_text(
                yaml.safe_dump(data, default_flow_style=False, sort_keys=False),
                encoding="utf-8",
            )
        except Exception as exc:
            logger.warning("Failed to save KG-Bioportal cache: %s", exc)

    @staticmethod
    def _fetch_yaml(url: str) -> Any:
        with urlopen(url, timeout=60) as response:  # noqa: S310
            return yaml.safe_load(response.read().decode("utf-8"))

    def fetch_manifest(self) -> Dict[str, Any]:
        """Return the KG-Bioportal manifest as ``{ontologies: [...], totals: {...}}``."""
        if self._is_cache_valid():
            cached = self._load_from_cache()
            if cached is not None:
                return cached

        logger.info("Fetching fresh KG-Bioportal manifest from %s", ONTO_STATS_URL)
        try:
            onto_stats = self._fetch_yaml(ONTO_STATS_URL)
            if not isinstance(onto_stats, dict) or not isinstance(
                onto_stats.get("ontologies"), list
            ):
                raise ValueError("Expected onto_stats.yaml with a top-level 'ontologies' list")

            try:
                totals = self._fetch_yaml(TOTAL_STATS_URL)
            except (HTTPError, URLError, yaml.YAMLError) as exc:
                # The per-ontology records are what the sync actually needs; the
                # totals are only used for logging, so a miss here is not fatal.
                logger.warning("Failed to fetch KG-Bioportal totals: %s", exc)
                totals = {}

            manifest = {
                "ontologies": onto_stats["ontologies"],
                "totals": totals if isinstance(totals, dict) else {},
            }
            self._save_to_cache(manifest)
            logger.info(
                "Successfully fetched %s KG-Bioportal transform records",
                len(manifest["ontologies"]),
            )
            return manifest
        except (HTTPError, URLError, ValueError, yaml.YAMLError) as exc:
            logger.error("Failed to fetch KG-Bioportal manifest: %s", exc)
            if self.cache_file.exists():
                logger.warning("Attempting to use expired KG-Bioportal cache as fallback")
                cached = self._load_from_cache()
                if cached is not None:
                    return cached
            raise

    # ------------------------------------------------------------- matching

    def resolve_match(self, entry: Dict[str, Any]) -> Tuple[Optional[str], str]:
        """Decide which KG-Registry resource an ontology entry belongs to.

        Returns ``(resource_id, reason)``. ``resource_id`` is None when the entry
        should not be written, and ``reason`` says why -- ``no_resource`` and
        ``name_mismatch`` mean "a curator could promote this via the sync map",
        while ``rejected`` means a curator already said no.

        Three ways an entry can match, in order of authority:

        1. ``confirmed`` in the sync map. BioPortal acronyms are not KG-Registry
           ids, and the two drift apart in both directions -- the Relation
           Ontology is ``OBOREL`` on BioPortal, and BioPortal's ``RO`` is the
           unrelated Radiomics Ontology -- so curated pairs win outright.
        2. ``rejected`` in the sync map: never written.
        3. The lowercased acronym is an existing resource id *and* the two names
           are similar enough to rule out an acronym collision.
        """
        acronym = str(entry.get("id", "")).strip().upper()
        if not acronym:
            return None, "no_acronym"

        if acronym in self.rejected_acronyms:
            return None, "rejected"

        confirmed_id = self.confirmed_matches.get(acronym)
        if confirmed_id:
            if confirmed_id in self.resource_names:
                return confirmed_id, "confirmed"
            logger.warning(
                "Sync map points %s at resource '%s', which does not exist", acronym, confirmed_id
            )
            return None, "confirmed_missing"

        resource_id = acronym.lower()
        if resource_id not in self.resource_names:
            return None, "no_resource"

        # A non-OK entry can only ever remove a product this sync itself wrote,
        # so it does not need the name check -- and skiplist entries carry no
        # name to check against anyway.
        if str(entry.get("status", "")).upper() != "OK":
            return resource_id, "acronym"

        similarity = name_similarity(entry.get("name", ""), self.resource_names[resource_id])
        if similarity < MIN_NAME_SIMILARITY:
            return None, "name_mismatch"
        return resource_id, "acronym"

    def suggest_resource(self, entry: Dict[str, Any]) -> str:
        """Suggest a resource for an unmatched entry, for the review report."""
        candidates = self.resources_by_name.get(normalized_name(entry.get("name", "")), [])
        return ",".join(candidates)

    @staticmethod
    def _resolution_rank(resolution: Tuple[Dict[str, Any], str]) -> Tuple[int, int, str]:
        """Rank competing entries for one resource; lower sorts first (wins)."""
        entry, reason = resolution
        is_ok = str(entry.get("status", "")).upper() == "OK"
        return (
            0 if is_ok else 1,
            0 if reason == "confirmed" else 1,
            str(entry.get("id", "")),
        )

    def pick_winners(
        self, resolutions: List[Tuple[Dict[str, Any], str, str]]
    ) -> List[Tuple[Dict[str, Any], str]]:
        """Reduce resolved entries to one per resource.

        BioPortal hosts the same ontology under more than one acronym -- the
        Epilepsy Ontology is both EPIO and EPILONT -- and every entry resolving
        to a given resource would write the same product id. Choose one rather
        than letting manifest order decide which wins.
        """
        by_resource: Dict[str, List[Tuple[Dict[str, Any], str]]] = {}
        for entry, resource_id, reason in resolutions:
            by_resource.setdefault(resource_id, []).append((entry, reason))

        winners: List[Tuple[Dict[str, Any], str]] = []
        for resource_id, candidates in sorted(by_resource.items()):
            candidates.sort(key=self._resolution_rank)
            winner = candidates[0]
            if len(candidates) > 1:
                logger.warning(
                    "Resource %s matched %s KG-Bioportal entries (%s); using %s",
                    resource_id,
                    len(candidates),
                    ", ".join(str(entry.get("id")) for entry, _ in candidates),
                    winner[0].get("id"),
                )
            winners.append((winner[0], resource_id))
        return winners

    # -------------------------------------------------------------- products

    def build_product(self, entry: Dict[str, Any], resource_id: str) -> Dict[str, Any]:
        """Build the GraphProduct describing one KG-Bioportal transform."""
        acronym = str(entry["id"]).strip().upper()
        source_name = str(entry.get("name") or acronym).strip()

        product: Dict[str, Any] = {
            "id": f"{resource_id}.{PRODUCT_SUFFIX}",
            "name": f"{acronym} KGX graph (KG-Bioportal)",
            "category": "GraphProduct",
            "description": (
                f"KGX TSV transform of {source_name} ({acronym}), produced by KG-Bioportal "
                f"from the BioPortal submission. The archive contains {acronym}_nodes.tsv "
                f"and {acronym}_edges.tsv."
            ),
            "product_url": entry.get("download_url"),
            "format": "kgx",
            "compression": "targz",
            "original_source": make_original_source_associations([resource_id]),
        }

        for field, source_field in (("node_count", "nodecount"), ("edge_count", "edgecount")):
            value = entry.get(source_field)
            if isinstance(value, int):
                product[field] = value

        version = str(entry.get("version") or "").strip()
        if version and version != "NA":
            product["latest_version"] = version

        return {key: value for key, value in product.items() if value not in (None, "", [])}

    def merge_product(self, products: List[Any], synced_product: Dict[str, Any]) -> bool:
        """Insert or refresh the KG-Bioportal product in ``products``, in place.

        Curator-added and build-added fields on an existing product are kept;
        only the fields this sync owns are overwritten. Returns whether anything
        changed. The list is mutated rather than rebuilt so the round-trip YAML
        handler keeps the rest of the page's formatting.
        """
        product_id = synced_product["id"]

        for product in products:
            if not isinstance(product, dict) or product.get("id") != product_id:
                continue
            before = copy.deepcopy(dict(product))
            # A new release means a new asset URL, which invalidates any file size
            # the retrieval pass recorded for the old one.
            if product.get("product_url") != synced_product.get("product_url"):
                product.pop("product_file_size", None)
            product.update(synced_product)
            # Managed fields that are absent from this run's product (e.g. a
            # version that became "NA") must not linger from the previous run.
            for field in MANAGED_PRODUCT_FIELDS:
                if field not in synced_product:
                    product.pop(field, None)
            return dict(product) != before

        products.append(synced_product)
        return True

    @staticmethod
    def remove_product(products: List[Any], product_id: str) -> bool:
        """Drop a KG-Bioportal product that no longer has a published artifact."""
        for index, product in enumerate(products):
            if isinstance(product, dict) and product.get("id") == product_id:
                del products[index]
                return True
        return False

    # ----------------------------------------------------------------- output

    @staticmethod
    def _today_iso() -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00:00Z")

    @staticmethod
    def page_style(resource_file: Path) -> str:
        """Detect which YAML sequence style a resource page is written in.

        Resource pages exist in two shapes, roughly half the registry each, and
        the difference is purely how the writer that last touched the page emits
        sequences. ``yaml.safe_dump`` (sync_obo_foundry, propagate_products)
        writes top-level list items flush at column zero; the ruamel handler in
        util/common.py (validate, prettify, populate_infores_ids) indents them.
        This sync adds one product to an otherwise untouched page, so it writes
        back in whichever style it found -- picking either one unconditionally
        would reflow every list on half the pages it visits.

        The tell is the first line under each top-level key that opens a
        sequence. Counting ``- `` lines outright would not work: in the flush
        style, sequences nested inside a list item are themselves indented.
        Some hand-edited pages mix both styles, so the majority wins.
        """
        try:
            text = resource_file.read_text(encoding="utf-8")
        except OSError:
            return "indented"
        if not text.startswith("---"):
            return "indented"
        end = text.find("\n---", 3)
        lines = (text[3:end] if end != -1 else text).splitlines()

        flush = indented = 0
        for index, line in enumerate(lines[:-1]):
            if not re.match(r"^[A-Za-z_][\w-]*:\s*$", line):
                continue
            following = lines[index + 1]
            if following.startswith("- "):
                flush += 1
            elif re.match(r"^ +- ", following):
                indented += 1

        return "flush" if flush > indented else "indented"

    def load_resource(self, resource_file: Path, style: str) -> Any:
        """Load a page with the loader matching how it will be written back."""
        if style == "indented":
            return frontmatter.load(resource_file, handler=self.yaml_handler)
        # safe_dump cannot represent the ruamel handler's CommentedMap, so pages
        # written back with it must be loaded through the plain loader.
        return frontmatter.load(resource_file)

    def write_resource(self, post: Any, resource_file: Path, style: str, dry_run: bool) -> None:
        post.metadata["last_modified_date"] = self._today_iso()
        if dry_run:
            return
        if style == "indented":
            text = dump_frontmatter_text(post, self.yaml_handler) + "\n"
        else:
            yaml_content = yaml.safe_dump(
                dict(post.metadata),
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
            ).strip()
            body = post.content.rstrip()
            text = f"---\n{yaml_content}\n---\n{body}\n" if body else f"---\n{yaml_content}\n---\n"
        resource_file.write_text(text, encoding="utf-8")

    def apply_entry(self, entry: Dict[str, Any], resource_id: str, dry_run: bool) -> str:
        """Write, refresh, or remove one resource's KG-Bioportal product."""
        resource_file = self.resource_file(resource_id)
        style = self.page_style(resource_file)
        post = self.load_resource(resource_file, style)
        metadata = post.metadata
        product_id = f"{resource_id}.{PRODUCT_SUFFIX}"

        if str(entry.get("status", "")).upper() != "OK":
            products = metadata.get("products")
            if not isinstance(products, list) or not self.remove_product(products, product_id):
                return "skipped"
            if not products:
                metadata.pop("products", None)
            logger.info("Removing stale KG-Bioportal product from %s", resource_id)
            self.write_resource(post, resource_file, style, dry_run)
            return "removed"

        if not entry.get("download_url"):
            logger.warning("KG-Bioportal entry %s is OK but has no download URL", entry.get("id"))
            return "skipped"

        if not isinstance(metadata.get("products"), list):
            metadata["products"] = []
        products = metadata["products"]
        was_present = any(
            isinstance(product, dict) and product.get("id") == product_id for product in products
        )
        if not self.merge_product(products, self.build_product(entry, resource_id)):
            return "skipped"

        logger.info(
            "%s KG-Bioportal product on %s", "Updating" if was_present else "Adding", resource_id
        )
        self.write_resource(post, resource_file, style, dry_run)
        return "updated" if was_present else "added"

    def write_report(self, unmatched: List[Dict[str, str]]) -> None:
        """Record entries a curator could resolve through the sync map."""
        self.report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.report_path, "w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, delimiter="\t")
            writer.writerow(["acronym", "kg_bioportal_name", "reason", "suggested_resource"])
            for row in unmatched:
                writer.writerow(
                    [
                        row["acronym"],
                        row["name"],
                        row["reason"],
                        row["suggested_resource"],
                    ]
                )
        logger.info(
            "Wrote %s unmatched KG-Bioportal entries to %s", len(unmatched), self.report_path
        )

    # -------------------------------------------------------------------- run

    def sync_all(self, dry_run: bool = False, limit: Optional[int] = None) -> Dict[str, int]:
        logger.info("Starting KG-Bioportal sync")
        stats = {
            "processed": 0,
            "added": 0,
            "updated": 0,
            "removed": 0,
            "skipped": 0,
            "failed": 0,
            "unmatched": 0,
        }

        manifest = self.fetch_manifest()
        entries = manifest["ontologies"]
        totals = manifest.get("totals") or {}
        if totals:
            logger.info(
                "KG-Bioportal transform of %s: %s ontologies, %s failed, %s skipped",
                totals.get("transform_date", "unknown date"),
                totals.get("totalcount", "?"),
                totals.get("failedcount", "?"),
                totals.get("skippedcount", "?"),
            )
        if limit:
            entries = entries[:limit]

        unmatched: List[Dict[str, str]] = []
        resolutions: List[Tuple[Dict[str, Any], str, str]] = []
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            stats["processed"] += 1
            resource_id, reason = self.resolve_match(entry)
            if resource_id is None:
                # "no_resource" is the overwhelmingly common case -- KG-Bioportal
                # covers all of BioPortal -- and is not worth reporting on.
                if reason in ("name_mismatch", "confirmed_missing"):
                    stats["unmatched"] += 1
                    unmatched.append(
                        {
                            "acronym": str(entry.get("id", "")),
                            "name": str(entry.get("name", "")),
                            "reason": reason,
                            "suggested_resource": self.suggest_resource(entry),
                        }
                    )
                elif reason == "no_resource":
                    suggestion = self.suggest_resource(entry)
                    if suggestion and str(entry.get("status", "")).upper() == "OK":
                        stats["unmatched"] += 1
                        unmatched.append(
                            {
                                "acronym": str(entry.get("id", "")),
                                "name": str(entry.get("name", "")),
                                "reason": reason,
                                "suggested_resource": suggestion,
                            }
                        )
                continue

            resolutions.append((entry, resource_id, reason))

        for entry, resource_id in self.pick_winners(resolutions):
            try:
                stats[self.apply_entry(entry, resource_id, dry_run=dry_run)] += 1
            except Exception as exc:
                logger.error(
                    "Failed to sync KG-Bioportal entry %s to %s: %s",
                    entry.get("id"),
                    resource_id,
                    exc,
                )
                stats["failed"] += 1

        if dry_run or limit:
            # A limited run has only seen part of the manifest; writing the report
            # from it would drop entries the last full run recorded.
            logger.info("Skipping the unmatched report (%s entries found)", len(unmatched))
        else:
            self.write_report(unmatched)

        logger.info("KG-Bioportal sync completed. Stats: %s", stats)
        return stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add KG-Bioportal KGX transform products to KG-Registry resources"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be done without writing files"
    )
    parser.add_argument(
        "--registry-root", type=str, help="Path to resource directory (default: ../resource)"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--limit", type=int, help="Limit number of manifest entries to process (for testing)"
    )
    parser.add_argument(
        "--no-cache", action="store_true", help="Disable cache and fetch fresh data"
    )
    parser.add_argument(
        "--cache-ttl", type=int, default=24, help="Cache time-to-live in hours (default: 24)"
    )

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    cache_ttl = 0 if args.no_cache else args.cache_ttl
    try:
        syncer = KGBioportalSync(registry_root=args.registry_root, cache_ttl_hours=cache_ttl)
        stats = syncer.sync_all(dry_run=args.dry_run, limit=args.limit)

        print("\nSync Summary:")
        print(f"  Processed: {stats['processed']}")
        print(f"  Added: {stats['added']}")
        print(f"  Updated: {stats['updated']}")
        print(f"  Removed: {stats['removed']}")
        print(f"  Skipped (no change): {stats['skipped']}")
        print(f"  Needs curation: {stats['unmatched']}")
        print(f"  Failed: {stats['failed']}")

        if stats["processed"] == 0:
            sys.exit(1)
    except Exception as exc:
        logger.error("KG-Bioportal sync failed: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
