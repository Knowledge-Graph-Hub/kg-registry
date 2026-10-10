---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: annethessen@gmail.com
  - contact_type: github
    value: diatomsRcool
  label: Anne Thessen
  orcid: 0000-0002-2908-3327
creation_date: '2025-09-29T00:00:00Z'
description: Vocabularies for describing exposure data to inform understanding of
  environmental health.
domains:
- biomedical
- environment
- environmental exposure
homepage_url: https://github.com/CTDbase/exposure-ontology
id: exo
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Exposure ontology
products:
- category: OntologyProduct
  description: Exposure ontology in OWL format
  format: owl
  id: exo.owl
  name: exo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: exo
  product_file_size: 17786
  product_url: http://purl.obolibrary.org/obo/exo.owl
- category: OntologyProduct
  description: Exposure ontology in OBO format
  format: obo
  id: exo.obo
  name: exo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: exo
  product_file_size: 12690
  product_url: http://purl.obolibrary.org/obo/exo.obo
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Exposure Ontology (EXO), produced by KG-Bioportal
    from the BioPortal submission. The archive contains EXO_nodes.tsv and EXO_edges.tsv.
  edge_count: 222
  format: kgx
  id: exo.kg-bioportal
  latest_version: '2025-08-29'
  name: EXO KGX graph (KG-Bioportal)
  node_count: 198
  original_source:
  - relation_type: prov:hadPrimarySource
    source: exo
  product_file_size: 11882
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/EXO.tar.gz
- category: OntologyProduct
  description: The draft Exposure Ontology (ExO) as distributed by CTD, which provides
    exposure context for CTD's exposure data.
  format: obo
  id: ctd.exposure_ontology
  name: CTD Exposure Ontology (ExO)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: ctd
  product_file_size: 61218
  product_url: https://ctdbase.org/reports/CTD_exposure_ontology.obo
- category: OntologyProduct
  description: Environmental conditions, treatments and exposures ontology in OWL
    format
  format: owl
  id: ecto.owl
  name: ecto.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 2277332
  product_url: http://purl.obolibrary.org/obo/ecto.owl
- category: OntologyProduct
  description: Environmental conditions, treatments and exposures ontology in OBO
    format
  format: obo
  id: ecto.obo
  name: ecto.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 1509031
  product_url: http://purl.obolibrary.org/obo/ecto.obo
- category: OntologyProduct
  description: Environmental conditions, treatments and exposures ontology in JSON
    format
  format: json
  id: ecto.json
  name: ecto.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 1646990
  product_url: http://purl.obolibrary.org/obo/ecto.json
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
  - Mattingly CJ
  - McKone TE
  - Callahan MA
  - Blake JA
  - Cohen Hubal EA
  doi: 10.1021/es2033857
  id: https://www.ncbi.nlm.nih.gov/pubmed/22324457
  journal: Environ Sci Technol
  preferred: true
  title: 'Providing the missing link: the exposure science ontology ExO'
  year: '2012'
repository: https://github.com/CTDbase/exposure-ontology
---
## Description

Vocabularies for describing exposure data to inform understanding of environmental health.

## Contacts

- Anne Thessen (annethessen@gmail.com) [ORCID: 0000-0002-2908-3327](https://orcid.org/0000-0002-2908-3327)

## Products

### exo.owl

Exposure ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/exo.owl](http://purl.obolibrary.org/obo/exo.owl)

**Format**: owl

### exo.obo

Exposure ontology in OBO format

**URL**: [http://purl.obolibrary.org/obo/exo.obo](http://purl.obolibrary.org/obo/exo.obo)

**Format**: obo

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*