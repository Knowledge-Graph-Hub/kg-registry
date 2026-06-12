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
        org_index={"ids": {"ncbi"}, "short_ids": set(), "labels": {
            "nationalcenterforbiotechnologyinformation"}},
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
    assert data["products"]["retrieval_warning_mentions"] == 1
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
