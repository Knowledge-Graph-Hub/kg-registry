---
layout: resource_detail
activity_status: active
id: drkg
name: Drug Repurposing Knowledge Graph
description: >-
  Drug Repurposing Knowledge Graph (DRKG) is a
  comprehensive biological knowledge graph relating
  genes, compounds, diseases, biological processes,
  side effects and symptoms.
domain: health
contacts:
- category: Individual
  orcid: 0000-0002-8367-0733
  github: https://github.com/bioannidis
  label: Vassilis N. Ioannidis
homepage_url: https://github.com/gnn4dr/DRKG
repository: https://github.com/gnn4dr/DRKG
category: KnowledgeGraph
products:
- id: drkg.graph
  name: DRKG graph
  description: >-
    DRKG graph files, including a TSV of triples,
    embeddings, ID mappings, and a glossary of
    relation types.
  url: https://dgl-data.s3-us-west-2.amazonaws.com/dataset/DRKG/drkg.tar.gz
  compression: targz
  category: GraphProduct
  derived_from: drkg
  original_source: drkg
---

Drug Repurposing Knowledge Graph (DRKG)
