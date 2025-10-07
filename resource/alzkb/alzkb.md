---
layout: resource_detail
activity_status: active
id: alzkb
name: Alzheimer's Knowledge Base
description: A knowledge base for AI research in Alzheimer Disease, based on graph databases.
domains:
- neuroscience
- biomedical
- health
- drug discovery
- genomics
contacts:
- category: Individual
  label: Joseph D Romano
  contact_details:
  - contact_type: github
    value: EpistasisLab
  - contact_type: url
    value: https://alzkb.ai/
curators:
- category: Individual
  contact_details:
  - contact_type: github
    value: caufieldjh
  label: Harry Caufield
homepage_url: https://alzkb.ai/Home
repository: https://github.com/EpistasisLab/AlzKB
category: KnowledgeGraph
publications:
- id: https://doi.org/10.2196/46777
  title: "The Alzheimer's Knowledge Base: A Knowledge Graph for Alzheimer Disease Research"
  preferred: true
  authors:
  - Joseph D Romano
  - Van Truong
  - Rachit Kumar
  - Mythreye Venkatesan
  - Britney E Graham
  - Yun Hao
  - Nick Matsumoto
  - Xi Li
  - Zhiping Wang
  - Marylyn D Ritchie
  - Li Shen
  - Jason H Moore
  journal: Journal of Medical Internet Research
  year: "2024"
  doi: doi:10.2196/46777
products:
- id: alzkb.browser
  name: AlzKB Graph Database Browser
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  product_url: https://alzkb.ai:7473/login
  category: GraphicalInterface
  format: http
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  secondary_source:
  - alzkb
  - hetionet
- id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  description: Memgraph data release for AlzKB.
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  category: GraphProduct
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  secondary_source:
  - alzkb
  - hetionet
---

The Alzheimer's Knowledge Base (AlzKB) is a comprehensive knowledge graph for Alzheimer's Disease research. It integrates data from 22 diverse public biomedical databases into a unified knowledge representation, providing a platform for AI-driven research and drug discovery/repurposing.

AlzKB contains 118,902 distinct nodes representing biomedical entities (genes, drugs, diseases, pathways, etc.) and 1,309,527 relationships between them. The knowledge graph is built using an OWL 2 ontology that enforces semantic consistency and enables ontological inference.

The knowledge base is designed to facilitate tasks such as predicting genetic targets for new drugs and identifying drugs that could be repurposed for Alzheimer's Disease treatment.
