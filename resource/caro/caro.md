---
activity_status: inactive
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Melissa Haendel
    orcid: 0000-0001-9114-8737
    contact_details:
      - contact_type: email
        value: haendel@ohsu.edu
      - contact_type: github
        value: mellybelly
creation_date: '2025-09-29T00:00:00Z'
description: An upper level ontology to facilitate interoperability between existing anatomy ontologies for different species
domains:
  - anatomy and development
homepage_url: https://github.com/obophenotype/caro/
id: caro
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Common Anatomy Reference Ontology
products:
  - category: OntologyProduct
    description: Common Anatomy Reference Ontology in OWL format
    format: owl
    id: caro.owl
    name: caro.owl
    product_file_size: 586722
    product_url: http://purl.obolibrary.org/obo/caro.owl
    original_source:
      - source: caro
        relation_type: prov:hadPrimarySource
  - id: caro.kg-bioportal
    name: CARO KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Common Anatomy Reference Ontology (CARO), produced by KG-Bioportal from the BioPortal submission. The archive contains CARO_nodes.tsv and CARO_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/CARO.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: caro
        relation_type: prov:hadPrimarySource
    node_count: 8891
    edge_count: 10155
    latest_version: '2023-03-15'
repository: https://github.com/obophenotype/caro
publications: []
---

## Description

An upper level ontology to facilitate interoperability between existing anatomy ontologies for different species

## Contacts

- Melissa Haendel (haendel@ohsu.edu) [ORCID: 0000-0001-9114-8737](https://orcid.org/0000-0001-9114-8737)

## Products

### caro.owl

Common Anatomy Reference Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/caro.owl](http://purl.obolibrary.org/obo/caro.owl)

**Format**: owl

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*
