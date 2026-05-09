"""Helpers for product source provenance associations."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

ORIGINAL_SOURCE_RELATION = "prov:hadPrimarySource"
SECONDARY_SOURCE_RELATION = "prov:wasInfluencedBy"


def make_source_association(source: str, relation_type: str) -> dict[str, str]:
    """Create a source association object in the schema shape."""
    return {"source": source, "relation_type": relation_type}


def make_original_source_associations(sources: Iterable[str]) -> list[dict[str, str]]:
    """Create default original_source associations."""
    return [
        make_source_association(source, ORIGINAL_SOURCE_RELATION)
        for source in _unique_non_empty_strings(sources)
    ]


def make_secondary_source_associations(sources: Iterable[str]) -> list[dict[str, str]]:
    """Create default secondary_source associations."""
    return [
        make_source_association(source, SECONDARY_SOURCE_RELATION)
        for source in _unique_non_empty_strings(sources)
    ]


def normalize_source_associations(
    associations: Any,
    default_relation_type: str,
) -> list[dict[str, str]]:
    """Normalize legacy strings and association mappings to schema-shaped objects."""
    normalized: list[dict[str, str]] = []
    seen: set[str] = set()
    for association in _ensure_list(associations):
        source = source_association_id(association)
        if not source or source in seen:
            continue
        relation_type = source_association_relation(association, default_relation_type)
        normalized.append(make_source_association(source, relation_type))
        seen.add(source)
    return normalized


def merge_source_associations(
    existing_associations: Any,
    new_sources: Iterable[str],
    default_relation_type: str,
) -> list[dict[str, str]]:
    """Merge new source identifiers into existing associations, preserving relations."""
    merged = normalize_source_associations(existing_associations, default_relation_type)
    seen = {association["source"] for association in merged}
    for source in _unique_non_empty_strings(new_sources):
        if source in seen:
            continue
        merged.append(make_source_association(source, default_relation_type))
        seen.add(source)
    return sorted(merged, key=lambda association: association["source"])


def source_association_id(association: Any) -> str | None:
    """Return the source identifier from either a new association or a legacy string."""
    if isinstance(association, str):
        source = association.strip()
        return source or None
    if isinstance(association, dict):
        source = association.get("source")
        if isinstance(source, str) and source.strip():
            return source.strip()
    return None


def source_association_relation(association: Any, default_relation_type: str | None = None) -> str | None:
    """Return the relation type from an association, falling back when needed."""
    if isinstance(association, dict):
        relation_type = association.get("relation_type")
        if isinstance(relation_type, str) and relation_type.strip():
            return relation_type.strip()
    return default_relation_type


def iter_source_ids(associations: Any) -> Iterable[str]:
    """Yield source identifiers from association objects or legacy strings."""
    for association in _ensure_list(associations):
        source = source_association_id(association)
        if source:
            yield source


def _ensure_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _unique_non_empty_strings(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for value in values:
        if not isinstance(value, str):
            continue
        source = value.strip()
        if not source or source in seen:
            continue
        unique.append(source)
        seen.add(source)
    return unique
