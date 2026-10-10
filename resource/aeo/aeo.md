---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: J.Bard@ed.ac.uk
  label: Jonathan Bard
creation_date: '2025-09-29T00:00:00Z'
description: AEO is an ontology of anatomical structures that expands CARO, the Common
  Anatomy Reference Ontology
domains:
- anatomy and development
homepage_url: https://github.com/obophenotype/human-developmental-anatomy-ontology/
id: aeo
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Anatomical Entity Ontology
products:
- category: OntologyProduct
  description: Anatomical Entity Ontology in OWL format
  format: owl
  id: aeo.owl
  name: aeo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aeo
  product_file_size: 25664
  product_url: http://purl.obolibrary.org/obo/aeo.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Anatomical Entity Ontology (AEO), produced by
    KG-Bioportal from the BioPortal submission. The archive contains AEO_nodes.tsv
    and AEO_edges.tsv.
  edge_count: 728
  format: kgx
  id: aeo.kg-bioportal
  name: AEO KGX graph (KG-Bioportal)
  node_count: 461
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aeo
  product_file_size: 18041
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/AEO.tar.gz
- category: OntologyProduct
  description: Human developmental anatomy, abstract in OWL format
  format: owl
  id: ehdaa2.owl
  name: ehdaa2.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehdaa2
  - relation_type: prov:hadPrimarySource
    source: aeo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: cl
  product_file_size: 125946
  product_url: http://purl.obolibrary.org/obo/ehdaa2.owl
- category: OntologyProduct
  description: Human developmental anatomy, abstract in OBO format
  format: obo
  id: ehdaa2.obo
  name: ehdaa2.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehdaa2
  - relation_type: prov:hadPrimarySource
    source: aeo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: cl
  product_file_size: 83809
  product_url: http://purl.obolibrary.org/obo/ehdaa2.obo
publications: []
repository: https://github.com/obophenotype/human-developmental-anatomy-ontology
---
## Description

AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology

## Contacts

- Jonathan Bard (J.Bard@ed.ac.uk)

## Products

### aeo.owl

Anatomical Entity Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/aeo.owl](http://purl.obolibrary.org/obo/aeo.owl)

**Format**: owl

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*