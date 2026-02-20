---
layout: resource_detail
activity_status: active
id: reacto
name: Reactome Entity Ontology (REACTO)
description: Representation of entities in Reactome
domains:
- biological systems
contacts:
- category: Individual
  label: Benjamin M. Good
  orcid: 0000-0002-7334-7852
  contact_details:
  - contact_type: email
    value: ben.mcgee.good@gmail.com
  - contact_type: github
    value: goodb
homepage_url: http://purl.obolibrary.org/obo/go/extensions/reacto.owl
repository: http://purl.obolibrary.org/obo/go/extensions/reacto.owl
category: Resource
last_modified_date: '2026-02-20T00:00:00Z'
products:
- category: OntologyProduct
  description: Primary REACTO ontology file representing Reactome entities in OWL.
  format: owl
  id: reacto.owl
  name: REACTO OWL Ontology
  original_source:
  - reacto
  product_url: http://purl.obolibrary.org/obo/go/extensions/reacto.owl
- category: OntologyProduct
  description: Integrated GO-LEGO-REACTO ontology for logical inference workflows.
  format: owl
  id: reacto.go-lego-reacto.owl
  name: GO LEGO REACTO Integrated Ontology
  original_source:
  - reacto
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-lego-reacto.owl
---

For logical inference, import the integrated tbox ontology http://purl.obolibrary.org/obo/go/extensions/go-lego-reacto.owl
