---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nrcs.usda.gov/
  label: USDA Natural Resources Conservation Service (NRCS)
creation_date: '2026-06-18T00:00:00Z'
description: The Soil Survey Geographic Database (SSURGO) is a detailed digital soil-survey
  dataset produced by the USDA Natural Resources Conservation Service (NRCS). It provides
  spatial map units and associated tabular attributes describing the physical and
  chemical properties of soils across the United States, generally at scales from
  1:12,000 to 1:63,360. SSURGO is the most detailed level of the USDA soil-survey
  series and is widely used in land management, agriculture, and environmental modeling.
  It serves as an upstream data source for KnowWhereGraph.
domains:
- agriculture
- environment
- general
homepage_url: https://websoilsurvey.nrcs.usda.gov/
id: ssurgo
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: Soil Survey Geographic Database (SSURGO)
products:
- category: Product
  description: Web Soil Survey provides interactive access to SSURGO soil data, allowing
    users to define areas of interest and view, print, and download detailed soil
    maps and property reports.
  format: http
  id: ssurgo.websoilsurvey
  name: Web Soil Survey
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ssurgo
  product_url: https://websoilsurvey.nrcs.usda.gov/
- category: Product
  description: Official NRCS Box-hosted distribution portal for downloading SSURGO
    soil survey spatial and tabular data by survey area.
  format: http
  id: ssurgo.download
  name: NRCS Soils Data Download Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ssurgo
  product_url: https://nrcs.app.box.com/v/soils
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-25: HTTP 404 error
    when accessing file'
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

The **Soil Survey Geographic Database (SSURGO)** is the most detailed level of
soil mapping produced by the USDA **Natural Resources Conservation Service
(NRCS)**. It captures soil-survey **map units** as spatial polygons together with
extensive tabular attributes describing soil composition, physical and chemical
properties, and interpretations for use.

SSURGO data are collected and distributed by survey area (typically a county or
similar unit) and are commonly applied in agriculture, land-use planning, and
environmental modeling. The database is an upstream data source for
**KnowWhereGraph**.

## Products

- **Web Soil Survey** — interactive viewer for defining an area of interest and
  obtaining soil maps and property reports.
- **NRCS Soils Data Download Portal** — official Box-hosted distribution of
  SSURGO spatial and tabular data by survey area.