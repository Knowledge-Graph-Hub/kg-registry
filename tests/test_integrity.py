"""Repository-level integrity checks that complement schema validation."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlparse

import frontmatter


HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent
RESOURCE_DIR = ROOT / "resource"

ALLOWED_SPDX = {
    "CC0-1.0",
    "CC-BY-3.0",
    "CC-BY-4.0",
}

OBO_TO_SPDX = {
    "CC BY 4.0": "CC-BY-4.0",
    "CC BY 3.0": "CC-BY-3.0",
    "CC0": "CC0-1.0",
}

PUBLICATION_ID_PATTERNS = [
    re.compile(r"^PMID:\d+$", re.IGNORECASE),
    re.compile(r"^https://www\.ncbi\.nlm\.nih\.gov/pubmed/\d+/?$"),
    re.compile(r"^https://pubmed\.ncbi\.nlm\.nih\.gov/\d+/?$"),
    re.compile(r"^doi:10\..+", re.IGNORECASE),
    re.compile(r"^https?://doi\.org/10\..+", re.IGNORECASE),
    re.compile(r"^arxiv:\d{4}\.\d{4,5}$", re.IGNORECASE),
    re.compile(r"^https://arxiv\.org/abs/.+", re.IGNORECASE),
    re.compile(r"^https://www\.biorxiv\.org/content/.+", re.IGNORECASE),
    re.compile(r"^https://www\.medrxiv\.org/content/.+", re.IGNORECASE),
    re.compile(r"^https://zenodo\.org/record/\d+/?$", re.IGNORECASE),
]

# Some current resources use compact internal citation identifiers instead of
# canonical DOI/PMID/URL forms. These should at least remain whitespace-free.
LEGACY_PUBLICATION_ID_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")


@lru_cache(maxsize=1)
def _load_root_resource_posts() -> list[tuple[Path, dict]]:
    posts: list[tuple[Path, dict]] = []
    for path in sorted(RESOURCE_DIR.glob("*/*.md")):
        if path.stem != path.parent.name:
            continue
        post = frontmatter.load(path)
        posts.append((path, dict(post.metadata)))
    return posts


def _iter_publications():
    for path, metadata in _load_root_resource_posts():
        for index, publication in enumerate(metadata.get("publications", []) or []):
            yield path, index, publication


def _is_supported_publication_identifier(identifier: str) -> bool:
    if any(pattern.match(identifier) for pattern in PUBLICATION_ID_PATTERNS):
        return True

    parsed = urlparse(identifier)
    if parsed.scheme in {"http", "https"} and parsed.netloc and " " not in identifier:
        return True

    return bool(LEGACY_PUBLICATION_ID_PATTERN.match(identifier))


def test_obo_spdx_mapping_targets_allowed_licenses():
    """Keep the OBO license mapping aligned with the SPDX allowlist used in tests."""
    assert set(OBO_TO_SPDX.values()) <= ALLOWED_SPDX


def test_root_resource_publications_have_at_most_one_preferred_entry():
    """A resource should not mark multiple publication entries as preferred."""
    violations = []

    for path, metadata in _load_root_resource_posts():
        publications = metadata.get("publications", []) or []
        preferred_count = sum(
            1 for publication in publications if isinstance(publication, dict) and publication.get("preferred")
        )
        if preferred_count > 1:
            violations.append(f"{path}: preferred_count={preferred_count}")

    assert not violations, "Multiple preferred publications found:\n" + "\n".join(violations)


def test_root_resource_publications_have_non_empty_identifier():
    """Every publication entry should carry a non-empty identifier or URL."""
    violations = []

    for path, index, publication in _iter_publications():
        if not isinstance(publication, dict):
            violations.append(f"{path} publication[{index}] is not a mapping")
            continue

        identifier = publication.get("id") or publication.get("url")
        if not isinstance(identifier, str) or not identifier.strip():
            violations.append(f"{path} publication[{index}] is missing id/url")

    assert not violations, "Publication identifier issues found:\n" + "\n".join(violations)


def test_root_resource_publication_identifiers_use_supported_formats():
    """Publication identifiers should be canonical URLs/prefixes or compact local identifiers."""
    violations = []

    for path, index, publication in _iter_publications():
        if not isinstance(publication, dict):
            continue

        identifier = publication.get("id") or publication.get("url")
        if not isinstance(identifier, str):
            continue

        normalized_identifier = identifier.strip()
        if not _is_supported_publication_identifier(normalized_identifier):
            violations.append(f"{path} publication[{index}] has unsupported identifier: {normalized_identifier}")

    assert not violations, "Unsupported publication identifiers found:\n" + "\n".join(violations)
