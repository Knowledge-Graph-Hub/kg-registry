"""Test extract-metadata helpers used for product page generation and propagation."""

from types import SimpleNamespace

import frontmatter
import yaml


def test_sanitize_product_for_page_preserves_source_product(extract_metadata_module):
    product = {
        "id": "demo.download",
        "warnings": ["File was not able to be retrieved when checked on 2026-03-30: timeout"],
    }

    sanitized = extract_metadata_module.sanitize_product_for_page(product)

    assert sanitized["warnings"] == [
        "File was not able to be retrieved when checked on 2026-03-30_ timeout"
    ]
    assert product["warnings"] == [
        "File was not able to be retrieved when checked on 2026-03-30: timeout"
    ]


def test_concat_propagates_cross_resource_products(
    extract_metadata_module,
    monkeypatch,
    tmp_path,
):
    def _write_resource(resource_id, metadata):
        resource_dir = tmp_path / "resource" / resource_id
        resource_dir.mkdir(parents=True)
        resource_path = resource_dir / f"{resource_id}.md"
        with resource_path.open("w", encoding="utf-8") as handle:
            handle.write("---\n")
            yaml.safe_dump(metadata, handle, sort_keys=False)
            handle.write("---\n")
            handle.write(f"\n# {metadata['name']}\n")
        return resource_path

    bto_path = _write_resource(
        "bto",
        {
            "id": "bto",
            "name": "BTO",
            "description": "BTO resource",
            "category": "Ontology",
            "domains": ["anatomy and development"],
            "products": [
                {
                    "id": "bto.owl",
                    "name": "bto.owl",
                    "category": "OntologyProduct",
                    "format": "owl",
                    "description": "Primary BTO ontology file",
                }
            ],
        },
    )
    bioteque_path = _write_resource(
        "bioteque",
        {
            "id": "bioteque",
            "name": "Bioteque",
            "description": "Bioteque resource",
            "category": "KnowledgeGraph",
            "domains": ["general"],
            "products": [
                {
                    "id": "bioteque.embeddings",
                    "name": "Bioteque embeddings",
                    "category": "GraphEmbeddingProduct",
                    "description": "Embeddings built using BTO",
                    "original_source": [
                        {"source": "bto", "relation_type": "prov:hadPrimarySource"}
                    ],
                }
            ],
        },
    )
    clinicalkg_path = _write_resource(
        "clinicalkg",
        {
            "id": "clinicalkg",
            "name": "ClinicalKG",
            "description": "ClinicalKG resource",
            "category": "KnowledgeGraph",
            "domains": ["clinical and phenotypic"],
            "products": [
                {
                    "id": "clinicalkg.graph",
                    "name": "ClinicalKG graph",
                    "category": "KnowledgeGraphProduct",
                    "description": "Graph with the BTO ontology product as a secondary source",
                    "secondary_source": [
                        {"source": "bto.owl", "relation_type": "prov:wasInfluencedBy"}
                    ],
                }
            ],
        },
    )

    monkeypatch.chdir(tmp_path)
    output_path = tmp_path / "unsorted.yml"

    cfg = extract_metadata_module.concat_resource_yaml(
        SimpleNamespace(
            files=[str(bto_path), str(bioteque_path), str(clinicalkg_path)],
            include=None,
            output=str(output_path),
        )
    )

    bto_resource = next(resource for resource in cfg["resources"] if resource["id"] == "bto")
    propagated_ids = {product["id"] for product in bto_resource["products"]}
    assert "bioteque.embeddings" in propagated_ids
    assert "clinicalkg.graph" in propagated_ids

    bto_metadata = frontmatter.load(bto_path).metadata
    persisted_ids = {product["id"] for product in bto_metadata["products"]}
    assert "bioteque.embeddings" in persisted_ids
    assert "clinicalkg.graph" in persisted_ids


def test_product_pages_are_written_only_under_the_owning_resource(
    extract_metadata_module,
    monkeypatch,
    tmp_path,
):
    """A product's detail page belongs to its owner, not to every page listing it.

    `goa.ftp` is owned by `goa` and propagated onto `go` because it cites `go` as
    a source. `go` is a string prefix of `goa`, so a bare `startswith` ownership
    test would also write the page under `resource/go/`.
    """

    def _write_resource(resource_id, metadata):
        resource_dir = tmp_path / "resource" / resource_id
        resource_dir.mkdir(parents=True)
        resource_path = resource_dir / f"{resource_id}.md"
        with resource_path.open("w", encoding="utf-8") as handle:
            handle.write("---\n")
            yaml.safe_dump(metadata, handle, sort_keys=False)
            handle.write("---\n")
            handle.write(f"\n# {metadata['name']}\n")
        return resource_path

    go_path = _write_resource(
        "go",
        {
            "id": "go",
            "name": "GO",
            "description": "Gene Ontology",
            "category": "Ontology",
            "domains": ["biological systems"],
            "products": [
                {
                    "id": "go.owl",
                    "name": "go.owl",
                    "category": "OntologyProduct",
                    "format": "owl",
                    "description": "GO in OWL",
                }
            ],
        },
    )
    goa_path = _write_resource(
        "goa",
        {
            "id": "goa",
            "name": "GOA",
            "description": "GO Annotation",
            "category": "DataSource",
            "domains": ["biological systems"],
            "products": [
                {
                    "id": "goa.ftp",
                    "name": "GOA FTP",
                    "category": "Product",
                    "format": "gaf",
                    "description": "GOA annotation files",
                    "original_source": [{"source": "go", "relation_type": "prov:hadPrimarySource"}],
                }
            ],
        },
    )

    monkeypatch.chdir(tmp_path)
    extract_metadata_module.concat_resource_yaml(
        SimpleNamespace(
            files=[str(go_path), str(goa_path)],
            include=None,
            output=str(tmp_path / "unsorted.yml"),
        )
    )

    # goa.ftp did propagate onto the go page ...
    go_metadata = frontmatter.load(go_path).metadata
    assert "goa.ftp" in {product["id"] for product in go_metadata["products"]}

    # ... but its detail page exists only under its owner.
    assert (tmp_path / "resource" / "goa" / "goa.ftp.md").exists()
    assert not (tmp_path / "resource" / "go" / "goa.ftp.md").exists()
    assert (tmp_path / "resource" / "go" / "go.owl.md").exists()


def test_concat_reaps_pages_for_products_that_no_longer_exist(
    extract_metadata_module,
    monkeypatch,
    tmp_path,
):
    """Renamed or dropped products must not leave their page behind.

    A page with hand-written content is reported and kept: the generator only ever
    writes frontmatter, so a body means someone edited it.
    """
    resource_dir = tmp_path / "resource" / "demo"
    resource_dir.mkdir(parents=True)
    resource_path = resource_dir / "demo.md"
    with resource_path.open("w", encoding="utf-8") as handle:
        handle.write("---\n")
        yaml.safe_dump(
            {
                "id": "demo",
                "name": "Demo",
                "description": "Demo resource",
                "category": "DataSource",
                "domains": ["general"],
                "products": [
                    {
                        "id": "demo.current",
                        "name": "Current",
                        "category": "Product",
                        "format": "tsv",
                        "description": "Still listed",
                    }
                ],
            },
            handle,
            sort_keys=False,
        )
        handle.write("---\n\n# Demo\n")

    def _write_page(product_id, body=""):
        path = resource_dir / f"{product_id}.md"
        path.write_text(
            f"---\nid: {product_id}\nname: {product_id}\nlayout: product_detail\n---\n{body}",
            encoding="utf-8",
        )
        return path

    stale = _write_page("demo.renamed-away")
    curated = _write_page("demo.hand-edited", body="\nCurated notes worth keeping.\n")
    eval_page = resource_dir / "demo_eval_automated.md"
    eval_page.write_text("---\nid: demo\nlayout: eval_detail\n---\n", encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    extract_metadata_module.concat_resource_yaml(
        SimpleNamespace(
            files=[str(resource_path)],
            include=None,
            output=str(tmp_path / "unsorted.yml"),
        )
    )

    assert not stale.exists(), "page for a dropped product should be reaped"
    assert curated.exists(), "page with hand-written content should be left alone"
    assert eval_page.exists(), "only product_detail pages are swept"
    assert (resource_dir / "demo.current.md").exists()
    assert resource_path.exists()


def test_reaper_ignores_resources_outside_the_processed_set(
    extract_metadata_module,
    monkeypatch,
    tmp_path,
):
    """A concat over a subset of files must not reap pages it never looked at."""
    for resource_id in ("alpha", "beta"):
        resource_dir = tmp_path / "resource" / resource_id
        resource_dir.mkdir(parents=True)
        with (resource_dir / f"{resource_id}.md").open("w", encoding="utf-8") as handle:
            handle.write("---\n")
            yaml.safe_dump(
                {
                    "id": resource_id,
                    "name": resource_id,
                    "description": f"{resource_id} resource",
                    "category": "DataSource",
                    "domains": ["general"],
                    "products": [],
                },
                handle,
                sort_keys=False,
            )
            handle.write("---\n")
        (resource_dir / f"{resource_id}.orphan.md").write_text(
            f"---\nid: {resource_id}.orphan\nlayout: product_detail\n---\n", encoding="utf-8"
        )

    monkeypatch.chdir(tmp_path)
    extract_metadata_module.concat_resource_yaml(
        SimpleNamespace(
            files=[str(tmp_path / "resource" / "alpha" / "alpha.md")],
            include=None,
            output=str(tmp_path / "unsorted.yml"),
        )
    )

    assert not (tmp_path / "resource" / "alpha" / "alpha.orphan.md").exists()
    assert (tmp_path / "resource" / "beta" / "beta.orphan.md").exists()


def test_validate_markdown_skips_pages_reaped_during_the_build(
    extract_metadata_module,
    tmp_path,
    capsys,
):
    """The build's file list is a snapshot, so it can name a page the concat reaped.

    tmp/resource-files.txt is written by `find` before the concat runs, and the
    concat deletes the page for any product its resource no longer lists. Reading
    the snapshot afterwards used to blow up with FileNotFoundError and fail the
    whole registry build.
    """
    reaped = tmp_path / "resource" / "alpha" / "alpha.reaped.md"

    extract_metadata_module.validate_markdown(SimpleNamespace(files=[str(reaped)]))

    assert "no longer present" in capsys.readouterr().out


def test_prettify_skips_pages_reaped_during_the_build(
    extract_metadata_module,
    tmp_path,
    capsys,
):
    """prettify reads the same snapshot, so it needs the same tolerance."""
    reaped = tmp_path / "resource" / "alpha" / "alpha.reaped.md"

    extract_metadata_module.prettify(SimpleNamespace(files=[str(reaped)]))

    assert "no longer present" in capsys.readouterr().out
