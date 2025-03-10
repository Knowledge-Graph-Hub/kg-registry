---
layout: resource_detail
activity_status: active
id: cl-kg
name: Cell Ontology Knowledge Graph (CL-KG)
description: >-
    CL-KG is a knowledge graph integrating the cell ontology and linked ontologies with hierarchical annotations of single cell transcriptomics data from CellXGene.
domain: biological systems
contacts:
  - category: Individual
    label: Ugur Bayindir
    orcid: 0000-0002-6012-3729
    github: ubyndr
homepage_url: https://cellular-semantics.github.io/CL_KG/
repository: https://github.com/Cellular-Semantics/CL_KG
license:
  label: Apache License 2.0
  id: https://www.apache.org/licenses/LICENSE-2.0
category: KnowledgeGraph
products:
- id: cl-kg.interface.neo4j
  name: CL-KG Neo4j graph instance
  description: Publicly available Neo4j instance for CL-KG.
  category: ProgrammingInterface
  url: https://cellular-semantics.sanger.ac.uk/browser/
  is_public: true
  is_neo4j: true
  connection_url: cl-kg-neo4j-db.cellgeni.sanger.ac.uk:443
---

CL-KG is a knowledge graph integrating the cell ontology and linked ontologies with hierarchical annotations of single cell transcriptomics data from CellXGene.
