---
layout: resource_detail
activity_status: active
id: hra-kg
name: Human Reference Atlas Knowledge Graph (HRA KG)
description: The HRA Knowledge Graph (HRA KG) is a linked open data resource that integrates anatomical structures, cell types, and biomarkers to support cross-scale biological queries.
domain: health
contacts:
  - category: Individual
    label: Katy Börner
    orcid: 0000-0002-3321-6137
homepage_url: https://apps.humanatlas.io/dashboard/data
repository: https://github.com/hubmapconsortium/hra-kg
license:
  label: CC-BY-4.0
  id: http://creativecommons.org/licenses/by/4.0/
products:
- id: hra-kg.graph.ttl
  name: HRA KG graph data, v2.2, Turtle format
  description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, Turtle format
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.ttl
  category: GraphProduct
  secondary_source:
  - hra-kg
  original_source:
  - hra-kg
  format: ttl
- id: hra-kg.graph.json
  name: HRA KG graph data, v2.2, JSON-LD format
  description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, JSON-LD format
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.json
  category: GraphProduct
  format: jsonld
  secondary_source:
  - hra-kg
  original_source:
  - hra-kg
- id: hra-kg.graph.xml
  name: HRA KG graph data, v2.2, RDF/XML format
  description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, RDF/XML format
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.xml
  category: GraphProduct
  secondary_source:
  - hra-kg
  original_source:
  - hra-kg
  format: rdfxml
- id: hra-kg.graph.nt
  name: HRA KG graph data, v2.2, N-Triples format
  description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, N-Triples format
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nt
  category: GraphProduct
  secondary_source:
  - hra-kg
  original_source:
  - hra-kg
  format: ntriples
- id: hra-kg.graph.nq
  name: HRA KG graph data, v2.2, N-Quads format
  description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, N-Quads format
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nq
  category: GraphProduct
  secondary_source:
  - hra-kg
  original_source:
  - hra-kg
  format: nquads
category: KnowledgeGraph
---

### Human Reference Atlas Knowledge Graph (HRA KG)

The **Human Reference Atlas Knowledge Graph (HRA KG)** is a **linked open data (LOD) resource** that provides a structured and queryable framework for integrating anatomical structures, cell types, and biomarkers across different biological scales.
