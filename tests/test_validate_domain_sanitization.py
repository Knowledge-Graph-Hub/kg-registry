"""Test domain sanitization performed by extract-metadata validation."""

import tempfile
from pathlib import Path
from types import SimpleNamespace

import yaml


def test_invalid_domains_are_removed_and_valid_remain(extract_metadata_module):
    mod = extract_metadata_module
    with tempfile.TemporaryDirectory() as td:
        res_dir = Path(td) / "tmpres"
        res_dir.mkdir(parents=True, exist_ok=True)
        md_path = res_dir / "tmpres.md"

        md = """---
id: tmpresx
layout: resource_detail
name: Temp Resource
domains:
  - biomedical
  - potatosalad
  - health
publications:
  - title: Example Pub
    id: https://doi.org/10.1000/xyz123
    year: 1990
products:
  - name: Minimal Product
    versions: [1, 2]
---

Content
"""
        md_path.write_text(md)

        args = SimpleNamespace(files=[str(md_path)])
        mod.validate_markdown(args)

        text = md_path.read_text()
        parts = text.split("---")
        assert len(parts) >= 3
        meta = yaml.safe_load(parts[1])

        # Expect invalid domain removed, valid remain in original order minus invalids
        assert meta.get("domains") == ["biomedical", "health"]
