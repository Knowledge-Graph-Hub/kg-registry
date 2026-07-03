---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: WorldClim
  contact_details:
  - contact_type: url
    value: https://www.worldclim.org/
creation_date: '2026-07-03T00:00:00Z'
description: WorldClim is a set of global climate layers (gridded climate data) at
  spatial resolutions down to about 1 km2, providing historical monthly, bioclimatic,
  and future (downscaled climate model) surfaces for temperature, precipitation, and
  related variables. It is widely used for species distribution modeling and other
  ecological and environmental applications.
domains:
- environment
- general
homepage_url: https://www.worldclim.org/
id: worldclim
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: WorldClim
products:
- category: GraphicalInterface
  description: WorldClim project website providing documentation and access to global
    historical, bioclimatic, and future climate data layers.
  format: http
  id: worldclim.portal
  name: WorldClim Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: worldclim
  product_url: https://www.worldclim.org/
- category: Product
  description: WorldClim version 2.1 global climate surfaces (historical monthly and
    bioclimatic variables) distributed as gridded raster data for use in ecological
    and environmental modeling.
  id: worldclim.download
  name: WorldClim 2.1 Climate Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: worldclim
  product_url: https://www.worldclim.org/data/worldclim21.html
---
# WorldClim

WorldClim provides high-spatial-resolution global climate layers derived from
weather station records interpolated across the globe. The data include historical
monthly climate, a set of derived bioclimatic variables, and future climate
projections downscaled from global climate models. WorldClim surfaces are a common
environmental input for species distribution and climate-impact modeling.
