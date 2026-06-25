---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.dhs.gov/"
    label: U.S. Department of Homeland Security
creation_date: '2026-06-18T00:00:00Z'
description: Homeland Infrastructure Foundation-Level Data (HIFLD) is a U.S. Department of Homeland Security program that provides national geospatial datasets describing the location and attributes of critical infrastructure across the United States. Datasets cover sectors such as hospitals and public health facilities, emergency medical and fire services, law enforcement, energy and utilities, transportation, and communications. The data are distributed as an ArcGIS Hub open-data catalog with downloads in formats including CSV, GeoJSON, KML, and shapefile, and via GeoServices/WMS/WFS APIs. HIFLD is an upstream source of the KnowWhereGraph.
domains:
  - public health
  - general
  - information technology
homepage_url: https://hifld-geoplatform.hub.arcgis.com/
id: hifld
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: "Homeland Infrastructure Foundation-Level Data (HIFLD)"
products:
  - category: Product
    description: HIFLD ArcGIS Hub open-data catalog of U.S. critical infrastructure geospatial datasets, with downloads in CSV, GeoJSON, KML, GeoTIFF, and shapefile formats.
    format: csv
    id: "hifld.catalog"
    is_public: true
    name: HIFLD Open Data Catalog
    product_url: https://hifld-geoplatform.hub.arcgis.com/search
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hifld
  - category: ProgrammingInterface
    description: ArcGIS Hub open-data API access to HIFLD datasets via GeoServices, WMS, and WFS endpoints for programmatic querying and download.
    format: http
    id: "hifld.api"
    is_public: true
    name: HIFLD Open Data API
    product_url: https://hifld-geoplatform.opendata.arcgis.com/
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hifld
---

# Homeland Infrastructure Foundation-Level Data (HIFLD)

## Overview

Homeland Infrastructure Foundation-Level Data (HIFLD) is a program of the U.S. Department of Homeland Security (DHS) that assembles and shares national geospatial datasets describing critical infrastructure across the United States. It is delivered as an ArcGIS Hub open-data platform where users can discover, analyze, and download individual layers.

## Data Content

HIFLD layers span many critical-infrastructure sectors, including:

- Public health and emergency services: hospitals, urgent care, emergency medical services, fire stations
- Public safety: law enforcement and correctional facilities
- Energy and utilities: power plants, transmission lines, pipelines
- Transportation: roads, rail, airports, ports
- Communications and other lifeline infrastructure

## Data Access

Datasets are available through the ArcGIS Hub catalog with downloads in formats such as CSV, GeoJSON, KML, GeoTIFF, and shapefile, and through GeoServices, WMS, and WFS API endpoints.

## Licensing Note

Many HIFLD layers are derived from U.S. federal sources and are in the public domain, but some individual layers carry use restrictions or are access-controlled. License terms vary by layer, so the resource-level license is recorded here as Not specified; consult each dataset's metadata for its specific terms.

## Relationship to KnowWhereGraph

HIFLD is an upstream data source used by the KnowWhereGraph, contributing critical-infrastructure and human-systems geospatial layers.
