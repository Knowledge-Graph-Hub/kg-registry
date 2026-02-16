#!/usr/bin/env python3
"""
Generate data quality metrics for KG-Registry resources.

This script scans all top-level Resource pages, computes aggregate quality
metrics, and writes a JSON artifact consumed by the dashboard page.
"""

from __future__ import annotations

import argparse
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from ftplib import FTP
from pathlib import Path
from statistics import median
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlparse

import requests
import yaml

from common import RESOURCE_DIR, ROOT, load_frontmatter_file

# Products in these categories are generally interfaces; provenance source
# metadata is less meaningful than for data products.
INTERFACE_CATEGORIES = {"GraphicalInterface", "ProgrammingInterface"}

# Scoring weights for "resources most in need of improvement".
ISSUE_WEIGHTS = {
    "stub_domain": 8,
    "no_products": 8,
    "missing_description": 3,
    "missing_homepage_url": 3,
    "missing_creation_date": 2,
    "missing_last_modified_date": 2,
    "unchanged_since_creation": 2,
    "stale_last_modified": 2,
    "product_missing_format": 1,
    "product_missing_original_source": 2,
    "product_missing_product_url": 2,
    "broken_link": 3,
}

ISSUE_LABELS = {
    "stub_domain": "Tagged as stub",
    "no_products": "No products listed",
    "missing_description": "Missing description",
    "missing_homepage_url": "Missing homepage_url",
    "missing_creation_date": "Missing creation_date",
    "missing_last_modified_date": "Missing last_modified_date",
    "unchanged_since_creation": "Not modified since creation",
    "stale_last_modified": "Stale last_modified_date",
    "product_missing_format": "Products missing format",
    "product_missing_original_source": "Products missing original_source",
    "product_missing_product_url": "Products missing product_url",
    "broken_link": "Broken/inaccessible links",
}

WARNING_RETRIEVAL_PATTERN = re.compile(
    r"^File was not able to be retrieved when checked on \d{4}-\d{2}-\d{2}:"
)

DEFAULT_CACHE_PATH = ROOT / "cache" / "quality_url_status_cache.yml"
DEFAULT_OUTPUT_PATH = ROOT / "reports" / "quality-dashboard.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate data quality metrics for KG-Registry resources."
    )
    parser.add_argument(
        "--resource-dir",
        default=str(RESOURCE_DIR),
        help="Path to the resource directory (default: resource/)",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT_PATH),
        help="Path to output JSON file (default: reports/quality-dashboard.json)",
    )
    parser.add_argument(
        "--cache-path",
        default=str(DEFAULT_CACHE_PATH),
        help="Path to URL status cache (default: cache/quality_url_status_cache.yml)",
    )
    parser.add_argument(
        "--check-links",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Run live URL checks (default: true). Use --no-check-links to disable.",
    )
    parser.add_argument(
        "--link-timeout",
        type=float,
        default=8.0,
        help="Timeout in seconds for each URL check (default: 8.0)",
    )
    parser.add_argument(
        "--link-workers",
        type=int,
        default=16,
        help="Number of worker threads for URL checks (default: 16)",
    )
    parser.add_argument(
        "--cache-ttl-days",
        type=int,
        default=14,
        help="Cache time-to-live in days when live link checks are enabled (default: 14)",
    )
    parser.add_argument(
        "--force-recheck",
        action="store_true",
        help="Ignore cache TTL and re-check all URLs live.",
    )
    return parser.parse_args()


def ensure_list(value: Any) -> List[Any]:
    if isinstance(value, list):
        return value
    if value is None:
        return []
    return [value]


def is_non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def parse_datetime(value: Any) -> Optional[datetime]:
    if value is None:
        return None
    if isinstance(value, datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)
    if not isinstance(value, str):
        return None

    text = value.strip()
    if not text:
        return None

    normalized = text.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        pass

    if len(text) >= 10:
        try:
            dt = datetime.strptime(text[:10], "%Y-%m-%d")
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return None


def load_resources(resource_dir: Path) -> List[Dict[str, Any]]:
    resources: List[Dict[str, Any]] = []
    for subdir in sorted(resource_dir.iterdir(), key=lambda p: p.name.lower()):
        if not subdir.is_dir():
            continue
        main_file = subdir / f"{subdir.name}.md"
        if not main_file.exists():
            continue
        metadata, _, error = load_frontmatter_file(main_file, use_ruamel=False)
        if error is not None or metadata is None:
            print(f"WARNING: could not parse {main_file}: {error}")
            continue
        if "id" not in metadata:
            metadata["id"] = subdir.name
        metadata["_resource_file"] = str(main_file.relative_to(ROOT))
        resources.append(metadata)
    return resources


def normalize_cache_entry(entry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if not isinstance(entry, dict):
        return None

    status_code = entry.get("status_code")
    error = entry.get("error")
    skip_reason = entry.get("skip_reason")
    checked_at = entry.get("checked_at")

    ok = entry.get("ok")
    if isinstance(ok, bool):
        pass
    else:
        if error:
            ok = False
        elif isinstance(status_code, int):
            ok = 200 <= status_code < 400
        elif skip_reason in {"html_page", "directory"}:
            ok = True
        else:
            ok = None

    return {
        "ok": ok,
        "status_code": status_code if isinstance(status_code, int) else None,
        "error": str(error) if error is not None else None,
        "checked_at": checked_at if isinstance(checked_at, str) else None,
        "source": "cache",
    }


def load_url_cache(cache_path: Path) -> Dict[str, Dict[str, Any]]:
    if not cache_path.exists():
        return {}
    try:
        with cache_path.open("r", encoding="utf-8") as handle:
            loaded = yaml.safe_load(handle) or {}
    except Exception as error:
        print(f"WARNING: could not read URL cache {cache_path}: {error}")
        return {}

    if not isinstance(loaded, dict):
        return {}

    normalized: Dict[str, Dict[str, Any]] = {}
    for url, entry in loaded.items():
        if not isinstance(url, str):
            continue
        norm = normalize_cache_entry(entry if isinstance(entry, dict) else {})
        if norm is not None:
            normalized[url] = norm
    return normalized


def save_url_cache(cache: Dict[str, Dict[str, Any]], cache_path: Path) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        yaml.safe_dump(cache, default_flow_style=False, sort_keys=True),
        encoding="utf-8",
    )


def is_cache_fresh(entry: Dict[str, Any], now: datetime, ttl_days: int) -> bool:
    checked_at = parse_datetime(entry.get("checked_at"))
    if checked_at is None:
        return False
    return checked_at >= now - timedelta(days=ttl_days)


def check_ftp_url(url: str, timeout: float) -> Dict[str, Any]:
    parsed = urlparse(url)
    host = parsed.hostname
    if not host:
        return {"ok": False, "status_code": None, "error": "FTP URL missing hostname"}

    path = parsed.path or "/"
    port = parsed.port or 21

    ftp = FTP()
    try:
        ftp.connect(host, port, timeout=timeout)
        ftp.login()
        try:
            size = ftp.size(path)
            if size is not None:
                return {"ok": True, "status_code": 200, "error": None}
        except Exception:
            pass
        try:
            ftp.cwd(path)
            return {"ok": True, "status_code": 200, "error": None}
        except Exception as error:
            return {"ok": False, "status_code": None, "error": f"FTP path error: {error}"}
    except Exception as error:
        return {"ok": False, "status_code": None, "error": f"FTP error: {error}"}
    finally:
        try:
            ftp.quit()
        except Exception:
            pass


def check_http_url(url: str, timeout: float) -> Dict[str, Any]:
    headers = {"User-Agent": "kg-registry-quality-dashboard/1.0"}

    try:
        head_resp = requests.head(url, timeout=timeout, allow_redirects=True, headers=headers)
        head_code = head_resp.status_code
        head_resp.close()
    except requests.RequestException as error:
        return {"ok": False, "status_code": None, "error": f"HEAD request failed: {error}"}

    if 200 <= head_code < 400:
        return {"ok": True, "status_code": head_code, "error": None}

    # Some endpoints disallow HEAD or return transient responses there.
    fallback_codes = {401, 403, 405, 429}
    if head_code in fallback_codes:
        try:
            get_resp = requests.get(url, timeout=timeout, allow_redirects=True, headers=headers)
            get_code = get_resp.status_code
            get_resp.close()
            if 200 <= get_code < 400:
                return {"ok": True, "status_code": get_code, "error": None}
            return {
                "ok": False,
                "status_code": get_code,
                "error": f"GET returned HTTP {get_code}",
            }
        except requests.RequestException as error:
            return {"ok": False, "status_code": head_code, "error": f"GET request failed: {error}"}

    return {
        "ok": False,
        "status_code": head_code,
        "error": f"HEAD returned HTTP {head_code}",
    }


def check_url(url: str, timeout: float) -> Dict[str, Any]:
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    if scheme in {"http", "https"}:
        result = check_http_url(url, timeout)
    elif scheme in {"ftp", "ftps"}:
        result = check_ftp_url(url, timeout)
    else:
        result = {"ok": False, "status_code": None, "error": f"Unsupported URL scheme: {scheme}"}

    result["checked_at"] = checked_at
    result["source"] = "live"
    return result


def evaluate_urls(
    urls: Iterable[str],
    *,
    check_links: bool,
    cache_path: Path,
    cache_ttl_days: int,
    force_recheck: bool,
    timeout: float,
    workers: int,
    now: datetime,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    unique_urls = sorted(set(urls))
    cache = load_url_cache(cache_path)
    results: Dict[str, Dict[str, Any]] = {}

    to_check_live: List[str] = []
    cache_hits = 0

    for url in unique_urls:
        cached = cache.get(url)
        if cached is not None:
            if not check_links:
                results[url] = dict(cached)
                cache_hits += 1
                continue
            if not force_recheck and is_cache_fresh(cached, now=now, ttl_days=cache_ttl_days):
                results[url] = dict(cached)
                cache_hits += 1
                continue
        if check_links:
            to_check_live.append(url)
        else:
            results[url] = {
                "ok": None,
                "status_code": None,
                "error": "unchecked",
                "checked_at": None,
                "source": "unchecked",
            }

    live_checked = 0
    if to_check_live:
        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futures = {pool.submit(check_url, url, timeout): url for url in to_check_live}
            for future in as_completed(futures):
                url = futures[future]
                try:
                    result = future.result()
                except Exception as error:
                    result = {
                        "ok": False,
                        "status_code": None,
                        "error": f"Unexpected link check error: {error}",
                        "checked_at": datetime.now(timezone.utc)
                        .isoformat(timespec="seconds")
                        .replace("+00:00", "Z"),
                        "source": "live",
                    }
                results[url] = result
                cache[url] = {
                    "ok": result.get("ok"),
                    "status_code": result.get("status_code"),
                    "error": result.get("error"),
                    "checked_at": result.get("checked_at"),
                }
                live_checked += 1
        save_url_cache(cache, cache_path)

    total = len(unique_urls)
    broken = sum(1 for info in results.values() if info.get("ok") is False)
    healthy = sum(1 for info in results.values() if info.get("ok") is True)
    unchecked = total - healthy - broken

    summary = {
        "total_unique_urls": total,
        "live_checked_urls": live_checked,
        "cache_hits": cache_hits,
        "healthy_urls": healthy,
        "broken_urls": broken,
        "unchecked_urls": unchecked,
    }
    return results, summary


def add_scored_issue(
    issue_bag: List[Dict[str, Any]],
    *,
    issue_key: str,
    count: int = 1,
) -> int:
    if count <= 0:
        return 0
    points = ISSUE_WEIGHTS[issue_key] * count
    issue_bag.append(
        {
            "issue_key": issue_key,
            "label": ISSUE_LABELS[issue_key],
            "count": count,
            "points": points,
        }
    )
    return points


def build_dashboard_data(
    resources: List[Dict[str, Any]],
    *,
    url_results: Dict[str, Dict[str, Any]],
    now: datetime,
    link_mode: str,
    link_summary: Dict[str, Any],
    cache_path: Path,
) -> Dict[str, Any]:
    status_counts: Dict[str, int] = {}
    stub_count = 0
    without_products = 0
    missing_description = 0
    missing_homepage = 0

    total_products = 0
    products_missing_format = 0
    products_missing_original_source = 0
    products_missing_product_url = 0
    retrieval_warning_count = 0

    with_both_dates = 0
    modified_after_creation = 0
    unchanged_since_creation = 0
    missing_creation_date = 0
    missing_last_modified_date = 0
    stale_over_365 = 0

    top_records: List[Dict[str, Any]] = []
    resource_broken_map: Dict[str, Dict[str, List[str]]] = {}

    # Collect URL references with resource context for per-resource broken-link counts.
    url_targets: List[Tuple[str, str]] = []

    for resource in resources:
        resource_id = str(resource.get("id", "unknown"))
        resource_name = resource.get("name") if is_non_empty_text(
            resource.get("name")) else resource_id

        activity_status = str(resource.get("activity_status", "unknown"))
        status_counts[activity_status] = status_counts.get(activity_status, 0) + 1

        domains = [str(d).strip().lower()
                   for d in ensure_list(resource.get("domains")) if d is not None]
        has_stub_domain = "stub" in domains
        if has_stub_domain:
            stub_count += 1

        products = ensure_list(resource.get("products"))
        if len(products) == 0:
            without_products += 1

        if not is_non_empty_text(resource.get("description")):
            missing_description += 1
        if not is_non_empty_text(resource.get("homepage_url")):
            missing_homepage += 1

        creation_dt = parse_datetime(resource.get("creation_date"))
        modified_dt = parse_datetime(resource.get("last_modified_date"))
        if creation_dt is None:
            missing_creation_date += 1
        if modified_dt is None:
            missing_last_modified_date += 1
        if creation_dt is not None and modified_dt is not None:
            with_both_dates += 1
            if modified_dt > creation_dt:
                modified_after_creation += 1
            else:
                unchanged_since_creation += 1
            if (now - modified_dt).days > 365:
                stale_over_365 += 1

        score = 0
        issues: List[Dict[str, Any]] = []

        if has_stub_domain:
            score += add_scored_issue(issues, issue_key="stub_domain")
        if len(products) == 0:
            score += add_scored_issue(issues, issue_key="no_products")
        if not is_non_empty_text(resource.get("description")):
            score += add_scored_issue(issues, issue_key="missing_description")
        if not is_non_empty_text(resource.get("homepage_url")):
            score += add_scored_issue(issues, issue_key="missing_homepage_url")
        if creation_dt is None:
            score += add_scored_issue(issues, issue_key="missing_creation_date")
        if modified_dt is None:
            score += add_scored_issue(issues, issue_key="missing_last_modified_date")
        if creation_dt is not None and modified_dt is not None and modified_dt <= creation_dt:
            score += add_scored_issue(issues, issue_key="unchanged_since_creation")
        if modified_dt is not None and (now - modified_dt).days > 365:
            score += add_scored_issue(issues, issue_key="stale_last_modified")

        # URLs at resource level
        for key in ("homepage_url", "repository"):
            url_value = resource.get(key)
            if is_non_empty_text(url_value):
                url_targets.append((resource_id, str(url_value)))

        missing_format_for_resource = 0
        missing_source_for_resource = 0
        missing_url_for_resource = 0
        warning_links_for_resource: set[str] = set()

        for product in products:
            if not isinstance(product, dict):
                continue
            total_products += 1

            if not is_non_empty_text(product.get("format")):
                products_missing_format += 1
                missing_format_for_resource += 1

            category = str(product.get("category", ""))
            if category not in INTERFACE_CATEGORIES:
                original_source = ensure_list(product.get("original_source"))
                has_source = any(is_non_empty_text(source) for source in original_source)
                if not has_source:
                    products_missing_original_source += 1
                    missing_source_for_resource += 1

            product_url = product.get("product_url")
            if is_non_empty_text(product_url):
                url_targets.append((resource_id, str(product_url)))
            else:
                products_missing_product_url += 1
                missing_url_for_resource += 1

            product_repository = product.get("repository")
            if is_non_empty_text(product_repository):
                url_targets.append((resource_id, str(product_repository)))

            warning_values = ensure_list(product.get("warnings"))
            for warning in warning_values:
                if isinstance(warning, str) and WARNING_RETRIEVAL_PATTERN.match(warning):
                    retrieval_warning_count += 1
                    if is_non_empty_text(product_url):
                        warning_url = str(product_url)
                        # If this run already has a healthy URL check, treat the warning as stale.
                        if url_results.get(warning_url, {}).get("ok") is not True:
                            warning_links_for_resource.add(warning_url)
                    else:
                        product_id = str(product.get("id", "unknown-product"))
                        warning_links_for_resource.add(f"warning:{resource_id}:{product_id}")

        if missing_format_for_resource:
            score += add_scored_issue(
                issues, issue_key="product_missing_format", count=missing_format_for_resource
            )
        if missing_source_for_resource:
            score += add_scored_issue(
                issues,
                issue_key="product_missing_original_source",
                count=missing_source_for_resource,
            )
        if missing_url_for_resource:
            score += add_scored_issue(
                issues, issue_key="product_missing_product_url", count=missing_url_for_resource
            )

        # Initialize from warning-derived link issues.
        if warning_links_for_resource:
            resource_broken_map[resource_id] = {}
            for item in warning_links_for_resource:
                resource_broken_map[resource_id][item] = ["warning"]

        top_records.append(
            {
                "id": resource_id,
                "name": resource_name,
                "activity_status": activity_status,
                "score": score,
                "issues": issues,
                "resource_page": f"resource/{resource_id}/{resource_id}.html",
            }
        )

    # Merge URL-check results into per-resource broken map.
    for resource_id, url in url_targets:
        info = url_results.get(url, {})
        if info.get("ok") is not False:
            continue
        if resource_id not in resource_broken_map:
            resource_broken_map[resource_id] = {}
        if url not in resource_broken_map[resource_id]:
            resource_broken_map[resource_id][url] = []
        source = str(info.get("source", "unknown"))
        if source not in resource_broken_map[resource_id][url]:
            resource_broken_map[resource_id][url].append(source)

    # Apply broken-link scoring.
    for record in top_records:
        rid = record["id"]
        broken_links = resource_broken_map.get(rid, {})
        broken_count = len(broken_links)
        if broken_count > 0:
            record["score"] += add_scored_issue(
                record["issues"], issue_key="broken_link", count=broken_count
            )
            record["broken_links"] = [
                {"url": url, "sources": sources}
                for url, sources in sorted(broken_links.items(), key=lambda kv: kv[0].lower())
            ]
        else:
            record["broken_links"] = []

        # Highest impact first.
        record["issues"].sort(
            key=lambda item: (-item["points"], item["label"].lower(), item["count"])
        )

    top_sorted = sorted(top_records, key=lambda r: (-r["score"], r["id"].lower()))
    top_ten = top_sorted[:10]

    scores = [item["score"] for item in top_records]
    average_score = round(sum(scores) / len(scores), 2) if scores else 0.0
    median_score = float(median(scores)) if scores else 0.0

    resources_with_broken_links = sum(1 for item in top_records if len(item["broken_links"]) > 0)
    try:
        cache_path_display = str(cache_path.relative_to(ROOT))
    except ValueError:
        cache_path_display = str(cache_path)

    data = {
        "generated_at": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "resource_count": len(resources),
        "resources": {
            "total": len(resources),
            "status_counts": status_counts,
            "stub_count": stub_count,
            "without_products": without_products,
            "missing_description": missing_description,
            "missing_homepage_url": missing_homepage,
            "with_broken_links": resources_with_broken_links,
        },
        "products": {
            "total": total_products,
            "missing_format": products_missing_format,
            "missing_original_source": products_missing_original_source,
            "missing_product_url": products_missing_product_url,
            "retrieval_warning_mentions": retrieval_warning_count,
        },
        "dates": {
            "with_both_dates": with_both_dates,
            "modified_after_creation": modified_after_creation,
            "unchanged_since_creation": unchanged_since_creation,
            "missing_creation_date": missing_creation_date,
            "missing_last_modified_date": missing_last_modified_date,
            "stale_over_365_days": stale_over_365,
        },
        "links": {
            "mode": link_mode,
            "cache_path": cache_path_display,
            **link_summary,
        },
        "scoring": {
            "weights": ISSUE_WEIGHTS,
            "average_score": average_score,
            "median_score": median_score,
            "resources_with_issues": sum(1 for score in scores if score > 0),
        },
        "top_resources": top_ten,
    }
    return data


def main() -> int:
    args = parse_args()

    resource_dir = Path(args.resource_dir).resolve()
    output_path = Path(args.output).resolve()
    cache_path = Path(args.cache_path).resolve()

    now = datetime.now(timezone.utc)

    resources = load_resources(resource_dir)
    if not resources:
        raise RuntimeError(f"No resources loaded from {resource_dir}")

    # Gather all URLs up front for global link checks.
    all_urls: List[str] = []
    for resource in resources:
        for key in ("homepage_url", "repository"):
            value = resource.get(key)
            if is_non_empty_text(value):
                all_urls.append(str(value))
        for product in ensure_list(resource.get("products")):
            if not isinstance(product, dict):
                continue
            for key in ("product_url", "repository"):
                value = product.get(key)
                if is_non_empty_text(value):
                    all_urls.append(str(value))

    url_results, link_summary = evaluate_urls(
        all_urls,
        check_links=args.check_links,
        cache_path=cache_path,
        cache_ttl_days=max(0, args.cache_ttl_days),
        force_recheck=args.force_recheck,
        timeout=max(1.0, args.link_timeout),
        workers=max(1, args.link_workers),
        now=now,
    )

    data = build_dashboard_data(
        resources,
        url_results=url_results,
        now=now,
        link_mode="live" if args.check_links else "cache-or-unchecked",
        link_summary=link_summary,
        cache_path=cache_path,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"Generated dashboard metrics for {len(resources)} resources")
    print(f"Output: {output_path}")
    print(
        "Links: "
        f"{data['links']['healthy_urls']} healthy, "
        f"{data['links']['broken_urls']} broken, "
        f"{data['links']['unchecked_urls']} unchecked "
        f"(mode={data['links']['mode']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
