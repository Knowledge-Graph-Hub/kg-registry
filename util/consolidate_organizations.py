#!/usr/bin/env python3
"""
Consolidate duplicate organization pages into single canonical pages.

This script:
1. Creates canonical organization pages (broad, fda, who)
2. Removes duplicate organization directories
3. Updates resource contacts to use the canonical org IDs
"""

import os
import pathlib
import re
import shutil
from datetime import datetime

import frontmatter

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOURCE_DIR = ROOT / "resource"
ORG_DIR = ROOT / "org"

# Organizations to consolidate
# Format: {canonical_id: {"label": display_label, "duplicates": [list of duplicate org IDs to remove], "patterns": [regex patterns to match in contacts]}}
CONSOLIDATIONS = {
    "broad": {
        "label": "Broad Institute",
        "short_id": "Broad",
        "description": "The Broad Institute of MIT and Harvard is a biomedical and genomic research center located in Cambridge, Massachusetts. It was founded in 2004 to bring together faculty, professional staff, and students from across MIT and Harvard to pursue transformative research in human disease. The Broad Institute develops and applies new tools and methods for genomic medicine, including genome sequencing, computational biology, and therapeutic development.",
        "homepage_url": "https://www.broadinstitute.org/",
        "github_url": "https://github.com/broadinstitute",
        "duplicates": [
            "broad-institute",
            "broad-institute-of-mit-and-harvard",
            "broad-institute-center-for-the-science-of-therapeu",
            "broad-institute-lincs-transcriptomics-center",
            "broad-institute-translator-team",
            "depmap-team-broad-institute",
            "project-achilles-broad-institute",
        ],
        "patterns": [
            r"(?i)broad\s*institute",
            r"(?i)project\s*achilles.*broad",
            r"(?i)depmap.*broad",
        ]
    },
    "fda": {
        "label": "U.S. Food and Drug Administration",
        "short_id": "FDA",
        "description": "The U.S. Food and Drug Administration (FDA) is a federal agency of the Department of Health and Human Services responsible for protecting public health by ensuring the safety, efficacy, and security of human and veterinary drugs, biological products, medical devices, food supply, cosmetics, and products that emit radiation.",
        "homepage_url": "https://www.fda.gov/",
        "github_url": "https://github.com/FDA",
        "duplicates": [
            "fda-center-for-drug-evaluation-and-research",
            "fda-substance-registration-system-team",
        ],
        "patterns": [
            r"(?i)\bfda\b",
            r"(?i)food\s+and\s+drug\s+administration",
        ]
    },
    "who": {
        "label": "World Health Organization",
        "short_id": "WHO",
        "description": "The World Health Organization (WHO) is a specialized agency of the United Nations responsible for international public health. Founded in 1948, WHO coordinates international health activities, sets health standards, and provides technical assistance to countries. WHO maintains important health classifications including ICD (International Classification of Diseases) and manages global health initiatives.",
        "homepage_url": "https://www.who.int/",
        "github_url": "https://github.com/WorldHealthOrganization",
        "duplicates": [
            "world-health-organization",
            "who-family-of-international-classifications",
        ],
        "patterns": [
            r"(?i)world\s*health\s*organization",
            r"(?i)\bwho\b(?!\.)",  # WHO but not in URLs
            r"(?i)who\s+family",
        ]
    },
    "sib": {
        "label": "SIB Swiss Institute of Bioinformatics",
        "short_id": "SIB",
        "description": "The SIB Swiss Institute of Bioinformatics is an academic institution dedicated to biological and biomedical data science. Founded in 1998, SIB coordinates research and education in bioinformatics throughout Switzerland and provides a wide range of bioinformatics databases, software tools, and services to life science researchers worldwide.",
        "homepage_url": "https://www.sib.swiss/",
        "github_url": "https://github.com/sib-swiss",
        "duplicates": [
            "bgee-team-sib-swiss-institute-of-bioinformatics",
            "calipho-group-sib-swiss-institute-of-bioinformatic",
            "evgeny-zdobnov-lab-sib-swiss-institute-of-bioinfor",
            "glyconnect-team-sib-swiss-institute-of-bioinformat",
            "metanetx-team-sib-swiss-institute-of-bioinformatic",
            "oma-team-sib-swiss-institute-of-bioinformatics",
            "sibils-swiss-institute-of-bioinformatics-literatur",
        ],
        "patterns": [
            r"(?i)sib\s+swiss\s+institute",
            r"(?i)swiss\s+institute\s+of\s+bioinformatics",
            r"(?i)\bsib\b.*bioinformatics",
        ]
    },
    "monarchinitiative": {
        "label": "Monarch Initiative",
        "short_id": "Monarch",
        "description": "The Monarch Initiative is an international consortium that integrates, aligns, and redistributes cross-species gene, genotype, variant, disease, and phenotype data to improve understanding of genetic disease and support translational research.",
        "homepage_url": "https://monarchinitiative.org/",
        "github_url": "https://github.com/monarch-initiative",
        "duplicates": [
            "monarch-initiative",
        ],
        "patterns": [
            r"(?i)monarch\s*initiative",
        ]
    },
}


def create_canonical_org_page(org_id: str, info: dict) -> bool:
    """Create a canonical organization page."""
    org_dir = ORG_DIR / org_id
    org_file = org_dir / f"{org_id}.md"
    
    if org_file.exists():
        print(f"  Organization page already exists: {org_file}")
        return False
    
    org_dir.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%dT00:00:00Z")
    
    metadata = {
        "id": org_id,
        "category": "Organization",
        "layout": "organization_detail",
        "label": info["label"],
        "short_id": info.get("short_id"),
        "description": info["description"],
        "homepage_url": info.get("homepage_url"),
        "creation_date": today,
        "last_modified_date": today,
    }
    
    if info.get("github_url"):
        metadata["github_url"] = info["github_url"]
    
    # Remove None values
    metadata = {k: v for k, v in metadata.items() if v is not None}
    
    content = f"""
{info['label']} is an organization associated with resources in the KG-Registry.
"""
    
    post = frontmatter.Post(content.strip())
    post.metadata = metadata
    
    with open(org_file, 'wb') as f:
        frontmatter.dump(post, f)
    
    print(f"  ✅ Created canonical org page: {org_file}")
    return True


def remove_duplicate_orgs(duplicates: list) -> int:
    """Remove duplicate organization directories."""
    removed = 0
    for dup_id in duplicates:
        dup_dir = ORG_DIR / dup_id
        if dup_dir.exists():
            shutil.rmtree(dup_dir)
            print(f"  🗑️  Removed duplicate: {dup_dir}")
            removed += 1
    return removed


def update_resource_contacts(canonical_id: str, patterns: list) -> int:
    """Update resource contacts to use the canonical org ID."""
    updated = 0
    
    for resource_dir in sorted(RESOURCE_DIR.iterdir()):
        if not resource_dir.is_dir():
            continue
        
        for md_file in resource_dir.glob("*.md"):
            # Skip product pages
            if md_file.stem.count('.') > 0 and md_file.stem != resource_dir.name:
                continue
            
            try:
                post = frontmatter.load(md_file)
            except Exception as e:
                print(f"  Error loading {md_file}: {e}")
                continue
            
            modified = False
            
            # Check contacts
            contacts = post.metadata.get("contacts", [])
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
                        print(f"  📝 {md_file.name}: '{label}' -> id: {canonical_id}")
                        break
            
            # Check curators too
            curators = post.metadata.get("curators", [])
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
                        print(f"  📝 {md_file.name} (curator): '{label}' -> id: {canonical_id}")
                        break
            
            if modified:
                with open(md_file, 'wb') as f:
                    frontmatter.dump(post, f)
                updated += 1
    
    return updated


def main():
    print("Consolidating organization pages...\n")
    
    for canonical_id, info in CONSOLIDATIONS.items():
        print(f"\n{'='*60}")
        print(f"Processing: {info['label']} (id: {canonical_id})")
        print('='*60)
        
        # Create canonical page
        print("\n1. Creating canonical organization page:")
        create_canonical_org_page(canonical_id, info)
        
        # Remove duplicates
        print("\n2. Removing duplicate organization directories:")
        removed = remove_duplicate_orgs(info["duplicates"])
        print(f"   Removed {removed} duplicate(s)")
        
        # Update resource contacts
        print("\n3. Updating resource contacts:")
        updated = update_resource_contacts(canonical_id, info["patterns"])
        print(f"   Updated {updated} resource file(s)")
    
    print("\n" + "="*60)
    print("✅ Consolidation complete!")
    print("="*60)


if __name__ == "__main__":
    main()
