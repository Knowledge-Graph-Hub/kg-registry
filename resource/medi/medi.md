---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: MeDI/MEDI is a curated dataset of medicines, diseases, indications, and
  contraindications for drug repurposing. The original Every Cure MATRIX Indication
  List repository is archived, with active development continued in the medic repository,
  which provides indication lists, drug lists, and regulatory source extracts.
domains:
- pharmacology
- drug discovery
- clinical
homepage_url: https://github.com/marcello-deluca/medic
id: medi
infores_id: medi
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: MeDI
products:
- category: ProcessProduct
  description: Active GitHub repository for MeDI/medic medicines, diseases, indications,
    and contraindications data and processing code
  format: http
  id: medi.github
  name: medic GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_url: https://github.com/marcello-deluca/medic
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: mondo
- category: Product
  description: Latest medic release of the MeDI dataset and related regulatory source
    extracts
  format: http
  id: medi.release
  name: MEDI Dataset Releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_url: https://github.com/marcello-deluca/medic/releases/tag/v1.0.1
- category: Product
  description: Matrix indication list spreadsheet from the medic v1.0.1 release
  id: medi.matrix_indication_list
  latest_version: v1.0.1
  name: Matrix Indication List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 2173559
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/matrix_indication_list.xlsx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:used
    source: mondo
- category: Product
  description: Flexible drug list CSV from the medic v1.0.1 release
  format: csv
  id: medi.drug_list_flexible
  latest_version: v1.0.1
  name: MeDI Flexible Drug List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 4428523
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/drug_list_flexible.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
- category: Product
  description: Stringent drug list CSV from the medic v1.0.1 release
  format: csv
  id: medi.drug_list_stringent
  latest_version: v1.0.1
  name: MeDI Stringent Drug List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 3672087
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/drug_list_stringent.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
- category: Product
  description: EMA regulatory source extract from the medic v1.0.1 release
  id: medi.ema
  latest_version: v1.0.1
  name: MeDI EMA Extract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 507869
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/ema.xlsx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ema
- category: Product
  description: PMDA regulatory source extract from the medic v1.0.1 release
  id: medi.pmda
  latest_version: v1.0.1
  name: MeDI PMDA Extract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 569703
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/pmda.xlsx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pmda
- category: Product
  description: FDA Orange Book regulatory source extract from the medic v1.0.1 release
  id: medi.orangebook
  latest_version: v1.0.1
  name: MeDI Orange Book Extract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 924266
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/orangebook.xlsx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: fda-orange-book
- category: ProcessProduct
  description: Archived Every Cure MATRIX Indication List repository that now points
    users to the medic repository
  format: http
  id: medi.legacy_github
  name: Archived MATRIX Indication List Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_url: https://github.com/everycure-org/matrix-indication-list
  warnings:
  - Repository is archived and deprecated in favor of https://github.com/marcello-deluca/medic.
- category: Product
  description: Curated TSV catalog of drug-disease indications classified as disease-modifying,
    symptomatic, or non-indications
  format: tsv
  id: pharmacotherapydb.indications
  name: PharmacotherapyDB Indications TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_file_size: 76754
  product_url: https://raw.githubusercontent.com/dhimmel/indications/gh-pages/catalog/indications.tsv
  secondary_source:
  - relation_type: prov:used
    source: doid
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:wasInformedBy
    source: labeledin
  - relation_type: prov:wasInformedBy
    source: medi
  - relation_type: prov:wasInformedBy
    source: ehrlink
  - relation_type: prov:wasInformedBy
    source: predict
repository: https://github.com/marcello-deluca/medic
taxon:
- NCBITaxon:9606
---
# MeDI (MATRIX Indication List)

## Overview

MEDI (MATRIX Indication List), now maintained through the `medic` repository, provides structured drug-indication and drug-contraindication relationships for drug repurposing research. The original Every Cure repository is archived and points users to the maintained `medic` repository.

## Data Content

MEDI includes:
- Drug indications extracted from DailyMed product labels
- Drug contraindications identified from safety information
- Mappings to standardized disease ontology terms (MONDO)
- Ground truth datasets for training predictive models

## Extraction Methodology

The dataset is generated through:
- Automated extraction from FDA DailyMed using LLMs
- Integration with EMA (European Medicines Agency) and PMDA (Pharmaceuticals and Medical Devices Agency) indications data
- Systematic normalization and mapping to MONDO ontology terms
- Quality control and validation processes

## Use Cases

MEDI serves as:
- Training data for drug repurposing prediction models
- Reference dataset for validating computational drug repositioning approaches
- Source of structured drug-disease relationships for knowledge graphs
- Ground truth for evaluating machine learning models in pharmacology

## Technical Implementation

The project uses:
- Jupyter Notebooks for data processing pipelines
- Automated data ingestion from DailyMed, EMA, and PMDA sources
- MONDO ontology integration for disease term standardization
- Version-controlled releases on GitHub

## Developed By

Every Cure organization, with primary development by Marcello DeLuca and contributors.

## Access

The dataset and processing code are freely available through the GitHub repository with regular versioned releases.