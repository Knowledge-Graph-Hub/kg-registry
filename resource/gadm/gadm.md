---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://gadm.org/about.html
    label: GADM
creation_date: '2026-06-18T00:00:00Z'
description: GADM (Database of Global Administrative Areas) provides maps and spatial data of administrative boundaries for all countries and their sub-divisions. The current version (4.1) delimits over 400,000 administrative areas across multiple levels, from countries down to local divisions. The polygons are distributed for download by country or for the entire world in several geospatial formats. GADM is used as an upstream source of administrative boundary data by projects such as KnowWhereGraph.
domains:
  - environment
  - general
  - information technology
homepage_url: https://gadm.org/
id: gadm
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: GADM license (free for academic/non-commercial use)
name: GADM
products:
  - category: Product
    description: Download page for GADM administrative boundary spatial data by country, the recommended approach for obtaining GADM polygons.
    id: gadm.download_country
    name: GADM Data Download (by country)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gadm
    product_url: https://gadm.org/download_country.html
  - category: Product
    description: Download page for GADM administrative boundary spatial data covering the entire world.
    id: gadm.download_world
    name: GADM Data Download (world)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gadm
    product_url: https://gadm.org/download_world.html
  - category: DocumentationProduct
    description: Metadata documentation describing the GADM data, its structure, and administrative levels.
    id: gadm.metadata
    name: GADM Metadata
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gadm
    product_url: https://gadm.org/metadata.html
synonyms:
  - Database of Global Administrative Areas
---

# GADM (Database of Global Administrative Areas)

## Overview

GADM provides maps and spatial data for all countries and their sub-divisions. Users can browse the maps online or download the underlying data to make their own maps and analyses. The data describe administrative boundary polygons (countries, states/provinces, districts, and lower-level divisions) at multiple administrative levels.

## Data Content

- The current version (4.1) delimits 400,276 administrative areas; version 5 is slated for release in January 2026.
- Data are available for download by country (the recommended approach) or for the entire world.
- Multiple geospatial formats are offered for download.

## Use Cases

- Joining administrative boundaries to tabular data for mapping and spatial analysis.
- Serving as an authoritative source of administrative regions for knowledge graphs and geospatial knowledge bases such as KnowWhereGraph.

## License

The data are freely available for academic use and other non-commercial use. Redistribution or commercial use is not allowed without prior permission. Using the data to create maps for figures in academic research articles is permitted. A small number of countries (e.g., Austria) are covered by a different license. See https://gadm.org/license.html for full details.
