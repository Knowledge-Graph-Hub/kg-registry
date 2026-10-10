---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: hoganwr@gmail.com
  - contact_type: github
    value: hoganwr
  label: William Hogan
  orcid: 0000-0002-9881-1017
creation_date: '2025-09-29T00:00:00Z'
description: An OWL2 ontology of phenomena in infectious disease epidemiology and
  population biology for use in epidemic simulation.
domains:
- biomedical
- infectious disease
- public health
- epidemiology
homepage_url: https://github.com/ApolloDev/apollo-sv
id: apollo_sv
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Apollo Structured Vocabulary
products:
- category: OntologyProduct
  description: Apollo Structured Vocabulary in OWL format
  format: owl
  id: apollo_sv.owl
  name: apollo_sv.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  product_file_size: 264551
  product_url: http://purl.obolibrary.org/obo/apollo_sv.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Apollo Structured Vocabulary (APOLLO-SV), produced
    by KG-Bioportal from the BioPortal submission. The archive contains APOLLO-SV_nodes.tsv
    and APOLLO-SV_edges.tsv.
  edge_count: 3597
  format: kgx
  id: apollo_sv.kg-bioportal
  latest_version: '2026-07-19'
  name: APOLLO-SV KGX graph (KG-Bioportal)
  node_count: 2334
  original_source:
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  product_file_size: 112213
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/APOLLO-SV.tar.gz
- category: OntologyProduct
  description: Sickle Cell Disease Ontology in OWL format
  format: owl
  id: scdo.owl
  name: scdo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scdo
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  - relation_type: prov:hadPrimarySource
    source: aro
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: cmo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dron
  - relation_type: prov:hadPrimarySource
    source: duo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eupath
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: ico
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: idomal
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: opmi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: symp
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 367519
  product_url: http://purl.obolibrary.org/obo/scdo.owl
- category: OntologyProduct
  description: Sickle Cell Disease Ontology in OBO format
  format: obo
  id: scdo.obo
  name: scdo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scdo
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  - relation_type: prov:hadPrimarySource
    source: aro
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: cmo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dron
  - relation_type: prov:hadPrimarySource
    source: duo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eupath
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: ico
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: idomal
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: opmi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: symp
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 324416
  product_url: http://purl.obolibrary.org/obo/scdo.obo
publications:
- authors:
  - William R. Hogan
  - Michael M. Wagner
  - Mathias Brochhausen
  - John Levander
  - Shawn T. Brown
  - Nicholas Millett
  - Jay DePasse
  - Josh Hanna
  doi: 10.1186/s13326-016-0092-y
  id: https://doi.org/10.1186/s13326-016-0092-y
  journal: Journal of Biomedical Semantics
  title: 'The Apollo Structured Vocabulary: an OWL2 ontology of phenomena in infectious
    disease epidemiology and population biology for use in epidemic simulation'
  year: '2016'
repository: https://github.com/ApolloDev/apollo-sv
---
## Description

An OWL2 ontology of phenomena in infectious disease epidemiology and population biology for use in epidemic simulation.

## Contacts

- William Hogan (hoganwr@gmail.com) [ORCID: 0000-0002-9881-1017](https://orcid.org/0000-0002-9881-1017)

## Products

### apollo_sv.owl

Apollo Structured Vocabulary in OWL format

**URL**: [http://purl.obolibrary.org/obo/apollo_sv.owl](http://purl.obolibrary.org/obo/apollo_sv.owl)

**Format**: owl

## Publications

- [The Apollo Structured Vocabulary: an OWL2 ontology of phenomena in infectious disease epidemiology and population biology for use in epidemic simulation](https://doi.org/10.1186/s13326-016-0092-y)

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*