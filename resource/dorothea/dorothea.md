---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-11T00:00:00Z'
description: "DoRothEA is a curated resource of transcription factor (TF) \u2013 target\
  \ gene (regulon) interactions with confidence scoring, enabling inference of TF\
  \ activity from gene expression data. It integrates literature-curated interactions\
  \ and various experimental evidence (e.g. ChIP-seq, TF binding motifs, perturbation\
  \ data) to build context-agnostic and confidence-stratified regulons for multiple\
  \ species. Frequently used with PROGENy to estimate pathway and TF activities."
domains:
- genomics
- biological systems
- biomedical
homepage_url: https://saezlab.github.io/dorothea/
id: dorothea
last_modified_date: '2025-09-11T00:00:00Z'
layout: resource_detail
name: DoRothEA
products:
- category: GraphProduct
  description: "Core TF\u2013target regulon knowledge graph (multi-species) with confidence\
    \ levels (A\u2013E)"
  id: dorothea.graph
  name: DoRothEA Regulon Graph
  product_url: https://github.com/saezlab/dorothea/releases/tag/v1.0.0
- category: ProcessProduct
  description: R package containing regulon data and helper functions for TF activity
    inference
  format: http
  id: dorothea.r-package
  name: DoRothEA R Package
  product_url: https://github.com/saezlab/dorothea/
- category: DocumentationProduct
  description: Project documentation, usage examples, and methodological notes
  format: http
  id: dorothea.docs
  name: DoRothEA Documentation
  product_url: https://saezlab.github.io/dorothea/articles/dorothea.html
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- doi: 10.1101/gr.240663.118
  id: doi:10.1101/gr.240663.118
  journal: Genome Research
  title: Benchmark and integration of resources for the estimation of human transcription
    factor activities
  year: '2019'
- doi: 10.1101/2023.03.30.534849
  id: doi:10.1101/2023.03.30.534849
  journal: bioRxiv
  title: Expanding the coverage of regulons from high-confidence prior knowledge for
    accurate estimation of transcription factor activities
  year: '2023'
---
# DoRothEA

## Overview

DoRothEA provides a curated, confidence-stratified collection of transcription factor (TF) to target gene interactions (regulons) across species. It aggregates multiple evidence sources (literature curation, ChIP-seq, in silico TF binding predictions, expression perturbation signatures) to support robust TF activity inference from transcriptomic data.

## Contents

- TF–target interactions labeled with confidence levels (A–E)
- Multi-species coverage (human, mouse; others via orthology mapping)
- R data objects and utilities for integration in analysis pipelines

## Access

- GitHub repository (releases, source, issues)
- R package install via devtools / GitHub
- Documentation site with examples and method description

## Usage

Often paired with PROGENy for complementary pathway and TF activity inference. Users subset regulons by confidence level (e.g., A–C) to balance coverage and specificity.

## Citation

Please cite the 2019 Nature Communications paper and, where appropriate, the latest preprint/update.

## Automated Evaluation

- View the automated evaluation: [dorothea automated evaluation](dorothea_eval_automated.html)
