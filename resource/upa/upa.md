---
activity_status: inactive
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Anne Morgat
    orcid: 0000-0002-1216-2969
    contact_details:
      - contact_type: email
        value: Anne.Morgat@sib.swiss
      - contact_type: github
        value: amorgat
creation_date: '2025-09-29T00:00:00Z'
description: A manually curated resource for the representation and annotation of metabolic pathways
domains:
  - biological systems
homepage_url: https://github.com/geneontology/unipathway
id: upa
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Unipathway
products:
  - category: OntologyProduct
    description: Unipathway in OWL format
    format: owl
    id: upa.owl
    name: upa.owl
    product_file_size: 798911
    product_url: http://purl.obolibrary.org/obo/upa.owl
    original_source:
      - source: upa
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Unipathway in OBO format
    format: obo
    id: upa.obo
    name: upa.obo
    product_file_size: 454223
    product_url: http://purl.obolibrary.org/obo/upa.obo
    original_source:
      - source: upa
        relation_type: prov:hadPrimarySource
  - id: upa.kg-bioportal
    name: UPA KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Unipathway (UPA), produced by KG-Bioportal from the BioPortal submission. The archive contains UPA_nodes.tsv and UPA_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/UPA.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: upa
        relation_type: prov:hadPrimarySource
    node_count: 4861
    edge_count: 19767
    latest_version: UniPathway Release 2015_03
repository: https://github.com/geneontology/unipathway
publications:
  - authors:
      - Morgat A
      - Coissac E
      - Coudert E
      - Axelsen KB
      - Keller G
      - Bairoch A
      - Bridge A
      - Bougueleret L
      - Xenarios I
      - Viari A
    doi: 10.1093/nar/gkr1023
    id: https://www.ncbi.nlm.nih.gov/pubmed/22102589
    journal: Nucleic Acids Res
    title: 'UniPathway: a resource for the exploration and annotation of metabolic pathways'
    year: '2012'
---

## Description

A manually curated resource for the representation and annotation of metabolic pathways

## Contacts

- Anne Morgat (Anne.Morgat@sib.swiss) [ORCID: 0000-0002-1216-2969](https://orcid.org/0000-0002-1216-2969)

## Products

### upa.owl

Unipathway in OWL format

**URL**: [http://purl.obolibrary.org/obo/upa.owl](http://purl.obolibrary.org/obo/upa.owl)

**Format**: owl

### upa.obo

Unipathway in OBO format

**URL**: [http://purl.obolibrary.org/obo/upa.obo](http://purl.obolibrary.org/obo/upa.obo)

**Format**: obo

## Publications

- [UniPathway: a resource for the exploration and annotation of metabolic pathways](https://www.ncbi.nlm.nih.gov/pubmed/22102589)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*
