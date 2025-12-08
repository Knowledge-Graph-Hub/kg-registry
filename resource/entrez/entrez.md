---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/home/about/contact/
  id: ncbi
  label: NCBI
creation_date: '2025-11-05T00:00:00Z'
description: Entrez is NCBI's primary text search and retrieval system that integrates
  multiple biological databases including PubMed, GenBank, Gene, Protein, and many
  others. It provides a unified query interface and retrieval mechanism across NCBI's
  vast collection of biomedical and genomic data resources, enabling researchers to
  search and access information from disparate databases using a single query system.
domains:
- biomedical
- literature
homepage_url: https://www.ncbi.nlm.nih.gov/Web/Search/entrezfs.html
id: entrez
infores_id: entrez
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: Entrez
products:
- category: ProgrammingInterface
  description: E-utilities API for programmatic access to Entrez databases
  format: http
  id: entrez.eutils
  name: Entrez E-utilities
  original_source:
  - entrez
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- category: GraphicalInterface
  description: Web-based search interface for Entrez databases
  format: http
  id: entrez.web
  name: Entrez Web Interface
  original_source:
  - entrez
  product_url: https://www.ncbi.nlm.nih.gov/sites/gquery
- category: ProgrammingInterface
  description: Entrez Direct command-line tools for Unix systems
  format: mixed
  id: entrez.edirect
  name: Entrez Direct (EDirect)
  original_source:
  - entrez
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK179288/
  repository: https://github.com/ncbi/entrez-direct
synonyms:
- Entrez
- NCBIGene
- NCBI Entrez
taxon:
- NCBITaxon:1
---

# Entrez

## Overview

Entrez is NCBI's primary text search and retrieval system that integrates multiple biological databases including PubMed, GenBank, Gene, Protein, and many others. It provides a unified query interface and retrieval mechanism across NCBI's vast collection of biomedical and genomic data resources.

## Key Features

- **Unified Search**: Single query interface across 40+ NCBI databases
- **Cross-Database Links**: Integrated links between related records in different databases
- **Programmatic Access**: E-utilities API and Entrez Direct command-line tools
- **Advanced Queries**: Boolean operators, field-specific searches, and query history
- **Comprehensive Coverage**: Access to literature, sequences, structures, genomes, and more

## Integrated Databases

Entrez provides access to numerous NCBI databases including:
- **Literature**: PubMed, PMC, Books
- **Genomics**: GenBank, Gene, Genome, Assembly
- **Proteins**: Protein, Structure
- **Clinical**: ClinVar, GTR, MedGen
- **Taxonomy**: Taxonomy
- And many more specialized databases

## Products

### E-utilities API
The Entrez Programming Utilities (E-utilities) provide programmatic access to NCBI databases through a set of server-side programs that accept fixed URL syntax for retrieving data.

### Entrez Direct (EDirect)
Command-line tools that provide access to NCBI's suite of interconnected databases from a Unix terminal window.

### Web Interface
The web-based Entrez Global Query Cross-Database Search System allows interactive searching across all Entrez databases.

## Information Resource ID

This resource has the Information Resource identifier: `infores:entrez`

## Domains

- Genomics
- Biomedical
- Literature
- Biological Systems

## Taxon Coverage

All organisms (NCBITaxon:1 - root of NCBI Taxonomy)