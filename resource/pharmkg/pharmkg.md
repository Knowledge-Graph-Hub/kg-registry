---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: MindRank-Biotech
  - contact_type: url
    value: https://github.com/MindRank-Biotech/PharmKG
  label: MindRank Biotech
description: >-
  PharmKG is a multi-relational, attributed biomedical knowledge graph benchmark
  that integrates curated databases and literature-derived relationships to link
  genes, drugs (chemicals), and diseases. It contains ~500,000 typed relations
  across ~7,600–8,000 disambiguated entities (29 relation types), with
  domain-specific features for entities from multi-omics sources (e.g., gene
  expression, chemical structure, disease embeddings). It provides baselines for
  knowledge graph embedding and a neural network-based method, and supports
  downstream tasks such as drug repurposing and target identification.
domains:
- biomedical
- drug discovery
- pharmacology
- health
homepage_url: https://github.com/MindRank-Biotech/PharmKG
id: pharmkg
layout: resource_detail
name: PharmKG
products:
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes, chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  secondary_source:
  - pharmkg
  product_url: https://zenodo.org/record/4077338
publications:
- authors:
  - Shuangjia Zheng
  - Jiahua Rao
  - Ying Song
  - Jixian Zhang
  - Xianglu Xiao
  - Evandro Fei Fang
  - Yuedong Yang
  - Zhangming Niu
  doi: 10.1093/bib/bbaa344
  id: doi:10.1093/bib/bbaa344
  journal: Briefings in Bioinformatics
  title: "PharmKG: a dedicated knowledge graph benchmark for biomedical data mining"
  year: '2021'
repository: https://github.com/MindRank-Biotech/PharmKG
---
PharmKG