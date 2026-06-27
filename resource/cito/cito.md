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
last_modified_date: '2026-06-18T00:00:00Z'
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
  format: http
  id: cito.documentation
  name: CiTO Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cito
  product_url: https://sparontologies.github.io/cito/current/cito.html
- category: GraphProduct
  description: Public SPARQL endpoint (OpenLink Virtuoso) providing query access to
    the complete FORUM knowledge graph. The former credentialed FTP tarball dump (2021)
    is no longer published; the SPARQL endpoint is the current canonical access point
    for the full RDF graph.
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
  - Peroni S
  - Shotton D
  doi: 10.1016/j.websem.2012.08.001
  id: https://doi.org/10.1016/j.websem.2012.08.001
  journal: Journal of Web Semantics
  preferred: true
  title: 'FaBiO and CiTO: ontologies for describing bibliographic resources and citations'
  year: '2012'
repository: https://github.com/sparontologies/cito
---
CiTO