---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/ghgreporting
  label: US Environmental Protection Agency
creation_date: '2026-07-01T00:00:00Z'
description: The US Environmental Protection Agency's Greenhouse Gas Reporting Program
  (GHGRP) collects annual greenhouse gas data from large emitting facilities, suppliers,
  and other sources across the United States. It includes fluorinated greenhouse gas
  emissions and supplies, some of which involve per- and polyfluoroalkyl substances
  (PFAS) and related fluorinated chemistry, reported by facility with location, chemical
  identity, and emission amounts. SAWGraph uses GHGRP facility emission data, obtained
  through the EPA PFAS Analytic Tools, as a primary source for PFAS-related releases
  from industrial facilities.
domains:
- environment
- chemistry and biochemistry
homepage_url: https://www.epa.gov/ghgreporting
id: epa-ghg
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: EPA Greenhouse Gas Reporting Program (GHGRP)
products:
- category: GraphicalInterface
  description: EPA landing page for the Greenhouse Gas Reporting Program, describing
    reported emissions data, tools, and downloads.
  format: http
  id: epa-ghg.landing
  name: EPA GHGRP landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-ghg
  product_url: https://www.epa.gov/ghgreporting
- category: GraphicalInterface
  description: EPA page providing fluorinated greenhouse gas emissions and supplies
    data reported to the GHGRP.
  format: http
  id: epa-ghg.fgas
  name: Fluorinated GHG Emissions and Supplies
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-ghg
  product_url: https://www.epa.gov/ghgreporting/fluorinated-greenhouse-gas-emissions-and-supplies-reported-ghgrp
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

The US Environmental Protection Agency's Greenhouse Gas Reporting Program
(GHGRP) collects annual greenhouse gas data from large emitting facilities and
suppliers across the United States, including fluorinated greenhouse gas
emissions and supplies reported by facility with location, chemical identity,
and emission amounts.

SAWGraph uses GHGRP facility emission data, obtained through the EPA PFAS
Analytic Tools, as a primary source for PFAS-related releases from industrial
facilities.