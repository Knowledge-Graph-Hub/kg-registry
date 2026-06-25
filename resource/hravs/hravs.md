---
activity_status: active
category: DataModel
contacts:
- category: Individual
  label: Katy Börner
  orcid: 0000-0002-3321-6137
creation_date: '2026-06-18T00:00:00Z'
description: HRAVS (Human Reference Atlas Value Set) is a controlled vocabulary that
  standardizes the names and definitions of research attributes used across the Human
  Reference Atlas (HRA) and the broader HuBMAP project. It is distributed as a SKOS-based
  value set within the HRA Knowledge Graph, providing a consistent, widely accepted
  set of terms for describing HRA metadata. HRAVS is bundled as an upstream component
  of the HRA Knowledge Graph (HRA-KG).
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
  description: The graph representation of the HRAVS (HuBMAP Research Attributes)
    value set dataset, latest version, Turtle format.
  format: ttl
  id: hravs.graph.ttl
  name: HRAVS graph data, Turtle format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hravs
  product_file_size: 604260
  product_url: https://cdn.humanatlas.io/digital-objects/vocab/hravs/latest/graph.ttl
- category: DataModelProduct
  description: The graph representation of the HRAVS (HuBMAP Research Attributes)
    value set dataset, latest version, JSON-LD format.
  format: jsonld
  id: hravs.graph.json
  name: HRAVS graph data, JSON-LD format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hravs
  product_file_size: 860
  product_url: https://cdn.humanatlas.io/digital-objects/vocab/hravs/latest/graph.json
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, Turtle format
  format: ttl
  id: hra-kg.graph.ttl
  name: HRA KG graph data, v2.2, Turtle format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 204030087
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.ttl
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, JSON-LD format
  format: jsonld
  id: hra-kg.graph.json
  name: HRA KG graph data, v2.2, JSON-LD format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 18043
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.json
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, RDF/XML format
  format: rdfxml
  id: hra-kg.graph.xml
  name: HRA KG graph data, v2.2, RDF/XML format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 185060502
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.xml
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, N-Triples format
  format: ntriples
  id: hra-kg.graph.nt
  name: HRA KG graph data, v2.2, N-Triples format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 291382102
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nt
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, N-Quads format
  format: nquads
  id: hra-kg.graph.nq
  name: HRA KG graph data, v2.2, N-Quads format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 376981902
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nq
publications:
- authors:
  - Andreas Bueckle
  - Bruce W. Herr
  - Josef Hardi
  - Ellen M. Quardokus
  - Mark A. Musen
  - Katy Börner
  doi: 10.1038/s41597-025-05183-6
  id: https://doi.org/10.1038/s41597-025-05183-6
  journal: Scientific Data
  title: Construction, Deployment, and Usage of the Human Reference Atlas Knowledge
    Graph
  year: '2025'
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