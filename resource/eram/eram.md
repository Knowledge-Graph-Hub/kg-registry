---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: The encyclopedia of Rare disease Annotation for Precision Medicine (eRAM)
  is a standardized system providing computational annotations for rare diseases to
  support precision medicine. eRAM provides annotations for approximately 16,000 rare
  diseases, including detailed information on clinical phenotypes, symptoms, genes,
  and genotypes. The database contains over 6,100 human disease-related phenotype
  terms, 31,600 mammalian phenotype terms, 10,200 symptoms from UMLS, 18,800 genes
  and 92,500 genotypes. eRAM organizes diseases in a tree structure to systematically
  display relationships between diseases with similar pathogenesis, close anatomical
  sites, the same clinical symptoms or subtypes, facilitating both research into rare
  disease mechanisms and clinical diagnosis and treatment decisions.
domains:
- clinical
- health
- phenotype
- precision medicine
id: eram
infores_id: eram
last_modified_date: '2025-11-19T00:00:00Z'
layout: resource_detail
name: 'eRAM: encyclopedia of rare disease annotations for precision medicine'
homepage_url: http://119.3.41.228/eram/
publications:
- id: PMID:29106618
  title: 'eRAM: encyclopedia of rare disease annotations for precision medicine'
  authors:
  - Jia J
  - An Z
  - Ming Y
  - Guo Y
  - Li W
  - Liang Y
  - Guo D
  - Li X
  - Tai J
  - Chen G
  - Jin Y
  - Liu Z
  - Ni X
  - Shi T
  journal: Nucleic Acids Research
  year: '2018'
  doi: 10.1093/nar/gkx1062
products:
- category: GraphicalInterface
  description: Web-based interface for browsing and querying rare disease annotations
    including phenotypes, symptoms, genes, and genotypes with tree-structured disease
    organization
  format: http
  id: eram.web
  name: eRAM Web Interface
  original_source:
  - eram
  product_url: http://119.3.41.228/eram/
- category: Product
  description: Downloadable data files containing rare disease annotations, phenotypes,
    symptoms, genes, and genotypes
  format: mixed
  id: eram.downloads
  name: eRAM Data Downloads
  original_source:
  - eram
  product_url: http://119.3.41.228/eram/download.php
synonyms:
- eRAM
taxon:
- NCBITaxon:9606
- NCBITaxon:40674
---

# eRAM: encyclopedia of rare disease annotations for precision medicine

The encyclopedia of Rare Disease Annotation for Precision Medicine (eRAM) provides computational annotations for rare diseases to support precision medicine applications. Developed to address the limited knowledge of rare diseases that forms a major obstacle to improving their treatment, eRAM focuses on detailed clinical phenotyping as a keystone for deciphering genes related to rare diseases and realizing precision medicine.

## Key Features

- **Comprehensive Coverage**: Annotations for approximately 16,000 rare diseases
- **Multi-source Phenotype Data**: 6,147 human disease-related phenotype terms, 31,661 mammalian phenotype terms, 10,202 symptoms from UMLS
- **Genetic Information**: 18,815 genes and 92,580 genotypes associated with rare diseases
- **Tree Structure Organization**: Systematic display of diseases and relationships between diseases with similar pathogenesis, close anatomical sites, or the same clinical symptoms
- **Clinical Support**: Provides clinical phenotypes with importance rankings and appropriate treatment strategies to facilitate timely diagnosis and treatment

## Data Sources

eRAM integrates information from multiple authoritative sources including the Human Disease Network, Online Mendelian Inheritance in Man (OMIM), the Unified Medical Language System (UMLS), the Disease Ontology, Medical Subject Headings (MeSH), and Orphanet.

## Information Resource ID

This resource has the Information Resource identifier: `infores:eram`
