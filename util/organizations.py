#!/usr/bin/env python3
"""
Organization management utilities for KG-Registry.

This module provides functions for:
- Creating organization pages
- Combining organization pages into registry files
- Consolidating duplicate organizations
- Updating resource contacts with organization references
"""

import argparse
import pathlib
import re
import shutil
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

import frontmatter

from common import (
    ROOT,
    RESOURCE_DIR,
    ORG_DIR,
    REGISTRY_DIR,
    create_id_from_label,
    get_today_iso,
    load_frontmatter_file,
    save_frontmatter_file,
)

__all__ = [
    # Constants
    "PARENT_ORGANIZATIONS",
    "DEFAULT_OUTPUT_FILE",
    # Functions
    "get_existing_org_ids",
    "get_parent_org_id",
    "create_organization_page",
    "remove_organization",
    "combine_organizations",
    "update_resource_contacts",
    "process_resource_organizations",
]

# =============================================================================
# Constants
# =============================================================================

DEFAULT_OUTPUT_FILE = REGISTRY_DIR / "organizations.yml"

# Parent organizations and patterns to match their teams
# Format: {parent_id: {"label": display_label, "patterns": [list of regex patterns]}}
PARENT_ORGANIZATIONS = {
    "ebi": {
        "label": "European Bioinformatics Institute",
        "patterns": [
            r"(?i)embl[\s-]*ebi",
            r"(?i)european\s+bioinformatics\s+institute",
            r"(?i)at\s+embl[\s-]*ebi",
            r"(?i)at\s+ebi",
            r"(?i)\(embl[\s-]*ebi\)",
            r"(?i)\(ebi\)",
            r"(?i)ensembl",
            r"(?i)chembl",
            r"(?i)uniprot",
            r"(?i)interpro",
            r"(?i)intact",
            r"(?i)reactome",
            r"(?i)rfam",
            r"(?i)pfam",
            r"(?i)rnacentral",
            r"(?i)goa\s+team",
            r"(?i)gwas\s*catalog",
            r"(?i)complex\s*portal",
            r"(?i)expression\s*atlas",
        ]
    },
    "ncbi": {
        "label": "National Center for Biotechnology Information",
        "patterns": [
            r"(?i)ncbi",
            r"(?i)national\s+center\s+for\s+biotechnology\s+information",
            r"(?i)national\s+library\s+of\s+medicine",
            r"(?i)\bnlm\b",
            r"(?i)pubmed",
            r"(?i)pubchem",
            r"(?i)clinvar",
            r"(?i)dbsnp",
            r"(?i)refseq",
            r"(?i)entrez",
            r"(?i)gene\s+database",
            r"(?i)homologene",
        ]
    },
    "wikimedia": {
        "label": "Wikimedia Foundation",
        "patterns": [
            r"(?i)wikimedia",
            r"(?i)wikipedia",
            r"(?i)wikidata",
        ]
    },
}


# =============================================================================
# Helper Functions
# =============================================================================


def get_existing_org_ids() -> Set[str]:
    """
    Get set of existing organization IDs.
    
    Returns:
        Set of organization directory names
    """
    if not ORG_DIR.exists():
        return set()
    return {d.name for d in ORG_DIR.iterdir() if d.is_dir()}


def get_parent_org_id(label: str) -> Optional[str]:
    """
    Check if an organization label matches a known parent organization pattern.
    
    Args:
        label: The organization label to check
        
    Returns:
        The parent organization ID if matched, None otherwise
    """
    for parent_id, info in PARENT_ORGANIZATIONS.items():
        for pattern in info["patterns"]:
            if re.search(pattern, label):
                return parent_id
    return None


# =============================================================================
# Organization Page Management
# =============================================================================


def create_organization_page(
    org_id: str,
    label: str,
    description: Optional[str] = None,
    homepage_url: Optional[str] = None,
    github_url: Optional[str] = None,
    short_id: Optional[str] = None,
    contact_details: Optional[List] = None,
    dry_run: bool = False,
    verbose: bool = True,
) -> bool:
    """
    Create a new organization page.
    
    Args:
        org_id: The organization ID (used for directory and filename)
        label: The organization label (display name)
        description: Description of the organization
        homepage_url: Organization's homepage URL
        github_url: Organization's GitHub URL
        short_id: Short form of the organization name
        contact_details: Optional contact details
        dry_run: If True, don't actually create the file
        verbose: If True, print status messages
        
    Returns:
        True if page was created, False if it already exists
    """
    org_dir = ORG_DIR / org_id
    org_file = org_dir / f"{org_id}.md"
    
    if org_file.exists():
        if verbose:
            print(f"  Organization page already exists: {org_file}")
        return False
    
    if dry_run:
        if verbose:
            print(f"  Would create organization page: {org_file}")
        return True
    
    # Create directory
    org_dir.mkdir(parents=True, exist_ok=True)
    
    # Build metadata
    today = get_today_iso()
    
    metadata = {
        "id": org_id,
        "category": "Organization",
        "layout": "organization_detail",
        "label": label,
        "description": description or f"{label} is an organization associated with knowledge graph resources in the KG-Registry.",
        "creation_date": today,
        "last_modified_date": today,
    }
    
    # Add optional fields
    if short_id:
        metadata["short_id"] = short_id
    if homepage_url:
        metadata["homepage_url"] = homepage_url
    if github_url:
        metadata["github_url"] = github_url
    if contact_details:
        metadata["contact_details"] = contact_details
    
    # Create content
    content = f"""
{label} is an organization associated with resources in the KG-Registry. This page was auto-generated and may need additional curation.
""".strip()
    
    # Save the file
    save_frontmatter_file(org_file, metadata, content)
    
    if verbose:
        print(f"  ✅ Created organization page: {org_file}")
    
    return True


def remove_organization(org_id: str, dry_run: bool = False, verbose: bool = True) -> bool:
    """
    Remove an organization directory.
    
    Args:
        org_id: The organization ID to remove
        dry_run: If True, don't actually remove
        verbose: If True, print status messages
        
    Returns:
        True if removed, False if didn't exist
    """
    org_dir = ORG_DIR / org_id
    
    if not org_dir.exists():
        return False
    
    if dry_run:
        if verbose:
            print(f"  Would remove: {org_dir}")
        return True
    
    shutil.rmtree(org_dir)
    
    if verbose:
        print(f"  🗑️  Removed: {org_dir}")
    
    return True


# =============================================================================
# Organization Combination
# =============================================================================


def combine_organizations(
    output_path: pathlib.Path = DEFAULT_OUTPUT_FILE,
    verbose: bool = True,
) -> int:
    """
    Read all organization .md files and combine their frontmatter into a single YAML file.
    
    Args:
        output_path: Path to write the combined YAML output
        verbose: If True, print status messages
        
    Returns:
        Number of organizations combined
    """
    import yaml
    
    organizations = []
    
    if not ORG_DIR.exists():
        if verbose:
            print(f"Warning: Organization directory {ORG_DIR} does not exist")
        return 0
    
    for org_subdir in sorted(ORG_DIR.iterdir()):
        if not org_subdir.is_dir():
            continue
        
        # Look for .md files in each organization subdirectory
        for md_file in org_subdir.glob("*.md"):
            metadata, _, error = load_frontmatter_file(md_file, use_ruamel=False)
            
            if error:
                print(f"Error loading {md_file}: {error}", file=sys.stderr)
                continue
            
            if not metadata:
                continue
                
            # Ensure it's actually an Organization
            if metadata.get("category") != "Organization":
                if verbose:
                    print(f"Warning: Skipping {md_file} - not an Organization (category: {metadata.get('category')})")
                continue
            
            organizations.append(metadata)
            if verbose:
                print(f"Loaded organization: {metadata.get('id', 'unknown')}")
    
    # Sort by ID
    organizations.sort(key=lambda x: x.get("id", ""))
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write("# Combined Organization metadata\n")
        f.write("# Auto-generated - do not edit directly\n")
        f.write("# Edit the individual files in org/ instead\n\n")
        f.write("organizations:\n")
        yaml.dump(organizations, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    if verbose:
        print(f"\n✅ Combined {len(organizations)} organization(s) into {output_path}")
    
    return len(organizations)


# =============================================================================
# Resource Contact Management
# =============================================================================


def update_resource_contacts(
    canonical_id: str,
    patterns: List[str],
    dry_run: bool = False,
    verbose: bool = True,
) -> int:
    """
    Update resource contacts to use a canonical organization ID.
    
    Args:
        canonical_id: The canonical organization ID to use
        patterns: Regex patterns to match organization labels
        dry_run: If True, don't actually update files
        verbose: If True, print status messages
        
    Returns:
        Number of resource files updated
    """
    updated = 0
    
    for resource_dir in sorted(RESOURCE_DIR.iterdir()):
        if not resource_dir.is_dir():
            continue
        
        for md_file in resource_dir.glob("*.md"):
            # Skip product pages
            if md_file.stem.count('.') > 0 and md_file.stem != resource_dir.name:
                continue
            
            metadata, content, error = load_frontmatter_file(md_file, use_ruamel=False)
            if error:
                if verbose:
                    print(f"  Error loading {md_file}: {error}")
                continue
            
            if not metadata:
                continue
            
            modified = False
            
            # Check contacts
            contacts = metadata.get("contacts", [])
            for contact in contacts:
                if contact.get("category") != "Organization":
                    continue
                
                label = contact.get("label", "")
                existing_id = contact.get("id")
                
                # Skip if already has the canonical ID
                if existing_id == canonical_id:
                    continue
                
                # Check if label matches any pattern
                for pattern in patterns:
                    if re.search(pattern, label):
                        contact["id"] = canonical_id
                        modified = True
                        if verbose:
                            print(f"  📝 {md_file.name}: '{label}' -> id: {canonical_id}")
                        break
            
            # Check curators too
            curators = metadata.get("curators", [])
            for curator in curators:
                if curator.get("category") != "Organization":
                    continue
                
                label = curator.get("label", "")
                existing_id = curator.get("id")
                
                if existing_id == canonical_id:
                    continue
                
                for pattern in patterns:
                    if re.search(pattern, label):
                        curator["id"] = canonical_id
                        modified = True
                        if verbose:
                            print(f"  📝 {md_file.name} (curator): '{label}' -> id: {canonical_id}")
                        break
            
            if modified:
                if not dry_run:
                    post = frontmatter.Post(content or "")
                    post.metadata = metadata
                    with open(md_file, 'wb') as f:
                        frontmatter.dump(post, f)
                updated += 1
    
    return updated


def process_resource_organizations(
    dry_run: bool = True,
    create_pages: bool = True,
    update_contacts: bool = True,
    verbose: bool = True,
) -> Tuple[int, int]:
    """
    Process all resource files to find Organization contacts.
    
    Creates new organization pages for unknown orgs and updates
    resource contacts with parent organization IDs where appropriate.
    
    Args:
        dry_run: If True, only report what would be done
        create_pages: If True, create new organization pages
        update_contacts: If True, update resource contacts
        verbose: If True, print status messages
        
    Returns:
        Tuple of (organizations_created, contacts_updated)
    """
    # Track organizations found
    orgs_to_create: Dict[str, Dict[str, Any]] = {}
    contacts_to_update: List[Tuple[pathlib.Path, int, str, str]] = []
    existing_org_ids = get_existing_org_ids()
    
    if verbose:
        print(f"Found {len(existing_org_ids)} existing organization(s)")
        print()
    
    # Process each resource file
    for resource_dir in sorted(RESOURCE_DIR.iterdir()):
        if not resource_dir.is_dir():
            continue
        
        for md_file in resource_dir.glob("*.md"):
            # Skip product pages
            if md_file.stem.count('.') > 0 and md_file.stem != resource_dir.name:
                continue
            
            metadata, _, error = load_frontmatter_file(md_file, use_ruamel=False)
            if error:
                if verbose:
                    print(f"Error loading {md_file}: {error}")
                continue
            
            if not metadata:
                continue
            
            contacts = metadata.get("contacts", [])
            
            for idx, contact in enumerate(contacts):
                if contact.get("category") != "Organization":
                    continue
                
                label = contact.get("label", "")
                existing_id = contact.get("id")
                contact_details = contact.get("contact_details", [])
                
                if not label:
                    continue
                
                # Check if this is a team of a known parent organization
                parent_id = get_parent_org_id(label)
                
                if parent_id:
                    # This is a team of a parent organization
                    if existing_id != parent_id:
                        contacts_to_update.append((md_file, idx, parent_id, label))
                        if verbose:
                            print(f"📝 {md_file.name}: '{label}' -> add id: {parent_id}")
                else:
                    # This is a standalone organization
                    if existing_id and existing_id in existing_org_ids:
                        continue
                    
                    # Generate an org ID
                    org_id = existing_id if existing_id else create_id_from_label(label)
                    
                    if org_id in existing_org_ids:
                        if not existing_id:
                            contacts_to_update.append((md_file, idx, org_id, label))
                            if verbose:
                                print(f"📝 {md_file.name}: '{label}' -> add id: {org_id}")
                    else:
                        # Need to create new org page
                        if org_id not in orgs_to_create:
                            orgs_to_create[org_id] = {
                                "label": label,
                                "contact_details": contact_details if contact_details else None
                            }
                            if verbose:
                                print(f"🆕 New organization: '{label}' (id: {org_id})")
    
    if verbose:
        print()
        print(f"Summary:")
        print(f"  Organizations to create: {len(orgs_to_create)}")
        print(f"  Contacts to update: {len(contacts_to_update)}")
        print()
    
    orgs_created = 0
    contacts_updated = 0
    
    if dry_run:
        if verbose:
            print("DRY RUN - no changes made.")
        return (len(orgs_to_create), len(contacts_to_update))
    
    # Create organization pages
    if create_pages and orgs_to_create:
        if verbose:
            print("Creating organization pages...")
        for org_id, info in sorted(orgs_to_create.items()):
            if create_organization_page(org_id, info["label"], contact_details=info.get("contact_details")):
                orgs_created += 1
    
    # Update resource contacts
    if update_contacts and contacts_to_update:
        if verbose:
            print("Updating resource contacts...")
        for resource_file, contact_idx, parent_id, label in contacts_to_update:
            metadata, content, error = load_frontmatter_file(resource_file, use_ruamel=False)
            if error or not metadata:
                continue
            
            contacts = metadata.get("contacts", [])
            if contact_idx < len(contacts):
                if contacts[contact_idx].get("id") != parent_id:
                    contacts[contact_idx]["id"] = parent_id
                    
                    post = frontmatter.Post(content or "")
                    post.metadata = metadata
                    with open(resource_file, 'wb') as f:
                        frontmatter.dump(post, f)
                    
                    contacts_updated += 1
                    if verbose:
                        print(f"  ✅ Updated {resource_file.name}: '{label}' -> id: {parent_id}")
    
    return (orgs_created, contacts_updated)


# =============================================================================
# CLI Entry Points
# =============================================================================


def main_combine():
    """CLI entry point for combining organizations."""
    parser = argparse.ArgumentParser(
        description="Combine Organization YAML files into a single file"
    )
    parser.add_argument(
        "-o", "--output",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_FILE,
        help=f"Output file path (default: {DEFAULT_OUTPUT_FILE})"
    )
    
    args = parser.parse_args()
    combine_organizations(args.output)


def main_create():
    """CLI entry point for creating organization pages."""
    parser = argparse.ArgumentParser(
        description="Create Organization pages and update Resource contacts"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually make changes (default is dry run)"
    )
    parser.add_argument(
        "--no-create-pages",
        action="store_true",
        help="Don't create new organization pages"
    )
    parser.add_argument(
        "--no-update-contacts",
        action="store_true",
        help="Don't update resource contacts"
    )
    
    args = parser.parse_args()
    
    process_resource_organizations(
        dry_run=not args.execute,
        create_pages=not args.no_create_pages,
        update_contacts=not args.no_update_contacts
    )


def main():
    """Main CLI entry point with subcommands."""
    parser = argparse.ArgumentParser(
        description="Organization management utilities for KG-Registry"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Combine subcommand
    combine_parser = subparsers.add_parser(
        "combine",
        help="Combine all organization pages into a single YAML file"
    )
    combine_parser.add_argument(
        "-o", "--output",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_FILE,
        help=f"Output file path (default: {DEFAULT_OUTPUT_FILE})"
    )
    
    # Create subcommand
    create_parser = subparsers.add_parser(
        "create",
        help="Create organization pages from resource contacts"
    )
    create_parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually make changes (default is dry run)"
    )
    create_parser.add_argument(
        "--no-create-pages",
        action="store_true",
        help="Don't create new organization pages"
    )
    create_parser.add_argument(
        "--no-update-contacts",
        action="store_true",
        help="Don't update resource contacts"
    )
    
    # Consolidate subcommand (placeholder for consolidation logic)
    consolidate_parser = subparsers.add_parser(
        "consolidate",
        help="Consolidate duplicate organizations"
    )
    consolidate_parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually make changes (default is dry run)"
    )
    
    args = parser.parse_args()
    
    if args.command == "combine":
        combine_organizations(args.output)
    elif args.command == "create":
        process_resource_organizations(
            dry_run=not args.execute,
            create_pages=not args.no_create_pages,
            update_contacts=not args.no_update_contacts
        )
    elif args.command == "consolidate":
        print("Consolidation logic - see consolidate_organizations.py for specific consolidations")
        print("This command can be extended with specific consolidation rules.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
