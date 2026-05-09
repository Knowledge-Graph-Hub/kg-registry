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
    label: "Gwênlyn Glusman"
creation_date: '2025-04-22T00:00:00Z'
description: A Translator knowledge provider focused on drug approval status and other drug-related metadata.
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
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
    product_file_size: 701451
    product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.9.tsv
    secondary_source:
      - source: drug-approvals-kp
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Edges for the Drug Approvals KP, v0.3.9
    format: kgx
    id: drug-approvals-kp.graph.edges
    name: Drug Approvals KP Graph Edges
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
    product_file_size: 31052966
    product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_edges_v0.3.9.tsv
    secondary_source:
      - source: drug-approvals-kp
        relation_type: prov:wasInfluencedBy
  - category: ProcessProduct
    description: Code for the Drug Approvals KP
    id: drug-approvals-kp.code
    name: Drug Approvals KP code
    original_source:
      - source: drug-approvals-kp
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/multiomicsKP/drug_approvals_kp
    secondary_source:
      - source: drug-approvals-kp
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compatibility:
      - standard: biolink
        version: 4.3.6
    description: KGX JSONL graph package for Drug Approvals KP distributed via the NCATS Translator release site (release 2026_03_19; build dakp_0.5.3_c3f74ab4_2025sep1_4.3.6; source version 0.5.3; Biolink 4.3.6; Node Normalizer 2025sep1).
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
      - source: drug-approvals-kp
        relation_type: prov:hadPrimarySource
    product_url: https://kgx-storage.rtx.ai/releases/dakp/latest/
    secondary_source:
      - source: translator
        relation_type: prov:wasInfluencedBy
    versions:
      - '2026_03_19'
      - dakp_0.5.3_c3f74ab4_2025sep1_4.3.6
  - category: GraphProduct
    compatibility:
      - standard: biolink
        version: 4.3.6
    description: Aggregated KGX JSONL graph package combining 29 Translator release sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer 2025sep1).
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
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: cohd
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: ctkp
        relation_type: prov:hadPrimarySource
      - source: drug-approvals-kp
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: drugrephub
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: gene2phenotype
        relation_type: prov:hadPrimarySource
      - source: geneticskp
        relation_type: prov:hadPrimarySource
      - source: go-cam
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pathbank
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: text-mining-kp
        relation_type: prov:hadPrimarySource
      - source: ttd
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:hadPrimarySource
    product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
    secondary_source:
      - source: translator
        relation_type: prov:wasInfluencedBy
    versions:
      - '2026_03_27'
      - 423af7989cac
repository: https://github.com/multiomicsKP/drug_approvals_kp
---

Drug Approvals KP

## Automated Evaluation

- View the automated evaluation: [drug-approvals-kp automated evaluation](drug-approvals-kp_eval_automated.html)
