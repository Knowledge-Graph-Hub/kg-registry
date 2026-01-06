---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: EpistasisLab
  - contact_type: url
    value: https://alzkb.ai/
  label: Joseph D Romano
curators:
- category: Individual
  contact_details:
  - contact_type: github
    value: caufieldjh
  label: Harry Caufield
description: A knowledge base for AI research in Alzheimer Disease, based on graph
  databases.
domains:
- neuroscience
- biomedical
- health
- drug discovery
- genomics
homepage_url: https://alzkb.ai/Home
id: alzkb
layout: resource_detail
name: Alzheimer's Knowledge Base
products:
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
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
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
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
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
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
  doi: doi:10.2196/46777
  id: https://doi.org/10.2196/46777
  journal: Journal of Medical Internet Research
  preferred: true
  title: 'The Alzheimer''s Knowledge Base: A Knowledge Graph for Alzheimer Disease
    Research'
  year: '2024'
repository: https://github.com/EpistasisLab/AlzKB
taxon:
- NCBITaxon:9606
---
The Alzheimer's Knowledge Base (AlzKB) is a comprehensive knowledge graph for Alzheimer's Disease research. It integrates data from 22 diverse public biomedical databases into a unified knowledge representation, providing a platform for AI-driven research and drug discovery/repurposing.

AlzKB contains 118,902 distinct nodes representing biomedical entities (genes, drugs, diseases, pathways, etc.) and 1,309,527 relationships between them. The knowledge graph is built using an OWL 2 ontology that enforces semantic consistency and enables ontological inference.

The knowledge base is designed to facilitate tasks such as predicting genetic targets for new drugs and identifying drugs that could be repurposed for Alzheimer's Disease treatment.

## Automated Evaluation

- View the automated evaluation: [alzkb automated evaluation](alzkb_eval_automated.html)
