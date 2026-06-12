---
reference_id: DOI:10.1093/bioadv/vbaf109
title: RNA knowledge-graph analysis through homogeneous embedding methods
authors:
- Francesco Torgano
- Mauricio Soto Gomez
- Matteo Zignani
- Jessica Gliozzo
- Emanuele Cavalleri
- Marco Mesiti
- Elena Casiraghi
- Giorgio Valentini
journal: Bioinformatics Advances
year: '2024'
doi: 10.1093/bioadv/vbaf109
content_type: abstract_only
---

# RNA knowledge-graph analysis through homogeneous embedding methods
**Authors:** Francesco Torgano, Mauricio Soto Gomez, Matteo Zignani, Jessica Gliozzo, Emanuele Cavalleri, Marco Mesiti, Elena Casiraghi, Giorgio Valentini
**Journal:** Bioinformatics Advances (2024)
**DOI:** [10.1093/bioadv/vbaf109](https://doi.org/10.1093/bioadv/vbaf109)

## Content

Abstract

Motivation
We recently introduced RNA-knowledge graph (KG), an ontology-based KG that integrates biological data on RNAs from over 60 public databases. RNA-KG captures functional relationships and interactions between RNA molecules and other biomolecules, chemicals, and biomedical concepts such as diseases and phenotypes, all represented within graph-structured bio-ontologies. We present the first comprehensive computational analysis of RNA-KG, evaluating the potential of graph representation learning and machine learning models to predict node types and edges within the graph.


Results
We performed node classification experiments to predict up to 81 distinct node types, and performed both generic- and specific-edge prediction tasks. Generic-edge prediction focused on identifying the presence of an edge irrespective of its type, while specific-edge prediction targeted specific interactions between ncRNAs, e.g. between microRNAs (miRNA-miRNA) or between small interfering RNA-messenger and RNA-messenger molecules (siRNA-mRNA), or relationships between ncRNA and biomedical concepts, e.g. miRNA-disease or lncRNA-Gene Ontology term relationships. Using embedding methods for homogeneous graphs, such as Large-scale Information Network Embedding (LINE) and node2vec, in combination with machine learning models like decision trees and random forests, we achieved balanced accuracy exceeding 90% for the 20 most common node types and over 80% for most specific-edge prediction tasks. These results show that simple embedding methods for homogeneous graphs can successfully predict nodes and edges of the RNA-KG, paving the way to discover novel ncRNA interactions and laying the foundation for further exploration, and utilization of this rich information source to enhance prediction accuracy and support further research into the “RNA world.”


Availability and implementation
Python code to reproduce the experiments is available at https://github.com/AnacletoLAB/RNA-KG_homogeneous_emb_analysis