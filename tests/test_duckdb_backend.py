"""Test DuckDB backend functionality."""

import json
import os
import tempfile
import unittest
from pathlib import Path

import yaml

from kg_registry.duckdb_backend import DuckDBBackend, sync_yaml_to_duckdb


class TestDuckDBBackend(unittest.TestCase):
    """Test DuckDB backend functionality."""

    def setUp(self):
        """Set up test data."""
        self.test_data = {
            "resources": [
                {
                    "id": "test-resource-1",
                    "name": "Test Resource 1",
                    "description": "A test resource for DuckDB testing",
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
                            "category": "DataProduct",
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

    def test_in_memory_backend(self):
        """Test in-memory DuckDB backend."""
        backend = DuckDBBackend()

        # Test that tables are created
        tables = backend.conn.execute("SHOW TABLES").fetchall()
        table_names = [table[0] for table in tables]

        self.assertIn("resources", table_names)
        self.assertIn("resource_domains", table_names)
        self.assertIn("resource_products", table_names)

        backend.close()

    def test_yaml_sync(self):
        """Test syncing YAML data to DuckDB."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = DuckDBBackend()
            count = backend.sync_from_yaml(yaml_file)

            self.assertEqual(count, 2)

            # Check resources were inserted
            resources = backend.conn.execute("SELECT * FROM resources").fetchall()
            self.assertEqual(len(resources), 2)

            # Check domains were inserted
            domains = backend.conn.execute("SELECT * FROM resource_domains").fetchall()
            self.assertEqual(len(domains), 3)  # 2 domains for resource1, 1 for resource2

            # Check products were inserted
            products = backend.conn.execute("SELECT * FROM resource_products").fetchall()
            self.assertEqual(len(products), 1)  # Only resource1 has products

            backend.close()

        finally:
            os.unlink(yaml_file)

    def test_query_resources(self):
        """Test querying resources with filters."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = DuckDBBackend()
            backend.sync_from_yaml(yaml_file)

            # Test query by category
            results = backend.query_resources(category="TestCategory")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "test-resource-1")

            # Test query by activity status
            results = backend.query_resources(activity_status="active")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "test-resource-1")

            # Test query by domain
            results = backend.query_resources(domain="test")
            self.assertEqual(len(results), 2)

            # Test query by name contains
            results = backend.query_resources(name_contains="Resource 1")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "test-resource-1")

            backend.close()

        finally:
            os.unlink(yaml_file)

    def test_search_resources(self):
        """Test searching resources."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = DuckDBBackend()
            backend.sync_from_yaml(yaml_file)

            # Test search by name
            results = backend.search_resources("Test Resource 1")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "test-resource-1")

            # Test search by description
            results = backend.search_resources("DuckDB testing")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "test-resource-1")

            # Test search with no results
            results = backend.search_resources("nonexistent")
            self.assertEqual(len(results), 0)

            backend.close()

        finally:
            os.unlink(yaml_file)

    def test_get_resource_stats(self):
        """Test getting resource statistics."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = DuckDBBackend()
            backend.sync_from_yaml(yaml_file)

            stats = backend.get_resource_stats()

            self.assertEqual(stats["total_resources"], 2)
            self.assertEqual(stats["active_resources"], 1)
            self.assertEqual(stats["by_category"]["TestCategory"], 1)
            self.assertEqual(stats["by_category"]["AnotherCategory"], 1)
            self.assertEqual(stats["by_domain"]["test"], 2)
            self.assertEqual(stats["by_domain"]["example"], 1)

            backend.close()

        finally:
            os.unlink(yaml_file)

    def test_sync_function(self):
        """Test standalone sync function."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        # Create a temporary database path without creating the file
        db_path = tempfile.mktemp(suffix=".duckdb")

        try:
            count = sync_yaml_to_duckdb(yaml_file, db_path)
            self.assertEqual(count, 2)

            # Verify data was synced
            backend = DuckDBBackend(db_path)
            resources = backend.conn.execute("SELECT COUNT(*) FROM resources").fetchone()[0]
            self.assertEqual(resources, 2)
            backend.close()

        finally:
            os.unlink(yaml_file)
            if os.path.exists(db_path):
                os.unlink(db_path)

    def test_context_manager(self):
        """Test DuckDB backend as context manager."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            with DuckDBBackend() as backend:
                count = backend.sync_from_yaml(yaml_file)
                self.assertEqual(count, 2)

                results = backend.query_active_resources()
                self.assertEqual(len(results), 1)

        finally:
            os.unlink(yaml_file)


if __name__ == "__main__":
    unittest.main()
