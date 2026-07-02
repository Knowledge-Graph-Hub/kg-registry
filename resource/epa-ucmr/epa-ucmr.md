---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/dwucmr
  label: US Environmental Protection Agency
creation_date: '2026-07-01T00:00:00Z'
description: The Unregulated Contaminant Monitoring Rule (UCMR) program directs the
  US Environmental Protection Agency to collect nationally representative occurrence
  data for contaminants that are not yet regulated in public drinking water systems.
  The fifth cycle (UCMR 5) requires monitoring for 29 per- and polyfluoroalkyl substances
  (PFAS) and lithium, producing sampling results reported by public water systems
  across the United States. SAWGraph uses UCMR PFAS monitoring results as a primary
  source for PFAS occurrence in drinking water.
domains:
- environment
- public health
- chemistry and biochemistry
homepage_url: https://www.epa.gov/dwucmr
id: epa-ucmr
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: EPA Unregulated Contaminant Monitoring Rule (UCMR)
products:
- category: GraphicalInterface
  description: EPA landing page for the Unregulated Contaminant Monitoring Rule program,
    describing monitoring cycles, contaminant lists, and access to occurrence data.
  format: http
  id: epa-ucmr.landing
  name: EPA UCMR landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  product_url: https://www.epa.gov/dwucmr
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
---
## Description

The Unregulated Contaminant Monitoring Rule (UCMR) program directs the US
Environmental Protection Agency to collect nationally representative occurrence
data for contaminants not yet regulated in public drinking water systems. UCMR 5
requires monitoring for 29 per- and polyfluoroalkyl substances (PFAS) and lithium.

SAWGraph uses UCMR PFAS monitoring results as a primary source for PFAS
occurrence in drinking water.