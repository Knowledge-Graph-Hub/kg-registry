#!/usr/bin/env python3
"""
Generate automated evaluations for all KnowledgeGraph resources without evaluations.
Uses web scraping to analyze homepages, repositories, and available documentation.
"""

import sys
import json
import datetime
from pathlib import Path
from urllib.parse import urlparse
import urllib.request
import urllib.error

# Setup paths
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

import yaml

def get_page_content(url):
    """Fetch page content with timeout and error handling"""
    if not url or url == 'N/A':
        return None
    
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; KG-Registry Evaluator)'},
            timeout=5
        )
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8', errors='ignore')
    except (urllib.error.URLError, urllib.error.HTTPError, Exception):
        return None

def evaluate_resource(resource):
    """Generate evaluation data for a resource based on available metadata"""
    rid = resource.get('id', '')
    name = resource.get('name', rid)
    homepage = resource.get('homepage_url', '')
    repo = resource.get('repository', '')
    description = resource.get('description', '')
    contacts = resource.get('contacts', [])
    products = resource.get('products', [])
    
    # Fetch homepage to check for documentation
    homepage_content = get_page_content(homepage) if homepage else None
    repo_content = get_page_content(repo) if repo else None
    
    # Evaluate Access Level and Types
    access_other = 'Y' if homepage or products else 'N'
    api_access = 'Y' if any(p.get('format') in ['json', 'api', 'http'] for p in products) else 'N'
    multi_access = 'Y' if len(products) > 1 else 'N'
    source_code = 'Y' if repo else 'N'
    downloadable = 'Y' if any(p.get('category') in ['DownloadableProduct', 'Product'] for p in products) else 'N'
    
    # Evaluate Provenance
    source_list = 'Y' if 'source' in description.lower() or any('source' in str(p).lower() for p in products) else 'N'
    source_versions = 'Y' if 'version' in description.lower() else 'N'
    import_deps = 'Y' if any(p.get('original_source') for p in products) else 'N'
    node_edge_sources = 'Y' if import_deps == 'Y' else 'N'
    edges_dedup = 'Y' if 'dedupl' in description.lower() else 'N'
    triples_source = 'Y' if any(p.get('format') in ['owl', 'rdf', 'ttl'] for p in products) else 'N'
    edge_schema = 'Y' if any(p.get('format') in ['owl', 'rdf', 'ttl', 'json'] for p in products) else 'N'
    
    # Evaluate Documentation
    bio_usable = 'Y' if description else 'N'
    resolvable_ids = 'Y' if repo else 'N'
    construction_docs = 'Y' if homepage_content and ('construct' in homepage_content.lower() or 'build' in homepage_content.lower()) else 'N'
    transform_docs = 'Y' if homepage_content and ('transform' in homepage_content.lower() or 'process' in homepage_content.lower()) else 'N'
    schema_used = 'Y' if any(p.get('format') in ['owl', 'json-ld'] for p in products) else 'N'
    
    # Evaluate Updates and Versioning
    stable_versions = 'Y' if repo else 'N'
    public_tracker = 'Y' if repo and 'github' in repo.lower() else 'N'
    kg_contact = 'Y' if contacts else 'N'
    updated_annually = 'Y' if repo else 'N'
    prior_versions = 'Y' if repo else 'N'
    
    # Evaluate Fitness for Purpose
    use_case = 'Y' if description else 'N'
    eval_others = 'N'  # Typically not available
    defined_scope = 'Y' if description else 'N'
    multi_eval_methods = 'N'  # Typically not available
    accuracy_metrics = 'N'  # Typically not available
    
    return {
        'access_other': access_other,
        'api_access': api_access,
        'multi_access': multi_access,
        'source_code': source_code,
        'downloadable': downloadable,
        'source_list': source_list,
        'source_versions': source_versions,
        'import_deps': import_deps,
        'node_edge_sources': node_edge_sources,
        'edges_dedup': edges_dedup,
        'triples_source': triples_source,
        'edge_schema': edge_schema,
        'bio_usable': bio_usable,
        'resolvable_ids': resolvable_ids,
        'construction_docs': construction_docs,
        'transform_docs': transform_docs,
        'schema_used': schema_used,
        'stable_versions': stable_versions,
        'public_tracker': public_tracker,
        'kg_contact': kg_contact,
        'updated_annually': updated_annually,
        'prior_versions': prior_versions,
        'use_case': use_case,
        'eval_others': eval_others,
        'defined_scope': defined_scope,
        'multi_eval_methods': multi_eval_methods,
        'accuracy_metrics': accuracy_metrics,
    }

def create_tsv_row(resource, evals):
    """Create a TSV row for the evaluation"""
    rid = resource.get('id', '')
    
    # Map evaluation keys to TSV columns
    fields = [
        rid,
        # Access Level and Types
        '',  # access_otherthanKG_text
        evals['access_other'],
        '',  # api_or_online_access_text
        evals['api_access'],
        '',  # multi_access_options_text
        evals['multi_access'],
        '',  # sourcecode_available_text
        evals['source_code'],
        '',  # downloadable_KG_text
        evals['downloadable'],
        # Provenance of Nodes and Edges
        '',  # source_list_provided_text
        evals['source_list'],
        '',  # source_versions_info_text
        evals['source_versions'],
        '',  # import_dependancies_text
        evals['import_deps'],
        '',  # node_edge_sources_text
        evals['node_edge_sources'],
        '',  # edges_deduplication_text
        evals['edges_dedup'],
        '',  # triples_source_details_text
        evals['triples_source'],
        '',  # edge_type_schema_text
        evals['edge_schema'],
        # Documented standards, schema, construction
        '',  # bio_usable_data_text
        evals['bio_usable'],
        '',  # resolvable_ids_text
        evals['resolvable_ids'],
        '',  # construction_docs_text
        evals['construction_docs'],
        '',  # transform_docs_text
        evals['transform_docs'],
        '',  # schema_used_text
        evals['schema_used'],
        # Update frequency and versioning
        '',  # stable_versions_text
        evals['stable_versions'],
        '',  # public_tracker_text
        evals['public_tracker'],
        '',  # kg_contact_info_text
        evals['kg_contact'],
        '',  # updated_annually_text
        evals['updated_annually'],
        '',  # prior_versions_access_text
        evals['prior_versions'],
        # Evaluation - Metrics and Fitness for Purpose
        '',  # use_case_provided_text
        evals['use_case'],
        '',  # eval_against_others_text
        evals['eval_others'],
        '',  # defined_scope_text
        evals['defined_scope'],
        '',  # multi_eval_methods_text
        evals['multi_eval_methods'],
        '',  # accuracy_metrics_text
        evals['accuracy_metrics'],
        # License Information
        '',  # License_text
    ]
    
    return '\t'.join(fields)

def main():
    # Load registry
    with open(ROOT / 'registry' / 'kgs.yml', 'r') as f:
        registry = yaml.safe_load(f)
    
    # Find KG resources without evaluations
    kgs_to_evaluate = []
    for resource in registry.get('resources', []):
        if resource.get('category') != 'KnowledgeGraph':
            continue
        
        rid = resource.get('id')
        if not rid:
            continue
        
        # Check for evaluations
        manual_eval = (ROOT / 'resource' / rid / f'{rid}_eval.md').exists()
        auto_eval = (ROOT / 'resource' / rid / f'{rid}_eval_automated.md').exists()
        
        if not (manual_eval or auto_eval):
            kgs_to_evaluate.append(resource)
    
    print(f"Evaluating {len(kgs_to_evaluate)} KnowledgeGraph resources...")
    
    # Generate evaluations and build TSV
    tsv_lines = []
    
    for i, resource in enumerate(kgs_to_evaluate, 1):
        rid = resource.get('id')
        print(f"[{i}/{len(kgs_to_evaluate)}] Evaluating {rid}...", end=' ', flush=True)
        
        try:
            evals = evaluate_resource(resource)
            row = create_tsv_row(resource, evals)
            tsv_lines.append(row)
            print("✓")
        except Exception as e:
            print(f"✗ ({e})")
    
    # Write to TSV file
    if tsv_lines:
        eval_tsv = ROOT / 'evals' / 'evals_automated.tsv'
        
        # Read existing file to get header
        with open(eval_tsv, 'r') as f:
            lines = f.readlines()
        
        # Append new rows
        new_lines = lines[:-1]  # Remove empty line at end if exists
        new_lines.extend([line + '\n' if not line.endswith('\n') else line for line in tsv_lines])
        new_lines.append('\n')  # Add final newline
        
        # Write back
        with open(eval_tsv, 'w') as f:
            f.writelines(new_lines)
        
        print(f"\n✓ Added {len(tsv_lines)} evaluation rows to evals_automated.tsv")
    else:
        print("\nNo evaluations generated")

if __name__ == '__main__':
    main()
