---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.kcr.uky.edu/contact.php
  label: University of Kentucky / Markey Cancer Center
creation_date: '2026-06-18T00:00:00Z'
description: The Kentucky Cancer Registry (KCR) is Kentucky's statewide population-based
  central cancer registry, hosted at the University of Kentucky and the Markey Cancer
  Center. KCR collects, manages, and reports incidence, treatment, and outcome data
  for cancers diagnosed among Kentucky residents. It is a participant in both the
  National Cancer Institute's Surveillance, Epidemiology, and End Results (SEER) Program
  and the Centers for Disease Control and Prevention's National Program of Cancer
  Registries (NPCR). KCR data serve as the primary data source for the Kentucky Cancer
  Registry Knowledge Graph (the .kcr graph) within the Cancer Registry KG.
domains:
- clinical
- public health
- biomedical
homepage_url: https://www.kcr.uky.edu/
id: kentucky-cancer-registry
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Kentucky Cancer Registry
products:
- category: GraphicalInterface
  description: Researcher data-request and research resources portal describing how
    to request KCR cancer surveillance data for approved research projects.
  id: kentucky-cancer-registry.research
  name: KCR Research Data Request Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kentucky-cancer-registry
  product_url: https://www.kcr.uky.edu/research/
- category: GraphicalInterface
  description: Cancer-Rates.com interactive interface providing population-based cancer
    incidence and mortality statistics for Kentucky derived from KCR data.
  id: kentucky-cancer-registry.cancer-rates
  name: Cancer-Rates.com Kentucky Statistics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kentucky-cancer-registry
  product_url: https://cancer-rates.com/ky/?datasource=mort&std=us2000
- category: GraphProduct
  description: RDF-based knowledge graph containing 207,766 unique tumor records from
    Kentucky Cancer Registry (2010-2016) with 232 columns of cancer data. Contains
    48,409,945 triples demonstrating the framework's ability to dynamically integrate
    multiple registry datasets without code changes.
  id: cancer-registry-kg.kcr
  name: Kentucky Cancer Registry Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cancer-registry-kg
  - relation_type: prov:hadPrimarySource
    source: kentucky-cancer-registry
  - relation_type: prov:hadPrimarySource
    source: naaccr
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 405 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
---
# Kentucky Cancer Registry

## Overview

The Kentucky Cancer Registry (KCR) is the statewide population-based central cancer
registry for the Commonwealth of Kentucky. It is administered through the University of
Kentucky and the Markey Cancer Center, where it collects, processes, and reports data on
cancer cases diagnosed among Kentucky residents.

## Programs

KCR contributes data to two national cancer surveillance efforts:

- **NCI SEER** — the National Cancer Institute's Surveillance, Epidemiology, and End
  Results Program
- **CDC NPCR** — the Centers for Disease Control and Prevention's National Program of
  Cancer Registries

## Use in the Cancer Registry KG

KCR is the primary data source for the Kentucky Cancer Registry Knowledge Graph (the
`.kcr` graph), one of the registry datasets integrated within the Cancer Registry KG.

## Access

Researchers can request KCR data through the registry's research resources portal. Public
incidence and mortality statistics for Kentucky are available via the Cancer-Rates.com
interface.