"""Test the shared parallel markdown loader used by extract-metadata."""

from pathlib import Path

from util.parallel_loader import filter_library_files, load_md_parallel


def test_load_md_parallel_reads_frontmatter(tmp_path):
    resource_dir = tmp_path / "demo"
    resource_dir.mkdir()
    resource_file = resource_dir / "demo.md"
    resource_file.write_text(
        "---\n"
        "id: demo\n"
        "name: Demo Resource\n"
        "---\n"
        "Demo body\n",
        encoding="utf-8",
    )

    results = load_md_parallel([str(resource_file)], max_workers=2)

    assert len(results) == 1
    filename, metadata, content = results[0]
    assert Path(filename) == resource_file
    assert metadata["id"] == "demo"
    assert metadata["name"] == "Demo Resource"
    assert content.strip() == "Demo body"


def test_filter_library_files_keeps_main_resource_pages():
    results = [
        ("resource/demo/demo.md", {"id": "demo", "name": "Demo"}, "body"),
        ("resource/demo/demo.sparql.md", {"id": "demo.sparql", "name": "Demo SPARQL"}, "body"),
    ]

    filtered = filter_library_files(results)

    assert filtered == [({"id": "demo", "name": "Demo"}, "body")]
