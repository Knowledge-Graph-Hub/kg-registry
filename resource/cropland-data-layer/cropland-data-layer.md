---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php
  label: USDA National Agricultural Statistics Service
creation_date: '2026-06-18T00:00:00Z'
description: The Cropland Data Layer (CDL) is an annual, georeferenced, crop-specific
  land cover raster map covering the conterminous United States, produced by the USDA
  National Agricultural Statistics Service (NASS). It is generated from satellite imagery
  and extensive agricultural ground reference data, classifying each 30-meter pixel
  into crop types and other land cover categories. The CDL serves as an upstream source
  for KnowWhereGraph and supports agricultural monitoring, acreage estimation, and
  land use analysis.
domains:
- agriculture
- environment
- general
homepage_url: https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php
id: cropland-data-layer
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: "Cropland Data Layer"
products:
- category: GraphicalInterface
  description: CroplandCROS web mapping application for interactive viewing, querying,
    and exporting Cropland Data Layer crop-type raster data.
  format: http
  id: cropland-data-layer.croplandcros
  name: CroplandCROS Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cropland-data-layer
  product_url: https://croplandcros.scinet.usda.gov/
publications:
- id: doi:10.1080/10106049.2011.562309
  title: 'Monitoring US agriculture: the US Department of Agriculture, National Agricultural
    Statistics Service, Cropland Data Layer Program'
---

The Cropland Data Layer (CDL) is an annual crop-specific land cover product for the
conterminous United States, produced by the USDA National Agricultural Statistics
Service (NASS). Built from satellite imagery combined with ground reference data,
it provides 30-meter resolution classifications of crop types and other land cover.
The CDL is freely available as a US federal government public domain dataset and is
used as an upstream data source for KnowWhereGraph.
