---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: katrina.schweikert@maine.edu
  - contact_type: github
    value: kschweikert
  label: Katrina Schweikert
description: The Safe Agricultural Products and Water Graph (SAWGraph) PFAS KG stores
  data on PFAS observations and releases, describing the samples, the geospatial features
  they were taken from, the sampled environmental media, the specific chemical substances
  and the measurement values observed.
domains:
- environment
- chemistry and biochemistry
- agriculture
homepage_url: https://sawgraph.github.io/
id: sawgraph
layout: resource_detail
name: SAWGraph PFAS KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SAWGraph PFAS KG
  format: http
  id: sawgraph.sparql
  name: SAWGraph PFAS KG SPARQL
  original_source:
  - source: sawgraph
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/sawgraph/sparql
- id: sawgraph.tpf
  name: SAWGraph PFAS KG TPF
  description: Triple Pattern Fragments endpoint for SAWGraph PFAS KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/sawgraph
  original_source:
  - source: sawgraph
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The SAWGraph PFAS knowledge graph, integrating PFAS observations and
    releases with the samples, geospatial features, environmental media, and chemical
    substances they describe. The RDF (Turtle) graph is constructed from federal and
    state PFAS datasets and geospatial reference data, and is served through the SAWGraph
    SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: sawgraph.graph
  name: SAWGraph PFAS Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: epa-sdwis
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: water-quality-portal
  - relation_type: prov:hadPrimarySource
    source: epa-ghg
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  - relation_type: prov:hadPrimarySource
    source: maine-egad
  product_url: https://github.com/SAWGraph/pfas-kg
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: epa-echo
  - relation_type: prov:wasInfluencedBy
    source: usgs-nhd
  - relation_type: prov:wasInfluencedBy
    source: us-census
  - relation_type: prov:wasInfluencedBy
    source: knowwheregraph
  - relation_type: prov:wasInfluencedBy
    source: ssurgo
  - relation_type: prov:wasInfluencedBy
    source: cropland-data-layer
repository: https://github.com/sawgraph
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
SAWGraph PFAS graph

## Automated Evaluation

- View the automated evaluation: [sawgraph automated evaluation](sawgraph_eval_automated.html)
