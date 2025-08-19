import tempfile
from pathlib import Path
import importlib.util
from types import SimpleNamespace
import yaml


def _load_extract_metadata_module(repo_root: Path):
    script_path = repo_root / "util" / "extract-metadata.py"
    spec = importlib.util.spec_from_file_location("extract_metadata", str(script_path))
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def test_invalid_domains_are_removed_and_valid_remain():
    repo_root = Path(__file__).resolve().parents[1]
    mod = _load_extract_metadata_module(repo_root)

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
