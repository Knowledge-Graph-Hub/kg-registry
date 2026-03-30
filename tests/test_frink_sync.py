"""Test FRINK registry transformation and merge behavior."""

def test_transform_frink_entry_to_resource(frink_syncer, frink_entry_example):
    resource = frink_syncer.transform_frink_to_kg_registry(frink_entry_example)

    assert resource["id"] == "prokn"
    assert resource["name"] == "Protein Knowledge Network"
    assert resource["description"] == "Protein-centric graph."
    assert resource["homepage_url"] == "https://example.org/prokn"
    assert resource["category"] == "KnowledgeGraph"
    assert resource["collection"] == ["okn"]
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
            "original_source": ["prokn"],
        },
        {
            "id": "prokn.tpf",
            "name": "Protein Knowledge Network TPF",
            "description": "Triple Pattern Fragments endpoint for Protein Knowledge Network",
            "category": "ProgrammingInterface",
            "product_url": "https://frink.apps.renci.org/ldf/prokn",
            "original_source": ["prokn"],
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
    assert merged_products["prokn.sparql"]["original_source"] == ["prokn"]
    assert merged_products["prokn.tpf"]["product_url"] == "https://frink.apps.renci.org/ldf/prokn"
