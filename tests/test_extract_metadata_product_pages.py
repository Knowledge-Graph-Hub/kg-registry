"""Test extract-metadata helpers used for standalone product page generation."""


def test_sanitize_product_for_page_preserves_source_product(extract_metadata_module):
    product = {
        "id": "demo.download",
        "warnings": ["File was not able to be retrieved when checked on 2026-03-30: timeout"],
    }

    sanitized = extract_metadata_module.sanitize_product_for_page(product)

    assert sanitized["warnings"] == [
        "File was not able to be retrieved when checked on 2026-03-30_ timeout"
    ]
    assert product["warnings"] == [
        "File was not able to be retrieved when checked on 2026-03-30: timeout"
    ]
