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
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT license
name: OpenPredict
products:
- category: ProgrammingInterface
  description: TRAPI 1.4 API for predicted drug treatments, drug-disease associations,
    similar entities, model metadata, and explanation endpoints
  format: http
  id: openpredict.api
  name: OpenPredict API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openpredict
  secondary_source:
  - relation_type: prov:used
    source: biolink
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: omim
  product_url: https://openpredict.semanticscience.org/docs
- category: GraphicalInterface
  description: Swagger UI documentation for interactively exploring OpenPredict API
    operations and examples
  format: http
  id: openpredict.ui
  name: OpenPredict Swagger UI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openpredict
  product_url: https://openpredict.semanticscience.org/docs
- category: Product
  description: OpenAPI JSON specification describing OpenPredict TRAPI, prediction,
    similarity, model, and explanation endpoints
  format: json
  id: openpredict.openapi
  name: OpenPredict OpenAPI Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openpredict
  product_url: https://openpredict.semanticscience.org/openapi.json
- category: Product
  description: Pre-computed prediction outputs exposed through API operations for
    predicted drugs, predicted diseases, similar entities, and evidence paths
  format: mixed
  id: openpredict.predictions
  name: OpenPredict Prediction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openpredict
  secondary_source:
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: omim
  product_url: https://openpredict.semanticscience.org/docs
  warnings:
  - Prediction results are exposed through POST/GET API operations rather than as
    a stable public bulk data file.
publications:
- authors:
  - Remzi Celebi
  - Joao Rebelo Moreira
  - Ahmed A. Hassan
  - Sandeep Ayyar
  - Lars Ridder
  - Tobias Kuhn
  - Michel Dumontier
  category: Publication
  doi: 10.7717/peerj-cs.281
  id: doi:10.7717/peerj-cs.281
  journal: PeerJ Computer Science
  preferred: true
  title: 'Towards FAIR protocols and workflows: the OpenPREDICT use case'
  year: '2020'
- authors:
  - Assaf Gottlieb
  - Gideon Y. Stein
  - Eytan Ruppin
  - Roded Sharan
  category: Publication
  doi: 10.1038/msb.2011.26
  id: doi:10.1038/msb.2011.26
  journal: Molecular Systems Biology
  title: 'PREDICT: a method for inferring novel drug indications with application
    to personalized medicine'
  year: '2011'
repository: https://github.com/MaastrichtU-IDS/translator-openpredict
synonyms:
- OpenPredict
- OpenPredict API
tags:
- translator
taxon:
- NCBITaxon:9606
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
TRAPI-compliant RESTful API providing programmatic access to drug repurposing predictions, similar-entity queries, model metadata, and evidence/explanation endpoints.

### OpenPredict Web Interface
Swagger UI documentation for exploring predictions, visualizing API examples, and accessing detailed operation schemas for drugs and diseases.

### OpenPredict Prediction Data
Pre-computed prediction results are exposed through the API operations rather than through a stable public bulk-download file.

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
