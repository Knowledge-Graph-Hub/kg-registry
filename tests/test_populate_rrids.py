"""Tests for the SciCrunch RRID backfill matching logic (util/populate_rrids.py).

All tests run offline against a recorded resolver response, so the default
test run never touches the network.
"""

import io
import json
import pathlib

import pytest

from util.populate_rrids import (
    confirm_rrid,
    extract_resolver_record,
    landing_url_matches,
    name_matches,
    names_compatible,
    normalize_url,
    registered_domain,
    registered_domain_matches,
    search_scicrunch,
    splice_rrid,
)

PAGE = """---
activity_status: active
id: zirc
name: Zebrafish International Resource Center
products:
- category: Product
  id: zirc.something
synonyms:
- ZIRC
taxon:
- NCBITaxon:7955
---

# Body text stays exactly as it was.
"""

FIXTURE = pathlib.Path(__file__).parent / "fixtures" / "scicrunch_resolver_scr_005065.json"


@pytest.fixture
def resolver_json():
    return json.loads(FIXTURE.read_text())


@pytest.fixture
def record(resolver_json):
    return extract_resolver_record(resolver_json)


def test_normalize_url():
    assert normalize_url("https://zebrafish.org/") == "zebrafish.org"
    assert normalize_url("http://www.zebrafish.org") == "zebrafish.org"
    assert normalize_url("http://zebrafish.org") == "zebrafish.org"
    assert normalize_url("https://mps.csb.pitt.edu/") == "mps.csb.pitt.edu"
    assert normalize_url("") == ""
    assert normalize_url(None) == ""
    # Differing schemes and trailing slashes normalize to the same value.
    assert normalize_url("http://zebrafish.org") == normalize_url("https://zebrafish.org/")


def test_extract_resolver_record(record):
    assert record is not None
    assert record["identifier"] == "SCR_005065"
    assert record["name"] == "Zebrafish International Resource Center"
    assert "ZIRC" in record["abbreviations"]
    assert "http://zebrafish.org" in record["landing_urls"]


def test_extract_resolver_record_empty():
    assert extract_resolver_record({}) is None
    assert extract_resolver_record({"hits": {"hits": []}}) is None


def test_landing_url_matches(record):
    # Resolver landing is http://zebrafish.org; our homepage is https://zebrafish.org/
    assert landing_url_matches(record, "https://zebrafish.org/") is True
    assert landing_url_matches(record, "http://www.zebrafish.org") is True
    assert landing_url_matches(record, "https://example.org/") is False
    assert landing_url_matches(record, "") is False


def test_name_matches(record):
    assert name_matches(record, "Zebrafish International Resource Center") is True
    assert name_matches(record, "ZIRC") is True  # via abbreviation
    assert name_matches(record, "some unrelated name") is False
    # Case-insensitive.
    assert name_matches(record, "zebrafish international resource center") is True


def test_confirm_rrid_high_confidence_on_url(record):
    high, reasons = confirm_rrid(
        record, "https://zebrafish.org/", "Zebrafish International Resource Center"
    )
    assert high is True
    assert any("landing page" in r for r in reasons)


def test_confirm_rrid_name_only_not_sufficient(record):
    # Name matches but homepage does not -> not auto-written, reported instead.
    high, reasons = confirm_rrid(
        record, "https://unrelated.example/", "Zebrafish International Resource Center"
    )
    assert high is False
    assert any("name" in r for r in reasons)


def test_confirm_rrid_no_record():
    high, reasons = confirm_rrid(None, "https://zebrafish.org/", "Zebrafish")
    assert high is False
    assert reasons


def test_registered_domain():
    assert registered_domain("https://data.4dnucleome.org/") == "4dnucleome.org"
    assert registered_domain("http://www.4dnucleome.org") == "4dnucleome.org"
    assert registered_domain("http://purl.obolibrary.org/obo/aero") == "obolibrary.org"
    assert registered_domain("https://example.co.uk/path") == "example.co.uk"
    assert registered_domain("") == ""


# The real-world cases that drove the domain+name gate (test batch, issue #757).
FOURDN = {
    "identifier": "SCR_016925",
    "name": "4D Nucleome",
    "synonyms": [],
    "abbreviations": [],
    "landing_urls": ["https://www.4dnucleome.org"],
}
IAO = {
    "identifier": "SCR_000477",
    "name": "Information Artifact Ontology",
    "synonyms": [],
    "abbreviations": [],
    "landing_urls": ["http://purl.obolibrary.org/obo/iao.owl"],
}


def test_names_compatible_token_subset():
    # "4D Nucleome" is a salient-token subset of "4D Nucleome Data Portal".
    assert names_compatible(FOURDN, "4D Nucleome Data Portal") is True
    # Different ontologies do not agree on salient words.
    assert names_compatible(IAO, "Adverse Event Reporting Ontology") is False


def test_registered_domain_matches_excludes_shared_hosts():
    # 4dn: data.4dnucleome.org vs www.4dnucleome.org -> same registered domain.
    assert registered_domain_matches(FOURDN, "https://data.4dnucleome.org/") is True
    # aero vs IAO: both on obolibrary.org, a shared host -> not a domain match.
    assert registered_domain_matches(IAO, "http://purl.obolibrary.org/obo/aero") is False


def test_confirm_rrid_domain_plus_name_writes_4dn():
    high, reasons = confirm_rrid(FOURDN, "https://data.4dnucleome.org/", "4D Nucleome Data Portal")
    assert high is True
    assert any("registered domain" in r for r in reasons)


def test_confirm_rrid_shared_host_collision_rejected():
    # aero's homepage and IAO's landing collide on obolibrary.org, but it is a
    # shared host and the names disagree -> must not auto-write.
    high, reasons = confirm_rrid(
        IAO, "http://purl.obolibrary.org/obo/aero", "Adverse Event Reporting Ontology"
    )
    assert high is False


def test_search_without_key_returns_empty():
    # No API key -> empty list, no network call.
    assert search_scicrunch("zebrafish", "") == []


def test_search_sends_apikey_header_and_parses_hits(resolver_json):
    # Build a search-style response from the recorded _source, and a fake opener
    # that records the request so we can assert the apikey header is sent.
    source = resolver_json["hits"]["hits"][0]["_source"]
    search_body = json.dumps({"hits": {"hits": [{"_source": source}]}}).encode()
    captured = {}

    def fake_opener(request, timeout=None):
        captured["url"] = request.full_url
        captured["headers"] = {k.lower(): v for k, v in request.header_items()}
        return io.BytesIO(search_body)

    result = search_scicrunch(
        "Zebrafish International Resource Center", "SECRET_KEY", opener=fake_opener
    )
    assert result == ["SCR_005065"]
    assert captured["headers"].get("apikey") == "SECRET_KEY"
    assert "RIN_Tool_pr/_search" in captured["url"]
    # Key is sent as a header, not leaked into the query string.
    assert "SECRET_KEY" not in captured["url"]


def test_splice_rrid_inserts_at_sorted_position():
    out = splice_rrid(PAGE, "SCR_005065")
    # Exactly one line added.
    assert out.count("\n") == PAGE.count("\n") + 1
    assert "rrid: SCR_005065" in out
    # Placed alphabetically: after 'products', before 'synonyms'.
    lines = out.split("\n")
    rrid_i = lines.index("rrid: SCR_005065")
    assert lines[rrid_i - 1].startswith("- NCBITaxon") is False
    assert any(l == "synonyms:" for l in lines[rrid_i:])
    assert any(l == "products:" for l in lines[:rrid_i])
    # Body and every other line are byte-for-byte unchanged.
    assert "# Body text stays exactly as it was." in out
    for line in PAGE.split("\n"):
        assert line in lines


def test_splice_rrid_idempotent():
    out = splice_rrid(PAGE, "SCR_005065")
    assert splice_rrid(out, "SCR_999999") == out  # already present -> unchanged


def test_splice_rrid_requires_frontmatter():
    with pytest.raises(ValueError):
        splice_rrid("no frontmatter here", "SCR_005065")
