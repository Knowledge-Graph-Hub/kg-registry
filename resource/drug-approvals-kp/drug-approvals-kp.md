---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: gglusman@isbscience.org
  - contact_type: github
    value: gglusman
  label: "Gw\xEAnlyn Glusman"
creation_date: '2025-04-22T00:00:00Z'
description: A Translator knowledge provider focused on drug approval status and other
  drug-related metadata.
domains:
- health
- pharmacology
- drug discovery
- biomedical
id: drug-approvals-kp
last_modified_date: '2026-01-06T00:00:00Z'
layout: resource_detail
name: Drug Approvals KP
products:
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - doid
  - hp
  - mondo
  product_file_size: 701451
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Edges for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Edges
  original_source:
  - chebi
  - doid
  - hp
  - mondo
  product_file_size: 31052966
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_edges_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
- category: ProcessProduct
  description: Code for the Drug Approvals KP
  id: drug-approvals-kp.code
  name: Drug Approvals KP code
  original_source:
  - drug-approvals-kp
  product_url: https://github.com/multiomicsKP/drug_approvals_kp
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Drug Approvals KP distributed via the NCATS
    Translator release site (release 2026_03_19; build dakp_0.5.3_c3f74ab4_2025sep1_4.3.6;
    source version 0.5.3; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 73999
  format: kgx-jsonl
  id: translator.dakp.graph
  latest_version: '2026_03_19'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator DAKP KGX Graph
  node_count: 3783
  original_source:
  - drug-approvals-kp
  product_url: https://kgx-storage.rtx.ai/releases/dakp/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_19'
  - dakp_0.5.3_c3f74ab4_2025sep1_4.3.6
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
repository: https://github.com/multiomicsKP/drug_approvals_kp
---
Drug Approvals KP

## Automated Evaluation

- View the automated evaluation: [drug-approvals-kp automated evaluation](drug-approvals-kp_eval_automated.html)