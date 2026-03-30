from pathlib import Path

import pytest
import yaml


@pytest.fixture
def parquet_backend_sample_data():
    return {
        "resources": [
            {
                "id": "test-resource-1",
                "name": "Test Resource 1",
                "description": "A test resource for Parquet testing",
                "category": "TestCategory",
                "activity_status": "active",
                "homepage_url": "https://example.com/test1",
                "repository": "https://github.com/test/test1",
                "creation_date": "2023-01-01T00:00:00Z",
                "last_modified_date": "2023-12-01T00:00:00Z",
                "license": {"id": "MIT", "label": "MIT License"},
                "domains": ["test", "example"],
                "contacts": [
                    {
                        "category": "Individual",
                        "label": "Test Person",
                        "contact_details": [
                            {"contact_type": "email", "value": "test@example.com"}
                        ],
                    }
                ],
                "products": [
                    {
                        "id": "test-resource-1.product1",
                        "name": "Test Product 1",
                        "category": "GraphProduct",
                        "description": "Test product description",
                        "format": "csv",
                        "product_url": "https://example.com/product1",
                    }
                ],
                "layout": "resource_detail",
            },
            {
                "id": "test-resource-2",
                "name": "Test Resource 2",
                "description": "Another test resource",
                "category": "AnotherCategory",
                "activity_status": "inactive",
                "homepage_url": "https://example.com/test2",
                "domains": ["test"],
                "license": "Apache-2.0",
                "products": [],
            },
        ]
    }


@pytest.fixture
def parquet_backend_taxa_data():
    return {
        "resources": [
            {
                "id": "test-resource-1",
                "name": "Test Resource 1",
                "description": "A test resource with taxa",
                "category": "TestCategory",
                "activity_status": "active",
                "homepage_url": "https://example.com/test1",
                "domains": ["test"],
                "taxon": ["NCBITaxon:9606", "NCBITaxon:10116"],
                "layout": "resource_detail",
            },
            {
                "id": "test-resource-2",
                "name": "Test Resource 2",
                "description": "Another test resource with taxa",
                "category": "TestCategory",
                "activity_status": "active",
                "homepage_url": "https://example.com/test2",
                "domains": ["test"],
                "taxon": ["NCBITaxon:3702"],
                "layout": "resource_detail",
            },
        ]
    }


@pytest.fixture
def parquet_backend_taxon_query_data():
    return {
        "resources": [
            {
                "id": "test-resource-1",
                "name": "Human Resource",
                "description": "Resource for human studies",
                "category": "TestCategory",
                "activity_status": "active",
                "homepage_url": "https://example.com/test1",
                "domains": ["test"],
                "taxon": ["NCBITaxon:9606"],
                "layout": "resource_detail",
            },
            {
                "id": "test-resource-2",
                "name": "Rat Resource",
                "description": "Resource for rat studies",
                "category": "TestCategory",
                "activity_status": "active",
                "homepage_url": "https://example.com/test2",
                "domains": ["test"],
                "taxon": ["NCBITaxon:10116"],
                "layout": "resource_detail",
            },
            {
                "id": "test-resource-3",
                "name": "Multi-taxon Resource",
                "description": "Resource for multiple taxa",
                "category": "TestCategory",
                "activity_status": "active",
                "homepage_url": "https://example.com/test3",
                "domains": ["test"],
                "taxon": ["NCBITaxon:3702"],
                "layout": "resource_detail",
            },
        ]
    }


@pytest.fixture
def parquet_backend_single_taxon_data():
    return {
        "resources": [
            {
                "id": "test-resource-1",
                "name": "Test Resource",
                "category": "TestCategory",
                "activity_status": "active",
                "domains": ["test"],
                "taxon": ["NCBITaxon:9606"],
                "layout": "resource_detail",
            },
        ]
    }


@pytest.fixture
def parquet_yaml_writer(tmp_path):
    def _write(data: dict, filename: str = "resources.yml") -> Path:
        output_path = tmp_path / filename
        output_path.write_text(yaml.safe_dump(data), encoding="utf-8")
        return output_path

    return _write
