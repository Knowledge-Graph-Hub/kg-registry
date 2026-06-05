---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://github.com/MannLabs
    label: Mann Labs
description: The Clinical Knowledge Graph (CKG) is an open-source platform that integrates proteomics and clinical data with knowledge from diverse biomedical databases and literature to support precision medicine. The CKG has reported scale of ~16 million nodes and ~220 million relationships and provides tooling for analysis, reporting, and knowledge discovery.
domains:
  - clinical
  - proteomics
  - biomedical
homepage_url: https://ckg.readthedocs.io/
id: clinicalkg
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: Clinical Knowledge Graph (CKG)
products:
  - category: DocumentationProduct
    description: Project documentation for installation, graph building, querying, reporting, and API usage.
    format: http
    id: clinicalkg.docs
    name: CKG Documentation
    original_source:
      - source: clinicalkg
        relation_type: prov:hadPrimarySource
    product_url: https://ckg.readthedocs.io/
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: clinicalkg
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - Alberto Santos
      - "Ana R. Colaço"
      - Annelaura B. Nielsen
      - Matthias Mann
    doi: 10.1101/2020.05.09.084897
    id: doi:10.1101/2020.05.09.084897
    journal: bioRxiv
    title: Clinical Knowledge Graph Integrates Proteomics Data into Clinical Decision-Making
    year: '2020'
repository: https://github.com/MannLabs/CKG
taxon:
  - NCBITaxon:9606
creation_date: '2025-08-12T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
---

Clinical Knowledge Graph

## Overview

CKG is both a biomedical knowledge graph and an analysis platform for integrating proteomics experiments with curated biomedical databases and literature-derived knowledge.

The public project documentation covers graph construction, database querying, project reports, notebooks, and API-level extension points, complementing the downloadable Neo4j dump already listed on this page.

## Evaluation

- View the evaluation: [clinicalkg evaluation](clinicalkg_eval.html)
