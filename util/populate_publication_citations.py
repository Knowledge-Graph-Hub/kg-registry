#!/usr/bin/env python3
"""Populate Resource publication citation metadata from the reference cache.

KG-Registry validates each Resource page's ``publications`` entries against
cached reference files produced by ``linkml-reference-validator`` (see
``util/reference_validation.py`` and ``docs/reference-validation.md``). The
validator reports *warnings* when a publication is missing fields that the
cache already knows (authors, journal, year, doi, title) and *errors* when a
present field disagrees with the cache (e.g. a wrong year).

This utility closes those gaps automatically. For each publication on a
Resource page it locates the matching cache file, fills in any missing
bibliographic fields, and corrects flagged year mismatches, then rewrites the
``publications:`` block in the canonical normalized form. It is the companion
"repair" step to the read-only validation in ``reference_validation.py``: run
the validator to find issues, run this to fix the cache-backed ones.

What it does NOT do (these still need human judgement):
  * Fetch missing cache files. If a publication has no cached reference, it is
    left untouched. Populate the cache first with
    ``uv run ./util/extract-metadata.py validate --fetch-publication-references
    resource/<id>/<id>.md``.
  * Add publications to a Resource that has none.
  * Resolve title / DOI / first-author mismatches, or remove duplicate
    citations. Only year mismatches are auto-corrected because the cached year
    (fetched from the publisher) is authoritative; other mismatches may mean the
    page cites a different work than the cache and should be reviewed by hand.

Canonical output format (matches the rest of the registry):
  * keys sorted alphabetically: authors, doi, id, journal, preferred, title, year
  * two-space, non-nested block indentation
  * ``doi:`` holds the bare DOI (no ``doi:`` prefix); the prefix belongs on
    ``id`` instead
  * scalars are single-quoted only when YAML requires it, so existing unquoted
    URLs/CURIEs are preserved

Only the ``publications:`` block of the front matter is rewritten; the rest of
the file (other front matter keys, ordering, and the Markdown body) is spliced
back verbatim.

Usage:
  # Preview the regenerated block(s) without touching files:
  uv run ./util/populate_publication_citations.py oma go drugbank

  # Apply the changes in place:
  uv run ./util/populate_publication_citations.py --apply oma go drugbank

Always re-run validation afterwards to confirm the warnings cleared:
  uv run ./util/extract-metadata.py validate resource/<id>/<id>.md
"""

from __future__ import annotations

import re
import sys
from argparse import ArgumentParser
from pathlib import Path

import yaml

# Reuse the canonical identifier -> cache-path logic from the validator so this
# utility and the validator always agree on which cache file backs a citation.
try:
    from util.reference_validation import (
        DEFAULT_CACHE_DIR,
        cache_path_for_reference,
        load_reference_cache,
        normalize_reference_id,
    )
except ModuleNotFoundError:  # when invoked as ./util/populate_publication_citations.py
    sys.path.insert(0, str(Path(__file__).parent.resolve()))
    from reference_validation import (
        DEFAULT_CACHE_DIR,
        cache_path_for_reference,
        load_reference_cache,
        normalize_reference_id,
    )

# Fields copied from the cache into a publication when missing, in the order the
# validator reports them. ``title`` is included because some pages omit it.
CACHE_FIELDS = ("authors", "journal", "title", "year", "doi")

# Canonical key order for a serialized publication entry (alphabetical).
KEY_ORDER = ("authors", "doi", "id", "journal", "preferred", "title", "year")


def resource_path(resource_id: str) -> Path:
    """Return the Markdown path for a Resource id (e.g. ``oma`` -> resource/oma/oma.md)."""

    return Path("resource") / resource_id / f"{resource_id}.md"


def load_front_matter(path: Path) -> dict:
    """Parse the YAML front matter (the block between the leading ``---`` fences).

    Returns the parsed mapping. Used for reading current publication values; the
    actual rewrite is done by line splicing so the Markdown body is untouched.
    """

    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        raise ValueError(f"{path}: no YAML front matter found")
    return yaml.safe_load(match.group(1))


def cache_for_publication(publication: dict, cache_dir: Path) -> dict | None:
    """Return cached reference front matter for a publication, or ``None``.

    The reference id is derived from the publication's ``doi`` (preferred) or
    ``id`` using the validator's :func:`normalize_reference_id`, then mapped to a
    cache file with :func:`cache_path_for_reference`. Missing cache files yield
    ``None`` so the caller leaves the entry unchanged.
    """

    raw = publication.get("doi") or publication.get("id")
    if not raw:
        return None
    reference_id = normalize_reference_id(str(raw))
    cache_path = cache_path_for_reference(reference_id, cache_dir)
    if not cache_path.exists():
        return None
    return load_reference_cache(cache_path)


def merge_publication(publication: dict, cache: dict | None) -> dict:
    """Merge cached bibliographic fields into a publication entry.

    Missing fields are filled from the cache; a present ``year`` that disagrees
    with the cache is corrected (the published year is authoritative). The
    ``doi`` value is normalized to the bare DOI with any ``doi:`` prefix
    stripped. All other present fields are preserved as-is.
    """

    merged = dict(publication)
    if cache:
        for field_name in CACHE_FIELDS:
            current = merged.get(field_name)
            cached_value = cache.get(field_name)
            if current in (None, "", []):
                if cached_value not in (None, "", []):
                    merged[field_name] = cached_value
            elif (
                field_name == "year"
                and cached_value
                and str(current) != str(cached_value)
            ):
                merged[field_name] = cached_value
    if merged.get("doi"):
        merged["doi"] = re.sub(r"^doi:", "", str(merged["doi"]))
    return merged


def _quote(value) -> str:
    """Single-quote a YAML scalar, doubling any embedded single quotes."""

    return "'" + str(value).replace("'", "''") + "'"


def _emit_scalar(key: str, value) -> str:
    """Render ``key: value`` for a nested line, quoting only when YAML needs it.

    Bare URLs and CURIEs (``https://...``, ``doi:10...``) stay unquoted because
    their colon is not followed by a space; titles containing ``": "`` and other
    YAML-significant forms are single-quoted. This mirrors the existing style of
    the registry pages to keep diffs minimal.
    """

    text = str(value)
    needs_quoting = (
        ": " in text
        or text.endswith(":")
        or " #" in text
        or text != text.strip()
        or text == ""
        or text[0] in "[]{}>|*&!%@`\"'#,"
    )
    return f"  {key}: {_quote(text) if needs_quoting else text}"


def format_publications_block(publications: list[dict]) -> str:
    """Serialize publications into the canonical ``publications:`` YAML block.

    Keys are emitted in :data:`KEY_ORDER`; empty/absent fields are skipped. The
    first key of each entry carries the ``- `` list marker.
    """

    lines = ["publications:"]
    for publication in publications:
        first = True
        for key in KEY_ORDER:
            value = publication.get(key)
            if value in (None, "", []):
                continue
            if key == "authors":
                lines.append("- authors:" if first else "  authors:")
                for author in value:
                    lines.append(f"  - {author}")
            elif key == "preferred":
                marker = "- " if first else "  "
                lines.append(f"{marker}preferred: {str(value).lower()}")
            elif key == "year":
                marker = "- " if first else "  "
                lines.append(f"{marker}year: {_quote(str(value))}")
            else:
                line = _emit_scalar(key, value)
                lines.append(("- " + line[2:]) if first else line)
            first = False
    return "\n".join(lines)


def build_block(resource_id: str, cache_dir: Path) -> str:
    """Compute the regenerated ``publications:`` block text for a Resource."""

    front_matter = load_front_matter(resource_path(resource_id))
    publications = front_matter.get("publications")
    if not publications:
        raise ValueError(f"{resource_id}: no publications to populate")
    merged = [
        merge_publication(pub, cache_for_publication(pub, cache_dir))
        for pub in publications
    ]
    return format_publications_block(merged)


def apply_block(resource_id: str, cache_dir: Path) -> str:
    """Rewrite a Resource's ``publications:`` block in place; return a status line.

    Splices the new block over the existing one within the front matter,
    leaving every other line of the file untouched.
    """

    path = resource_path(resource_id)
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines[0] != "---":
        raise ValueError(f"{path}: file does not start with '---'")
    front_matter_end = lines.index("---", 1)

    start = next(
        (i for i in range(1, front_matter_end) if lines[i] == "publications:"),
        None,
    )
    if start is None:
        raise ValueError(f"{resource_id}: no 'publications:' key in front matter")

    # The block runs until the next top-level front matter key (unindented).
    end = front_matter_end
    for i in range(start + 1, front_matter_end):
        if re.match(r"^[A-Za-z_][\w-]*:", lines[i]):
            end = i
            break

    new_block = build_block(resource_id, cache_dir).split("\n")
    updated = lines[:start] + new_block + lines[end:]
    path.write_text("\n".join(updated), encoding="utf-8")
    return f"applied {resource_id}: replaced lines {start + 1}-{end} with {len(new_block)} lines"


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser(
        description=(
            "Populate Resource publication citation metadata from the reference "
            "cache. Prints the regenerated block(s) by default; use --apply to "
            "write changes in place."
        )
    )
    parser.add_argument(
        "resources",
        nargs="+",
        metavar="RESOURCE_ID",
        help="Resource ids to process (e.g. oma go drugbank)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Rewrite the publications block in place (default: print a preview)",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=DEFAULT_CACHE_DIR,
        help=f"Reference cache directory (default: {DEFAULT_CACHE_DIR})",
    )
    args = parser.parse_args(argv)

    for resource_id in args.resources:
        if args.apply:
            print(apply_block(resource_id, args.cache_dir))
        else:
            print(f"########## {resource_id} ##########")
            print(build_block(resource_id, args.cache_dir))
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
