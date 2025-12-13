---
layout: resource_detail
activity_status: unresponsive
id: rdbridge
name: RDBridge
description: Rare Disease Bridge (RDBridge) offers search functions for genes, potential
  drugs, pathways, literature, and medical imaging data that will support mechanistic
  research, drug development, diagnosis, and treatment for rare diseases.
domains:
- health
- biomedical
- precision medicine
- clinical
contacts:
- category: Individual
  label: Qian-Nan Hu
  contact_details:
  - contact_type: email
    value: qnhu@sibs.ac.cn
homepage_url: http://rdb.lifesynther.com/
repository: http://rdb.lifesynther.com/
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
publications:
- doi: doi:10.1093/bioinformatics/btad440
  id: doi:10.1093/bioinformatics/btad440
  preferred: true
  year: '2023'
  journal: Bioinformatics
  authors:
  - Xing H
  - Zhang D
  - Cai P
  - Zhang R
  - Hu QN
  title: 'RDBridge: a knowledge graph of rare diseases based on large-scale text mining'
category: KnowledgeGraph
products:
- category: GraphicalInterface
  id: rdbridge.webinterface
  name: RDBridge Web Interface
  description: Graphical interface for exploring the RDBridge knowledge graph of rare
    diseases
  original_source:
  - rdbridge
  product_url: http://rdb.lifesynther.com/
  format: http
  is_public: true
- category: GraphProduct
  id: rdbridge.graph
  name: RDBridge Knowledge Graph
  description: Knowledge graph connecting rare diseases with genes, drugs, pathways,
    and medical images
  original_source:
  - rdbridge
  edge_count: 22293
  node_count: 11704
- category: Product
  id: rdbridge.literaturedatabase
  name: RDBridge Literature Database
  description: Curated collection of 235,631 scientific publications related to rare
    diseases
  original_source:
  - rdbridge
  format: http
warnings:
- Homepage may be inaccessible (March 5 2025)
taxon:
- NCBITaxon:9606
---

