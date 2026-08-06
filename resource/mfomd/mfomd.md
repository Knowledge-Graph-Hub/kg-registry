---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Janna Hastings
    orcid: 0000-0002-3469-4923
    contact_details:
      - contact_type: email
        value: "janna.hastings@gmail.com"
      - contact_type: github
        value: "jannahastings"
creation_date: '2025-09-29T00:00:00Z'
description: An ontology to describe and classify mental diseases such as schizophrenia, annotated with DSM-IV and ICD codes where applicable
domains:
  - biomedical
homepage_url: https://github.com/jannahastings/mental-functioning-ontology
id: "mfomd"
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: "http://creativecommons.org/licenses/by/3.0/"
  label: CC BY 3.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Mental Disease Ontology
products:
  - category: OntologyProduct
    description: Mental Disease Ontology in OWL format
    format: owl
    id: "mfomd.owl"
    name: mfomd.owl
    product_file_size: 1294
    product_url: http://purl.obolibrary.org/obo/mfomd.owl
    original_source:
      - source: mfomd
        relation_type: prov:hadPrimarySource
  - id: mfomd.kg-bioportal
    name: MFOMD KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of MFO Mental Disease Ontology (MFOMD), produced by KG-Bioportal from the BioPortal submission. The archive contains MFOMD_nodes.tsv and MFOMD_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/MFOMD.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: mfomd
        relation_type: prov:hadPrimarySource
    node_count: 34
    edge_count: 11
    latest_version: '2020-04-26'
repository: https://github.com/jannahastings/mental-functioning-ontology
publications:
  - authors:
      - Werner Ceusters
      - Barry Smith
    doi: "10.1186/2041-1480-1-10"
    id: "https://pubmed.ncbi.nlm.nih.gov/21143905"
    journal: J Biomed Semantics
    preferred: true
    title: Foundations for a realist ontology of mental disease
    year: "2010"
---

## Description

An ontology to describe and classify mental diseases such as schizophrenia, annotated with DSM-IV and ICD codes where applicable

## Contacts

- Janna Hastings (janna.hastings@gmail.com) [ORCID: 0000-0002-3469-4923](https://orcid.org/0000-0002-3469-4923)

## Products

### mfomd.owl

Mental Disease Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/mfomd.owl](http://purl.obolibrary.org/obo/mfomd.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
