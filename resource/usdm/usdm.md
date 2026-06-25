---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: National Drought Mitigation Center
    contact_details:
      - contact_type: url
        value: https://droughtmonitor.unl.edu/About/ContactUs.aspx
creation_date: '2026-06-18T00:00:00Z'
description: >-
  The U.S. Drought Monitor (USDM) is a weekly map and dataset that
  classifies the location and severity of drought across the United States,
  its territories, and tribal areas. It is produced jointly by the National
  Drought Mitigation Center at the University of Nebraska-Lincoln, the U.S.
  Department of Agriculture, and the National Oceanic and Atmospheric
  Administration, drawing on numerous climatic and hydrologic indicators plus
  local expert input. USDM data and maps serve as an upstream source for
  KnowWhereGraph.
domains:
  - environment
  - agriculture
  - public health
homepage_url: https://droughtmonitor.unl.edu/
id: usdm
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: "U.S. Drought Monitor"
products:
  - category: GraphicalInterface
    description: Interactive web portal presenting the current weekly U.S. Drought
      Monitor map and severity classifications.
    format: http
    id: usdm.map
    name: U.S. Drought Monitor Current Map
    original_source:
      - relation_type: prov:hadPrimarySource
        source: usdm
    product_url: https://droughtmonitor.unl.edu/CurrentMap.aspx
  - category: Product
    description: GIS and data download portal providing USDM drought severity
      maps and tabular data for download.
    format: http
    id: usdm.data
    name: U.S. Drought Monitor GIS and Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: usdm
    product_url: https://droughtmonitor.unl.edu/DmData/GISData.aspx
---

## Description

The **U.S. Drought Monitor (USDM)** is a weekly map and dataset that classifies
the location and severity of drought across the United States, its territories,
and tribal areas. It is produced jointly by the **National Drought Mitigation
Center** at the University of Nebraska-Lincoln, the **U.S. Department of
Agriculture (USDA)**, and the **National Oceanic and Atmospheric Administration
(NOAA)**, integrating numerous climatic and hydrologic indicators along with
input from local experts.

USDM drought maps and underlying data serve as an upstream source for
**KnowWhereGraph**.

## Products

- **U.S. Drought Monitor Current Map** — interactive web portal showing the
  current weekly drought severity map.
- **U.S. Drought Monitor GIS and Data** — GIS and data download portal for USDM
  maps and tabular drought data.
