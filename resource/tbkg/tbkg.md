---
id: tbkg
layout: resource_detail
name: Tumor-Biomarker Knowledge Graph
description: A weighted heterogeneous knowledge graph containing four types of entities
  (Tumor, Biomarker, Drug, and ADR)  extracted from MEDLINE corpus for adverse drug
  reaction discovery in antitumor drugs. TBKG uses a naive  Bayesian model to explore
  correlations and provides explainable predictions through tumor-biomarker-drug  pathways.
  The knowledge graph contains 1,179 tumors, 2,550 biomarkers, 1,806 drugs, and 756
  ADRs with six  types of relationships totaling 139,254 edges.
category: KnowledgeGraph
activity_status: unknown
domains:
- drug discovery
- pharmacology
- biomedical
- clinical
- systems biology
- translational
homepage_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full
repository: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
publications:
- id: PMID:33584816
  title: Adverse Drug Reaction Discovery Using a Tumor-Biomarker Knowledge Graph
  authors:
  - Wang M
  - Ma X
  - Si J
  - Tang H
  - Wang H
  - Li T
  - Ouyang W
  - Gong L
  - Tang Y
  - He X
  - Huang W
  - Liu X
  journal: Frontiers in Genetics
  year: '2021'
  doi: 10.3389/fgene.2020.625659
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
creation_date: '2025-11-22T00:00:00Z'
last_modified_date: '2025-11-22T00:00:00Z'
products:
- id: tbkg.data
  name: TBKG Knowledge Graph Data
  description: Weighted heterogeneous knowledge graph extracted from MEDLINE corpus
    containing 1,179 tumors, 2,550 biomarkers, 1,806 drugs, and 756 ADRs with 139,254
    relationship edges (Tumor-Biomarker, Tumor-Drug, Tumor-ADR, Drug-Biomarker, Drug-ADR,
    Biomarker-ADR). Includes correlation weights calculated using naive Bayesian model.
  category: GraphProduct
  product_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
  original_source:
  - tbkg
- id: tbkg.osimertinib_case_study
  name: TBKG Osimertinib ADR Case Study Data
  description: Clinical validation dataset with calculated ADRs for osimertinib ranked
    by importance, biomarker pathways explaining drug-ADR relationships, and clinical
    data from 8 lung adenocarcinoma patients. Model achieved Kappa=0.68 concordance
    with official manual and 0.81 three-fold cross-validation accuracy.
  category: Product
  product_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
  original_source:
  - tbkg
taxon:
- NCBITaxon:9606
---

## Overview

TBKG (Tumor-Biomarker Knowledge Graph) is an explainable knowledge graph-based approach for discovering potential adverse drug reactions (ADRs) of antitumor drugs. The system extracts entities from biomedical literature (MEDLINE database with 22+ million citations) using the UMLS Metathesaurus 2020AA and Apache cTAKES natural language processing tool.

## Key Features

- **Entity Types**: Four node types (Tumor, Biomarker, Drug, ADR) with minimum frequency threshold of 50
- **Knowledge Graph Structure**: Weighted heterogeneous graph with undirected edges representing correlations
- **Relationship Discovery**: Naive Bayesian model combining prior and posterior probabilities to avoid bias
- **ADR Discovery**: Depth-first search algorithm to find all paths between drug-ADR pairs
- **Explainability**: Provides tumor-biomarker-drug pathways explaining predicted ADRs
- **Performance**: 0.81 accuracy in three-fold cross-validation, outperforms co-occurrence analysis

## Data Sources

- MEDLINE database (1928-2020, filtered with "cancer therapy" keyword)
- UMLS Metathesaurus 2020AA for entity dictionaries
- WHO source dictionary for ADR coding
- Clinical validation from 3rd Xiangya Hospital (8 patients, 2017-2020)

## Technical Implementation

- **Entity Extraction**: cTAKES NLP system with UMLS concept mapping
- **Importance Measure**: log(p(biomarker|tumor present)) - log(p(biomarker|tumor absent))
- **Graph Construction**: Binary matrix representation (0/1 for entity presence in abstracts)
- **Cross-validation**: Three-fold to prevent overfitting

## Clinical Validation

Osimertinib case study demonstrated:
- Moderate consistency with official manual (Kappa=0.68)
- Better specificity than co-occurrence methods (Kappa=0.4)
- Discovery of rare/unreported ADRs (e.g., renal failure requiring dialysis)
- Identification of mediating biomarkers (e.g., Macrophage-Activating Factors for nephrosclerosis)

## Applications

- Early ADR detection before drug development
- Mechanism research through biomarker pathways
- Clinical decision support for oncologists
- Literature-based drug safety surveillance
- Rare ADR discovery and explanation
