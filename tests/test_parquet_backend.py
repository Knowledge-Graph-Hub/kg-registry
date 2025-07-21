"""Test Parquet backend functionality."""

import json
import os
import tempfile
import unittest
from pathlib import Path

import yaml

from kg_registry.parquet_backend import ParquetBackend, sync_yaml_to_parquet, DuckDBParquetQuerier


class TestParquetBackend(unittest.TestCase):
    """Test Parquet backend functionality."""

    def setUp(self):
        """Set up test data."""
        self.test_data = {
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
                    "license": {
                        "id": "MIT",
                        "label": "MIT License"
                    },
                    "domains": ["test", "example"],
                    "contacts": [
                        {
                            "category": "Individual",
                            "label": "Test Person",
                            "contact_details": [
                                {
                                    "contact_type": "email",
                                    "value": "test@example.com"
                                }
                            ]
                        }
                    ],
                    "products": [
                        {
                            "id": "test-resource-1.product1",
                            "name": "Test Product 1",
                            "category": "DataProduct",
                            "description": "Test product description",
                            "format": "csv",
                            "product_url": "https://example.com/product1"
                        }
                    ],
                    "layout": "resource_detail"
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
                    "products": []
                }
            ]
        }
        # Create a temporary directory for Parquet files
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up after tests."""
        # Remove temporary directory and files
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_in_memory_backend(self):
        """Test in-memory Parquet backend."""
        backend = ParquetBackend()
        
        # Test that tables are created
        tables_query = backend.conn.execute("SHOW TABLES")
        tables = tables_query.fetchall()
        table_names = [table[0] for table in tables]
        
        self.assertIn("resources", table_names)
        self.assertIn("resource_domains", table_names)
        self.assertIn("resource_products", table_names)
        
        backend.close()

    def test_yaml_sync(self):
        """Test syncing YAML data to Parquet."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = ParquetBackend(self.temp_dir)
            count = backend.sync_from_yaml(yaml_file)
            
            self.assertEqual(count, 2)
            
            # Check Parquet files were created
            parquet_files = [f for f in os.listdir(self.temp_dir) if f.endswith('.parquet')]
            self.assertEqual(len(parquet_files), 3)  # resources, domains, products
            
            # Check resources were inserted
            resources_query = backend.conn.execute("SELECT * FROM resources")
            resources = resources_query.fetchall()
            self.assertEqual(len(resources), 2)
            
            # Check domains were inserted
            domains_query = backend.conn.execute("SELECT * FROM resource_domains")
            domains = domains_query.fetchall()
            self.assertEqual(len(domains), 3)  # 2 domains for resource1, 1 for resource2
            
            # Check products were inserted
            products_query = backend.conn.execute("SELECT * FROM resource_products")
            products = products_query.fetchall()
            self.assertEqual(len(products), 1)  # Only resource1 has products
            
            backend.close()
            
        finally:
            os.unlink(yaml_file)

    def test_query_resources(self):
        """Test querying resources with filters."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = ParquetBackend()
            backend.sync_from_yaml(yaml_file)
            
            # Test filter by category
            results = backend.query_resources(category="TestCategory")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['id'], 'test-resource-1')
            
            # Test filter by activity_status
            results = backend.query_resources(activity_status="active")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['id'], 'test-resource-1')
            
            # Test filter by domain
            results = backend.query_resources(domain="example")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['id'], 'test-resource-1')
            
            backend.close()
            
        finally:
            os.unlink(yaml_file)

    def test_search_resources(self):
        """Test searching resources."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = ParquetBackend()
            backend.sync_from_yaml(yaml_file)
            
            # Test search by name
            results = backend.search_resources("Test Resource 1")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['id'], 'test-resource-1')
            
            # Test search by description
            results = backend.search_resources("Parquet testing")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['id'], 'test-resource-1')
            
            # Test search with no results
            results = backend.search_resources("nonexistent")
            self.assertEqual(len(results), 0)
            
            backend.close()
            
        finally:
            os.unlink(yaml_file)

    def test_get_resource_stats(self):
        """Test getting resource statistics."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            backend = ParquetBackend()
            backend.sync_from_yaml(yaml_file)
            
            stats = backend.get_resource_stats()
            
            self.assertEqual(stats['total_resources'], 2)
            self.assertEqual(stats['active_resources'], 1)
            self.assertEqual(stats['by_category']['TestCategory'], 1)
            self.assertEqual(stats['by_category']['AnotherCategory'], 1)
            self.assertEqual(stats['by_domain']['test'], 2)
            self.assertEqual(stats['by_domain']['example'], 1)
            
            backend.close()
            
        finally:
            os.unlink(yaml_file)

    def test_sync_function(self):
        """Test standalone sync function."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            count = sync_yaml_to_parquet(yaml_file, self.temp_dir)
            self.assertEqual(count, 2)
            
            # Verify Parquet files were created
            parquet_files = [f for f in os.listdir(self.temp_dir) if f.endswith('.parquet')]
            self.assertEqual(len(parquet_files), 3)  # resources, domains, products
            
            # Verify data was synced by loading and querying
            backend = ParquetBackend()
            backend.load_from_parquet(self.temp_dir)
            resources_query = backend.conn.execute("SELECT COUNT(*) FROM resources")
            resources_count_row = resources_query.fetchone()
            resources_count = resources_count_row[0] if resources_count_row else 0
            self.assertEqual(resources_count, 2)
            backend.close()
            
        finally:
            os.unlink(yaml_file)

    def test_duckdb_parquet_querier(self):
        """Test DuckDBParquetQuerier."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            # First sync data to Parquet
            sync_yaml_to_parquet(yaml_file, self.temp_dir)
            
            # Then test querying directly from Parquet
            with DuckDBParquetQuerier(self.temp_dir) as querier:
                # Basic query
                results = querier.execute_query("SELECT * FROM resources")
                self.assertEqual(len(results), 2)
                
                # Filter query
                results = querier.execute_query(
                    "SELECT * FROM resources WHERE category = ?", 
                    ["TestCategory"]
                )
                self.assertEqual(len(results), 1)
                self.assertEqual(results[0]['id'], 'test-resource-1')
                
                # Join query
                results = querier.execute_query("""
                    SELECT r.id, r.name, d.domain
                    FROM resources r
                    JOIN resource_domains d ON r.id = d.resource_id
                    WHERE d.domain = 'example'
                """)
                self.assertEqual(len(results), 1)
                self.assertEqual(results[0]['id'], 'test-resource-1')
                self.assertEqual(results[0]['domain'], 'example')
                
        finally:
            os.unlink(yaml_file)

    def test_context_manager(self):
        """Test Parquet backend as context manager."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(self.test_data, f)
            yaml_file = f.name

        try:
            with ParquetBackend() as backend:
                count = backend.sync_from_yaml(yaml_file)
                self.assertEqual(count, 2)
                
                results = backend.query_active_resources()
                self.assertEqual(len(results), 1)
                
        finally:
            os.unlink(yaml_file)


if __name__ == '__main__':
    unittest.main()
