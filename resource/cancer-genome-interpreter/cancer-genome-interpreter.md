---
activity_status: active
category: DataSource
creation_date: '2025-08-12T00:00:00Z'
description: Cancer Genome Interpreter (CGI) is a resource that annotates tumor genomic alterations to identify likely oncogenic events and interpret their potential therapeutic, prognostic, and diagnostic relevance using curated knowledge bases, machine learning (BoostDM, OncodriveMUT), and clinical evidence levels.
domains:
  - biomedical
  - clinical
  - precision medicine
  - drug discovery
id: cancer-genome-interpreter
last_modified_date: '2025-09-16T00:00:00Z'
layout: resource_detail
name: Cancer Genome Interpreter
license:
  id: https://www.cancergenomeinterpreter.org/conditions#license
  label: Cancer Genome Interpreter License and Terms
products:
- category: GraphicalInterface
  description: Web portal for submitting variant lists, interpreting oncogenicity, and exploring biomarkers
  format: http
  id: cancer-genome-interpreter.portal
  name: Cancer Genome Interpreter Portal
  product_url: https://www.cancergenomeinterpreter.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to annotation and interpretation endpoints
  format: http
  id: cancer-genome-interpreter.api
  name: Cancer Genome Interpreter REST API
  product_url: https://www.cancergenomeinterpreter.org/rest_api
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
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
---
# Cancer Genome Interpreter

Cancer Genome Interpreter provides annotation and interpretation of somatic tumor alterations, integrating oncogenicity prediction and clinical actionability evidence.