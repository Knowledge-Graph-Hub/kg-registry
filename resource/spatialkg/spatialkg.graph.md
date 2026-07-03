---
category: GraphProduct
description: The SAWGraph Spatial KG as an RDF (Turtle) graph. It contains all Level
  13 grid cells from the S2 grid together with administrative regions of levels 1
  to 3 (states, counties, and county subdivisions) and the spatial relationships between
  them for the 48 contiguous U.S. states. S2 grid cells and state/county geometries
  are taken from KnowWhereGraph, and county subdivisions are sourced from the US Census
  Bureau. The graph is served through the SAWGraph Spatial KG SPARQL and Triple Pattern
  Fragments endpoints.
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
layout: product_detail
---
