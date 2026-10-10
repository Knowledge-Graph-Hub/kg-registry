---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: yongqunh@med.umich.edu
  - contact_type: github
    value: yongqunh
  label: Yongqun Oliver He
  orcid: 0000-0001-9189-9661
creation_date: '2025-09-29T00:00:00Z'
description: The Ontology of Precision Medicine and Investigation (OPMI) aims to ontologically
  represent and standardize various entities and relations associated with precision
  medicine and related investigations at different conditions.
domains:
- biomedical
- precision medicine
- general
homepage_url: https://github.com/OPMI/opmi
id: opmi
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Ontology of Precision Medicine and Investigation
products:
- category: OntologyProduct
  description: Ontology of Precision Medicine and Investigation in OWL format
  format: owl
  id: opmi.owl
  name: opmi.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opmi
  product_file_size: 394555
  product_url: http://purl.obolibrary.org/obo/opmi.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Ontology of Precision Medicine and Investigation
    (OPMI), produced by KG-Bioportal from the BioPortal submission. The archive contains
    OPMI_nodes.tsv and OPMI_edges.tsv.
  edge_count: 10056
  format: kgx
  id: opmi.kg-bioportal
  latest_version: 'Vision Release: 1.0.166'
  name: OPMI KGX graph (KG-Bioportal)
  node_count: 4201
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opmi
  product_file_size: 194304
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/OPMI.tar.gz
- category: OntologyProduct
  description: clinical LABoratory Ontology in OWL format
  format: owl
  id: labo.owl
  name: labo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: labo
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: omiabis
  - relation_type: prov:hadPrimarySource
    source: omrse
  - relation_type: prov:hadPrimarySource
    source: opmi
  product_file_size: 47001
  product_url: http://purl.obolibrary.org/obo/labo.owl
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
  - He Y
  - Ong E
  - Schaub J
  - Dowd F
  - O'Toole JF
  - Siapos A
  - Reich C
  - Seager S
  - Wan L
  - Yu H
  - Zheng J
  - Stoeckert C
  - Yang X
  - Yang S
  - Steck B
  - Park C
  - Barisoni L
  - Kretzler M
  - Himmelfarb J
  - Iyengar R
  - Mooney SD
  id: http://ceur-ws.org/Vol-2931/ICBO_2019_paper_34.pdf
  journal: CEUR Workshop Proceedings
  preferred: true
  title: 'OPMI: the Ontology of Precision Medicine and Investigation and its Support
    for Clinical Data and Metadata Representation and Analysis'
  year: '2019'
repository: https://github.com/OPMI/opmi
---
## Description

The Ontology of Precision Medicine and Investigation (OPMI) aims to ontologically represent and standardize various entities and relations associated with precision medicine and related investigations at different conditions.

## Contacts

- Yongqun Oliver He (yongqunh@med.umich.edu) [ORCID: 0000-0001-9189-9661](https://orcid.org/0000-0001-9189-9661)

## Products

### opmi.owl

Ontology of Precision Medicine and Investigation in OWL format

**URL**: [http://purl.obolibrary.org/obo/opmi.owl](http://purl.obolibrary.org/obo/opmi.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*