---
activity_status: active
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/waterdata
  label: US Environmental Protection Agency
creation_date: '2026-10-21T00:00:00Z'
description: The Water Quality Exchange (WQX) is the US EPA's national data format and submission
  mechanism for sharing water quality monitoring data. State, tribal, and federal agencies,
  local governments, universities, and non-governmental organizations submit monitoring locations,
  sampling activities, and results, which populate EPA's WQX database. Data can be prepared
  with spreadsheet templates, submitted through the WQXWeb application, or sent as WQX XML
  through the EPA Exchange Network. WQX data are published to the public through the Water
  Quality Portal, which combines them with USGS NWIS data. Version 3.0 is current and version
  2.2 is also supported.
domains:
- environment
- water resources
homepage_url: https://www.epa.gov/waterdata/water-quality-data
id: wqx
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: Public domain (U.S. federal government work)
name: Water Quality Exchange (WQX)
products:
- category: DataModelProduct
  description: 'The WQX data flow package on the EPA Exchange Network: the XML schema, flow
    configuration document, schema change logs, and the Data Exchange Template for versions
    3.0 and 2.2.'
  format: xml
  id: wqx.schema
  name: WQX Data Exchange Schema and Template
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wqx
  product_url: https://exchangenetwork.net/data-exchange/wqx/
- category: DocumentationProduct
  description: EPA guidance and the WQXWeb application for reformatting and submitting monitoring
    data to WQX, including templates, the WQXWeb REST API, and Exchange Network node submission.
  format: http
  id: wqx.upload-guidance
  name: Water Quality Data Upload with WQX
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wqx
  product_url: https://www.epa.gov/waterdata/water-quality-data-upload-wqx
- category: Product
  description: Downloadable Excel template and data-dictionary packages for importing physical-chemical,
    biological, habitat, metrics, lab, and continuous monitoring results into WQX Web.
  format: xlsx
  id: wqx.web-templates
  name: WQX Web Template Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wqx
  product_url: https://www.epa.gov/waterdata/water-quality-exchange-web-template-files
- category: GraphicalInterface
  description: EPA's Central Data Exchange (CDX), the electronic reporting portal through
    which registered users log in to WQXWeb to submit water quality data.
  format: http
  id: wqx.cdx
  name: WQXWeb via EPA Central Data Exchange
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wqx
  product_url: https://cdx.epa.gov/
synonyms:
- WQX
- Water Quality eXchange
version: '3.0'
---

# Water Quality Exchange (WQX)

## Overview

WQX is the US EPA's national data format and submission mechanism for water quality monitoring data. Organizations submit monitoring locations, sampling activities, and results into EPA's WQX database, which is then served to the public through the Water Quality Portal (`water-quality-portal`) alongside USGS NWIS data.

## Access

- WQX XML schema and Data Exchange Template (Exchange Network), versions 3.0 and 2.2.
- Water Quality Data Upload with WQX: WQXWeb guidance and application.
- WQX Web template files (Excel).
- WQXWeb access through EPA's Central Data Exchange (CDX).

WQX is the submission standard and EPA database; the Water Quality Portal is the downstream warehouse that serves WQX data.

## Citation

US Environmental Protection Agency. Water Quality Exchange (WQX). https://www.epa.gov/waterdata/water-quality-data
