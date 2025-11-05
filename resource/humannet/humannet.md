---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.inetbio.org/humannet/
  label: INetBio
creation_date: '2025-11-05T00:00:00Z'
description: HumanNet is a probabilistic functional gene network for Homo sapiens
  that integrates genomic and proteomic data from multiple sources to predict functional
  relationships between genes. The network uses a modified Bayesian integration approach
  to combine evidence from diverse data types including protein-protein interactions,
  gene co-expression, phylogenetic profiling, and literature mining. HumanNet provides
  confidence scores for gene-gene functional linkages and can be used for gene function
  prediction, disease gene prioritization, and pathway analysis.
domains:
- genomics
- systems biology
- biomedical
- biological systems
homepage_url: https://www.inetbio.org/humannet/
id: humannet
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: HumanNet
products:
- category: GraphicalInterface
  description: Web interface for querying and visualizing the HumanNet functional
    gene network
  format: http
  id: humannet.web
  name: HumanNet Web Interface
  original_source:
  - humannet
  product_url: https://www.inetbio.org/humannet/
- category: GraphProduct
  description: Downloadable functional gene network with confidence scores
  format: tsv
  id: humannet.network
  name: HumanNet Network File
  original_source:
  - humannet
  product_url: https://www.inetbio.org/humannet/download.php
- category: ProgrammingInterface
  description: API for programmatic access to HumanNet data
  format: http
  id: humannet.api
  name: HumanNet API
  original_source:
  - humannet
  product_url: https://www.inetbio.org/humannet/
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
publications:
- id: https://doi.org/10.1093/nar/gky1126
synonyms:
- HumanNet
- humannet
taxon:
- NCBITaxon:9606
---
# HumanNet

## Overview

HumanNet is a probabilistic functional gene network for Homo sapiens that integrates genomic and proteomic data from multiple sources to predict functional relationships between genes.

Using a modified Bayesian integration approach, HumanNet combines evidence from diverse data types including protein-protein interactions, gene co-expression patterns, phylogenetic profiling, and biomedical literature to construct a comprehensive functional network with confidence-weighted gene-gene linkages.

## Key Features

- **Comprehensive Coverage**: Network spanning the human genome
- **Multi-Source Integration**: Combines protein interactions, co-expression, phylogeny, and literature
- **Confidence Scores**: Probabilistic scores for functional linkages
- **Multiple Versions**: Different network versions for specific applications (XN, XC, XI)
- **Web Tools**: Interactive visualization and analysis tools
- **Tissue-Specific Networks**: Context-specific functional networks

## Research Applications

- Gene function prediction
- Disease gene prioritization
- Pathway analysis and enrichment
- Systems biology studies
- Network-based drug target discovery
- Functional module identification

## Products

### HumanNet Web Interface
Interactive platform for querying genes, visualizing network neighborhoods, and performing gene function predictions.

### HumanNet Network File
Downloadable network files containing gene-gene functional linkages with confidence scores in various formats.

### HumanNet API
Programmatic access to HumanNet data for integration into computational workflows and analysis pipelines.

## Information Resource ID

This resource has the Information Resource identifier: `infores:humannet`

## Publications

- [HumanNet v3: an improved database of human gene networks for disease research](https://doi.org/10.1093/nar/gky1126) (2019)

## Domains

- Genomics
- Systems Biology
- Biomedical
- Biological Systems

## Taxon Coverage

Human (NCBITaxon:9606)