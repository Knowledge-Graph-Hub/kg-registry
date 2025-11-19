---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: qingyao.huang@uzh.ch
  label: Qingyao Huang
creation_date: '2025-10-30T00:00:00Z'
description: TISSUES is an integrative web resource providing evidence on tissue-specific
  gene and protein expression in mammals. The database combines manually curated literature,
  large-scale proteomics and transcriptomics screens, and automatic text mining, mapping
  all evidence to common protein identifiers and Brenda Tissue Ontology terms with
  unified confidence scores for cross-comparison.
domains:
- genomics
- proteomics
- anatomy and development
homepage_url: https://tissues.jensenlab.org/
id: tissues
infores_id: tissues
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International
name: TISSUES
products:
- category: GraphicalInterface
  description: Web interface for searching and visualizing tissue expression data
    with schematic human body visualization
  format: http
  id: tissues.web
  name: TISSUES Web Interface
  original_source:
  - tissues
  product_url: https://tissues.jensenlab.org/
- category: GraphicalInterface
  description: Search interface for querying genes, proteins, and tissues
  format: http
  id: tissues.search
  name: TISSUES Search
  original_source:
  - tissues
  product_url: https://tissues.jensenlab.org/Search
- category: Product
  description: Downloadable datasets of tissue expression evidence including integrated
    scores and source-specific data
  format: tsv
  id: tissues.downloads
  name: TISSUES Data Downloads
  product_url: https://tissues.jensenlab.org/Downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2025-10-30: No Content-Length
    header found'
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
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - drkg
  - idisk
  - brenda
  - ctd
  - drugbank
  - kegg
  - pharmgkb
  - reactome
  - sider
  - tissues
  - bgee
  - doid
  - uberon
  - cl
  - hgnc
  - chembl
  - chebi
publications:
- id: PMID:29617745
  preferred: true
  title: 'TISSUES 2.0: an integrative web resource on mammalian tissue expression.'
- id: PMID:26244659
  title: Comprehensive comparison of large-scale tissue expression datasets.
repository: https://github.com/opalasca/TISSUES_Update
synonyms:
- TISSUES 2.0
---
# TISSUES

## Overview

TISSUES is a comprehensive, integrative web resource that aggregates and unifies evidence about tissue-specific gene and protein expression in mammals. Developed by the Jensen Lab and maintained at the Swiss Institute of Bioinformatics, University of Zurich, TISSUES provides a weekly-updated platform that combines multiple sources of tissue expression data with confidence scoring and intuitive visualization.

## Data Sources

TISSUES integrates evidence from three main types of sources:

### 1. Manual Curation
- Literature-derived tissue expression annotations
- Expert-curated relationships from published studies
- High-confidence tissue-protein associations

### 2. High-Throughput Data
- Large-scale proteomics screens
- Transcriptomics experiments
- Gene expression profiling studies

### 3. Text Mining
- Automatic extraction from scientific literature
- Co-occurrence analysis of genes/proteins with tissue terms
- Literature-wide association mining

## Data Integration

All evidence is unified through:
- Mapping to common protein identifiers
- Standardization using Brenda Tissue Ontology terms
- Assignment of confidence scores for each evidence type
- Cross-source comparison and integration

## Features

### Visualization
- Schematic human body representation
- Expression patterns displayed on anatomical diagrams
- Intuitive overview of tissue-specific expression

### Confidence Scoring
- Unified scoring system across all evidence types
- Facilitates comparison between different data sources
- Enables assessment of evidence quality and reliability

### Weekly Updates
- Regular incorporation of new literature
- Integration of newly published datasets
- Continuous expansion of coverage

## Use Cases

TISSUES can be used for:
- Identifying tissue-specific expression patterns
- Validating target tissue localization for drug development
- Exploring potential off-target effects
- Comparative analysis across tissues
- Integration into systems biology workflows

## Funding

Supported by the Novo Nordisk Foundation, Danish Council for Independent Research, Innovation Fund Denmark, National Institutes of Health, and CSIRO.

## Development Team

Originally developed by Alberto Santos, Oana Palasca, Christian Stolte, Kalliopi Tsafou, Sune Frankild, Janos Binder, Sean O'Donoghue, Jan Gorodkin, and Lars Juhl Jensen from the Novo Nordisk Foundation Center for Protein Research and collaborating institutions.

Currently maintained by Qingyao Huang at Swiss Institute of Bioinformatics, University of Zurich.