---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Alpha Tom Kodamullil
    orcid: 0000-0001-9896-3531
    contact_details:
      - contact_type: email
        value: alpha.tom.kodamullil@scai.fraunhofer.de
      - contact_type: github
        value: akodamullil
creation_date: '2025-09-29T00:00:00Z'
description: An application ontology that represents comprehensive knowledge involving a variety of fields of medical and biological aspects.
domains:
  - biomedical
homepage_url: https://github.com/SCAI-BIO/BiomarkerOntology
id: bmont
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Biomarker Ontology
products:
  - category: OntologyProduct
    description: Includes axioms linking to other ontologies, but no imports of those ontologies
    format: owl
    id: bmont.BMONT.owl
    name: bmont.BMONT.owl
    product_file_size: 167585
    product_url: http://purl.obolibrary.org/obo/BMONT.owl
    original_source:
      - source: bmont
        relation_type: prov:hadPrimarySource
  - id: bmont.kg-bioportal
    name: BMONT KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of The Biomarker Ontology (BMONT), produced by KG-Bioportal from the BioPortal submission. The archive contains BMONT_nodes.tsv and BMONT_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/BMONT.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: bmont
        relation_type: prov:hadPrimarySource
    node_count: 1222
    edge_count: 2215
    latest_version: 'Version Release: 0.5.8'
repository: https://github.com/SCAI-BIO/BiomarkerOntology
publications: []
---

## Description

An application ontology that represents comprehensive knowledge involving a variety of fields of medical and biological aspects.

## Contacts

- Alpha Tom Kodamullil (alpha.tom.kodamullil@scai.fraunhofer.de) [ORCID: 0000-0001-9896-3531](https://orcid.org/0000-0001-9896-3531)

## Products

### bmont.BMONT.owl

Includes axioms linking to other ontologies, but no imports of those ontologies

**URL**: [http://purl.obolibrary.org/obo/BMONT.owl](http://purl.obolibrary.org/obo/BMONT.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
