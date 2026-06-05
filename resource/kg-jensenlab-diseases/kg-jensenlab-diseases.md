---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: colxu@scripps.edu
  - contact_type: github
    value: colleenXu
  label: Colleen Xu
creation_date: '2025-05-06T00:00:00Z'
description: An ingest of Jensen Lab's DISEASES resource, for Translator use (output
  in Translator standards and NodeNormed, using own custom pipeline)
domains:
- biomedical
homepage_url: https://github.com/biothings/pending.api/tree/translator-output/plugins/DISEASES
id: kg-jensenlab-diseases
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: JensenLab DISEASES KG
products:
- category: DocumentationProduct
  description: Translator plugin repository directory for the JensenLab DISEASES ingest,
    including parser code, metadata, and generated outputs.
  format: http
  id: kg-jensenlab-diseases.docs
  name: JensenLab DISEASES Translator Plugin
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  product_url: https://github.com/biothings/pending.api/tree/translator-output/plugins/DISEASES
- category: GraphProduct
  description: KGX nodes file for JensenLab DISEASES KG
  format: kgx-jsonl
  id: kg-jensenlab-diseases.nodes.kgx
  name: DISEASES KGX nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  product_file_size: 130
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_kgx_nodes.jsonl
- category: GraphProduct
  description: KGX edges file for JensenLab DISEASES KG
  format: kgx-jsonl
  id: kg-jensenlab-diseases.edges.kgx
  name: DISEASES KGX edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  product_file_size: 132
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_kgx_edges.jsonl
- category: GraphProduct
  description: TRAPI edges file for JensenLab DISEASES KG
  format: trapi-jsonl
  id: kg-jensenlab-diseases.edges.trapi
  name: DISEASES TRAPI edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  product_file_size: 132
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_trapi_edges.jsonl
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
repository: https://github.com/biothings/pending.api/tree/translator-output/plugins/DISEASES
---
# JensenLab DISEASES KG

JensenLab DISEASES KG is a Translator-oriented ingest of the Jensen Lab DISEASES
resource, produced in Translator-compatible output formats through a custom
plugin pipeline. The page captures the exported KGX and TRAPI-style artifacts for
this derived graph representation rather than the upstream DISEASES resource
itself.

The owned products here point to the plugin implementation and generated graph
files. The propagated `enrichr-kg` product is preserved because it cites this
resource as one of many upstream contributors in a downstream integrated graph.

## Automated Evaluation

- View the automated evaluation: [kg-jensenlab-diseases automated evaluation](kg-jensenlab-diseases_eval_automated.html)