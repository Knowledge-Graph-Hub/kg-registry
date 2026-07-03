---
category: GraphProduct
description: The Geoconnex knowledge graph, an open community-contributed RDF graph
  linking U.S. hydrologic features via persistent identifiers. It integrates USGS
  reference features (NHDPlus High Resolution hydrologic units, Watershed Boundary
  Dataset subwatersheds, reference stream gages, and national aquifers) with community-contributed
  feature registries, and is served through the Geoconnex SPARQL and Triple Pattern
  Fragments endpoints.
format: ttl
id: geoconnex.graph
name: GEOCONNEX Knowledge Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: geoconnex
- relation_type: prov:hadPrimarySource
  source: usgs-nhd
- relation_type: prov:hadPrimarySource
  source: usgs-nwis
product_url: https://github.com/internetofwater/geoconnex.us
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: epa-sdwis
- relation_type: prov:wasInfluencedBy
  source: us-census
layout: product_detail
---
