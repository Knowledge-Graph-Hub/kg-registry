---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: https://github.com/bioannidis
    label: Vassilis N. Ioannidis
    orcid: 0000-0002-8367-0733
description: Drug Repurposing Knowledge Graph (DRKG) is a comprehensive biological knowledge graph relating genes, compounds, diseases, biological processes, side effects and symptoms.
domains:
  - health
homepage_url: https://github.com/gnn4dr/DRKG
id: drkg
layout: resource_detail
name: Drug Repurposing Knowledge Graph
products:
  - category: GraphProduct
    compression: targz
    description: DRKG graph files, including a TSV of triples, embeddings, ID mappings, and a glossary of relation types.
    id: drkg.graph
    name: DRKG graph
    original_source:
      - source: drkg
        relation_type: prov:hadPrimarySource
    product_file_size: 216650245
    product_url: https://dgl-data.s3-us-west-2.amazonaws.com/dataset/DRKG/drkg.tar.gz
  - category: GraphProduct
    description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing and integrating information from diverse biomedical resources including DRKG, iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome, SIDER, and others).
    id: ibkh.graph
    name: iBKH Knowledge Graph
    original_source:
      - source: drkg
        relation_type: prov:hadPrimarySource
      - source: idisk
        relation_type: prov:hadPrimarySource
      - source: brenda
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: pharmgkb
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
repository: https://github.com/gnn4dr/DRKG
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-01-06T00:00:00Z'
---

Drug Repurposing Knowledge Graph (DRKG)

## Automated Evaluation

- View the automated evaluation: [drkg automated evaluation](drkg_eval_automated.html)
