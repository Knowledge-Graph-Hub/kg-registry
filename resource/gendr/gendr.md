---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://hagr.ageing-map.org/help.html#gendr
    label: Human Ageing Genomic Resources
creation_date: '2025-11-05T00:00:00Z'
description: GenDR (Database of Dietary Restriction-Related Genes) is a curated database of genes associated with dietary restriction (DR) and its effects on longevity and aging. Part of the Human Ageing Genomic Resources (HAGR), GenDR compiles experimental data on genes whose expression or function is altered by dietary restriction regimens across multiple model organisms. The database includes information on gene function, expression changes, and links to aging-related phenotypes.
domains:
  - genomics
  - health
  - nutrition
  - biological systems
homepage_url: https://hagr.ageing-map.org/diet/
id: gendr
infores_id: gendr
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: GenDR Database of Dietary Restriction-Related Genes
products:
  - category: GraphicalInterface
    description: Web-based search and browsing interface for GenDR
    format: http
    id: gendr.web
    name: GenDR Web Interface
    original_source:
      - source: gendr
        relation_type: prov:hadPrimarySource
    product_url: https://hagr.ageing-map.org/diet/
  - category: Product
    description: Downloadable dataset of dietary restriction-related genes
    format: csv
    id: gendr.data
    latest_version: Build 4
    name: GenDR Data Download
    original_source:
      - source: gendr
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: pubmed
        relation_type: prov:wasInformedBy
      - source: ncbigene
        relation_type: prov:wasInformedBy
    product_file_size: 8209
    product_url: https://hagr.ageing-map.org/diet/dataset.zip
  - category: Product
    description: Excel spreadsheet of dietary-restriction gene expression signatures
      from the HAGR meta-analysis of dietary restriction in mammals
    format: http
    id: gendr.expression-signatures
    name: GenDR Dietary Restriction Expression Signatures
    original_source:
      - source: gendr
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: pubmed
        relation_type: prov:wasInformedBy
    product_file_size: 49152
    product_url: https://hagr.ageing-map.org/diet/TableS2.xls
publications:
  - authors:
      - de Magalhaes JP
      - Abidi Z
      - Dos Santos GA
      - Avelar RA
      - Barardo D
    doi: 10.1093/nar/gkad927
    id: doi:10.1093/nar/gkad927
    journal: Nucleic Acids Research
    preferred: true
    title: 'Human Ageing Genomic Resources: updates on key databases in ageing research'
    year: '2023'
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
Download complete datasets of GenDR genes and associated metadata for computational
analysis. HAGR lists GenDR Build 4 with 214 gene manipulations and 172 expression
changes.

### Expression Signatures
The dietary restriction gene expression signatures are available as an Excel
spreadsheet linked from the HAGR downloads page.

## Information Resource ID

This resource has the Information Resource identifier: `infores:gendr`

## Publications

- [Human Ageing Genomic Resources: updates on key databases in ageing research](https://doi.org/10.1093/nar/gkad927) (2023)

## Domains

- Genomics
- Health
- Nutrition
- Biological Systems

## Taxon Coverage

Eukaryota (NCBITaxon:2759) - includes yeast, C. elegans, Drosophila, rodents, and other model organisms
