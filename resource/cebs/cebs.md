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
last_modified_date: '2026-10-27T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs.niehs.nih.gov/cebs/search
- category: GraphicalInterface
  description: DTT Data Collections Guided Search, providing filterable, downloadable
    tables for curated NIEHS Division of Translational Toxicology (DTT) data collections
    (e.g., clinical chemistry, hematology, and other individual animal data; treatment-related
    findings; DTT publications; and a Tox21 p53 activator dataset)
  format: http
  id: cebs.dtt-data-collections
  name: DTT Data Collections Guided Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs-ext.niehs.nih.gov/datasets
- category: Product
  description: Toxicology study data from NTP and other programs
  format: mixed
  id: cebs.data
  name: CEBS Study Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs.niehs.nih.gov/cebs/
- category: ProgrammingInterface
  connection_url: https://manticore.niehs.nih.gov/cebsapi/v1
  description: Programmatic API access to CEBS data, documented by the CEBS API user
    help. Note that as of October 2026 the documented base URL (https://manticore.niehs.nih.gov/cebsapi/v1)
    and example requests returned HTTP 404.
  format: http
  id: cebs.api
  name: CEBS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: ntp
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
- category: GraphProduct
  description: 'CEBS Automat: per-source KGX knowledge graph download (Biolink 4.2.6).'
  format: kgx-jsonl
  id: automat.cebs
  name: CEBS_Automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:wasInformedBy
    source: ubergraph
  product_url: https://stars.renci.org/var/plater/bl-4.2.6/CEBS_Automat/
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
rrid: SCR_006778
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

### DTT Data Collections Guided Search
Guided search over curated NIEHS Division of Translational Toxicology (DTT) data collections, with results shown as filterable tables available for download: [https://cebs-ext.niehs.nih.gov/datasets](https://cebs-ext.niehs.nih.gov/datasets).

### CEBS API
Programmatic access to CEBS data for computational toxicology applications, documented in the [CEBS API User Help](https://tools.niehs.nih.gov/cebs3/support/assets/docs/CEBS_API-User-Help.pdf). As of October 2026, the documented base URL (`https://manticore.niehs.nih.gov/cebsapi/v1`) returned HTTP 404.

## Data Sources

CEBS data come primarily from studies conducted by the National Toxicology Program (NTP) and the NIEHS Division of Translational Toxicology (DTT), including carcinogenicity, short-term toxicity, and genetic toxicity studies, as well as non-DTT studies of environmental health interest deposited by other investigators. Some DTT data collections incorporate Tox21 assay results.

## Citation

Per the CEBS citation guidance: Chemical Effects in Biological Systems (CEBS). Research Triangle Park, NC (USA): Division of Translational Toxicology, NIEHS (DTT). https://cebs.niehs.nih.gov/cebs/

Martini C, et al. CEBS update: curated toxicology database with enhanced tools for data integration. Nucleic Acids Research. 2022. doi:10.1093/nar/gkab981

## Information Resource ID

This resource has the Information Resource identifier: `infores:cebs`

## Domains

- Toxicology
- Biomedical
- Health
- Public Health