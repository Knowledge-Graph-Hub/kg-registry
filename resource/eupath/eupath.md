---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jiezhen@med.umich.edu
  - contact_type: github
    value: zhengj2007
  label: Jie Zheng
  orcid: 0000-0002-2999-0103
creation_date: '2025-09-29T00:00:00Z'
description: An ontology is developed to support Eukaryotic Pathogen, Host & Vector
  Genomics Resource (VEuPathDB; https://veupathdb.org).
domains:
- organisms
- biomedical
- infectious disease
- microbiology
- host-pathogen interactions
homepage_url: https://github.com/VEuPathDB-ontology/VEuPathDB-ontology
id: eupath
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: VEuPathDB ontology
products:
- category: OntologyProduct
  description: VEuPathDB ontology in OWL format
  format: owl
  id: eupath.owl
  name: eupath.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eupath
  product_file_size: 438457
  product_url: http://purl.obolibrary.org/obo/eupath.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of VEuPathDB Ontology (EUPATH), produced by KG-Bioportal
    from the BioPortal submission. The archive contains EUPATH_nodes.tsv and EUPATH_edges.tsv.
  edge_count: 13057
  format: kgx
  id: eupath.kg-bioportal
  latest_version: '2023-05-30'
  name: EUPATH KGX graph (KG-Bioportal)
  node_count: 6164
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eupath
  product_file_size: 396273
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/EUPATH.tar.gz
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
  - Zheng, Jie
  - Cade, JasShon
  - Brunk, Brian
  - Roos, David
  - Stoeckert, Christian
  - James, San
  - Arinaitwe, Emmanuel
  - Greenhouse, Bryan
  - Dorsey, Grant
  - Sullivan, Steven
  - Carlton, Jane
  - Carrasco-Escobar, Gabriel
  - Gamboa, Dionicia
  - Maguina-Mercedes, Paula
  - Vinetz, Joseph
  doi: 10.5281/zenodo.6685957
  id: https://doi.org/10.5281/zenodo.6685957
  journal: Zenodo
  title: Malaria study data integration and information retrieval based on OBO Foundry
    ontologies.
  year: '2016'
repository: https://github.com/VEuPathDB-ontology/VEuPathDB-ontology
---
## Description

An ontology is developed to support Eukaryotic Pathogen, Host & Vector Genomics Resource (VEuPathDB; https://veupathdb.org).

## Contacts

- Jie Zheng (jiezhen@med.umich.edu) [ORCID: 0000-0002-2999-0103](https://orcid.org/0000-0002-2999-0103)

## Products

### eupath.owl

VEuPathDB ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/eupath.owl](http://purl.obolibrary.org/obo/eupath.owl)

**Format**: owl

## Publications

- [Malaria study data integration and information retrieval based on OBO Foundry ontologies.](https://doi.org/10.5281/zenodo.6685957)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*