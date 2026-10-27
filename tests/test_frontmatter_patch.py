"""Tests for minimal-diff frontmatter writes (issue #934).

The concat step used to re-dump whole resource pages with ``yaml.dump``,
re-wrapping descriptions and re-indenting lists on pages that only gained one
propagated product. ``write_frontmatter_minimal`` must leave unchanged pages
untouched and splice only the changed blocks into pages that did change.
"""

import copy
from types import SimpleNamespace

import frontmatter
import yaml

from util.frontmatter_patch import patch_frontmatter_text, write_frontmatter_minimal

# Hand-formatted page: a description wrapped at a different width than
# yaml.dump would use, four-space list indentation, and a body with a trailing
# newline. A full re-dump changes all three.
PAGE = """---
id: demo
name: Demo
category: DataSource
description: A demo resource whose description is wrapped by hand at a width that yaml.dump would not choose.
domains:
  - genomics
products:
  - category: Product
    id: demo.data
    name: Demo data
    description: Demo download, also wrapped
      by hand.
    original_source:
      - source: demo
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    id: demo.web
    name: Demo web
    original_source:
      - source: demo
        relation_type: prov:hadPrimarySource
last_modified_date: '2026-01-01T00:00:00Z'
---
# Demo

Body text.
"""


def _load(text):
    post = frontmatter.loads(text)
    return post.metadata, post.content


def _changed_lines(old, new):
    old_lines, new_lines = old.split("\n"), new.split("\n")
    return [line for line in old_lines if line not in new_lines]


def test_unchanged_page_is_not_rewritten(tmp_path):
    page = tmp_path / "demo.md"
    page.write_text(PAGE, encoding="utf-8")
    metadata, md = _load(PAGE)

    assert write_frontmatter_minimal(page, metadata, md) is False
    assert page.read_text(encoding="utf-8") == PAGE


def test_appended_product_leaves_existing_text_byte_for_byte():
    metadata, md = _load(PAGE)
    metadata["products"].append(
        {
            "category": "Product",
            "id": "other.thing",
            "name": "Other thing",
            "original_source": [{"relation_type": "prov:hadPrimarySource", "source": "demo"}],
        }
    )

    text = patch_frontmatter_text(PAGE, metadata, md)

    assert text is not None
    assert _changed_lines(PAGE, text) == []
    assert text.startswith(PAGE.split("last_modified_date")[0])
    assert "  - category: Product\n    id: other.thing" in text
    assert frontmatter.loads(text).metadata == metadata
    assert text.endswith("Body text.\n")


def test_changed_product_only_rewrites_the_changed_key():
    metadata, md = _load(PAGE)
    metadata["products"][1]["original_source"].append(
        {"relation_type": "prov:hadPrimarySource", "source": "upstream"}
    )

    text = patch_frontmatter_text(PAGE, metadata, md)

    assert text is not None
    assert frontmatter.loads(text).metadata == metadata
    # The hand-wrapped descriptions survive; only demo.web's source list changed.
    assert "description: A demo resource whose description is wrapped by hand" in text
    assert "    description: Demo download, also wrapped\n      by hand." in text
    removed = _changed_lines(PAGE, text)
    assert set(removed) <= {"      - source: demo", "        relation_type: prov:hadPrimarySource"}


def test_removed_and_new_top_level_keys():
    metadata, md = _load(PAGE)
    del metadata["domains"]
    metadata["infores_id"] = "demo"

    text = patch_frontmatter_text(PAGE, metadata, md)

    assert text is not None
    assert frontmatter.loads(text).metadata == metadata
    assert "  - genomics" not in text
    # New keys go in sorted position, like a full yaml.dump would put them.
    assert text.index("infores_id: demo") < text.index("last_modified_date")


def test_body_change_keeps_frontmatter_text():
    metadata, _ = _load(PAGE)
    text = patch_frontmatter_text(PAGE, metadata, "# Demo\n\nNew body.\n")

    assert text is not None
    assert text.split("---\n")[1] == PAGE.split("---\n")[1]
    assert text.endswith("New body.\n")


def test_unpatchable_yaml_falls_back_to_full_dump(tmp_path):
    page = tmp_path / "flow.md"
    page.write_text("---\nid: flow\nproducts: [{id: flow.a, name: A}]\n---\nBody\n", encoding="utf-8")
    metadata, md = _load(page.read_text(encoding="utf-8"))
    metadata["products"].append({"id": "flow.b", "name": "B"})

    assert write_frontmatter_minimal(page, metadata, md) is True
    assert frontmatter.load(page).metadata == metadata


def test_dedupe_keeps_warning_order(extract_metadata_module, monkeypatch, tmp_path):
    """Dropping an older duplicate warning must not re-sort the others (#934)."""
    warnings = [
        "Missing license file",
        "File was not able to be retrieved when checked on 2026-10-20: HTTP 404 error",
        "File was not able to be retrieved when checked on 2026-10-27: HTTP 404 error",
    ]
    meta = {
        "id": "demo",
        "name": "Demo",
        "category": "DataSource",
        "domains": ["genomics"],
        "products": [{"id": "demo.data", "name": "Demo data", "category": "Product", "warnings": warnings}],
    }
    resource_dir = tmp_path / "resource" / "demo"
    resource_dir.mkdir(parents=True)
    page = resource_dir / "demo.md"
    page.write_text("---\n" + yaml.safe_dump(meta, sort_keys=False) + "---\n# Demo\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    extract_metadata_module.concat_resource_yaml(
        SimpleNamespace(files=[str(page)], include=None, output=str(tmp_path / "out.yml"))
    )

    persisted = frontmatter.load(page).metadata["products"][0]["warnings"]
    assert persisted == [warnings[0], warnings[2]]


def test_concat_is_idempotent(extract_metadata_module, monkeypatch, tmp_path):
    """A second concat run changes nothing, and the first touches only pages that gained a product."""
    resource_root = tmp_path / "resource"

    def _write(resource_id, text):
        d = resource_root / resource_id
        d.mkdir(parents=True)
        (d / f"{resource_id}.md").write_text(text, encoding="utf-8")
        return d / f"{resource_id}.md"

    source = _write("demo", PAGE)
    unrelated_text = PAGE.replace("demo", "lonely").replace("Demo", "Lonely")
    unrelated = _write("lonely", unrelated_text)
    derived_meta = {
        "id": "derived",
        "name": "Derived",
        "category": "KnowledgeGraph",
        "domains": ["genomics"],
        "products": [
            {
                "id": "derived.graph",
                "name": "Derived graph",
                "category": "GraphProduct",
                "original_source": [{"relation_type": "prov:hadPrimarySource", "source": "demo"}],
            }
        ],
    }
    derived = _write("derived", "---\n" + yaml.safe_dump(derived_meta, sort_keys=False) + "---\n# Derived\n")
    monkeypatch.chdir(tmp_path)

    def _run():
        files = sorted(str(p) for p in resource_root.rglob("*.md"))
        extract_metadata_module.concat_resource_yaml(
            SimpleNamespace(files=files, include=None, output=str(tmp_path / "out.yml"))
        )
        return {p: p.read_text(encoding="utf-8") for p in sorted(resource_root.rglob("*.md"))}

    first = _run()
    # The unrelated page neither owns a new product nor receives one.
    assert unrelated.read_text(encoding="utf-8") == unrelated_text
    # The source page gained derived.graph without reflowing its own text.
    source_text = source.read_text(encoding="utf-8")
    assert "derived.graph" in source_text
    assert _changed_lines(PAGE, source_text) == []

    second = _run()
    assert second == first
    assert derived.exists()
