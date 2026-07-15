---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://disc.gsfc.nasa.gov/contact
  label: NASA GES DISC (Goddard Earth Sciences Data and Information Services Center)
creation_date: '2026-07-01T00:00:00Z'
description: NASA's Goddard Earth Sciences Data and Information Services Center (GES
  DISC) is one of NASA's Earth Observing System Data and Information System (EOSDIS)
  data centers, operated at Goddard Space Flight Center. It archives and distributes
  Earth science data spanning atmospheric composition, the global water and energy
  cycles, precipitation (including the GPM and TRMM missions), and atmospheric dynamics,
  along with associated data access services, tools, and APIs (e.g., OPeNDAP and Earthdata
  access) for discovering, subsetting, and retrieving these datasets.
domains:
- environment
- general
homepage_url: https://disc.gsfc.nasa.gov/
id: nasa-gesdisc
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://www.earthdata.nasa.gov/engage/open-data-services-software-policies
  label: NASA Open Data Policy (U.S. Government work, public domain)
name: NASA GES DISC (Goddard Earth Sciences Data and Information Services Center)
products:
- category: Product
  description: The GES DISC data archive, providing discovery, access, and download
    of NASA Earth science datasets (atmospheric composition, water and energy cycles,
    precipitation, and atmospheric dynamics) through the dataset catalog, OPeNDAP,
    and Earthdata access services and APIs.
  format: mixed
  id: nasa-gesdisc.archive
  name: GES DISC Data Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nasa-gesdisc
  product_url: https://disc.gsfc.nasa.gov/datasets
  warnings: []
- category: GraphProduct
  description: The NASA Knowledge Graph Dataset (NASA-GESDISC-KG), an RDF knowledge
    graph integrating NASA satellite datasets, scientific publications, instruments,
    platforms, projects, data centers, and science keywords, derived from NASA GES
    DISC data holdings.
  format: ttl
  id: nasa-gesdisc-kg.graph
  name: NASA-GESDISC-KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nasa-gesdisc-kg
  - relation_type: prov:wasDerivedFrom
    source: nasa-gesdisc
  product_url: https://frink.renci.org/nasa-gesdisc-kg
---
# NASA GES DISC (Goddard Earth Sciences Data and Information Services Center)

## Overview

NASA's Goddard Earth Sciences Data and Information Services Center (GES DISC) is one of the data centers of NASA's Earth Observing System Data and Information System (EOSDIS), operated at Goddard Space Flight Center. GES DISC archives and distributes a broad range of Earth science data, with focus areas including atmospheric composition, the global water and energy cycles, precipitation (including the Global Precipitation Measurement, GPM, and Tropical Rainfall Measuring Mission, TRMM), and atmospheric dynamics.

## Access

GES DISC provides data discovery and access through its dataset catalog, along with tools and services such as OPeNDAP and NASA Earthdata access mechanisms and APIs for subsetting and retrieving data.