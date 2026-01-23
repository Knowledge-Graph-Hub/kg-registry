"""Tests for FTP URL checking functionality.

Test fixtures are available in tests/fixtures/:
- test_ftp_resources.yml: Test data for processor.py check_urls (uses resource_purl field)
- test_ftp_parallel.yml: Test data for retrieve-file-sizes-parallel.py (uses product_url field)

Both fixtures include examples of:
- FTP file URLs (e.g., ftp://ftp.ncbi.nlm.nih.gov/README.ftp)
- FTP directory URLs (e.g., ftp://ftp.ncbi.nlm.nih.gov/pub/)
- HTTPS URLs for comparison testing
"""

import importlib.util
import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Add util directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "util"))

# Define fixture directory
FIXTURES_DIR = Path(__file__).parent / "fixtures"


# Load processor.py (has dashes in name)
processor_spec = importlib.util.spec_from_file_location(
    "processor", Path(__file__).parent.parent / "util" / "processor.py"
)
processor = importlib.util.module_from_spec(processor_spec)
processor_spec.loader.exec_module(processor)

# Load retrieve-file-sizes.py (has dashes in name)
retrieve_spec = importlib.util.spec_from_file_location(
    "retrieve_file_sizes", Path(__file__).parent.parent / "util" / "retrieve-file-sizes.py"
)
retrieve_file_sizes = importlib.util.module_from_spec(retrieve_spec)
retrieve_spec.loader.exec_module(retrieve_file_sizes)


class TestFTPURLChecker(TestCase):
    """Test FTP URL checking functionality in processor.py and retrieve-file-sizes.py."""

    def test_ftp_file_size_retrieval(self):
        """Test that FTP file size can be retrieved successfully."""
        # Test with a known public FTP file
        url = "ftp://ftp.ncbi.nlm.nih.gov/README.ftp"

        size, error, info = retrieve_file_sizes.get_ftp_info(url)

        # Should successfully get file size
        self.assertIsNotNone(size)
        self.assertIsNone(error)
        self.assertIn("content_length", info)
        self.assertEqual(info["protocol"], "ftp")
        self.assertIn("checked_at", info)
        self.assertGreater(size, 0)

    def test_ftp_directory_detection(self):
        """Test that FTP directories are correctly identified."""
        # Test with a known public FTP directory
        url = "ftp://ftp.ncbi.nlm.nih.gov/pub/"

        size, error, info = retrieve_file_sizes.get_ftp_info(url)

        # Should identify as directory
        self.assertIsNone(size)
        self.assertIsNone(error)
        self.assertEqual(info.get("skip_reason"), "directory")
        self.assertEqual(info["protocol"], "ftp")
        self.assertIn("checked_at", info)

    def test_ftp_nonexistent_path(self):
        """Test that nonexistent FTP paths return appropriate errors."""
        # Test with a path that doesn't exist
        url = "ftp://ftp.ncbi.nlm.nih.gov/nonexistent_file_12345.txt"

        size, error, info = retrieve_file_sizes.get_ftp_info(url)

        # Should return error
        self.assertIsNone(size)
        self.assertIsNotNone(error)
        self.assertIn("error", info)
        self.assertEqual(info["protocol"], "ftp")

    def test_ftp_invalid_url_scheme(self):
        """Test that non-FTP URLs are rejected by get_ftp_info."""
        # Test with HTTP URL (wrong protocol)
        url = "http://example.com/file.txt"

        size, error, info = retrieve_file_sizes.get_ftp_info(url)

        # Should return error about wrong scheme
        self.assertIsNone(size)
        self.assertIsNotNone(error)
        self.assertIn("Not an FTP URL", error)

    def test_cache_skip_reason_includes_directory(self):
        """Test that cache_should_skip recognizes 'directory' as a skip reason."""
        cache = {
            "ftp://example.com/somedir/": {
                "skip_reason": "directory",
                "checked_at": "2025-12-04T00:00:00Z",
            }
        }

        should_skip, entry = retrieve_file_sizes.cache_should_skip(
            "ftp://example.com/somedir/", cache
        )

        self.assertTrue(should_skip)
        self.assertIsNotNone(entry)
        self.assertEqual(entry["skip_reason"], "directory")

    def test_get_file_size_from_header_routes_ftp(self):
        """Test that get_file_size_from_header correctly routes FTP URLs to get_ftp_info."""
        url = "ftp://ftp.ncbi.nlm.nih.gov/README.ftp"

        size, error, info = retrieve_file_sizes.get_file_size_from_header(url)

        # Should successfully process through FTP handler
        self.assertIsNotNone(size)
        self.assertIsNone(error)
        self.assertEqual(info["protocol"], "ftp")


class TestProcessorFTPChecking(TestCase):
    """Test FTP URL validation in processor.py check_urls functionality."""

    @patch("builtins.exit")
    def test_processor_check_urls_with_valid_ftp(self, mock_exit):
        """Test that processor.check_urls correctly validates valid FTP URLs."""
        resources = [
            {
                "id": "test_resource",
                "products": [
                    {"id": "test_product", "resource_purl": "ftp://ftp.ncbi.nlm.nih.gov/README.ftp"}
                ],
            }
        ]

        args = MagicMock()

        # Should not raise or exit with error
        processor.check_urls(resources, args)
        mock_exit.assert_not_called()

    @patch("builtins.exit")
    @patch("builtins.print")
    def test_processor_check_urls_with_invalid_ftp(self, mock_print, mock_exit):
        """Test that processor.check_urls correctly fails on invalid FTP URLs."""
        resources = [
            {
                "id": "test_resource",
                "products": [
                    {
                        "id": "test_product_fail",
                        "resource_purl": "ftp://ftp.ncbi.nlm.nih.gov/nonexistent_12345.txt",
                    }
                ],
            }
        ]

        args = MagicMock()

        # Should call exit(1) for failed URLs
        processor.check_urls(resources, args)
        mock_exit.assert_called_with(1)

    @patch("builtins.exit")
    def test_processor_handles_none_url(self, mock_exit):
        """Test that processor.check_urls handles None URLs gracefully."""
        resources = [
            {
                "id": "test_resource",
                "products": [{"id": "test_product_no_url", "resource_purl": None}],
            }
        ]

        args = MagicMock()

        # Should not fail on None URLs
        processor.check_urls(resources, args)
        mock_exit.assert_not_called()

    @patch("builtins.exit")
    def test_processor_handles_empty_url(self, mock_exit):
        """Test that processor.check_urls handles empty URLs gracefully."""
        resources = [
            {
                "id": "test_resource",
                "products": [{"id": "test_product_empty_url", "resource_purl": ""}],
            }
        ]

        args = MagicMock()

        # Should not fail on empty URLs
        processor.check_urls(resources, args)
        mock_exit.assert_not_called()


class TestFTPFixtures(TestCase):
    """Test fixture files for integration testing."""

    def test_processor_fixture_exists(self):
        """Verify test_ftp_resources.yml fixture exists for processor tests."""
        fixture_path = FIXTURES_DIR / "test_ftp_resources.yml"
        self.assertTrue(fixture_path.exists(), f"Fixture file should exist at {fixture_path}")

    def test_parallel_fixture_exists(self):
        """Verify test_ftp_parallel.yml fixture exists for parallel retriever tests."""
        fixture_path = FIXTURES_DIR / "test_ftp_parallel.yml"
        self.assertTrue(fixture_path.exists(), f"Fixture file should exist at {fixture_path}")

    def test_processor_fixture_structure(self):
        """Verify test_ftp_resources.yml has expected structure."""
        import yaml

        fixture_path = FIXTURES_DIR / "test_ftp_resources.yml"

        with open(fixture_path, "r") as f:
            data = yaml.safe_load(f)

        self.assertIn("resources", data)
        self.assertIsInstance(data["resources"], list)
        self.assertGreater(len(data["resources"]), 0)

        # Check for FTP URLs in products
        has_ftp_url = False
        for resource in data["resources"]:
            for product in resource.get("products", []):
                if "resource_purl" in product:
                    url = product["resource_purl"]
                    if url and url.startswith("ftp://"):
                        has_ftp_url = True
                        break

        self.assertTrue(has_ftp_url, "Fixture should contain at least one FTP URL")

    def test_parallel_fixture_structure(self):
        """Verify test_ftp_parallel.yml has expected structure."""
        import yaml

        fixture_path = FIXTURES_DIR / "test_ftp_parallel.yml"

        with open(fixture_path, "r") as f:
            data = yaml.safe_load(f)

        self.assertIn("resources", data)
        self.assertIsInstance(data["resources"], list)
        self.assertGreater(len(data["resources"]), 0)

        # Check for FTP URLs in products
        has_ftp_url = False
        for resource in data["resources"]:
            for product in resource.get("products", []):
                if "product_url" in product:
                    url = product["product_url"]
                    if url and url.startswith("ftp://"):
                        has_ftp_url = True
                        break

        self.assertTrue(has_ftp_url, "Fixture should contain at least one FTP URL")
