---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.airfire.org/
  label: USFS AirFire / Pacific Wildland Fire Sciences Laboratory
creation_date: '2026-06-18T00:00:00Z'
description: BlueSky is the U.S. Forest Service AirFire team's wildfire smoke modeling
  framework (NOT the social network of the same name). It chains together fire information,
  fuel loading, consumption, emissions, plume rise, and meteorological dispersion
  models to predict where smoke from wildland fires will travel and how it affects
  ground-level air quality. AirFire operates BlueSky Daily Runs that produce routine
  smoke forecasts, distributed through the AirFire tools portal for fire and air-quality
  decision support. It is developed and maintained by the USFS Pacific Northwest Research
  Station's Pacific Wildland Fire Sciences Laboratory.
domains:
- environment
- public health
- information technology
homepage_url: https://www.airfire.org/
id: bluesky
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: BlueSky Smoke Modeling Framework
products:
- category: GraphicalInterface
  description: AirFire Tools portal providing access to BlueSky Daily Run smoke forecasts,
    the BlueSky Daily Run Viewer, the BlueSky Playground, and related smoke and fire
    products.
  format: http
  id: bluesky.portal
  name: AirFire Tools Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bluesky
  product_url: https://tools.airfire.org/
- category: DocumentationProduct
  description: Source code and documentation for the BlueSky Pipeline, the BlueSky
    smoke modeling framework rearchitected as a pipeable collection of standalone
    modules for fire emissions, plume rise, and smoke dispersion.
  format: http
  id: bluesky.code
  name: BlueSky Pipeline Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bluesky
  product_url: https://github.com/pnwairfire/bluesky
- category: GraphProduct
  description: KnowWhereGraph knowledge graph with 29+ billion RDF triples integrating
    30+ environmental and geospatial data layers accessible through SPARQL endpoint
  edge_count: 29000000000
  format: rdfxml
  id: knowwheregraph.graph
  name: KnowWhereGraph RDF Knowledge Graph
  node_count: 5000000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: knowwheregraph
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: bluesky
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: cdc-svi
  - relation_type: prov:hadPrimarySource
    source: cropland-data-layer
  - relation_type: prov:hadPrimarySource
    source: epa-aqs
  - relation_type: prov:hadPrimarySource
    source: gadm
  - relation_type: prov:hadPrimarySource
    source: gnis
  - relation_type: prov:hadPrimarySource
    source: hifld
  - relation_type: prov:hadPrimarySource
    source: mtbs
  - relation_type: prov:hadPrimarySource
    source: nhpn
  - relation_type: prov:hadPrimarySource
    source: nifc
  - relation_type: prov:hadPrimarySource
    source: noaa-hms
  - relation_type: prov:hadPrimarySource
    source: noaa-ncei
  - relation_type: prov:hadPrimarySource
    source: openfema
  - relation_type: prov:hadPrimarySource
    source: reliefweb
  - relation_type: prov:hadPrimarySource
    source: ssurgo
  - relation_type: prov:hadPrimarySource
    source: us-census
  - relation_type: prov:hadPrimarySource
    source: usdm
  - relation_type: prov:hadPrimarySource
    source: usgs-comcat
  product_url: https://knowwheregraph.org/
---
# BlueSky Smoke Modeling Framework

BlueSky is the U.S. Forest Service AirFire team's framework for modeling wildfire
smoke. It is not related to the Bluesky social network; this is the USFS AirFire
smoke-and-air-quality modeling system. BlueSky links a chain of models -- fire
information, fuel loading, fuel consumption, emissions, plume rise, and
meteorological dispersion -- to predict where smoke from wildland fires travels
and how it degrades ground-level air quality.

AirFire runs BlueSky operationally as the BlueSky Daily Runs, generating routine
smoke forecasts that are distributed through the AirFire tools portal
(tools.airfire.org) alongside related smoke and fire products. The framework is
developed and maintained by the USFS Pacific Northwest Research Station's Pacific
Wildland Fire Sciences Laboratory. BlueSky is an upstream data source for
KnowWhereGraph.