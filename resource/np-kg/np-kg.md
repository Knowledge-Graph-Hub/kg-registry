---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: sanyabt
  label: Sanya Bathla Taneja
description: NP-KG is a graph framework that creates a biomedical knowledge graph
  to identify and generate mechanistic hypotheses for pharmacokinetic natural product-drug
  interactions (NPDIs).
domains:
- health
- pharmacology
- drug discovery
- biomedical
homepage_url: https://doi.org/10.5281/zenodo.6814507
id: np-kg
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: NP-KG
products:
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as TSV
    file
  id: np-kg.graph.tsv
  name: NP-KG TSV
  original_source:
  - np-kg
  product_file_size: 1074149258
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.tsv?download=1
  secondary_source:
  - np-kg
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as NetworkX
    multidigraph object
  dump_format: gpickle
  id: np-kg.graph.networkx
  name: NP-KG gpickle
  original_source:
  - np-kg
  product_file_size: 936065236
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.gpickle?download=1
  secondary_source:
  - np-kg
publications:
- authors:
  - Taneja SB
  - Callahan TJ
  - Paine MF
  - Kane-Gill SL
  - Kilicoglu H
  - Joachimiak MP
  - Boyce RD
  doi: doi:10.1016/j.jbi.2023.104341
  id: doi:10.1016/j.jbi.2023.104341
  preferred: true
  title: '''Developing a Knowledge Graph for Pharmacokinetic Natural Product-Drug
    Interactions'''
  year: '2023'
repository: https://github.com/sanyabt/np-kg
---
NP-KG is a graph framework that creates a biomedical knowledge graph (KG) to identify and generate mechanistic hypotheses for pharmacokinetic natural product-drug interactions (NPDIs). NP-KG uses the PheKnowLator ecosystem to create an ontology-grounded KG. It then uses two relation extraction systems to extract triples from full texts of natural product-related scientific literature to create a literature-based graph, and integrates the nodes and edges in the ontology-grounded KG.

## Automated Evaluation

- View the automated evaluation: [np-kg automated evaluation](np-kg_eval_automated.html)
