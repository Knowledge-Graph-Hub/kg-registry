---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-12-11T00:00:00Z'
description: FORUM is a Knowledge Graph providing a semantic representation of relations
  between chemicals and biomedical concepts. It is built from a federation of life
  science databases and scientific literature repositories. FORUM supports metabolomics
  studies by enabling the identification of biomarkers and classification of individuals
  through comprehensive chemical-concept associations.
domains:
- chemistry and biochemistry
- biomedical
homepage_url: https://forum-webapp.semantic-metabolomics.fr/
id: forum
last_modified_date: '2026-05-28T00:00:00Z'
layout: resource_detail
name: FORUM
products:
- category: GraphicalInterface
  description: FORUM web application interface for semantic metabolomics exploration
  id: forum.webapp
  name: FORUM Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://forum-webapp.semantic-metabolomics.fr/
- category: ProgrammingInterface
  description: FORUM REST API for programmatic access to chemical-disease associations
  id: forum.api
  name: FORUM API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://forum-webapp.semantic-metabolomics.fr/#/openapi-documentation
- category: DocumentationProduct
  description: FORUM VoID (Vocabulary of Interlinked Datasets) metadata describing
    the knowledge graph structure
  id: forum.void
  name: FORUM VoID Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 96461
  product_url: https://forum.semantic-metabolomics.fr/.well-known/void
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete
    FORUM data
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cheminf
  - relation_type: prov:hadPrimarySource
    source: chemont
  - relation_type: prov:hadPrimarySource
    source: cito
  - relation_type: prov:hadPrimarySource
    source: dc
  - relation_type: prov:hadPrimarySource
    source: fabio
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: skos
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: FTP error: timed
    out'
  - File was not able to be retrieved when checked on 2026-03-30_ FTP error_ timed
    out
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
  title: 'FORUM: building a Knowledge Graph from public databases and scientific literature
    to extract associations between chemicals and diseases'
  year: '2021'
repository: https://github.com/eMetaboHUB/Forum-DiseasesChem
---
FORUM

## Automated Evaluation

- View the automated evaluation: [forum automated evaluation](forum_eval_automated.html)