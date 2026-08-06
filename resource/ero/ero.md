---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Marc Ciriello
  contact_details:
  - contact_type: email
    value: Marc_Ciriello@hms.harvard.edu
creation_date: '2025-09-29T00:00:00Z'
description: An ontology of research resources such as instruments. protocols, reagents,
  animal models and biospecimens.
domains:
- biomedical
- information technology
homepage_url: https://open.med.harvard.edu/wiki/display/eaglei/Ontology
id: ero
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/2.0/
  label: CC BY 2.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: eagle-i resource ontology
products:
- category: OntologyProduct
  description: eagle-i resource ontology in OWL format
  format: owl
  id: ero.owl
  name: ero.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ero
  product_url: http://purl.obolibrary.org/obo/ero.owl
  warnings: []
- id: ero.kg-bioportal
  name: ERO KGX graph (KG-Bioportal)
  category: GraphProduct
  description: KGX TSV transform of Eagle-I Research Resource Ontology (ERO), produced
    by KG-Bioportal from the BioPortal submission. The archive contains ERO_nodes.tsv
    and ERO_edges.tsv.
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/ERO.tar.gz
  format: kgx
  compression: targz
  original_source:
  - source: ero
    relation_type: prov:hadPrimarySource
  node_count: 4384
  edge_count: 9033
  latest_version: '2013-08-02'
publications: []
---
## Description

An ontology of research resources such as instruments. protocols, reagents, animal models and biospecimens.

## Contacts

- Marc Ciriello (Marc_Ciriello@hms.harvard.edu)

## Products

### ero.owl

eagle-i resource ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/ero.owl](http://purl.obolibrary.org/obo/ero.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
