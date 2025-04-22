---
layout: resource_detail
activity_status: active
id: drug-approvals-kp
name: Drug Approvals KP
description: A Translator knowledge provider focused on drug approval status and other drug-related metadata.
domains:
- health
category: KnowledgeGraph
contacts:
- category: Individual
  label: Gwênlyn Glusman
  contact_details:
  - contact_type: email
    value: gglusman@isbscience.org
  - contact_type: github
    value: gglusman
repository: https://github.com/multiomicsKP/drug_approvals_kp
products:
- id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  description: Nodes for the Drug Approvals KP, v0.3.7
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.7.tsv
  category: GraphProduct
  format: kgx
  secondary_source:
  - drug-approvals-kp
  original_source:
  - chebi
  - do
  - hp
  - mondo
- id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Nodes
  description: Nodes for the Drug Approvals KP, v0.3.7
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.7.tsv
  category: GraphProduct
  format: kgx
  secondary_source:
  - drug-approvals-kp
  original_source:
  - chebi
  - do
  - hp
  - mondo
- id: drug-approvals-kp.code
  name: Drug Approvals KP code
  description: Code for the Drug Approvals KP
  product_url: https://github.com/multiomicsKP/drug_approvals_kp
  category: ProcessProduct
  secondary_source:
  - drug-approvals-kp
  original_source:
  - drug-approvals-kp
collection:
- translator
---

Drug Approvals KP
