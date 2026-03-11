---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://orkg.org/about
  label: Open Research Knowledge Graph Team
creation_date: '2026-03-11T00:00:00Z'
description: The Open Research Knowledge Graph (ORKG) aims to describe research papers
  in a structured manner. With the ORKG, papers are easier to find and compare. It
  provides structured, machine-readable representations of research contributions
  that can be queried, compared, and reused.
domains:
- literature
homepage_url: https://orkg.org/
id: orkg
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
last_modified_date: '2026-03-11T00:00:00Z'
name: Open Research Knowledge Graph
repository: https://gitlab.com/TIBHannover/orkg/orkg-frontend/
products:
- category: GraphicalInterface
  description: Web interface for browsing, searching, and comparing research contributions
    in the ORKG
  format: http
  id: orkg.portal
  name: ORKG Web Portal
  original_source:
  - orkg
  product_url: https://orkg.org/
- category: ProgrammingInterface
  description: REST API providing programmatic access to ORKG data and structured
    research contribution metadata
  format: http
  id: orkg.api
  name: ORKG REST API
  original_source:
  - orkg
  product_url: https://orkg.org/api
- category: Product
  description: ORKG data dump in N-Triples RDF format for bulk download and reuse
  format: ntriples
  id: orkg.dump
  name: ORKG RDF Data Dump
  original_source:
  - orkg
  product_url: https://orkg.org/about
publications:
- id: https://doi.org/10.1145/3360901.3364435
  title: "Towards a Knowledge Graph for Science"
  year: "2019"
synonyms:
- ORKG
---

# Open Research Knowledge Graph (ORKG)

## Overview

The Open Research Knowledge Graph (ORKG) is a scholarly knowledge graph that describes research contributions from scientific papers in a structured, machine-readable manner. It is developed by TIB – Leibniz Information Centre for Science and Technology.

## Key Features

- **Structured Research Descriptions**: Research contributions are described using structured data rather than unstructured text
- **Comparisons**: Enables systematic comparison of research contributions across papers
- **FAIR Principles**: Data is represented as Linked Data following FAIR (Findable, Accessible, Interoperable, Reusable) principles
- **Community-driven**: Researchers can contribute structured descriptions of their own papers

## Applications

- **Literature Search**: Find papers by their structured content, not just keywords
- **Research Comparison**: Systematically compare methodologies, results, and findings across papers
- **Knowledge Discovery**: Explore connections between research contributions
- **Data Reuse**: Programmatic access to structured research metadata via REST API and RDF dumps
