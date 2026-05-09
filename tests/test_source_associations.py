"""Tests for product source provenance association helpers."""

from util.source_associations import (
    ORIGINAL_SOURCE_RELATION,
    SECONDARY_SOURCE_RELATION,
    iter_source_ids,
    ensure_direct_product_primary_source,
    make_original_source_associations,
    make_secondary_source_associations,
    merge_source_associations,
)


def test_source_association_defaults_and_legacy_iteration():
    original = make_original_source_associations(["go", "go", "", "hp"])
    secondary = make_secondary_source_associations(["translator"])

    assert original == [
        {"source": "go", "relation_type": ORIGINAL_SOURCE_RELATION},
        {"source": "hp", "relation_type": ORIGINAL_SOURCE_RELATION},
    ]
    assert secondary == [
        {"source": "translator", "relation_type": SECONDARY_SOURCE_RELATION}
    ]
    assert list(iter_source_ids(["go", {"source": "hp", "relation_type": "prov:used"}])) == [
        "go",
        "hp",
    ]


def test_merge_source_associations_preserves_existing_relation_type():
    merged = merge_source_associations(
        [{"source": "go", "relation_type": "prov:used"}],
        ["go", "hp"],
        ORIGINAL_SOURCE_RELATION,
    )

    assert merged == [
        {"source": "go", "relation_type": "prov:used"},
        {"source": "hp", "relation_type": ORIGINAL_SOURCE_RELATION},
    ]


def test_ensure_direct_product_primary_source_promotes_owned_product_source():
    product = {
        "id": "genomickb.site",
        "secondary_source": [
            {"source": "genomickb", "relation_type": SECONDARY_SOURCE_RELATION},
            {"source": "translator", "relation_type": SECONDARY_SOURCE_RELATION},
        ],
    }

    assert ensure_direct_product_primary_source("genomickb", product) is True
    assert product["original_source"] == [
        {"source": "genomickb", "relation_type": ORIGINAL_SOURCE_RELATION}
    ]
    assert product["secondary_source"] == [
        {"source": "translator", "relation_type": SECONDARY_SOURCE_RELATION}
    ]
