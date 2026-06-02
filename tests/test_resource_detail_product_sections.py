from pathlib import Path


def test_resource_detail_product_sections_use_product_ownership():
    layout = Path("_layouts/resource_detail.html").read_text(encoding="utf-8")

    assert "{% elsif p.secondary_source %}" not in layout
    assert "product_has_page_secondary_source" not in layout
    assert "first_secondary_source_id" not in layout
    assert "p.id == page.id or first_segment == page.id" in layout
    assert "candidate_source_resource_id == page.id" in layout
