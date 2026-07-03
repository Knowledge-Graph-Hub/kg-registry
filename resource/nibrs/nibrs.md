---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.fbi.gov/how-we-can-help-you/more-fbi-services-and-information/ucr
  label: FBI Criminal Justice Information Services (CJIS) Division
creation_date: '2026-07-03T00:00:00Z'
description: The National Incident-Based Reporting System (NIBRS) is the crime data
  collection program of the FBI Uniform Crime Reporting (UCR) Program, administered
  by the Criminal Justice Information Services (CJIS) Division. NIBRS captures detailed,
  incident-level data on criminal offenses reported by participating law enforcement
  agencies, including information on offenses, offenders, victims, arrestees, and
  property. Each incident is described through a standardized set of data elements
  and segments. NIBRS data are widely reused for justice and public safety analysis
  and are published through the FBI Crime Data Explorer.
domains:
- public health
- general
homepage_url: https://cde.ucr.cjis.gov/
id: nibrs
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: National Incident-Based Reporting System
products:
- category: GraphicalInterface
  description: The FBI Crime Data Explorer (CDE) is the public platform for accessing,
    exploring, and downloading NIBRS incident-level crime data reported by law enforcement
    agencies across the United States.
  format: http
  id: nibrs.cde
  is_public: true
  name: FBI Crime Data Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nibrs
  product_url: https://cde.ucr.cjis.gov/
- category: GraphProduct
  description: The Rural Resilience KG graph, a cross-domain RDF knowledge graph integrating
    health and justice data for rural resilience. It integrates justice/crime data
    from the National Incident-Based Reporting System (NIBRS), substance-use survey
    data from the National Survey on Drug Use and Health (NSDUH), mental health treatment
    providers from the National Directory of Mental Health Treatment Facilities, county
    rurality classifications from the USDA Rural-Urban Continuum Codes, and US administrative-area
    geography, served via the FRINK/Proto-OKN infrastructure.
  format: ttl
  id: ruralkg.graph
  name: Rural Resilience KG graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ruralkg
  - relation_type: prov:hadPrimarySource
    source: nibrs
  - relation_type: prov:hadPrimarySource
    source: nsduh
  - relation_type: prov:hadPrimarySource
    source: national-directory-mental-health-facilities
  - relation_type: prov:hadPrimarySource
    source: rural-urban-continuum-codes
  product_url: https://frink.renci.org/registry/kgs/rural-kg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: us-census
---
## Description

The **National Incident-Based Reporting System (NIBRS)** is the FBI's
incident-level crime data collection program, part of the Uniform Crime
Reporting (UCR) Program and administered by the Criminal Justice Information
Services (CJIS) Division. NIBRS records detailed data on each criminal
incident, covering offenses, offenders, victims, arrestees, and property
through a standardized set of data elements and segments.

In the KG-Registry, NIBRS is recorded as an upstream justice/crime data source
for the **Rural Resilience KG**, whose justice data are extracted from NIBRS.

## Products

- **FBI Crime Data Explorer** — the official public platform for accessing and
  downloading NIBRS incident-level crime data.