---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nal.usda.gov/
  label: USDA National Agricultural Library
creation_date: '2026-07-01T00:00:00Z'
description: The National Agricultural Library Thesaurus (NALT) is a controlled vocabulary
  of agricultural terms maintained by the USDA National Agricultural Library. It provides
  standardized terminology and hierarchical relationships covering agriculture, biology,
  the environment, and related sciences, and is published as SKOS linked data. NALT
  is used to semantically align terms in downstream resources such as the Soil Organic
  Carbon Knowledge Graph (SOCKG), where roughly 61% of the graph's classes and properties
  are mapped to NALT concepts for consistent terminology and interoperability.
domains:
- agriculture
- environment
- general
homepage_url: https://agclass.nal.usda.gov/
id: nalt
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: National Agricultural Library Thesaurus
products:
- category: GraphicalInterface
  description: The NAL Thesaurus (NALT) web browser for searching and exploring agricultural
    terms, their definitions, and their hierarchical and associative relationships.
  format: http
  id: nalt.browser
  is_public: true
  name: NAL Thesaurus Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nalt
  product_url: https://agclass.nal.usda.gov/
- category: ProgrammingInterface
  description: The NAL Thesaurus published as SKOS linked open data, providing machine-readable
    access to NALT concepts and relationships for semantic alignment and integration.
  format: http
  id: nalt.lod
  is_public: true
  name: NAL Thesaurus Linked Open Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nalt
  product_url: https://lod.nal.usda.gov/nalt/
---
# National Agricultural Library Thesaurus (NALT)

## Overview

The National Agricultural Library Thesaurus (NALT) is a controlled vocabulary
maintained by the USDA National Agricultural Library. It provides standardized
agricultural terminology together with hierarchical (broader/narrower) and
associative relationships, covering agriculture, biology, the environment, and
related sciences.

## Data Content

NALT is published as SKOS (Simple Knowledge Organization System) linked open data,
making its concepts and relationships available for reuse and semantic mapping.

## Use in Knowledge Graphs

NALT is used to semantically align terminology in the Soil Organic Carbon Knowledge
Graph (SOCKG). Approximately 61% of SOCKG's classes and properties are mapped to
NALT concepts (via `rdfs:seeAlso`) to ensure consistent terminology and
interoperability for soil carbon research.

## License

As a work of the U.S. federal government, NALT is generally in the public domain
(U.S. Government Work).
