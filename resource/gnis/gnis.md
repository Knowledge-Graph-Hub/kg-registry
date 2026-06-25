---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.usgs.gov/
  label: U.S. Geological Survey (USGS)
creation_date: '2026-06-18T00:00:00Z'
description: The Geographic Names Information System (GNIS) is the U.S. federal and
  national standard for geographic nomenclature, serving as the official repository
  of names and attributes for physical and cultural geographic features across the
  United States, its territories, and Antarctica. It is developed and maintained by
  the U.S. Geological Survey's National Geospatial Program in support of the U.S.
  Board on Geographic Names. For each feature it records the official name, feature
  class, state and county, geographic coordinates, elevation, historical and variant
  names, and related metadata. GNIS is the upstream source for the KnowWhereGraph
  geospatial knowledge graph.
domains:
- general
- information technology
- environment
homepage_url: https://www.usgs.gov/tools/geographic-names-information-system-gnis
id: gnis
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: Geographic Names Information System
products:
- category: GraphicalInterface
  description: Domestic Names search application for querying GNIS geographic features
    by name, feature class, state, and county.
  format: http
  id: gnis.search
  name: GNIS Domestic Names Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnis
  product_url: https://edits.nationalmap.gov/apps/gaz-domestic/public/search/names
- category: Product
  description: GNIS data download portal providing bulk geographic names files for
    the United States, individual states, and topical extracts.
  format: http
  id: gnis.download
  name: GNIS Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnis
  product_url: https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data
- category: GraphicalInterface
  description: GNIS-LD, the Linked Data (RDF/GeoSPARQL) version of GNIS published by
    the STKO Lab at UC Santa Barbara, with a public SPARQL endpoint and downloadable
    triples.
  format: http
  id: gnis.linkeddata
  name: GNIS-LD (Linked Data)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnis
  product_url: https://gnis-ld.org/
---

## Description

The Geographic Names Information System (GNIS) is the official U.S. gazetteer of
geographic feature names, maintained by the U.S. Geological Survey (USGS) in
support of the U.S. Board on Geographic Names. It is the federal and national
standard for geographic nomenclature, covering physical and cultural features
across the United States, its territories, and Antarctica, with attributes such
as official name, feature class, location, coordinates, elevation, and variant
names. GNIS data is in the U.S. public domain and serves as an upstream source
for the KnowWhereGraph geospatial knowledge graph.

## Products

- **GNIS Domestic Names Search** — web application for searching geographic
  features by name and attributes.
- **GNIS Data Download** — bulk download portal for national, state, and topical
  geographic names files.
- **GNIS-LD (Linked Data)** — RDF/GeoSPARQL Linked Data edition of GNIS with a
  public SPARQL endpoint and downloadable triples.
