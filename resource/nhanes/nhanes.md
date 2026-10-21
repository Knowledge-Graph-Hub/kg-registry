---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.cdc.gov/nchs/nhanes/
  label: CDC National Center for Health Statistics
creation_date: '2026-10-21T00:00:00Z'
description: NHANES, the National Health and Nutrition Examination Survey, is a program of
  the CDC's National Center for Health Statistics that assesses the health and nutritional
  status of adults and children in the United States. It is unusual in combining household
  interviews with standardized physical examinations and laboratory tests. Run continuously
  since 1999, it uses a multistage probability sample of the non-institutionalized US population
  and releases public-use data in two-year cycles.
domains:
- public health
- nutrition
- epidemiology
homepage_url: https://www.cdc.gov/nchs/nhanes/
id: nhanes
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: Public domain (U.S. Government work)
name: NHANES (National Health and Nutrition Examination Survey)
products:
- category: Product
  description: The main data portal listing NHANES questionnaire, examination, and laboratory
    data files and documentation, organized by survey cycle.
  format: mixed
  id: nhanes.data
  name: NHANES Questionnaires, Datasets, and Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhanes
  product_url: https://wwwn.cdc.gov/nchs/nhanes/default.aspx
- category: Product
  description: Public-use data files for the ongoing (1999-onward) NHANES, grouped by component
    (demographics, dietary, examination, laboratory, questionnaire), with methods and response
    rates.
  format: mixed
  id: nhanes.continuous
  name: Continuous NHANES Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhanes
  product_url: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx
- category: DocumentationProduct
  description: 'Tutorial modules on using NHANES data: datasets and documentation, sample
    design, weighting, variance estimation, and dietary analyses, with sample code.'
  format: http
  id: nhanes.tutorials
  name: NHANES Tutorials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhanes
  product_url: https://wwwn.cdc.gov/nchs/nhanes/tutorials/default.aspx
rrid: SCR_013201
taxon:
- NCBITaxon:9606
---

# NHANES (National Health and Nutrition Examination Survey)

## Overview

NHANES is the CDC National Center for Health Statistics program that assesses the health and nutritional status of the US population by combining interviews, physical examinations, and laboratory tests. It has run continuously since 1999 and releases public-use data in two-year cycles.

## Access

- NHANES data portal: questionnaire, examination, and laboratory files by cycle.
- Continuous NHANES documentation and public-use files.
- NHANES tutorials, with sample code.

## Citation

Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey. https://wwwn.cdc.gov/nchs/nhanes/NhanesCitation.aspx
