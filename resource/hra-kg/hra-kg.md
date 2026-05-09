---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    label: "Katy Börner"
    orcid: 0000-0002-3321-6137
description: The HRA Knowledge Graph (HRA KG) is a linked open data resource that integrates anatomical structures, cell types, and biomarkers to support cross-scale biological queries.
domains:
  - health
  - anatomy and development
  - biological systems
  - biomedical
homepage_url: https://apps.humanatlas.io/dashboard/data
id: hra-kg
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Human Reference Atlas Knowledge Graph (HRA KG)
products:
  - category: GraphProduct
    description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, Turtle format
    format: ttl
    id: hra-kg.graph.ttl
    name: HRA KG graph data, v2.2, Turtle format
    original_source:
      - source: hra-kg
        relation_type: prov:hadPrimarySource
    product_file_size: 204030087
    product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.ttl
  - category: GraphProduct
    description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, JSON-LD format
    format: jsonld
    id: hra-kg.graph.json
    name: HRA KG graph data, v2.2, JSON-LD format
    original_source:
      - source: hra-kg
        relation_type: prov:hadPrimarySource
    product_file_size: 18043
    product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.json
  - category: GraphProduct
    description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, RDF/XML format
    format: rdfxml
    id: hra-kg.graph.xml
    name: HRA KG graph data, v2.2, RDF/XML format
    original_source:
      - source: hra-kg
        relation_type: prov:hadPrimarySource
    product_file_size: 185060502
    product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.xml
  - category: GraphProduct
    description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, N-Triples format
    format: ntriples
    id: hra-kg.graph.nt
    name: HRA KG graph data, v2.2, N-Triples format
    original_source:
      - source: hra-kg
        relation_type: prov:hadPrimarySource
    product_file_size: 291382102
    product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nt
  - category: GraphProduct
    description: The graph representation of the Human Reference Atlas (HRA) dataset, v2.2, N-Quads format
    format: nquads
    id: hra-kg.graph.nq
    name: HRA KG graph data, v2.2, N-Quads format
    original_source:
      - source: hra-kg
        relation_type: prov:hadPrimarySource
    product_file_size: 376981902
    product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nq
repository: https://github.com/hubmapconsortium/hra-kg
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2025-08-12T00:00:00Z'
---

### Human Reference Atlas Knowledge Graph (HRA KG)

The **Human Reference Atlas Knowledge Graph (HRA KG)** is a **linked open data (LOD) resource** that provides a structured and queryable framework for integrating anatomical structures, cell types, and biomarkers across different biological scales.

## Evaluation

- View the evaluation: [hra-kg evaluation](hra-kg_eval.html)
