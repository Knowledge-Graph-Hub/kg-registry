---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: topalis@imbb.forth.gr
  label: Pantelis Topalis
creation_date: '2025-09-29T00:00:00Z'
description: An application ontology for use with miRNA databases.
domains:
- chemistry and biochemistry
homepage_url: http://code.google.com/p/mirna-ontology/
id: mirnao
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: microRNA Ontology
products:
- category: OntologyProduct
  description: microRNA Ontology in OWL format
  format: owl
  id: mirnao.owl
  name: mirnao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirnao
  product_url: http://purl.obolibrary.org/obo/mirnao.owl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-08-12: HTTP 404 error
    when accessing file'
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of MicroRNA Ontology (MIRNAO), produced by KG-Bioportal
    from the BioPortal submission. The archive contains MIRNAO_nodes.tsv and MIRNAO_edges.tsv.
  edge_count: 764
  format: kgx
  id: mirnao.kg-bioportal
  latest_version: '1.7'
  name: MIRNAO KGX graph (KG-Bioportal)
  node_count: 695
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirnao
  product_file_size: 34554
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/MIRNAO.tar.gz
publications: []
---
## Description

An application ontology for use with miRNA databases.

## Contacts

- Pantelis Topalis (topalis@imbb.forth.gr)

## Products

### mirnao.owl

microRNA Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/mirnao.owl](http://purl.obolibrary.org/obo/mirnao.owl)

**Format**: owl

**Domains**: chemistry and biochemistry

---

*This resource was automatically synchronized from the OBO Foundry registry.*