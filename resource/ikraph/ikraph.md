---
layout: resource_detail
activity_status: active
id: ikraph
name: iKraph
description: "A large-scale KG assembled from PubMed abstracts."
category: KnowledgeGraph
homepage_url: https://biokde.insilicom.com/
repository: https://github.com/myinsilicom/iKraph
domains:
  - health
publications:
  - authors:
    - Zhang Y
    - Sui X
    - Pan F
    - Yu K
    - Li K
    - Tian S
    - Erdengasileng A
    - Han Q
    - Wang W
    - Wang J
    - Wang J
    - Sun D
    - Chung H
    - Zhou J
    - Zhou E
    - Lee B
    - Zhang P
    - Qiu X
    - Zhao T
    - Zhang J
    title: "A comprehensive large-scale biomedical knowledge graph for AI-powered data-driven biomedical research"
    doi: 10.1038/s42256-025-01014-w
    preferred: true
contacts:
  - category: Individual
    label: "Jinfeng Zhang"
    email: jinfeng@insilicom.com
products:
- category: GraphicalInterface
  description: Biomedical Knowledge Discovery Engine. Interface for iKraph
  id: ikraph.site
  name: BioKDE
  original_source:
  - ikraph
  product_url: https://biokde.insilicom.com/
  secondary_source:
  - ikraph
- id: ikraph.code
  name: iKraph Code
  description: Code for named entity recognition, relation extraction, and drug repurposing in assembly and analysis of iKraph
  product_url: https://github.com/myinsilicom/iKraph
  category: ProcessProduct
  secondary_source:
  - ikraph
  original_source:
  - ikraph
- id: ikraph.graph
  name: iKraph graph metadata
  description: Graph metadata for iKraph, including a list of relations, entity type-specific metadata, data sources, and drug repurposing predictions.
  product_url: https://zenodo.org/records/14851275/files/data.tar.gz?download=1
  category: GraphProduct
  secondary_source:
  - ikraph
  original_source:
  - ikraph
  compression: targz
  format: json
- id: ikraph.graph
  name: iKraph graph data
  description: Graph data for iKraph
  product_url: https://zenodo.org/records/14851275/files/iKraph_full.tar.gz?download=1
  category: GraphProduct
  secondary_source:
  - ikraph
  original_source:
  - ikraph
  compression: targz