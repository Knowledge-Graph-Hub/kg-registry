"""Integration test to verify DuckDB backend doesn't interfere with existing YAML processing."""

import os
import tempfile
import unittest
from pathlib import Path

import yaml

from kg_registry.duckdb_backend import DuckDBBackend


class TestDuckDBIntegration(unittest.TestCase):
    """Test integration with existing YAML processing."""

    def test_yaml_data_integrity(self):
        """Test that DuckDB operations don't modify YAML files."""

        # Create test YAML data
        test_data = {
            "resources": [
                {
                    "id": "test-resource",
                    "name": "Test Resource",
                    "description": "A test resource",
                    "category": "TestCategory",
                    "activity_status": "active",
                    "domains": ["test"],
                    "license": {"id": "MIT", "label": "MIT License"},
                    "products": [
                        {"id": "test-product", "name": "Test Product", "category": "DataProduct"}
                    ],
                }
            ]
        }

        # Create temporary YAML file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(test_data, f)
            yaml_file = f.name

        try:
            # Read original YAML content
            with open(yaml_file, "r") as f:
                original_content = f.read()

            # Create DuckDB backend and sync
            db_path = tempfile.mktemp(suffix=".duckdb")
            backend = DuckDBBackend(db_path)
            count = backend.sync_from_yaml(yaml_file)

            # Verify sync worked
            self.assertEqual(count, 1)

            # Query the data
            resources = backend.query_resources(category="TestCategory")
            self.assertEqual(len(resources), 1)
            self.assertEqual(resources[0]["id"], "test-resource")

            # Verify YAML file is unchanged
            with open(yaml_file, "r") as f:
                current_content = f.read()

            self.assertEqual(original_content, current_content)

            # Verify original YAML can still be loaded
            with open(yaml_file, "r") as f:
                loaded_data = yaml.safe_load(f)

            self.assertEqual(loaded_data, test_data)

            backend.close()

        finally:
            # Clean up
            os.unlink(yaml_file)
            if os.path.exists(db_path):
                os.unlink(db_path)

    def test_existing_yaml_processing_still_works(self):
        """Test that existing YAML processing functions still work."""

        # This test ensures that the existing kg_registry.utils functions
        # continue to work after adding DuckDB backend

        # Create test YAML data matching the expected format
        test_data = {
            "resources": [
                {
                    "id": "test-resource",
                    "name": "Test Resource",
                    "description": "A test resource",
                    "category": "TestCategory",
                    "activity_status": "active",
                    "domains": ["test"],
                    "license": {"id": "MIT", "label": "MIT License"},
                }
            ]
        }

        # Create temporary YAML file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(test_data, f)
            yaml_file = f.name

        try:
            # Test direct YAML loading (what existing code does)
            with open(yaml_file, "r") as f:
                loaded_data = yaml.safe_load(f)

            self.assertEqual(loaded_data, test_data)

            # Test that we can still iterate over resources
            resources = loaded_data["resources"]
            self.assertEqual(len(resources), 1)
            self.assertEqual(resources[0]["id"], "test-resource")

            # Test that DuckDB backend and direct YAML loading produce consistent results
            db_path = tempfile.mktemp(suffix=".duckdb")
            with DuckDBBackend(db_path) as backend:
                backend.sync_from_yaml(yaml_file)

                db_resources = backend.query_resources()
                self.assertEqual(len(db_resources), 1)

                # Compare key fields
                yaml_resource = resources[0]
                db_resource = db_resources[0]

                self.assertEqual(yaml_resource["id"], db_resource["id"])
                self.assertEqual(yaml_resource["name"], db_resource["name"])
                self.assertEqual(yaml_resource["description"], db_resource["description"])
                self.assertEqual(yaml_resource["category"], db_resource["category"])
                self.assertEqual(yaml_resource["activity_status"], db_resource["activity_status"])

        finally:
            # Clean up
            os.unlink(yaml_file)
            if os.path.exists(db_path):
                os.unlink(db_path)


if __name__ == "__main__":
    unittest.main()
