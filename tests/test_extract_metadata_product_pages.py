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
                    "original_source": [{"source": "bto", "relation_type": "prov:hadPrimarySource"}],
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
                    "secondary_source": [{"source": "bto.owl", "relation_type": "prov:wasInfluencedBy"}],
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
