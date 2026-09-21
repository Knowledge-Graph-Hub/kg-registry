"""Test that validation rejects `category` values that are not schema classes."""

import tempfile
from pathlib import Path
from types import SimpleNamespace

import pytest


def _write_resource(td, category, product_category, contact_category="Individual"):
    res_dir = Path(td) / "tmpres"
    res_dir.mkdir(parents=True, exist_ok=True)
    md_path = res_dir / "tmpres.md"
    md_path.write_text(
        f"""---
id: tmpres
layout: resource_detail
name: Temp Resource
category: {category}
domains:
  - biomedical
contacts:
  - category: {contact_category}
    label: Someone
products:
  - id: tmpres.download
    name: Download
    category: {product_category}
    format: tsv
---

Content
"""
    )
    return md_path


def test_check_category_classes_accepts_schema_classes(extract_metadata_module):
    obj = {
        "id": "x",
        "category": "KnowledgeGraph",
        "contacts": [{"category": "Organization", "label": "Lab"}],
        "products": [
            {"id": "x.kg", "category": "GraphProduct"},
            {"id": "x.api", "category": "ProgrammingInterface"},
            {"id": "x.plain"},
        ],
    }
    assert extract_metadata_module.check_category_classes(obj, "Resource") == []


def test_check_category_classes_reports_each_bad_value(extract_metadata_module):
    obj = {
        "id": "x",
        "category": "Dataset",
        "contacts": [{"category": "Person", "label": "Someone"}],
        "products": [
            {"id": "x.kg", "category": "GraphProduct"},
            {"id": "x.portal", "category": "Portal"},
        ],
    }
    errors = extract_metadata_module.check_category_classes(obj, "Resource")
    assert len(errors) == 3
    assert errors[0].startswith("category: 'Dataset' is not a Resource class")
    assert errors[1].startswith("contacts[0].category: 'Person' is not a Contact class")
    assert errors[2].startswith("products[1].category: 'Portal' is not a Product class")
    assert "GraphicalInterface" in errors[2]


def test_validate_markdown_fails_on_off_schema_product_category(extract_metadata_module):
    with tempfile.TemporaryDirectory() as td:
        md_path = _write_resource(td, "DataSource", "DataProduct")
        args = SimpleNamespace(files=[str(md_path)], skip_publication_reference_validation=True)
        with pytest.raises(SystemExit):
            extract_metadata_module.validate_markdown(args)


def test_validate_markdown_passes_on_schema_categories(extract_metadata_module):
    with tempfile.TemporaryDirectory() as td:
        md_path = _write_resource(td, "DataSource", "Product")
        args = SimpleNamespace(files=[str(md_path)], skip_publication_reference_validation=True)
        extract_metadata_module.validate_markdown(args)
