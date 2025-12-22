---
activity_status: active
category: Ontology
description: FABIO (Functional Requirements for Bibliographic Records Object) is a
  comprehensive ontology for describing bibliographic resources and their properties.
  It extends the FRBR (Functional Requirements for Bibliographic Records) model into
  a machine-readable ontology format, enabling semantic representation of bibliographic
  entities, relationships, and metadata. FABIO supports the organization and discovery
  of scholarly works and publication resources across knowledge systems.
domains:
- literature
- general
homepage_url: https://sparontologies.github.io/fabio/current/fabio.html
id: fabio
layout: resource_detail
name: FABIO
products:
- category: OntologyProduct
  description: FABIO ontology in Turtle RDF format
  format: ttl
  id: fabio.ttl
  name: FABIO Turtle File
  product_file_size: 140152
  product_url: http://purl.org/spar/fabio.ttl
- category: DocumentationProduct
  description: FABIO ontology documentation, specification, and usage guidelines
  id: fabio.documentation
  name: FABIO Documentation
  product_url: https://sparontologies.github.io/fabio/current/fabio.html
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete
    FORUM data
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
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
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  secondary_source:
  - forum
  warnings:
  - File was not able to be retrieved when checked on 2025-12-18_ FTP error_ timed
    out
  - File was not able to be retrieved when checked on 2025-12-18_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2025-12-22: FTP error: timed
    out'
- category: OntologyProduct
  description: OpenBioDiv-O, the OpenBiodiv Ontology
  format: ttl
  id: openbiodiv.ontology.ttl
  is_public: true
  name: OpenBioDiv-O
  original_source:
  - skos
  - proton
  - fabio
  - doco
  - openbiodiv
  product_file_size: 8176
  product_url: https://raw.githubusercontent.com/pensoft/OpenBiodiv/refs/heads/master/ontology/openbiodiv-ontology-latest.ttl
  secondary_source:
  - openbiodiv
repository: https://github.com/SPAROntologies/fabio
---
FABIO