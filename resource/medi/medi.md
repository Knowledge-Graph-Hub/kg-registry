---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: MEDI (MATRIX Indication List) is a curated dataset of drug indications
  and contraindications extracted from FDA DailyMed product labels using large language
  models. Developed by the Every Cure organization, MEDI provides ground truth data
  for drug repurposing predictive models by mapping drug-indication and drug-contraindication
  relationships with standardized disease ontology terms (MONDO).
domains:
- pharmacology
- drug discovery
- clinical
homepage_url: https://github.com/everycure-org/matrix-indication-list
id: medi
infores_id: medi
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/everycure-org/matrix-indication-list/blob/main/LICENSE
  label: License (see repository)
name: MeDI
products:
- category: Product
  description: GitHub repository containing the MEDI dataset, extraction pipelines,
    and processing code for drug indications and contraindications
  format: mixed
  id: medi.github
  name: MEDI GitHub Repository
  original_source:
  - medi
  product_url: https://github.com/everycure-org/matrix-indication-list
- category: Product
  description: Latest release of the MEDI dataset containing curated drug-indication
    and drug-contraindication mappings
  id: medi.release
  name: MEDI Dataset Releases
  product_url: https://github.com/everycure-org/matrix-indication-list/releases
repository: https://github.com/everycure-org/matrix-indication-list
taxon:
- NCBITaxon:9606
---

# MeDI (MATRIX Indication List)

## Overview

MEDI (MATRIX Indication List) is a curated dataset developed by the Every Cure organization that provides structured drug-indication and drug-contraindication relationships extracted from FDA DailyMed product labels. The resource uses large language models (LLMs) to systematically extract therapeutic indications and contraindications from drug labels, providing high-quality ground truth data for computational drug repurposing research.

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
