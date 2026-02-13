---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: edgargaticaCU
  label: Edgar Gatica
- category: Individual
  contact_details:
  - contact_type: github
    value: bill-baumgartner
  label: Bill Baumgartner
creation_date: '2026-01-22T00:00:00Z'
description: Translator Text Mining Provider that produces knowledge-graph assertions
  from literature mining workflows and exposes them as a KGX graph.
domains:
- biomedical
- literature
- translational
homepage_url: https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap
id: text-mining-kp
last_modified_date: '2026-01-22T00:00:00Z'
layout: resource_detail
name: Text Mining KP
products:
- category: GraphProduct
  description: Release files for the Text Mining KP
  id: text-mining-kp.graph
  name: Text Mining KP Release Files
  product_url: https://storage.googleapis.com/translator-text-workflow-dev-public/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2026-02-04_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-13: No Content-Length
    header found'
- category: GraphProduct
  description: KGX graph package for Text Mining KP (build tmkp_tmkp-2023-03-05_1.0_2025sep1_4.3.6;
    release 2025_12_15)
  format: kgx
  id: translator.tmkp.graph
  name: Translator TMKP KGX Graph
  original_source:
  - text-mining-kp
  product_url: https://stars.renci.org/var/translator/releases/tmkp/2025_12_15/
  secondary_source:
  - translator
repository: https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap
synonyms:
- tmkp
tags:
- translator
---
Text Mining KP produces literature-mined knowledge graph assertions for Translator.

## Automated Evaluation

- View the automated evaluation: [text-mining-kp automated evaluation](text-mining-kp_eval_automated.html)