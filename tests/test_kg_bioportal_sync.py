"""Tests for KG-Bioportal transform sync behavior."""

import textwrap

import frontmatter
import pytest
import yaml

from util.sync_kg_bioportal import KGBioportalSync, name_similarity

FLUSH_PAGE = """\
---
id: agro
name: Agronomy Ontology
category: Ontology
domains:
- agriculture
last_modified_date: '2026-01-01T00:00:00Z'
products:
- id: agro.owl
  name: AgrO
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/agro.owl
---
## Description

Agronomy.
"""

INDENTED_PAGE = """\
---
id: zeco
name: Zebrafish Experimental Conditions Ontology
category: Ontology
domains:
  - environment
last_modified_date: '2026-01-01T00:00:00Z'
products:
  - id: zeco.owl
    name: zeco.owl
    category: OntologyProduct
    product_url: http://purl.obolibrary.org/obo/zeco.owl
---
## Description

Zebrafish.
"""

SYNC_MAP = """\
confirmed:
  OBOREL: ro
  MISSINGTARGET: nonexistent
rejected:
  - RO
"""


def write_page(registry_root, resource_id, text):
    resource_dir = registry_root / resource_id
    resource_dir.mkdir(parents=True, exist_ok=True)
    page = resource_dir / f"{resource_id}.md"
    page.write_text(textwrap.dedent(text), encoding="utf-8")
    return page


@pytest.fixture
def syncer(tmp_path):
    registry_root = tmp_path / "resource"
    write_page(registry_root, "agro", FLUSH_PAGE)
    write_page(registry_root, "zeco", INDENTED_PAGE)
    write_page(
        registry_root,
        "ro",
        "---\nid: ro\nname: Relation Ontology\ncategory: Ontology\n---\nRO.\n",
    )
    map_path = tmp_path / "sync_map.yaml"
    map_path.write_text(SYNC_MAP, encoding="utf-8")
    return KGBioportalSync(
        registry_root=str(registry_root),
        map_path=str(map_path),
        report_path=str(tmp_path / "report.tsv"),
    )


@pytest.fixture
def agro_entry():
    return {
        "id": "AGRO",
        "status": "OK",
        "reason": "",
        "name": "AGRonomy Ontology",
        "version": "2026-01-01",
        "nodecount": 5102,
        "edgecount": 8691,
        "submission_id": "12",
        "download_url": "https://example.org/releases/data-2026.07/AGRO.tar.gz",
    }


# --------------------------------------------------------------------- matching


def test_name_similarity_accepts_reworded_names_and_rejects_collisions():
    # Genuine matches that read very differently.
    assert name_similarity("Uber Anatomy Ontology", "Uberon multi-species anatomy ontology") > 0.3
    assert name_similarity("Relations Ontology", "Relation Ontology") > 0.3
    assert name_similarity("Microarray and Gene Expression Data Ontology",
                           "Microarray experimental conditions") > 0.3
    # Acronym collisions in the live manifest.
    assert name_similarity("Radiomics Ontology", "Relation Ontology") == 0.0
    assert name_similarity("Atlas Ontology Model", "ATOM") == 0.0
    assert name_similarity("PatientSafetyOntology", "Plant Stress Ontology") == 0.0
    # phenotypic/phenotype falls just under the per-token threshold, which is why
    # PATO is carried in the sync map rather than matched automatically.
    assert name_similarity("Phenotypic Quality Ontology", "Phenotype And Trait Ontology") == 0.0


def test_acronym_match_requires_similar_names(syncer, agro_entry):
    assert syncer.resolve_match(agro_entry) == ("agro", "acronym")

    collision = dict(agro_entry, id="ZECO", name="Zone Enforcement Compliance Ontology")
    assert syncer.resolve_match(collision) == (None, "name_mismatch")


def test_confirmed_map_entry_overrides_acronym(syncer, agro_entry):
    # OBOREL is not a resource id, but the map points it at ro.
    assert syncer.resolve_match(dict(agro_entry, id="OBOREL", name="Relations Ontology")) == (
        "ro",
        "confirmed",
    )


def test_rejected_acronym_is_never_written(syncer, agro_entry):
    # RO would otherwise match the ro resource outright.
    assert syncer.resolve_match(dict(agro_entry, id="RO", name="Relation Ontology")) == (
        None,
        "rejected",
    )


def test_confirmed_map_entry_pointing_at_a_missing_resource_is_reported(syncer, agro_entry):
    assert syncer.resolve_match(dict(agro_entry, id="MISSINGTARGET")) == (
        None,
        "confirmed_missing",
    )


def test_entry_without_a_matching_resource_is_skipped(syncer, agro_entry):
    assert syncer.resolve_match(dict(agro_entry, id="NOSUCHTHING")) == (None, "no_resource")


def test_failed_entry_skips_the_name_check(syncer, agro_entry):
    """Skiplist entries carry no name, but must still be able to remove a product."""
    entry = dict(agro_entry, status="Skipped", reason="too_large", name="")
    assert syncer.resolve_match(entry) == ("agro", "acronym")


def test_successful_transform_wins_over_a_failed_duplicate(syncer, agro_entry):
    failed = dict(agro_entry, id="AGRO2", status="Failed")
    resolutions = [(failed, "agro", "acronym"), (agro_entry, "agro", "acronym")]
    assert syncer.pick_winners(resolutions) == [(agro_entry, "agro")]


def test_curated_match_wins_over_a_heuristic_duplicate(syncer, agro_entry):
    heuristic = dict(agro_entry, id="ZAGRO")
    resolutions = [(heuristic, "agro", "acronym"), (agro_entry, "agro", "confirmed")]
    assert syncer.pick_winners(resolutions) == [(agro_entry, "agro")]


# --------------------------------------------------------------------- products


def test_build_product_shape(syncer, agro_entry):
    product = syncer.build_product(agro_entry, "agro")

    assert product["id"] == "agro.kg-bioportal"
    assert product["name"] == "AGRO KGX graph (KG-Bioportal)"
    assert product["category"] == "GraphProduct"
    assert product["product_url"] == agro_entry["download_url"]
    assert product["format"] == "kgx"
    assert product["compression"] == "targz"
    assert product["node_count"] == 5102
    assert product["edge_count"] == 8691
    assert product["latest_version"] == "2026-01-01"
    assert product["original_source"] == [
        {"source": "agro", "relation_type": "prov:hadPrimarySource"}
    ]
    # Naming the aggregator here would make propagate_products copy every
    # transform onto the kg-bioportal page.
    assert "kg-bioportal" not in [
        association["source"] for association in product["original_source"]
    ]
    assert "secondary_source" not in product


def test_build_product_drops_placeholder_version(syncer, agro_entry):
    assert "latest_version" not in syncer.build_product(dict(agro_entry, version="NA"), "agro")


def test_merge_preserves_curated_fields_and_reports_no_change_on_rerun(syncer, agro_entry):
    product = syncer.build_product(agro_entry, "agro")
    products = [dict(product, product_file_size=1234, warnings=["curated"])]

    assert syncer.merge_product(products, syncer.build_product(agro_entry, "agro")) is False
    assert products[0]["product_file_size"] == 1234
    assert products[0]["warnings"] == ["curated"]


def test_merge_drops_file_size_when_the_release_asset_moves(syncer, agro_entry):
    products = [dict(syncer.build_product(agro_entry, "agro"), product_file_size=1234)]
    moved = dict(agro_entry, download_url="https://example.org/releases/data-2026.08/AGRO.tar.gz")

    assert syncer.merge_product(products, syncer.build_product(moved, "agro")) is True
    assert "product_file_size" not in products[0]
    assert products[0]["product_url"] == moved["download_url"]


def test_merge_clears_a_managed_field_that_disappeared(syncer, agro_entry):
    products = [syncer.build_product(agro_entry, "agro")]
    unversioned = dict(agro_entry, version="NA")

    assert syncer.merge_product(products, syncer.build_product(unversioned, "agro")) is True
    assert "latest_version" not in products[0]


def test_merge_leaves_other_products_alone(syncer, agro_entry):
    products = [{"id": "agro.owl", "name": "AgrO"}]

    assert syncer.merge_product(products, syncer.build_product(agro_entry, "agro")) is True
    assert [product["id"] for product in products] == ["agro.owl", "agro.kg-bioportal"]


def test_remove_product_only_touches_the_synced_id(syncer):
    products = [{"id": "agro.owl"}, {"id": "agro.kg-bioportal"}]

    assert syncer.remove_product(products, "agro.kg-bioportal") is True
    assert [product["id"] for product in products] == ["agro.owl"]
    assert syncer.remove_product(products, "agro.kg-bioportal") is False


# ------------------------------------------------------------------------ pages


def test_apply_entry_adds_updates_then_removes(syncer, agro_entry):
    page = syncer.resource_file("agro")

    assert syncer.apply_entry(agro_entry, "agro", dry_run=False) == "added"
    metadata = frontmatter.load(page).metadata
    product = next(p for p in metadata["products"] if p["id"] == "agro.kg-bioportal")
    assert product["node_count"] == 5102
    assert metadata["last_modified_date"] != "2026-01-01T00:00:00Z"
    # The page's own product is untouched.
    assert metadata["products"][0]["id"] == "agro.owl"

    assert syncer.apply_entry(agro_entry, "agro", dry_run=False) == "skipped"

    grown = dict(agro_entry, nodecount=6000)
    assert syncer.apply_entry(grown, "agro", dry_run=False) == "updated"
    metadata = frontmatter.load(page).metadata
    product = next(p for p in metadata["products"] if p["id"] == "agro.kg-bioportal")
    assert product["node_count"] == 6000

    failed = dict(agro_entry, status="Failed", reason="transform_error")
    assert syncer.apply_entry(failed, "agro", dry_run=False) == "removed"
    metadata = frontmatter.load(page).metadata
    assert [p["id"] for p in metadata["products"]] == ["agro.owl"]


def test_apply_entry_dry_run_writes_nothing(syncer, agro_entry):
    page = syncer.resource_file("agro")
    before = page.read_text(encoding="utf-8")

    assert syncer.apply_entry(agro_entry, "agro", dry_run=True) == "added"
    assert page.read_text(encoding="utf-8") == before


def test_failed_entry_on_an_untouched_page_is_a_no_op(syncer, agro_entry):
    page = syncer.resource_file("agro")
    before = page.read_text(encoding="utf-8")

    failed = dict(agro_entry, status="Failed", reason="transform_error")
    assert syncer.apply_entry(failed, "agro", dry_run=False) == "skipped"
    assert page.read_text(encoding="utf-8") == before


@pytest.mark.parametrize(
    ("resource_id", "expected_style", "expected_marker"),
    [("agro", "flush", "\n- id: agro.kg-bioportal"), ("zeco", "indented", "\n  - id: zeco.")],
)
def test_page_style_is_preserved(syncer, agro_entry, resource_id, expected_style, expected_marker):
    page = syncer.resource_file(resource_id)
    assert syncer.page_style(page) == expected_style

    entry = dict(agro_entry, id=resource_id.upper())
    syncer.apply_entry(entry, resource_id, dry_run=False)

    text = page.read_text(encoding="utf-8")
    assert expected_marker in text
    assert syncer.page_style(page) == expected_style


def test_page_style_uses_the_majority_when_a_page_mixes_both(tmp_path):
    page = tmp_path / "mixed.md"
    page.write_text(
        "---\n"
        "id: mixed\n"
        "domains:\n"
        "  - agriculture\n"
        "contacts:\n"
        "  - category: Individual\n"
        "publications:\n"
        "- title: Flush\n"
        "---\n"
        "- a body bullet\n"
        "- another body bullet\n",
        encoding="utf-8",
    )
    assert KGBioportalSync.page_style(page) == "indented"


def test_markdown_body_is_preserved(syncer, agro_entry):
    page = syncer.resource_file("agro")
    syncer.apply_entry(agro_entry, "agro", dry_run=False)
    assert "Agronomy." in page.read_text(encoding="utf-8")


# ----------------------------------------------------------------------- report


def test_sync_all_reports_entries_a_curator_could_resolve(syncer, agro_entry, monkeypatch):
    entries = [
        agro_entry,
        # OK, acronym matches a resource, but the names disagree.
        {
            "id": "ZECO",
            "status": "OK",
            "name": "Zone Enforcement Compliance Ontology",
            "download_url": "https://example.org/ZECO.tar.gz",
        },
        # OK, no resource by that acronym, but the name matches one exactly.
        {
            "id": "OBOREL2",
            "status": "OK",
            "name": "Relation Ontology",
            "download_url": "https://example.org/OBOREL2.tar.gz",
        },
        # OK, and nothing in the registry resembles it -- not worth reporting.
        {
            "id": "UNRELATED",
            "status": "OK",
            "name": "Some Other Ontology",
            "download_url": "https://example.org/UNRELATED.tar.gz",
        },
    ]
    monkeypatch.setattr(
        syncer, "fetch_manifest", lambda: {"ontologies": entries, "totals": {}}
    )

    stats = syncer.sync_all()

    assert stats["added"] == 1
    assert stats["unmatched"] == 2
    rows = syncer.report_path.read_text(encoding="utf-8").strip().splitlines()
    assert rows[0].split("\t") == [
        "acronym",
        "kg_bioportal_name",
        "reason",
        "suggested_resource",
    ]
    reported = {row.split("\t")[0]: row.split("\t") for row in rows[1:]}
    assert set(reported) == {"ZECO", "OBOREL2"}
    assert reported["OBOREL2"][3] == "ro"


# ------------------------------------------------------------------- sync map


def test_shipped_sync_map_is_internally_consistent():
    """The map must not both confirm and reject an acronym, or point nowhere."""
    syncer = KGBioportalSync()
    with open(syncer.map_path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    confirmed = {str(key).upper() for key in data.get("confirmed") or {}}
    rejected = {str(value).upper() for value in data.get("rejected") or []}
    assert not confirmed & rejected

    for acronym, resource_id in (data.get("confirmed") or {}).items():
        assert resource_id in syncer.resource_names, f"{acronym} points at missing {resource_id}"
