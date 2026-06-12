"""Cache-backed validation for Resource publication metadata."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

import frontmatter
import yaml


DEFAULT_CACHE_DIR = Path("references_cache")
DEFAULT_CONFIG_PATHS = (
    Path(".linkml-reference-validator.yaml"),
    Path(".linkml-reference-validator.yml"),
)
TRUE_VALUES = {"1", "true", "yes", "y", "on"}


@dataclass
class PublicationReferenceCheck:
    """Validation details for one publication reference."""

    reference_id: str
    cache_path: Path | None = None
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class PublicationReferenceReport:
    """Aggregate publication reference validation output."""

    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checked_count: int = 0
    missing_cache_count: int = 0
    fetched_count: int = 0


def validate_publication_references(
    metadata: dict[str, Any],
    source_path: str | Path,
    *,
    cache_dir: str | Path | None = None,
    config_path: str | Path | None = None,
    fetch_missing: bool = False,
    require_cache: bool = False,
) -> PublicationReferenceReport:
    """Validate publication metadata against linkml-reference-validator cache files."""

    report = PublicationReferenceReport()
    publications = metadata.get("publications") or []
    if not isinstance(publications, list) or not publications:
        return report

    cache_root = resolve_cache_dir(cache_dir, config_path)
    config = Path(config_path) if config_path else find_default_config()
    source_path = Path(source_path)

    for index, publication in enumerate(publications):
        if not isinstance(publication, dict):
            continue

        raw_identifier = publication.get("id") or publication.get("doi")
        if not raw_identifier:
            continue

        reference_id = normalize_reference_id(str(raw_identifier))
        cache_path = cache_path_for_reference(reference_id, cache_root)

        if not cache_path.exists() and fetch_missing:
            if cache_reference(reference_id, cache_root, config):
                report.fetched_count += 1

        if not cache_path.exists():
            report.missing_cache_count += 1
            if require_cache:
                report.errors.append(
                    f"{source_path} publication[{index}] {reference_id} has no cached reference at {cache_path}"
                )
            continue

        cached = load_reference_cache(cache_path)
        check = compare_publication_to_cache(publication, cached, reference_id, cache_path)
        report.checked_count += 1
        report.errors.extend(
            f"{source_path} publication[{index}] {message}" for message in check.errors
        )
        report.warnings.extend(
            f"{source_path} publication[{index}] {message}" for message in check.warnings
        )

    if report.missing_cache_count and not require_cache:
        report.warnings.append(
            f"{source_path}: {report.missing_cache_count} publication reference(s) were not cached in {cache_root}"
        )

    return report


def compare_publication_to_cache(
    publication: dict[str, Any],
    cached: dict[str, Any],
    reference_id: str,
    cache_path: Path,
) -> PublicationReferenceCheck:
    """Compare one Publication object to cached reference front matter."""

    check = PublicationReferenceCheck(reference_id=reference_id, cache_path=cache_path)

    cached_reference_id = cached.get("reference_id")
    if cached_reference_id and normalize_reference_id(str(cached_reference_id)) != reference_id:
        check.errors.append(
            f"uses cache {cache_path} for {reference_id}, but cache declares {cached_reference_id}"
        )

    _compare_text_field(check, publication, cached, "title", strict=True)
    _compare_text_field(check, publication, cached, "journal", strict=False)
    _compare_text_field(check, publication, cached, "year", strict=True)

    pub_doi = publication.get("doi")
    cached_doi = cached.get("doi")
    if pub_doi and cached_doi and normalize_doi(str(pub_doi)) != normalize_doi(str(cached_doi)):
        check.errors.append(
            f"doi {pub_doi!r} does not match cached doi {cached_doi!r} in {cache_path}"
        )

    pub_authors = _coerce_list(publication.get("authors"))
    cached_authors = _coerce_list(cached.get("authors"))
    if pub_authors and cached_authors:
        pub_first = normalize_author(pub_authors[0])
        cached_first = normalize_author(cached_authors[0])
        if pub_first and cached_first and pub_first != cached_first:
            check.errors.append(
                f"first author {pub_authors[0]!r} does not match cached first author {cached_authors[0]!r} in {cache_path}"
            )
    elif cached_authors and not pub_authors:
        check.warnings.append(f"authors missing; cached authors are available in {cache_path}")

    for field_name in ("title", "journal", "year", "doi"):
        if cached.get(field_name) and not publication.get(field_name):
            check.warnings.append(f"{field_name} missing; cached {field_name} is available in {cache_path}")

    return check


def resolve_cache_dir(
    cache_dir: str | Path | None = None, config_path: str | Path | None = None
) -> Path:
    """Resolve the reference cache directory from args, env, config, or default."""

    if cache_dir:
        return Path(cache_dir)

    env_cache = os.environ.get("KG_REGISTRY_REFERENCE_CACHE_DIR") or os.environ.get(
        "REFERENCE_CACHE_DIR"
    )
    if env_cache:
        return Path(env_cache)

    config = Path(config_path) if config_path else find_default_config()
    if config:
        configured = cache_dir_from_config(config)
        if configured:
            return configured

    return DEFAULT_CACHE_DIR


def find_default_config() -> Path | None:
    """Return the first local linkml-reference-validator config file, if any."""

    for config_path in DEFAULT_CONFIG_PATHS:
        if config_path.exists():
            return config_path
    return None


def cache_dir_from_config(config_path: Path) -> Path | None:
    """Extract cache_dir from a linkml-reference-validator config file."""

    try:
        data = yaml.safe_load(config_path.read_text()) or {}
    except OSError:
        return None

    if not isinstance(data, dict):
        return None

    section = data.get("validation") if isinstance(data.get("validation"), dict) else data
    cache_dir = section.get("cache_dir") if isinstance(section, dict) else None
    return Path(cache_dir) if cache_dir else None


def normalize_reference_id(raw_identifier: str) -> str:
    """Normalize KG-Registry publication IDs into reference-validator IDs."""

    identifier = raw_identifier.strip()
    if not identifier:
        return identifier

    pubmed_match = re.match(
        r"^https?://(?:www\.)?(?:pubmed\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pubmed)/(\d+)/?$",
        identifier,
        flags=re.IGNORECASE,
    )
    if pubmed_match:
        return f"PMID:{pubmed_match.group(1)}"

    doi_url_match = re.match(r"^https?://(?:dx\.)?doi\.org/(10\..+)$", identifier, re.IGNORECASE)
    if doi_url_match:
        return f"DOI:{doi_url_match.group(1)}"

    if re.match(r"^doi:10\.", identifier, flags=re.IGNORECASE):
        return f"DOI:{identifier.split(':', 1)[1]}"

    if re.match(r"^10\.\S+/.+", identifier):
        return f"DOI:{identifier}"

    if re.match(r"^pmid[:\s]+\d+$", identifier, flags=re.IGNORECASE):
        pmid = re.split(r"[:\s]+", identifier, maxsplit=1)[1]
        return f"PMID:{pmid}"

    if identifier.isdigit():
        return f"PMID:{identifier}"

    parsed = urlparse(identifier)
    if parsed.scheme in {"http", "https"}:
        return f"url:{identifier}"

    prefix_match = re.match(r"^([A-Za-z_]+)[:\s]+(.+)$", identifier)
    if prefix_match:
        prefix = prefix_match.group(1)
        normalized_prefix = prefix.lower() if prefix.lower() in {"url", "file"} else prefix.upper()
        return f"{normalized_prefix}:{prefix_match.group(2).strip()}"

    return identifier


def cache_path_for_reference(reference_id: str, cache_dir: str | Path) -> Path:
    """Return the cache path generated by linkml-reference-validator."""

    safe_id = (
        reference_id.replace(":", "_")
        .replace("/", "_")
        .replace("?", "_")
        .replace("=", "_")
    )
    return Path(cache_dir) / f"{safe_id}.md"


def cache_reference(reference_id: str, cache_dir: Path, config_path: Path | None = None) -> bool:
    """Fetch a reference into the cache using linkml-reference-validator when available."""

    command = shutil.which("linkml-reference-validator")
    if not command:
        return False

    args = [command, "cache", "reference", reference_id, "--cache-dir", str(cache_dir)]
    if config_path:
        args.extend(["--config", str(config_path)])

    completed = subprocess.run(args, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return completed.returncode == 0


def load_reference_cache(cache_path: str | Path) -> dict[str, Any]:
    """Load front matter from a linkml-reference-validator cache file."""

    post = frontmatter.load(str(cache_path))
    return dict(post.metadata)


def normalize_doi(value: str) -> str:
    """Normalize DOI strings for equality checks."""

    doi = value.strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:", "", doi, flags=re.IGNORECASE)
    return doi.rstrip(".").casefold()


def normalize_text(value: str) -> str:
    """Normalize bibliographic text enough to compare common formatting variants."""

    text = value.strip().casefold()
    text = re.sub(r"\s+", " ", text)
    return text.rstrip(".")


def normalize_author(value: str) -> str:
    """Normalize an author string for first-author comparisons."""

    text = normalize_text(value)
    text = re.sub(r"[.,]", "", text)
    return text


def env_flag(name: str, default: bool = False) -> bool:
    """Read a boolean environment flag."""

    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().casefold() in TRUE_VALUES


def _compare_text_field(
    check: PublicationReferenceCheck,
    publication: dict[str, Any],
    cached: dict[str, Any],
    field_name: str,
    *,
    strict: bool,
) -> None:
    published_value = publication.get(field_name)
    cached_value = cached.get(field_name)
    if not published_value or not cached_value:
        return

    if normalize_text(str(published_value)) != normalize_text(str(cached_value)):
        message = (
            f"{field_name} {published_value!r} does not match cached {field_name} "
            f"{cached_value!r} in {check.cache_path}"
        )
        if strict:
            check.errors.append(message)
        else:
            check.warnings.append(message)


def _coerce_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Iterable):
        return [str(item) for item in value if item is not None]
    return [str(value)]
