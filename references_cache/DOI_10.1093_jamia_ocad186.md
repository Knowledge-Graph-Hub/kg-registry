---
reference_id: DOI:10.1093/jamia/ocad186
title: Clustering rare diseases within an ontology-enriched knowledge graph
authors:
- Jaleal Sanjak
- Jessica Binder
- Arjun Singh Yadaw
- Qian Zhu
- Ewy A Mathé
journal: Journal of the American Medical Informatics Association
year: '2023'
doi: 10.1093/jamia/ocad186
content_type: abstract_only
---

# Clustering rare diseases within an ontology-enriched knowledge graph
**Authors:** Jaleal Sanjak, Jessica Binder, Arjun Singh Yadaw, Qian Zhu, Ewy A Mathé
**Journal:** Journal of the American Medical Informatics Association (2023)
**DOI:** [10.1093/jamia/ocad186](https://doi.org/10.1093/jamia/ocad186)

## Content

Abstract

Objective
Identifying sets of rare diseases with shared aspects of etiology and pathophysiology may enable drug repurposing. Toward that aim, we utilized an integrative knowledge graph to construct clusters of rare diseases.


Materials and Methods
Data on 3242 rare diseases were extracted from the National Center for Advancing Translational Science Genetic and Rare Diseases Information center internal data resources. The rare disease data enriched with additional biomedical data, including gene and phenotype ontologies, biological pathway data, and small molecule-target activity data, to create a knowledge graph (KG). Node embeddings were trained and clustered. We validated the disease clusters through semantic similarity and feature enrichment analysis.


Results
Thirty-seven disease clusters were created with a mean size of 87 diseases. We validate the clusters quantitatively via semantic similarity based on the Orphanet Rare Disease Ontology. In addition, the clusters were analyzed for enrichment of associated genes, revealing that the enriched genes within clusters are highly related.


Discussion
We demonstrate that node embeddings are an effective method for clustering diseases within a heterogenous KG. Semantically similar diseases and relevant enriched genes have been uncovered within the clusters. Connections between disease clusters and drugs are enumerated for follow-up efforts.


Conclusion
We lay out a method for clustering rare diseases using graph node embeddings. We develop an easy-to-maintain pipeline that can be updated when new data on rare diseases emerges. The embeddings themselves can be paired with other representation learning methods for other data types, such as drugs, to address other predictive modeling problems.