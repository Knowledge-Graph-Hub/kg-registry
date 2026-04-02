---
activity_status: active
category: KnowledgeGraph
collection:
- translator
creation_date: '2026-02-18T00:00:00Z'
description: Clinical Trials Knowledge Provider (CTKP) is a Translator knowledge provider
  maintained by the Multiomics Provider that exposes clinical trial-derived associations
  from ClinicalTrials.gov (via AACT), including trial interventions, conditions, and
  related biomedical entities.
domains:
- clinical
- health
- translational
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Clinical-Trials-KP
id: ctkp
last_modified_date: '2026-02-18T00:00:00Z'
layout: resource_detail
name: Clinical Trials KP
products:
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for CTKP distributed via the NCATS Translator
    release site (release 2026_03_27; build ctkp_3.1.37_a99268cc_2025sep1_4.3.6; source
    version 3.1.37; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 438575
  format: kgx-jsonl
  id: translator.ctkp.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator CTKP KGX Graph
  node_count: 41243
  original_source:
  - ctkp
  product_url: https://kgx-storage.rtx.ai/releases/ctkp/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - ctkp_3.1.37_a99268cc_2025sep1_4.3.6
- category: DocumentationProduct
  description: Translator wiki documentation for Clinical Trials KP, including source
    and access details.
  format: http
  id: ctkp.docs
  name: Clinical Trials KP Documentation
  original_source:
  - ctkp
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Clinical-Trials-KP
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
  - alliance
  - bgee
  - bindingdb
  - chembl
  - cohd
  - ctd
  - ctkp
  - drug-approvals-kp
  - dgidb
  - diseases
  - drugrephub
  - drugcentral
  - gtopdb
  - gene2phenotype
  - geneticskp
  - go-cam
  - goa
  - hp
  - icees-kg
  - intact
  - ncbigene
  - panther
  - pathbank
  - semmeddb
  - sider
  - signor
  - text-mining-kp
  - ttd
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - 423af7989cac
repository: https://github.com/multiomicsKP/clinical_trials_kp
tags:
- translator
---
# Clinical Trials KP

CTKP provides Translator-facing clinical trial associations derived from ClinicalTrials.gov data.