---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.enhanceratlas.org/
  label: Qian Lab, Johns Hopkins University School of Medicine
creation_date: '2026-06-18T00:00:00Z'
description: EnhancerAtlas is a genome-wide atlas of enhancer annotations spanning
  a large number of human and animal cell and tissue types. The resource integrates
  diverse high-throughput experimental datasets (including histone modifications,
  DNase-seq, transcription factor binding, and other epigenomic signals) to predict
  consensus enhancer regions and infer enhancer-target gene interactions. EnhancerAtlas
  2.0 provides enhancer annotations for 586 tissue and cell types across nine species,
  making it a comprehensive reference for regulatory genomics. It serves as an upstream
  data source for the GenomicKB knowledge graph.
domains:
- genomics
- systems biology
- biological systems
homepage_url: http://www.enhanceratlas.org/
id: enhanceratlas
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: EnhancerAtlas
products:
- category: DataProduct
  description: Downloadable enhancer annotation datasets covering 586 tissue and cell
    types across nine species, including predicted enhancer regions and enhancer-target
    gene interactions, available in BED and related tabular formats.
  id: enhanceratlas.download
  name: EnhancerAtlas 2.0 Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  product_url: http://www.singlecelldb.com/downloadv2.php
- category: GraphicalInterface
  description: A web-based browser for exploring and visualizing enhancer annotations
    by species, tissue, and cell type within the EnhancerAtlas resource.
  id: enhanceratlas.browse
  name: EnhancerAtlas 2.0 Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  product_url: http://www.singlecelldb.com/browse.php
- category: GraphProduct
  description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
  dump_format: neo4j
  format: http
  id: genomickb.graph
  name: GenomicKB Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomickb
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: endb
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  - relation_type: prov:hadPrimarySource
    source: ccre
  - relation_type: prov:hadPrimarySource
    source: fire
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
publications:
- authors:
  - Gao T
  - Qian J
  doi: 10.1093/nar/gkz980
  id: https://pubmed.ncbi.nlm.nih.gov/31740966/
  journal: Nucleic Acids Res
  preferred: true
  title: 'EnhancerAtlas 2.0: an updated resource with enhancer annotation in 586 tissue/cell
    types across nine species'
  year: '2020'
---
# EnhancerAtlas

## Overview

EnhancerAtlas is a genome-wide atlas of enhancer annotations across a broad range of human and animal cell and tissue types. Enhancers are regulatory DNA elements that boost the transcription of their target genes, often from a distance, and identifying them genome-wide is a central challenge in regulatory genomics. EnhancerAtlas addresses this by integrating many independent high-throughput datasets to predict consensus enhancer regions and to link those enhancers to the genes they regulate.

## Data and Coverage

EnhancerAtlas 2.0 provides enhancer annotation in 586 tissue and cell types across nine species. The annotations are derived from the integration of diverse epigenomic and genomic data types, including histone modification profiles, chromatin accessibility (DNase-seq), transcription factor binding, and other regulatory signals. In addition to enhancer locations, the resource provides predicted enhancer-target gene interactions, supporting downstream analyses of gene regulatory networks.

## Access and Use

Enhancer annotation datasets and enhancer-gene interaction data can be downloaded from the EnhancerAtlas download portal, and a web browser interface allows interactive exploration by species, tissue, and cell type. EnhancerAtlas is used as an upstream primary data source for the GenomicKB knowledge graph.

## Citation

When using EnhancerAtlas, please cite Gao T and Qian J, "EnhancerAtlas 2.0: an updated resource with enhancer annotation in 586 tissue/cell types across nine species," Nucleic Acids Research, 2020 (doi:10.1093/nar/gkz980).