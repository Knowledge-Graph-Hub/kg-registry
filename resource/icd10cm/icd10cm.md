---
activity_status: active
category: Ontology
creation_date: '2025-10-30T00:00:00Z'
description: ICD-10-CM (International Classification of Diseases, 10th Revision, Clinical
  Modification) is a clinical modification of the WHO's ICD-10 system, providing diagnostic
  codes used for billing, epidemiology, and health management in the United States,
  with greater specificity than the international version.
domains:
- clinical
- health
homepage_url: https://icd10cmtool.cdc.gov/
id: icd10cm
infores_id: icd10cm
last_modified_date: '2025-11-26T00:00:00Z'
layout: resource_detail
name: ICD-10-CM
products:
- category: GraphicalInterface
  description: Interactive web-based search tool for ICD-10-CM codes
  format: http
  id: icd10cm.tool
  name: ICD-10-CM Browser Tool
  original_source:
  - icd10cm
  product_url: https://icd10cmtool.cdc.gov/
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
  - File was not able to be retrieved when checked on 2025-12-05_ Error connecting
    to URL_ Exceeded 30 redirects.
  - 'File was not able to be retrieved when checked on 2025-12-08: Error connecting
    to URL: Exceeded 30 redirects.'
synonyms:
- ICD-10-CM
- ICD10 Clinical Modification
- International Classification of Diseases, 10th Revision, Clinical Modification
---
# ICD-10-CM

## Overview

ICD-10-CM (International Classification of Diseases, 10th Revision, Clinical Modification) is the United States' clinical modification of the World Health Organization's ICD-10 system. It provides a standardized system of diagnostic codes used throughout the US healthcare system for billing, epidemiological tracking, health management, and clinical documentation.

## Key Features

- **Greater Specificity**: More detailed codes than the international ICD-10 version
- **Clinical Detail**: Enhanced to capture clinical concepts important to US healthcare
- **Laterality**: Specifies left, right, or bilateral for paired organs
- **Episode of Care**: Indicates initial encounter, subsequent encounter, or sequela
- **Combination Codes**: Single codes for frequently co-occurring conditions
- **Regular Updates**: Annual updates to reflect new diseases and clinical advances

## Structure

ICD-10-CM codes consist of 3-7 alphanumeric characters:
- **First character**: Alphabetic (A-Z)
- **Second character**: Numeric (0-9)
- **Characters 3-7**: Alphanumeric providing additional specificity
- **7th character**: Extension for encounter type (initial, subsequent, sequela)

## Code Categories

### Disease Index
Diagnostic codes organized by disease entity, covering:
- Infectious and parasitic diseases
- Neoplasms
- Diseases of body systems
- Congenital malformations
- Symptoms and abnormal findings

### External Causes
Codes for injuries and external causes including:
- Accidents and injuries
- Environmental factors
- Activity codes
- Place of occurrence

### Drugs and Chemicals
Codes for:
- Poisoning by drugs and chemicals
- Adverse effects
- Underdosing

### Neoplasms
Detailed neoplasm codes organized by:
- Anatomical site
- Behavior (malignant, benign, uncertain, unspecified)

## Applications

- **Medical Billing**: Required for health insurance claims in the US
- **Epidemiology**: Tracking disease patterns and public health surveillance
- **Health Statistics**: Population health reporting and research
- **Clinical Documentation**: Standard terminology for medical records
- **Quality Measurement**: Healthcare quality metrics and reporting
- **Resource Allocation**: Health planning and management
- **Research**: Clinical and health services research

## Integration

ICD-10-CM is integrated into:
- Electronic Health Record (EHR) systems
- Medical billing software
- Public health surveillance systems
- Clinical decision support tools
- Athena (OHDSI vocabulary mappings)
- Terminology mapping services
- Knowledge graphs (UBKG)

## Maintenance

ICD-10-CM is maintained by:
- **National Center for Health Statistics (NCHS)**: Part of the CDC
- **Centers for Medicare & Medicaid Services (CMS)**

Annual updates are released on October 1st each fiscal year.

## Access

- **CDC ICD-10-CM Tool**: Interactive browser at https://icd10cmtool.cdc.gov/
- **FTP Downloads**: Code files, guidelines, and documentation
- **Mapping Files**: Crosswalks to ICD-9-CM and other terminologies

## Related Standards

- **ICD-10**: International version (less detailed)
- **ICD-10-PCS**: Procedure Coding System (used with ICD-10-CM for inpatient procedures)
- **SNOMED CT**: More granular clinical terminology
- **ICD-11**: Next generation (not yet adopted in US)

## Compliance

ICD-10-CM has been mandatory for all HIPAA-covered entities in the United States since October 1, 2015.

## Citation

When using ICD-10-CM data, cite: Centers for Disease Control and Prevention, National Center for Health Statistics. ICD-10-CM Official Guidelines and code sets.