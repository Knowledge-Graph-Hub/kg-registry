---
activity_status: active
category: DataModel
contacts:
  - category: Individual
    label: "Katy Börner"
    orcid: 0000-0002-3321-6137
creation_date: '2026-06-18T00:00:00Z'
description: >-
  HRAVS (Human Reference Atlas Value Set) is a controlled vocabulary that
  standardizes the names and definitions of research attributes used across
  the Human Reference Atlas (HRA) and the broader HuBMAP project. It is
  distributed as a SKOS-based value set within the HRA Knowledge Graph,
  providing a consistent, widely accepted set of terms for describing HRA
  metadata. HRAVS is bundled as an upstream component of the HRA Knowledge
  Graph (HRA-KG).
domains:
  - biomedical
  - anatomy and development
  - information technology
homepage_url: https://humanatlas.io/
id: hravs
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Human Reference Atlas Value Set (HRAVS)
products:
  - category: DataModelProduct
    description: The graph representation of the HRAVS (HuBMAP Research Attributes) value set dataset, latest version, Turtle format.
    format: ttl
    id: hravs.graph.ttl
    name: HRAVS graph data, Turtle format
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hravs
    product_url: https://cdn.humanatlas.io/digital-objects/vocab/hravs/latest/graph.ttl
  - category: DataModelProduct
    description: The graph representation of the HRAVS (HuBMAP Research Attributes) value set dataset, latest version, JSON-LD format.
    format: jsonld
    id: hravs.graph.json
    name: HRAVS graph data, JSON-LD format
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hravs
    product_url: https://cdn.humanatlas.io/digital-objects/vocab/hravs/latest/graph.json
publications:
  - id: https://doi.org/10.1038/s41597-025-05183-6
    title: "Construction, Deployment, and Usage of the Human Reference Atlas Knowledge Graph"
    authors:
      - Andreas Bueckle
      - Bruce W. Herr
      - Josef Hardi
      - Ellen M. Quardokus
      - Mark A. Musen
      - Katy Börner
    journal: Scientific Data
    year: '2025'
    doi: 10.1038/s41597-025-05183-6
repository: https://github.com/hubmapconsortium/hra-vocab
---

## Description

The **Human Reference Atlas Value Set (HRAVS)** is a controlled vocabulary that
standardizes the names and definitions of research attributes used across the
**Human Reference Atlas (HRA)** and the wider HuBMAP project. Its purpose is to
ensure a consistent, widely accepted set of terms so that HRA metadata can be
described and queried in a uniform way.

HRAVS is published as a SKOS-based value set and is bundled as an upstream
component of the **HRA Knowledge Graph (HRA-KG)**, with its source data curated
in the [hra-vocab](https://github.com/hubmapconsortium/hra-vocab) repository and
distributed through the Human Reference Atlas digital-object infrastructure.

## Products

- **HRAVS graph data, Turtle format** — the value set as a SKOS/RDF graph in Turtle.
- **HRAVS graph data, JSON-LD format** — the value set as a SKOS/RDF graph in JSON-LD.
