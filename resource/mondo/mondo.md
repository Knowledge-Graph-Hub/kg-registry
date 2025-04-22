---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: nicolevasilevsky
  label: Nicole Vasilevsky
  orcid: 0000-0001-5208-3432
- category: Individual
  contact_details:
  - contact_type: github
    value: sabrinatoro
  label: Sabrina Toro
  orcid: 0000-0002-4142-7153
description: The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions across the world. The name Mondo comes from the Latin word ‘mundus’ and means ‘for the world.’
domains:
- health
homepage_url: https://mondo.monarchinitiative.org/
id: mondo
layout: resource_detail
license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
name: Mondo Disease Ontology
products:
- category: DataModelProduct
  description: OWL release of MONDO. The Complete ontology with merged imports.
  format: owl
  id: mondo.owl
  name: Mondo Disease Ontology OWL release
  original_source:
  - mondo
  product_url: https://purl.obolibrary.org/obo/mondo.owl
  secondary_source:
  - mondo
- category: DataModelProduct
  description: OBO release of MONDO.
  format: obo
  id: mondo.obo
  name: Mondo Disease Ontology OBO release
  original_source:
  - mondo
  product_url: https://purl.obolibrary.org/obo/mondo.obo
  secondary_source:
  - mondo
- category: DataModelProduct
  description: JSON release of MONDO (obograph json).
  format: json
  id: mondo.json
  name: Mondo Disease Ontology JSON release
  original_source:
  - mondo
  product_url: https://purl.obolibrary.org/obo/mondo.json
  secondary_source:
  - mondo
- category: ProcessProduct
  description: Utility code for supporting the operations of the Human Disease Ontology
  id: do.code.utils
  name: DO.utils
  original_source:
  - do
  product_url: https://github.com/DiseaseOntology/DO.utils
  secondary_source:
  - do
- category: MappingProduct
  description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
  format: sssom
  id: mondo.sssom
  name: MONDO SSSOM
  original_source:
  - do
  - hp
  - hgnc
  product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
  secondary_source:
  - mondo
repository: https://github.com/DiseaseOntology/HumanDiseaseOntology
---
MONDO Disease Ontology