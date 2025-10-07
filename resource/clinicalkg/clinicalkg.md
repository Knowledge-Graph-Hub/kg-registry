---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/MannLabs
  label: Mann Labs
description: The Clinical Knowledge Graph (CKG) is an open-source platform that integrates
  proteomics and clinical data with knowledge from diverse biomedical databases and
  literature to support precision medicine. The CKG has reported scale of ~16 million
  nodes and ~220 million relationships and provides tooling for analysis, reporting,
  and knowledge discovery.
domains:
- clinical
- proteomics
- biomedical
- health
homepage_url: https://ckg.readthedocs.io/
id: clinicalkg
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: Clinical Knowledge Graph (CKG)
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
publications:
- authors:
  - Alberto Santos
  - "Ana R. Cola\xE7o"
  - Annelaura B. Nielsen
  - Matthias Mann
  doi: 10.1101/2020.05.09.084897
  id: doi:10.1101/2020.05.09.084897
  journal: bioRxiv
  title: Clinical Knowledge Graph Integrates Proteomics Data into Clinical Decision-Making
  year: '2020'
repository: https://github.com/MannLabs/CKG
---
Clinical Knowledge Graph

## Evaluation

- View the evaluation: [clinicalkg evaluation](clinicalkg_eval.html)
