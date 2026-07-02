---
category: GraphProduct
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
layout: product_detail
---
