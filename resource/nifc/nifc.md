---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nifc.gov/
  label: National Interagency Fire Center
creation_date: '2026-06-18T00:00:00Z'
description: NIFC Open Data is the public geospatial data hub of the National Interagency
  Fire Center, the U.S. interagency coordination center for wildland fire support
  based in Boise, Idaho. Hosted on an Esri ArcGIS Open Data portal, it publishes authoritative
  wildfire data including current and historical incident locations, fire perimeters,
  and related operational layers from the Wildland Fire Interagency Geospatial Services
  (WFIGS) program. The data serve as an upstream source for downstream knowledge graphs
  such as KnowWhereGraph.
domains:
- environment
- general
homepage_url: https://data-nifc.opendata.arcgis.com/
id: nifc
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain (no copyright)
name: National Interagency Fire Center Open Data
products:
- category: Product
  description: WFIGS current interagency fire perimeters, providing polygon geometries
    for active and recent wildfire incidents across the United States, downloadable
    in multiple geospatial formats and available as a hosted feature service.
  format: json
  id: nifc.fire-perimeters
  name: WFIGS Current Interagency Fire Perimeters
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nifc
  product_url: https://data-nifc.opendata.arcgis.com/datasets/wfigs-current-interagency-fire-perimeters
- category: GraphicalInterface
  description: NIFC Open Data portal interface for searching, browsing, previewing
    on maps, and downloading wildfire geospatial datasets and feature layers.
  format: http
  id: nifc.portal
  is_public: true
  name: NIFC Open Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nifc
  product_url: https://data-nifc.opendata.arcgis.com/
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
# National Interagency Fire Center Open Data

## Overview

NIFC Open Data is the open geospatial data portal of the National Interagency Fire Center (NIFC), the United States interagency hub for wildland fire coordination, planning, and logistics located on a 55-acre campus in Boise, Idaho. The portal is built on Esri's ArcGIS Open Data (Hub) platform and exposes authoritative wildfire datasets to the public.

## Data Content

The portal publishes wildfire-related geospatial layers from the Wildland Fire Interagency Geospatial Services (WFIGS) program and partner agencies, including:

- Current and historical wildfire incident locations
- Current and historical interagency fire perimeters
- Operational and situational support layers used by fire personnel and emergency services

Datasets are downloadable in common geospatial formats (GeoJSON, shapefile, CSV, KML) and are also served as live ArcGIS feature services.

## Access and License

Data are produced by U.S. federal agencies and are generally in the public domain (no copyright) within the United States. The portal provides web-based search, map preview, and direct download, plus programmatic access through ArcGIS REST feature services.

## Relationship to Other Resources

NIFC Open Data is an upstream primary source feeding downstream geospatial knowledge graphs, notably KnowWhereGraph, which integrates wildfire hazard layers among its many environmental data sources.