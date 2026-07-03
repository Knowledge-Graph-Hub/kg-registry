---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.census.gov/naics/
  label: US Census Bureau
creation_date: '2026-07-03T00:00:00Z'
description: The North American Industry Classification System (NAICS) is the standard
  used by US federal statistical agencies to classify business establishments by their
  type of economic activity. Developed jointly by the United States, Canada, and Mexico,
  NAICS assigns each establishment a hierarchical industry code. SAWGraph uses NAICS
  codes to classify the industry of facilities in its Facilities and Industries Ontology
  (FIO) knowledge graph, where facility records drawn from EPA's Facility Registry
  Service carry NAICS classifications.
domains:
- general
homepage_url: https://www.census.gov/naics/
id: naics
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: North American Industry Classification System (NAICS)
products:
- category: GraphicalInterface
  description: US Census Bureau guidance page describing the North American Industry
    Classification System, its hierarchical structure, and how business establishments
    are classified by their type of economic activity.
  format: http
  id: naics.landing
  name: NAICS reference page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: naics
  product_url: https://www.census.gov/programs-surveys/economic-census/year/2022/guidance/understanding-naics.html
---
## Description

The North American Industry Classification System (NAICS) is the standard used by
US federal statistical agencies to classify business establishments by their type
of economic activity. It was developed jointly by the United States, Canada, and
Mexico and assigns each establishment a hierarchical industry code.

SAWGraph uses NAICS codes to classify the industry of facilities in its Facilities
and Industries Ontology (FIO) knowledge graph. Facility records drawn from EPA's
Facility Registry Service carry NAICS classifications that populate the FIO industry
classification scheme.
