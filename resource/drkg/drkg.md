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
description: Drug Repurposing Knowledge Graph (DRKG) is a comprehensive biological
  knowledge graph relating genes, compounds, diseases, biological processes, side
  effects and symptoms.
domains:
- health
homepage_url: https://github.com/gnn4dr/DRKG
id: drkg
layout: resource_detail
name: Drug Repurposing Knowledge Graph
products:
- category: GraphProduct
  compression: targz
  description: DRKG graph files, including a TSV of triples, embeddings, ID mappings,
    and a glossary of relation types.
  id: drkg.graph
  name: DRKG graph
  original_source:
  - drkg
  product_file_size: 216650245
  product_url: https://dgl-data.s3-us-west-2.amazonaws.com/dataset/DRKG/drkg.tar.gz
  secondary_source:
  - drkg
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - drkg
  - idisk
  - brenda
  - ctd
  - drugbank
  - kegg
  - pharmgkb
  - reactome
  - sider
  - tissues
  - bgee
  - doid
  - uberon
  - cl
  - hgnc
  - chembl
  - chebi
repository: https://github.com/gnn4dr/DRKG
---
Drug Repurposing Knowledge Graph (DRKG)