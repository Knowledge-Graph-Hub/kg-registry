---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: egon.willighagen@gmail.com
  - contact_type: github
    value: egonw
  label: Egon Willighagen
  orcid: 0000-0001-7542-0286
creation_date: '2025-09-29T00:00:00Z'
description: Includes terms for the descriptors commonly used in cheminformatics software
  applications and the algorithms which generate them.
domains:
- chemistry and biochemistry
homepage_url: https://github.com/semanticchemistry/semanticchemistry
id: cheminf
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Chemical Information Ontology
products:
- category: OntologyProduct
  description: Chemical Information Ontology in OWL format
  format: owl
  id: cheminf.owl
  name: cheminf.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cheminf
  product_file_size: 22830
  product_url: http://purl.obolibrary.org/obo/cheminf.owl
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
  - Hastings J
  - Chepelev L
  - Willighagen E
  - Adams N
  - Steinbeck C
  - Dumontier M
  doi: 10.1371/journal.pone.0025513
  id: https://www.ncbi.nlm.nih.gov/pubmed/21991315
  journal: PLoS One
  title: 'The chemical information ontology: provenance and disambiguation for chemical
    data on the biological semantic web'
  year: '2011'
repository: https://github.com/semanticchemistry/semanticchemistry
---
## Description

Includes terms for the descriptors commonly used in cheminformatics software applications and the algorithms which generate them.

## Contacts

- Egon Willighagen (egon.willighagen@gmail.com) [ORCID: 0000-0001-7542-0286](https://orcid.org/0000-0001-7542-0286)

## Products

### cheminf.owl

Chemical Information Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/cheminf.owl](http://purl.obolibrary.org/obo/cheminf.owl)

**Format**: owl

## Publications

- [The chemical information ontology: provenance and disambiguation for chemical data on the biological semantic web](https://www.ncbi.nlm.nih.gov/pubmed/21991315)

**Domains**: chemistry and biochemistry

---

*This resource was automatically synchronized from the OBO Foundry registry.*