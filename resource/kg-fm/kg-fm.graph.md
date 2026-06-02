---
category: GraphProduct
description: Neo4j framework-materials knowledge graph constructed from Web of Science
  abstracts and publication metadata with LLM-assisted information extraction. The
  paper reports 2.53 million nodes and 4.01 million relationships covering materials,
  properties, structures, applications, and related literature.
edge_count: 4010000
id: kg-fm.graph
name: KG-FM Neo4j Knowledge Graph
node_count: 2530000
original_source:
- relation_type: prov:hadPrimarySource
  source: kg-fm
- relation_type: prov:hadPrimarySource
  source: web-of-science
product_url: https://github.com/MontageBai/KGFM
warnings:
- No standalone Neo4j database dump, public graph endpoint, or versioned graph release
  was identified in the GitHub repository when curated on 2026-06-02; the repository
  provides source text, JSON extraction files, and Python scripts for constructing
  and using the graph.
layout: product_detail
---
