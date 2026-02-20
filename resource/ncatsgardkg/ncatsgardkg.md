---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jsanjak@gmail.com
  label: Jaleal Sanjak
description: The NCATS GARD Knowledge Graph integrates data about rare diseases, creating
  a comprehensive resource for rare disease research and drug discovery. It leverages
  clustering and machine learning approaches to identify relationships between rare
  diseases and potential therapeutic targets.
domains:
- health
- biomedical
- clinical
- genomics
homepage_url: https://github.com/ncats/RD-Clust
id: ncatsgardkg
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: NCATS GARD KG
publications:
- doi: 10.1093/jamia/ocad186
  id: https://doi.org/10.1093/jamia/ocad186
  title: A knowledge graph approach to rare disease research and drug discovery
  year: '2023'
- doi: 10.1101/2023.02.15.528673
  id: https://doi.org/10.1101/2023.02.15.528673
  title: 'RD-Clust: A tool for rare disease clustering and drug discovery'
  year: '2023'
repository: https://github.com/ncats/RD-Clust
products:
- category: ProcessProduct
  description: RD-Clust source repository implementing NCATS GARD KG clustering and analysis workflows.
  format: http
  id: ncatsgardkg.code
  name: NCATS GARD KG Source Repository
  original_source:
  - ncatsgardkg
  product_url: https://github.com/ncats/RD-Clust
- category: Product
  description: Repository subdirectory containing raw datasets used to construct the NCATS GARD KG workflow.
  format: http
  id: ncatsgardkg.raw-data
  name: NCATS GARD KG Raw Data Directory
  original_source:
  - ncatsgardkg
  product_url: https://github.com/ncats/RD-Clust/tree/main/data/raw
taxon:
- NCBITaxon:9606
---
# NCATS GARD KG

The NCATS GARD Knowledge Graph (KG) is a comprehensive knowledge graph focused on rare diseases, developed by the National Center for Advancing Translational Sciences (NCATS). This resource integrates data from the Genetic and Rare Diseases Information Center (GARD) and other sources to create a rich network of relationships between rare diseases, genes, drugs, and other biomedical entities.

The knowledge graph leverages advanced clustering and machine learning approaches to identify patterns and relationships that can inform rare disease research and drug discovery efforts. It provides a structured representation of rare disease knowledge that can be used to support translational research and precision medicine applications.

## Key Features

- Comprehensive integration of rare disease data from GARD and other sources
- Machine learning-enhanced clustering of diseases and therapeutic targets
- Support for drug discovery and repurposing efforts
- Structured knowledge representation suitable for computational analysis

## Applications

The NCATS GARD KG supports various research applications including:
- Rare disease drug discovery and repurposing
- Identification of disease-disease relationships
- Biomarker discovery for rare diseases
- Precision medicine approaches for rare disease patients

## Development

This resource is developed and maintained by researchers at NCATS as part of their mission to advance translational sciences and improve treatments for rare diseases.

## Evaluation

- View the evaluation: [ncatsgardkg evaluation](ncatsgardkg_eval.html)
