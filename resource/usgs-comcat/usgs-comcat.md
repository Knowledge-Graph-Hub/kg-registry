---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.usgs.gov/programs/earthquake-hazards
  label: U.S. Geological Survey (USGS) Earthquake Hazards Program
creation_date: '2026-06-18T00:00:00Z'
description: The Advanced National Seismic System (ANSS) Comprehensive Earthquake
  Catalog (ComCat) is the U.S. Geological Survey's authoritative catalog of earthquake
  events. It aggregates seismic event records contributed by ANSS networks and other
  sources, including event origins (location, depth, and time), magnitudes, and associated
  phase and product data. ComCat is accessible through a web-based earthquake search
  interface and a programmatic FDSN-standard event web service, and serves as an upstream
  source for the KnowWhereGraph.
domains:
- environment
- general
- information technology
homepage_url: https://earthquake.usgs.gov/data/comcat/
id: usgs-comcat
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. federal government public domain
name: USGS Comprehensive Earthquake Catalog (ComCat)
products:
- category: GraphicalInterface
  description: Web interface for searching and downloading earthquake events from
    ComCat by time, location, magnitude, and other parameters
  format: http
  id: usgs-comcat.search
  name: USGS Earthquake Catalog Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs-comcat
  product_url: https://earthquake.usgs.gov/earthquakes/search/
- category: ProgrammingInterface
  description: FDSN-standard event web service providing programmatic query access
    to ComCat earthquake events, origins, and magnitudes in multiple formats
  format: http
  id: usgs-comcat.fdsnws
  name: USGS FDSN Event Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs-comcat
  product_url: https://earthquake.usgs.gov/fdsnws/event/1/
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
# USGS Comprehensive Earthquake Catalog (ComCat)

## Overview

The Advanced National Seismic System (ANSS) Comprehensive Earthquake Catalog (ComCat) is maintained by the U.S. Geological Survey (USGS) Earthquake Hazards Program. It is an authoritative catalog of earthquake events, combining seismic records from contributing ANSS networks and other sources. Each entry includes event origins (location, depth, and origin time), magnitudes, and associated phase and product information.

## Access

- Search interface: query and download events by time, location, magnitude, and other parameters at the USGS earthquake search page
- FDSN event web service: programmatic, standards-based access to event, origin, and magnitude data in multiple output formats

## Related resources

ComCat serves as an upstream source for the KnowWhereGraph.

## Terms and citation

ComCat is produced by the U.S. Geological Survey, a U.S. federal agency; its data are generally in the U.S. public domain. Please attribute the USGS Earthquake Hazards Program when using the catalog.