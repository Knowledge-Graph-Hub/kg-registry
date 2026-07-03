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
creation_date: '2025-12-08T00:00:00Z'
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
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: SAWGraph PFAS KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SAWGraph PFAS KG
  format: http
  id: sawgraph.sparql
  name: SAWGraph PFAS KG SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sawgraph
  product_url: https://apps.okn.us/sawgraph/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for SAWGraph PFAS KG
  id: sawgraph.tpf
  name: SAWGraph PFAS KG TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sawgraph
  product_url: https://apps.okn.us/ldf/sawgraph
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
- category: GraphProduct
  description: The SAWGraph Facilities and Industries Ontology (FIO) / Facility Registry
    Service (FRS) knowledge graph, an RDF (Turtle) graph representing US facilities
    from EPA's Facility Registry Service together with their NAICS and SIC industry
    classifications and spatial locations. It is served through the SAWGraph FRS SPARQL
    and Triple Pattern Fragments endpoints.
  format: ttl
  id: fiokg.graph
  name: SAWGraph FRS Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fiokg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  product_url: https://github.com/SAWGraph/fio
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: naics
  - relation_type: prov:wasInfluencedBy
    source: sic
- category: GraphProduct
  description: The SAWGraph Hydrology knowledge graph, describing surface water bodies
    (lakes, rivers, wetlands), the flowlines that connect them, and groundwater features
    (aquifers, wells, springs) together with their locations. Surface water bodies
    and flowlines are modeled from USGS NHDPlus data (NHDWaterbody and NHDFlowline);
    groundwater features are drawn primarily from individual state geological surveys
    (for example, the Maine Geological Survey). The RDF (Turtle) graph is served through
    the SAWGraph Hydrology KG SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: hydrologykg.graph
  name: SAWGraph Hydrology Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hydrologykg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: usgs-nhd
  product_url: https://github.com/SAWGraph/water-kg
- category: GraphProduct
  description: The SAWGraph Spatial KG as an RDF (Turtle) graph. It contains all Level
    13 grid cells from the S2 grid together with administrative regions of levels
    1 to 3 (states, counties, and county subdivisions) and the spatial relationships
    between them for the 48 contiguous U.S. states. S2 grid cells and state/county
    geometries are taken from KnowWhereGraph, and county subdivisions are sourced
    from the US Census Bureau. The graph is served through the SAWGraph Spatial KG
    SPARQL and Triple Pattern Fragments endpoints.
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
repository: https://github.com/sawgraph
---
SAWGraph PFAS graph

## Automated Evaluation

- View the automated evaluation: [sawgraph automated evaluation](sawgraph_eval_automated.html)