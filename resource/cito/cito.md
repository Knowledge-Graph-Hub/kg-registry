---
activity_status: active
category: Ontology
description: CiTO (Citation Typing Ontology) is a formal ontology that provides a
  machine-readable vocabulary for describing the nature and type of citations within
  bibliographic references. It enables the semantic representation of the relationships
  between citing and cited scholarly works, supporting the analysis of citation networks
  and the characterization of how one publication cites another.
domains:
- literature
- general
homepage_url: https://sparontologies.github.io/cito/current/cito.html
id: cito
layout: resource_detail
name: CiTO
products:
- category: OntologyProduct
  description: CiTO ontology in Turtle RDF format
  format: ttl
  id: cito.ttl
  name: CiTO Turtle File
  product_file_size: 53618
  product_url: http://purl.org/spar/cito.ttl
- category: DocumentationProduct
  description: CiTO documentation and specification
  id: cito.documentation
  name: CiTO Documentation
  product_url: https://sparontologies.github.io/cito/current/cito.html
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
  - File was not able to be retrieved when checked on 2026-02-04_ FTP error_ timed
    out
  - File was not able to be retrieved when checked on 2026-01-30_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2026-02-13: FTP error: timed
    out'
repository: https://github.com/sparontologies/cito
---
CiTO