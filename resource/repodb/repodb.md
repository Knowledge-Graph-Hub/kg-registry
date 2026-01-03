---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://datascience.unm.edu/
  label: University of New Mexico Translational Informatics Division
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.chiragjpgroup.org/
  label: Harvard School of Medicine Patel Group
creation_date: '2025-07-17T00:00:00Z'
description: RepoDB is a standard dataset of drug repositioning successes and failures  that
  can be used to fairly and reproducibly benchmark computational  repositioning methods.
  The database contains approved drugs, their  indications, and clinical trial outcomes.
domains:
- drug discovery
- pharmacology
- clinical
- biomedical
homepage_url: https://unmtid-shinyapps.net/shiny/repodb/
id: repodb
infores_id: repodb
last_modified_date: '2025-08-07T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: RepoDB
products:
- category: Product
  description: Complete RepoDB dataset containing drug repositioning successes and
    failures, with approved drugs, indications, and clinical trial outcomes
  format: csv
  id: repodb.full_dataset
  name: RepoDB Full Dataset
  original_source:
  - drugcentral
  - clinicaltrialsgov
  product_url: https://unmtid-shinyapps.net/shiny/repodb/session/98046b0f66cea75c432b5576c1ba2840/download/downloadFull?w=
  warnings:
  - File was not able to be retrieved when checked on 2026-01-02_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-27_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-07_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-03: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: Interactive web interface for exploring RepoDB data with drug-centric  and
    disease-centric search capabilities
  id: repodb.web_interface
  name: RepoDB Web Interface
  product_url: https://unmtid-shinyapps.net/shiny/repodb/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- doi: 10.1038/sdata.2017.29
  id: doi:10.1038/sdata.2017.29
  preferred: true
  title: A standard database for drug repositioning
- id: pmid:28291243
  title: A standard database for drug repositioning
taxon:
- NCBITaxon:9606
---
# RepoDB: A Standard Database for Drug Repositioning

RepoDB is a comprehensive database designed to support drug repositioning research by providing a standard set of drug repositioning successes and failures. This resource enables fair and reproducible benchmarking of computational repositioning methods by offering curated data on approved drugs, their therapeutic indications, and clinical trial outcomes.

## Overview

Drug repositioning (also known as drug repurposing) involves finding new therapeutic uses for existing approved drugs. RepoDB addresses the critical need for standardized datasets in this field by providing:

- **Repositioning Successes**: Drugs that have been successfully repositioned for new indications
- **Repositioning Failures**: Clinical trials that did not result in successful repositioning
- **Approved Drug-Indication Pairs**: Current therapeutic uses of approved drugs
- **Clinical Trial Data**: Outcomes from ClinicalTrials.gov

## Data Sources and Methodology

RepoDB integrates data from two primary sources:

### DrugCentral
- Comprehensive database of approved drugs and their indications
- Provides information on drug properties, targets, and therapeutic uses
- Ensures data quality and standardization

### ClinicalTrials.gov
- Clinical trial registry maintained by the NIH
- Source of clinical trial outcomes and repositioning attempts
- Provides data on both successful and failed repositioning efforts

## Key Features

### Web Interface Functionality
- **Drug-centric searching**: Explore repositioning data by specific drugs
- **Disease-centric searching**: Find repositioning opportunities by therapeutic area
- **Interactive visualizations**: Explore data characteristics and relationships
- **Full dataset download**: Access complete RepoDB data for computational analysis

### Data Characteristics
- Curated drug repositioning successes and failures
- Standardized drug and disease identifiers
- Clinical trial phase information
- Temporal data on drug approvals and repositioning events

## Applications

### Research Applications
- **Computational Method Benchmarking**: Standard dataset for evaluating repositioning algorithms
- **Drug Discovery**: Identify potential repositioning opportunities
- **Clinical Research**: Understand patterns in successful and failed repositioning
- **Pharmacovigilance**: Study drug safety across different indications

### Educational Use
- Teaching drug repositioning concepts
- Demonstrating computational drug discovery methods
- Case studies in pharmaceutical research

## Data Updates

RepoDB is regularly updated to maintain current and comprehensive coverage:

- **Original Version (2017)**: Developed by Harvard School of Medicine Patel Group
- **2020 Update**: Enhanced by University of New Mexico with updated sources
- **2023 Update**: Latest version with current DrugCentral, AACT, and UMLS data

## Citation Guidelines

When using RepoDB, please cite:
- Brown AS, Patel CJ. A standard database for drug repositioning. Sci Data. 2017;4:170029.

## Access and Usage

### Data Download
- Full dataset available through the web interface
- CSV format for computational analysis
- Regular updates ensure data currency

### Web Interface
- Interactive exploration at: https://unmtid-shinyapps.net/shiny/repodb/
- No registration required for basic access
- Educational and research use encouraged

## License and Terms

RepoDB is released under the Creative Commons Attribution 4.0 International License, making it freely available for:
- Educational purposes
- Scientific research
- Commercial applications (with attribution)

## Development Team

### Current Maintainers
- **University of New Mexico**: Translational Informatics Division
- **Data Science Team**: Jeremy Yang and collaborators

### Original Developers
- **Harvard School of Medicine**: Patel Group
- **Principal Investigators**: AS Brown and CJ Patel

## Technical Specifications

- **Data Format**: CSV, web-accessible
- **Update Frequency**: Periodic updates with new source data
- **Access Method**: Web interface and direct download
- **API**: Web-based search and filtering capabilities