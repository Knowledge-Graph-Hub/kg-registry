---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://publichealth.lsuhsc.edu/louisiana-tumor-registry/ltr-contact-us.aspx
  label: LSUHSC School of Public Health, Louisiana Tumor Registry
creation_date: '2026-06-18T00:00:00Z'
description: The Louisiana Tumor Registry (LTR) is Louisiana's statewide, population-based
  cancer incidence registry, housed in the School of Public Health at LSU Health Sciences
  Center New Orleans. It collects, manages, and reports data on all newly diagnosed
  cancer cases among Louisiana residents and participates in both the NCI Surveillance,
  Epidemiology, and End Results (SEER) Program and the CDC National Program of Cancer
  Registries (NPCR). LTR data support cancer surveillance, research, and public health
  planning, and serve as the primary data source for the Cancer Registry KG (the .ltr
  graph).
domains:
- public health
- clinical
- biomedical
homepage_url: https://publichealth.lsuhsc.edu/louisiana-tumor-registry/
id: louisiana-tumor-registry
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Louisiana Tumor Registry
products:
- category: GraphicalInterface
  description: Web page describing how researchers and other parties may request Louisiana
    Tumor Registry data, including data use agreement and request procedures.
  format: http
  id: louisiana-tumor-registry.data-request
  name: Louisiana Tumor Registry Data Request
  original_source:
  - relation_type: prov:hadPrimarySource
    source: louisiana-tumor-registry
  product_url: https://publichealth.lsuhsc.edu/louisiana-tumor-registry/data-usestatistics/data-request.aspx
- category: GraphProduct
  description: RDF-based knowledge graph containing 374,682 unique tumor records from
    Louisiana Tumor Registry (2000-2016) with 240 columns of NAACCR-standardized cancer
    data including demographics, tumor characteristics, treatment, and outcomes. Contains
    90,673,527 triples stored in Virtuoso triplestore with SPARQL endpoint access.
  id: cancer-registry-kg.ltr
  name: Louisiana Tumor Registry Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cancer-registry-kg
  - relation_type: prov:hadPrimarySource
    source: louisiana-tumor-registry
  - relation_type: prov:hadPrimarySource
    source: naaccr
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 405 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
---
The Louisiana Tumor Registry (LTR) is the statewide, population-based cancer
incidence registry for the state of Louisiana, operated by the School of Public
Health at Louisiana State University Health Sciences Center New Orleans
(LSUHSC). LTR ascertains and maintains records on all reportable cancers
diagnosed among Louisiana residents.

As a SEER registry (NCI Surveillance, Epidemiology, and End Results Program) and
an NPCR registry (CDC National Program of Cancer Registries), LTR provides
high-quality, standardized cancer incidence and survival data used for
surveillance, epidemiologic research, special studies, and public health
program planning.

LTR data serve as the primary data source for the Cancer Registry KG, the
`.ltr` graph in the Knowledge Graph Hub ecosystem.