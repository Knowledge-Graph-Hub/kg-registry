---
activity_status: active
category: Aggregator
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
  Data Model format for federated research across multiple healthcare systems.
domains:
- clinical
- biomedical
- health
- information technology
homepage_url: https://athena.ohdsi.org/
id: athena
infores_id: athena
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: Athena
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing standardized vocabularies
  format: http
  id: athena.web
  name: Athena Vocabulary Browser
  original_source:
  - athena
  product_url: https://athena.ohdsi.org/search-terms/start
- category: Product
  description: Downloadable standardized vocabulary bundles for OMOP CDM
  format: csv
  id: athena.vocabularies
  name: Athena Vocabulary Downloads
  original_source:
  - athena
  product_url: https://athena.ohdsi.org/vocabulary/list
  warnings:
  - File was not able to be retrieved when checked on 2025-12-07_ Error connecting
    to URL_ Exceeded 30 redirects.
  - File was not able to be retrieved when checked on 2025-12-08_ Error connecting
    to URL_ Exceeded 30 redirects.
  - 'File was not able to be retrieved when checked on 2025-12-08: Error connecting
    to URL: Exceeded 30 redirects.'
- category: MappingProduct
  description: Concept mappings between different terminology systems
  format: csv
  id: athena.mappings
  name: Athena Concept Mappings
  original_source:
  - snomedct
  - icd10
  - icd10cm
  - mesh
  - loinc
  - cdiscvocab
  - ciel
  product_url: https://athena.ohdsi.org/search-terms/start
  secondary_source:
  - athena
  warnings:
  - File was not able to be retrieved when checked on 2025-12-07_ Error connecting
    to URL_ Exceeded 30 redirects.
  - File was not able to be retrieved when checked on 2025-12-08_ Error connecting
    to URL_ Exceeded 30 redirects.
  - 'File was not able to be retrieved when checked on 2025-12-08: Error connecting
    to URL: Exceeded 30 redirects.'
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
- **Free Access**: Public access to standardized vocabularies for research
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
Web-based interface for searching, browsing, and exploring standardized vocabularies and their relationships.

### Vocabulary Downloads
Downloadable vocabulary bundles in CSV format for local implementation in OMOP CDM databases.

### Concept Mappings
Cross-vocabulary mappings enabling interoperability between different terminology systems.

## Information Resource ID

This resource has the Information Resource identifier: `infores:athena`

## Domains

- Clinical
- Biomedical
- Health
- Information Technology

## Taxon Coverage

Human (NCBITaxon:9606)