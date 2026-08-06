---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Frederic Bastian
    orcid: 0000-0002-9415-5104
    contact_details:
      - contact_type: email
        value: bgee@sib.swiss
      - contact_type: github
        value: fbastian
creation_date: '2025-09-29T00:00:00Z'
description: This ontology represents concepts related to homology, as well as other concepts used to describe similarity and non-homology.
domains:
  - anatomy and development
homepage_url: https://github.com/BgeeDB/homology-ontology
id: hom
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Homology Ontology
products:
  - category: OntologyProduct
    description: Homology Ontology in OWL format
    format: owl
    id: hom.owl
    name: hom.owl
    product_file_size: 9398
    product_url: http://purl.obolibrary.org/obo/hom.owl
    original_source:
      - source: hom
        relation_type: prov:hadPrimarySource
  - id: hom.kg-bioportal
    name: HOM KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Ontology of Homology and Related Concepts in Biology (HOM), produced by KG-Bioportal from the BioPortal submission. The archive contains HOM_nodes.tsv and HOM_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/HOM.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: hom
        relation_type: prov:hadPrimarySource
    node_count: 86
    edge_count: 84
    latest_version: releases/2015-01-07
repository: https://github.com/BgeeDB/homology-ontology
publications:
  - authors:
      - Julien Roux
      - Marc Robinson-Rechavi
    doi: 10.1016/j.tig.2009.12.012
    id: https://doi.org/10.1016/j.tig.2009.12.012
    journal: Trends in Genetics
    title: An ontology to clarify homology-related concepts
    year: '2010'
---

## Description

This ontology represents concepts related to homology, as well as other concepts used to describe similarity and non-homology.

## Contacts

- Frederic Bastian (bgee@sib.swiss) [ORCID: 0000-0002-9415-5104](https://orcid.org/0000-0002-9415-5104)

## Products

### hom.owl

Homology Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/hom.owl](http://purl.obolibrary.org/obo/hom.owl)

**Format**: owl

## Publications

- [An ontology to clarify homology-related concepts](https://doi.org/10.1016/j.tig.2009.12.012)

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*
