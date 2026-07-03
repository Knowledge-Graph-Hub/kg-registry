---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: david.kedrowski@maine.edu
  - contact_type: github
    value: dkedrowski
  label: David Kedrowski
description: The SAWGraph Spatial KG is part of the Safe Agricultural Products and
  Water Graph (SAWGraph) project. It contains all the Level 13 grid cells from the
  S2 grid as well as administrative regions of levels 1 to 3 (states, counties, and
  county subdivisions) and the spatial relationships between them for the 48 contiguous
  states in the U.S.
domains:
- environment
homepage_url: https://sawgraph.github.io/
id: spatialkg
layout: resource_detail
name: SAWGraph Spatial KG
products:
- category: GraphProduct
  description: The SAWGraph Spatial KG as an RDF (Turtle) graph. It contains all Level
    13 grid cells from the S2 grid together with administrative regions of levels 1
    to 3 (states, counties, and county subdivisions) and the spatial relationships
    between them for the 48 contiguous U.S. states. S2 grid cells and state/county
    geometries are taken from KnowWhereGraph, and county subdivisions are sourced from
    the US Census Bureau. The graph is served through the SAWGraph Spatial KG SPARQL
    and Triple Pattern Fragments endpoints.
  format: ttl
  id: spatialkg.graph
  name: SAWGraph Spatial KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spatialkg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  product_url: https://github.com/SAWGraph/geospatial-kg
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: knowwheregraph
  - relation_type: prov:wasInfluencedBy
    source: us-census
- category: ProgrammingInterface
  description: SPARQL endpoint for SAWGraph Spatial KG
  format: http
  id: spatialkg.sparql
  name: SAWGraph Spatial KG SPARQL
  original_source:
  - source: spatialkg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/spatialkg/sparql
- id: spatialkg.tpf
  name: SAWGraph Spatial KG TPF
  description: Triple Pattern Fragments endpoint for SAWGraph Spatial KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/spatialkg
  original_source:
  - source: spatialkg
    relation_type: prov:hadPrimarySource
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-02T00:00:00Z'
---
SAWGraph Spatial KG

## Automated Evaluation

- View the automated evaluation: [spatialkg automated evaluation](spatialkg_eval_automated.html)
