---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.itis.gov/
  - contact_type: email
    value: itiswebmaster@itis.gov
  label: Integrated Taxonomic Information System (ITIS)
creation_date: '2025-09-03T00:00:00Z'
description: The Integrated Taxonomic Information System (ITIS) provides authoritative
  taxonomic information on plants, animals, fungi, and microbes of North America and
  the world. ITIS compiles standardized scientific names, common names, taxonomic
  serial numbers (TSNs), hierarchical classification, and associated metadata curated
  through interagency and international collaboration to support biodiversity data
  integration, ecological research, regulatory processes, and interoperability across
  biological information systems.
domains:
- organisms
- environment
homepage_url: https://www.itis.gov/
id: itis
last_modified_date: '2025-09-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.itis.gov/access.html
  label: Public Domain
name: ITIS
products:
- category: GraphicalInterface
  description: Web portal for browsing taxonomic records, hierarchical classification,
    name sources, and reports
  format: http
  id: itis.portal
  name: ITIS Web Portal
  original_source:
  - itis
  product_url: https://www.itis.gov/
- category: ProgrammingInterface
  description: REST JSON services providing programmatic access to taxonomic records,
    synonyms, hierarchy, and search utilities
  id: itis.api
  is_public: true
  name: ITIS REST Services
  original_source:
  - itis
  product_url: https://www.itis.gov/ws_description.html
- category: Product
  description: Downloadable full database dump (Delorme) package containing authoritative
    ITIS taxonomic data
  id: itis.download
  name: ITIS Data Download Package
  original_source:
  - itis
  product_url: https://www.itis.gov/downloads/
- category: Product
  description: itis OBO
  format: obo
  id: obo-db-ingest.itis.obo
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: itis OBO
  original_source:
  - itis
  product_file_size: 10936424
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  compression: gzip
  description: ITIS OWL
  format: owl
  id: obo-db-ingest.itis.owl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: ITIS OWL
  original_source:
  - itis
  product_file_size: 14607611
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.owl.gz
  secondary_source:
  - obo-db-ingest
- category: Product
  compression: gzip
  description: ITIS OBO Graph JSON
  format: json
  id: obo-db-ingest.itis.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: ITIS OBO Graph JSON
  original_source:
  - itis
  product_file_size: 12669423
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.json.gz
  secondary_source:
  - obo-db-ingest
---
## Overview

The Integrated Taxonomic Information System (ITIS) is a partnership of U.S., Canadian, and Mexican agencies, and other organizations, producing a curated reference of global taxonomic information. Each taxon is assigned a persistent Taxonomic Serial Number (TSN) that facilitates integration and reconciliation across biodiversity, ecological, and regulatory datasets.

## Data Scope

- Scientific and common names with synonymy and name usage
- Hierarchical classification spanning kingdoms to species (and infraspecific ranks)
- Authorship, publication, and nomenclatural references
- Geographic data indicators and taxonomic status flags
- Cross-references to other authoritative nomenclature sources where available

## Access & Services

Programmatic access is provided via publicly available REST services returning JSON for record lookup, hierarchy traversal, and search queries. Bulk database downloads support offline integration and local analytics. OBO, OWL, and OBO Graph JSON exports are available via the OBO DB ingest transformation for ontology/graph workflows.

## Licensing & Use

ITIS data are in the public domain. Users may copy and use the data freely with appropriate attribution recommended (e.g., citing ITIS and access date). See the access and data use policy page for details.

## Citation

Integrated Taxonomic Information System (ITIS). www.itis.gov (Accessed YYYY-MM-DD).

## Contact

General inquiries or technical questions: itiswebmaster@itis.gov. Additional support and documentation are available through the portal and web service description pages.