"""Test that validation requires the broader domain of each specific domain."""


def test_specific_domain_with_parent_passes(extract_metadata_module):
    obj = {"domains": ["neuroscience", "neurodegenerative disease", "genomics"]}
    assert extract_metadata_module.check_domain_parents(obj) == []


def test_specific_domain_without_parent_is_reported(extract_metadata_module):
    obj = {"domains": ["biomedical", "neurodegenerative disease", "cancer"]}
    errors = extract_metadata_module.check_domain_parents(obj)
    assert len(errors) == 1
    assert "'neurodegenerative disease'" in errors[0]
    assert "'neuroscience' must also be listed" in errors[0]


def test_broad_and_unknown_domains_need_no_parent(extract_metadata_module):
    obj = {"domains": ["general", "other", "potatosalad"]}
    assert extract_metadata_module.check_domain_parents(obj) == []


def test_every_specific_domain_names_a_broad_domain(extract_metadata_module):
    sv = extract_metadata_module.get_schema_view()
    permissible = sv.get_enum("DomainEnum").permissible_values
    for name, pv in permissible.items():
        if pv.is_a:
            assert pv.is_a in permissible, name
            assert permissible[pv.is_a].is_a is None, f"{name} is nested more than two levels"
            assert pv.meaning, f"{name} has no meaning"
