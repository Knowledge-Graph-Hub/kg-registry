---
category: GraphProduct
description: The SAWGraph Hydrology knowledge graph, describing surface water bodies
  (lakes, rivers, wetlands), the flowlines that connect them, and groundwater features
  (aquifers, wells, springs) together with their locations. Surface water bodies and
  flowlines are modeled from USGS NHDPlus data (NHDWaterbody and NHDFlowline); groundwater
  features are drawn primarily from individual state geological surveys (for example,
  the Maine Geological Survey). The RDF (Turtle) graph is served through the SAWGraph
  Hydrology KG SPARQL and Triple Pattern Fragments endpoints.
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
layout: product_detail
---
