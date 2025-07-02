"""Test DOI URL formatting to ensure consistent resolution."""

import unittest
import re


class TestDOIFormatting(unittest.TestCase):
    """Test cases for DOI URL formatting consistency."""

    def test_doi_url_normalization(self):
        """Test that DOI URLs are properly normalized to remove 'doi:' prefix."""
        # Test cases: input DOI -> expected normalized DOI
        test_cases = [
            ("doi:10.1093/nar/gkab1016", "10.1093/nar/gkab1016"),
            ("10.1093/nar/gkab1016", "10.1093/nar/gkab1016"),
            ("doi:10.1186/s12859-020-3517-7", "10.1186/s12859-020-3517-7"),
            ("10.1186/s12859-020-3517-7", "10.1186/s12859-020-3517-7"),
        ]
        
        for input_doi, expected_normalized in test_cases:
            with self.subTest(input_doi=input_doi):
                # Simulate the normalization logic used in templates and JS
                normalized = re.sub(r'^doi:', '', input_doi)
                self.assertEqual(normalized, expected_normalized)
                
                # Verify the final URL would be correct
                final_url = f"https://doi.org/{normalized}"
                expected_url = f"https://doi.org/{expected_normalized}"
                self.assertEqual(final_url, expected_url)
                
                # Ensure we don't have double prefix
                self.assertNotIn("doi:doi:", final_url)
                self.assertNotIn("doi:/doi:", final_url)

    def test_doi_url_patterns(self):
        """Test that generated DOI URLs follow expected patterns."""
        test_dois = [
            "doi:10.1093/nar/gkab1016",
            "10.1093/nar/gkab1016"
        ]
        
        for doi in test_dois:
            with self.subTest(doi=doi):
                # Apply normalization
                normalized = re.sub(r'^doi:', '', doi)
                final_url = f"https://doi.org/{normalized}"
                
                # Check URL pattern is correct
                expected_pattern = r'^https://doi\.org/10\.\d+/.+'
                self.assertRegex(final_url, expected_pattern,
                               f"DOI URL {final_url} doesn't match expected pattern")
                
                # Ensure no malformed URLs
                self.assertNotIn("//doi:", final_url)
                self.assertNotIn("/doi:doi:", final_url)


if __name__ == '__main__':
    unittest.main()