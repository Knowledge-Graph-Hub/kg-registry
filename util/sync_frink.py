#!/usr/bin/env python3
"""
Sync script for FRINK OKN knowledge graphs.

This script fetches the FRINK OKN registry manifest and creates or updates
KG-Registry resource pages for registered graphs. Existing pages are merged
conservatively so manually curated metadata and graph product inventories are
preserved while FRINK-managed discovery metadata stays current.
"""

from __future__ import annotations

import argparse
import copy
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import frontmatter  # type: ignore
import yaml

try:
    from util.source_associations import make_original_source_associations
except ModuleNotFoundError:
    from source_associations import make_original_source_associations


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# Some FRINK shortnames map onto an existing KG-Registry id that differs from the
# raw shortname -- e.g. a duplicate that has been merged into a canonical entry.
# Mapping them here makes the sync update the canonical page instead of recreating
# the duplicate resource directory on the next run.
SHORTNAME_ALIASES = {
    "ufokn": "uf-okn",
}


class FRINKSync:
    """Synchronize FRINK OKN registry entries with KG-Registry."""

    def __init__(self, registry_root: Optional[str] = None, cache_ttl_hours: int = 24):
        script_dir = Path(__file__).resolve().parent
        self.registry_root = (
            Path(registry_root)
            if registry_root is not None
            else script_dir.parent / "resource"
        )
        self.frink_registry_url = (
            "https://raw.githubusercontent.com/frink-okn/okn-registry/main/"
            "docs/registry/kgs.yaml"
        )
        self.cache_ttl_hours = cache_ttl_hours
        self.cache_dir = script_dir.parent / "cache"
        self.cache_file = self.cache_dir / "frink_registry_cache.yaml"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.existing_resources = self._load_existing_resources()

    def _load_existing_resources(self) -> Dict[str, Path]:
        resources: Dict[str, Path] = {}
        if not self.registry_root.exists():
            return resources

        for resource_dir in self.registry_root.iterdir():
            if not resource_dir.is_dir():
                continue
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if resource_file.exists():
                resources[resource_dir.name] = resource_file
        return resources

    def _today_iso(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00:00Z")

    def _is_cache_valid(self) -> bool:
        if not self.cache_file.exists():
            return False

        cache_age_hours = (time.time() - os.path.getmtime(self.cache_file)) / 3600
        is_valid = cache_age_hours < self.cache_ttl_hours

        if is_valid:
            logger.info(
                "FRINK cache is valid (age: %.1f hours, TTL: %s hours)",
                cache_age_hours,
                self.cache_ttl_hours,
            )
        else:
            logger.info(
                "FRINK cache expired (age: %.1f hours, TTL: %s hours)",
                cache_age_hours,
                self.cache_ttl_hours,
            )

        return is_valid

    def _load_from_cache(self) -> Optional[List[Dict[str, Any]]]:
        try:
            data = yaml.safe_load(self.cache_file.read_text(encoding="utf-8"))
        except Exception as exc:
            logger.warning("Failed to load FRINK cache: %s", exc)
            return None

        if isinstance(data, list):
            logger.info("Loaded %s FRINK registry entries from cache", len(data))
            return data
        return None

    def _save_to_cache(self, data: List[Dict[str, Any]]) -> None:
        try:
            self.cache_file.write_text(
                yaml.safe_dump(data, default_flow_style=False, sort_keys=False),
                encoding="utf-8",
            )
            logger.info("Cached %s FRINK registry entries to %s", len(data), self.cache_file)
        except Exception as exc:
            logger.warning("Failed to save FRINK cache: %s", exc)

    def fetch_frink_data(self) -> List[Dict[str, Any]]:
        if self._is_cache_valid():
            cached_data = self._load_from_cache()
            if cached_data is not None:
                return cached_data

        logger.info("Fetching fresh FRINK registry data from %s", self.frink_registry_url)
        try:
            with urlopen(self.frink_registry_url, timeout=30) as response:  # noqa: S310
                text = response.read().decode("utf-8")
            data = yaml.safe_load(text)
            if isinstance(data, dict) and isinstance(data.get("kgs"), list):
                entries = data["kgs"]
            elif isinstance(data, list):
                entries = data
            else:
                raise ValueError("Expected FRINK registry YAML with a top-level 'kgs' list")

            self._save_to_cache(entries)
            logger.info("Successfully fetched %s FRINK registry entries", len(entries))
            return entries
        except (HTTPError, URLError, ValueError, yaml.YAMLError) as exc:
            logger.error("Failed to fetch FRINK registry data: %s", exc)
            if self.cache_file.exists():
                logger.warning("Attempting to use expired FRINK cache as fallback")
                cached_data = self._load_from_cache()
                if cached_data is not None:
                    return cached_data
            raise

    def transform_frink_to_kg_registry(self, frink_kg: Dict[str, Any]) -> Dict[str, Any]:
        resource_id = str(frink_kg.get("shortname", "")).strip()
        if not resource_id:
            raise ValueError("FRINK entry is missing shortname")
        resource_id = SHORTNAME_ALIASES.get(resource_id, resource_id)

        resource_name = str(frink_kg.get("title", resource_id)).strip()
        description = str(frink_kg.get("description", "")).strip() or "Description unavailable."

        documentation_path = (
            frink_kg.get("frink-options", {}) or {}
        ).get("documentation-path") or resource_id
        homepage = frink_kg.get("homepage") or (
            f"https://frink.renci.org/registry/kgs/{documentation_path}/"
        )

        contacts = self._transform_contacts(frink_kg.get("contact"))
        products = self._build_products(resource_id=resource_id,
                                        resource_name=resource_name, data=frink_kg)

        resource = {
            "id": resource_id,
            "name": resource_name,
            "description": description,
            "activity_status": "active",
            "homepage_url": homepage,
            "contacts": contacts,
            "products": products,
            "collection": ["okn"],
            "domains": ["general"],
            "layout": "resource_detail",
            "category": "KnowledgeGraph",
        }
        return {k: v for k, v in resource.items() if v not in (None, [], "")}

    def _transform_contacts(self, contact_data: Any) -> List[Dict[str, Any]]:
        if not isinstance(contact_data, dict):
            return []

        contact: Dict[str, Any] = {"category": "Individual"}
        if contact_data.get("label"):
            contact["label"] = str(contact_data["label"]).strip()

        details: List[Dict[str, str]] = []
        if contact_data.get("email"):
            details.append({"contact_type": "email", "value": str(contact_data["email"]).strip()})
        if contact_data.get("github"):
            github_value = str(contact_data["github"]).strip()
            if github_value:
                details.append({"contact_type": "github", "value": github_value})

        if details:
            contact["contact_details"] = details

        return [contact] if len(contact) > 1 else []

    def _build_products(
        self, resource_id: str, resource_name: str, data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        products: List[Dict[str, Any]] = []

        sparql = data.get("sparql")
        if sparql:
            products.append(
                {
                    "id": f"{resource_id}.sparql",
                    "name": f"{resource_name} SPARQL",
                    "description": f"SPARQL endpoint for {resource_name}",
                    "category": "ProgrammingInterface",
                    "product_url": sparql,
                    "original_source": make_original_source_associations([resource_id]),
                }
            )

        tpf = data.get("tpf")
        if tpf:
            products.append(
                {
                    "id": f"{resource_id}.tpf",
                    "name": f"{resource_name} TPF",
                    "description": f"Triple Pattern Fragments endpoint for {resource_name}",
                    "category": "ProgrammingInterface",
                    "product_url": tpf,
                    "original_source": make_original_source_associations([resource_id]),
                }
            )

        return products

    def _load_existing_post(self, resource_file: Path) -> Tuple[Dict[str, Any], str]:
        if not resource_file.exists():
            return {}, ""

        try:
            post = frontmatter.load(resource_file)
            metadata = dict(post.metadata) if isinstance(post.metadata, dict) else {}
            return metadata, post.content
        except Exception as exc:
            logger.warning("Failed to load existing metadata from %s: %s", resource_file, exc)
            return {}, resource_file.read_text(encoding="utf-8")

    def _contact_identity(self, contact: Dict[str, Any]) -> Tuple[str, str, str]:
        email = ""
        github = ""
        for detail in contact.get("contact_details", []) or []:
            if not isinstance(detail, dict):
                continue
            if detail.get("contact_type") == "email":
                email = str(detail.get("value", "")).strip().lower()
            if detail.get("contact_type") == "github":
                github = str(detail.get("value", "")).strip().lower()
        label = str(contact.get("label", "")).strip().lower()
        return label, email, github

    def merge_contacts(
        self, existing_contacts: Any, synced_contacts: Any
    ) -> List[Dict[str, Any]]:
        existing = [copy.deepcopy(c) for c in existing_contacts or [] if isinstance(c, dict)]
        synced = [copy.deepcopy(c) for c in synced_contacts or [] if isinstance(c, dict)]
        if not existing:
            return synced
        if not synced:
            return existing

        merged = synced[:]
        seen = {self._contact_identity(contact) for contact in synced}
        for contact in existing:
            identity = self._contact_identity(contact)
            if identity in seen:
                continue
            merged.append(contact)
            seen.add(identity)
        return merged

    def merge_products(
        self, existing_products: Any, synced_products: Any, resource_id: str
    ) -> List[Dict[str, Any]]:
        existing = [copy.deepcopy(p) for p in existing_products or [] if isinstance(p, dict)]
        synced = [copy.deepcopy(p) for p in synced_products or [] if isinstance(p, dict)]
        if not existing:
            return synced
        if not synced:
            return existing

        synced_by_id = {
            product.get("id"): product for product in synced if isinstance(product.get("id"), str)
        }
        merged: List[Dict[str, Any]] = []
        seen_ids = set()

        for product in existing:
            product_id = product.get("id")
            if isinstance(product_id, str) and product_id in synced_by_id:
                updated = copy.deepcopy(product)
                updated.update(synced_by_id[product_id])
                if not updated.get("original_source"):
                    updated["original_source"] = make_original_source_associations([resource_id])
                merged.append(updated)
                seen_ids.add(product_id)
            else:
                merged.append(product)

        for product in synced:
            product_id = product.get("id")
            if product_id in seen_ids:
                continue
            merged.append(product)

        return merged

    def merge_resource_metadata(
        self, existing_metadata: Dict[str, Any], synced_metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        if not existing_metadata:
            return copy.deepcopy(synced_metadata)

        merged = copy.deepcopy(existing_metadata)

        for field in ["name", "description", "homepage_url", "activity_status", "category", "layout"]:
            if synced_metadata.get(field):
                merged[field] = synced_metadata[field]

        merged["collection"] = self._merge_unique_lists(
            existing_metadata.get("collection"), synced_metadata.get("collection")
        )
        merged["domains"] = self._merge_domains(
            existing_metadata.get("domains"), synced_metadata.get("domains")
        )
        merged["contacts"] = self.merge_contacts(
            existing_metadata.get("contacts"), synced_metadata.get("contacts")
        )
        merged["products"] = self.merge_products(
            existing_metadata.get("products"), synced_metadata.get(
                "products"), synced_metadata["id"]
        )

        return merged

    def _merge_unique_lists(self, existing: Any, synced: Any) -> List[Any]:
        merged: List[Any] = []
        for item in (existing or []) + (synced or []):
            if item not in merged:
                merged.append(item)
        return merged

    def _merge_domains(self, existing: Any, synced: Any) -> List[str]:
        existing_domains = [domain for domain in existing or [] if isinstance(domain, str)]
        synced_domains = [domain for domain in synced or [] if isinstance(domain, str)]

        if existing_domains:
            # Treat FRINK's fallback "general" domain as a backfill for missing data,
            # not as a domain to append to curated resource annotations.
            if synced_domains == ["general"]:
                cleaned_existing = [domain for domain in existing_domains if domain != "general"]
                return cleaned_existing or ["general"]
            return self._merge_unique_lists(existing_domains, synced_domains)

        return synced_domains

    def _metadata_for_compare(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        comparable = copy.deepcopy(metadata)
        comparable.pop("last_modified_date", None)
        return comparable

    def _content_for_compare(self, content: str) -> str:
        return content.strip()

    def _serialize_resource(self, metadata: Dict[str, Any], content: str) -> str:
        yaml_content = yaml.safe_dump(
            metadata,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
        ).strip()
        body = content.rstrip()
        if body:
            return f"---\n{yaml_content}\n---\n{body}\n"
        return f"---\n{yaml_content}\n---\n"

    def _default_content(self, resource_data: Dict[str, Any]) -> str:
        return (
            f"{resource_data['name']}\n\n"
            "## Description\n\n"
            f"{resource_data['description']}\n\n"
            "*This resource was automatically synchronized from the FRINK OKN registry.*"
        )

    def sync_kg(self, frink_kg: Dict[str, Any], dry_run: bool = False) -> str:
        synced_metadata = self.transform_frink_to_kg_registry(frink_kg)
        resource_id = synced_metadata["id"]
        resource_dir = self.registry_root / resource_id
        resource_file = resource_dir / f"{resource_id}.md"

        existing_metadata, existing_content = self._load_existing_post(resource_file)
        merged_metadata = self.merge_resource_metadata(existing_metadata, synced_metadata)

        today_iso = self._today_iso()
        if existing_metadata.get("creation_date"):
            merged_metadata["creation_date"] = existing_metadata["creation_date"]
        else:
            merged_metadata["creation_date"] = today_iso

        content = existing_content if self._content_for_compare(existing_content) else self._default_content(
            synced_metadata
        )

        is_new = not resource_file.exists()
        has_changed = is_new or (
            self._metadata_for_compare(existing_metadata)
            != self._metadata_for_compare(merged_metadata)
            or self._content_for_compare(existing_content) != self._content_for_compare(content)
        )

        if not has_changed:
            logger.info("No FRINK changes detected for %s", resource_id)
            return "skipped"

        merged_metadata["last_modified_date"] = today_iso
        if dry_run:
            logger.info("[DRY RUN] Would %s resource: %s",
                        "create" if is_new else "update", resource_id)
            return "created" if is_new else "updated"

        resource_dir.mkdir(parents=True, exist_ok=True)
        resource_file.write_text(
            self._serialize_resource(merged_metadata, content),
            encoding="utf-8",
        )
        logger.info("%s resource: %s", "Created" if is_new else "Updated", resource_id)
        return "created" if is_new else "updated"

    def sync_all(self, dry_run: bool = False, limit: Optional[int] = None) -> Dict[str, int]:
        logger.info("Starting FRINK OKN sync")
        stats = {"processed": 0, "created": 0, "updated": 0, "failed": 0, "skipped": 0}

        entries = self.fetch_frink_data()
        if limit:
            entries = entries[:limit]

        for entry in entries:
            resource_id = entry.get("shortname", "<missing>")
            logger.info("Processing FRINK entry: %s", resource_id)
            stats["processed"] += 1
            try:
                status = self.sync_kg(entry, dry_run=dry_run)
                stats[status] += 1
            except Exception as exc:
                logger.error("Failed to sync FRINK entry %s: %s", resource_id, exc)
                stats["failed"] += 1

        logger.info("FRINK sync completed. Stats: %s", stats)
        return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync FRINK OKN resources to KG-Registry")
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be done without writing files"
    )
    parser.add_argument(
        "--registry-root",
        type=str,
        help="Path to resource directory (default: ../resource)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of FRINK entries to process (for testing)",
    )
    parser.add_argument(
        "--no-cache", action="store_true", help="Disable cache and fetch fresh data"
    )
    parser.add_argument(
        "--cache-ttl",
        type=int,
        default=24,
        help="Cache time-to-live in hours (default: 24)",
    )

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    cache_ttl = 0 if args.no_cache else args.cache_ttl
    try:
        syncer = FRINKSync(registry_root=args.registry_root, cache_ttl_hours=cache_ttl)
        stats = syncer.sync_all(dry_run=args.dry_run, limit=args.limit)

        print("\nSync Summary:")
        print(f"  Processed: {stats['processed']}")
        print(f"  Created: {stats['created']}")
        print(f"  Updated: {stats['updated']}")
        print(f"  Failed: {stats['failed']}")
        print(f"  Skipped: {stats['skipped']}")

        if stats["processed"] == 0 or (
            stats["created"] == 0 and stats["updated"] == 0 and stats["failed"] == stats["processed"]
        ):
            sys.exit(1)
    except Exception as exc:
        logger.error("FRINK sync failed: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
