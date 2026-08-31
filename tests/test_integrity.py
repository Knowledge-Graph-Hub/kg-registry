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
            1
            for publication in publications
            if isinstance(publication, dict) and publication.get("preferred")
        )
        if preferred_count > 1:
            violations.append(f"{path}: preferred_count={preferred_count}")

    assert not violations, "Multiple preferred publications found:\n" + "\n".join(violations)


def test_root_resource_publications_have_non_empty_identifier():
    """Every publication entry should carry a non-empty `id`."""
    violations = []

    for path, index, publication in _iter_publications():
        if not isinstance(publication, dict):
            violations.append(f"{path} publication[{index}] is not a mapping")
            continue

        identifier = publication.get("id")
        if not isinstance(identifier, str) or not identifier.strip():
            violations.append(f"{path} publication[{index}] is missing id")

    assert not violations, "Publication identifier issues found:\n" + "\n".join(violations)


def test_root_resource_publication_identifiers_use_supported_formats():
    """Publication identifiers should be canonical URLs/prefixes or compact local identifiers."""
    violations = []

    for path, index, publication in _iter_publications():
        if not isinstance(publication, dict):
            continue

        identifier = publication.get("id")
        if not isinstance(identifier, str):
            continue

        normalized_identifier = identifier.strip()
        if not _is_supported_publication_identifier(normalized_identifier):
            violations.append(
                f"{path} publication[{index}] has unsupported identifier: {normalized_identifier}"
            )

    assert not violations, "Unsupported publication identifiers found:\n" + "\n".join(violations)


@lru_cache(maxsize=1)
def _resource_ids() -> frozenset[str]:
    return frozenset(
        str(metadata.get("id") or path.parent.name)
        for path, metadata in _load_root_resource_posts()
    )


def _iter_products():
    for path, metadata in _load_root_resource_posts():
        resource_id = str(metadata.get("id") or path.parent.name)
        for index, product in enumerate(metadata.get("products", []) or []):
            if isinstance(product, dict):
                yield path, resource_id, index, product


def test_product_ids_are_namespaced_under_an_existing_resource():
    """Every product ID must be `<resource-id>.<suffix>` for a Resource that exists.

    Product ownership is decided by that prefix: it picks the Resource scored for
    the product's metadata quality and the directory holding its detail page. A
    product whose prefix names no Resource is owned by nobody and drops out of
    both. Either the prefix is wrong or the product does not belong here.
    """
    violations = []

    for path, _resource_id, index, product in _iter_products():
        product_id = product.get("id")
        if not isinstance(product_id, str) or not product_id.strip():
            violations.append(f"{path} products[{index}] is missing id")
            continue

        product_id = product_id.strip()
        owner, separator, _ = product_id.partition(".")
        if not separator or not owner:
            violations.append(f"{path} products[{index}] id {product_id!r} has no resource prefix")
        elif owner not in _resource_ids():
            violations.append(
                f"{path} products[{index}] id {product_id!r} has prefix {owner!r}, "
                "which is not a Resource ID"
            )

    assert not violations, "Product ownership issues found:\n" + "\n".join(violations)


def test_products_are_listed_on_their_owning_resource_page():
    """A product must appear on the page of the Resource that owns it.

    Products are also propagated onto the page of every Resource they cite as a
    source, so being listed somewhere is not enough.
    """
    listed_by_owner: dict[str, set[str]] = {}
    all_product_ids: set[str] = set()

    for _path, resource_id, _index, product in _iter_products():
        product_id = product.get("id")
        if not isinstance(product_id, str) or "." not in product_id:
            continue
        product_id = product_id.strip()
        all_product_ids.add(product_id)
        listed_by_owner.setdefault(resource_id, set()).add(product_id)

    violations = [
        f"{product_id} is not listed on resource/{product_id.split('.', 1)[0]}/"
        for product_id in sorted(all_product_ids)
        if product_id not in listed_by_owner.get(product_id.split(".", 1)[0], set())
    ]

    assert not violations, "Products missing from their owner's page:\n" + "\n".join(violations)


def test_product_detail_pages_live_under_their_owning_resource():
    """Detail pages belong in the owner's directory, never a propagation target's."""
    violations = []

    for path in sorted(RESOURCE_DIR.glob("*/*.md")):
        if path.stem == path.parent.name:
            continue
        metadata = dict(frontmatter.load(path).metadata)
        if str(metadata.get("layout", "")).strip() != "product_detail":
            continue

        product_id = metadata.get("id")
        if not isinstance(product_id, str) or "." not in product_id:
            violations.append(f"{path} has no namespaced product id")
            continue

        owner = product_id.split(".", 1)[0]
        if owner != path.parent.name:
            violations.append(f"{path} holds {product_id!r}, owned by {owner!r}")

    assert not violations, "Misplaced product detail pages found:\n" + "\n".join(violations)


def test_no_stale_product_detail_pages():
    """Every product detail page must describe a product some Resource still lists.

    Product pages are generated, and `remove_stale_product_pages` reaps them when a
    product is renamed or dropped. A page left behind publishes a URL for something
    the registry no longer describes.
    """
    listed_product_ids = {
        product["id"].strip()
        for _path, _resource_id, _index, product in _iter_products()
        if isinstance(product.get("id"), str) and product["id"].strip()
    }

    violations = []
    for path in sorted(RESOURCE_DIR.glob("*/*.md")):
        if path.stem == path.parent.name:
            continue
        metadata = dict(frontmatter.load(path).metadata)
        if str(metadata.get("layout", "")).strip() != "product_detail":
            continue

        product_id = metadata.get("id")
        product_id = product_id.strip() if isinstance(product_id, str) else path.stem
        if product_id not in listed_product_ids:
            violations.append(f"{path} describes {product_id!r}, which no Resource lists")

    assert not violations, "Stale product detail pages found:\n" + "\n".join(violations)


def test_every_product_has_a_detail_page():
    """Each product needs the page its Resource page links to."""
    violations = []
    for _path, _resource_id, _index, product in _iter_products():
        product_id = product.get("id")
        if not isinstance(product_id, str) or "." not in product_id:
            continue
        product_id = product_id.strip()
        owner = product_id.split(".", 1)[0]
        if not (RESOURCE_DIR / owner / f"{product_id}.md").exists():
            violations.append(f"{product_id} has no page at resource/{owner}/{product_id}.md")

    assert not violations, "Products without a detail page:\n" + "\n".join(sorted(set(violations)))
