"""Test taxon mapping generation behavior for fast default builds."""


def test_generate_taxon_mapping_uses_fallback_hierarchy_by_default(
    generate_taxon_mapping_module,
    monkeypatch,
):
    monkeypatch.setattr(
        generate_taxon_mapping_module,
        "get_all_database_taxa",
        lambda _: {"NCBITaxon:40674", "NCBITaxon:9606", "NCBITaxon:10090", "NCBITaxon:10116"},
    )

    def _unexpected_oak_import():
        raise AssertionError("oaklib should not be loaded for the default fast path")

    monkeypatch.setattr(generate_taxon_mapping_module, "get_oak_adapter", _unexpected_oak_import)

    mapping = generate_taxon_mapping_module.generate_taxon_mapping(
        "unused",
        filter_taxa=["NCBITaxon:40674", "NCBITaxon:9606"],
        use_oaklib=False,
    )

    assert mapping["NCBITaxon:40674"] == [
        "NCBITaxon:40674",
        "NCBITaxon:9606",
        "NCBITaxon:10090",
        "NCBITaxon:10116",
    ]
    assert mapping["NCBITaxon:9606"] == ["NCBITaxon:9606"]
