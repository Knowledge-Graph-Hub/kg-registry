---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: FDA-SRS@fda.hhs.gov
  label: FDA Substance Registration System Team
creation_date: '2025-07-17T00:00:00Z'
description: FDA's Global Substance Registration System (GSRS) is a comprehensive
  database that provides Unique Ingredient Identifiers (UNIIs) for substances in FDA-regulated
  products. UNIIs uniquely define substances based on scientific identity characteristics
  using ISO 11238 data elements, enabling efficient and accurate exchange of substance
  information across regulatory domains.
domains:
- clinical
- drug discovery
- pharmacology
- public health
homepage_url: https://precision.fda.gov/uniisearch
id: unii
last_modified_date: '2025-09-24T00:00:00Z'
layout: resource_detail
name: FDA Global Substance Registration System (UNII)
products:
- category: GraphicalInterface
  description: Web-based search interface for finding substances by UNII, name, or
    other identifiers
  format: http
  id: unii.search
  name: UNII Search Service
  product_url: https://precision.fda.gov/uniisearch
- category: Product
  compression: zip
  description: Downloadable list of all UNIIs with basic substance information
  format: csv
  id: unii.list
  name: UNII List Download
  product_url: https://precision.fda.gov/uniisearch/archive/latest/UNIIs.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-24: HTTP 403 error
    when accessing file'
- category: Product
  compression: zip
  description: Comprehensive UNII data with detailed substance attributes and mappings
  format: mixed
  id: unii.data
  name: UNII Data Download
  product_url: https://precision.fda.gov/uniisearch/archive/latest/UNII_Data.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-24: HTTP 403 error
    when accessing file'
- category: Product
  description: Legacy UNII identifiers for historical substances
  format: txt
  id: unii.legacy
  name: Legacy UNIIs
  product_url: https://precision.fda.gov/uniisearch/archive/latest/Legacy_UNIIs.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-24: HTTP 403 error
    when accessing file'
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - do
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
publications:
- id: https://www.fda.gov/science-research/fda-grand-rounds/fdas-global-substance-registration-system-gsrs-unique-ingredient-identifiers-uniis-uniquely-define
  title: 'FDA Grand Rounds: FDA''s Global Substance Registration System (GSRS) Unique
    Ingredient Identifiers (UNIIs)'
repository: https://ginas.ncats.nih.gov/ginas/app
---
# FDA Global Substance Registration System (UNII)

The FDA's Global Substance Registration System (GSRS) is a comprehensive, authoritative database that generates Unique Ingredient Identifiers (UNIIs) for substances in FDA-regulated products. Developed through collaboration between the FDA's Informatics team, NIH's National Center for Advancing Translational Sciences (NCATS), and the European Medicines Agency (EMA), GSRS addresses the critical need for accurate substance identification across global regulatory domains.

## Overview

UNIIs are generated based on scientific identity characteristics using ISO 11238 data elements, providing standardized identifiers that transcend the variability of substance names across different regulatory domains, countries, and regions. The system classifies substances as chemical, protein, nucleic acid, polymer, structurally diverse, or mixture as detailed in ISO 11238 and ISO DTS 19844 standards.

## Key Features

- **Comprehensive Coverage**: UNIIs can be generated for any substance at any time in the regulatory life cycle, from atoms to organisms
- **Global Standardization**: Enables efficient and accurate exchange of substance information across regulatory domains
- **Scientific Classification**: Substances are defined by standardized, scientific descriptions rather than variable names
- **Regulatory Integration**: Used in electronic listing systems like DailyMed and throughout product life cycles including clinical trials, marketing, and post-market surveillance

## Products and Access

The GSRS provides multiple ways to access UNII data:

1. **UNII Search Service**: Interactive web interface for searching substances by UNII, name, or other identifiers
2. **Downloadable Data**: Comprehensive datasets including UNII lists and detailed substance data
3. **Public GSRS Interface**: Full access to the Global Substance Registration System hosted by NCATS
4. **PrecisionFDA Integration**: Collaborative tools for filtering, exporting, and creating GSRS records

## Applications

UNII identifiers are essential for:
- Drug labeling and electronic submissions
- Clinical trial identification
- Product safety monitoring
- Global supply chain tracking
- Regulatory compliance across FDA-regulated products (food, drugs, tobacco, cosmetics)

## Data Quality and Updates

The system is regularly updated, with the most recent data refresh on August 18, 2025. UNIIs are generated based on the best available public information, and synonyms and mappings are continuously refined. The FDA encourages reporting of data issues to maintain accuracy and completeness.