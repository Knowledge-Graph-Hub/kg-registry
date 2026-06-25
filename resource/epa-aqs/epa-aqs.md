---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: "US Environmental Protection Agency"
    contact_details:
      - contact_type: url
        value: https://www.epa.gov/aqs
creation_date: '2026-06-18T00:00:00Z'
description: >-
  The Air Quality System (AQS) is the US Environmental Protection Agency's
  repository of ambient air-quality monitoring data, assembled to support air
  quality assessments, area designations, modeling for permit review, and
  reports to Congress mandated by the Clean Air Act. It holds pollutant
  measurements from thousands of monitoring stations operated by EPA, state,
  local, and tribal agencies, along with meteorological data, station location
  information, and quality-assurance records. AQS data are exposed
  programmatically through a public REST API that returns JSON. AQS is an
  upstream data source for the KnowWhereGraph.
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
name: "EPA Air Quality System (AQS)"
products:
  - category: GraphicalInterface
    description: The AQS landing page describing the Air Quality System repository and providing access to data, tools, and documentation.
    format: http
    id: epa-aqs.landing
    name: EPA Air Quality System (AQS) landing page
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-aqs
    product_url: https://www.epa.gov/aqs
  - category: ProgrammingInterface
    description: The AQS Data API, a public REST web service returning JSON for programmatic access to ambient air-quality sample data, monitor metadata, and quality-assurance records.
    format: http
    id: epa-aqs.api
    name: AQS Data API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-aqs
    product_url: https://aqs.epa.gov/aqsweb/documents/data_api.html
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
