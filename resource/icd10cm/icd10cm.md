---
activity_status: active
category: Ontology
collection:
- omop
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: nchsicd10cm@cdc.gov
  - contact_type: url
    value: https://www.cdc.gov/nchs/icd/icd-10-cm/index.html
  label: NCHS ICD-10-CM (National Center for Health Statistics, CDC)
creation_date: '2025-10-30T00:00:00Z'
description: ICD-10-CM (International Classification of Diseases, 10th Revision, Clinical
  Modification) is a clinical modification of the WHO's ICD-10 system, providing diagnostic
  codes used for billing, epidemiology, and health management in the United States,
  with greater specificity than the international version.
domains:
- clinical
- biomedical
homepage_url: https://icd10cmtool.cdc.gov/
id: icd10cm
infores_id: icd10cm
last_modified_date: '2026-04-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.cdc.gov/other/agencymaterials.html
  label: Public Domain
name: ICD-10-CM
products:
- category: GraphicalInterface
  description: Interactive web-based search tool for ICD-10-CM codes
  format: http
  id: icd10cm.tool
  name: ICD-10-CM Browser Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  product_url: https://icd10cmtool.cdc.gov/
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
- category: GraphProduct
  description: KGX distribution of the SRI-Reference KG
  format: kgx
  id: sri-reference-kg.graph
  name: SRI-Reference KG (KGX distribution)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: decipher
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  - relation_type: prov:hadPrimarySource
    source: cureid
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_file_size: 230046094
  product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
synonyms:
- ICD-10-CM
- ICD10 Clinical Modification
- International Classification of Diseases, 10th Revision, Clinical Modification
taxon:
- NCBITaxon:9606
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