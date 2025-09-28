#!/usr/bin/env python3
"""
Sync script for OBO Foundry ontologies.

This script fetches the OBO Foundry ontology registry and creates/updates
KG-Registry resources for each ontology, transforming the metadata to fit
our schema structure.
"""

import os
import sys
import yaml
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import re

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OBOFoundrySync:
    """Synchronize OBO Foundry ontologies with KG-Registry"""
    
    def __init__(self, registry_root: Optional[str] = None):
        """Initialize the sync class"""
        if registry_root is None:
            # Default to the registry root directory relative to this script
            script_dir = Path(__file__).parent
            self.registry_root = script_dir.parent / 'resource'
        else:
            self.registry_root = Path(registry_root)
        
        self.obo_foundry_url = "https://obofoundry.org/registry/ontologies.yml"
        self.existing_resources = self._load_existing_resources()
        
    def _load_existing_resources(self) -> Dict[str, Path]:
        """Load existing resources to check for updates"""
        resources = {}
        if self.registry_root.exists():
            for resource_dir in self.registry_root.iterdir():
                if resource_dir.is_dir():
                    resource_file = resource_dir / f"{resource_dir.name}.md"
                    if resource_file.exists():
                        resources[resource_dir.name] = resource_file
        return resources
    
    def _map_obo_domain_to_schema(self, obo_domain: str) -> List[str]:
        """Map OBO Foundry domain to KG-Registry DomainEnum values"""
        domain_mapping = {
            'anatomy and development': ['anatomy and development'],
            'biological systems': ['biological systems'],
            'chemistry and biochemistry': ['chemistry and biochemistry'],
            'diet, metabolomics, and nutrition': ['chemistry and biochemistry'],
            'health': ['biomedical'],
            'information': ['biomedical'],
            'information technology': ['biomedical'],
            'investigations': ['biomedical'],
            'organisms': ['biological systems'],
            'phenotype': ['biological systems'],
            'simulation': ['biological systems'],
            'upper': ['biological systems'],
            'environment': ['environment'],
            'agriculture': ['agriculture']
        }
        
        if obo_domain in domain_mapping:
            return domain_mapping[obo_domain]
        elif obo_domain:
            # Default to biological systems for unrecognized domains
            logger.warning(f"Unknown OBO domain '{obo_domain}', defaulting to 'biological systems'")
            return ['biological systems']
        else:
            # Default for missing domain
            return ['biological systems']
    
    def _filter_valid_tags(self, obo_tags: List[str]) -> List[str]:
        """Filter OBO tags to only include valid TagEnum values"""
        valid_tags = {'biopragmatics', 'core', 'translator'}
        filtered_tags = []
        
        for tag in obo_tags:
            if tag in valid_tags:
                filtered_tags.append(tag)
            else:
                logger.debug(f"Skipping invalid tag: {tag}")
        
        return filtered_tags
        
    def fetch_obo_foundry_data(self) -> List[Dict[str, Any]]:
        """Fetch the OBO Foundry ontologies data"""
        logger.info(f"Fetching OBO Foundry data from {self.obo_foundry_url}")
        
        try:
            response = requests.get(self.obo_foundry_url, timeout=30)
            response.raise_for_status()
            
            # Get raw bytes and handle encoding carefully
            content_bytes = response.content
            
            # Try to decode as UTF-8, replacing problematic characters
            try:
                text_content = content_bytes.decode('utf-8')
            except UnicodeDecodeError:
                text_content = content_bytes.decode('utf-8', errors='replace')
            
            # Clean up problematic characters that might cause YAML issues
            import re
            # Remove or replace problematic Unicode characters
            text_content = re.sub(r'[^\x00-\x7F]+', ' ', text_content)  # Replace non-ASCII with space
            
            # Parse YAML data - the OBO registry is a list of ontologies
            data = yaml.safe_load(text_content)
            
            if not isinstance(data, list):
                # Check if it's a dict with ontologies as values
                if isinstance(data, dict):
                    # Try to find ontologies in the data structure
                    if 'ontologies' in data:
                        data = data['ontologies']
                    else:
                        # Assume the values are the ontologies
                        data = list(data.values())
                else:
                    raise ValueError(f"Expected a list of ontologies or dict, got {type(data)}")
                
            logger.info(f"Successfully fetched {len(data)} ontologies from OBO Foundry")
            return data
            
        except Exception as e:
            logger.error(f"Failed to fetch OBO Foundry data: {e}")
            raise
    
    def transform_obo_to_kg_registry(self, obo_ontology: Dict[str, Any]) -> Dict[str, Any]:
        """Transform OBO Foundry ontology metadata to KG-Registry format"""
        
        # Extract basic information
        ontology_id = obo_ontology.get('id', '').lower()
        title = obo_ontology.get('title', ontology_id.upper())
        
        # Map activity status
        activity_status = obo_ontology.get('activity_status', 'active')
        if activity_status not in ['active', 'inactive', 'orphaned']:
            activity_status = 'active'
        
        # Get description
        description = obo_ontology.get('description', '')
        
        # Get homepage - try multiple fields
        homepage_url = (obo_ontology.get('homepage') or 
                       obo_ontology.get('page') or 
                       obo_ontology.get('ontology_purl'))
        
        # Get repository
        repository = obo_ontology.get('repository')
        
        # Get license information - format as License object
        license_info = obo_ontology.get('license', {})
        if isinstance(license_info, dict):
            license_obj = {
                'id': license_info.get('url', ''),
                'label': license_info.get('label', 'Not specified')
            }
            if license_info.get('logo'):
                license_obj['logo'] = license_info['logo']
        else:
            license_obj = {
                'id': '',
                'label': str(license_info) if license_info else 'Not specified'
            }
        
        # Extract contact information
        contacts = []
        contact_info = obo_ontology.get('contact')
        if contact_info:
            if isinstance(contact_info, dict):
                contact_details = []
                if contact_info.get('email'):
                    contact_details.append(f"Email: {contact_info['email']}")
                if contact_info.get('github'):
                    contact_details.append(f"GitHub: {contact_info['github']}")
                if contact_info.get('orcid'):
                    contact_details.append(f"ORCID: {contact_info['orcid']}")
                
                contacts.append({
                    'category': 'contact',
                    'contact_details': '; '.join(contact_details)
                })
        
        # Extract products/releases
        products = []
        obo_products = obo_ontology.get('products', [])
        
        for product in obo_products:
            if isinstance(product, dict):
                product_name = product.get('id', product.get('title', 'Unknown'))
                product_url = product.get('ontology_purl')
                product_description = product.get('description', product.get('title', ''))
                product_format = product.get('format', 'owl')
                
                if product_url:
                    products.append({
                        'name': product_name,
                        'description': product_description,
                        'url': product_url,
                        'format': product_format
                    })
        
        # If no products found but ontology_purl exists, create a default product
        if not products and obo_ontology.get('ontology_purl'):
            products.append({
                'name': f"{ontology_id}.owl",
                'description': f"Primary OWL file for {title}",
                'url': obo_ontology['ontology_purl'],
                'format': 'owl'
            })
        
        # Get domain/categories and map to valid DomainEnum values
        obo_domain = obo_ontology.get('domain', '')
        domains = self._map_obo_domain_to_schema(obo_domain)
        obo_tags = obo_ontology.get('tags', [])
        tags = self._filter_valid_tags(obo_tags)
        
        # Extract publications
        publications = []
        obo_publications = obo_ontology.get('publications', [])
        
        for pub in obo_publications:
            if isinstance(pub, dict):
                pub_title = pub.get('title', 'Untitled')
                pub_id = pub.get('id', '')
                if pub_id:
                    publications.append({
                        'title': pub_title,
                        'url': pub_id if pub_id.startswith('http') else f"https://www.ncbi.nlm.nih.gov/pubmed/{pub_id}"
                    })
        
        # Build the KG-Registry resource structure
        kg_resource = {
            'id': ontology_id,
            'name': title,
            'description': description,
            'activity_status': activity_status,
            'homepage_url': homepage_url,
            'repository': repository,
            'license': license_obj,
            'domains': domains,  # Use 'domains' (plural) as per schema
            'contacts': contacts,
            'products': products,
            'publications': publications,
            'collection': ['obo-foundry'],  # Add to OBO Foundry collection
            'layout': 'resource_detail',
            'category': 'Resource'
        }
        
        # Add tags if available
        if tags:
            kg_resource['tags'] = tags
        
        # Add taxon information if available
        taxon = obo_ontology.get('taxon')
        if taxon and isinstance(taxon, dict):
            kg_resource['taxon'] = {
                'id': taxon.get('id', ''),
                'label': taxon.get('label', '')
            }
        
        # Clean up None values
        kg_resource = {k: v for k, v in kg_resource.items() if v is not None and v != ''}
        
        return kg_resource
    
    def create_resource_markdown(self, resource_data: Dict[str, Any]) -> str:
        """Create markdown content for a resource"""
        
        # YAML frontmatter
        frontmatter = {
            'id': resource_data['id'],
            'name': resource_data['name'],
            'description': resource_data['description'],
            'activity_status': resource_data['activity_status'],
            'homepage_url': resource_data.get('homepage_url'),
            'repository': resource_data.get('repository'),
            'license': resource_data['license'],
            'collection': resource_data['collection'],
            'layout': resource_data['layout'],
            'category': resource_data['category']
        }
        
        # Add optional fields
        for field in ['domains', 'tags', 'taxon']:
            if field in resource_data:
                frontmatter[field] = resource_data[field]
        
        # Clean up None values in frontmatter
        frontmatter = {k: v for k, v in frontmatter.items() if v is not None}
        
        # Convert to YAML string
        yaml_content = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
        
        # Markdown content
        markdown_content = f"""---
{yaml_content}---

## Description

{resource_data['description']}

"""
        
        # Add contacts section
        if resource_data.get('contacts'):
            markdown_content += "## Contacts\n\n"
            for contact in resource_data['contacts']:
                markdown_content += f"- {contact['contact_details']}\n"
            markdown_content += "\n"
        
        # Add products section
        if resource_data.get('products'):
            markdown_content += "## Products\n\n"
            for product in resource_data['products']:
                markdown_content += f"### {product['name']}\n\n"
                if product.get('description'):
                    markdown_content += f"{product['description']}\n\n"
                if product.get('url'):
                    markdown_content += f"**URL**: [{product['url']}]({product['url']})\n\n"
                if product.get('format'):
                    markdown_content += f"**Format**: {product['format']}\n\n"
        
        # Add publications section
        if resource_data.get('publications'):
            markdown_content += "## Publications\n\n"
            for pub in resource_data['publications']:
                title = pub.get('title', 'Untitled')
                url = pub.get('url', '')
                if url:
                    markdown_content += f"- [{title}]({url})\n"
                else:
                    markdown_content += f"- {title}\n"
            markdown_content += "\n"
        
        # Add additional information
        if resource_data.get('domains'):
            domains_str = ', '.join(resource_data['domains'])
            markdown_content += f"**Domains**: {domains_str}\n\n"
        
        if resource_data.get('tags'):
            tags_str = ', '.join(resource_data['tags'])
            markdown_content += f"**Tags**: {tags_str}\n\n"
        
        if resource_data.get('taxon'):
            taxon = resource_data['taxon']
            markdown_content += f"**Taxon**: {taxon.get('label', '')} ({taxon.get('id', '')})\n\n"
        
        markdown_content += "---\n\n*This resource was automatically synchronized from the OBO Foundry registry.*\n"
        
        return markdown_content
    
    def sync_ontology(self, obo_ontology: Dict[str, Any]) -> bool:
        """Sync a single ontology to KG-Registry format"""
        
        ontology_id = obo_ontology.get('id', '').lower()
        if not ontology_id:
            logger.warning("Skipping ontology without ID")
            return False
        
        logger.info(f"Processing ontology: {ontology_id}")
        
        try:
            # Transform to KG-Registry format
            kg_resource = self.transform_obo_to_kg_registry(obo_ontology)
            
            # Create resource directory
            resource_dir = self.registry_root / ontology_id
            resource_dir.mkdir(parents=True, exist_ok=True)
            
            # Create markdown file
            markdown_content = self.create_resource_markdown(kg_resource)
            resource_file = resource_dir / f"{ontology_id}.md"
            
            # Check if this is an update or new resource
            is_new = ontology_id not in self.existing_resources
            
            # Write the file
            with open(resource_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            if is_new:
                logger.info(f"Created new resource: {ontology_id}")
            else:
                logger.info(f"Updated existing resource: {ontology_id}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to sync ontology {ontology_id}: {e}")
            return False
    
    def sync_all(self, dry_run: bool = False, limit: Optional[int] = None) -> Dict[str, int]:
        """Sync all OBO Foundry ontologies"""
        
        logger.info("Starting OBO Foundry sync")
        
        stats = {
            'processed': 0,
            'created': 0,
            'updated': 0,
            'failed': 0,
            'skipped': 0
        }
        
        try:
            # Fetch OBO Foundry data
            ontologies = self.fetch_obo_foundry_data()
            
            # Limit ontologies if specified
            if limit:
                ontologies = ontologies[:limit]
            
            for ontology in ontologies:
                ontology_id = ontology.get('id', '').lower()
                
                # Skip inactive or obsolete ontologies
                activity_status = ontology.get('activity_status', 'active')
                is_obsolete = ontology.get('is_obsolete', False)
                
                if activity_status in ['inactive', 'orphaned'] or is_obsolete:
                    logger.info(f"Skipping {ontology_id}: status={activity_status}, obsolete={is_obsolete}")
                    stats['skipped'] += 1
                    continue
                
                stats['processed'] += 1
                
                if dry_run:
                    logger.info(f"[DRY RUN] Would sync ontology: {ontology_id}")
                    continue
                
                # Check if this is new or existing
                is_new = ontology_id not in self.existing_resources
                
                if self.sync_ontology(ontology):
                    if is_new:
                        stats['created'] += 1
                    else:
                        stats['updated'] += 1
                else:
                    stats['failed'] += 1
            
            logger.info(f"Sync completed. Stats: {stats}")
            return stats
            
        except Exception as e:
            logger.error(f"Sync failed: {e}")
            raise

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Sync OBO Foundry ontologies to KG-Registry')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without making changes')
    parser.add_argument('--registry-root', type=str,
                       help='Path to registry root directory (default: ../resource)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--limit', type=int,
                       help='Limit number of ontologies to process (for testing)')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        syncer = OBOFoundrySync(registry_root=args.registry_root)
        stats = syncer.sync_all(dry_run=args.dry_run, limit=args.limit)
        
        print(f"\nSync Summary:")
        print(f"  Processed: {stats['processed']}")
        print(f"  Created: {stats['created']}")
        print(f"  Updated: {stats['updated']}")
        print(f"  Failed: {stats['failed']}")
        print(f"  Skipped: {stats['skipped']}")
        
        if stats['failed'] > 0:
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Sync failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()