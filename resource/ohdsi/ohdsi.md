---
activity_status: active
category: Aggregator
collection:
  - omop
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.ohdsi.org/
    id: ohdsi
    label: OHDSI
creation_date: '2026-04-10T00:00:00Z'
description: Observational Health Data Sciences and Informatics (OHDSI) is an open, international collaborative that develops and maintains the OMOP Common Data Model, standardized clinical vocabularies, and open-source analytics tooling for observational health research. In KG-Registry, this entry represents the parent OHDSI ecosystem that publishes OMOP specifications and distributes standardized vocabulary access through Athena.
domains:
  - clinical
  - biomedical
  - health
  - information technology
homepage_url: https://www.ohdsi.org/
id: ohdsi
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: OHDSI
products:
  - category: GraphicalInterface
    description: Main OHDSI web portal for community, documentation, working groups, and software resources
    format: http
    id: ohdsi.portal
    name: OHDSI Web Portal
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://www.ohdsi.org/
  - category: DataModelProduct
    description: OMOP Common Data Model specification and downloadable DDL artifacts maintained by the OHDSI community
    format: http
    id: ohdsi.omop_cdm
    name: OMOP Common Data Model
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: athena
        relation_type: prov:wasInformedBy
    product_url: https://ohdsi.github.io/CommonDataModel/
    repository: https://github.com/OHDSI/CommonDataModel
  - category: GraphicalInterface
    description: Athena web application for searching OHDSI standardized vocabularies and preparing OMOP vocabulary downloads
    format: http
    id: ohdsi.athena
    name: OHDSI Athena Vocabulary Browser
    original_source:
      - source: athena
        relation_type: prov:hadPrimarySource
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://athena.ohdsi.org/search-terms/start
    warnings:
      - Athena is an authenticated web application; access to vocabulary download workflows requires login.
  - category: Product
    description: Standardized vocabulary bundles for OMOP CDM assembled through the Athena authenticated web application
    format: csv
    id: ohdsi.athena_vocabularies
    name: OHDSI Standardized Vocabulary Downloads
    original_source:
      - source: athena
        relation_type: prov:hadPrimarySource
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://athena.ohdsi.org/vocabulary/list
    warnings:
      - Athena vocabulary downloads are prepared through the logged-in web application; stable direct public file URLs are not exposed.
  - category: ProcessProduct
    description: OHDSI methods suite for standardized analytics on OMOP CDM data, including characterization, population-level effect estimation, and patient-level prediction
    format: http
    id: ohdsi.hades
    name: HADES
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://ohdsi.github.io/Hades/
    repository: https://github.com/OHDSI/Hades
  - category: ProcessProduct
    description: R package used to dynamically generate OMOP CDM documentation and DDL scripts for supported SQL dialects
    format: http
    id: ohdsi.cdm_r_package
    name: CDM R Package
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/CommonDataModel/
    repository: https://github.com/OHDSI/CommonDataModel
  - category: ProcessProduct
    description: Tool that runs more than 3,500 data quality checks against an OMOP CDM instance
    format: http
    id: ohdsi.data_quality_dashboard
    name: Data Quality Dashboard
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/DataQualityDashboard
    repository: https://github.com/OHDSI/DataQualityDashboard
  - category: ProcessProduct
    description: Package for broad database characterization against an OMOP CDM instance
    format: http
    id: ohdsi.achilles
    name: Achilles
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/Achilles
    repository: https://github.com/OHDSI/Achilles
  - category: ProcessProduct
    description: Application for displaying results from Achilles and Data Quality Dashboard to support data quality and characterization research
    format: http
    id: ohdsi.ares
    name: ARES
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/Ares
    repository: https://github.com/OHDSI/Ares
  - category: ProcessProduct
    description: Open-source software for conducting scientific analyses on standardized observational data
    format: http
    id: ohdsi.atlas
    name: ATLAS
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://atlas-demo.ohdsi.org/
    repository: https://github.com/OHDSI/Atlas
  - category: ProcessProduct
    description: Interactive ETL design application for mapping source data into the OMOP Common Data Model using WhiteRabbit scan results
    format: http
    id: ohdsi.rabbit_in_a_hat
    name: Rabbit-In-A-Hat
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/WhiteRabbit
    repository: https://github.com/OHDSI/WhiteRabbit
  - category: ProcessProduct
    description: Package for generating cohort covariates and other features from OMOP CDM data
    format: http
    id: ohdsi.feature_extraction
    name: Feature Extraction
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/FeatureExtraction
    repository: https://github.com/OHDSI/FeatureExtraction
  - category: ProcessProduct
    description: Package for evaluating and diagnosing cohort phenotype definitions built on OMOP CDM data
    format: http
    id: ohdsi.cohort_diagnostics
    name: Cohort Diagnostics
    original_source:
      - source: ohdsi
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/OHDSI/CohortDiagnostics
    repository: https://github.com/OHDSI/CohortDiagnostics
synonyms:
  - Observational Health Data Sciences and Informatics
taxon:
  - NCBITaxon:9606
---

# OHDSI

## Overview

OHDSI is the open collaborative behind the OMOP Common Data Model, the OHDSI standardized
vocabularies, and a broader ecosystem of open-source methods and tools for observational
health research.

This KG-Registry entry is intended to capture the parent OHDSI/OMOP context that
ties together the data model and the standardized vocabularies. The vocabulary browsing
surface itself is represented separately in the existing `athena` resource.

## Products

### OHDSI Web Portal

The main OHDSI site for community information, documentation, working groups, and
software links.

### OMOP Common Data Model

The community-maintained OMOP CDM specification and implementation artifacts, including
documentation and DDL downloads for supported database platforms.

### OHDSI Tooling

The OMOP CDM page also points to the main software stack used to build, validate,
characterize, and analyze OMOP-formatted data, including HADES, the CDM R package,
Data Quality Dashboard, Achilles, ARES, ATLAS, Rabbit-In-A-Hat, Feature Extraction,
and Cohort Diagnostics.

### OHDSI Standardized Vocabularies

The standardized vocabularies used across OMOP clinical domains and distributed through
Athena for browsing and download.
