#!/usr/bin/env python3
"""
Automatically annotate resources with NCBITaxon IDs based on descriptions and metadata.

This script scans all resource markdown files and intelligently assigns appropriate
NCBITaxon identifiers based on keywords in descriptions, domains, and categories.

Usage:
    python util/auto_annotate_taxa.py [--dry-run] [--verbose] [--limit N]
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Optional
import yaml

# Taxon mapping based on organism keywords
TAXON_KEYWORDS = {
    'NCBITaxon:9606': {  # Human
        'keywords': ['human', 'homo sapiens', 'h. sapiens', 'hsa', 'clinical', 'patient', 'disease', 'medical', 'cancer cell', 'cell line', 'genome project', 'genome sample'],
        'patterns': [r'human\s+', r'humans?$', r'homo\s+sapiens', r'\bhsa\b', r'clinical', r'medical genetics', r'personalized medicine', r'cancer\s+cell', r'cell\s+line', r'genome\s+sample']
    },
    'NCBITaxon:10090': {  # Mouse
        'keywords': ['mouse', 'mus musculus', 'murine', 'transgenic mouse'],
        'patterns': [r'mouse', r'mus\s+musculus', r'murine', r'transgenic\s+mouse']
    },
    'NCBITaxon:10116': {  # Rat
        'keywords': ['rat', 'rattus', 'rodent'],
        'patterns': [r'\brat\b', r'rattus', r'rodent']
    },
    'NCBITaxon:7227': {  # Fruit fly (Drosophila)
        'keywords': ['drosophila', 'fruit fly', 'fly genetics'],
        'patterns': [r'drosophila', r'fruit\s+fly', r'flybase']
    },
    'NCBITaxon:6239': {  # C. elegans
        'keywords': ['caenorhabditis elegans', 'c. elegans', 'worm'],
        'patterns': [r'caenorhabditis', r'c\.\s+elegans', r'wormbase']
    },
    'NCBITaxon:7955': {  # Zebrafish
        'keywords': ['zebrafish', 'danio rerio'],
        'patterns': [r'zebrafish', r'danio\s+rerio']
    },
    'NCBITaxon:4932': {  # Yeast (S. cerevisiae)
        'keywords': ['saccharomyces cerevisiae', 'yeast', 's. cerevisiae', 'sgd'],
        'patterns': [r'saccharomyces', r'\byeast\b', r'cerevisiae']
    },
    'NCBITaxon:3702': {  # Arabidopsis thaliana
        'keywords': ['arabidopsis', 'a. thaliana', 'plant'],
        'patterns': [r'arabidopsis', r'a\.\s+thaliana', r'tair']
    },
    'NCBITaxon:40674': {  # Mammalia (all mammals)
        'keywords': ['mammal', 'mammalian', 'mammalogist'],
        'patterns': [r'mammal']
    },
    'NCBITaxon:2': {  # Bacteria
        'keywords': ['bacteria', 'bacterial', 'prokaryote', 'microbial', 'microbiome', 'microbiota', '16s', 'metagenom'],
        'patterns': [r'\bbacteria\b', r'bacterial', r'prokaryot', r'microbial', r'microbiome', r'microbiota', r'16s', r'metagenom']
    },
    'NCBITaxon:2157': {  # Archaea
        'keywords': ['archaea', 'archaeal', 'archaebacteria'],
        'patterns': [r'archaea', r'archaeal', r'archaebacteria']
    },
    'NCBITaxon:2759': {  # Eukaryota (general eukaryotes including fungi, protists, algae)
        'keywords': ['eukaryote', 'eukaryotic', 'fungi', 'fungal', 'protozoa', 'protist', 'algae', 'microbe'],
        'patterns': [r'eukaryot', r'fungi', r'fungal', r'protozoa', r'protist', r'algae', r'microbe']
    },
    'NCBITaxon:131567': {  # Cellular organisms (all organisms with cells)
        'keywords': ['organism', 'living', 'life', 'biological diversity', 'multi-organism', 'cross-kingdom'],
        'patterns': [r'organisms?\s+across', r'multi.organism', r'diverse\s+organisms', r'cellular\s+organisms']
    },
}

# Resources known to be organism-specific or multi-organism
RESOURCE_TAXA = {
    '1000genomes': ['NCBITaxon:9606'],  # Human variation
    'bgee': ['NCBITaxon:9606', 'NCBITaxon:10090', 'NCBITaxon:10116', 'NCBITaxon:7227', 'NCBITaxon:6239', 'NCBITaxon:7955', 'NCBITaxon:4932', 'NCBITaxon:3702'],  # Multi-species expression
    'chembl': ['NCBITaxon:9606', 'NCBITaxon:10090'],  # Mostly human and mouse compounds
    'drugbank': ['NCBITaxon:9606'],  # Human-focused drug data
    'ensembl': ['NCBITaxon:9606', 'NCBITaxon:10090', 'NCBITaxon:10116', 'NCBITaxon:7227', 'NCBITaxon:7955'],  # Multi-species genomics
    'flybase': ['NCBITaxon:7227'],  # Drosophila
    'genecards': ['NCBITaxon:9606'],  # Human genes
    'kegg': ['NCBITaxon:9606', 'NCBITaxon:10090', 'NCBITaxon:10116', 'NCBITaxon:7227', 'NCBITaxon:6239', 'NCBITaxon:7955', 'NCBITaxon:4932', 'NCBITaxon:3702'],  # General metabolic pathways
    'omim': ['NCBITaxon:9606'],  # Human genetic diseases
    'pubchem': [],  # Chemical database, no organism specificity
    'reactome': ['NCBITaxon:9606', 'NCBITaxon:10090'],  # Mostly human and mouse pathways
    'uniprot': ['NCBITaxon:9606', 'NCBITaxon:10090', 'NCBITaxon:10116', 'NCBITaxon:7227', 'NCBITaxon:6239', 'NCBITaxon:7955', 'NCBITaxon:4932', 'NCBITaxon:3702'],  # Multi-organism proteins
    'wikipathways': ['NCBITaxon:9606', 'NCBITaxon:10090'],  # Human and mouse pathways
    'mousemine': ['NCBITaxon:10090'],  # Mouse
    'ratmine': ['NCBITaxon:10116'],  # Rat
    'wormbase': ['NCBITaxon:6239'],  # C. elegans
    'zfin': ['NCBITaxon:7955'],  # Zebrafish
    'sgd': ['NCBITaxon:4932'],  # S. cerevisiae
    'pombase': ['NCBITaxon:4896'],  # S. pombe (fission yeast)
    'tair': ['NCBITaxon:3702'],  # Arabidopsis
    'rgd': ['NCBITaxon:10116'],  # Rat Genome Database
    'mgi': ['NCBITaxon:10090'],  # Mouse Genome Informatics
    'dictybase': ['NCBITaxon:44689'],  # Dictyostelium discoideum
    'xenbase': ['NCBITaxon:8355'],  # Xenopus (African clawed frog)
    # Microbiome and microbial resources
    'greengenes': ['NCBITaxon:2', 'NCBITaxon:2157', 'NCBITaxon:2759'],  # Bacteria, Archaea, Eukaryota
    'silva': ['NCBITaxon:2', 'NCBITaxon:2157'],  # 16S rRNA (bacteria and archaea)
    'rdp': ['NCBITaxon:2', 'NCBITaxon:2157'],  # Ribosomal database (bacteria and archaea)
    'mgnify': ['NCBITaxon:131567'],  # Multi-domain metagenomics
    'patric': ['NCBITaxon:2'],  # Bacterial genome resource
    'bacdive': ['NCBITaxon:2'],  # Bacterial culture collection
    'bv-brc': ['NCBITaxon:2', 'NCBITaxon:2157'],  # Bacterial/viral genome resource center
    # Human-focused resources
    'achilles': ['NCBITaxon:9606'],  # Human cancer cell lines
    '4dn': ['NCBITaxon:9606'],  # Human nuclear organization
}

def score_taxa_for_resource(resource_name: str, description: str, domains: List[str], category: str) -> Dict[str, float]:
    """Score each taxon based on how well it matches the resource."""
    scores: Dict[str, float] = {}

    text_to_search = f"{resource_name} {description} {' '.join(domains)} {category}".lower()

    # First check for hardcoded resource names
    for resource_id, taxa in RESOURCE_TAXA.items():
        if resource_id in resource_name.lower():
            for taxon in taxa:
                scores[taxon] = scores.get(taxon, 0) + 10.0

    # Then score based on keywords and patterns
    for taxon, tax_data in TAXON_KEYWORDS.items():
        # Keyword matching (partial match, case-insensitive)
        for keyword in tax_data['keywords']:
            if keyword in text_to_search:
                scores[taxon] = scores.get(taxon, 0) + 2.0

        # Pattern matching (regex)
        for pattern in tax_data['patterns']:
            if re.search(pattern, text_to_search, re.IGNORECASE):
                scores[taxon] = scores.get(taxon, 0) + 3.0

    return scores

def select_taxa(scores: Dict[str, float], threshold: float = 3.0) -> List[str]:
    """Select taxa that score above threshold, sorted by score."""
    selected = [(taxon, score) for taxon, score in scores.items() if score >= threshold]
    selected.sort(key=lambda x: -x[1])  # Sort by score descending
    return [taxon for taxon, _ in selected]

def read_resource_file(file_path: Path) -> Optional[Dict]:
    """Read a resource markdown file and parse YAML frontmatter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    return {
                        'path': file_path,
                        'content': content,
                        'frontmatter': frontmatter if frontmatter else {},
                    }
                except yaml.YAMLError:
                    return None
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return None

def has_taxon(resource: Dict) -> bool:
    """Check if resource already has taxon annotation."""
    return 'taxon' in resource['frontmatter']

def annotate_resource(resource: Dict) -> bool:
    """Add taxon annotation to a resource if it doesn't have one."""
    if has_taxon(resource):
        return False

    frontmatter = resource['frontmatter']
    resource_name = frontmatter.get('id', '').lower()
    description = frontmatter.get('description', '').lower()
    domains = [d.lower() for d in frontmatter.get('domains', [])]
    category = frontmatter.get('category', '').lower()

    # Score and select taxa
    scores = score_taxa_for_resource(resource_name, description, domains, category)
    selected_taxa = select_taxa(scores)

    if selected_taxa:
        resource['frontmatter']['taxon'] = selected_taxa
        return True

    return False

def write_resource_file(resource: Dict) -> bool:
    """Write updated resource back to file."""
    try:
        path = resource['path']
        frontmatter = resource['frontmatter']
        content = resource['content']

        # Rebuild content with updated frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            new_yaml = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
            new_content = f"---\n{new_yaml}---{parts[2]}"

            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"Error writing {resource['path']}: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Automatically annotate resources with NCBITaxon IDs"
    )
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--limit', type=int, default=None, help='Limit number of resources to process')

    args = parser.parse_args()

    # Find all main resource files
    resource_dir = Path('/home/harry/kg-registry/resource')
    resource_files = sorted([
        f for f in resource_dir.rglob('*.md')
        if f.parent.name == f.stem  # Only main resource files, not products
    ])

    if args.limit:
        resource_files = resource_files[:args.limit]

    annotated_count = 0
    skipped_count = 0
    error_count = 0

    print(f"Processing {len(resource_files)} resources...")

    for file_path in resource_files:
        resource = read_resource_file(file_path)
        if not resource:
            error_count += 1
            continue

        if has_taxon(resource):
            skipped_count += 1
            if args.verbose:
                print(f"  SKIP: {file_path.parent.name} (already has taxon)")
            continue

        if annotate_resource(resource):
            frontmatter = resource['frontmatter']
            taxa = frontmatter.get('taxon', [])

            if args.verbose or not args.dry_run:
                print(f"  ADD: {file_path.parent.name} -> {', '.join(taxa)}")

            if not args.dry_run:
                if write_resource_file(resource):
                    annotated_count += 1
                else:
                    error_count += 1
            else:
                annotated_count += 1
        else:
            if args.verbose:
                print(f"  SKIP: {file_path.parent.name} (no matching taxa)")

    print(f"\nResults:")
    print(f"  Annotated: {annotated_count}")
    print(f"  Skipped (already have taxon): {skipped_count}")
    print(f"  Skipped (no matching taxa): {len(resource_files) - annotated_count - skipped_count - error_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total: {len(resource_files)}")

if __name__ == '__main__':
    main()
