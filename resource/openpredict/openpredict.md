---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://openpredict.semanticscience.org/
  label: Institute for Data Science at Maastricht University
creation_date: '2025-11-05T00:00:00Z'
description: OpenPredict is an NCATS Translator Knowledge Provider that provides machine
  learning-based predictions for drug-target interactions and drug-disease associations
  to support drug repurposing. OpenPredict integrates multiple biomedical knowledge
  graphs and applies various machine learning algorithms to predict potential therapeutic
  uses for existing drugs. The service offers predictions with confidence scores and
  provides evidence trails linking drugs to diseases through intermediate biological
  entities like targets and pathways.
domains:
- drug discovery
- pharmacology
- precision medicine
- translational
- biomedical
homepage_url: https://openpredict.semanticscience.org/
id: openpredict
infores_id: openpredict
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: OpenPredict
products:
- category: ProgrammingInterface
  description: TRAPI-compliant API for drug repurposing predictions
  format: http
  id: openpredict.api
  name: OpenPredict API
  original_source:
  - openpredict
  product_url: https://openpredict.semanticscience.org/
- category: GraphicalInterface
  description: Web interface for exploring drug repurposing predictions
  format: http
  id: openpredict.ui
  name: OpenPredict Web Interface
  original_source:
  - openpredict
  product_url: https://openpredict.semanticscience.org/
- category: Product
  description: Pre-computed drug-disease predictions
  format: mixed
  id: openpredict.predictions
  name: OpenPredict Prediction Data
  original_source:
  - openpredict
  product_url: https://openpredict.semanticscience.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-05_ HTTP 405 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-06_ HTTP 405 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-09: HTTP 405 error
    when accessing file'
publications:
- id: https://doi.org/10.1093/bioinformatics/btab540
repository: https://github.com/MaastrichtU-IDS/translator-openpredict
synonyms:
- OpenPredict
- OpenPredict API
tags:
- translator
---
# OpenPredict

## Overview

OpenPredict is an NCATS Translator Knowledge Provider that provides machine learning-based predictions for drug-target interactions and drug-disease associations to support drug repurposing.

Developed at the Institute for Data Science at Maastricht University, OpenPredict integrates multiple biomedical knowledge graphs and applies various machine learning algorithms to identify potential new therapeutic uses for existing drugs.

## Key Features

- **Drug Repurposing**: Predictions of drug-disease associations for repurposing opportunities
- **Drug-Target Predictions**: Machine learning models for drug-target interactions
- **Multi-Algorithm Approach**: Ensemble of ML models for robust predictions
- **Confidence Scoring**: Probability scores for all predictions
- **Evidence Trails**: Provenance and reasoning paths for predictions
- **TRAPI Integration**: Part of the NCATS Translator ecosystem
- **Open Source**: Transparent methods and publicly accessible

## Machine Learning Approaches

OpenPredict employs multiple algorithms including:
- Knowledge graph embeddings
- Graph neural networks
- Matrix factorization
- Similarity-based methods
- Ensemble learning

## Products

### OpenPredict API
TRAPI-compliant RESTful API providing programmatic access to drug repurposing predictions and drug-target interaction predictions.

### OpenPredict Web Interface
Interactive web portal for exploring predictions, visualizing evidence trails, and accessing detailed information about drugs and diseases.

### OpenPredict Prediction Data
Pre-computed prediction datasets covering drug-disease and drug-target associations with confidence scores.

## Information Resource ID

This resource has the Information Resource identifier: `infores:openpredict`

## Publications

- [OpenPredict: a web server to predict drug-target interactions and drug-disease associations](https://doi.org/10.1093/bioinformatics/btab540) (2021)

## Repository

Source code and documentation: https://github.com/MaastrichtU-IDS/translator-openpredict

## Domains

- Drug Discovery
- Pharmacology
- Precision Medicine
- Translational
- Biomedical

## Tags

- NCATS Translator