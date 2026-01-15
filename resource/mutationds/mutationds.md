---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.cancergenomeinterpreter.org/
  - contact_type: email
    value: cancerinterpreter@irbbarcelona.org
  id: cgi-team
  label: Cancer Genome Interpreter Team
creation_date: '2025-08-12T00:00:00Z'
description: The Catalog of Validated Oncogenic Mutations is part of the Cancer Genome
  Interpreter and contains a compiled inventory of mutations in cancer genes that
  are demonstrated to drive tumor growth or predispose to cancer, combining data from
  DoCM, ClinVar, OncoKB, and experimental assays.
domains:
- genomics
- biomedical
homepage_url: https://www.cancergenomeinterpreter.org/mutations
id: mutationds
last_modified_date: '2026-01-15T00:00:00Z'
layout: resource_detail
name: Catalog of Validated Oncogenic Mutations
products:
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
publications:
- category: Publication
  id: PMID:34090623
  preferred: true
synonyms:
- MutationDS
- CGI Mutations
warnings:
- ClinicalKG dump includes mutationds as one of many integrated sources; the dedicated
  mutation catalog is maintained under Cancer Genome Interpreter.
---
# Mutationds