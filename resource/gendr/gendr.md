---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://genomics.senescence.info/help.html
  label: Human Ageing Genomic Resources
creation_date: '2025-11-05T00:00:00Z'
description: GenDR (Database of Dietary Restriction-Related Genes) is a curated database of genes associated with dietary restriction (DR) and its effects on longevity and aging. Part of the Human Ageing Genomic Resources (HAGR), GenDR compiles experimental data on genes whose expression or function is altered by dietary restriction regimens across multiple model organisms. The database includes information on gene function, expression changes, and links to aging-related phenotypes.
domains:
  - genomics
  - health
  - nutrition
  - biological systems
homepage_url: http://genomics.senescence.info/diet/
id: gendr
infores_id: gendr
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: GenDR Database of Dietary Restriction-Related Genes
products:
- category: GraphicalInterface
  description: Web-based search and browsing interface for GenDR
  format: http
  id: gendr.web
  name: GenDR Web Interface
  original_source:
  - gendr
  product_url: http://genomics.senescence.info/diet/
- category: Product
  description: Downloadable dataset of dietary restriction-related genes
  format: csv
  id: gendr.data
  name: GenDR Data Download
  original_source:
  - gendr
  product_url: http://genomics.senescence.info/diet/dataset.zip
- category: ProgrammingInterface
  description: Programmatic access to GenDR data
  format: http
  id: gendr.api
  name: GenDR API
  original_source:
  - gendr
  product_url: http://genomics.senescence.info/diet/help.html#api
publications:
- id: https://doi.org/10.1093/nar/gkp1108
synonyms:
  - GenDR
  - gendr
taxon:
- NCBITaxon:2759
---

# GenDR Database of Dietary Restriction-Related Genes

## Overview

GenDR (Database of Dietary Restriction-Related Genes) is a curated database of genes associated with dietary restriction (DR) and its effects on longevity and aging. Part of the Human Ageing Genomic Resources (HAGR), GenDR compiles experimental data on genes whose expression or function is altered by dietary restriction regimens across multiple model organisms.

## Key Features

- **Curated Gene Data**: Manually curated information on DR-related genes
- **Multi-Organism Coverage**: Data from multiple model organisms including yeast, worms, flies, mice, and rats
- **Expression Data**: Gene expression changes under dietary restriction conditions
- **Longevity Links**: Connections between DR genes and aging/longevity phenotypes
- **Functional Annotations**: Gene function and pathway information

## Research Applications

GenDR supports research in:
- Aging and longevity mechanisms
- Caloric restriction effects on gene expression
- Nutrigenomics and metabolic regulation
- Translational gerontology research
- Systems biology of aging

## Products

### Web Interface
Search and browse dietary restriction-related genes through an interactive web interface with detailed gene information and cross-references.

### Data Downloads
Download complete datasets of GenDR genes and associated metadata for computational analysis.

### API Access
Programmatic access to GenDR data for integration into bioinformatics workflows.

## Information Resource ID

This resource has the Information Resource identifier: `infores:gendr`

## Publications

- [The GenDR database: a resource for dietary restriction-related genes](https://doi.org/10.1093/nar/gkp1108) (2010)

## Domains

- Genomics
- Health
- Nutrition
- Biological Systems

## Taxon Coverage

Eukaryota (NCBITaxon:2759) - includes yeast, C. elegans, Drosophila, rodents, and other model organisms

