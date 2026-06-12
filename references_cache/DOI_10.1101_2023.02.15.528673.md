---
reference_id: DOI:10.1101/2023.02.15.528673
title: Clustering rare diseases within an ontology-enriched knowledge graph
authors:
- Jaleal Sanjak
- Qian Zhu
- Ewy A. Mathé
year: '2023'
doi: 10.1101/2023.02.15.528673
content_type: abstract_only
---

# Clustering rare diseases within an ontology-enriched knowledge graph
**Authors:** Jaleal Sanjak, Qian Zhu, Ewy A. Mathé
**DOI:** [10.1101/2023.02.15.528673](https://doi.org/10.1101/2023.02.15.528673)

## Content

Structured Abstract

Objective
Identifying sets of rare diseases with shared aspects of etiology and pathophysiology may enable drug repurposing and/or platform based therapeutic development. Toward that aim, we utilized an integrative knowledge graph-based approach to constructing clusters of rare diseases.


Materials and Methods
Data on 3,242 rare diseases were extracted from the National Center for Advancing Translational Science (NCATS) Genetic and Rare Diseases Information center (GARD) internal data resources. The rare disease data was enriched with additional biomedical data, including gene and phenotype ontologies, biological pathway data and small molecule-target activity data, to create a knowledge graph (KG). Node embeddings were used to convert nodes into vectors upon which k-means clustering was applied. We validated the disease clusters through semantic similarity and feature enrichment analysis.


Results
A node embedding model was trained on the ontology enriched rare disease KG and k-means clustering was applied to the embedding vectors resulting in 37 disease clusters with a mean size of 87 diseases. We validate the disease clusters quantitatively by looking at semantic similarity of clustered diseases, using the Orphanet Rare Disease Ontology. In addition, the clusters were analyzed for enrichment of associated genes, revealing that the enriched genes within clusters were shown to be highly related.


Discussion
We demonstrate that node embeddings are an effective method for clustering diseases within a heterogenous KG. Semantically similar diseases and relevant enriched genes have been uncovered within the clusters. Connections between disease clusters and approved or investigational drugs are enumerated for follow-up efforts.


Conclusion
Our study lays out a method for clustering rare diseases using the graph node embeddings. We develop an easy to maintain pipeline that can be updated when new data on rare diseases emerges. The embeddings themselves can be paired with other representation learning methods for other data types, such as drugs, to address other predictive modeling problems. Detailed subnetwork analysis and in-depth review of individual clusters may lead to translatable findings. Future work will focus on incorporation of additional data sources, with a particular focus on common disease data.