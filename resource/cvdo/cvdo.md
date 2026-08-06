---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Paul Fabry
    orcid: 0000-0002-3336-2476
    contact_details:
      - contact_type: email
        value: paul.fabry@usherbrooke.ca
      - contact_type: github
        value: pfabry
creation_date: '2025-09-29T00:00:00Z'
description: An ontology to describe entities related to cardiovascular diseases
domains:
  - biomedical
homepage_url: https://github.com/OpenLHS/CVDO
id: cvdo
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Cardiovascular Disease Ontology
products:
  - category: OntologyProduct
    description: Cardiovascular Disease Ontology in OWL format
    format: owl
    id: cvdo.owl
    name: cvdo.owl
    product_file_size: 105498
    product_url: http://purl.obolibrary.org/obo/cvdo.owl
    original_source:
      - source: cvdo
        relation_type: prov:hadPrimarySource
  - id: cvdo.kg-bioportal
    name: CVDO KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Cardiovascular Disease Ontology (CVDO), produced by KG-Bioportal from the BioPortal submission. The archive contains CVDO_nodes.tsv and CVDO_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/CVDO.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: cvdo
        relation_type: prov:hadPrimarySource
    node_count: 1023
    edge_count: 1865
    latest_version: '2024-05-17'
repository: https://github.com/OpenLHS/CVDO
publications: []
---

## Description

An ontology to describe entities related to cardiovascular diseases

## Contacts

- Paul Fabry (paul.fabry@usherbrooke.ca) [ORCID: 0000-0002-3336-2476](https://orcid.org/0000-0002-3336-2476)

## Products

### cvdo.owl

Cardiovascular Disease Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/cvdo.owl](http://purl.obolibrary.org/obo/cvdo.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
