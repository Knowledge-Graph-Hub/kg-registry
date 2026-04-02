---
activity_status: active
category: KnowledgeGraph
collection:
- translator
creation_date: '2026-02-18T00:00:00Z'
description: Genetics KP is a Translator knowledge provider focused on integrating
  genetic association evidence (including GWAS-derived signals) into a unified framework
  for gene-disease relationship analysis.
domains:
- genomics
- health
- translational
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Genetics-Knowledge-Provider
id: geneticskp
last_modified_date: '2026-02-18T00:00:00Z'
layout: resource_detail
name: Genetics KP
products:
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Genetics KP distributed via the NCATS Translator
    release site (release 2026_03_27; build geneticskp_2026-03-27_1f1ad62b_2025sep1_4.3.6;
    source version 2026-03-27; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 653544
  format: kgx-jsonl
  id: translator.geneticskp.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Genetics KP KGX Graph
  node_count: 28023
  original_source:
  - geneticskp
  product_url: https://kgx-storage.rtx.ai/releases/geneticskp/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - geneticskp_2026-03-27_1f1ad62b_2025sep1_4.3.6
- category: ProgrammingInterface
  description: Translator Reasoner API endpoint for Genetics KP.
  format: http
  id: geneticskp.trapi
  name: Genetics KP TRAPI Endpoint
  original_source:
  - geneticskp
  product_url: https://genetics-kp.transltr.io/genetics_provider/trapi/v1.4/
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
repository: https://github.com/broadinstitute/genetics-kp-dev
tags:
- translator
---
# Genetics KP

Genetics KP contributes Translator-compatible genetic evidence and associations.