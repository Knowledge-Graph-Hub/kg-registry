---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.census.gov/
    label: US Census Bureau
creation_date: '2026-06-18T00:00:00Z'
description: The United States Census Bureau is the federal agency responsible for producing demographic, socioeconomic, and geographic data about the people and economy of the United States. Its data products include the decennial Census, the American Community Survey (ACS), economic and business surveys, and TIGER/Line geographic boundary files. These datasets are widely reused for socioeconomic linkage and administrative geography enrichment in downstream knowledge graphs.
domains:
  - public health
  - general
  - information technology
homepage_url: https://www.census.gov/
id: us-census
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: United States Census Bureau
products:
  - category: GraphicalInterface
    description: data.census.gov is the Census Bureau's primary web platform for searching, exploring, and downloading data from the decennial Census, American Community Survey, and other Census programs.
    format: http
    id: us-census.data
    is_public: true
    name: data.census.gov
    product_url: https://data.census.gov/
    original_source:
      - relation_type: prov:hadPrimarySource
        source: us-census
  - category: ProgrammingInterface
    description: The Census Data API provides programmatic access to Census Bureau datasets, including the decennial Census, American Community Survey, and economic surveys, for developers building applications and data pipelines.
    format: http
    id: us-census.api
    is_public: true
    name: Census Data API
    product_url: https://www.census.gov/data/developers.html
    original_source:
      - relation_type: prov:hadPrimarySource
        source: us-census
---

# United States Census Bureau

## Overview

The United States Census Bureau is the principal federal agency for collecting and disseminating data about the American people and economy. It conducts the constitutionally mandated decennial Census of Population and Housing, the annual American Community Survey (ACS), and numerous economic, business, and demographic surveys.

## Data Content

- **Decennial Census**: Population and housing counts collected every ten years.
- **American Community Survey (ACS)**: Ongoing survey providing detailed socioeconomic and demographic estimates.
- **TIGER/Line**: Geographic and cartographic boundary files for administrative geographies (states, counties, tracts, block groups, ZIP Code Tabulation Areas).
- **Economic surveys**: Business, industry, and economic indicator data.

## Use in Knowledge Graphs

Census data serves as an upstream source for multiple knowledge graphs, including the Cancer Registry KG (socioeconomic linkage) and KnowWhereGraph (administrative geographies and demographics).

## Access

- **data.census.gov**: Web interface for searching and downloading Census data.
- **Census Data API**: Programmatic access for developers (https://www.census.gov/data/developers.html).

## License

As a work of the U.S. federal government, Census Bureau data products are generally in the public domain (U.S. Government Work).
