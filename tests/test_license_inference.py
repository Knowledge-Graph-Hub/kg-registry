"""Tests for upstream license inference on aggregate resources."""

import frontmatter
import yaml

from util.license_inference import (
    STATUS_INFERRED,
    STATUS_PROVIDED,
    TIERS,
    LicenseIndex,
    apply_inferred_licenses,
    classify_license,
    has_declared_license,
    is_inferred_license,
    most_restrictive,
    upstream_sources,
)

CC0 = {"id": "https://creativecommons.org/publicdomain/zero/1.0/", "label": "CC0-1.0"}
CC_BY = {"id": "https://creativecommons.org/licenses/by/4.0/", "label": "CC BY 4.0"}
CC_BY_SA = {"id": "https://creativecommons.org/licenses/by-sa/4.0/", "label": "CC-BY-SA-4.0"}
CC_BY_NC = {"id": "https://creativecommons.org/licenses/by-nc/4.0/", "label": "CC BY-NC 4.0"}
CC_BY_ND = {"id": "https://creativecommons.org/licenses/by-nd/4.0/", "label": "CC BY-ND 4.0"}
CUSTOM = {"id": "https://www.omim.org/help/agreement", "label": "Custom"}


def _resource(resource_id, category="DataSource", license=None, products=None, **extra):
    resource = {"id": resource_id, "name": resource_id, "category": category}
    if license is not None:
        resource["license"] = license
    if products is not None:
        resource["products"] = products
    resource.update(extra)
    return resource


def _product(
    product_id, sources=None, relation="prov:hadPrimarySource", license=None, secondary=None
):
    product = {"id": product_id, "name": product_id, "category": "GraphProduct"}
    if sources:
        product["original_source"] = [{"source": s, "relation_type": relation} for s in sources]
    if secondary:
        product["secondary_source"] = [{"source": s, "relation_type": r} for s, r in secondary]
    if license is not None:
        product["license"] = license
    return product


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------


def test_tier_order_is_least_to_most_restrictive():
    assert TIERS == (
        "public domain",
        "permissive",
        "copyleft",
        "non-commercial",
        "no derivatives",
        "custom",
    )
    assert most_restrictive(["permissive", None, "public domain"]) == "permissive"
    assert most_restrictive(["copyleft", "custom", "non-commercial"]) == "custom"
    assert most_restrictive([None, None]) is None


def test_classify_by_url():
    cases = {
        "public domain": [
            CC0["id"],
            "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
            "https://creativecommons.org.publicdomain/zero/1.0/",
            "https://www.usa.gov/government-works",
        ],
        "permissive": [
            CC_BY["id"],
            "https://creativecommons.org/licenses/by/",
            "https://www.apache.org/licenses/",
            "https://opensource.org/license/mit/",
            "https://www.apache.org/licenses/LICENSE-2.0",
            "https://opendatacommons.org/licenses/by/1-0/",
        ],
        "copyleft": [
            CC_BY_SA["id"],
            "https://opendatacommons.org/licenses/odbl/1-0/",
            "https://www.gnu.org/licenses/gpl-3.0.en.html",
            "https://www.gnu.org/licenses/",
            "https://opensource.org/license/gpl-3-0",
            "https://opensource.org/licenses/LGPL-2.1",
        ],
        "non-commercial": [CC_BY_NC["id"], "https://creativecommons.org/licenses/by-nc-sa/4.0/"],
        "no derivatives": [
            CC_BY_ND["id"],
            "https://creativecommons.org/licenses/by-nc-nd/3.0/igo/deed.en",
        ],
        "custom": [CUSTOM["id"]],
    }
    for tier, urls in cases.items():
        for url in urls:
            assert classify_license({"id": url}) == tier, url


def test_classify_falls_back_to_label_when_url_unknown_or_missing():
    cases = [
        ("", "US federal government public domain", "public domain"),
        ("https://www.ncbi.nlm.nih.gov/home/about/policies/", "Public Domain", "public domain"),
        ("https://www.bindingdb.org/rwd/bind/info.jsp", "CC BY 4.0", "permissive"),
        ("", "Open Database License (ODbL) 1.0", "copyleft"),
        ("http://cpdb.molgen.mpg.de/", "Free for academic use", "non-commercial"),
        ("https://example.org/x", "Varies", "custom"),
        # Free use with attribution is permissive; a ban on altering content is no derivatives.
        ("https://example.org/mesh", "Freely provided with attribution", "permissive"),
        (
            "https://example.org/hpo",
            "Free with attribution; content may not be altered",
            "no derivatives",
        ),
        # A mixed label lands on the most restrictive license it names,
        # with or without a recognized URL beside it.
        ("", "CC0, CC BY, and CC BY-NC (mixed)", "non-commercial"),
        (CC0["id"], "CC0, CC BY, and CC BY-NC (mixed)", "non-commercial"),
        (CC0["id"], "CC0 and CC BY (mixed)", "permissive"),
        # A label that matches nothing does not loosen or tighten a known URL.
        (CC_BY["id"], "Custom", "permissive"),
        # "non-commercial and commercial" in either order is a grant, not a restriction.
        (
            "https://www.ema.europa.eu/en/legal-notice",
            "May be reproduced for non-commercial and commercial purposes with acknowledgement",
            "permissive",
        ),
        ("https://example.org/a", "Free for commercial and non-commercial use", "permissive"),
        ("https://example.org/b", "Free for non-commercial and commercial use", "permissive"),
        # Spellings seen in the registry.
        (
            "https://www.omim.org/help/agreement",
            "OMIM Use Agreement (research/educational use; license required for commercial use)",
            "non-commercial",
        ),
        ("https://example.org/c", "GPLv3", "copyleft"),
        ("https://example.org/d", "LGPL-2.1", "copyleft"),
    ]
    for url, label, tier in cases:
        assert classify_license({"id": url, "label": label}) == tier, label


def test_placeholders_and_inferred_do_not_count_as_declared():
    assert not has_declared_license(None)
    assert not has_declared_license({})
    assert not has_declared_license({"id": "", "label": "Not specified"})
    assert has_declared_license({"id": "", "label": "Public Domain"})
    assert has_declared_license(CC_BY)
    assert classify_license({"id": "", "label": "Not specified"}) is None
    inferred = dict(CC_BY, status=STATUS_INFERRED, inferred_from=["x"])
    assert is_inferred_license(inferred)
    assert not is_inferred_license(CC_BY)
    assert not has_declared_license(inferred)
    assert classify_license(inferred) is None


# ---------------------------------------------------------------------------
# Upstream discovery
# ---------------------------------------------------------------------------


def test_upstream_sources_respects_relations_ownership_and_self():
    kg = _resource(
        "kg",
        category="KnowledgeGraph",
        components=["comp"],
        products=[
            _product(
                "kg.graph",
                ["a", "kg", "b.owl"],
                secondary=[("agg", "prov:wasInfluencedBy"), ("c", "prov:used")],
            ),
            _product("kg.api", ["a"], relation="prov:wasInformedBy"),
            # Propagated from elsewhere: not owned by kg, its provenance is not kg's.
            _product("other.graph", ["z"]),
        ],
    )
    assert upstream_sources(kg) == ["comp", "a", "b.owl", "c"]


# ---------------------------------------------------------------------------
# Inference
# ---------------------------------------------------------------------------


def test_infers_most_restrictive_and_lists_winners():
    nc_http = {"id": "http://creativecommons.org/licenses/by-nc/4.0/", "label": "CC-BY-NC"}
    resources = [
        _resource("pd", license=CC0),
        _resource("by", license=CC_BY),
        _resource("nc", license=CC_BY_NC),
        _resource("nc2", license=nc_http),
        _resource(
            "kg",
            category="KnowledgeGraph",
            products=[_product("kg.graph", ["pd", "by", "nc", "nc2", "ghost"])],
        ),
    ]
    index = LicenseIndex(resources)
    inferred = index.infer(resources[-1])
    assert inferred is not None
    assert inferred["status"] == STATUS_INFERRED
    assert inferred["restrictiveness"] == "non-commercial"
    assert inferred["inferred_from"] == ["nc", "nc2"]
    assert inferred["unresolved_sources"] == ["ghost"]
    # http and https forms of the same license count as one; the first-seen URL is kept.
    assert inferred["id"] == CC_BY_NC["id"]
    assert inferred["label"] in {"CC BY-NC 4.0", "CC-BY-NC"}


def test_product_license_beats_resource_license_and_products_back_fill():
    resources = [
        _resource(
            "src",
            license=CC0,
            products=[
                _product("src.restricted", license=CC_BY_ND),
                _product("src.open", license=CC_BY),
            ],
        ),
        _resource(
            "nolic",
            products=[_product("nolic.a", license=CC_BY), _product("nolic.b", license=CC_BY_SA)],
        ),
        _resource(
            "kg1", category="KnowledgeGraph", products=[_product("kg1.graph", ["src.restricted"])]
        ),
        _resource("kg2", category="KnowledgeGraph", products=[_product("kg2.graph", ["src"])]),
        _resource("kg3", category="KnowledgeGraph", products=[_product("kg3.graph", ["nolic"])]),
    ]
    index = LicenseIndex(resources)
    assert index.infer(resources[2])["restrictiveness"] == "no derivatives"
    assert index.infer(resources[3])["restrictiveness"] == "public domain"
    # A resource with no license but licensed products takes the most restrictive of those.
    assert index.infer(resources[4])["restrictiveness"] == "copyleft"


def test_inference_is_transitive_and_survives_cycles():
    resources = [
        _resource("leaf", license=CUSTOM),
        _resource(
            "mid", category="KnowledgeGraph", products=[_product("mid.graph", ["leaf", "top"])]
        ),
        _resource("top", category="KnowledgeGraph", products=[_product("top.graph", ["mid"])]),
        _resource(
            "orphan", category="KnowledgeGraph", products=[_product("orphan.graph", ["nothing"])]
        ),
    ]
    index = LicenseIndex(resources)
    top = index.infer(resources[2])
    assert top["restrictiveness"] == "custom"
    assert top["inferred_from"] == ["mid"]
    mid = index.infer(resources[1])
    assert mid["restrictiveness"] == "custom"
    # "top" sits in a cycle with "mid". Its only license is the one it takes
    # from "mid", so from "mid" it is unresolved, not a contributor.
    assert mid["inferred_from"] == ["leaf"]
    assert mid["unresolved_sources"] == ["top"]
    assert index.infer(resources[3]) is None


def test_stale_inferred_license_on_a_source_is_recomputed_not_trusted():
    # A page may still carry an inferred block from an earlier build. It is not a
    # provided license, so resolution recomputes from that source's own upstream.
    stale = dict(CC0, status=STATUS_INFERRED, inferred_from=["gone"])
    resources = [
        _resource("leaf", license=CC_BY_NC),
        _resource(
            "mid",
            category="KnowledgeGraph",
            license=stale,
            products=[_product("mid.graph", ["leaf"])],
        ),
        _resource("top", category="KnowledgeGraph", products=[_product("top.graph", ["mid"])]),
    ]
    inferred = LicenseIndex(resources).infer(resources[2])
    assert inferred["restrictiveness"] == "non-commercial"


# ---------------------------------------------------------------------------
# Application and write-back
# ---------------------------------------------------------------------------


def _write_page(root, metadata):
    page_dir = root / "resource" / metadata["id"]
    page_dir.mkdir(parents=True)
    page = page_dir / f"{metadata['id']}.md"
    with page.open("w", encoding="utf-8") as handle:
        handle.write("---\n")
        yaml.safe_dump(metadata, handle, sort_keys=False)
        handle.write("---\n\n# Page\n")
    return page


def _license_block(lines):
    start = lines.index("license:")
    stop = next(
        i for i in range(start + 1, len(lines)) if lines[i][:1].isalpha() or lines[i] == "---"
    )
    return start, stop


def test_apply_writes_only_inheriting_unlicensed_pages_and_never_overwrites(tmp_path):
    stale = {
        "id": "stale",
        "name": "stale",
        "category": "KnowledgeGraph",
        "license": {
            "id": CUSTOM["id"],
            "label": "Custom",
            "status": STATUS_INFERRED,
            "restrictiveness": "custom",
            "inferred_from": ["gone"],
            "unresolved_sources": [],
        },
        "products": [_product("stale.graph", ["src"])],
    }
    objs = [
        _resource("src", license=CC_BY_SA),
        _resource("kg", category="KnowledgeGraph", products=[_product("kg.graph", ["src"])]),
        _resource("ds", category="DataSource", products=[_product("ds.graph", ["src"])]),
        _resource("alone", category="Aggregator"),
        _resource(
            "declared",
            category="KnowledgeGraph",
            license=CC_BY,
            products=[_product("declared.graph", ["src"])],
        ),
        _resource(
            "placeholder",
            category="KnowledgeGraph",
            license={"id": "", "label": "Not specified"},
            products=[_product("placeholder.graph", ["src"])],
        ),
        stale,
    ]
    pages = {obj["id"]: _write_page(tmp_path, obj) for obj in objs}
    originals = {rid: page.read_text(encoding="utf-8") for rid, page in pages.items()}

    summary = apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")

    assert summary["inferred"] == ["kg", "stale"]
    assert summary["removed"] == []
    assert summary["unresolved"] == ["alone"]
    assert summary["placeholder"] == ["placeholder"]
    assert sorted(summary["written"]) == ["kg", "stale"]

    expected = {
        "id": CC_BY_SA["id"],
        "label": CC_BY_SA["label"],
        "status": STATUS_INFERRED,
        "restrictiveness": "copyleft",
        "inferred_from": ["src"],
        "unresolved_sources": [],
    }
    assert frontmatter.load(str(pages["kg"])).metadata["license"] == expected
    # The stale inferred block was replaced in place.
    assert frontmatter.load(str(pages["stale"])).metadata["license"] == expected
    # Provided and placeholder licenses are untouched, on disk and in memory.
    assert pages["declared"].read_text(encoding="utf-8") == originals["declared"]
    assert pages["placeholder"].read_text(encoding="utf-8") == originals["placeholder"]
    assert objs[4]["license"] == CC_BY
    assert objs[5]["license"] == {"id": "", "label": "Not specified"}
    assert "license" not in objs[2]
    assert pages["ds"].read_text(encoding="utf-8") == originals["ds"]

    # The page body is preserved, and so is every other line of the front matter.
    assert frontmatter.load(str(pages["kg"])).content.strip() == "# Page"
    rewritten = pages["kg"].read_text(encoding="utf-8").split("\n")
    start, stop = _license_block(rewritten)
    assert rewritten[:start] + rewritten[stop:] == originals["kg"].split("\n")
    # The new block sits where a key sort would put it.
    keys = [line.split(":", 1)[0] for line in rewritten[1:] if line and line[0].isalpha()]
    assert keys.index("license") == keys.index("id") + 1 < keys.index("name")

    # A second pass with nothing changed writes nothing.
    summary = apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")
    assert summary["written"] == []

    statuses = {row["resource_id"]: row["status"] for row in summary["rows"]}
    assert statuses == {
        "kg": "inferred",
        "stale": "inferred",
        "alone": "no-upstream",
        "declared": "conflict",
        "placeholder": "placeholder",
    }


def test_apply_removes_inferred_block_when_sources_no_longer_resolve(tmp_path):
    kg = _resource(
        "kg",
        category="KnowledgeGraph",
        license=dict(CC_BY, status=STATUS_INFERRED, inferred_from=["src"]),
        products=[_product("kg.graph", ["src"])],
    )
    objs = [_resource("src"), kg]
    page = _write_page(tmp_path, kg)
    summary = apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")
    assert summary["removed"] == ["kg"]
    assert summary["written"] == ["kg"]
    assert "license" not in kg
    assert "license" not in frontmatter.load(str(page)).metadata


def test_code_constants_match_schema_enums():
    # The values written to pages are plain strings. The schema validates them
    # against these enums, so the two lists must not drift apart.
    from util.common import SOURCE_SCHEMA_PATH

    schema = yaml.safe_load(SOURCE_SCHEMA_PATH.read_text())
    enums = schema["enums"]
    assert list(enums["LicenseRestrictivenessEnum"]["permissible_values"]) == list(TIERS)
    assert list(enums["LicenseStatusEnum"]["permissible_values"]) == [
        STATUS_PROVIDED,
        STATUS_INFERRED,
    ]


def test_apply_fills_an_empty_license_block_and_reports_refusals(tmp_path, capsys):
    empty = _resource(
        "empty", category="KnowledgeGraph", products=[_product("empty.graph", ["src"])]
    )
    missing = _resource(
        "missing", category="KnowledgeGraph", products=[_product("missing.graph", ["src"])]
    )
    objs = [_resource("src", license=CC_BY_NC), empty, missing]
    page = _write_page(tmp_path, empty)
    # A bare key with nothing under it, as a hand-written page may carry.
    page.write_text(
        page.read_text(encoding="utf-8").replace("id: empty\n", "id: empty\nlicense:\n")
    )
    # "missing" has no page at all.

    summary = apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")

    assert frontmatter.load(str(page)).metadata["license"]["status"] == STATUS_INFERRED
    assert summary["written"] == ["empty"]
    assert summary["refused"] == ["missing"]
    assert summary["inferred"] == ["empty"]
    # The export never shows a license the page does not carry.
    assert "license" not in missing
    assert "not written" in capsys.readouterr().out


def test_reflowed_inferred_block_is_not_rewritten(tmp_path):
    kg = _resource("kg", category="KnowledgeGraph", products=[_product("kg.graph", ["src"])])
    objs = [_resource("src", license=CC_BY_SA), kg]
    page = _write_page(tmp_path, kg)
    apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")
    # Another build step re-indents the page the way the ruamel handler does.
    text = page.read_text(encoding="utf-8")
    reflowed = text.replace("  inferred_from:\n  - src\n", "  inferred_from:\n    - src\n")
    assert reflowed != text
    page.write_text(reflowed, encoding="utf-8")

    summary = apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")
    assert summary["written"] == []
    assert page.read_text(encoding="utf-8") == reflowed


def test_indented_dashes_inside_a_scalar_are_not_the_front_matter_close(tmp_path):
    kg = _resource(
        "kg",
        category="KnowledgeGraph",
        description="First line\n  ---\nstill the description",
        products=[_product("kg.graph", ["src"])],
    )
    objs = [_resource("src", license=CC_BY), kg]
    page = _write_page(tmp_path, kg)
    original = frontmatter.load(str(page))
    assert "---" in original.metadata["description"]

    apply_inferred_licenses(objs, write=True, resource_dir=tmp_path / "resource")

    rewritten = frontmatter.load(str(page))
    assert rewritten.metadata["description"] == original.metadata["description"]
    assert rewritten.metadata["license"]["status"] == STATUS_INFERRED
    assert rewritten.content == original.content


def test_nested_walks_are_memoized_and_cycles_are_not():
    resources = [
        _resource("leaf", license=CC_BY_NC),
        _resource(
            "shared", category="KnowledgeGraph", products=[_product("shared.graph", ["leaf"])]
        ),
        _resource("a", category="KnowledgeGraph", products=[_product("a.graph", ["shared"])]),
        _resource("b", category="KnowledgeGraph", products=[_product("b.graph", ["shared"])]),
        _resource("x", category="KnowledgeGraph", products=[_product("x.graph", ["y"])]),
        _resource("y", category="KnowledgeGraph", products=[_product("y.graph", ["x", "leaf"])]),
    ]
    index = LicenseIndex(resources)
    computed = []
    original = index._infer

    def counting(resource, visiting):
        if resource["id"] not in index._inferred:
            computed.append(resource["id"])
        return original(resource, visiting)

    index._infer = counting
    assert index.infer(resources[2])["restrictiveness"] == "non-commercial"
    assert index.infer(resources[3])["restrictiveness"] == "non-commercial"
    # "shared" was reached below a root and still computed only once.
    assert computed.count("shared") == 1
    # A walk cut by the cycle guard is right for its root but not cached.
    assert index.infer(resources[4])["restrictiveness"] == "non-commercial"
    assert "x" not in index._inferred
    assert "y" not in index._inferred
