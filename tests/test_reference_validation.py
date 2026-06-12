"""Tests for cache-backed publication reference validation."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


def _load_reference_validation(repo_root: Path):
    module_path = repo_root / "util" / "reference_validation.py"
    spec = importlib.util.spec_from_file_location("reference_validation_under_test", module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _write_cache(cache_dir: Path, filename: str, metadata: str) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / filename).write_text(f"---\n{metadata}---\n\n## Content\n\nCached text\n")


def test_publication_reference_metadata_matches_cache(repo_root: Path, tmp_path: Path):
    mod = _load_reference_validation(repo_root)
    _write_cache(
        tmp_path,
        "DOI_10.1000_example.md",
        """reference_id: DOI:10.1000/example
title: Example Resource paper
authors:
- Smith J
- Jones A
journal: Journal of Examples
year: '2024'
doi: 10.1000/example
""",
    )

    report = mod.validate_publication_references(
        {
            "publications": [
                {
                    "id": "doi:10.1000/example",
                    "title": "Example Resource paper",
                    "authors": ["Smith J", "Jones A"],
                    "journal": "Journal of Examples",
                    "year": "2024",
                    "doi": "10.1000/example",
                }
            ]
        },
        "resource/example/example.md",
        cache_dir=tmp_path,
        require_cache=True,
    )

    assert report.checked_count == 1
    assert report.errors == []


def test_publication_reference_metadata_mismatch_is_error(repo_root: Path, tmp_path: Path):
    mod = _load_reference_validation(repo_root)
    _write_cache(
        tmp_path,
        "PMID_12345.md",
        """reference_id: PMID:12345
title: Correct title
authors:
- Correct A
year: '2024'
doi: 10.1000/correct
""",
    )

    report = mod.validate_publication_references(
        {
            "publications": [
                {
                    "id": "PMID:12345",
                    "title": "Wrong title",
                    "authors": ["Wrong A"],
                    "year": "2023",
                    "doi": "10.1000/wrong",
                }
            ]
        },
        "resource/example/example.md",
        cache_dir=tmp_path,
        require_cache=True,
    )

    assert any("title 'Wrong title' does not match cached title 'Correct title'" in e for e in report.errors)
    assert any("year '2023' does not match cached year '2024'" in e for e in report.errors)
    assert any("doi '10.1000/wrong' does not match cached doi '10.1000/correct'" in e for e in report.errors)
    assert any("first author 'Wrong A' does not match cached first author 'Correct A'" in e for e in report.errors)


def test_uncached_publication_reference_can_be_required(repo_root: Path, tmp_path: Path):
    mod = _load_reference_validation(repo_root)

    report = mod.validate_publication_references(
        {"publications": [{"id": "https://doi.org/10.1000/missing"}]},
        "resource/example/example.md",
        cache_dir=tmp_path,
        require_cache=True,
    )

    assert report.missing_cache_count == 1
    assert any("DOI:10.1000/missing has no cached reference" in e for e in report.errors)


def test_validate_markdown_runs_publication_reference_validation(
    extract_metadata_module,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
):
    mod = extract_metadata_module
    resource_dir = tmp_path / "tmpres"
    resource_dir.mkdir()
    md_path = resource_dir / "tmpres.md"
    md_path.write_text(
        """---
id: tmpres
layout: resource_detail
category: DataSource
name: Temp Resource
domains:
  - biomedical
publications:
  - id: PMID:12345
products:
  - id: tmpres.product
    category: Product
    name: Minimal Product
---

Content
"""
    )

    monkeypatch.setattr(mod, "validate", lambda **_: SimpleNamespace(results=[]))

    def fake_validate_publication_references(*args, **kwargs):
        return SimpleNamespace(errors=["publication mismatch"], warnings=["publication warning"])

    monkeypatch.setattr(
        mod,
        "validate_publication_references",
        fake_validate_publication_references,
    )

    with pytest.raises(SystemExit):
        mod.validate_markdown(SimpleNamespace(files=[str(md_path)]))
