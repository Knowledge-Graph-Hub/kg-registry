---
id: mondo
name: Mondo Disease Ontology
description: A global community effort to harmonize multiple disease resources to
  yield a coherent merged ontology.
activity_status: active
homepage_url: https://monarch-initiative.github.io/mondo
repository: https://github.com/monarch-initiative/mondo
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
collection:
- obo-foundry
layout: resource_detail
category: Ontology
domains:
- biomedical
taxon:
- NCBITaxon:33208
contacts:
- category: Individual
  label: Sabrina Toro
  orcid: 0000-0002-4142-7153
  contact_details:
  - contact_type: email
    value: Sabrina@tislab.org
  - contact_type: github
    value: sabrinatoro
products:
- id: mondo.owl
  name: Mondo OWL edition
  description: Complete ontology with merged imports.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/mondo.owl
- id: mondo.obo
  name: Mondo OBO Format edition
  description: OBO serialization of mondo.owl.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/mondo.obo
- id: mondo.json
  name: Mondo JSON edition
  description: Obographs serialization of mondo.owl.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/mondo.json
- id: mondo.mondo-base.owl
  name: Mondo Base Release
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding the external ontologies themselves
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/mondo/mondo-base.owl
- id: mondo.mondo-simple.owl
  name: Mondo Simple Release
  description: The main ontology classes and their hierarchies, without references
    to external terms.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/mondo/mondo-simple.owl
---

## Description

A global community effort to harmonize multiple disease resources to yield a coherent merged ontology.

## Contacts

- Sabrina Toro (Sabrina@tislab.org) [ORCID: 0000-0002-4142-7153](https://orcid.org/0000-0002-4142-7153)

## Products

### Mondo OWL edition

Complete ontology with merged imports.

**URL**: [http://purl.obolibrary.org/obo/mondo.owl](http://purl.obolibrary.org/obo/mondo.owl)

**Format**: owl

### Mondo OBO Format edition

OBO serialization of mondo.owl.

**URL**: [http://purl.obolibrary.org/obo/mondo.obo](http://purl.obolibrary.org/obo/mondo.obo)

**Format**: obo

### Mondo JSON edition

Obographs serialization of mondo.owl.

**URL**: [http://purl.obolibrary.org/obo/mondo.json](http://purl.obolibrary.org/obo/mondo.json)

**Format**: obo

### Mondo Base Release

The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves

**URL**: [http://purl.obolibrary.org/obo/mondo/mondo-base.owl](http://purl.obolibrary.org/obo/mondo/mondo-base.owl)

**Format**: owl

### Mondo Simple Release

The main ontology classes and their hierarchies, without references to external terms.

**URL**: [http://purl.obolibrary.org/obo/mondo/mondo-simple.owl](http://purl.obolibrary.org/obo/mondo/mondo-simple.owl)

**Format**: owl

## Publications

- [Mondo: Integrating Disease Terminology Across Communities](https://doi.org/10.1093/genetics/iyaf215)
- [Mondo: Unifying diseases for the world, by the world](https://www.medrxiv.org/content/10.1101/2022.04.13.22273750)

**Domains**: biomedical

**Taxon**: NCBITaxon:33208

---

*This resource was automatically synchronized from the OBO Foundry registry.*
