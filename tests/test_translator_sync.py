"""Tests for Translator release synchronization."""

from util.sync_translator import TranslatorSync


def test_build_product_uses_latest_url_and_concrete_versions():
    syncer = TranslatorSync(cache_ttl_hours=1)
    product = syncer.build_product(
        release_key="bindingdb",
        summary={
            "release_version": "2026_03_06",
            "build_version": "bindingdb_202603_2f3418c8_2025sep1_4.3.6",
            "source_version": "202603",
            "biolink_version": "4.3.6",
            "node_norm_version": "2025sep1",
        },
        graph_metadata={
            "version": "bindingdb_202603_2f3418c8_2025sep1_4.3.6",
            "license": "MIT",
            "schema": {
                "nodes_summary": {"total_count": 736988},
                "edges_summary": {"total_count": 1045781},
            },
            "isBasedOn": [{"id": "bindingdb"}],
        },
    )

    assert product["id"] == "translator.bindingdb.graph"
    assert product["name"] == "Translator BindingDB KGX Graph"
    assert product["format"] == "kgx-jsonl"
    assert product["product_url"] == "https://kgx-storage.rtx.ai/releases/bindingdb/latest/"
    assert product["latest_version"] == "2026_03_06"
    assert product["versions"] == [
        "2026_03_06",
        "bindingdb_202603_2f3418c8_2025sep1_4.3.6",
    ]
    assert product["original_source"] == ["bindingdb"]
    assert product["secondary_source"] == ["translator"]
    assert product["node_count"] == 736988
    assert product["edge_count"] == 1045781
    assert product["compatibility"] == [{"standard": "biolink", "version": "4.3.6"}]
    assert product["license"] == {
        "id": "https://opensource.org/license/mit/",
        "label": "MIT",
    }


def test_build_product_maps_translator_aggregate_sources_to_registry_ids():
    syncer = TranslatorSync(cache_ttl_hours=1)
    product = syncer.build_product(
        release_key="translator_kg",
        summary={
            "release_version": "2026_03_27",
            "build_version": "2026_03_27",
            "biolink_version": "4.3.6",
            "node_norm_version": "2025sep1",
        },
        graph_metadata={
            "version": "2026_03_27",
            "schema": {
                "nodes_summary": {"total_count": 1696790},
                "edges_summary": {"total_count": 29243943},
            },
            "isBasedOn": [
                {"id": "alliance"},
                {"id": "dakp"},
                {"id": "drug_rep_hub"},
                {"id": "go_cam"},
                {"id": "hpoa"},
                {"id": "icees"},
                {"id": "ncbi_gene"},
                {"id": "tmkp"},
            ],
        },
    )

    assert product["id"] == "translator.translator_kg.graph"
    assert product["name"] == "Translator Aggregate KGX Graph"
    assert product["original_source"] == [
        "alliance",
        "drug-approvals-kp",
        "drugrephub",
        "go-cam",
        "hp",
        "icees-kg",
        "ncbigene",
        "text-mining-kp",
    ]
    assert product["latest_version"] == "2026_03_27"
    assert product["versions"] == ["2026_03_27"]
