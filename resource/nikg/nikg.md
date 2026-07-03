---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jinggao@purdue.edu
  label: Jing Gao
description: Neighborhood Information KG (NIKG) is a knowledge graph warehouse for
  neighborhood information.
domains:
- public health
homepage_url: https://frink.renci.org/registry/kgs/neighborhood-kg/
id: nikg
layout: resource_detail
name: Neighborhood Information KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for Neighborhood Information KG
  format: http
  id: nikg.sparql
  name: Neighborhood Information KG SPARQL
  original_source:
  - source: nikg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/nikg/sparql
- id: nikg.tpf
  name: Neighborhood Information KG TPF
  description: Triple Pattern Fragments endpoint for Neighborhood Information KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/nikg
  original_source:
  - source: nikg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The Neighborhood Information KG (NIKG) RDF graph, a knowledge graph warehouse
    integrating neighborhood-level information such as demographics, land use, local
    incidents and injuries, and proximity to trauma centers. Built from census data
    and other neighborhood-level records, the graph is served in RDF (Turtle) through
    the NIKG SPARQL and Triple Pattern Fragments endpoints hosted on the FRINK / Proto-OKN
    infrastructure.
  format: ttl
  id: nikg.graph
  is_public: true
  name: Neighborhood Information KG RDF Graph
  original_source:
  - source: nikg
    relation_type: prov:hadPrimarySource
  - source: us-census
    relation_type: prov:hadPrimarySource
  product_url: https://frink.renci.org/registry/kgs/neighborhood-kg/
  secondary_source:
  - source: nij
    relation_type: prov:wasInfluencedBy
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-03T00:00:00Z'
---
Neighborhood Information KG

## Automated Evaluation

- View the automated evaluation: [nikg automated evaluation](nikg_eval_automated.html)
