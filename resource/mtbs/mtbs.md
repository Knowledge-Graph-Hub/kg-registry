---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mtbs.gov/
  label: Monitoring Trends in Burn Severity (MTBS), USGS / USDA Forest Service
creation_date: '2026-06-18T00:00:00Z'
description: Monitoring Trends in Burn Severity (MTBS) is an interagency program that
  consistently maps the burn severity and perimeter extent of large wildfires across
  all lands of the United States from 1984 to the present. Fires are mapped where
  they meet size thresholds of 1,000 acres or greater in the western U.S. and 500
  acres or greater in the eastern U.S., covering the continental U.S., Alaska, Hawaii,
  and Puerto Rico. The program is a joint effort of the U.S. Geological Survey (USGS)
  and the USDA Forest Service. MTBS data serve as an upstream source for KnowWhereGraph.
domains:
- environment
- general
homepage_url: https://www.mtbs.gov/
id: mtbs
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Monitoring Trends in Burn Severity
products:
- category: Product
  description: MTBS Direct Download page providing fire-level and state/national burn
    severity and perimeter datasets plus web map services.
  format: http
  id: mtbs.direct-download
  name: MTBS Direct Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mtbs
  product_url: https://www.mtbs.gov/direct-download
- category: GraphicalInterface
  description: Interactive burn severity viewer for visualizing, filtering, and downloading
    MTBS fire perimeter and burn severity data.
  format: http
  id: mtbs.viewer
  name: MTBS Burn Severity Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mtbs
  product_url: https://burnseverity.cr.usgs.gov/viewer/
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
publications: []
---
## Description

Monitoring Trends in Burn Severity (MTBS) is an interagency program that consistently maps the burn severity and perimeter extent of large wildfires across all lands of the United States from 1984 to the present. Fires are mapped where they meet size thresholds of 1,000 acres or greater in the western U.S. and 500 acres or greater in the eastern U.S., covering the continental U.S., Alaska, Hawaii, and Puerto Rico. The program is a joint effort of the U.S. Geological Survey (USGS) and the USDA Forest Service. MTBS data serve as an upstream source for KnowWhereGraph.

## Contacts

- Monitoring Trends in Burn Severity (MTBS), USGS / USDA Forest Service (https://www.mtbs.gov/)

## Products

### MTBS Direct Download

MTBS Direct Download page providing fire-level and state/national burn severity and perimeter datasets plus web map services.

**URL**: [https://www.mtbs.gov/direct-download](https://www.mtbs.gov/direct-download)

**Format**: http

### MTBS Burn Severity Viewer

Interactive burn severity viewer for visualizing, filtering, and downloading MTBS fire perimeter and burn severity data.

**URL**: [https://burnseverity.cr.usgs.gov/viewer/](https://burnseverity.cr.usgs.gov/viewer/)

**Format**: http

**Domains**: environment, general