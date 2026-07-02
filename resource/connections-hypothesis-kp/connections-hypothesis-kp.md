---
activity_status: active
category: KnowledgeGraph
collection:
  - translator
contacts:
  - category: Individual
    label: Gregory Hyde
description: A Translator Knowledge Provider exploring connections hypotheses.
domains:
  - biomedical
homepage_url: https://github.com/di2ag/chp_api
id: connections-hypothesis-kp
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: Connections Hypothesis KP
products:
  - category: GraphProduct
    description: Bayesian-network knowledge graph served by the Connections Hypothesis
      Provider over the Translator TRAPI interface. Inference is computed over a breast
      cancer dataset from The Cancer Genome Atlas (TCGA), supporting queries relating
      genetic, therapeutic, and patient clinical features to patient survival.
    format: http
    id: connections-hypothesis-kp.graph
    name: Connections Hypothesis KP Knowledge Graph
    original_source:
      - source: connections-hypothesis-kp
        relation_type: prov:hadPrimarySource
      - source: tcga
        relation_type: prov:hadPrimarySource
    product_url: https://smart-api.info/registry?q=412af63e15b73e5a30778aac84ce313f
  - category: ProcessProduct
    description: Source code for the Connections Hypothesis Provider API implementation.
    format: http
    id: connections-hypothesis-kp.code
    name: Connections Hypothesis KP Source Code
    original_source:
      - source: connections-hypothesis-kp
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/di2ag/chp_api/tree/production
  - category: DocumentationProduct
    description: SmartAPI registry listing for CHP service metadata and interface documentation.
    format: http
    id: connections-hypothesis-kp.smartapi
    name: Connections Hypothesis KP SmartAPI Entry
    original_source:
      - source: connections-hypothesis-kp
        relation_type: prov:hadPrimarySource
    product_url: https://smart-api.info/registry?q=412af63e15b73e5a30778aac84ce313f
creation_date: '2025-03-09T00:00:00Z'
---

A Translator Knowledge Provider exploring connections hypotheses.

## Automated Evaluation

- View the automated evaluation: [connections-hypothesis-kp automated evaluation](connections-hypothesis-kp_eval_automated.html)
