---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.samhsa.gov/data
  label: Substance Abuse and Mental Health Services Administration (SAMHSA)
creation_date: '2026-07-03T00:00:00Z'
description: The National Directory of Mental Health Treatment Facilities is a directory
  published by the Substance Abuse and Mental Health Services Administration (SAMHSA)
  listing mental health treatment facilities across the United States. For each facility
  it records identifying and location information along with the mental health services
  offered. The directory is compiled primarily from SAMHSA's National Substance Use
  and Mental Health Services Survey and is widely reused to locate and characterize
  mental health treatment providers and the services they deliver.
domains:
- public health
- clinical
- general
homepage_url: https://www.samhsa.gov/data/report/national-directory-mental-health-treatment-facilities
id: national-directory-mental-health-facilities
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: National Directory of Mental Health Treatment Facilities
products:
- category: GraphicalInterface
  description: The SAMHSA report page for the National Directory of Mental Health
    Treatment Facilities, providing the directory documents and downloadable facility
    listings.
  format: http
  id: national-directory-mental-health-facilities.samhsa-page
  is_public: true
  name: SAMHSA National Directory of Mental Health Treatment Facilities page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: national-directory-mental-health-facilities
  product_url: https://www.samhsa.gov/data/report/national-directory-mental-health-treatment-facilities
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

The **National Directory of Mental Health Treatment Facilities** is a SAMHSA
directory of mental health treatment facilities across the United States,
recording facility location and identifying information together with the
mental health services each facility provides.

In the KG-Registry, this directory is recorded as an upstream data source for
the **Rural Resilience KG**, whose mental health treatment providers and
services are sourced from the National Directory of Mental Health Treatment
Facilities.

## Products

- **SAMHSA National Directory of Mental Health Treatment Facilities page** — the
  official report page providing the directory documents and facility listings.