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
last_modified_date: '2026-05-28T00:00:00Z'
layout: resource_detail
name: Text Mining KP
products:
- category: GraphProduct
  description: Release files for the Text Mining KP
  id: text-mining-kp.graph
  name: Text Mining KP Release Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://storage.googleapis.com/translator-text-workflow-dev-public/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for TMKP distributed via the NCATS Translator
    release site (release 2026_03_06; build tmkp_tmkp-2023-03-05_6dadae40_2025sep1_4.3.6;
    source version tmkp-2023-03-05; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 1861988
  format: kgx-jsonl
  id: translator.tmkp.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator TMKP KGX Graph
  node_count: 32276
  original_source:
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/tmkp/latest/
  versions:
  - '2026_03_06'
  - tmkp_tmkp-2023-03-05_6dadae40_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
repository: https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap
synonyms:
- tmkp
tags:
- translator
---
Text Mining KP produces literature-mined knowledge graph assertions for Translator.

## Automated Evaluation

- View the automated evaluation: [text-mining-kp automated evaluation](text-mining-kp_eval_automated.html)