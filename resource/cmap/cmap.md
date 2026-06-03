---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: cmap@broadinstitute.org
  - contact_type: url
    value: https://www.broadinstitute.org/connectivity-map-cmap
  id: broad
  label: Broad Institute
creation_date: '2025-01-10T00:00:00Z'
description: The Connectivity Map (CMap) is a groundbreaking genome-scale perturbation
  resource containing over 3 million gene expression profiles cataloging transcriptional
  responses to chemical, genetic, and disease perturbations across multiple cancer
  cell types. Developed by the Broad Institute as part of the NIH Library of Integrated
  Network-Based Cellular Signatures (LINCS) program, CMap addresses fundamental challenges
  in understanding protein function and small molecule mechanisms of action by creating
  a comprehensive catalog of cellular signatures representing systematic perturbation.
  The database employs the L1000 high-throughput gene expression assay, which directly
  measures ~978 landmark genes and computationally infers expression of ~11,350 additional
  genes using inference algorithms, providing a cost-effective reduced representation
  of the transcriptome. CMap contains signatures from approximately 5,000 small-molecule
  compounds, 3,000 genetic reagents including shRNAs, CRISPR knockdowns, and overexpression
  constructs, tested primarily across nine core cancer cell lines that include A375,
  A549, HA1E, HCC515, HT29, HEPG2, MCF7, PC3, and VCAP. The resource enables researchers
  to query with their own gene expression signatures to identify perturbagens that
  induce similar or opposing transcriptional responses, thereby discovering unexpected
  connections between diseases, drug mechanisms, and protein functions. CMap data
  is accessible through CLUE, a cloud-based unified environment providing user-friendly
  web applications including query tools, data browsers, metadata search, and visualization
  apps for exploring perturbation-driven gene expression patterns. The database supports
  diverse research applications including drug repurposing by identifying compounds
  with similar mechanisms, target identification by finding small molecules that mimic
  genetic perturbations, disease mechanism understanding by connecting disease signatures
  to perturbagen responses, and biomarker discovery through systematic analysis of
  transcriptional responses. While personalized support ended in July 2022, all data,
  tools, and extensive documentation through Connectopedia remain fully accessible,
  with over 1.5 million replicate-collapsed signatures and 3 million profiles available
  for download and programmatic access via Python libraries and APIs.
domains:
- genomics
- drug discovery
- pharmacology
homepage_url: https://clue.io/
id: cmap
infores_id: cmap
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://clue.io/connectopedia/terms
  label: CLUE Terms of Use
name: Connectivity Map
products:
- category: GraphicalInterface
  description: Cloud-based user interface providing suite of apps for querying gene
    expression signatures, browsing perturbagen data, searching metadata, and visualizing
    connectivity results
  format: http
  id: cmap.clue
  name: CLUE Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: ProgrammingInterface
  description: Python library cmapBQ for programmatic access to CMap data through
    Google BigQuery with query capabilities for signatures and metadata
  format: http
  id: cmap.python_api
  is_public: true
  name: cmapBQ Python Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://cmapbq.readthedocs.io/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: GraphicalInterface
  description: Query app enabling users to search CMap database with custom gene expression
    signatures to find perturbagens with similar or opposing transcriptional effects
  format: http
  id: cmap.query_app
  name: CLUE Query App
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/query
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: Product
  description: Data releases containing replicate-collapsed signatures and gene expression
    profiles in GCTx matrix format available for download
  format: hdf5
  id: cmap.data_downloads
  name: CMap Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/releases/data-dashboard
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: DocumentationProduct
  description: Comprehensive knowledge base containing glossary, tutorials, analytical
    methods, experimental protocols, and detailed documentation
  format: http
  id: cmap.connectopedia
  name: Connectopedia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/connectopedia
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
publications:
- id: https://doi.org/10.1016/j.cell.2017.10.049
  title: 'A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000
    Profiles'
repository: https://github.com/cmap
synonyms:
- CMap
- Connectivity Map
- LINCS L1000
taxon:
- NCBITaxon:9606
---
# Connectivity Map

## Overview

The Connectivity Map (CMap) is a genome-scale library of cellular signatures that catalogs transcriptional responses to chemical, genetic, and disease perturbations, enabling systematic exploration of connections between diseases, drugs, and genes through over 3 million gene expression profiles.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cmap`