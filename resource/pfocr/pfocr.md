---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://pfocr.wikipathways.org/
    label: WikiPathways
creation_date: '2025-11-05T00:00:00Z'
description: Pathway Figure OCR (PFOCR) is a resource that extracts biological pathway information from figures in scientific publications using optical character recognition (OCR) and machine learning. PFOCR automatically identifies pathway diagrams in published literature, extracts gene and protein names from pathway figures, and creates structured pathway data. The resource enables discovery of pathway knowledge that exists only in figure format and is not captured in article text or structured databases.
domains:
  - pathways
  - literature
  - biomedical
  - systems biology
homepage_url: https://pfocr.wikipathways.org/
id: pfocr
infores_id: pfocr
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: PFOCR
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing extracted pathway figures
    format: http
    id: pfocr.web
    name: PFOCR Web Interface
    original_source:
      - source: pfocr
        relation_type: prov:hadPrimarySource
    product_url: https://pfocr.wikipathways.org/
  - category: Product
    description: GitHub repository containing the Jekyll site and database content
      for PFOCR, including figure metadata in the _figures directory
    format: http
    id: pfocr.database_repository
    name: PFOCR Database Repository
    original_source:
      - source: pfocr
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/wikipathways/pfocr-database
    repository: https://github.com/wikipathways/pfocr-database
  - category: Product
    description: Search metadata JSON used by the PFOCR website for figure, gene,
      pathway, and keyword search
    format: json
    id: pfocr.search_json
    name: PFOCR Search JSON
    original_source:
      - source: pfocr
        relation_type: prov:hadPrimarySource
    product_file_size: 55889831
    product_url: https://pfocr.wikipathways.org/search.json
  - category: Product
    description: JSON file containing all PFOCR figure information for pathway figures
      extracted from literature
    format: json
    id: pfocr.figure_info_json
    name: PFOCR Figure Information JSON
    original_source:
      - source: pfocr
        relation_type: prov:hadPrimarySource
    product_file_size: 59089985
    product_url: https://pfocr.wikipathways.org/json/getFigureInfo.json
  - category: Product
    description: Current GMT release of PFOCR pathway figure gene sets distributed
      through WikiPathways data downloads
    format: txt
    id: pfocr.gmt
    name: PFOCR GMT Gene Sets
    original_source:
      - source: pfocr
        relation_type: prov:hadPrimarySource
    product_url: https://data.wikipathways.org/pfocr/current/
  - category: ProgrammingInterface
    description: JSON endpoints and help documentation for accessing PFOCR extracted
      pathway figure data programmatically
    format: http
    id: pfocr.api
    name: PFOCR API
    original_source:
      - source: pfocr
        relation_type: prov:hadPrimarySource
    product_url: https://pfocr.wikipathways.org/help.html#download
publications:
  - authors:
      - Hanspers K
      - Riutta A
      - Summer-Kutmon M
      - Pico AR
    doi: 10.1186/s13059-020-02181-2
    id: doi:10.1186/s13059-020-02181-2
    journal: Genome Biology
    preferred: true
    title: Pathway information extracted from 25 years of pathway figures
    year: '2020'
  - authors:
      - Riutta A
      - Hanspers K
      - Pico AR
    doi: 10.1101/379446
    id: doi:10.1101/379446
    journal: bioRxiv
    title: Identifying Genes in Published Pathway Figure Images
    year: '2018'
repository: https://github.com/wikipathways/pfocr-database
synonyms:
  - PFOCR
  - Pathway Figure OCR
warnings:
  - The formerly listed wikipathways/pfocr repository returned 404 during 2026-06-02
    curation; the maintained database repository is wikipathways/pfocr-database.
---

# PFOCR - Pathway Figure OCR

## Overview

Pathway Figure OCR (PFOCR) is a resource that extracts biological pathway information from figures in scientific publications using optical character recognition (OCR) and machine learning.

PFOCR addresses the challenge that much pathway knowledge exists only in published figures and is not captured in article abstracts or structured databases. By automatically processing pathway diagrams, PFOCR makes this "hidden" knowledge discoverable and machine-readable.

## Key Features

- **Automated Figure Processing**: Identifies pathway figures in publications using machine learning
- **OCR Extraction**: Extracts gene/protein names and pathway elements from figures
- **Entity Recognition**: Identifies and normalizes biological entities (genes, proteins, metabolites)
- **Pathway Reconstruction**: Creates structured pathway data from visual representations
- **Literature Coverage**: Processes figures from PubMed Central and other sources
- **Integration**: Data compatible with WikiPathways and other pathway resources

## Research Applications

- Literature-based pathway discovery
- Pathway knowledge mining
- Gene function annotation
- Systems biology network construction
- Complement to text mining approaches
- Pathway database enrichment

## Products

### PFOCR Web Interface
Search and browse pathway information extracted from literature figures with visualization of source figures and extracted data.

### PFOCR Pathway Data
Structured pathway data extracted from literature figures, including gene/protein interactions and pathway relationships in machine-readable formats.

### PFOCR API
Programmatic access to PFOCR data for integration with pathway analysis tools and knowledge graphs.

## Information Resource ID

This resource has the Information Resource identifier: `infores:pfocr`

## Publications

- [PFOCR: A flexible extraction pipeline for automated optical character recognition of pathway images](https://doi.org/10.1101/379446) (2018)

## Repository

Database repository: https://github.com/wikipathways/pfocr-database

## Domains

- Pathways
- Literature
- Biomedical
- Systems Biology
