---
activity_status: active
category: Aggregator
creation_date: '2025-08-12T00:00:00Z'
description: "PhosphoSitePlus is a comprehensive resource for experimentally validated\
  \ post-translational modifications (PTMs) with emphasis on phosphorylation, ubiquitination,\
  \ acetylation, methylation and more. It aggregates curated site-specific modification\
  \ data, kinase\u2013substrate relationships, protein domains, mutation impact annotations,\
  \ sequence motifs, and pathway/interaction context to support signaling, proteomics,\
  \ and systems biology research."
domains:
- proteomics
- biomedical
- biological systems
homepage_url: https://www.phosphosite.org/
id: phosphositeplus
last_modified_date: '2025-09-11T00:00:00Z'
layout: resource_detail
name: PhosphoSitePlus
products:
- category: GraphicalInterface
  description: "Web portal for browsing PTM sites, kinase\u2013substrate relationships,\
    \ motifs, mutations and protein pages"
  format: http
  id: phosphositeplus.portal
  name: PhosphoSitePlus Portal
  product_url: https://www.phosphosite.org/
- category: Product
  description: "Bulk data downloads (PTM site tables, kinase\u2013substrate data,\
    \ regulatory sites, disease-associated mutations) requiring agreement to terms"
  format: http
  id: phosphositeplus.downloads
  name: PhosphoSitePlus Downloads
  product_url: https://www.phosphosite.org/staticDownloads
- category: DocumentationProduct
  description: Methodology and curation overview including data sources and evidence
    criteria
  format: http
  id: phosphositeplus.about
  name: PhosphoSitePlus About & Methods
  product_url: https://www.phosphosite.org/staticAboutPhosphosite
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
  - do
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
publications:
- doi: 10.1093/nar/gku1267
  id: doi:10.1093/nar/gku1267
  journal: Nucleic Acids Research
  title: 'PhosphoSitePlus, 2014: mutations, PTMs and recalibrations.'
  year: '2014'
---
# PhosphoSitePlus

## Overview

PhosphoSitePlus aggregates high-quality experimentally validated post-translational modification (PTM) information, including phosphorylation, ubiquitination, acetylation, methylation, SUMOylation and others. Each modification site is annotated with residue position, surrounding sequence context, upstream enzymes (where known), literature references, and functional notes.

## Access

- Portal: interactive protein and site search, motif analysis, kinase–substrate browsing
- Downloads: bulk flat files for PTM sites, kinase–substrate pairs, regulatory and disease-associated annotations
- About/Methods: curation policies, evidence sources, data model explanation

## Citation

Please cite the latest PhosphoSitePlus update and foundational 2011 description paper when using the resource.