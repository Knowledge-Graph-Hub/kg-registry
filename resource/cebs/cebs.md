---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cebs.niehs.nih.gov/
  label: NIEHS
- category: Organization
  contact_details:
  - contact_type: email
    value: CEBS-support@mail.nih.gov
  label: CEBS Support
creation_date: '2025-11-05T00:00:00Z'
description: Chemical Effects in Biological Systems (CEBS) is a public, web-accessible,
  manually curated repository of toxicology study data from the National Toxicology
  Program (NTP) and other research programs. CEBS contains individual-level and summarized
  study data from carcinogenicity studies, short-term toxicity studies, genetic toxicity
  assays, and other toxicological investigations. The database integrates chemical
  structure information, study designs, experimental conditions, and biological effects
  to support toxicology research and risk assessment.
domains:
- toxicology
- biomedical
- public health
homepage_url: https://cebs.niehs.nih.gov/
id: cebs
infores_id: cebs
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
name: CEBS
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing CEBS toxicology data
  format: http
  id: cebs.web
  name: CEBS Search Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  product_url: https://cebs.niehs.nih.gov/cebs/search
- category: Product
  description: Toxicology study data from NTP and other programs
  format: mixed
  id: cebs.data
  name: CEBS Study Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  product_url: https://cebs.niehs.nih.gov/cebs/
- category: ProgrammingInterface
  connection_url: https://manticore.niehs.nih.gov/cebsapi/v1
  description: Programmatic API access to CEBS data, documented by the CEBS API user
    help
  format: http
  id: cebs.api
  name: CEBS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  product_url: https://tools.niehs.nih.gov/cebs3/support/assets/docs/CEBS_API-User-Help.pdf
- category: DocumentationProduct
  description: CEBS citation guidance for referencing the database and study URLs
  format: pdf
  id: cebs.citation-guide
  name: Citing CEBS
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  product_file_size: 152093
  product_url: https://cebs.niehs.nih.gov/cebs/support/download/Citing-CEBS.pdf
publications:
- authors:
  - Cari Martini
  - Ying Frances Liu
  - Hui Gong
  - Nicole Sayers
  - German Segura
  - Jennifer Fostel
  doi: 10.1093/nar/gkab981
  id: doi:10.1093/nar/gkab981
  journal: Nucleic Acids Research
  preferred: true
  title: 'CEBS update: curated toxicology database with enhanced tools for data integration'
  year: '2022'
- authors:
  - Isabel A. Lea
  - Hui Gong
  - Anand Paleja
  - Asif Rashid
  - Jennifer Fostel
  doi: 10.1093/nar/gkw1077
  id: doi:10.1093/nar/gkw1077
  journal: Nucleic Acids Research
  title: 'CEBS: a comprehensive annotated database of toxicological data'
  year: '2017'
synonyms:
- CEBS
- Chemical Effects in Biological Systems
---
# Chemical Effects in Biological Systems

## Overview

Chemical Effects in Biological Systems (CEBS) is a public, web-accessible, manually curated repository of toxicology study data from the National Toxicology Program (NTP) and other research programs.

CEBS contains comprehensive data from multiple study types including carcinogenicity studies, short-term toxicity studies, genetic toxicity assays, reproductive and developmental toxicity studies, and other toxicological investigations. The database provides detailed information at both individual animal and study summary levels.

## Key Features

- **Comprehensive Study Data**: Individual-level and summarized toxicology data
- **Multiple Study Types**: Carcinogenicity, acute/chronic toxicity, genetic toxicity, reproductive/developmental toxicity
- **Chemical Information**: Integrated with chemical structure and properties
- **Study Metadata**: Detailed experimental designs, dosing regimens, and conditions
- **Pathology Data**: Histopathological findings and lesion classifications
- **Public Access**: Free access for research and regulatory purposes

## Research Applications

- Toxicology research and hypothesis generation
- Risk assessment and safety evaluation
- Computational toxicology modeling
- Adverse outcome pathway (AOP) development
- Cross-study comparisons and meta-analysis
- Support for read-across and QSAR approaches

## Products

### CEBS Search Interface
Web-based interface for querying and browsing NTP toxicology studies with advanced search capabilities.

### CEBS Study Data
Downloadable toxicology study data including individual animal data, pathology findings, and study summaries.

### CEBS API
Programmatic access to CEBS data for computational toxicology applications.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cebs`

## Domains

- Toxicology
- Biomedical
- Health
- Public Health