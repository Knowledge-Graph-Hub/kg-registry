---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: bpeters@lji.org
  label: Bjoern Peters
description: The Core Ontology for Biology and Biomedicine (COB) brings together key
  terms from a wide range of OBO Foundry projects into a single, small ontology to
  improve interoperability and term reuse across the OBO community.
domains:
- upper
- biomedical
- biological systems
homepage_url: https://obofoundry.org/COB/
id: cob
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: Core Ontology for Biology and Biomedicine
products:
- category: DataModelProduct
  description: Core Ontology for Biology and Biomedicine, main ontology
  format: owl
  id: cob.owl
  name: COB OWL
  product_file_size: 7391
  product_url: http://purl.obolibrary.org/obo/cob.owl
- category: DataModelProduct
  description: Base module for COB
  format: owl
  id: cob.base
  name: COB Base Module
  product_file_size: 2798
  product_url: http://purl.obolibrary.org/obo/cob/cob-base.owl
- category: DataModelProduct
  description: COB with native IDs preserved rather than rewired to OBO IDs
  format: owl
  id: cob.native
  name: COB Native Module
  product_file_size: 6472
  product_url: http://purl.obolibrary.org/obo/cob/cob-native.owl
- category: DataModelProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 240665663
  product_url: https://www.ebi.ac.uk/efo/efo.owl
  secondary_source:
  - efo
- category: DataModelProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 64058275
  product_url: https://www.ebi.ac.uk/efo/efo.obo
  secondary_source:
  - efo
repository: https://github.com/OBOFoundry/COB
---
# Core Ontology for Biology and Biomedicine (COB)

The Core Ontology for Biology and Biomedicine (COB) is a small, focused ontology that brings together essential terms from multiple Open Biological and Biomedical Ontology (OBO) Foundry projects. Its primary goal is to improve interoperability and facilitate term reuse across the biomedical ontology community.

## Overview

COB addresses a critical challenge in biomedical ontologies: the scattered placement of fundamental terms across various domain-specific ontologies. Rather than creating new terms, COB primarily imports and organizes existing high-quality terms from established OBO ontologies, making them more findable and usable.

COB anchors these terms in the Basic Formal Ontology (BFO) while simplifying some of the more complex aspects that have proven challenging for users in the biomedical domain. This approach ensures compatibility with BFO while improving usability.

## Key Features

- Provides a small, concise ontology focused on fundamental biomedical concepts
- Collects widely-used terms previously scattered across various OBO ontologies
- Simplifies import dependencies for domain ontologies
- Ensures each OBO Foundry ontology can use one or more COB terms as a root
- Maintains compatibility with BFO while reducing complexity

## Purpose and Use Cases

COB is designed to serve as a top-level ontology for biology and biomedicine, creating a framework where different domain ontologies can interoperate effectively. It is particularly useful for:

- Ontology developers who need fundamental terms for their domain ontologies
- Researchers integrating data across multiple biomedical domains
- Anyone using OBO Foundry ontologies who needs access to general biomedical concepts

By providing a single location for commonly used terms, COB simplifies ontology development and use while promoting standardization across the biomedical domain.