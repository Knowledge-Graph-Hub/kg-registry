---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Andrew Padilla
  contact_details:
  - contact_type: email
    value: apadilla@lincolninst.edu
  - contact_type: github
    value: adplincinst
- category: Individual
  contact_details:
  - contact_type: email
    value: apadilla@lincolninst.edu
  label: Andrew Padilla
description: Geoconnex is an open, community-driven knowledge graph linking U.S. hydrologic
  features to enable seamless water data discovery, access, and collaborative monitoring.
domains:
- environment
homepage_url: https://docs.geoconnex.us/about/intro
id: geoconnex
layout: resource_detail
name: GEOCONNEX
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for GEOCONNEX
  format: http
  id: geoconnex.sparql
  name: GEOCONNEX SPARQL
  original_source:
  - source: geoconnex
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/geoconnex/sparql
- id: geoconnex.tpf
  name: GEOCONNEX TPF
  description: Triple Pattern Fragments endpoint for GEOCONNEX
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/geoconnex
  original_source:
  - source: geoconnex
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The Geoconnex knowledge graph, an open community-contributed RDF graph
    linking U.S. hydrologic features via persistent identifiers. It integrates USGS
    reference features (NHDPlus High Resolution hydrologic units, Watershed Boundary
    Dataset subwatersheds, reference stream gages, and national aquifers) with
    community-contributed feature registries, and is served through the Geoconnex
    SPARQL and Triple Pattern Fragments endpoints.
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
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-02T00:00:00Z'
---
GEOCONNEX

## Automated Evaluation

- View the automated evaluation: [geoconnex automated evaluation](geoconnex_eval_automated.html)
