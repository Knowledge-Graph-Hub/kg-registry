#!/usr/bin/env python3
"""Infer licenses for aggregate resources from their upstream sources.

A KnowledgeGraph or Aggregator that declares no license of its own is, by
default, bound by the licenses of whatever it was built from. This module
reads the provenance already recorded on a resource's products
(``original_source`` and ``secondary_source`` associations) and on the
``components`` field, resolves each upstream source to a license, and picks
the most restrictive one. The result is written to the resource's
``license`` field with ``status: inferred``. A provided license is never
overwritten.

Restrictiveness is a coarse ladder, least to most restrictive:

    public domain < permissive < copyleft < non-commercial
                  < no derivatives < custom

``custom`` covers any license that could not be placed on the ladder: bespoke
terms of use, subscriptions, controlled access, and "varies". It sits at the
top because a consumer must read those terms before reuse, so it is the
tier that most constrains what can be said about the aggregate.

Only provenance relations that mean "this content came from there" count:
``prov:hadPrimarySource``, ``prov:wasDerivedFrom``, and ``prov:used``.
``prov:wasInfluencedBy`` and ``prov:wasInformedBy`` do not carry content and
are ignored.

Usage (from the repository root)::

    uv run python util/infer_licenses.py --dry-run
    uv run python util/infer_licenses.py --report reports/license-inference.tsv

The build (``extract-metadata.py concat``) calls ``apply_inferred_licenses``
directly, so a normal ``make`` run keeps the field current.
"""

from __future__ import annotations

import csv
import pathlib
import re
from collections import Counter
from copy import deepcopy
from typing import Any, Iterable, Mapping, Optional

try:
    from util.source_associations import (
        resource_owns_product,
        source_association_id,
        source_association_relation,
        source_resource_id,
    )
except ImportError:  # pragma: no cover - fallback for direct script execution
    from source_associations import (  # type: ignore
        resource_owns_product,
        source_association_id,
        source_association_relation,
        source_resource_id,
    )

__all__ = [
    "TIERS",
    "TIER_RANK",
    "INHERITING_CATEGORIES",
    "CONTENT_RELATIONS",
    "STATUS_PROVIDED",
    "STATUS_INFERRED",
    "classify_license",
    "has_declared_license",
    "is_inferred_license",
    "most_restrictive",
    "upstream_sources",
    "LicenseIndex",
    "infer_license",
    "apply_inferred_licenses",
    "LicenseWriteRefused",
    "write_report",
]

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent
RESOURCE_DIR = ROOT / "resource"

#: Least to most restrictive. Position is rank.
TIERS: tuple[str, ...] = (
    "public domain",
    "permissive",
    "copyleft",
    "non-commercial",
    "no derivatives",
    "custom",
)
TIER_RANK: dict[str, int] = {tier: rank for rank, tier in enumerate(TIERS)}

#: Values of the license ``status`` field.
STATUS_PROVIDED = "provided"
STATUS_INFERRED = "inferred"

#: Resource categories whose license defaults to their sources' licenses.
INHERITING_CATEGORIES: frozenset[str] = frozenset({"KnowledgeGraph", "Aggregator"})

#: Provenance relations through which a license propagates.
CONTENT_RELATIONS: frozenset[str] = frozenset(
    {"prov:hadPrimarySource", "prov:wasDerivedFrom", "prov:used"}
)

#: The default relation for each source field, mirroring source_associations.
_DEFAULT_RELATION = {
    "original_source": "prov:hadPrimarySource",
    "secondary_source": "prov:wasInfluencedBy",
}

# URL fragments checked in order. First match wins, so the more specific
# Creative Commons variants come before the plain attribution form.
_URL_TIERS: tuple[tuple[str, str], ...] = (
    ("creativecommons.org/publicdomain/zero", "public domain"),
    ("creativecommons.org.publicdomain/zero", "public domain"),  # typo seen in data
    ("creativecommons.org/public-domain/pdm", "public domain"),
    ("creativecommons.org/publicdomain/mark", "public domain"),
    ("creativecommons.org/share-your-work/public-domain/cc0", "public domain"),
    ("spdx.org/licenses/cc0", "public domain"),
    ("spdx.org/licenses/cc-pddc", "public domain"),
    ("usa.gov/government-works", "public domain"),
    ("creativecommons.org/licenses/by-nc-nd", "no derivatives"),
    ("creativecommons.org/licenses/by-nd", "no derivatives"),
    ("spdx.org/licenses/cc-by-nc-nd", "no derivatives"),
    ("spdx.org/licenses/cc-by-nd", "no derivatives"),
    ("creativecommons.org/licenses/by-nc", "non-commercial"),
    ("spdx.org/licenses/cc-by-nc", "non-commercial"),
    ("polyformproject.org/licenses/noncommercial", "non-commercial"),
    ("creativecommons.org/licenses/by-sa", "copyleft"),
    ("spdx.org/licenses/cc-by-sa", "copyleft"),
    ("opendatacommons.org/licenses/odbl", "copyleft"),
    ("spdx.org/licenses/odbl", "copyleft"),
    ("gnu.org/licenses/", "copyleft"),
    ("opensource.org/license/gpl", "copyleft"),
    ("opensource.org/licenses/gpl", "copyleft"),
    ("opensource.org/license/lgpl", "copyleft"),
    ("opensource.org/licenses/lgpl", "copyleft"),
    ("opensource.org/license/agpl", "copyleft"),
    ("opensource.org/licenses/agpl", "copyleft"),
    ("spdx.org/licenses/gpl", "copyleft"),
    ("spdx.org/licenses/lgpl", "copyleft"),
    ("spdx.org/licenses/agpl", "copyleft"),
    ("creativecommons.org/licenses/by/", "permissive"),
    ("spdx.org/licenses/cc-by-", "permissive"),
    ("opendatacommons.org/licenses/by", "permissive"),
    ("opendatacommons.org/licenses/pddl", "public domain"),
    ("opensource.org/license/mit", "permissive"),
    ("opensource.org/licenses/mit", "permissive"),
    ("spdx.org/licenses/mit", "permissive"),
    ("opensource.org/license/bsd", "permissive"),
    ("opensource.org/licenses/bsd", "permissive"),
    ("spdx.org/licenses/bsd", "permissive"),
    ("apache.org/licenses/", "permissive"),
    ("opensource.org/licenses/apache", "permissive"),
    ("spdx.org/licenses/apache", "permissive"),
    ("opensource.org/licenses/artistic", "permissive"),
    ("spdx.org/licenses/artistic", "permissive"),
    ("w3.org/consortium/legal/2015/copyright-software", "permissive"),
    ("wtfpl.net", "permissive"),
)

# Label patterns, checked in order when the URL is absent or unrecognized.
# A label naming several licenses ("CC0 and CC BY-NC (mixed)") lands on the
# most restrictive one it names, which is the reading a consumer needs.
_LABEL_TIERS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(
            r"\bby[\s-]*nc[\s-]*nd\b|\bby[\s-]*nd\b|no[\s-]*derivative"
            r"|no[\s-]*modification|not be (?:altered|modified)|may not be altered|unaltered",
            re.I,
        ),
        "no derivatives",
    ),
    (
        re.compile(
            r"\bby[\s-]*nc\b|\bnon[\s-]*commercial\b|\bnoncommercial\b|\bacademic\b"
            r"|\bnon[\s-]*profit\b|\bnonprofit\b|research\s*(?:and|or|/)\s*educational",
            re.I,
        ),
        "non-commercial",
    ),
    (
        re.compile(r"\bby[\s-]*sa\b|\bodbl\b|\bshare[\s-]*alike\b|\b[al]?gpl(?:v?\d)?\b", re.I),
        "copyleft",
    ),
    (
        re.compile(
            r"\bcc[\s-]*by\b|\bcc\s+by\b|\bmit\b|\bapache\b|\bbsd\b|\bartistic\b"
            r"|\bodc[\s-]*by\b|\bopen data license\b|\battribution\b"
            r"|freely (?:available|provided)",
            re.I,
        ),
        "permissive",
    ),
    (
        re.compile(
            r"\bcc0\b|\bcc[\s-]*zero\b|\bpublic[\s-]*domain\b|\bgovernment work\b"
            r"|\bpublic records\b|\bno copyright\b",
            re.I,
        ),
        "public domain",
    ),
)

# "non-commercial and commercial" (either order) describes a grant to every
# kind of user, not a restriction. It is stripped before the non-commercial
# pattern can see it, and on its own it reads as permissive.
_NC_AND_COMMERCIAL = re.compile(
    r"non[\s-]*commercial\s+(?:and|or)\s+commercial(?:\s+(?:use|purposes?))?"
    r"|commercial\s+(?:and|or)\s+non[\s-]*commercial(?:\s+(?:use|purposes?))?",
    re.I,
)

#: Labels that mean "no license recorded" even though the field is present.
_PLACEHOLDER_LABELS = re.compile(r"^\s*(not specified|unspecified|unknown|none|n/?a|tbd)\s*$", re.I)


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------


def _license_url(license_obj: Any) -> str:
    if isinstance(license_obj, str):
        return license_obj.strip()
    if isinstance(license_obj, Mapping):
        for key in ("id", "url"):
            value = license_obj.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def _license_label(license_obj: Any) -> str:
    if isinstance(license_obj, Mapping):
        value = license_obj.get("label")
        if isinstance(value, str):
            return value.strip()
    return ""


def is_inferred_license(license_obj: Any) -> bool:
    """Return True if the license field was filled in by inference."""
    if not isinstance(license_obj, Mapping):
        return False
    return str(license_obj.get("status") or "").strip().lower() == STATUS_INFERRED


def has_declared_license(license_obj: Any) -> bool:
    """Return True if the license field carries a license the resource provided.

    An inferred license does not count. Neither does an empty mapping, or
    one whose only content is a placeholder label such as "Not specified".
    """
    if is_inferred_license(license_obj):
        return False
    url = _license_url(license_obj)
    if url:
        return True
    label = _license_label(license_obj)
    return bool(label) and not _PLACEHOLDER_LABELS.match(label)


def normalize_license_url(url: str) -> str:
    """Canonical form of a license URL for matching and counting."""
    value = url.strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = re.sub(r"^www\.", "", value)
    value = re.sub(r"/(legalcode|deed(\.[a-z]{2})?)$", "", value)
    return value.rstrip("/")


def classify_license(license_obj: Any) -> Optional[str]:
    """Place a license on the restrictiveness ladder.

    Returns one of ``TIERS``, or None when the field carries no license.
    A license that carries a URL or label but matches nothing known is
    ``custom``.
    """
    if not has_declared_license(license_obj):
        return None
    url_tier = _classify_url(_license_url(license_obj))
    label_tier = _classify_label(_license_label(license_obj))
    # A label is curator commentary on the URL. It can add a restriction the
    # URL does not show ("CC0 and CC BY-NC (mixed)" on a CC0 page) but it
    # cannot loosen one, so the more restrictive of the two wins. A label
    # that matches nothing is not a vote.
    if url_tier is not None and label_tier is not None:
        return most_restrictive([url_tier, label_tier])
    if url_tier is not None:
        return url_tier
    if label_tier is not None:
        return label_tier
    return "custom"


def _classify_url(url: str) -> Optional[str]:
    url = normalize_license_url(url)
    if not url:
        return None
    # The normalized URL has no trailing slash, so match fragments without
    # one too. Order in _URL_TIERS keeps "licenses/by" from claiming the
    # by-nc, by-nd, and by-sa forms, which are listed before it.
    for fragment, tier in _URL_TIERS:
        if fragment.rstrip("/") in url:
            return tier
    return None


def _classify_label(label: str) -> Optional[str]:
    stripped, grants_both = _NC_AND_COMMERCIAL.subn("", label)
    if not stripped and not grants_both:
        return None
    for pattern, tier in _LABEL_TIERS:
        if pattern.search(stripped):
            return tier
    return "permissive" if grants_both else None


def most_restrictive(tiers: Iterable[Optional[str]]) -> Optional[str]:
    """Return the highest-ranked tier among those given, ignoring None."""
    best: Optional[str] = None
    for tier in tiers:
        if tier is None:
            continue
        if best is None or TIER_RANK[tier] > TIER_RANK[best]:
            best = tier
    return best


# ---------------------------------------------------------------------------
# Upstream discovery
# ---------------------------------------------------------------------------


def upstream_sources(resource: Mapping[str, Any]) -> list[str]:
    """Return the source IDs whose content flows into this resource.

    Sources come from the resource's ``components`` and from the
    ``original_source``/``secondary_source`` associations on products the
    resource owns. Only ``CONTENT_RELATIONS`` count. The resource itself and
    anything it owns are excluded. Order is first-seen, without duplicates.
    """
    resource_id = str(resource.get("id") or "").strip()
    found: list[str] = []
    seen: set[str] = set()

    def _add(source_id: Optional[str]) -> None:
        if not source_id:
            return
        source_id = source_id.strip()
        if not source_id or source_id in seen:
            return
        if source_resource_id(source_id) == resource_id:
            return
        seen.add(source_id)
        found.append(source_id)

    components = resource.get("components")
    if isinstance(components, str):
        components = [components]
    if isinstance(components, list):
        for component in components:
            if isinstance(component, str):
                _add(component)
            elif isinstance(component, Mapping):
                _add(component.get("id"))

    products = resource.get("products")
    if not isinstance(products, list):
        return found
    for product in products:
        if not isinstance(product, Mapping):
            continue
        product_id = product.get("id")
        # Products propagated from elsewhere list this resource as a source.
        # Their provenance describes the other resource, not this one.
        if isinstance(product_id, str) and "." in product_id:
            if not resource_owns_product(resource_id, product_id):
                continue
        for field_name, default_relation in _DEFAULT_RELATION.items():
            associations = product.get(field_name)
            if associations is None:
                continue
            if not isinstance(associations, list):
                associations = [associations]
            for association in associations:
                relation = source_association_relation(association, default_relation)
                if relation not in CONTENT_RELATIONS:
                    continue
                _add(source_association_id(association))
    return found


# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------


class LicenseIndex:
    """Lookup of resources and their owned products, with memoized inference."""

    def __init__(self, resources: Iterable[Mapping[str, Any]]):
        self.resources: dict[str, Mapping[str, Any]] = {}
        self.products: dict[str, Mapping[str, Any]] = {}
        for resource in resources:
            resource_id = resource.get("id")
            if not isinstance(resource_id, str) or not resource_id.strip():
                continue
            resource_id = resource_id.strip()
            self.resources[resource_id] = resource
            products = resource.get("products")
            if not isinstance(products, list):
                continue
            for product in products:
                if not isinstance(product, Mapping):
                    continue
                product_id = product.get("id")
                if isinstance(product_id, str) and resource_owns_product(resource_id, product_id):
                    self.products.setdefault(product_id.strip(), product)
        self._inferred: dict[str, Optional[dict[str, Any]]] = {}

    # -- single-source resolution ------------------------------------------

    def resolve_source(
        self, source_id: str, visiting: frozenset[str]
    ) -> tuple[Optional[Any], Optional[str]]:
        """Return (license_obj, tier) for a source ID, or (None, None).

        Resolution order: the product's own license, the owning resource's
        declared license, the most restrictive license among the resource's
        owned products, and finally the resource's own inferred license.
        ``visiting`` guards against cycles in the provenance graph.
        """
        resource_id = source_resource_id(source_id)
        if source_id != resource_id:
            product = self.products.get(source_id)
            if product is not None:
                tier = classify_license(product.get("license"))
                if tier is not None:
                    return product.get("license"), tier
        resource = self.resources.get(resource_id)
        if resource is None:
            return None, None
        tier = classify_license(resource.get("license"))
        if tier is not None:
            return resource.get("license"), tier

        best_license, best_tier = None, None
        products = resource.get("products")
        if isinstance(products, list):
            for product in products:
                if not isinstance(product, Mapping):
                    continue
                product_id = product.get("id")
                if not (
                    isinstance(product_id, str) and resource_owns_product(resource_id, product_id)
                ):
                    continue
                tier = classify_license(product.get("license"))
                if tier is not None and (
                    best_tier is None or TIER_RANK[tier] > TIER_RANK[best_tier]
                ):
                    best_license, best_tier = product.get("license"), tier
        if best_tier is not None:
            return best_license, best_tier

        if resource_id in visiting:
            return None, None
        inferred = self._infer(resource, visiting)
        if inferred is not None:
            return {"id": inferred["id"], "label": inferred["label"]}, inferred["restrictiveness"]
        return None, None

    # -- whole-resource inference ------------------------------------------

    def _infer(
        self, resource: Mapping[str, Any], visiting: frozenset[str]
    ) -> Optional[dict[str, Any]]:
        resource_id = str(resource.get("id") or "").strip()
        if resource_id in self._inferred:
            return self._inferred[resource_id]
        visiting = visiting | {resource_id}

        resolved: list[tuple[str, Any, str]] = []
        unresolved: list[str] = []
        for source_id in upstream_sources(resource):
            license_obj, tier = self.resolve_source(source_id, visiting)
            if tier is None:
                unresolved.append(source_id)
            else:
                resolved.append((source_id, license_obj, tier))

        if not resolved:
            result = None
        else:
            top = most_restrictive(tier for _, _, tier in resolved)
            assert top is not None
            winners = [(sid, lic) for sid, lic, tier in resolved if tier == top]
            chosen_url, chosen_label = _choose_license(lic for _, lic in winners)
            result = {
                "id": chosen_url,
                "label": chosen_label,
                "status": STATUS_INFERRED,
                "restrictiveness": top,
                "inferred_from": sorted(sid for sid, _ in winners),
                "unresolved_sources": sorted(unresolved),
            }
        # Memoize only complete answers: a cycle-truncated walk may have
        # skipped sources that a later, differently-rooted walk can reach.
        if not (visiting - {resource_id}):
            self._inferred[resource_id] = result
        return result

    def infer(self, resource: Mapping[str, Any]) -> Optional[dict[str, Any]]:
        """Infer a license for a resource from its upstream sources.

        Returns a mapping with ``id``, ``label``, ``status``, ``restrictiveness``,
        ``inferred_from`` (the sources at the winning tier) and
        ``unresolved_sources`` (sources with no license anywhere), or None
        when no upstream license could be found at all.
        """
        return self._infer(resource, frozenset())


def _choose_license(licenses: Iterable[Any]) -> tuple[str, str]:
    """Pick one representative URL and label from the winning licenses.

    Prefer a license that has a URL. Among those, take the most common
    canonical URL, ties broken alphabetically, and its most common label.
    """
    by_url: dict[str, Counter[str]] = {}
    original_url: dict[str, str] = {}
    label_only: Counter[str] = Counter()
    for license_obj in licenses:
        url = _license_url(license_obj)
        label = _license_label(license_obj)
        if url:
            key = normalize_license_url(url)
            by_url.setdefault(key, Counter())[label] += 1
            original_url.setdefault(key, url)
        elif label:
            label_only[label] += 1
    if by_url:
        key = sorted(by_url, key=lambda k: (-sum(by_url[k].values()), k))[0]
        labels = by_url[key]
        label = sorted(labels, key=lambda lab: (-labels[lab], lab == "", lab))[0]
        return original_url[key], label
    if label_only:
        return "", sorted(label_only, key=lambda lab: (-label_only[lab], lab))[0]
    return "", ""


def infer_license(
    resource: Mapping[str, Any], resources: Iterable[Mapping[str, Any]]
) -> Optional[dict[str, Any]]:
    """Convenience wrapper: build an index and infer for one resource."""
    return LicenseIndex(resources).infer(resource)


# ---------------------------------------------------------------------------
# Application to the registry
# ---------------------------------------------------------------------------


def _is_inheriting(resource: Mapping[str, Any]) -> bool:
    return str(resource.get("category") or "").strip() in INHERITING_CATEGORIES


def apply_inferred_licenses(
    objs: list[dict[str, Any]],
    *,
    write: bool = True,
    resource_dir: pathlib.Path = RESOURCE_DIR,
    only_ids: Optional[Iterable[str]] = None,
) -> dict[str, Any]:
    """Fill in ``license`` on every inheriting resource that provides none.

    Mutates ``objs`` in place. The value written carries ``status: inferred``
    and names the sources it came from. A provided license is never touched.
    A placeholder license block (present, but empty or "Not specified") is
    left alone as well, and reported as ``placeholder``. When ``write`` is
    true, resource pages whose inferred license changed are rewritten. A
    resource that has since gained a provided license simply keeps it; the
    inferred block is gone because the curator replaced it.

    A page that cannot take the block (missing, no front matter, or a
    ``license`` the writer must not touch) is reported under ``refused`` with
    a warning, and the inferred license is dropped from the object so the
    registry export never shows a license the page does not carry.

    Returns a summary with ``inferred``, ``removed``, ``unresolved`` (IDs that
    inherit but resolved nothing), ``placeholder``, ``written``, ``refused``
    and a ``rows`` list suitable for :func:`write_report`.
    """
    index = LicenseIndex(objs)
    wanted = set(only_ids) if only_ids is not None else None
    summary: dict[str, Any] = {
        "inferred": [],
        "removed": [],
        "unresolved": [],
        "placeholder": [],
        "written": [],
        "refused": [],
        "rows": [],
    }

    for obj in objs:
        resource_id = obj.get("id")
        if not isinstance(resource_id, str) or not resource_id.strip():
            continue
        if wanted is not None and resource_id not in wanted:
            continue
        if not _is_inheriting(obj):
            continue

        current = obj.get("license")
        declared = has_declared_license(current)
        previous = _plain(current) if is_inferred_license(current) else None
        placeholder = (
            isinstance(current, Mapping) and bool(current) and not declared and previous is None
        )
        inferred = index.infer(obj)
        summary["rows"].append(_report_row(obj, declared, inferred, placeholder))

        if declared or placeholder:
            if placeholder:
                summary["placeholder"].append(resource_id)
            continue

        if inferred is None:
            if "license" in obj:
                del obj["license"]
            if previous is not None:
                summary["removed"].append(resource_id)
            summary["unresolved"].append(resource_id)
        else:
            obj["license"] = deepcopy(inferred)
            summary["inferred"].append(resource_id)

        if write and previous != inferred:
            try:
                if _write_inferred_license(resource_dir, resource_id, inferred):
                    summary["written"].append(resource_id)
            except LicenseWriteRefused as refusal:
                # Keep the export honest: a license the page does not carry
                # must not appear in the registry either.
                print(f"WARN: inferred license for {resource_id} not written: {refusal}")
                if inferred is not None:
                    obj.pop("license", None)
                    summary["inferred"].remove(resource_id)
                summary["refused"].append(resource_id)

    return summary


def _plain(value: Any) -> Any:
    """Convert nested mappings and sequences to plain Python for comparison."""
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(v) for v in value]
    return value


_TOP_LEVEL_KEY = re.compile(r"^([A-Za-z0-9_]+):")


def _parsed_license(block: list[str]) -> Any:
    """The value of a ``license`` block, or None for an empty or unreadable one."""
    import yaml

    if not block:
        return None
    try:
        parsed = yaml.safe_load("\n".join(block))
    except yaml.YAMLError:
        return None
    return parsed.get("license") if isinstance(parsed, dict) else None


class LicenseWriteRefused(RuntimeError):
    """The page could not take an inferred license without harming what is there."""


def _block_is_replaceable(block: list[str]) -> bool:
    """A license block may be replaced if it is inferred or holds nothing.

    A bare ``license:`` line, or one whose value parses to null or an empty
    mapping, is not a provided license. Anything else that lacks
    ``status: inferred`` belongs to the curator.
    """
    import yaml

    if any(line.strip() == f"status: {STATUS_INFERRED}" for line in block):
        return True
    try:
        parsed = yaml.safe_load("\n".join(block))
    except yaml.YAMLError:
        return False
    return not (isinstance(parsed, dict) and parsed.get("license"))


def _write_inferred_license(
    resource_dir: pathlib.Path, resource_id: str, value: Optional[dict[str, Any]]
) -> bool:
    """Set or remove the inferred ``license`` block on a page, touching nothing else.

    The block is spliced into the front matter as text. Re-serializing the
    whole page with any YAML dumper reflows lines the page's other tools
    wrote, and that churn hides the real change. A ``license`` block that
    is not marked ``status: inferred`` is never touched. A new block is
    placed where a key sort would put it.
    """
    import yaml

    fn = resource_dir / resource_id / f"{resource_id}.md"
    if not fn.exists():
        raise LicenseWriteRefused(f"{fn} does not exist (is the working directory the repo root?)")
    text = fn.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise LicenseWriteRefused(f"{fn} has no front matter")
    close = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if close is None:
        raise LicenseWriteRefused(f"{fn} has no closing front matter delimiter")
    front = lines[1:close]

    start = next((i for i, line in enumerate(front) if line.startswith("license:")), None)
    stop = len(front)
    if start is not None:
        stop = next(
            (i for i in range(start + 1, len(front)) if _TOP_LEVEL_KEY.match(front[i])),
            len(front),
        )
    existing = front[start:stop] if start is not None else []
    if existing and not _block_is_replaceable(existing):
        raise LicenseWriteRefused(
            f"{fn} already carries a license that is not marked status: {STATUS_INFERRED}"
        )

    new_block: list[str] = []
    if value is not None:
        dumped = yaml.dump({"license": value}, sort_keys=True, allow_unicode=True)
        new_block = dumped.rstrip("\n").split("\n")
    # Compare what the block means, not how it is laid out. Other build steps
    # re-dump touched pages through ruamel with a different indent and width,
    # and a textual comparison would rewrite the block on every other build.
    if _parsed_license(existing) == _parsed_license(new_block):
        return False

    if start is not None:
        del front[start:stop]
    if new_block:
        position = next(
            (
                i
                for i, line in enumerate(front)
                if _TOP_LEVEL_KEY.match(line) and line.split(":", 1)[0] > "license"
            ),
            len(front),
        )
        front[position:position] = new_block
    lines[1:close] = front
    fn.write_text("\n".join(lines), encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

REPORT_COLUMNS = (
    "resource_id",
    "category",
    "status",
    "declared_license",
    "declared_tier",
    "inferred_license",
    "inferred_tier",
    "inferred_from",
    "unresolved_sources",
)


def _report_row(
    resource: Mapping[str, Any],
    declared: bool,
    inferred: Optional[dict[str, Any]],
    placeholder: bool = False,
) -> dict[str, str]:
    declared_tier = classify_license(resource.get("license")) if declared else None
    inferred_tier = inferred["restrictiveness"] if inferred else None
    if not upstream_sources(resource):
        status = "no-upstream"
    elif placeholder:
        status = "placeholder"
    elif (
        declared
        and inferred_tier
        and TIER_RANK[inferred_tier] > TIER_RANK[declared_tier or TIERS[0]]
    ):
        status = "conflict"
    elif declared:
        status = "declared"
    elif inferred:
        status = "inferred"
    else:
        status = "unresolved"
    return {
        "resource_id": str(resource.get("id") or ""),
        "category": str(resource.get("category") or ""),
        "status": status,
        "declared_license": (
            (_license_url(resource.get("license")) or _license_label(resource.get("license")))
            if declared or placeholder
            else ""
        ),
        "declared_tier": declared_tier or "",
        "inferred_license": (inferred or {}).get("id") or (inferred or {}).get("label", ""),
        "inferred_tier": inferred_tier or "",
        "inferred_from": "|".join((inferred or {}).get("inferred_from", [])),
        "unresolved_sources": "|".join((inferred or {}).get("unresolved_sources", [])),
    }


def write_report(rows: Iterable[Mapping[str, str]], path: pathlib.Path) -> None:
    """Write report rows as TSV, sorted by resource ID."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_COLUMNS, delimiter="\t")
        writer.writeheader()
        for row in sorted(rows, key=lambda r: r["resource_id"]):
            writer.writerow({key: row.get(key, "") for key in REPORT_COLUMNS})
