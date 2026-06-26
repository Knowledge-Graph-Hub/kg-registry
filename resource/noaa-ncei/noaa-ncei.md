---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncei.noaa.gov/contact
  label: NOAA National Centers for Environmental Information
creation_date: '2026-06-18T00:00:00Z'
description: The NOAA National Centers for Environmental Information (NCEI) is the
  U.S. government's archive and steward for environmental data, hosting one of the
  most significant collections of oceanic, atmospheric, climate, weather, and geophysical
  data on Earth. NCEI preserves and provides access to records including the Storm
  Events Database, historical hurricane and tropical cyclone tracks (IBTrACS), climate
  summaries, and a broad range of monitoring products. These data are an upstream
  source for the KnowWhereGraph project.
domains:
- environment
- public health
- general
homepage_url: https://www.ncei.noaa.gov/
id: noaa-ncei
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US Government Work (public domain)
name: NOAA National Centers for Environmental Information
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and discovering NCEI's archived
    environmental datasets across climate, weather, ocean, and geophysical domains.
  format: http
  id: noaa-ncei.data-search
  name: NCEI Data Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: noaa-ncei
  product_url: https://www.ncei.noaa.gov/access/search/data-search
- category: Product
  description: The Storm Events Database documenting the occurrence of storms and
    other significant weather phenomena in the United States, with downloadable records
    and bulk CSV files.
  format: csv
  id: noaa-ncei.storm-events
  name: NOAA Storm Events Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: noaa-ncei
  product_url: https://www.ncdc.noaa.gov/stormevents/
- category: Product
  description: The International Best Track Archive for Climate Stewardship (IBTrACS),
    a unified global collection of historical tropical cyclone (hurricane) track and
    intensity data.
  format: mixed
  id: noaa-ncei.ibtracs
  name: International Best Track Archive (IBTrACS)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: noaa-ncei
  product_url: https://www.ncei.noaa.gov/products/international-best-track-archive
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-25: Error connecting
    to URL: (''Connection aborted.'', RemoteDisconnected(''Remote end closed connection
    without response''))'
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
# NOAA National Centers for Environmental Information

## Description

The **NOAA National Centers for Environmental Information (NCEI)** is the U.S.
government's primary archive and steward for environmental data. It maintains
one of the most significant environmental data collections on Earth, spanning
oceanic, atmospheric, climate, weather, and geophysical records.

NCEI's holdings include the **Storm Events Database**, historical hurricane and
tropical cyclone tracks via the **International Best Track Archive for Climate
Stewardship (IBTrACS)**, climate normals and summaries, and numerous monitoring
products. As a U.S. federal data center, its data are generally in the public
domain. NCEI is an upstream data source for the **KnowWhereGraph** project.

## Products

- **NCEI Data Search** — web portal for discovering and accessing archived datasets.
- **NOAA Storm Events Database** — records of storms and significant weather events in the U.S.
- **International Best Track Archive (IBTrACS)** — unified global historical tropical cyclone track data.