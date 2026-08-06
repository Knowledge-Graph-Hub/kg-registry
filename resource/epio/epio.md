---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: alpha.tom.kodamullil@scai.fraunhofer.de
      - contact_type: github
        value: akodamullil
    label: Alpha Tom Kodamullil
    orcid: 0000-0001-9896-3531
creation_date: '2025-09-29T00:00:00Z'
description: A application driven Epilepsy Ontology with official terms from the ILAE.
domains:
  - biomedical
homepage_url: https://github.com/SCAI-BIO/EpilepsyOntology
id: epio
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Epilepsy Ontology
products:
  - category: OntologyProduct
    description: Epilepsy Ontology in OWL format
    format: owl
    id: epio.owl
    name: epio.owl
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epio
    product_file_size: 415175
    product_url: http://purl.obolibrary.org/obo/epio.owl
  - id: epio.kg-bioportal
    name: EPIO KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of EpilepsyOntology (EPIO), produced by KG-Bioportal from the BioPortal submission. The archive contains EPIO_nodes.tsv and EPIO_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/EPIO.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: epio
        relation_type: prov:hadPrimarySource
    node_count: 3100
    edge_count: 5472
    latest_version: 'Version Release: 1.0.0'
publications: []
repository: https://github.com/SCAI-BIO/EpilepsyOntology
---

## Description

A application driven Epilepsy Ontology with official terms from the ILAE.

## Contacts

- Alpha Tom Kodamullil (alpha.tom.kodamullil@scai.fraunhofer.de) [ORCID: 0000-0001-9896-3531](https://orcid.org/0000-0001-9896-3531)

## Products

### epio.owl

Epilepsy Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/epio.owl](http://purl.obolibrary.org/obo/epio.owl)

**Format**: owl

### epio.EPIO_merged.owl

Epilepsy Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/EPIO_merged.owl](http://purl.obolibrary.org/obo/EPIO_merged.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
