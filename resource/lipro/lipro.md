---
id: lipro
name: Lipid Ontology
description: An ontology representation of the LIPIDMAPS nomenclature classification.
activity_status: inactive
homepage_url: https://obofoundry.org/ontology/lipro.html
license:
  id: ''
  label: Not specified
collection:
- obo-foundry
layout: resource_detail
category: Ontology
creation_date: '2025-09-29T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
domains:
- chemistry and biochemistry
contacts:
- category: Individual
  label: Christopher Baker
  orcid: 0000-0003-4004-6479
  contact_details:
  - contact_type: email
    value: bakerc@unb.ca
products:
- id: lipro.owl
  name: Lipid Ontology OWL product
  description: OWL-DL edition of the Lipid Ontology (LiPrO), representing the LIPIDMAPS
    nomenclature classification. Served as an archived mirror via AberOWL; the original
    OBO PURL no longer resolves.
  category: OntologyProduct
  format: owl
  product_url: http://aber-owl.net/media/ontologies/LIPRO/4/lipro.owl
  original_source:
  - source: lipro
    relation_type: prov:hadPrimarySource
publications:
- authors:
  - Chepelev LL
  - Riazanov A
  - Kouznetsov A
  - Low HS
  - Dumontier M
  - Baker CJO
  doi: 10.1186/1471-2105-12-303
  id: https://doi.org/10.1186/1471-2105-12-303
  journal: BMC Bioinformatics
  title: Prototype semantic infrastructure for automated small molecule classification
    and annotation in lipidomics
  year: '2011'
---
## Description

An ontology representation of the LIPIDMAPS nomenclature classification. The ontology
describes the LIPIDMAPS nomenclature classification explicitly using description logics
(OWL-DL). Lipid classes are organized hierarchically with the super-classes restricted
by generic necessary conditions; more specific necessary conditions define membership
requirements for sub-classes of lipid according to appropriate functional groups. Note:
this ontology is obsolete (deprecated) in the OBO Foundry.

## Contacts

- Christopher Baker (bakerc@unb.ca) [ORCID: 0000-0003-4004-6479](https://orcid.org/0000-0003-4004-6479)

**Domains**: chemistry and biochemistry

---

*This resource was automatically synchronized from the OBO Foundry registry.*
