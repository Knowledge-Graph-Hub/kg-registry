"""Tests for OBO Foundry sync merge behavior."""

import frontmatter

from util.sync_obo_foundry import OBOFoundrySync


def test_merge_resource_metadata_preserves_curated_fields_and_products(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    existing = {
        "id": "go",
        "infores_id": "go",
        "synonyms": ["GO"],
        "domains": ["biomedical"],
        "contacts": [
            {
                "category": "Organization",
                "label": "Gene Ontology Consortium",
                "contact_details": [
                    {"contact_type": "url", "value": "https://geneontology.org/"}
                ],
            }
        ],
        "products": [
            {
                "id": "go.owl",
                "name": "GO (OWL edition)",
                "category": "OntologyProduct",
                "product_file_size": 123,
                "warnings": ["cached warning"],
            },
            {
                "id": "go.api",
                "name": "Gene Ontology API",
                "category": "ProgrammingInterface",
                "product_url": "https://api.geneontology.org/",
            },
        ],
    }
    synced = {
        "id": "go",
        "name": "Gene Ontology",
        "description": "An ontology for describing the function of genes and gene products",
        "homepage_url": "http://geneontology.org/",
        "activity_status": "active",
        "category": "Ontology",
        "layout": "resource_detail",
        "collection": ["obo-foundry"],
        "domains": ["biological systems"],
        "contacts": [
            {
                "category": "Individual",
                "label": "Suzi Aleksander",
                "contact_details": [
                    {"contact_type": "email", "value": "suzia@stanford.edu"}
                ],
            }
        ],
        "products": [
            {
                "id": "go.owl",
                "name": "GO (OWL edition)",
                "description": "The main ontology in OWL",
                "category": "OntologyProduct",
                "product_url": "http://purl.obolibrary.org/obo/go.owl",
                "format": "owl",
            }
        ],
    }

    merged = syncer.merge_resource_metadata(existing, synced)
    merged_products = {product["id"]: product for product in merged["products"]}

    assert merged["infores_id"] == "go"
    assert merged["synonyms"] == ["GO"]
    assert merged["domains"] == ["biomedical", "biological systems"]
    assert len(merged["contacts"]) == 2
    assert set(merged_products) == {"go.owl", "go.api"}
    assert merged_products["go.owl"]["product_file_size"] == 123
    assert merged_products["go.owl"]["warnings"] == ["cached warning"]
    assert merged_products["go.owl"]["product_url"] == "http://purl.obolibrary.org/obo/go.owl"


def test_sync_ontology_preserves_curated_body_and_extra_metadata(tmp_path):
    registry_root = tmp_path / "resource"
    resource_dir = registry_root / "go"
    resource_dir.mkdir(parents=True)
    resource_path = resource_dir / "go.md"
    resource_path.write_text(
        """---
id: go
name: Gene Ontology
infores_id: go
creation_date: '2025-03-16T00:00:00Z'
last_modified_date: '2026-04-10T00:00:00Z'
products:
- id: go.api
  name: Gene Ontology API
  category: ProgrammingInterface
  product_url: https://api.geneontology.org/
---
# Curated Notes

Keep this body.
""",
        encoding="utf-8",
    )

    syncer = OBOFoundrySync(registry_root=str(registry_root))
    syncer.sync_ontology(
        {
            "id": "go",
            "title": "Gene Ontology",
            "description": "An ontology for describing the function of genes and gene products",
            "homepage": "http://geneontology.org/",
            "domain": "biological systems",
            "products": [
                {
                    "id": "owl",
                    "title": "GO (OWL edition)",
                    "ontology_purl": "http://purl.obolibrary.org/obo/go.owl",
                    "format": "owl",
                }
            ],
        }
    )

    post = frontmatter.load(resource_path)
    products = {product["id"]: product for product in post.metadata["products"]}

    assert post.metadata["infores_id"] == "go"
    assert post.metadata["creation_date"] == "2025-03-16T00:00:00Z"
    assert post.metadata["last_modified_date"] == syncer._today_iso()
    assert set(products) == {"go.api", "go.owl"}
    assert "Keep this body." in post.content
