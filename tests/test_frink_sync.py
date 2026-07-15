"""Test FRINK registry transformation and merge behavior."""

import copy

from util.sync_frink import SHORTNAME_ALIASES

def test_transform_frink_entry_to_resource(frink_syncer, frink_entry_example):
    resource = frink_syncer.transform_frink_to_kg_registry(frink_entry_example)

    assert resource["id"] == "prokn"
    assert resource["name"] == "Protein Knowledge Network"
    assert resource["description"] == "Protein-centric graph."
    assert resource["homepage_url"] == "https://example.org/prokn"
    assert resource["category"] == "KnowledgeGraph"
    assert resource["collection"] == ["okn"]
    assert resource["domains"] == ["general"]
    assert resource["contacts"] == [
        {
            "category": "Individual",
            "label": "Chuming Chen",
            "contact_details": [
                {"contact_type": "email", "value": "chenc@udel.edu"},
                {"contact_type": "github", "value": "chenchuming"},
            ],
        }
    ]
    assert resource["products"] == [
        {
            "id": "prokn.sparql",
            "name": "Protein Knowledge Network SPARQL",
            "description": "SPARQL endpoint for Protein Knowledge Network",
            "category": "ProgrammingInterface",
            "product_url": "https://frink.apps.renci.org/prokn/sparql",
            "original_source": [{"source": "prokn", "relation_type": "prov:hadPrimarySource"}],
        },
        {
            "id": "prokn.tpf",
            "name": "Protein Knowledge Network TPF",
            "description": "Triple Pattern Fragments endpoint for Protein Knowledge Network",
            "category": "ProgrammingInterface",
            "product_url": "https://frink.apps.renci.org/ldf/prokn",
            "original_source": [{"source": "prokn", "relation_type": "prov:hadPrimarySource"}],
        },
    ]


def test_merge_preserves_existing_graph_products_and_adds_frink_endpoints(
    frink_syncer,
    frink_existing_resource_example,
    frink_synced_resource_example,
):
    merged = frink_syncer.merge_resource_metadata(
        frink_existing_resource_example,
        frink_synced_resource_example,
    )

    assert merged["name"] == "Protein Knowledge Network"
    assert merged["description"] == "Protein-centric graph."
    assert merged["homepage_url"] == "https://example.org/prokn"
    assert merged["domains"] == ["proteomics"]
    assert len(merged["contacts"]) == 2

    merged_products = {product["id"]: product for product in merged["products"]}
    assert set(merged_products) == {"prokn.graph", "prokn.sparql", "prokn.tpf"}
    assert merged_products["prokn.graph"]["category"] == "GraphProduct"
    assert merged_products["prokn.sparql"]["product_url"] == "https://frink.apps.renci.org/prokn/sparql"
    assert merged_products["prokn.sparql"]["original_source"] == [
        {"source": "prokn", "relation_type": "prov:hadPrimarySource"}
    ]
    assert merged_products["prokn.tpf"]["product_url"] == "https://frink.apps.renci.org/ldf/prokn"


def test_merge_backfills_missing_domains_from_frink_sync(
    frink_syncer,
    frink_existing_resource_example,
    frink_synced_resource_example,
):
    existing_without_domains = copy.deepcopy(frink_existing_resource_example)
    existing_without_domains.pop("domains", None)

    merged = frink_syncer.merge_resource_metadata(
        existing_without_domains,
        frink_synced_resource_example,
    )

    assert merged["domains"] == ["general"]


def test_aliased_shortname_transforms_to_canonical_id(frink_syncer):
    """A FRINK shortname aliased to a merged resource resolves to the canonical id."""
    assert SHORTNAME_ALIASES.get("biomarkerkg") == "biomarker"

    entry = {
        "shortname": "biomarkerkg",
        "title": "BiomarkerKB KG",
        "description": "The BiomarkerKB knowledge graph.",
        "homepage": "https://biomarkerkb.org/home/",
        "sparql": "https://apps.okn.us/biomarkerkg/sparql",
        "tpf": "https://apps.okn.us/ldf/biomarkerkg",
        "contact": {"label": "Jeet Vora", "email": "jeetvora@gwu.edu", "github": "jeet-vora"},
    }
    resource = frink_syncer.transform_frink_to_kg_registry(entry)

    # Targets the canonical resource, not a new "biomarkerkg" directory.
    assert resource["id"] == "biomarker"
    # Endpoint product ids use the canonical id so they merge in place.
    assert {p["id"] for p in resource["products"]} == {"biomarker.sparql", "biomarker.tpf"}


def test_merge_preserve_identity_keeps_canonical_fields(
    frink_syncer, frink_existing_resource_example
):
    """When a FRINK entry is aliased onto a curated resource, its identity fields
    (name/description/homepage) must not be overwritten, but products still merge."""
    synced = {
        "id": "prokn",
        "name": "BiomarkerKB KG",
        "description": "Different description from the merged duplicate.",
        "homepage_url": "https://biomarkerkb.org/home/",
        "activity_status": "active",
        "products": [
            {
                "id": "prokn.sparql",
                "name": "BiomarkerKB KG SPARQL",
                "description": "SPARQL endpoint for BiomarkerKB KG",
                "category": "ProgrammingInterface",
                "product_url": "https://apps.okn.us/biomarkerkg/sparql",
                "original_source": [{"source": "prokn", "relation_type": "prov:hadPrimarySource"}],
            }
        ],
    }

    merged = frink_syncer.merge_resource_metadata(
        frink_existing_resource_example, synced, preserve_identity=True
    )

    # Canonical identity preserved.
    assert merged["name"] == "Old ProKN"
    assert merged["description"] == "Old description."
    assert merged["homepage_url"] == "https://old.example.org"
    # Products still merged (endpoint url updated in place, no duplicate).
    merged_products = {p["id"]: p for p in merged["products"]}
    assert set(merged_products) == {"prokn.graph", "prokn.sparql"}
    assert merged_products["prokn.sparql"]["product_url"] == "https://apps.okn.us/biomarkerkg/sparql"


def test_merge_without_preserve_identity_still_overwrites(
    frink_syncer, frink_existing_resource_example
):
    """Non-aliased entries keep the original overwrite behavior."""
    synced = {
        "id": "prokn",
        "name": "New Name",
        "description": "New description.",
        "homepage_url": "https://new.example.org",
    }
    merged = frink_syncer.merge_resource_metadata(
        frink_existing_resource_example, synced, preserve_identity=False
    )
    assert merged["name"] == "New Name"
    assert merged["description"] == "New description."
    assert merged["homepage_url"] == "https://new.example.org"
