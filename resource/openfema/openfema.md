---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.fema.gov/about/openfema
    label: Federal Emergency Management Agency (FEMA)
creation_date: '2026-06-18T00:00:00Z'
description: OpenFEMA is the U.S. Federal Emergency Management Agency's open-data program, providing public access to FEMA's program data. It publishes datasets covering federal disaster declarations, individual and public assistance, hazard mitigation, flood insurance, and other emergency-management programs. Data are distributed as downloadable files and through a versioned RESTful API. OpenFEMA is an upstream source for KnowWhereGraph.
domains:
  - public health
  - environment
  - general
homepage_url: https://www.fema.gov/about/openfema
id: openfema
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: "OpenFEMA"
products:
  - category: Product
    description: Catalog of OpenFEMA datasets covering federal disaster declarations, individual and public assistance, hazard mitigation, flood insurance, and related FEMA programs, available as downloadable CSV, JSON, and other file formats.
    format: http
    id: openfema.datasets
    name: OpenFEMA Data Sets
    original_source:
      - relation_type: prov:hadPrimarySource
        source: openfema
    product_url: https://www.fema.gov/about/openfema/data-sets
  - category: ProgrammingInterface
    description: Versioned RESTful API for querying OpenFEMA datasets programmatically, supporting OData-style filtering, selection, ordering, and paging with JSON, JSONA, and CSV output.
    format: http
    id: openfema.api
    name: OpenFEMA API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: openfema
    product_url: https://www.fema.gov/about/openfema/api
---

# OpenFEMA

## Overview

OpenFEMA is the open-data program of the U.S. Federal Emergency Management Agency (FEMA). It provides public, machine-readable access to FEMA program data, including federal disaster declarations, individual and public assistance awards, hazard mitigation, flood insurance, and related emergency-management datasets.

## Access

OpenFEMA data are available both as bulk downloadable files (CSV, JSON, and other formats) and through a versioned RESTful API. The API supports OData-style query parameters for filtering, selecting, ordering, and paging across the full dataset catalog.

## Provenance

OpenFEMA is published by FEMA as a U.S. Government work in the public domain, and serves as an upstream data source for KnowWhereGraph.
