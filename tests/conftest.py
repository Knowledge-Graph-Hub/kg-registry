import copy

import pytest

from util.sync_frink import FRINKSync


@pytest.fixture
def frink_syncer():
    return FRINKSync(cache_ttl_hours=1)


@pytest.fixture
def frink_entry_example():
    return {
        "shortname": "prokn",
        "title": "Protein Knowledge Network",
        "description": "Protein-centric graph.",
        "homepage": "https://example.org/prokn",
        "sparql": "https://frink.apps.renci.org/prokn/sparql",
        "tpf": "https://frink.apps.renci.org/ldf/prokn",
        "contact": {
            "label": "Chuming Chen",
            "email": "chenc@udel.edu",
            "github": "chenchuming",
        },
        "frink-options": {"documentation-path": "prokn"},
    }


@pytest.fixture
def frink_existing_resource_example():
    return {
        "id": "prokn",
        "name": "Old ProKN",
        "description": "Old description.",
        "homepage_url": "https://old.example.org",
        "category": "KnowledgeGraph",
        "layout": "resource_detail",
        "collection": ["okn"],
        "domains": ["proteomics"],
        "products": [
            {
                "id": "prokn.graph",
                "name": "ProKN Graph Export",
                "description": "CSV dump",
                "category": "GraphProduct",
                "format": "csv",
                "product_url": "https://example.org/prokn.csv",
            },
            {
                "id": "prokn.sparql",
                "name": "Legacy SPARQL",
                "description": "Old endpoint description",
                "category": "ProgrammingInterface",
                "product_url": "https://old.example.org/sparql",
                "original_source": ["prokn", "legacy"],
            },
        ],
        "contacts": [
            {
                "category": "Individual",
                "label": "Legacy Contact",
                "contact_details": [{"contact_type": "email", "value": "legacy@example.org"}],
            }
        ],
    }


@pytest.fixture
def frink_synced_resource_example(frink_entry_example, frink_syncer):
    return copy.deepcopy(frink_syncer.transform_frink_to_kg_registry(frink_entry_example))
