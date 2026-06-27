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
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
name: FORUM
products:
- category: GraphicalInterface
  description: FORUM web application interface for semantic metabolomics exploration
  format: http
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
  format: http
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
  format: ttl
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
  description: Public SPARQL endpoint (OpenLink Virtuoso) providing query access to
    the complete FORUM knowledge graph. The former credentialed FTP tarball dump
    (2021) is no longer published; the SPARQL endpoint is the current canonical
    access point for the full RDF graph.
  format: http
  id: forum.graph.dump
  name: FORUM Knowledge Graph SPARQL Endpoint
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
  product_url: https://forum.semantic-metabolomics.fr/sparql
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