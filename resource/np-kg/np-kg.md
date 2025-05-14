---
layout: resource_detail
activity_status: active
id: np-kg
name: NP-KG
description: NP-KG is a graph framework that creates a biomedical knowledge graph
  to identify and generate mechanistic hypotheses for pharmacokinetic natural product-drug
  interactions (NPDIs).
domains:
- health
- pharmacology
- drug discovery
- biomedical
contacts:
- category: Individual
  label: Sanya Bathla Taneja
  contact_details:
  - contact_type: github
    value: sanyabt
homepage_url: https://doi.org/10.5281/zenodo.6814507
repository: https://github.com/sanyabt/np-kg
products:
- id: np-kg.graph.tsv
  name: NP-KG TSV
  description: Merged KG with ontology-grounded KG and literature-based graph as TSV
    file
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.tsv?download=1
  category: GraphProduct
  secondary_source:
  - np-kg
  original_source:
  - np-kg
- id: np-kg.graph.networkx
  name: NP-KG gpickle
  description: Merged KG with ontology-grounded KG and literature-based graph as NetworkX
    multidigraph object
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.gpickle?download=1
  dump_format: gpickle
  category: GraphProduct
  secondary_source:
  - np-kg
  original_source:
  - np-kg
license:
  label: CC-BY-4.0
  id: https://creativecommons.org/licenses/by/4.0/
publications:
- doi: doi:10.1016/j.jbi.2023.104341
  id: doi:10.1016/j.jbi.2023.104341
  preferred: true
  year: '2023'
  authors:
  - Taneja SB
  - Callahan TJ
  - Paine MF
  - Kane-Gill SL
  - Kilicoglu H
  - Joachimiak MP
  - Boyce RD
  title: '''Developing a Knowledge Graph for Pharmacokinetic Natural Product-Drug
    Interactions'''
category: KnowledgeGraph
---

NP-KG is a graph framework that creates a biomedical knowledge graph (KG) to identify and generate mechanistic hypotheses for pharmacokinetic natural product-drug interactions (NPDIs). NP-KG uses the PheKnowLator ecosystem to create an ontology-grounded KG. It then uses two relation extraction systems to extract triples from full texts of natural product-related scientific literature to create a literature-based graph, and integrates the nodes and edges in the ontology-grounded KG.