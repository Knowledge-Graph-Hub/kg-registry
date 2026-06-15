---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-11-22T00:00:00Z'
description: KG-Predict is a knowledge graph computational framework for drug repurposing
  that integrates multiple types of genotypic and phenotypic data. The framework constructs
  GP-KG (Genotype-Phenotype Knowledge Graph), containing 1,246,726 associations between
  61,146 biomedical entities from various databases. KG-Predict uses graph embedding
  methods to learn low-dimensional representations of entities and relations, enabling
  inference of new drug-disease interactions. The system has been validated for identifying
  repositioned candidate drugs, particularly for Alzheimer's disease, achieving high
  performance metrics (AUROC = 0.981, AUPR = 0.409) and successfully prioritizing
  FDA-approved and clinical trial anti-AD drugs.
domains:
- drug discovery
- systems biology
- biomedical
- pharmacology
- genomics
- phenotype
homepage_url: https://nlp.case.edu/public/data/GPKG-Predict/
id: kg-predict
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://www.elsevier.com/open-access/userlicense/1.0/
  label: Elsevier User License
name: KG-Predict
products:
- category: GraphProduct
  description: GP-KG tab-delimited knowledge graph containing 1,246,726 associations
    between 61,146 entities from multiple genotypic and phenotypic databases
  format: tsv
  id: kg-predict.gpkg
  name: GP-KG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 48397035
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: umls
- category: ProcessProduct
  description: Python implementation of KG-Predict framework for graph embedding and
    drug repurposing prediction
  format: http
  id: kg-predict.code
  name: KG-Predict Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/code/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-12: Error connecting
    to URL: HTTPSConnectionPool(host=''nlp.case.edu'', port=443): Max retries exceeded
    with url: /public/data/GPKG-Predict/code/ (Caused by NewConnectionError("HTTPSConnection(host=''nlp.case.edu'',
    port=443): Failed to establish a new connection: [Errno 113] No route to host"))'
  - 'File was not able to be retrieved when checked on 2026-06-15: Timeout connecting
    to URL'
- category: DocumentationProduct
  description: Source data documentation for the GP-KG download
  format: http
  id: kg-predict.raw_data
  name: GP-KG Raw Data Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 17402
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/data/Raw_Data.docx
- category: Product
  description: Alzheimer's disease case study drug repurposing predictions
  format: csv
  id: kg-predict.ad_predictions
  name: AD Drug Predictions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 44034
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/case_study_predict_results.csv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clinicaltrialsgov
- category: Product
  description: Alzheimer's disease National Clinical Trial evidence file used with
    the KG-Predict case study
  format: csv
  id: kg-predict.ad_nct_evidence
  name: AD National Clinical Trial Evidence
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 1789
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/ad_nct_evidence.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: clinicaltrialsgov
publications:
- authors:
  - Zhenxiang Gao
  - Pingjian Ding
  - Rong Xu
  doi: 10.1016/j.jbi.2022.104133
  id: doi:10.1016/j.jbi.2022.104133
  journal: Journal of Biomedical Informatics
  title: 'KG-Predict: A knowledge graph computational framework for drug repurposing'
  year: '2022'
synonyms:
- GPKG-Predict
- GP-KG
taxon:
- NCBITaxon:9606
---
# KG-Predict

## Overview

KG-Predict is a computational framework designed for drug repurposing through knowledge graph embedding and inference. The system addresses the challenge of integrating and analyzing complex, heterogeneous biomedical data to identify new therapeutic applications for existing drugs.

The framework constructs GP-KG (Genotype-Phenotype Knowledge Graph), a comprehensive knowledge graph that integrates multiple types of entities and relations from various genotypic and phenotypic databases. GP-KG contains 1,246,726 associations between 61,146 biomedical entities, including drugs, diseases, genes, proteins, pathways, and phenotypes.

KG-Predict aggregates heterogeneous topological and semantic information from GP-KG to learn low-dimensional representations of entities and relations using advanced graph embedding techniques. These learned representations enable the inference of novel drug-disease interactions for drug repurposing applications.

## Key Features

- **Comprehensive Knowledge Graph**: GP-KG with 1,246,726 associations and 61,146 entities
- **Multi-modal Integration**: Combines genotypic and phenotypic data from multiple databases
- **Graph Embedding**: Advanced methods for learning entity and relation representations
- **High Performance**: AUROC = 0.981, AUPR = 0.409, MRR = 0.261 in cross-validation
- **Validated Applications**: Successfully applied to Alzheimer's disease drug discovery

## Performance

In cross-validation experiments, KG-Predict demonstrated superior performance compared to other state-of-the-art graph embedding methods:

- **AUROC** (Area Under Receiver Operating Characteristic): 0.981
- **AUPR** (Area Under Precision-Recall): 0.409
- **MRR** (Mean Reciprocal Rank): 0.261

## Case Study: Alzheimer's Disease

KG-Predict was applied to identify novel repositioned candidate drugs for Alzheimer's disease (AD), achieving:

- **AUROC**: 0.868
- **AUPR**: 0.364
- Successfully prioritized both FDA-approved and active clinical trial anti-AD drugs among top predictions

## Data Sources

GP-KG integrates data from multiple genotypic and phenotypic databases, including information about:

- Drug-disease associations
- Drug-target interactions
- Gene-disease associations
- Protein-protein interactions
- Pathway information
- Phenotypic data

## Technical Implementation

The framework is implemented in Python and includes:

- Configuration files for model parameters
- Data processing pipelines
- Graph embedding model implementations
- Training and testing scripts
- Case study analysis tools

## Automated Evaluation

- View the automated evaluation: [kg-predict automated evaluation](kg-predict_eval_automated.html)