---
activity_status: active
category: KnowledgeGraph
description: FORUM is a Knowledge Graph providing a semantic representation of relations
  between chemicals and biomedical concepts. It is built from a federation of life
  science databases and scientific literature repositories. FORUM supports metabolomics
  studies by enabling the identification of biomarkers and classification of individuals
  through comprehensive chemical-concept associations.
domains:
- chemistry and biochemistry
- metabolomics
- biomedical
homepage_url: https://forum-webapp.semantic-metabolomics.fr/
id: forum
layout: resource_detail
name: FORUM
repository: https://github.com/eMetaboHUB/Forum-DiseasesChem
products:
- category: GraphicalInterface
  description: FORUM web application interface for semantic metabolomics exploration
  id: forum.webapp
  name: FORUM Web Application
  product_url: https://forum-webapp.semantic-metabolomics.fr/
- category: ProgrammingInterface
  description: FORUM REST API for programmatic access to chemical-disease associations
  id: forum.api
  name: FORUM API
  product_url: https://forum-webapp.semantic-metabolomics.fr/#/openapi-documentation
- category: DocumentationProduct
  description: FORUM VoID (Vocabulary of Interlinked Datasets) metadata describing the knowledge graph structure
  id: forum.void
  name: FORUM VoID Metadata
  product_url: https://forum.semantic-metabolomics.fr/.well-known/void
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete FORUM data
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  original_source:
  - mesh
  - chebi
  - cito
  - fabio
  - dc
  - cheminf
  - skos
  - chemont
  - pubchem
  - pubmed
  secondary_source:
  - forum
publications:
- authors:
  - Delmas M
  - Filangi O
  - Paulhe N
  - Vinson F
  - Duperier C
  - Garrier W
  - Saunier PE
  - Pitarch Y
  - Jourdan F
  - Giacomoni F
  - Frainay C
  doi: 10.1093/bioinformatics/btab627
  id: doi:10.1093/bioinformatics/btab627
  journal: Bioinformatics
  preferred: true
  title: 'FORUM: building a Knowledge Graph from public databases and scientific literature to extract associations between chemicals and diseases'
  year: '2021'
---

FORUM
