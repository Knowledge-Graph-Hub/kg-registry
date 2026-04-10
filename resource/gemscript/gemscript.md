---
activity_status: active
category: DataSource
collection:
- omop
creation_date: '2026-04-10T00:00:00Z'
description: Gemscript is a medication and device terminology used primarily within
  the UK's Vision 3 general practice software. Maintained by RESIP UK and integrated
  with dm+d-aligned descriptions, Gemscript provides unique internal drug identifiers
  and associated prescribing metadata used to select, classify, and manage medicines
  and appliances in active clinical workflows. Although Gemscript remains in active
  operational use, its distribution appears to occur through Vision update channels
  rather than a single public bulk-download site.
domains:
- clinical
- health
- pharmacology
homepage_url: https://help.visionhealth.co.uk/DLM860/consultation_manager/Content/Whats%20New.htm
id: gemscript
last_modified_date: '2026-04-10T00:00:00Z'
layout: resource_detail
name: Gemscript
products:
- category: DocumentationProduct
  description: Vision help documentation describing Gemscript as the integrated drug
    dictionary used in Vision 3 prescribing workflows
  format: http
  id: gemscript.documentation
  name: Gemscript Vision Help Documentation
  original_source:
  - gemscript
  product_url: https://help.visionhealth.co.uk/DLM860/consultation_manager/Content/Whats%20New.htm
- category: DocumentationProduct
  description: Monthly Gemscript bulletin summarizing additions, deletions, name changes,
    and drug class changes in the active dictionary
  format: pdf
  id: gemscript.bulletin
  name: Gemscript Monthly Bulletin
  original_source:
  - gemscript
  product_file_size: 166947
  product_url: https://help.visionhealth.co.uk/PDFs/Dictionaries/Gemscript/Gemscript_Bulletin_Mar_2025.pdf
- category: Product
  description: Downloadable standardized vocabulary bundles for OMOP CDM assembled
    through the authenticated Athena web application
  format: csv
  id: athena.vocabularies
  name: Athena Vocabulary Downloads
  original_source:
  - snomedct
  - icd10
  - icd10cm
  - mesh
  - loinc
  - cdiscvocab
  - ciel
  - rxnorm
  - ndcd
  - gemscript
  - medispan-gpi
  product_url: https://athena.ohdsi.org/vocabulary/list
  secondary_source:
  - athena
  warnings:
  - Athena vocabulary downloads are prepared through the logged-in web application;
    stable direct public file URLs are not exposed.
synonyms:
- Gemscript Drug Dictionary
- GemscriptDrug
taxon:
- NCBITaxon:9606
---
# Gemscript

## Overview

Gemscript is a drug and device coding system used within Vision 3 in UK primary care.
Vision documentation describes it as an integrated dm+d drug dictionary maintained
by RESIP UK and used to support prescribing, drug selection, drug class browsing,
and related medication workflows.

Gemscript identifiers are internal numeric codes used in operational software contexts.
Public documentation about the terminology exists, but distribution of full dictionary
updates appears to occur through Vision download and update mechanisms rather than
through a single openly documented bulk download site.

## Products

### Gemscript Vision Help Documentation

Official Vision help material describing the introduction and operational use of Gemscript
in prescribing workflows.

### Gemscript Monthly Bulletin

Representative public release bulletin documenting monthly dictionary additions, deletions,
and maintenance changes.