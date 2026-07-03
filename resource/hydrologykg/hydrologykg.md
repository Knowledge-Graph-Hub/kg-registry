---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: torsten.hahmann@maine.edu
  label: Torsten Hahmann
description: The Hydrology KG is the part of the SAWGraph project that describes streams,
  waterbodies and wells and their locations.
domains:
- environment
homepage_url: https://sawgraph.github.io/
id: hydrologykg
layout: resource_detail
name: SAWGraph Hydrology KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SAWGraph Hydrology KG
  format: http
  id: hydrologykg.sparql
  name: SAWGraph Hydrology KG SPARQL
  original_source:
  - source: hydrologykg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/hydrologykg/sparql
- id: hydrologykg.tpf
  name: SAWGraph Hydrology KG TPF
  description: Triple Pattern Fragments endpoint for SAWGraph Hydrology KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/hydrologykg
  original_source:
  - source: hydrologykg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The SAWGraph Hydrology knowledge graph, describing surface water bodies
    (lakes, rivers, wetlands), the flowlines that connect them, and groundwater features
    (aquifers, wells, springs) together with their locations. Surface water bodies
    and flowlines are modeled from USGS NHDPlus data (NHDWaterbody and NHDFlowline);
    groundwater features are drawn primarily from individual state geological surveys
    (for example, the Maine Geological Survey). The RDF (Turtle) graph is served
    through the SAWGraph Hydrology KG SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: hydrologykg.graph
  name: SAWGraph Hydrology Knowledge Graph
  product_url: https://github.com/SAWGraph/water-kg
  original_source:
  - source: hydrologykg
    relation_type: prov:hadPrimarySource
  - source: sawgraph
    relation_type: prov:wasDerivedFrom
  - source: usgs-nhd
    relation_type: prov:hadPrimarySource
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-02T00:00:00Z'
---
SAWGraph Hydrology KG

## Automated Evaluation

- View the automated evaluation: [hydrologykg automated evaluation](hydrologykg_eval_automated.html)
