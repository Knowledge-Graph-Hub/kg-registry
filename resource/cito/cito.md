---
activity_status: active
category: Ontology
creation_date: '2025-12-11T00:00:00Z'
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
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: CiTO
products:
- category: OntologyProduct
  description: CiTO ontology in Turtle RDF format
  format: ttl
  id: cito.ttl
  name: CiTO Turtle File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cito
  product_file_size: 53618
  product_url: http://purl.org/spar/cito.ttl
- category: DocumentationProduct
  description: CiTO documentation and specification
  id: cito.documentation
  name: CiTO Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cito
  product_url: https://sparontologies.github.io/cito/current/cito.html
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
  - File was not able to be retrieved when checked on 2026-03-30_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2026-06-15: FTP error: timed
    out'
  - 'File was not able to be retrieved when checked on 2026-06-16: FTP error: timed
    out'
repository: https://github.com/sparontologies/cito
---
CiTO