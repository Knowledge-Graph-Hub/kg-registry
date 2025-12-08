#!/usr/bin/env python3
"""
Create Organization pages for all Organizations used as Contacts in Resource pages.

For organizations that are teams of known parent organizations (EBI, NCBI, Wikimedia),
this script adds the parent organization's ID to the contact instead of creating
a new organization page.

For other organizations, it creates new Organization pages with stub content.
"""

import argparse
import os
import pathlib
import re
import sys
from datetime import datetime
from typing import Optional

import frontmatter
from ruamel.yaml import YAML

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOURCE_DIR = ROOT / "resource"
ORG_DIR = ROOT / "org"

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
            r"(?i)ensembl",  # Ensembl is at EBI
            r"(?i)chembl",   # ChEMBL is at EBI
            r"(?i)uniprot",  # UniProt has EBI involvement
            r"(?i)interpro", # InterPro is at EBI
            r"(?i)intact",   # IntAct is at EBI
            r"(?i)reactome", # Reactome has EBI involvement
            r"(?i)rfam",     # Rfam is at EBI
            r"(?i)pfam",     # Pfam is at EBI
            r"(?i)rnacentral", # RNAcentral is at EBI
            r"(?i)goa\s+team", # GOA is at EBI
            r"(?i)gwas\s*catalog", # GWAS Catalog is at EBI
            r"(?i)complex\s*portal", # Complex Portal is at EBI
            r"(?i)expression\s*atlas", # Expression Atlas is at EBI
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


def create_org_id(label: str) -> str:
    """
    Create a valid organization ID from a label.
    
    Args:
        label: The organization label
        
    Returns:
        A lowercase, hyphenated ID suitable for use as a directory/file name
    """
    # Remove special characters and convert to lowercase
    org_id = re.sub(r'[^\w\s-]', '', label.lower())
    # Replace spaces with hyphens
    org_id = re.sub(r'\s+', '-', org_id)
    # Remove multiple consecutive hyphens
    org_id = re.sub(r'-+', '-', org_id)
    # Strip leading/trailing hyphens
    org_id = org_id.strip('-')
    # Truncate to reasonable length
    if len(org_id) > 50:
        org_id = org_id[:50].rstrip('-')
    return org_id


def create_organization_page(org_id: str, label: str, contact_details: list = None) -> bool:
    """
    Create a new organization page.
    
    Args:
        org_id: The organization ID (used for directory and filename)
        label: The organization label (display name)
        contact_details: Optional contact details from the resource
        
    Returns:
        True if page was created, False if it already exists
    """
    org_dir = ORG_DIR / org_id
    org_file = org_dir / f"{org_id}.md"
    
    if org_file.exists():
        print(f"  Organization page already exists: {org_file}")
        return False
    
    # Create directory
    org_dir.mkdir(parents=True, exist_ok=True)
    
    # Prepare frontmatter
    today = datetime.now().strftime("%Y-%m-%dT00:00:00Z")
    
    metadata = {
        "id": org_id,
        "category": "Organization",
        "layout": "organization_detail",
        "label": label,
        "description": f"{label} is an organization associated with knowledge graph resources in the KG-Registry.",
        "creation_date": today,
        "last_modified_date": today,
    }
    
    # Add contact details if provided
    if contact_details:
        metadata["contact_details"] = contact_details
    
    # Create the page content
    content = f"""
{label} is an organization associated with resources in the KG-Registry. This page was auto-generated and may need additional curation.
"""
    
    # Write the file
    post = frontmatter.Post(content.strip())
    post.metadata = metadata
    
    with open(org_file, 'wb') as f:
        frontmatter.dump(post, f)
    
    print(f"  ✅ Created organization page: {org_file}")
    return True


def update_resource_contact(resource_file: pathlib.Path, contact_idx: int, parent_id: str) -> bool:
    """
    Update a resource contact to add the parent organization ID.
    
    Args:
        resource_file: Path to the resource file
        contact_idx: Index of the contact to update
        parent_id: The parent organization ID to add
        
    Returns:
        True if updated, False otherwise
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 1500
    
    post = frontmatter.load(resource_file)
    
    contacts = post.metadata.get("contacts", [])
    if contact_idx >= len(contacts):
        return False
    
    contact = contacts[contact_idx]
    
    # Check if already has the correct ID
    if contact.get("id") == parent_id:
        return False
    
    # Add the parent ID
    contact["id"] = parent_id
    
    # Write back
    with open(resource_file, 'wb') as f:
        frontmatter.dump(post, f)
    
    return True


def process_resources(dry_run: bool = True, create_pages: bool = True, update_contacts: bool = True):
    """
    Process all resource files to find Organization contacts.
    
    Args:
        dry_run: If True, only report what would be done
        create_pages: If True, create new organization pages for unknown orgs
        update_contacts: If True, update resource contacts with parent org IDs
    """
    # Track organizations found
    orgs_to_create = {}  # {org_id: {"label": label, "contact_details": details}}
    contacts_to_update = []  # [(resource_file, contact_idx, parent_id, label)]
    existing_org_ids = set()
    
    # Get existing organization IDs
    if ORG_DIR.exists():
        for org_subdir in ORG_DIR.iterdir():
            if org_subdir.is_dir():
                existing_org_ids.add(org_subdir.name)
    
    print(f"Found {len(existing_org_ids)} existing organization(s): {sorted(existing_org_ids)}")
    print()
    
    # Process each resource file
    for resource_dir in sorted(RESOURCE_DIR.iterdir()):
        if not resource_dir.is_dir():
            continue
        
        for md_file in resource_dir.glob("*.md"):
            # Skip product pages (they have dots in the filename before .md)
            if md_file.stem.count('.') > 0 and md_file.stem != resource_dir.name:
                continue
            
            try:
                post = frontmatter.load(md_file)
            except Exception as e:
                print(f"Error loading {md_file}: {e}")
                continue
            
            contacts = post.metadata.get("contacts", [])
            
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
                        print(f"📝 {md_file.name}: '{label}' -> add id: {parent_id}")
                else:
                    # This is a standalone organization
                    if existing_id and existing_id in existing_org_ids:
                        # Already has an ID pointing to existing org
                        continue
                    
                    # Generate an org ID
                    org_id = existing_id if existing_id else create_org_id(label)
                    
                    if org_id in existing_org_ids:
                        # Org page exists, but contact doesn't reference it
                        if not existing_id:
                            contacts_to_update.append((md_file, idx, org_id, label))
                            print(f"📝 {md_file.name}: '{label}' -> add id: {org_id}")
                    else:
                        # Need to create new org page
                        if org_id not in orgs_to_create:
                            orgs_to_create[org_id] = {
                                "label": label,
                                "contact_details": contact_details if contact_details else None
                            }
                            print(f"🆕 New organization: '{label}' (id: {org_id})")
    
    print()
    print(f"Summary:")
    print(f"  Organizations to create: {len(orgs_to_create)}")
    print(f"  Contacts to update: {len(contacts_to_update)}")
    print()
    
    if dry_run:
        print("DRY RUN - no changes made. Run with --execute to apply changes.")
        return
    
    # Create organization pages
    if create_pages and orgs_to_create:
        print("Creating organization pages...")
        for org_id, info in sorted(orgs_to_create.items()):
            create_organization_page(org_id, info["label"], info.get("contact_details"))
    
    # Update resource contacts
    if update_contacts and contacts_to_update:
        print("Updating resource contacts...")
        for resource_file, contact_idx, parent_id, label in contacts_to_update:
            if update_resource_contact(resource_file, contact_idx, parent_id):
                print(f"  ✅ Updated {resource_file.name}: '{label}' -> id: {parent_id}")


def main():
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
    
    process_resources(
        dry_run=not args.execute,
        create_pages=not args.no_create_pages,
        update_contacts=not args.no_update_contacts
    )


if __name__ == "__main__":
    main()
