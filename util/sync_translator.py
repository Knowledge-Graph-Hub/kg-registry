#!/usr/bin/env python3
"""
Sync script for NCATS Translator KGX release metadata.

This script updates the ``translator`` resource page based on the Translator
release summary feed and per-release ``graph-metadata.json`` documents hosted at
https://kgx-storage.rtx.ai/releases/.
"""

from __future__ import annotations

import argparse
import copy
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import frontmatter  # type: ignore
import yaml


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class TranslatorSync:
    """Synchronize Translator release products with the ``translator`` resource page."""

    SUMMARY_URL = "https://kgx-storage.rtx.ai/releases/latest-release-summary.json"
    RELEASES_BASE_URL = "https://kgx-storage.rtx.ai/releases"

    SOURCE_ID_OVERRIDES = {
        "dakp": "drug-approvals-kp",
        "drug_rep_hub": "drugrephub",
        "go_cam": "go-cam",
        "hpoa": "hp",
        "icees": "icees-kg",
        "ncbi_gene": "ncbigene",
        "tmkp": "text-mining-kp",
    }

    NAME_OVERRIDES = {
        "bindingdb": "Translator BindingDB KGX Graph",
        "drugcentral": "Translator DrugCentral KGX Graph",
        "pathbank": "Translator PathBank KGX Graph",
        "translator_kg": "Translator Aggregate KGX Graph",
    }

    LABEL_OVERRIDES = {
        "bindingdb": "BindingDB",
        "ctd": "CTD",
        "ctkp": "CTKP",
        "dakp": "Drug Approvals KP",
        "dgidb": "DGIdb",
        "diseases": "DISEASES",
        "drug_rep_hub": "Drug Repurposing Hub",
        "gene2phenotype": "Gene2Phenotype",
        "geneticskp": "Genetics KP",
        "go_cam": "GO-CAM",
        "goa": "GOA",
        "gtopdb": "GToPdb",
        "hpoa": "HPOA",
        "icees": "ICEES",
        "intact": "IntAct",
        "panther": "PANTHER",
        "semmeddb": "SemMedDB",
        "sider": "SIDER",
        "signor": "SIGNOR",
        "tmkp": "TMKP",
        "ttd": "TTD",
        "translator_kg": "Translator aggregate graph",
    }

    LICENSE_OVERRIDES = {
        "MIT": {
            "id": "https://opensource.org/license/mit/",
            "label": "MIT",
        }
    }

    def __init__(self, registry_root: Optional[str] = None, cache_ttl_hours: int = 24):
        script_dir = Path(__file__).resolve().parent
        self.registry_root = (
            Path(registry_root)
            if registry_root is not None
            else script_dir.parent / "resource"
        )
        self.resource_file = self.registry_root / "translator" / "translator.md"
        self.cache_ttl_hours = cache_ttl_hours
        self.cache_dir = script_dir.parent / "cache"
        self.cache_file = self.cache_dir / "translator_release_cache.json"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.existing_resources = self._load_existing_resources()
        self.resource_names = self._load_resource_names()

    def _today_iso(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00:00Z")

    def _load_existing_resources(self) -> Dict[str, Path]:
        resources: Dict[str, Path] = {}
        if not self.registry_root.exists():
            return resources

        for resource_dir in self.registry_root.iterdir():
            if not resource_dir.is_dir():
                continue
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if resource_file.exists():
                resources[resource_dir.name] = resource_file
        return resources

    def _load_resource_names(self) -> Dict[str, str]:
        names: Dict[str, str] = {}
        for resource_id, resource_path in self.existing_resources.items():
            try:
                metadata = frontmatter.load(resource_path).metadata
            except Exception as exc:
                logger.debug("Failed to load resource name from %s: %s", resource_path, exc)
                continue
            name = metadata.get("name")
            if isinstance(name, str) and name.strip():
                names[resource_id] = name.strip()
        return names

    def _is_cache_valid(self) -> bool:
        if not self.cache_file.exists():
            return False

        cache_age_hours = (time.time() - os.path.getmtime(self.cache_file)) / 3600
        is_valid = cache_age_hours < self.cache_ttl_hours
        if is_valid:
            logger.info(
                "Translator cache is valid (age: %.1f hours, TTL: %s hours)",
                cache_age_hours,
                self.cache_ttl_hours,
            )
        else:
            logger.info(
                "Translator cache expired (age: %.1f hours, TTL: %s hours)",
                cache_age_hours,
                self.cache_ttl_hours,
            )
        return is_valid

    def _load_from_cache(self) -> Optional[List[Dict[str, Any]]]:
        try:
            data = json.loads(self.cache_file.read_text(encoding="utf-8"))
        except Exception as exc:
            logger.warning("Failed to load Translator cache: %s", exc)
            return None

        if isinstance(data, list):
            logger.info("Loaded %s Translator release entries from cache", len(data))
            return data
        return None

    def _save_to_cache(self, data: List[Dict[str, Any]]) -> None:
        try:
            self.cache_file.write_text(json.dumps(
                data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            logger.info("Cached %s Translator release entries to %s", len(data), self.cache_file)
        except Exception as exc:
            logger.warning("Failed to save Translator cache: %s", exc)

    def _fetch_json(self, url: str) -> Any:
        with urlopen(url, timeout=30) as response:  # noqa: S310
            return json.loads(response.read().decode("utf-8"))

    def fetch_translator_data(self) -> List[Dict[str, Any]]:
        if self._is_cache_valid():
            cached_data = self._load_from_cache()
            if cached_data is not None:
                return cached_data

        logger.info("Fetching fresh Translator release data from %s", self.SUMMARY_URL)
        try:
            summary = self._fetch_json(self.SUMMARY_URL)
            if not isinstance(summary, dict):
                raise ValueError("Expected Translator release summary JSON object")

            records: List[Dict[str, Any]] = []
            for release_key in sorted(summary):
                release_summary = summary[release_key]
                if not isinstance(release_summary, dict):
                    raise ValueError(f"Expected dict for Translator release {release_key}")
                metadata_url = (
                    f"{self.RELEASES_BASE_URL}/{release_key}/latest/graph-metadata.json"
                )
                records.append(
                    {
                        "release_key": release_key,
                        "summary": release_summary,
                        "graph_metadata": self._fetch_json(metadata_url),
                    }
                )

            self._save_to_cache(records)
            logger.info("Successfully fetched %s Translator release entries", len(records))
            return records
        except (HTTPError, URLError, ValueError, json.JSONDecodeError) as exc:
            logger.error("Failed to fetch Translator release data: %s", exc)
            if self.cache_file.exists():
                logger.warning("Attempting to use expired Translator cache as fallback")
                cached_data = self._load_from_cache()
                if cached_data is not None:
                    return cached_data
            raise

    def _map_source_id(self, source_id: str) -> str:
        return self.SOURCE_ID_OVERRIDES.get(source_id, source_id)

    def _label_for_release_key(self, release_key: str, mapped_resource_id: Optional[str] = None) -> str:
        if release_key in self.LABEL_OVERRIDES:
            return self.LABEL_OVERRIDES[release_key]

        if mapped_resource_id and mapped_resource_id in self.resource_names:
            return self.resource_names[mapped_resource_id]

        parts = release_key.replace("_", " ").replace("-", " ").split()
        return " ".join(part.upper() if len(part) <= 4 else part.capitalize() for part in parts)

    def _product_name(
        self,
        release_key: str,
        mapped_resource_id: Optional[str],
        existing_name: Optional[str],
    ) -> str:
        if existing_name:
            return existing_name
        if release_key in self.NAME_OVERRIDES:
            return self.NAME_OVERRIDES[release_key]
        return f"Translator {self._label_for_release_key(release_key, mapped_resource_id)} KGX Graph"

    def _description_for_product(
        self,
        release_key: str,
        summary: Dict[str, Any],
        graph_metadata: Dict[str, Any],
        mapped_sources: List[str],
    ) -> str:
        release_version = summary.get("release_version")
        build_version = summary.get("build_version") or graph_metadata.get("version")
        source_version = summary.get("source_version")
        biolink_version = summary.get("biolink_version") or graph_metadata.get("biolinkVersion")
        node_norm_version = summary.get("node_norm_version") or graph_metadata.get("babelVersion")

        detail_bits = []
        if release_version:
            detail_bits.append(f"release {release_version}")
        if build_version:
            detail_bits.append(f"build {build_version}")
        if source_version:
            detail_bits.append(f"source version {source_version}")
        if biolink_version:
            detail_bits.append(f"Biolink {biolink_version}")
        if node_norm_version:
            detail_bits.append(f"Node Normalizer {node_norm_version}")
        detail_text = "; ".join(detail_bits)

        if release_key == "translator_kg":
            return (
                "Aggregated KGX JSONL graph package combining "
                f"{len(mapped_sources)} Translator release sources"
                + (f" ({detail_text})." if detail_text else ".")
            )

        label = self._label_for_release_key(
            release_key, mapped_sources[0] if mapped_sources else None)
        return (
            f"KGX JSONL graph package for {label} distributed via the NCATS Translator release site"
            + (f" ({detail_text})." if detail_text else ".")
        )

    def _versions_for_product(
        self,
        summary: Dict[str, Any],
        graph_metadata: Dict[str, Any],
    ) -> Tuple[Optional[str], List[str]]:
        latest_version = summary.get("release_version")
        versions: List[str] = []
        for value in [
            summary.get("release_version"),
            summary.get("build_version"),
            graph_metadata.get("version"),
        ]:
            if not isinstance(value, str) or not value.strip():
                continue
            if value not in versions:
                versions.append(value)
        return latest_version, versions

    def _license_for_product(self, graph_metadata: Dict[str, Any]) -> Optional[Dict[str, str]]:
        license_value = graph_metadata.get("license")
        if isinstance(license_value, str) and license_value in self.LICENSE_OVERRIDES:
            return copy.deepcopy(self.LICENSE_OVERRIDES[license_value])
        return None

    def _compatibility_for_product(self, summary: Dict[str, Any], graph_metadata: Dict[str, Any]) -> List[Dict[str, str]]:
        biolink_version = summary.get("biolink_version") or graph_metadata.get("biolinkVersion")
        if isinstance(biolink_version, str) and biolink_version.strip():
            return [{"standard": "biolink", "version": biolink_version}]
        return []

    def _mapped_original_sources(self, release_key: str, graph_metadata: Dict[str, Any]) -> List[str]:
        mapped_sources: List[str] = []
        for source in graph_metadata.get("isBasedOn", []) or []:
            if not isinstance(source, dict):
                continue
            source_id = source.get("id")
            if not isinstance(source_id, str) or not source_id.strip():
                continue
            mapped_source = self._map_source_id(source_id.strip())
            if mapped_source not in mapped_sources:
                mapped_sources.append(mapped_source)

        if mapped_sources:
            return mapped_sources

        mapped_release_key = self._map_source_id(release_key)
        return [mapped_release_key]

    def _existing_translator_product_names(self, metadata: Dict[str, Any]) -> Dict[str, str]:
        names: Dict[str, str] = {}
        for product in metadata.get("products", []) or []:
            if not isinstance(product, dict):
                continue
            product_id = product.get("id")
            name = product.get("name")
            if isinstance(product_id, str) and isinstance(name, str) and product_id.startswith("translator."):
                names[product_id] = name
        return names

    def build_product(
        self,
        release_key: str,
        summary: Dict[str, Any],
        graph_metadata: Dict[str, Any],
        existing_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        mapped_sources = self._mapped_original_sources(release_key, graph_metadata)
        mapped_primary_source = mapped_sources[0] if mapped_sources else None
        product_id = f"translator.{release_key}.graph"
        latest_version, versions = self._versions_for_product(summary, graph_metadata)
        schema = graph_metadata.get("schema") or {}

        product: Dict[str, Any] = {
            "category": "GraphProduct",
            "description": self._description_for_product(
                release_key=release_key,
                summary=summary,
                graph_metadata=graph_metadata,
                mapped_sources=mapped_sources,
            ),
            "format": "kgx-jsonl",
            "id": product_id,
            "name": self._product_name(
                release_key=release_key,
                mapped_resource_id=mapped_primary_source,
                existing_name=existing_name,
            ),
            "original_source": mapped_sources,
            "product_url": f"{self.RELEASES_BASE_URL}/{release_key}/latest/",
            "secondary_source": ["translator"],
        }

        if isinstance(latest_version, str) and latest_version.strip():
            product["latest_version"] = latest_version
        if versions:
            product["versions"] = versions

        node_count = (schema.get("nodes_summary") or {}).get("total_count")
        if isinstance(node_count, int):
            product["node_count"] = node_count

        edge_count = (schema.get("edges_summary") or {}).get("total_count")
        if isinstance(edge_count, int):
            product["edge_count"] = edge_count

        compatibility = self._compatibility_for_product(summary, graph_metadata)
        if compatibility:
            product["compatibility"] = compatibility

        license_obj = self._license_for_product(graph_metadata)
        if license_obj:
            product["license"] = license_obj

        return product

    def build_products(
        self,
        records: List[Dict[str, Any]],
        existing_metadata: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        existing_names = self._existing_translator_product_names(existing_metadata)
        products = []
        for record in records:
            release_key = record["release_key"]
            products.append(
                self.build_product(
                    release_key=release_key,
                    summary=record["summary"],
                    graph_metadata=record["graph_metadata"],
                    existing_name=existing_names.get(f"translator.{release_key}.graph"),
                )
            )
        return products

    def _load_existing_post(self) -> Tuple[Dict[str, Any], str]:
        if not self.resource_file.exists():
            return {}, ""
        post = frontmatter.load(self.resource_file)
        metadata = dict(post.metadata) if isinstance(post.metadata, dict) else {}
        return metadata, post.content

    def _metadata_for_compare(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        comparable = copy.deepcopy(metadata)
        comparable.pop("last_modified_date", None)
        return comparable

    def _content_for_compare(self, content: str) -> str:
        return content.strip()

    def _serialize_resource(self, metadata: Dict[str, Any], content: str) -> str:
        yaml_content = yaml.safe_dump(
            metadata,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
        ).strip()
        body = content.rstrip()
        if body:
            return f"---\n{yaml_content}\n---\n{body}\n"
        return f"---\n{yaml_content}\n---\n"

    def sync(self, dry_run: bool = False) -> str:
        existing_metadata, existing_content = self._load_existing_post()
        if not existing_metadata:
            raise FileNotFoundError(f"Translator resource file not found: {self.resource_file}")

        records = self.fetch_translator_data()
        merged_metadata = copy.deepcopy(existing_metadata)
        merged_metadata["description"] = (
            "Aggregated, transformed graph datasets distributed by the NCATS Translator "
            "program via the Translator KGX release site. Each package provides a KGX "
            "graph built from an upstream source and normalized with Translator pipelines."
        )
        merged_metadata["homepage_url"] = f"{self.RELEASES_BASE_URL}/"
        merged_metadata["products"] = self.build_products(records, existing_metadata)

        today_iso = self._today_iso()
        if existing_metadata.get("creation_date"):
            merged_metadata["creation_date"] = existing_metadata["creation_date"]
        else:
            merged_metadata["creation_date"] = today_iso

        has_changed = self._metadata_for_compare(existing_metadata) != self._metadata_for_compare(
            merged_metadata
        )

        if not has_changed:
            logger.info("No Translator changes detected")
            return "skipped"

        merged_metadata["last_modified_date"] = today_iso
        if dry_run:
            logger.info("[DRY RUN] Would update resource: translator")
            return "updated"

        self.resource_file.write_text(
            self._serialize_resource(merged_metadata, existing_content),
            encoding="utf-8",
        )
        logger.info("Updated resource: translator")
        return "updated"


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync Translator release metadata to KG-Registry")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without writing files",
    )
    parser.add_argument(
        "--registry-root",
        type=str,
        help="Path to resource directory (default: ../resource)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable cache and fetch fresh data",
    )
    parser.add_argument(
        "--cache-ttl",
        type=int,
        default=24,
        help="Cache time-to-live in hours (default: 24)",
    )

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    cache_ttl = 0 if args.no_cache else args.cache_ttl
    try:
        syncer = TranslatorSync(registry_root=args.registry_root, cache_ttl_hours=cache_ttl)
        status = syncer.sync(dry_run=args.dry_run)

        print("\nSync Summary:")
        print("  Processed: 1")
        print(f"  Updated: {1 if status == 'updated' else 0}")
        print(f"  Skipped: {1 if status == 'skipped' else 0}")
    except Exception as exc:
        logger.error("Translator sync failed: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
