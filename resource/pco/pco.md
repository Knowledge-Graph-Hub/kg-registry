---
activity_status: active
category: Ontology
collection:
- obo-foundry
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: rlwalls2008@gmail.com
  - contact_type: github
    value: ramonawalls
  label: Ramona Walls
  orcid: 0000-0001-8815-0078
creation_date: '2025-09-29T00:00:00Z'
description: An ontology about groups of interacting organisms such as populations
  and communities
domains:
- environment
- ecology
homepage_url: https://github.com/PopulationAndCommunityOntology/pco
id: pco
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Population and Community Ontology
products:
- category: OntologyProduct
  description: Population and Community Ontology in OWL format
  format: owl
  id: pco.owl
  name: pco.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 62282
  product_url: http://purl.obolibrary.org/obo/pco.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Population and Community Ontology (PCO), produced
    by KG-Bioportal from the BioPortal submission. The archive contains PCO_nodes.tsv
    and PCO_edges.tsv.
  edge_count: 1052
  format: kgx
  id: pco.kg-bioportal
  latest_version: '2013-10-03'
  name: PCO KGX graph (KG-Bioportal)
  node_count: 558
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pco
  product_file_size: 27141
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/PCO.tar.gz
- category: OntologyProduct
  description: An ontology of core ecological entities in OWL format
  format: owl
  id: ecocore.owl
  name: ecocore.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocore
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1287569
  product_url: http://purl.obolibrary.org/obo/ecocore.owl
- category: OntologyProduct
  description: An ontology of core ecological entities in OBO format
  format: obo
  id: ecocore.obo
  name: ecocore.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocore
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 834439
  product_url: http://purl.obolibrary.org/obo/ecocore.obo
- category: OntologyProduct
  description: main ENVO OWL release
  format: owl
  id: envo.owl
  name: main ENVO OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 819909
  product_url: http://purl.obolibrary.org/obo/envo.owl
- category: OntologyProduct
  description: ENVO in obographs JSON format
  format: json
  id: envo.json
  name: ENVO in obographs JSON format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 653600
  product_url: http://purl.obolibrary.org/obo/envo.json
- category: OntologyProduct
  description: ENVO in OBO Format. May be lossy
  format: obo
  id: envo.obo
  name: ENVO in OBO Format. May be lossy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 595276
  product_url: http://purl.obolibrary.org/obo/envo.obo
- category: OntologyProduct
  description: OBO-Basic edition of ENVO
  format: obo
  id: envo.subsets.envo-basic.obo
  name: OBO-Basic edition of ENVO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 422465
  product_url: http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo
- category: OntologyProduct
  description: Earth Microbiome Project subset
  format: owl
  id: envo.subsets.envoEmpo.owl
  name: Earth Microbiome Project subset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 19016
  product_url: http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl
- category: OntologyProduct
  description: GSC Lite subset of ENVO
  format: obo
  id: envo.subsets.EnvO-Lite-GSC.obo
  name: GSC Lite subset of ENVO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 12912
  product_url: http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo
publications:
- authors:
  - Walls RL
  - Deck J
  - Guralnick R
  - Baskauf S
  - Beaman R
  - Blum S
  - Bowers S
  - Buttigieg PL
  - Davies N
  - Endresen D
  - Gandolfo MA
  - Hanner R
  - Janning A
  - Krishtalka L
  - Matsunaga A
  - Midford P
  - Morrison N
  - Tuama ÉÓ
  - Schildhauer M
  - Smith B
  - Stucky BJ
  - Thomer A
  - Wieczorek J
  - Whitacre J
  - Wooley J
  doi: 10.1371/journal.pone.0089606
  id: https://www.ncbi.nlm.nih.gov/pubmed/24595056
  journal: PLoS One
  preferred: true
  title: 'Semantics in Support of Biodiversity Knowledge Discovery: An Introduction
    to the Biological Collections Ontology and Related Ontologies'
  year: '2014'
repository: https://github.com/PopulationAndCommunityOntology/pco
---
## Description

An ontology about groups of interacting organisms such as populations and communities

## Contacts

- Ramona Walls (rlwalls2008@gmail.com) [ORCID: 0000-0001-8815-0078](https://orcid.org/0000-0001-8815-0078)

## Products

### pco.owl

Population and Community Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/pco.owl](http://purl.obolibrary.org/obo/pco.owl)

**Format**: owl

**Domains**: environment

---

*This resource was automatically synchronized from the OBO Foundry registry.*