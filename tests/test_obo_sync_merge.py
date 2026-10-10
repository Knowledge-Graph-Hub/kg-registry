"""Tests for OBO Foundry sync merge behavior."""

import frontmatter
import pytest

from util.source_associations import resource_owns_product
from util.sync_obo_foundry import OBOFoundrySync


def test_merge_resource_metadata_preserves_curated_fields_products_and_publications(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    existing = {
        "id": "go",
        "infores_id": "go",
        "synonyms": ["GO"],
        "domains": ["biomedical"],
        "publications": [
            {
                "id": "PMID:10802651",
                "title": "Original title",
                "preferred": True,
            }
        ],
        "contacts": [
            {
                "category": "Organization",
                "label": "Gene Ontology Consortium",
                "contact_details": [{"contact_type": "url", "value": "https://geneontology.org/"}],
            }
        ],
        "products": [
            {
                "id": "go.owl",
                "name": "GO (OWL edition)",
                "category": "OntologyProduct",
                "product_file_size": 123,
                "warnings": ["cached warning"],
            },
            {
                "id": "go.api",
                "name": "Gene Ontology API",
                "category": "ProgrammingInterface",
                "product_url": "https://api.geneontology.org/",
            },
        ],
    }
    synced = {
        "id": "go",
        "name": "Gene Ontology",
        "description": "An ontology for describing the function of genes and gene products",
        "homepage_url": "http://geneontology.org/",
        "activity_status": "active",
        "category": "Ontology",
        "layout": "resource_detail",
        "collection": ["obo-foundry"],
        "domains": ["biological systems"],
        "contacts": [
            {
                "category": "Individual",
                "label": "Suzi Aleksander",
                "contact_details": [{"contact_type": "email", "value": "suzia@stanford.edu"}],
            }
        ],
        "products": [
            {
                "id": "go.owl",
                "name": "GO (OWL edition)",
                "description": "The main ontology in OWL",
                "category": "OntologyProduct",
                "product_url": "http://purl.obolibrary.org/obo/go.owl",
                "format": "owl",
            }
        ],
        "publications": [
            {
                "id": "PMID:10802651",
                "title": "Gene ontology: tool for the unification of biology. The Gene Ontology Consortium",
            },
            {
                "id": "https://doi.org/10.1093/nar/gkaf1271",
                "title": "The Gene Ontology resource: enriching a GOld mine",
            },
        ],
    }

    merged = syncer.merge_resource_metadata(existing, synced)
    merged_products = {product["id"]: product for product in merged["products"]}
    merged_publications = {publication["id"]: publication for publication in merged["publications"]}

    assert merged["infores_id"] == "go"
    assert merged["synonyms"] == ["GO"]
    assert merged["domains"] == ["biomedical", "biological systems"]
    assert len(merged["contacts"]) == 2
    assert set(merged_products) == {"go.owl", "go.api"}
    assert merged_products["go.owl"]["product_file_size"] == 123
    assert merged_products["go.owl"]["warnings"] == ["cached warning"]
    assert merged_products["go.owl"]["product_url"] == "http://purl.obolibrary.org/obo/go.owl"
    assert set(merged_publications) == {"PMID:10802651", "https://doi.org/10.1093/nar/gkaf1271"}
    assert merged_publications["PMID:10802651"]["preferred"] is True
    assert (
        merged_publications["PMID:10802651"]["title"]
        == "Gene ontology: tool for the unification of biology. The Gene Ontology Consortium"
    )


def test_sync_ontology_preserves_curated_body_and_extra_metadata(tmp_path):
    registry_root = tmp_path / "resource"
    resource_dir = registry_root / "go"
    resource_dir.mkdir(parents=True)
    resource_path = resource_dir / "go.md"
    resource_path.write_text(
        """---
id: go
name: Gene Ontology
infores_id: go
creation_date: '2025-03-16T00:00:00Z'
last_modified_date: '2026-04-10T00:00:00Z'
products:
- id: go.api
  name: Gene Ontology API
  category: ProgrammingInterface
  product_url: https://api.geneontology.org/
---
# Curated Notes

Keep this body.
""",
        encoding="utf-8",
    )

    syncer = OBOFoundrySync(registry_root=str(registry_root))
    syncer.sync_ontology(
        {
            "id": "go",
            "title": "Gene Ontology",
            "description": "An ontology for describing the function of genes and gene products",
            "homepage": "http://geneontology.org/",
            "domain": "biological systems",
            "products": [
                {
                    "id": "owl",
                    "title": "GO (OWL edition)",
                    "ontology_purl": "http://purl.obolibrary.org/obo/go.owl",
                    "format": "owl",
                }
            ],
        }
    )

    post = frontmatter.load(resource_path)
    products = {product["id"]: product for product in post.metadata["products"]}

    assert post.metadata["infores_id"] == "go"
    assert post.metadata["creation_date"] == "2025-03-16T00:00:00Z"
    assert post.metadata["last_modified_date"] == syncer._today_iso()
    assert set(products) == {"go.api", "go.owl"}
    assert "Keep this body." in post.content


@pytest.mark.parametrize(
    ("raw_identifier", "expected"),
    [
        (
            "https://www.ncbi.nlm.nih.gov/pubmed/10802651",
            "https://www.ncbi.nlm.nih.gov/pubmed/10802651",
        ),
        ("10.1093/nar/gkaf1271", "doi:10.1093/nar/gkaf1271"),
        ("10802651", "PMID:10802651"),
        (10802651, "PMID:10802651"),
    ],
)
def test_normalize_publication_id(raw_identifier, expected, tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    assert syncer._normalize_publication_id(raw_identifier) == expected


def test_transform_obo_to_kg_registry_emits_publication_ids(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    resource = syncer.transform_obo_to_kg_registry(
        {
            "id": "go",
            "title": "Gene Ontology",
            "publications": [
                {"id": "https://www.ncbi.nlm.nih.gov/pubmed/10802651", "title": "PubMed paper"},
                {"id": "10.1093/nar/gkaf1271", "title": "DOI paper"},
                {"id": "10802651", "title": "Numeric PMID"},
            ],
        }
    )

    assert resource["publications"] == [
        {"id": "https://www.ncbi.nlm.nih.gov/pubmed/10802651", "title": "PubMed paper"},
        {"id": "doi:10.1093/nar/gkaf1271", "title": "DOI paper"},
        {"id": "PMID:10802651", "title": "Numeric PMID"},
    ]


def test_merge_products_excludes_configured_product_ids(tmp_path):
    """Products listed in the exclusions config must never be (re-)added."""
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    # Inject an exclusion rather than depending on the shipped config file.
    syncer.product_exclusions = {"pcl": {"pcl.json", "pcl-base.owl"}}

    existing = [{"id": "pcl.owl"}, {"id": "pcl.obo"}]
    # The OBO registry advertises variant products that do not resolve.
    synced = [
        {"id": "pcl.owl"},
        {"id": "pcl.obo"},
        {"id": "pcl.json"},
        {"id": "pcl-base.owl"},
    ]

    merged = syncer.merge_products(existing, synced, excluded_ids=syncer.product_exclusions["pcl"])
    merged_ids = {p["id"] for p in merged}
    assert merged_ids == {"pcl.owl", "pcl.obo"}


def test_merge_products_strips_excluded_existing_products(tmp_path):
    """An excluded product already present is removed (and not re-synced)."""
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    excluded = {"t4fs-community.owl"}

    existing = [{"id": "t4fs.owl"}, {"id": "t4fs-community.owl"}]
    synced = [{"id": "t4fs.owl"}, {"id": "t4fs-community.owl"}]

    merged = syncer.merge_products(existing, synced, excluded_ids=excluded)
    assert {p["id"] for p in merged} == {"t4fs.owl"}


def test_transform_obo_namespaces_product_ids_under_the_ontology(tmp_path):
    """Every generated product id must be owned by its ontology.

    The OBO Foundry registry advertises ids in two shapes: path-style
    (`chebi/chebi_lite.obo`) and variant-style (`hancestro-base.owl`). The latter
    starts with the ontology id but its first dot-separated segment does not, so
    it has to be namespaced explicitly.
    """
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    resource = syncer.transform_obo_to_kg_registry(
        {
            "id": "hancestro",
            "title": "HANCESTRO",
            "products": [
                {"id": "hancestro.owl", "title": "HANCESTRO OWL"},
                {"id": "hancestro-base.owl", "title": "HANCESTRO Base"},
                {"id": "hancestro/subsets/basic.obo", "title": "HANCESTRO Basic"},
                {"id": "extras.json", "title": "Unprefixed extra"},
            ],
        }
    )

    assert [product["id"] for product in resource["products"]] == [
        "hancestro.owl",
        "hancestro.hancestro-base.owl",
        "hancestro.subsets.basic.obo",
        "hancestro.extras.json",
    ]
    for product in resource["products"]:
        assert resource_owns_product("hancestro", product["id"])


def test_merge_resource_metadata_keeps_curated_license_label_for_same_url(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    curated = {
        "id": "https://hpo.jax.org/app/license",
        "label": "HPO License (free with attribution; content may not be altered)",
    }
    synced_same = {"id": "https://hpo.jax.org/app/license", "label": "hpo"}
    synced_moved = {"id": "https://example.org/new-license", "label": "hpo"}
    baseline = {"fields": {"license": synced_same}, "products": {}}

    kept = syncer.merge_resource_metadata(
        {"id": "hp", "license": curated}, {"id": "hp", "license": synced_same}, baseline
    )
    assert kept["license"] == curated
    assert syncer.conflicts == []

    # Upstream moved the license too: both sides changed, so the curated
    # license stays and the clash is reported for review.
    clashed = syncer.merge_resource_metadata(
        {"id": "hp", "license": curated}, {"id": "hp", "license": synced_moved}, baseline
    )
    assert clashed["license"] == curated
    assert [(c["ontology"], c["field"]) for c in syncer.conflicts] == [("hp", "license")]

    # An untouched license follows upstream.
    followed = syncer.merge_resource_metadata(
        {"id": "hp", "license": synced_same}, {"id": "hp", "license": synced_moved}, baseline
    )
    assert followed["license"] == synced_moved

    filled = syncer.merge_resource_metadata({"id": "hp"}, {"id": "hp", "license": synced_same})
    assert filled["license"] == synced_same


def test_transform_obo_omits_license_when_upstream_has_none(tmp_path):
    """An ontology without a license upstream gets no license block.

    A placeholder such as ``label: Not specified`` counts as missing on the
    quality dashboard and in license inference, and it hides the gap on the
    page (#719). No block is the honest shape.
    """
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))

    for upstream in (
        {"id": "aao", "title": "AAO"},
        {"id": "aao", "title": "AAO", "license": {}},
        {"id": "aao", "title": "AAO", "license": None},
        {"id": "aao", "title": "AAO", "license": ""},
    ):
        resource = syncer.transform_obo_to_kg_registry(upstream)
        assert "license" not in resource, upstream
        page = syncer.create_resource_markdown(resource)
        assert "license" not in page.split("---")[1]

    with_license = syncer.transform_obo_to_kg_registry(
        {
            "id": "go",
            "title": "Gene Ontology",
            "license": {
                "url": "https://creativecommons.org/licenses/by/4.0/",
                "label": "CC BY 4.0",
            },
        }
    )
    assert with_license["license"] == {
        "id": "https://creativecommons.org/licenses/by/4.0/",
        "label": "CC BY 4.0",
    }

    label_only = syncer.transform_obo_to_kg_registry(
        {"id": "x", "title": "X", "license": {"label": "CC BY 3.0"}}
    )
    assert label_only["license"] == {"id": "", "label": "CC BY 3.0"}


def test_merge_resource_metadata_keeps_curated_license_when_sync_has_none(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    curated = {"id": "https://creativecommons.org/licenses/by/4.0/", "label": "CC BY 4.0"}

    merged = syncer.merge_resource_metadata({"id": "pao", "license": curated}, {"id": "pao"})
    assert merged["license"] == curated


# --- Local edits win over unchanged upstream values (#901) -----------------

FMA_OBO = {
    "id": "fma",
    "name": "Foundational Model of Anatomy Ontology",
    "repository": "https://bitbucket.org/uwsig/fma",
    "license": {
        "id": "http://sig.biostr.washington.edu/projects/fm/FMA_Release",
        "label": "CUSTOM",
    },
}


def _fma_baseline():
    return {
        "fields": {
            "name": FMA_OBO["name"],
            "repository": FMA_OBO["repository"],
            "license": FMA_OBO["license"],
        },
        "products": {},
    }


def test_local_edit_survives_when_upstream_is_unchanged(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    local = {
        "id": "fma",
        "name": "Foundational Model of Anatomy Ontology",
        "repository": "https://github.com/uw-sig/FMA",
        "license": {"id": "https://creativecommons.org/licenses/by/4.0/", "label": "CC BY 4.0"},
    }

    merged = syncer.merge_resource_metadata(local, dict(FMA_OBO), _fma_baseline())

    assert merged["repository"] == "https://github.com/uw-sig/FMA"
    assert merged["license"] == local["license"]
    assert syncer.conflicts == []


def test_upstream_change_applies_to_untouched_field(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    local = {"id": "fma", "name": FMA_OBO["name"], "repository": FMA_OBO["repository"]}
    incoming = dict(FMA_OBO, repository="https://github.com/uw-sig/FMA")

    merged = syncer.merge_resource_metadata(local, incoming, _fma_baseline())

    assert merged["repository"] == "https://github.com/uw-sig/FMA"
    assert syncer.conflicts == []


def test_both_sides_changed_keeps_local_and_reports(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    local = {"id": "fma", "name": "FMA (curated name)", "repository": FMA_OBO["repository"]}
    incoming = dict(FMA_OBO, name="Foundational Model of Anatomy")

    merged = syncer.merge_resource_metadata(local, incoming, _fma_baseline())

    assert merged["name"] == "FMA (curated name)"
    assert syncer.conflicts == [
        {
            "ontology": "fma",
            "field": "name",
            "local": "FMA (curated name)",
            "last_synced": FMA_OBO["name"],
            "incoming": "Foundational Model of Anatomy",
        }
    ]


def test_without_sync_record_local_value_is_kept_and_reported(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    local = {"id": "fma", "repository": "https://github.com/uw-sig/FMA"}

    merged = syncer.merge_resource_metadata(local, dict(FMA_OBO))

    assert merged["repository"] == "https://github.com/uw-sig/FMA"
    # Fields the page lacks are still filled from upstream.
    assert merged["name"] == FMA_OBO["name"]
    assert [c["field"] for c in syncer.conflicts] == ["repository"]
    assert syncer.conflicts[0]["last_synced"] is None


def test_product_fields_follow_the_same_rule(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    baseline = {
        "fields": {},
        "products": {
            "fma.owl": {
                "description": "FMA (subset) in OWL format",
                "product_url": "http://purl.obolibrary.org/obo/fma.owl",
            }
        },
    }
    local = {
        "id": "fma",
        "products": [
            {
                "id": "fma.owl",
                "description": "Curated description",
                "product_url": "http://purl.obolibrary.org/obo/fma.owl",
                "product_file_size": 208047132,
            }
        ],
    }
    incoming = {
        "id": "fma",
        "products": [
            {
                "id": "fma.owl",
                "description": "FMA (subset) in OWL format",
                "product_url": "http://purl.org/sig/ont/fma.owl",
            }
        ],
    }

    merged = syncer.merge_resource_metadata(local, incoming, baseline)
    product = merged["products"][0]

    assert product["description"] == "Curated description"
    assert product["product_url"] == "http://purl.org/sig/ont/fma.owl"
    assert product["product_file_size"] == 208047132
    assert syncer.conflicts == []


def test_product_removed_locally_is_not_re_added(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    baseline = {"fields": {}, "products": {"go.owl": {}, "go.obo": {}}}
    incoming = [{"id": "go.owl"}, {"id": "go.obo"}, {"id": "go.json"}]

    merged = syncer.merge_products(
        [{"id": "go.owl"}], incoming, baseline_products=baseline["products"], ontology_id="go"
    )

    # go.obo was synced before and removed by a curator; go.json is new upstream.
    assert [p["id"] for p in merged] == ["go.owl", "go.json"]


def test_last_modified_date_unchanged_when_nothing_changes(tmp_path):
    registry_root = tmp_path / "resource"
    (registry_root / "fma").mkdir(parents=True)
    page = registry_root / "fma" / "fma.md"
    record = {
        "id": "fma",
        "title": "Foundational Model of Anatomy Ontology",
        "repository": "https://bitbucket.org/uwsig/fma",
    }
    syncer = OBOFoundrySync(
        registry_root=str(registry_root), state_path=str(tmp_path / "state.yml")
    )
    synced = syncer.transform_obo_to_kg_registry(record)
    syncer.state["ontologies"]["fma"] = syncer.snapshot(synced)
    # The page carries everything the sync would write, except a curated repository.
    page_metadata = dict(
        synced,
        repository="https://github.com/uw-sig/FMA",
        creation_date="2025-06-25T00:00:00Z",
        last_modified_date="2026-10-09T00:00:00Z",
    )
    page.write_text(syncer._serialize_resource(page_metadata, "Body."), encoding="utf-8")
    syncer.existing_resources = syncer._load_existing_resources()

    before = page.read_text(encoding="utf-8")
    assert syncer.sync_ontology(record)

    assert page.read_text(encoding="utf-8") == before
    assert syncer.conflicts == []


def test_sync_all_saves_state_and_dry_run_writes_nothing(tmp_path, monkeypatch):
    registry_root = tmp_path / "resource"
    (registry_root / "fma").mkdir(parents=True)
    page = registry_root / "fma" / "fma.md"
    page.write_text("---\nid: fma\nname: Old name\n---\nBody.\n", encoding="utf-8")
    state_path = tmp_path / "state.yml"
    record = {"id": "fma", "title": "Foundational Model of Anatomy Ontology"}

    syncer = OBOFoundrySync(registry_root=str(registry_root), state_path=str(state_path))
    monkeypatch.setattr(syncer, "fetch_obo_foundry_data", lambda: [record])
    before = page.read_text(encoding="utf-8")
    stats = syncer.sync_all(dry_run=True)
    assert page.read_text(encoding="utf-8") == before
    assert not state_path.exists()
    assert stats["conflicts"] == 1

    syncer = OBOFoundrySync(registry_root=str(registry_root), state_path=str(state_path))
    monkeypatch.setattr(syncer, "fetch_obo_foundry_data", lambda: [record])
    syncer.sync_all()
    reloaded = OBOFoundrySync(registry_root=str(registry_root), state_path=str(state_path))
    assert reloaded.state["ontologies"]["fma"]["fields"]["name"] == record["title"]


def test_seed_state_records_values_without_sources(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    seeded = syncer.seed_state(
        [
            {
                "id": "fma",
                "title": "FMA",
                "products": [{"id": "fma.owl", "ontology_purl": "http://x/fma.owl"}],
            }
        ]
    )

    assert seeded == 1
    entry = syncer.state["ontologies"]["fma"]
    assert entry["fields"]["name"] == "FMA"
    assert "original_source" not in entry["products"]["fma.owl"]


# --- Ontology dependencies become product sources (#421) -------------------


def _registry_with(tmp_path, *ids):
    root = tmp_path / "resource"
    for resource_id in ids:
        (root / resource_id).mkdir(parents=True, exist_ok=True)
        (root / resource_id / f"{resource_id}.md").write_text(f"---\nid: {resource_id}\n---\n")
    return root


def test_dependencies_become_sources_on_non_base_products(tmp_path):
    root = _registry_with(tmp_path, "bfo", "ro")
    syncer = OBOFoundrySync(registry_root=str(root))

    resource = syncer.transform_obo_to_kg_registry(
        {
            "id": "cl",
            "title": "Cell Ontology",
            "dependencies": [
                {"id": "bfo"},
                {"id": "ro"},
                {"id": "notinregistry"},
                {"id": "go/extensions/go-bridge-to-nifstd.owl", "type": "BridgeOntology"},
            ],
            "products": [
                {"id": "cl.owl"},
                {"id": "cl/cl-base.owl"},
                {"id": "cl/cl-basic.obo"},
            ],
        }
    )
    sources = {p["id"]: [s["source"] for s in p["original_source"]] for p in resource["products"]}

    assert sources == {
        "cl.owl": ["cl", "bfo", "ro"],
        "cl.cl-base.owl": ["cl"],
        "cl.cl-basic.obo": ["cl", "bfo", "ro"],
    }


def test_dependency_sources_merge_with_curated_sources(tmp_path):
    syncer = OBOFoundrySync(registry_root=str(tmp_path / "resource"))
    own = {"relation_type": "prov:hadPrimarySource", "source": "cl"}
    bfo = {"relation_type": "prov:hadPrimarySource", "source": "bfo"}
    ro = {"relation_type": "prov:hadPrimarySource", "source": "ro"}
    uberon = {"relation_type": "prov:hadPrimarySource", "source": "uberon"}
    curated = {"relation_type": "prov:wasDerivedFrom", "source": "hpa"}

    # First sync after seeding: no recorded sources, so every upstream source is added.
    merged = syncer.merge_products(
        [{"id": "cl.owl", "original_source": [own, curated]}],
        [{"id": "cl.owl", "original_source": [own, bfo, ro]}],
        baseline_products={"cl.owl": {}},
        ontology_id="cl",
    )
    assert merged[0]["original_source"] == [own, curated, bfo, ro]

    # Upstream later drops ro and adds uberon; the curated source stays.
    merged = syncer.merge_products(
        merged,
        [{"id": "cl.owl", "original_source": [own, bfo, uberon]}],
        baseline_products={"cl.owl": {"original_source": [own, bfo, ro]}},
        ontology_id="cl",
    )
    assert merged[0]["original_source"] == [own, curated, bfo, uberon]
