"""Tests for product source provenance association helpers."""

from util.source_associations import (
    ORIGINAL_SOURCE_RELATION,
    SECONDARY_SOURCE_RELATION,
    ensure_direct_product_primary_source,
    iter_source_ids,
    make_original_source_associations,
    make_secondary_source_associations,
    merge_source_associations,
    resource_owns_product,
    source_resource_id,
)


def test_source_association_defaults_and_legacy_iteration():
    original = make_original_source_associations(["go", "go", "", "hp"])
    secondary = make_secondary_source_associations(["translator"])

    assert original == [
        {"source": "go", "relation_type": ORIGINAL_SOURCE_RELATION},
        {"source": "hp", "relation_type": ORIGINAL_SOURCE_RELATION},
    ]
    assert secondary == [{"source": "translator", "relation_type": SECONDARY_SOURCE_RELATION}]
    assert list(iter_source_ids(["go", {"source": "hp", "relation_type": "prov:used"}])) == [
        "go",
        "hp",
    ]
    assert source_resource_id("go") == "go"
    assert source_resource_id("go.owl") == "go"


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


def test_resource_owns_product_matches_whole_first_segment():
    assert resource_owns_product("go", "go.owl")
    assert resource_owns_product("biobtree", "biobtree.graph.human-subgraph")
    assert resource_owns_product("open-tree-of-life", "open-tree-of-life.api")


def test_resource_owns_product_rejects_string_prefix_matches():
    """A resource whose ID is a string prefix of another's must not claim its products."""
    assert not resource_owns_product("go", "goa.ftp")
    assert not resource_owns_product("mi", "mint.psicquic")
    assert not resource_owns_product("chea", "chea-kg.graph")
    assert not resource_owns_product("pr", "pr-asserted.owl")


def test_resource_owns_product_handles_missing_and_malformed_ids():
    assert not resource_owns_product("go", "go")  # undotted: no owner segment
    assert not resource_owns_product("", "go.owl")
    assert not resource_owns_product("go", None)
    assert not resource_owns_product(None, "go.owl")
    assert resource_owns_product(" go ", " go.owl ")  # surrounding whitespace tolerated
