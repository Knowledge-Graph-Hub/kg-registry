"""Tests for OBO Foundry sync merge behavior."""

import frontmatter
import pytest

from util.sync_obo_foundry import OBOFoundrySync


def test_merge_resource_metadata_preserves_curated_fields_products_and_publications(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    existing = {
        "id": "go",
        "infores_id": "go",
        "synonyms": ["GO"],
        "domains": ["biomedical"],
        "publications": [
            {
                "id": "PMID:10802651",
                "title": "Original title",
                "preferred": True,
            }
        ],
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
        "publications": [
            {
                "id": "PMID:10802651",
                "title": "Gene ontology: tool for the unification of biology. The Gene Ontology Consortium",
            },
            {
                "id": "https://doi.org/10.1093/nar/gkaf1271",
                "title": "The Gene Ontology resource: enriching a GOld mine",
            },
        ],
    }

    merged = syncer.merge_resource_metadata(existing, synced)
    merged_products = {product["id"]: product for product in merged["products"]}
    merged_publications = {publication["id"]: publication for publication in merged["publications"]}

    assert merged["infores_id"] == "go"
    assert merged["synonyms"] == ["GO"]
    assert merged["domains"] == ["biomedical", "biological systems"]
    assert len(merged["contacts"]) == 2
    assert set(merged_products) == {"go.owl", "go.api"}
    assert merged_products["go.owl"]["product_file_size"] == 123
    assert merged_products["go.owl"]["warnings"] == ["cached warning"]
    assert merged_products["go.owl"]["product_url"] == "http://purl.obolibrary.org/obo/go.owl"
    assert set(merged_publications) == {"PMID:10802651", "https://doi.org/10.1093/nar/gkaf1271"}
    assert merged_publications["PMID:10802651"]["preferred"] is True
    assert (
        merged_publications["PMID:10802651"]["title"]
        == "Gene ontology: tool for the unification of biology. The Gene Ontology Consortium"
    )


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


@pytest.mark.parametrize(
    ("raw_identifier", "expected"),
    [
        ("https://www.ncbi.nlm.nih.gov/pubmed/10802651", "https://www.ncbi.nlm.nih.gov/pubmed/10802651"),
        ("10.1093/nar/gkaf1271", "doi:10.1093/nar/gkaf1271"),
        ("10802651", "PMID:10802651"),
        (10802651, "PMID:10802651"),
    ],
)
def test_normalize_publication_id(raw_identifier, expected, tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    assert syncer._normalize_publication_id(raw_identifier) == expected


def test_transform_obo_to_kg_registry_emits_publication_ids(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    resource = syncer.transform_obo_to_kg_registry(
        {
            "id": "go",
            "title": "Gene Ontology",
            "publications": [
                {"id": "https://www.ncbi.nlm.nih.gov/pubmed/10802651", "title": "PubMed paper"},
                {"id": "10.1093/nar/gkaf1271", "title": "DOI paper"},
                {"id": "10802651", "title": "Numeric PMID"},
            ],
        }
    )

    assert resource["publications"] == [
        {"id": "https://www.ncbi.nlm.nih.gov/pubmed/10802651", "title": "PubMed paper"},
        {"id": "doi:10.1093/nar/gkaf1271", "title": "DOI paper"},
        {"id": "PMID:10802651", "title": "Numeric PMID"},
    ]


def test_merge_products_excludes_configured_product_ids(tmp_path):
    """Products listed in the exclusions config must never be (re-)added."""
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    # Inject an exclusion rather than depending on the shipped config file.
    syncer.product_exclusions = {"pcl": {"pcl.json", "pcl-base.owl"}}

    existing = [{"id": "pcl.owl"}, {"id": "pcl.obo"}]
    # The OBO registry advertises variant products that do not resolve.
    synced = [
        {"id": "pcl.owl"},
        {"id": "pcl.obo"},
        {"id": "pcl.json"},
        {"id": "pcl-base.owl"},
    ]

    merged = syncer.merge_products(
        existing, synced, excluded_ids=syncer.product_exclusions["pcl"]
    )
    merged_ids = {p["id"] for p in merged}
    assert merged_ids == {"pcl.owl", "pcl.obo"}


def test_merge_products_strips_excluded_existing_products(tmp_path):
    """An excluded product already present is removed (and not re-synced)."""
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    excluded = {"t4fs-community.owl"}

    existing = [{"id": "t4fs.owl"}, {"id": "t4fs-community.owl"}]
    synced = [{"id": "t4fs.owl"}, {"id": "t4fs-community.owl"}]

    merged = syncer.merge_products(existing, synced, excluded_ids=excluded)
    assert {p["id"] for p in merged} == {"t4fs.owl"}
