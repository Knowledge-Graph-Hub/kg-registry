---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.fhwa.dot.gov/planning/processes/tools/nhpn/
  label: Federal Highway Administration (FHWA), U.S. Department of Transportation
creation_date: '2026-06-18T00:00:00Z'
description: The National Highway Planning Network (NHPN) is a geospatial network
  database of line features representing just over 450,000 miles of highways across
  the United States, maintained by the Federal Highway Administration (FHWA) of the
  U.S. Department of Transportation. It includes the National Highway System (NHS),
  the Interstate System, the Strategic Highway Network (STRAHNET), NHS Intermodal
  Connectors, and all roads classified as principal or rural minor arterial. The data
  is assembled from road networks submitted by State Departments of Transportation
  as part of their Highway Performance Monitoring System (HPMS) submissions. NHPN
  is used as an upstream geospatial source for KnowWhereGraph.
domains:
- environment
- information technology
- general
homepage_url: https://www.fhwa.dot.gov/planning/processes/tools/nhpn/
id: nhpn
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. federal government work (public domain)
name: National Highway Planning Network
products:
- category: Product
  description: NHPN version 14.05 distributed as zipped GeoJSON, containing the geospatial
    line features for the national highway network.
  format: json
  id: nhpn.geojson
  name: NHPN GeoJSON edition
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpn
  product_file_size: 127105820
  product_url: https://www.fhwa.dot.gov/planning/processes/tools/nhpn/2015/nhpnv14-05geojson.zip
- category: Product
  description: NHPN version 14.05 distributed as a zipped Esri Shapefile (a bundle
    of several files), containing the geospatial line features for the national highway
    network.
  format: mixed
  id: nhpn.shp
  name: NHPN Shapefile edition
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpn
  product_file_size: 182540623
  product_url: https://www.fhwa.dot.gov/planning/processes/tools/nhpn/2015/nhpnv14-05shp.zip
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
## Description

The National Highway Planning Network (NHPN) is a geospatial network database
maintained by the Federal Highway Administration (FHWA), an agency of the U.S.
Department of Transportation. It contains line features representing just over
450,000 miles of U.S. highways, including the National Highway System (NHS), the
Interstate System, the Strategic Highway Network (STRAHNET), NHS Intermodal
Connectors, and all roads classified as principal or rural minor arterial.

The network is assembled from road data submitted by State Departments of
Transportation through the Highway Performance Monitoring System (HPMS). It
supports NHS mapping, freight-flow modeling (Freight Analysis Framework), and the
Highway Economic Requirements System - State Version (HERS-ST). NHPN serves as an
upstream geospatial data source for KnowWhereGraph.

The current version (14.05) is available for download as Shapefile, GML, KML, and
GeoJSON.

**Domains**: environment, information technology, general