---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: caripark@iastate.edu
  - contact_type: github
    value: caripark
  label: Carissa Park
  orcid: 0000-0002-2346-5201
creation_date: '2025-09-29T00:00:00Z'
description: An ontology of traits covering vertebrates
domains:
- phenotype
homepage_url: https://github.com/AnimalGenome/vertebrate-trait-ontology
id: vt
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Vertebrate trait ontology
products:
- category: OntologyProduct
  description: Vertebrate trait ontology in OWL format
  format: owl
  id: vt.owl
  name: vt.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 416669
  product_url: http://purl.obolibrary.org/obo/vt.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Vertebrate Trait Ontology (VT), produced by KG-Bioportal
    from the BioPortal submission. The archive contains VT_nodes.tsv and VT_edges.tsv.
  edge_count: 4953
  format: kgx
  id: vt.kg-bioportal
  latest_version: '2026-07-23'
  name: VT KGX graph (KG-Bioportal)
  node_count: 4116
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 200324
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/VT.tar.gz
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
  - Carissa A Park
  - Susan M Bello
  - Cynthia L Smith
  - Zhi-Liang Hu
  - Diane H Munzenmaier
  - Rajni Nigam
  - Jennifer R Smith
  - Mary Shimoyama
  - Janan T Eppig
  - James M Reecy
  doi: 10.1186/2041-1480-4-13
  id: https://www.ncbi.nlm.nih.gov/pubmed/23937709
  journal: J Biomed Semantics
  preferred: true
  title: 'The Vertebrate Trait Ontology: a controlled vocabulary for the annotation
    of trait data across species'
  year: '2013'
repository: https://github.com/AnimalGenome/vertebrate-trait-ontology
---
## Description

An ontology of traits covering vertebrates

## Contacts

- Carissa Park (caripark@iastate.edu) [ORCID: 0000-0002-2346-5201](https://orcid.org/0000-0002-2346-5201)

## Products

### vt.owl

Vertebrate trait ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/vt.owl](http://purl.obolibrary.org/obo/vt.owl)

**Format**: owl

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*