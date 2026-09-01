"""Test quality dashboard aggregation and coverage metrics."""

from datetime import datetime, timezone
from pathlib import Path


def test_build_dashboard_data_counts_and_scoring(quality_dashboard_module):
    mod = quality_dashboard_module
    repo_root = Path(__file__).resolve().parents[1]
    now = datetime(2026, 2, 16, tzinfo=timezone.utc)
    resources = [
        {
            "id": "stubres",
            "name": "Stub Resource",
            "activity_status": "active",
            "domains": ["stub"],
            "products": [],
            "creation_date": "2026-01-01T00:00:00Z",
            "last_modified_date": "2026-01-01T00:00:00Z",
        },
        {
            "id": "res2",
            "name": "Resource Two",
            "category": "DataSource",
            "activity_status": "active",
            "description": "Has products",
            "homepage_url": "https://example.org/res2",
            "repository": "https://github.com/example/res2",
            "infores_id": "res2",
            "license": {"id": "https://creativecommons.org/licenses/by/4.0/", "label": "CC BY 4.0"},
            "contacts": [{"category": "Organization", "id": "ncbi", "label": "NCBI"}],
            "creation_date": "2026-01-01T00:00:00Z",
            "last_modified_date": "2026-01-10T00:00:00Z",
            "publications": [{"id": "PMID:12345", "title": "Old title"}],
            "products": [
                {
                    "id": "res2.graph",
                    "category": "GraphProduct",
                    "name": "Graph",
                },
                {
                    "id": "res2.download",
                    "category": "GraphProduct",
                    "name": "Download",
                    "format": "tsv",
                    "original_source": [
                        {"source": "stubres", "relation_type": "prov:hadPrimarySource"}
                    ],
                    "product_url": "https://example.org/bad-link",
                    "warnings": [
                        "File was not able to be retrieved when checked on 2026-02-10: timeout"
                    ],
                },
            ],
        },
    ]

    url_results = {
        "https://example.org/res2": {"ok": True, "source": "live"},
        "https://example.org/bad-link": {"ok": False, "source": "live", "status_code": 404},
    }
    link_summary = {
        "total_unique_urls": 2,
        "live_checked_urls": 2,
        "cache_hits": 0,
        "healthy_urls": 1,
        "broken_urls": 1,
        "unchecked_urls": 0,
    }

    data = mod.build_dashboard_data(
        resources,
        org_index={
            "ids": {"ncbi"},
            "short_ids": set(),
            "labels": {"nationalcenterforbiotechnologyinformation"},
        },
        url_results=url_results,
        citation_reports={
            "res2": {
                "errors": ["resource/res2/res2.md publication[0] title mismatch"],
                "warnings": [],
                "issue_count": 1,
                "publication_entries_with_issues": 1,
            }
        },
        now=now,
        link_mode="live",
        link_summary=link_summary,
        cache_path=repo_root / "cache" / "quality_url_status_cache.yml",
    )

    assert data["resources"]["total"] == 2
    assert data["resources"]["stub_count"] == 1
    assert data["resources"]["without_products"] == 1
    assert data["resources"]["missing_license"] == 1
    assert data["resources"]["missing_repository"] == 1
    assert data["resources"]["missing_infores_id"] == 1
    assert data["resources"]["missing_fairsharing_id"] == 2
    assert data["resources"]["missing_contacts"] == 1
    assert data["resources"]["without_publications"] == 1
    assert data["resources"]["with_citation_issues"] == 1
    assert data["resources"]["contacts_with_org_connection"] == 1
    assert data["resources"]["contacts_without_org_connection"] == 0
    assert data["products"]["total"] == 2
    assert data["products"]["missing_format"] == 1
    assert data["products"]["missing_original_source"] == 1
    assert data["products"]["missing_product_url"] == 1
    assert data["products"]["with_retrieval_warning"] == 1
    assert data["citations"]["publication_entries_total"] == 1
    assert data["citations"]["publication_entries_with_issues"] == 1
    assert data["citations"]["resources_without_publications"] == 1
    assert data["citations"]["resources_with_citation_issues"] == 1
    assert data["citations"]["validation_errors"] == 1
    assert data["dates"]["modified_after_creation"] == 1
    assert data["dates"]["unchanged_since_creation"] == 1
    assert data["links"]["broken_urls"] == 1
    assert data["resources"]["with_broken_links"] == 1
    assert sorted(data["detail_lists"]["resource_total_ids"]) == ["res2", "stubres"]
    assert sorted(data["detail_lists"]["product_total_ids"]) == ["res2.download", "res2.graph"]
    assert data["detail_lists"]["missing_contacts_resource_ids"] == ["stubres"]
    assert data["detail_lists"]["resources_without_publications_ids"] == ["stubres"]
    assert data["detail_lists"]["resources_with_citation_issue_ids"] == ["res2"]
    assert data["detail_lists"]["broken_link_page_ids"] == ["res2.download"]
    assert data["detail_lists"]["resource_with_broken_links_ids"] == ["res2"]

    top = data["top_resources"]
    assert len(top) == 2
    assert top[0]["id"] == "stubres"
    assert top[0]["score"] > top[1]["score"]


def test_resources_are_scored_only_for_products_they_own(quality_dashboard_module):
    """A Resource must not be penalized for products propagated onto its page.

    ``agg.download`` has no format, no original_source, no product_url and a
    broken URL. It is owned by ``agg`` and propagated onto ``src``, which cites
    it as a source. Only ``agg`` should be scored for it.
    """
    mod = quality_dashboard_module
    repo_root = Path(__file__).resolve().parents[1]
    now = datetime(2026, 2, 16, tzinfo=timezone.utc)

    broken_product = {
        "id": "agg.download",
        "category": "GraphProduct",
        "name": "Aggregated Download",
        "repository": "https://example.org/broken-repo",
        "warnings": ["File was not able to be retrieved when checked on 2026-02-10: timeout"],
    }
    resources = [
        {"id": "agg", "name": "Aggregator", "products": [dict(broken_product)]},
        {"id": "src", "name": "Source", "products": [dict(broken_product)]},
    ]

    data = mod.build_dashboard_data(
        resources,
        org_index={"ids": set(), "short_ids": set(), "labels": set()},
        url_results={"https://example.org/broken-repo": {"ok": False, "source": "live"}},
        citation_reports={},
        now=now,
        link_mode="live",
        link_summary={
            "total_unique_urls": 1,
            "live_checked_urls": 1,
            "cache_hits": 0,
            "healthy_urls": 0,
            "broken_urls": 1,
            "unchecked_urls": 0,
        },
        cache_path=repo_root / "cache" / "quality_url_status_cache.yml",
    )

    by_id = {record["id"]: record for record in data["top_resources"]}
    product_issues = {
        "product_missing_format",
        "product_missing_original_source",
        "product_missing_product_url",
        "broken_link",
    }

    agg_issues = {issue["issue_key"] for issue in by_id["agg"]["issues"]}
    src_issues = {issue["issue_key"] for issue in by_id["src"]["issues"]}
    assert product_issues <= agg_issues, "owner must be scored for its own product"
    assert not (product_issues & src_issues), "non-owner must not be scored for it"
    assert by_id["src"]["broken_links"] == []

    # The registry-wide totals still count the product once, from either page.
    assert data["products"]["total"] == 1
    assert data["products"]["missing_format"] == 1
    assert data["products"]["missing_original_source"] == 1
    assert data["products"]["missing_product_url"] == 1
    assert data["products"]["with_retrieval_warning"] == 1
    assert data["resources"]["with_broken_links"] == 1
    assert data["detail_lists"]["resource_with_broken_links_ids"] == ["agg"]


def test_product_metrics_count_unique_products(quality_dashboard_module):
    """Products propagated onto source Resource pages are counted only once.

    ``propagate_products`` copies a derived product onto every Resource page
    listed as one of its sources, so the same product ID appears on several
    pages. Every product metric must count distinct products.
    """
    mod = quality_dashboard_module
    repo_root = Path(__file__).resolve().parents[1]
    now = datetime(2026, 2, 16, tzinfo=timezone.utc)

    shared_product = {
        "id": "agg.download",
        "category": "GraphProduct",
        "name": "Aggregated Download",
        "warnings": ["File was not able to be retrieved when checked on 2026-02-10: timeout"],
    }
    resources = [
        {
            "id": "agg",
            "name": "Aggregator",
            "products": [dict(shared_product)],
        },
        # The propagated copies, as they appear on each cited source's page.
        {
            "id": "src1",
            "name": "Source One",
            "products": [
                dict(shared_product),
                {"id": "src1.graph", "category": "GraphProduct", "name": "Src1 Graph"},
            ],
        },
        {
            "id": "src2",
            "name": "Source Two",
            "products": [dict(shared_product)],
        },
    ]

    data = mod.build_dashboard_data(
        resources,
        org_index={"ids": set(), "short_ids": set(), "labels": set()},
        url_results={},
        citation_reports={},
        now=now,
        link_mode="cache-or-unchecked",
        link_summary={
            "total_unique_urls": 0,
            "live_checked_urls": 0,
            "cache_hits": 0,
            "healthy_urls": 0,
            "broken_urls": 0,
            "unchecked_urls": 0,
        },
        cache_path=repo_root / "cache" / "quality_url_status_cache.yml",
    )

    # Four product entries across the three pages, but only two distinct products.
    assert data["products"]["total"] == 2
    assert data["products"]["missing_format"] == 2
    assert data["products"]["missing_original_source"] == 2
    assert data["products"]["missing_product_url"] == 2
    assert data["products"]["with_retrieval_warning"] == 1

    # Every product figure equals the length of the list it drills down into.
    detail = data["detail_lists"]
    assert data["products"]["total"] == len(detail["product_total_ids"])
    assert data["products"]["missing_format"] == len(detail["products_missing_format_ids"])
    assert data["products"]["missing_original_source"] == len(
        detail["products_missing_original_source_ids"]
    )
    assert data["products"]["missing_product_url"] == len(
        detail["products_missing_product_url_ids"]
    )
    assert data["products"]["with_retrieval_warning"] == len(
        detail["retrieval_warning_product_ids"]
    )
    assert detail["product_total_ids"] == ["agg.download", "src1.graph"]


def test_products_without_ids_are_counted_separately(quality_dashboard_module):
    """Unidentified products fall back to per-resource synthetic IDs, not deduped away."""
    mod = quality_dashboard_module
    repo_root = Path(__file__).resolve().parents[1]
    now = datetime(2026, 2, 16, tzinfo=timezone.utc)
    resources = [
        {
            "id": "res1",
            "name": "Resource One",
            "products": [
                {"category": "GraphProduct", "name": "Unnamed A"},
                {"category": "GraphProduct", "name": "Unnamed B"},
            ],
        },
        {
            "id": "res2",
            "name": "Resource Two",
            "products": [{"category": "GraphProduct", "name": "Unnamed C"}],
        },
    ]

    data = mod.build_dashboard_data(
        resources,
        org_index={"ids": set(), "short_ids": set(), "labels": set()},
        url_results={},
        citation_reports={},
        now=now,
        link_mode="cache-or-unchecked",
        link_summary={
            "total_unique_urls": 0,
            "live_checked_urls": 0,
            "cache_hits": 0,
            "healthy_urls": 0,
            "broken_urls": 0,
            "unchecked_urls": 0,
        },
        cache_path=repo_root / "cache" / "quality_url_status_cache.yml",
    )

    assert data["products"]["total"] == 3
    assert data["detail_lists"]["product_total_ids"] == [
        "res1.product-1",
        "res1.product-2",
        "res2.product-1",
    ]


def test_knowledge_graph_evaluation_coverage(quality_dashboard_module):
    repo_root = Path(__file__).resolve().parents[1]
    mod = quality_dashboard_module
    now = datetime(2026, 2, 16, tzinfo=timezone.utc)
    resources = [
        {
            "id": "drugmechdb",
            "name": "DrugMechDB",
            "category": "KnowledgeGraph",
            "_resource_file": "resource/drugmechdb/drugmechdb.md",
        },
        {
            "id": "smart",
            "name": "SMART",
            "category": "KnowledgeGraph",
            "_resource_file": "resource/smart/smart.md",
        },
    ]

    data = mod.build_dashboard_data(
        resources,
        org_index={"ids": set(), "short_ids": set(), "labels": set()},
        url_results={},
        citation_reports={},
        now=now,
        link_mode="cache-or-unchecked",
        link_summary={
            "total_unique_urls": 0,
            "live_checked_urls": 0,
            "cache_hits": 0,
            "healthy_urls": 0,
            "broken_urls": 0,
            "unchecked_urls": 0,
        },
        cache_path=repo_root / "cache" / "quality_url_status_cache.yml",
    )

    assert data["knowledge_graph_evaluations"]["knowledge_graph_total"] == 2
    assert data["knowledge_graph_evaluations"]["with_evaluation_page"] == 1
    assert data["knowledge_graph_evaluations"]["without_evaluation_page"] == 1
    assert data["detail_lists"]["kg_with_evaluation_page_resource_ids"] == ["drugmechdb"]
    assert data["detail_lists"]["kg_without_evaluation_page_resource_ids"] == ["smart"]


def test_normalize_cache_entry_with_legacy_skip_reason(quality_dashboard_module):
    mod = quality_dashboard_module
    normalized = mod.normalize_cache_entry(
        {
            "skip_reason": "html_page",
            "checked_at": "2026-02-15T00:00:00Z",
        }
    )

    assert normalized is not None
    assert normalized["ok"] is True
    assert normalized["source"] == "cache"


class _FakeResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def close(self):
        pass


def _install_fake_requests(monkeypatch, mod, responder):
    """Replace mod.requests with a stub whose head/get call `responder(method, url)`."""

    class _FakeRequests:
        # Preserve the real exception types the code catches.
        exceptions = mod.requests.exceptions
        RequestException = mod.requests.RequestException

        @staticmethod
        def head(url, **kwargs):
            return responder("head", url)

        @staticmethod
        def get(url, **kwargs):
            return responder("get", url)

    monkeypatch.setattr(mod, "requests", _FakeRequests)


def test_is_sparql_endpoint(quality_dashboard_module):
    mod = quality_dashboard_module
    assert mod.is_sparql_endpoint("https://frink.apps.renci.org/wikidata/sparql")
    assert mod.is_sparql_endpoint("https://apps.okn.us/identifier-mappings/sparql/")
    assert not mod.is_sparql_endpoint("https://example.org/data.owl")
    assert not mod.is_sparql_endpoint("https://example.org/sparqlx")


def test_check_http_url_treats_406_and_412_as_live(quality_dashboard_module, monkeypatch):
    mod = quality_dashboard_module
    for code in (406, 412):
        _install_fake_requests(monkeypatch, mod, lambda method, url, code=code: _FakeResponse(code))
        result = mod.check_http_url("https://example.org/page", timeout=5.0)
        assert result["ok"] is True, f"HTTP {code} should be treated as live"
        assert result.get("access_restricted") is True


def test_check_http_url_probes_sparql_endpoints(quality_dashboard_module, monkeypatch):
    mod = quality_dashboard_module

    def responder(method, url):
        # A bare request (no query) 404s; a SPARQL query succeeds.
        if "query=" in url:
            return _FakeResponse(200)
        return _FakeResponse(404)

    _install_fake_requests(monkeypatch, mod, responder)
    result = mod.check_http_url("https://frink.apps.renci.org/wikidata/sparql", timeout=5.0)
    assert result["ok"] is True
    assert result.get("sparql_probe") is True


def test_check_http_url_still_flags_dead_sparql_endpoint(quality_dashboard_module, monkeypatch):
    mod = quality_dashboard_module
    # Endpoint is genuinely gone: every request 404s, including the query probe.
    _install_fake_requests(monkeypatch, mod, lambda method, url: _FakeResponse(404))
    result = mod.check_http_url("https://gone.example.org/sparql", timeout=5.0)
    assert result["ok"] is False


class _FlakyResponder:
    """Responder that fails a set number of times before succeeding."""

    def __init__(self, mod, failures, exc_factory, then_code=200):
        self.mod = mod
        self.remaining = failures
        self.exc_factory = exc_factory
        self.then_code = then_code
        self.calls = []

    def __call__(self, method, url):
        self.calls.append(method)
        if self.remaining > 0:
            self.remaining -= 1
            raise self.exc_factory()
        return _FakeResponse(self.then_code)


def test_check_http_url_falls_back_to_get_on_head_404(quality_dashboard_module, monkeypatch):
    """A host answering HEAD 404 but GET 200 is reachable, not broken.

    Real cases: dsstox's clowder.edap-cluster.com URL and ssurgo's box.com URL.
    """
    mod = quality_dashboard_module
    calls = []

    def responder(method, url):
        calls.append(method)
        return _FakeResponse(404 if method == "head" else 200)

    _install_fake_requests(monkeypatch, mod, responder)
    result = mod.check_http_url("https://example.org/file.zip", timeout=5.0)
    assert result["ok"] is True
    assert result["status_code"] == 200
    assert calls == ["head", "get"], "GET must be attempted after a HEAD 404"


def test_check_http_url_falls_back_to_get_when_head_connection_fails(
    quality_dashboard_module, monkeypatch
):
    """Some hosts drop HEAD connections but serve GET fine (noaa-ncei.ibtracs)."""
    mod = quality_dashboard_module

    def responder(method, url):
        if method == "head":
            raise mod.requests.exceptions.ConnectionError("RemoteDisconnected")
        return _FakeResponse(200)

    _install_fake_requests(monkeypatch, mod, responder)
    result = mod.check_http_url("https://example.org/page", timeout=5.0)
    assert result["ok"] is True
    assert result["status_code"] == 200


def test_check_http_url_retries_once_on_connection_error(quality_dashboard_module, monkeypatch):
    """A single transient reset must not write a durable broken-link warning."""
    mod = quality_dashboard_module
    responder = _FlakyResponder(
        mod, failures=1, exc_factory=lambda: mod.requests.exceptions.ConnectionError("reset")
    )
    _install_fake_requests(monkeypatch, mod, responder)
    monkeypatch.setattr(mod, "_RETRY_DELAY_SECONDS", 0)
    result = mod.check_http_url("https://example.org/page", timeout=5.0)
    assert result["ok"] is True
    assert responder.calls == ["head", "head"], "HEAD should be retried once, then succeed"


def test_check_http_url_does_not_retry_timeouts(quality_dashboard_module, monkeypatch):
    """Timeouts dominate genuinely dead hosts; retrying them only doubles runtime."""
    mod = quality_dashboard_module
    calls = []

    def responder(method, url):
        calls.append(method)
        raise mod.requests.exceptions.Timeout("timed out")

    _install_fake_requests(monkeypatch, mod, responder)
    monkeypatch.setattr(mod, "_RETRY_DELAY_SECONDS", 0)
    result = mod.check_http_url("https://dead.example.org/page", timeout=5.0)
    assert result["ok"] is False
    assert calls == ["head", "get"], "one HEAD and one GET, no timeout retries"


def test_check_http_url_still_reports_genuinely_dead_urls(quality_dashboard_module, monkeypatch):
    """The GET fallback must not turn real 404s into false positives."""
    mod = quality_dashboard_module
    _install_fake_requests(monkeypatch, mod, lambda method, url: _FakeResponse(404))
    result = mod.check_http_url("https://example.org/gone.zip", timeout=5.0)
    assert result["ok"] is False
    assert result["status_code"] == 404
    assert "GET returned HTTP 404" in result["error"]


def test_check_http_url_reports_both_failures_when_neither_verb_responds(
    quality_dashboard_module, monkeypatch
):
    mod = quality_dashboard_module

    def responder(method, url):
        raise mod.requests.exceptions.Timeout("timed out")

    _install_fake_requests(monkeypatch, mod, responder)
    monkeypatch.setattr(mod, "_RETRY_DELAY_SECONDS", 0)
    result = mod.check_http_url("https://dead.example.org/page", timeout=5.0)
    assert result["ok"] is False
    assert result["status_code"] is None
    assert "HEAD request failed" in result["error"]
    assert "GET request failed" in result["error"]


def test_check_http_url_keeps_access_restricted_semantics(quality_dashboard_module, monkeypatch):
    """403 on both verbs stays reachable-but-restricted, not broken."""
    mod = quality_dashboard_module
    _install_fake_requests(monkeypatch, mod, lambda method, url: _FakeResponse(403))
    result = mod.check_http_url("https://example.org/page", timeout=5.0)
    assert result["ok"] is True
    assert result.get("access_restricted") is True
