---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.osha.gov/data/sic-manual
  label: US Department of Labor, Occupational Safety and Health Administration
creation_date: '2026-07-03T00:00:00Z'
description: The Standard Industrial Classification (SIC) is a legacy United States
  government system for classifying industries by a four-digit code, established in
  1937 and largely superseded by NAICS. SIC codes remain in use across many federal
  datasets. SAWGraph uses SIC codes, alongside NAICS, to classify the industry of
  facilities in its Facilities and Industries Ontology (FIO) knowledge graph, where
  facility records drawn from EPA's Facility Registry Service carry SIC classifications.
domains:
- general
homepage_url: https://www.osha.gov/data/sic-manual
id: sic
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: Standard Industrial Classification (SIC)
products:
- category: GraphicalInterface
  description: The OSHA SIC Manual, a searchable reference for the Standard Industrial
    Classification system describing industry divisions, major groups, and four-digit
    SIC codes.
  format: http
  id: sic.manual
  name: OSHA SIC Manual
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sic
  product_url: https://www.osha.gov/data/sic-manual
- category: GraphProduct
  description: The SAWGraph Facilities and Industries Ontology (FIO) / Facility Registry
    Service (FRS) knowledge graph, an RDF (Turtle) graph representing US facilities
    from EPA's Facility Registry Service together with their NAICS and SIC industry
    classifications and spatial locations. It is served through the SAWGraph FRS SPARQL
    and Triple Pattern Fragments endpoints.
  format: ttl
  id: fiokg.graph
  name: SAWGraph FRS Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fiokg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  product_url: https://github.com/SAWGraph/fio
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: naics
  - relation_type: prov:wasInfluencedBy
    source: sic
---
## Description

The Standard Industrial Classification (SIC) is a legacy United States government
system for classifying industries by a four-digit code. It was established in 1937
and has largely been superseded by the North American Industry Classification System
(NAICS), but SIC codes remain in use across many federal datasets.

SAWGraph uses SIC codes, alongside NAICS, to classify the industry of facilities in
its Facilities and Industries Ontology (FIO) knowledge graph. Facility records drawn
from EPA's Facility Registry Service carry SIC classifications that populate the FIO
industry classification scheme.