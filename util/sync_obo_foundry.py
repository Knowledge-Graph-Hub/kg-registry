#!/usr/bin/env python3
"""
Sync script for OBO Foundry ontologies.

This script fetches the OBO Foundry ontology registry and creates/updates
KG-Registry resources for each ontology, transforming the metadata to fit
our schema structure.
"""

import copy
import sys
import yaml
import requests
import os
import time
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, UTC
import logging

import frontmatter

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class OBOFoundrySync:
    """Synchronize OBO Foundry ontologies with KG-Registry"""

    def __init__(self, registry_root: Optional[str] = None, cache_ttl_hours: int = 24):
        """
        Initialize the sync class

        Args:
            registry_root: Path to registry root directory
            cache_ttl_hours: Cache time-to-live in hours (default: 24)
        """
        if registry_root is None:
            # Default to the registry root directory relative to this script
            script_dir = Path(__file__).parent
            self.registry_root = script_dir.parent / 'resource'
        else:
            self.registry_root = Path(registry_root)

        self.obo_foundry_url = "https://obofoundry.org/registry/ontologies.yml"
        self.existing_resources = self._load_existing_resources()
        self.product_exclusions = self._load_product_exclusions()

        # Cache configuration
        self.cache_ttl_hours = cache_ttl_hours
        self.cache_dir = Path(__file__).parent.parent / 'cache'
        self.cache_file = self.cache_dir / 'obo_foundry_cache.yml'

        # Create cache directory if it doesn't exist
        self.cache_dir.mkdir(parents=True, exist_ok=True)

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

    def _load_product_exclusions(self) -> Dict[str, set]:
        """Load per-ontology product ids that the sync must never (re-)add.

        These are products the OBO Foundry registry advertises but that are not
        actually published (their PURLs 404). See util/obo_sync_exclusions.yaml.
        """
        exclusions: Dict[str, set] = {}
        config_path = Path(__file__).parent / 'obo_sync_exclusions.yaml'
        if not config_path.exists():
            return exclusions
        try:
            with open(config_path, 'r', encoding='utf-8') as handle:
                data = yaml.safe_load(handle) or {}
            for ontology_id, product_ids in (data.get('exclude_products') or {}).items():
                exclusions[str(ontology_id).lower()] = {
                    str(pid) for pid in (product_ids or [])
                }
        except Exception as e:
            logger.warning(f"Failed to load product exclusions: {e}")
        return exclusions

    def _map_obo_domain_to_schema(self, obo_domain: str) -> List[str]:
        """Map OBO Foundry domain to KG-Registry DomainEnum values"""
        domain_mapping = {
            'anatomy and development': ['anatomy and development'],
            'biological systems': ['biological systems'],
            'chemistry and biochemistry': ['chemistry and biochemistry'],
            'diet, metabolomics, and nutrition': ['nutrition'],
            'health': ['biomedical'],
            'information': ['information technology'],
            'information technology': ['information technology'],
            'investigations': ['general'],
            'organisms': ['organisms'],
            'phenotype': ['phenotype'],
            'simulation': ['information technology'],
            'upper': ['general'],
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

    def _normalize_publication_id(self, identifier: Any) -> Optional[str]:
        """Normalize publication identifiers to a schema-compatible `id` value."""
        if isinstance(identifier, int):
            return f"PMID:{identifier}"

        if not isinstance(identifier, str):
            return None

        normalized = identifier.strip()
        if not normalized:
            return None

        lower = normalized.lower()
        if normalized.isdigit():
            return f"PMID:{normalized}"
        if lower.startswith(('http://', 'https://', 'pmid:', 'doi:', 'arxiv:')):
            return normalized
        if lower.startswith('10.'):
            return f"doi:{normalized}"

        return normalized

    def _is_cache_valid(self) -> bool:
        """Check if cache file exists and is within TTL"""
        if not self.cache_file.exists():
            return False

        cache_age_hours = (time.time() - os.path.getmtime(self.cache_file)) / 3600
        is_valid = cache_age_hours < self.cache_ttl_hours

        if is_valid:
            logger.info(
                f"Cache is valid (age: {cache_age_hours:.1f} hours, TTL: {self.cache_ttl_hours} hours)")
        else:
            logger.info(
                f"Cache expired (age: {cache_age_hours:.1f} hours, TTL: {self.cache_ttl_hours} hours)")

        return is_valid

    def _load_from_cache(self) -> Optional[List[Dict[str, Any]]]:
        """Load OBO Foundry data from cache"""
        try:
            with open(self.cache_file, 'r') as f:
                data = yaml.safe_load(f)
                logger.info(f"Loaded {len(data)} ontologies from cache")
                return data
        except Exception as e:
            logger.warning(f"Failed to load cache: {e}")
            return None

    def _save_to_cache(self, data: List[Dict[str, Any]]) -> None:
        """Save OBO Foundry data to cache"""
        try:
            with open(self.cache_file, 'w') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Cached {len(data)} ontologies to {self.cache_file}")
        except Exception as e:
            logger.warning(f"Failed to save cache: {e}")

    def fetch_obo_foundry_data(self) -> List[Dict[str, Any]]:
        """Fetch the OBO Foundry ontologies data (with caching)"""

        # Check if we can use cached data
        if self._is_cache_valid():
            cached_data = self._load_from_cache()
            if cached_data is not None:
                return cached_data

        # Cache miss or invalid - fetch fresh data
        logger.info(f"Fetching fresh OBO Foundry data from {self.obo_foundry_url}")

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
            # Replace non-ASCII with space
            text_content = re.sub(r'[^\x00-\x7F]+', ' ', text_content)

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

            # Save to cache for next time
            self._save_to_cache(data)

            return data

        except Exception as e:
            logger.error(f"Failed to fetch OBO Foundry data: {e}")

            # Try to use expired cache as fallback
            if self.cache_file.exists():
                logger.warning("Attempting to use expired cache as fallback")
                cached_data = self._load_from_cache()
                if cached_data is not None:
                    return cached_data

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

        # Get description - use placeholder if missing
        description = obo_ontology.get('description', '').strip()
        if not description:
            description = "Description unavailable."

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

        # Enhancement 1: Transform contact information to Contact class objects
        contacts = []
        contact_info = obo_ontology.get('contact')
        if contact_info:
            if isinstance(contact_info, dict):
                contact_obj: Dict[str, Any] = {
                    'category': 'Individual'  # Use Individual as default Contact category
                }

                # Add label if available
                if contact_info.get('label'):
                    contact_obj['label'] = contact_info['label']

                # Add ORCID if available
                if contact_info.get('orcid'):
                    contact_obj['orcid'] = contact_info['orcid']

                # Build contact_details list with proper structure
                contact_details: List[Dict[str, str]] = []
                if contact_info.get('email'):
                    contact_details.append({
                        'contact_type': 'email',
                        'value': contact_info['email']
                    })

                if contact_info.get('github'):
                    contact_details.append({
                        'contact_type': 'github',
                        'value': contact_info['github']
                    })

                if contact_details:
                    contact_obj['contact_details'] = contact_details

                contacts.append(contact_obj)
            elif isinstance(contact_info, str):
                # Handle simple string contact
                contact_obj: Dict[str, Any] = {
                    'category': 'Individual'
                }
                if '@' in contact_info:
                    contact_obj['contact_details'] = [{
                        'contact_type': 'email',
                        'value': contact_info
                    }]
                else:
                    contact_obj['label'] = contact_info
                contacts.append(contact_obj)

        # Enhancement 2: Include products as Product objects (per schema)
        products = []
        obo_products = obo_ontology.get('products', [])

        for i, product in enumerate(obo_products):
            if isinstance(product, dict):
                # Generate unique Product ID: [Resource ID].[Product ID suffix]
                product_id_raw = product.get('id', f"product-{i + 1}")

                # If product ID doesn't start with resource ID, prefix it
                if not product_id_raw.startswith(ontology_id):
                    product_id = f"{ontology_id}.{product_id_raw}"
                else:
                    product_id = product_id_raw

                # Sanitize product ID: replace slashes with dots to avoid file system issues
                product_id = product_id.replace('/', '.')

                # Detect format from product ID, URL, or explicit format field
                product_format = product.get('format', '')
                if not product_format:
                    # Try to detect from product ID or URL
                    product_url = product.get('ontology_purl', '')
                    if product_id.endswith('.owl'):
                        product_format = 'owl'
                    elif product_id.endswith('.obo'):
                        product_format = 'obo'
                    elif product_id.endswith('.json'):
                        product_format = 'json'
                    elif 'owl' in product_url.lower():
                        product_format = 'owl'
                    elif 'obo' in product_url.lower():
                        product_format = 'obo'
                    elif 'json' in product_url.lower():
                        product_format = 'json'
                    else:
                        product_format = 'owl'  # Default to OWL

                # Normalize format for KG-Registry consistency
                if product_format == 'owl-rdf/xml':
                    product_format = 'owl'

                # Use OBO Foundry description if available, otherwise create format-based description
                obo_description = product.get('description') or product.get('title')
                if obo_description:
                    product_description = obo_description
                else:
                    # Create format-based description
                    format_name = product_format.upper()
                    product_description = f"{title} in {format_name} format"

                product_obj = {
                    'id': product_id,
                    'name': product.get('title', product_id),
                    'description': product_description,
                    'format': product_format,
                    'category': 'OntologyProduct'  # Set category to OntologyProduct for ontology products
                }

                # Add product URL if available
                if product.get('ontology_purl'):
                    product_obj['product_url'] = product['ontology_purl']

                products.append(product_obj)

        # If no products found but ontology_purl exists, create a default product
        if not products and obo_ontology.get('ontology_purl'):
            # Detect format from URL
            ontology_url = obo_ontology['ontology_purl']
            if 'obo' in ontology_url.lower():
                default_format = 'obo'
                default_id = f"{ontology_id}.obo"
            elif 'json' in ontology_url.lower():
                default_format = 'json'
                default_id = f"{ontology_id}.json"
            else:
                default_format = 'owl'
                default_id = f"{ontology_id}.owl"

            products.append({
                'id': default_id,
                'name': f"{title} ({default_format.upper()})",
                'description': f"{title} in {default_format.upper()} format",
                'product_url': obo_ontology['ontology_purl'],
                'format': default_format,
                'category': 'OntologyProduct'  # Set category to OntologyProduct for ontology products
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
                pub_id = self._normalize_publication_id(pub.get('id'))
                if pub_id:
                    publications.append({
                        'id': pub_id,
                        'title': pub_title,
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
            'category': 'Ontology'  # Set category to Ontology for OBO Foundry ontologies
        }

        # Add tags if available
        if tags:
            kg_resource['tags'] = tags

        # Add taxon information if available
        taxon = obo_ontology.get('taxon')
        if taxon:
            if isinstance(taxon, dict):
                # Single taxon as dict - extract the ID and convert to list
                taxon_id = taxon.get('id', '')
                if taxon_id:
                    kg_resource['taxon'] = [taxon_id]
            elif isinstance(taxon, list):
                # Multiple taxa as list - extract IDs
                taxon_ids = []
                for t in taxon:
                    if isinstance(t, dict):
                        taxon_id = t.get('id', '')
                        if taxon_id:
                            taxon_ids.append(taxon_id)
                    elif isinstance(t, str):
                        # Already a CURIE ID
                        taxon_ids.append(t)
                if taxon_ids:
                    kg_resource['taxon'] = taxon_ids
            elif isinstance(taxon, str):
                # Single taxon as string (CURIE ID)
                kg_resource['taxon'] = [taxon]

        # Clean up None values
        kg_resource = {k: v for k, v in kg_resource.items() if v is not None and v != ''}

        return kg_resource

    def _load_existing_metadata(self, resource_file: Path) -> Dict[str, Any]:
        """Load YAML frontmatter from an existing resource markdown file."""
        if not resource_file.exists():
            return {}

        try:
            text = resource_file.read_text(encoding='utf-8')
            if not text.startswith('---'):
                return {}
            parts = text.split('---', 2)
            if len(parts) < 3:
                return {}
            data = yaml.safe_load(parts[1])
            return data if isinstance(data, dict) else {}
        except Exception as e:
            logger.warning(f"Failed to load existing metadata from {resource_file}: {e}")
            return {}

    def _load_existing_post(self, resource_file: Path) -> Tuple[Dict[str, Any], str]:
        """Load existing metadata and markdown body from a resource file."""
        if not resource_file.exists():
            return {}, ""

        try:
            post = frontmatter.load(resource_file)
            metadata = dict(post.metadata) if isinstance(post.metadata, dict) else {}
            return metadata, post.content
        except Exception as exc:
            logger.warning("Failed to load existing post from %s: %s", resource_file, exc)
            return {}, resource_file.read_text(encoding='utf-8')

    def _today_iso(self) -> str:
        """Return today's date normalized as ISO date-time with Z suffix."""
        return datetime.now(UTC).strftime('%Y-%m-%dT00:00:00Z')

    def _contact_identity(self, contact: Dict[str, Any]) -> Tuple[str, str, str]:
        label = str(contact.get('label', '')).strip().lower()
        email = ""
        github = ""
        for detail in contact.get('contact_details', []) or []:
            if not isinstance(detail, dict):
                continue
            if detail.get('contact_type') == 'email':
                email = str(detail.get('value', '')).strip().lower()
            elif detail.get('contact_type') == 'github':
                github = str(detail.get('value', '')).strip().lower()
        return label, email, github

    def merge_contacts(self, existing_contacts: Any, synced_contacts: Any) -> List[Dict[str, Any]]:
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
        self,
        existing_products: Any,
        synced_products: Any,
        excluded_ids: Optional[set] = None,
    ) -> List[Dict[str, Any]]:
        excluded_ids = excluded_ids or set()

        def _is_excluded(product: Dict[str, Any]) -> bool:
            return isinstance(product.get('id'), str) and product['id'] in excluded_ids

        existing = [
            copy.deepcopy(p)
            for p in existing_products or []
            if isinstance(p, dict) and not _is_excluded(p)
        ]
        synced = [
            copy.deepcopy(p)
            for p in synced_products or []
            if isinstance(p, dict) and not _is_excluded(p)
        ]
        if not existing:
            return synced
        if not synced:
            return existing

        synced_by_id = {
            product.get('id'): product for product in synced if isinstance(product.get('id'), str)
        }
        merged: List[Dict[str, Any]] = []
        seen_ids = set()

        for product in existing:
            product_id = product.get('id')
            if isinstance(product_id, str) and product_id in synced_by_id:
                updated = copy.deepcopy(product)
                updated.update(synced_by_id[product_id])
                merged.append(updated)
                seen_ids.add(product_id)
            else:
                merged.append(product)

        for product in synced:
            product_id = product.get('id')
            if product_id in seen_ids:
                continue
            merged.append(product)

        return merged

    def _publication_identity(self, publication: Dict[str, Any]) -> Tuple[str, str]:
        identifier = self._normalize_publication_id(publication.get('id'))
        if identifier:
            return ('id', identifier)

        title = str(publication.get('title', '')).strip().lower()
        return ('title', title)

    def merge_publications(
        self, existing_publications: Any, synced_publications: Any
    ) -> List[Dict[str, Any]]:
        existing = [copy.deepcopy(p) for p in existing_publications or [] if isinstance(p, dict)]
        synced = [copy.deepcopy(p) for p in synced_publications or [] if isinstance(p, dict)]
        if not existing:
            return synced
        if not synced:
            return existing

        synced_by_identity = {}
        for publication in synced:
            identity = self._publication_identity(publication)
            if identity[1]:
                synced_by_identity[identity] = publication

        merged: List[Dict[str, Any]] = []
        seen = set()

        for publication in existing:
            identity = self._publication_identity(publication)
            if identity[1] and identity in synced_by_identity:
                updated = copy.deepcopy(publication)
                updated.update(synced_by_identity[identity])
                merged.append(updated)
                seen.add(identity)
            else:
                merged.append(publication)
                if identity[1]:
                    seen.add(identity)

        for publication in synced:
            identity = self._publication_identity(publication)
            if identity[1] and identity in seen:
                continue
            merged.append(publication)
            if identity[1]:
                seen.add(identity)

        return merged

    def _merge_unique_lists(self, existing: Any, synced: Any) -> List[Any]:
        merged: List[Any] = []
        for item in (existing or []) + (synced or []):
            if item not in merged:
                merged.append(item)
        return merged

    def merge_resource_metadata(
        self, existing_metadata: Dict[str, Any], synced_metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        if not existing_metadata:
            return copy.deepcopy(synced_metadata)

        merged = copy.deepcopy(existing_metadata)

        for field in [
            'name',
            'description',
            'homepage_url',
            'repository',
            'activity_status',
            'category',
            'layout',
            'license',
        ]:
            if synced_metadata.get(field):
                merged[field] = copy.deepcopy(synced_metadata[field])

        for field in ['domains', 'tags', 'taxon', 'collection']:
            merged_values = self._merge_unique_lists(
                existing_metadata.get(field), synced_metadata.get(field)
            )
            if merged_values:
                merged[field] = merged_values

        merged['contacts'] = self.merge_contacts(
            existing_metadata.get('contacts'), synced_metadata.get('contacts')
        )
        ontology_id = str(
            existing_metadata.get('id') or synced_metadata.get('id') or ''
        ).lower()
        merged['products'] = self.merge_products(
            existing_metadata.get('products'),
            synced_metadata.get('products'),
            excluded_ids=self.product_exclusions.get(ontology_id, set()),
        )
        merged['publications'] = self.merge_publications(
            existing_metadata.get('publications'), synced_metadata.get('publications')
        )

        return merged

    def _metadata_for_compare(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        comparable = copy.deepcopy(metadata)
        comparable.pop('last_modified_date', None)
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
        """Create default markdown body for newly synchronized resources."""
        body = f"""## Description

{resource_data['description']}

"""

        if resource_data.get('contacts'):
            body += "## Contacts\n\n"
            for contact in resource_data['contacts']:
                contact_line = []
                if contact.get('label'):
                    contact_line.append(contact['label'])

                if contact.get('contact_details'):
                    contact_details = contact['contact_details']
                    if isinstance(contact_details, list):
                        email_detail = next(
                            (cd for cd in contact_details if cd.get('contact_type') == 'email'), None
                        )
                        if email_detail:
                            contact_line.append(f"({email_detail['value']})")
                    else:
                        contact_line.append(f"({contact_details})")

                if contact.get('orcid'):
                    contact_line.append(
                        f"[ORCID: {contact['orcid']}](https://orcid.org/{contact['orcid']})"
                    )

                if contact_line:
                    body += f"- {' '.join(contact_line)}\n"
                else:
                    body += f"- Contact (category: {contact.get('category', 'Unknown')})\n"
            body += "\n"

        if resource_data.get('products'):
            body += "## Products\n\n"
            for product in resource_data['products']:
                body += f"### {product['name']}\n\n"
                if product.get('description'):
                    body += f"{product['description']}\n\n"
                if product.get('product_url'):
                    body += f"**URL**: [{product['product_url']}]({product['product_url']})\n\n"
                if product.get('format'):
                    body += f"**Format**: {product['format']}\n\n"

        if resource_data.get('publications'):
            body += "## Publications\n\n"
            for pub in resource_data['publications']:
                title = pub.get('title', 'Untitled')
                identifier = pub.get('id') or pub.get('url') or ''
                if identifier:
                    body += f"- [{title}]({identifier})\n"
                else:
                    body += f"- {title}\n"
            body += "\n"

        if resource_data.get('domains'):
            domains_str = ', '.join(resource_data['domains'])
            body += f"**Domains**: {domains_str}\n\n"

        if resource_data.get('tags'):
            tags_str = ', '.join(resource_data['tags'])
            body += f"**Tags**: {tags_str}\n\n"

        if resource_data.get('taxon'):
            taxon = resource_data['taxon']
            if isinstance(taxon, list):
                body += f"**Taxon**: {', '.join(taxon)}\n\n"
            elif isinstance(taxon, dict):
                body += f"**Taxon**: {taxon.get('label', '')} ({taxon.get('id', '')})\n\n"

        body += "---\n\n*This resource was automatically synchronized from the OBO Foundry registry.*"
        return body

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

        # Keep date fields in frontmatter when present
        if resource_data.get('creation_date'):
            frontmatter['creation_date'] = resource_data['creation_date']
        if resource_data.get('last_modified_date'):
            frontmatter['last_modified_date'] = resource_data['last_modified_date']

        # Add optional fields including enhanced Contact and Product objects
        for field in ['domains', 'tags', 'taxon', 'contacts', 'products']:
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

        # Add contacts section (enhanced Contact objects)
        if resource_data.get('contacts'):
            markdown_content += "## Contacts\n\n"
            for contact in resource_data['contacts']:
                contact_line = []
                if contact.get('label'):
                    contact_line.append(contact['label'])

                # Handle contact_details list structure
                if contact.get('contact_details'):
                    contact_details = contact['contact_details']
                    if isinstance(contact_details, list):
                        # Find email for primary contact info
                        email_detail = next(
                            (cd for cd in contact_details if cd.get('contact_type') == 'email'), None)
                        if email_detail:
                            contact_line.append(f"({email_detail['value']})")
                    else:
                        # Fallback for simple string contact_details
                        contact_line.append(f"({contact_details})")

                if contact.get('orcid'):
                    contact_line.append(
                        f"[ORCID: {contact['orcid']}](https://orcid.org/{contact['orcid']})")

                if contact_line:
                    markdown_content += f"- {' '.join(contact_line)}\n"
                else:
                    markdown_content += f"- Contact (category: {contact.get('category', 'Unknown')})\n"
            markdown_content += "\n"

        # Add products section (enhanced Product objects)
        if resource_data.get('products'):
            markdown_content += "## Products\n\n"
            for product in resource_data['products']:
                markdown_content += f"### {product['name']}\n\n"
                if product.get('description'):
                    markdown_content += f"{product['description']}\n\n"
                if product.get('product_url'):
                    markdown_content += f"**URL**: [{product['product_url']}]({product['product_url']})\n\n"
                if product.get('format'):
                    markdown_content += f"**Format**: {product['format']}\n\n"

        # Add publications section
        if resource_data.get('publications'):
            markdown_content += "## Publications\n\n"
            for pub in resource_data['publications']:
                title = pub.get('title', 'Untitled')
                identifier = pub.get('id') or pub.get('url') or ''
                if identifier:
                    markdown_content += f"- [{title}]({identifier})\n"
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
            if isinstance(taxon, list):
                taxon_str = ', '.join(taxon)
                markdown_content += f"**Taxon**: {taxon_str}\n\n"
            elif isinstance(taxon, dict):
                # Legacy format - convert for display
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

            resource_file = resource_dir / f"{ontology_id}.md"

            is_new = ontology_id not in self.existing_resources
            existing_metadata, existing_content = self._load_existing_post(resource_file)
            merged_metadata = self.merge_resource_metadata(existing_metadata, kg_resource)

            today_iso = self._today_iso()
            if existing_metadata.get('creation_date'):
                merged_metadata['creation_date'] = existing_metadata['creation_date']
            else:
                merged_metadata['creation_date'] = today_iso

            content = existing_content if self._content_for_compare(existing_content) else self._default_content(
                kg_resource
            )

            has_changed = is_new or (
                self._metadata_for_compare(existing_metadata)
                != self._metadata_for_compare(merged_metadata)
                or self._content_for_compare(existing_content) != self._content_for_compare(content)
            )

            if not has_changed:
                logger.info("No OBO Foundry changes detected for %s", ontology_id)
                return True

            merged_metadata['last_modified_date'] = today_iso
            resource_file.write_text(
                self._serialize_resource(merged_metadata, content),
                encoding='utf-8',
            )

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

                # Enhancement 4: Include inactive/obsolete ontologies (don't skip them)
                activity_status = ontology.get('activity_status', 'active')
                is_obsolete = ontology.get('is_obsolete', False)

                # Log status but continue processing all ontologies
                if activity_status in ['inactive', 'obsolete', 'orphaned'] or is_obsolete:
                    logger.info(
                        f"Processing {ontology_id} with status={activity_status}, obsolete={is_obsolete}")
                else:
                    logger.info(f"Processing active ontology: {ontology_id}")

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
    parser.add_argument('--no-cache', action='store_true',
                        help='Disable cache and fetch fresh data')
    parser.add_argument('--cache-ttl', type=int, default=24,
                        help='Cache time-to-live in hours (default: 24)')

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Set cache TTL to 0 if --no-cache is specified (forces fresh fetch)
        cache_ttl = 0 if args.no_cache else args.cache_ttl

        syncer = OBOFoundrySync(registry_root=args.registry_root, cache_ttl_hours=cache_ttl)
        stats = syncer.sync_all(dry_run=args.dry_run, limit=args.limit)

        print(f"\nSync Summary:")
        print(f"  Processed: {stats['processed']}")
        print(f"  Created: {stats['created']}")
        print(f"  Updated: {stats['updated']}")
        print(f"  Failed: {stats['failed']}")
        print(f"  Skipped: {stats['skipped']}")

        # Only exit with error if sync completely failed or no ontologies were processed
        # Failed individual ontologies (usually due to missing descriptions) are expected
        if stats['processed'] == 0 or (stats['created'] == 0 and stats['updated'] == 0 and stats['failed'] == stats['processed']):
            sys.exit(1)

    except Exception as e:
        logger.error(f"Sync failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
