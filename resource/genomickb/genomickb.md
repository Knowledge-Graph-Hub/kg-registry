---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: wyq@umich.edu
    label: Yiqun Wang
  - category: Individual
    contact_details:
      - contact_type: email
        value: drjieliu@umich.edu
    label: Jie Liu
description: Genomic Knowledgebase (GenomicKB) is a database that uses a knowledge graph to consolidate genomic datasets and annotations. GenomicKB integrates data from more than 30 consortia, in which the genomic entities and relationships are represented as diverse nodes and edges with properties.
domains:
  - biological systems
  - genomics
  - biomedical
homepage_url: https://gkb.dcmb.med.umich.edu/
id: genomickb
layout: resource_detail
license:
  id: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome#modal-licence-preview
  label: PolyForm Noncommercial License 1.0.0
name: GenomicKB
products:
  - category: GraphicalInterface
    description: Graphical interface for GenomicKB
    id: genomickb.site
    name: GenomicKB Site
    original_source:
      - source: genomickb
        relation_type: prov:hadPrimarySource
    product_url: https://gkb.dcmb.med.umich.edu/search
  - category: GraphProduct
    description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
    dump_format: neo4j
    id: genomickb.graph
    name: GenomicKB Graph Dump
    original_source:
      - source: genomickb
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: epd
        relation_type: prov:hadPrimarySource
      - source: dbsuper
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: dgv
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: encode
        relation_type: prov:hadPrimarySource
      - source: fantom5
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: dbvar
        relation_type: prov:hadPrimarySource
      - source: endb
        relation_type: prov:hadPrimarySource
      - source: enhanceratlas
        relation_type: prov:hadPrimarySource
    product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
creation_date: '2025-03-20T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---

GenomicKB

## Evaluation

- View the evaluation: [genomickb evaluation](genomickb_eval.html)
