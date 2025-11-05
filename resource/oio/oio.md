---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://obofoundry.org/
  label: OBO Foundry
creation_date: '2025-11-05T00:00:00Z'
description: The OBO Interoperability Ontology (OIO) was a set of annotation properties and ontology metadata standards developed to promote interoperability between OBO Foundry ontologies. Its terms and properties have been superseded by OMO (Ontology Metadata Ontology) and are now considered deprecated. OIO provided foundational metadata terms that were widely used in early OBO ontologies for describing ontology versioning, imports, and other metadata.
domains:
  - biological systems
  - upper
id: oio
infores_id: oio
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: OBO Interoperability Ontology
products:
- category: OntologyProduct
  description: OBO Interoperability Ontology in OWL format
  format: owl
  id: oio.owl
  name: OIO OWL
  original_source:
  - oio
- category: OntologyProduct
  description: OBO Interoperability Ontology in OBO format
  format: obo
  id: oio.obo
  name: OIO OBO
  original_source:
  - oio
synonyms:
  - OIO
  - oio
warnings:
- This ontology is deprecated. Its functionality has been superseded by OMO (Ontology Metadata Ontology).
---

# OBO Interoperability Ontology

## Overview

The OBO Interoperability Ontology (OIO) was a set of annotation properties and ontology metadata standards developed to promote interoperability between OBO Foundry ontologies. 

**Important:** This ontology is now deprecated. Its terms and properties have been superseded by OMO (Ontology Metadata Ontology), which provides a more comprehensive and modern approach to ontology metadata.

## Historical Context

OIO provided foundational metadata terms that were widely used in early OBO ontologies for describing:
- Ontology versioning information
- Import relationships between ontologies
- Metadata about terms and properties
- Cross-references and mappings

These capabilities are now provided by the Ontology Metadata Ontology (OMO), which should be used for new ontology development.

## Products

### OWL and OBO Formats
The deprecated OIO ontology is still available in OWL and OBO formats for legacy purposes, but users should migrate to OMO for current projects.

## Information Resource ID

This resource has the Information Resource identifier: `infores:oio`

## Domains

- Biological Systems
- Upper (ontology metadata)

## OBO Foundry

This ontology was part of the OBO Foundry collection of interoperable ontologies.
