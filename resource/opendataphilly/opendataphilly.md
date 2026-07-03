---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://opendataphilly.org/
  label: OpenDataPhilly
creation_date: '2026-07-03T00:00:00Z'
description: OpenDataPhilly is the open data portal for the Philadelphia region,
  cataloging hundreds of public datasets, APIs, and applications from the City of
  Philadelphia and partner organizations. Datasets span public safety, health,
  transportation, property, and other civic domains, including the Philadelphia
  crime incidents dataset.
domains:
- public health
- general
homepage_url: https://opendataphilly.org/
id: opendataphilly
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: OpenDataPhilly
products:
- category: GraphicalInterface
  description: Open data portal cataloging public datasets, APIs, and applications
    for the Philadelphia region.
  format: http
  id: opendataphilly.site
  is_public: true
  name: OpenDataPhilly Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opendataphilly
  product_url: https://opendataphilly.org/
- category: DataProduct
  description: Philadelphia crime incidents dataset, recording reported crimes with
    time, category, coordinate, and ZIP-code attributes.
  format: http
  id: opendataphilly.crime
  is_public: true
  name: Philadelphia Crime Incidents
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opendataphilly
  product_url: https://opendataphilly.org/datasets/crime-incidents/
---
# OpenDataPhilly

OpenDataPhilly is the open data portal for the Philadelphia region. It catalogs
hundreds of public datasets, APIs, and applications published by the City of
Philadelphia and partner organizations, spanning public safety, health,
transportation, property, and other civic domains.

DREAM-KG references the OpenDataPhilly Philadelphia crime incidents dataset
(recorded internally as `phila_crime`, with time, category, coordinate, and
ZIP-code attributes) for planned neighborhood-safety integration.
