---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/aqs
  label: US Environmental Protection Agency
creation_date: '2026-06-18T00:00:00Z'
description: The Air Quality System (AQS) is the US Environmental Protection Agency's
  repository of ambient air-quality monitoring data, assembled to support air quality
  assessments, area designations, modeling for permit review, and reports to Congress
  mandated by the Clean Air Act. It holds pollutant measurements from thousands of
  monitoring stations operated by EPA, state, local, and tribal agencies, along with
  meteorological data, station location information, and quality-assurance records.
  AQS data are exposed programmatically through a public REST API that returns JSON.
  AQS is an upstream data source for the KnowWhereGraph.
domains:
- environment
- public health
homepage_url: https://www.epa.gov/aqs
id: epa-aqs
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: EPA Air Quality System (AQS)
products:
- category: GraphicalInterface
  description: The AQS landing page describing the Air Quality System repository and
    providing access to data, tools, and documentation.
  format: http
  id: epa-aqs.landing
  name: EPA Air Quality System (AQS) landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-aqs
  product_url: https://www.epa.gov/aqs
- category: ProgrammingInterface
  description: The AQS Data API, a public REST web service returning JSON for programmatic
    access to ambient air-quality sample data, monitor metadata, and quality-assurance
    records.
  format: http
  id: epa-aqs.api
  name: AQS Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-aqs
  product_url: https://aqs.epa.gov/aqsweb/documents/data_api.html
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

The **EPA Air Quality System (AQS)** is the US Environmental Protection Agency's
repository of ambient air-quality monitoring data. It assists in air quality
assessments, area designations, modeling for permit review, and the preparation
of reports to Congress as mandated by the Clean Air Act.

AQS contains pollutant measurements collected from thousands of monitoring
stations operated by EPA, state, local, and tribal air-pollution control
agencies, together with meteorological data, station location information, and
quality-assurance records. The data are an upstream source for the
KnowWhereGraph.

## Products

- **EPA Air Quality System (AQS) landing page** — the AQS homepage providing
  access to data, tools, and documentation.
- **AQS Data API** — a public REST web service returning JSON for programmatic
  access to ambient air-quality sample data and related metadata.