import tempfile
from pathlib import Path
import importlib.util
from types import SimpleNamespace
import yaml


def _load_extract_metadata_module(repo_root: Path):
    """Dynamically load util/extract-metadata.py as a module."""
    script_path = repo_root / "util" / "extract-metadata.py"
    spec = importlib.util.spec_from_file_location("extract_metadata", str(script_path))
    assert spec is not None and spec.loader is not None, "Could not load extract-metadata.py"
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def test_validate_coerces_numeric_strings_and_writes_back():
    repo_root = Path(__file__).resolve().parents[1]
    mod = _load_extract_metadata_module(repo_root)

    with tempfile.TemporaryDirectory() as td:
        # Create a resource-like directory and markdown file
        res_dir = Path(td) / "tmpres"
        res_dir.mkdir(parents=True, exist_ok=True)
        md_path = res_dir / "tmpres.md"

        md = """---
id: tmpresx
layout: resource_detail
name: Temp Resource
domains:
  - biomedical
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

        # Run validator (which should coerce and write back in-place)
        args = SimpleNamespace(files=[str(md_path)])
        mod.validate_markdown(args)

        # Read frontmatter back and assert types are strings
        text = md_path.read_text()
        parts = text.split("---")
        assert len(parts) >= 3, "Frontmatter missing"
        meta = yaml.safe_load(parts[1])

        # Publication year should be a string
        pubs = meta.get("publications", [])
        assert isinstance(pubs, list) and pubs, "Missing publications"
        assert isinstance(pubs[0]["year"], str)
        assert pubs[0]["year"] == "1990"

        # Product versions should be a list of strings
        prods = meta.get("products", [])
        assert isinstance(prods, list) and prods, "Missing products"
        versions = prods[0].get("versions")
        assert isinstance(versions, list)
        assert all(isinstance(v, str) for v in versions)
        assert versions == ["1", "2"]
