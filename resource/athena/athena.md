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
  label: OHDSI
creation_date: '2025-11-05T00:00:00Z'
description: Athena is the OHDSI (Observational Health Data Sciences and Informatics)
  standardized vocabulary repository that provides access to standardized terminologies
  and vocabularies for observational healthcare data. It includes SNOMED CT, RxNorm,
  LOINC, ICD codes, and many other standard vocabularies, along with mappings between
  them. Athena enables the transformation of healthcare data into the OMOP Common
  Data Model format for federated research across multiple healthcare systems. Access
  to vocabulary selection and download workflows is mediated through the Athena web
  application rather than stable public download URLs.
domains:
- clinical
- biomedical
- information technology
homepage_url: https://athena.ohdsi.org/
id: athena
infores_id: athena
last_modified_date: '2026-04-10T00:00:00Z'
layout: resource_detail
name: Athena
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing standardized vocabularies;
    account login is required for download workflows
  format: http
  id: athena.web
  name: Athena Vocabulary Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  product_url: https://athena.ohdsi.org/search-terms/start
  warnings:
  - Athena is an authenticated web application; access to vocabulary download workflows
    requires login.
- category: Product
  description: Downloadable standardized vocabulary bundles for OMOP CDM assembled
    through the authenticated Athena web application
  format: csv
  id: athena.vocabularies
  name: Athena Vocabulary Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: cdiscvocab
  - relation_type: prov:hadPrimarySource
    source: ciel
  - relation_type: prov:hadPrimarySource
    source: gemscript
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: medispan-gpi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: snomedct
  product_url: https://athena.ohdsi.org/vocabulary/list
  warnings:
  - Athena vocabulary downloads are prepared through the logged-in web application;
    stable direct public file URLs are not exposed.
- category: MappingProduct
  description: Concept mappings between different terminology systems
  format: csv
  id: athena.mappings
  name: Athena Concept Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: cdiscvocab
  - relation_type: prov:hadPrimarySource
    source: ciel
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: snomedct
  product_url: https://athena.ohdsi.org/search-terms/start
  warnings:
  - Athena mapping exports are accessed through the authenticated Athena web application;
    stable direct public file URLs are not exposed.
- category: DataModelProduct
  description: OMOP Common Data Model specification and downloadable DDL artifacts
    maintained by the OHDSI community
  format: http
  id: ohdsi.omop_cdm
  name: OMOP Common Data Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohdsi
  product_url: https://ohdsi.github.io/CommonDataModel/
  repository: https://github.com/OHDSI/CommonDataModel
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: athena
- category: GraphicalInterface
  description: Athena web application for searching OHDSI standardized vocabularies
    and preparing OMOP vocabulary downloads
  format: http
  id: ohdsi.athena
  name: OHDSI Athena Vocabulary Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: ohdsi
  product_url: https://athena.ohdsi.org/search-terms/start
  warnings:
  - Athena is an authenticated web application; access to vocabulary download workflows
    requires login.
- category: Product
  description: Standardized vocabulary bundles for OMOP CDM assembled through the
    Athena authenticated web application
  format: csv
  id: ohdsi.athena_vocabularies
  name: OHDSI Standardized Vocabulary Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: ohdsi
  product_url: https://athena.ohdsi.org/vocabulary/list
  warnings:
  - Athena vocabulary downloads are prepared through the logged-in web application;
    stable direct public file URLs are not exposed.
synonyms:
- Athena
- OHDSI Athena
taxon:
- NCBITaxon:9606
---
# Athena

## Overview

Athena is the OHDSI (Observational Health Data Sciences and Informatics) standardized vocabulary repository that provides access to standardized terminologies and vocabularies for observational healthcare data.

It includes major healthcare terminologies such as SNOMED CT, RxNorm, LOINC, ICD-10, ICD-9CM, CPT, and many others, along with comprehensive mappings between them. Athena is essential for transforming healthcare data into the OMOP Common Data Model (CDM) format.

## Key Features

- **Comprehensive Vocabularies**: 100+ standardized terminologies and code systems
- **Concept Mappings**: Extensive mappings between different terminology systems
- **OMOP CDM Support**: Vocabularies formatted for OMOP Common Data Model
- **Regular Updates**: Frequent updates to maintain currency with source vocabularies
- **Account-Based Access**: Vocabulary selection and download workflows are handled
  through the Athena web application
- **Concept Search**: Advanced search capabilities across all vocabularies

## Integrated Vocabularies

Athena includes:
- Clinical terminologies (SNOMED CT, ICD-10, ICD-9CM, CPT)
- Drug vocabularies (RxNorm, NDC, ATC)
- Laboratory codes (LOINC)
- Procedure codes (CPT, HCPCS, ICD-10-PCS)
- Observation codes (UCUM, READ)
- And many more specialized vocabularies

## Products

### Athena Vocabulary Browser
Web-based interface for searching, browsing, and exploring standardized vocabularies and their relationships. Athena is exposed as an authenticated web application rather than as a stable set of public direct-download URLs.

### Vocabulary Downloads
Downloadable vocabulary bundles in CSV format for local implementation in OMOP CDM databases. In practice, these are selected and prepared within the logged-in Athena interface, so the registry points to the Athena entry page rather than to a stable file URL.

### Concept Mappings
Cross-vocabulary mappings enabling interoperability between different terminology systems. As with vocabulary downloads, Athena exposes these through the web application workflow rather than stable public file links.

## Information Resource ID

This resource has the Information Resource identifier: `infores:athena`

## Domains

- Clinical
- Biomedical
- Health
- Information Technology

## Taxon Coverage

Human (NCBITaxon:9606)