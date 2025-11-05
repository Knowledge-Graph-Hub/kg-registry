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
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: PFOCR
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing extracted pathway figures
  format: http
  id: pfocr.web
  name: PFOCR Web Interface
  original_source:
  - pfocr
  product_url: https://pfocr.wikipathways.org/
- category: Product
  description: Extracted pathway information from literature figures
  format: json
  id: pfocr.data
  name: PFOCR Pathway Data
  original_source:
  - pfocr
  product_url: https://github.com/wikipathways/pfocr-database
- category: ProgrammingInterface
  description: API for accessing PFOCR extracted pathway data
  format: http
  id: pfocr.api
  name: PFOCR API
  original_source:
  - pfocr
  product_url: https://pfocr.wikipathways.org/
publications:
- id: https://doi.org/10.1101/379446
repository: https://github.com/wikipathways/pfocr
synonyms:
  - PFOCR
  - Pathway Figure OCR
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

Source code: https://github.com/wikipathways/pfocr

## Domains

- Pathways
- Literature
- Biomedical
- Systems Biology
