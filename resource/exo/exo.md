---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Anne Thessen
    orcid: 0000-0002-2908-3327
    contact_details:
      - contact_type: email
        value: annethessen@gmail.com
      - contact_type: github
        value: diatomsRcool
creation_date: '2025-09-29T00:00:00Z'
description: Vocabularies for describing exposure data to inform understanding of environmental health.
domains:
  - biomedical
homepage_url: https://github.com/CTDbase/exposure-ontology
id: exo
last_modified_date: '2026-08-06T00:00:00Z'
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
    product_file_size: 17786
    product_url: http://purl.obolibrary.org/obo/exo.owl
    original_source:
      - source: exo
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Exposure ontology in OBO format
    format: obo
    id: exo.obo
    name: exo.obo
    product_file_size: 12690
    product_url: http://purl.obolibrary.org/obo/exo.obo
    original_source:
      - source: exo
        relation_type: prov:hadPrimarySource
  - id: exo.kg-bioportal
    name: EXO KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Exposure Ontology (EXO), produced by KG-Bioportal from the BioPortal submission. The archive contains EXO_nodes.tsv and EXO_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/EXO.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: exo
        relation_type: prov:hadPrimarySource
    node_count: 198
    edge_count: 222
    latest_version: '2025-08-29'
repository: https://github.com/CTDbase/exposure-ontology
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
