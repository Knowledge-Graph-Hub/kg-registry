"""Non-ASCII text in frontmatter must be written as literal UTF-8, not escaped.

PyYAML's ``yaml.dump`` escapes every non-ASCII character unless it is given
``allow_unicode=True``, so a rewrite turned ``Anja Füllgrabe`` into
``"Anja F\\xFCllgrabe"``. The values still parsed back the same, but the files
became hard to read and every regeneration produced noisy diffs (issue #759).
"""

import re
from pathlib import Path
from types import SimpleNamespace

import frontmatter
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
ESCAPED_NON_ASCII = re.compile(r"\\x[0-9A-Fa-f]{2}|\\u[0-9A-Fa-f]{4}|\\U[0-9A-Fa-f]{8}")

AUTHOR = "Anja Füllgrabe"
EN_DASH_DESCRIPTION = "Curated drug–disease paths"
NBSP_AUTHOR = "Nicole E. Bodycombe"


def _frontmatter_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    return text[4 : text.index("\n---", 4) + 1]


def _write_resource(root: Path, resource_id: str, metadata: dict) -> Path:
    resource_dir = root / "resource" / resource_id
    resource_dir.mkdir(parents=True)
    resource_path = resource_dir / f"{resource_id}.md"
    with resource_path.open("w", encoding="utf-8") as handle:
        handle.write("---\n")
        yaml.safe_dump(metadata, handle, sort_keys=False, allow_unicode=True)
        handle.write("---\n")
        handle.write(f"\n# {metadata['name']}\n")
    return resource_path


def test_concat_writes_non_ascii_frontmatter_unescaped(
    extract_metadata_module,
    monkeypatch,
    tmp_path,
):
    upstream_path = _write_resource(
        tmp_path,
        "upstream",
        {
            "id": "upstream",
            "name": "Upstream",
            "description": "Upstream resource",
            "category": "DataSource",
            "domains": ["general"],
            "products": [
                {
                    "id": "upstream.data",
                    "name": "Upstream data",
                    "category": "Product",
                    "description": "Upstream data file",
                }
            ],
            "publications": [
                {
                    "id": "doi:10.1234/example",
                    "title": "Example",
                    "authors": [AUTHOR, NBSP_AUTHOR],
                }
            ],
        },
    )
    downstream_path = _write_resource(
        tmp_path,
        "downstream",
        {
            "id": "downstream",
            "name": "Downstream",
            "description": "Downstream resource",
            "category": "KnowledgeGraph",
            "domains": ["general"],
            "products": [
                {
                    "id": "downstream.graph",
                    "name": "Downstream graph",
                    "category": "GraphProduct",
                    "description": EN_DASH_DESCRIPTION,
                    "original_source": [
                        {"source": "upstream", "relation_type": "prov:hadPrimarySource"}
                    ],
                }
            ],
        },
    )

    monkeypatch.chdir(tmp_path)
    output_path = tmp_path / "unsorted.yml"
    extract_metadata_module.concat_resource_yaml(
        SimpleNamespace(
            files=[str(upstream_path), str(downstream_path)],
            include=None,
            output=str(output_path),
        )
    )

    # The upstream page is rewritten to carry the propagated downstream product.
    upstream_fm = _frontmatter_text(upstream_path)
    assert "downstream.graph" in upstream_fm
    assert AUTHOR in upstream_fm
    assert EN_DASH_DESCRIPTION in upstream_fm
    assert NBSP_AUTHOR in upstream_fm
    assert not ESCAPED_NON_ASCII.search(upstream_fm)
    assert frontmatter.load(upstream_path).metadata["publications"][0]["authors"] == [
        AUTHOR,
        NBSP_AUTHOR,
    ]

    # Generated product pages are written the same way.
    product_page = tmp_path / "resource" / "downstream" / "downstream.graph.md"
    product_fm = _frontmatter_text(product_page)
    assert EN_DASH_DESCRIPTION in product_fm
    assert not ESCAPED_NON_ASCII.search(product_fm)

    # So is the combined YAML output.
    output_text = output_path.read_text(encoding="utf-8")
    assert AUTHOR in output_text
    assert not ESCAPED_NON_ASCII.search(output_text)


def test_resource_pages_have_no_escaped_non_ascii_frontmatter():
    offenders = []
    for path in sorted((REPO_ROOT / "resource").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---", 4)
        if end == -1:
            continue
        match = ESCAPED_NON_ASCII.search(text[4:end])
        if match:
            offenders.append(f"{path.relative_to(REPO_ROOT)}: {match.group(0)}")

    assert not offenders, (
        "Frontmatter contains escaped non-ASCII characters; write YAML with "
        "allow_unicode=True and keep the characters as literal UTF-8:\n" + "\n".join(offenders[:20])
    )
