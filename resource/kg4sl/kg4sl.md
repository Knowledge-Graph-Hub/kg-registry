---
activity_status: active
category: KnowledgeGraph
creation_date: '2026-04-06T00:00:00Z'
description: KG4SL is a knowledge-graph neural network project for predicting synthetic lethal gene pairs in human cancers. It is released with SynLethKG, the supporting knowledge graph used for model training and evaluation.
domains:
  - biomedical
  - genomics
  - drug discovery
homepage_url: https://github.com/JieZheng-ShanghaiTech/KG4SL
id: kg4sl
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: KG4SL
products:
  - category: GraphProduct
    description: Data files for SynLethKG, the knowledge graph used by KG4SL and described as constructed from SynLethDB (v1.0/v2.0) and Hetionet.
    format: mixed
    id: kg4sl.synlethkg
    name: SynLethKG Data Files
    original_source:
      - source: kg4sl
        relation_type: prov:hadPrimarySource
      - source: synlethdb
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: hetionet
        relation_type: prov:wasInfluencedBy
    product_url: https://github.com/JieZheng-ShanghaiTech/KG4SL/tree/main/data
  - category: ProcessProduct
    description: Repository containing preprocessing, training, and evaluation code for KG4SL.
    format: mixed
    id: kg4sl.code
    license:
      id: https://opensource.org/licenses/MIT
      label: MIT License
    name: KG4SL Code
    original_source:
      - source: kg4sl
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/JieZheng-ShanghaiTech/KG4SL
publications:
- authors:
  - Shike Wang
  - Fan Xu
  - Yunyang Li
  - Jie Wang
  - Ke Zhang
  - Yong Liu
  - Min Wu
  - Jie Zheng
  doi: 10.1093/bioinformatics/btab271
  id: https://doi.org/10.1093/bioinformatics/btab271
  journal: Bioinformatics
  preferred: true
  title: 'KG4SL: knowledge graph neural network for synthetic lethality prediction in human cancers'
  year: '2021'
repository: https://github.com/JieZheng-ShanghaiTech/KG4SL
taxon:
  - NCBITaxon:9606
---

# KG4SL

KG4SL is a cancer-focused synthetic lethality prediction project built around a graph neural network. Its associated graph asset, SynLethKG, is released with the project as the structured knowledge graph used for model training and evaluation.
