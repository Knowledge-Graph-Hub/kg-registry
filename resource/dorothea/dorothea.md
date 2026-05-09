---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-11T00:00:00Z'
description: "DoRothEA is a curated resource of transcription factor (TF) – target gene (regulon) interactions with confidence scoring, enabling inference of TF activity from gene expression data. It integrates literature-curated interactions and various experimental evidence (e.g. ChIP-seq, TF binding motifs, perturbation data) to build context-agnostic and confidence-stratified regulons for multiple species. Frequently used with PROGENy to estimate pathway and TF activities."
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
    description: "Core TF–target regulon knowledge graph (multi-species) with confidence levels (A–E)"
    id: dorothea.graph
    name: DoRothEA Regulon Graph
    product_url: https://github.com/saezlab/dorothea/releases/tag/v1.0.0
    original_source:
      - source: dorothea
        relation_type: prov:hadPrimarySource
  - category: ProcessProduct
    description: R package containing regulon data and helper functions for TF activity inference
    format: http
    id: dorothea.r-package
    name: DoRothEA R Package
    product_url: https://github.com/saezlab/dorothea/
    original_source:
      - source: dorothea
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Project documentation, usage examples, and methodological notes
    format: http
    id: dorothea.docs
    name: DoRothEA Documentation
    product_url: https://saezlab.github.io/dorothea/articles/dorothea.html
    original_source:
      - source: dorothea
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: achilles
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ccle
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: cellosaurus
        relation_type: prov:hadPrimarySource
      - source: clue
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pharmacodb
        relation_type: prov:hadPrimarySource
      - source: prism
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: offsides
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: repohub
        relation_type: prov:hadPrimarySource
      - source: chemicalchecker
        relation_type: prov:hadPrimarySource
      - source: repodb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: creeds
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: dorothea
        relation_type: prov:hadPrimarySource
      - source: progeny
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: huri
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: omnipath
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - source: bioteque
        relation_type: prov:wasInfluencedBy
publications:
  - doi: 10.1101/gr.240663.118
    id: doi:10.1101/gr.240663.118
    journal: Genome Research
    title: Benchmark and integration of resources for the estimation of human transcription factor activities
    year: '2019'
  - doi: 10.1101/2023.03.30.534849
    id: doi:10.1101/2023.03.30.534849
    journal: bioRxiv
    title: Expanding the coverage of regulons from high-confidence prior knowledge for accurate estimation of transcription factor activities
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
