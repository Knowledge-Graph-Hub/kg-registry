---
layout: eval_detail
---

# Evaluation for pharmkg

| Field | Value |
|---|---|
| Access Level and Types | Yes - PharmKG provides embeddings, learned low-dimensional representations for entities and relations via KGE models. It also provides top predicted paths for mechanistic interpretation (Fig 6) and t-SNE visualizations showing semantic structure (Fig 5). |
| Provenance of Nodes and Edges | Yes — An integration of 6 sources (OMIM, DrugBank, PharmGKB, TTD, SIDER, HumanNet); plus entity features from MeSH, PubChem, BioBERT, BioGPS, and Connectivity Map |
| Documented standards, schema, construction | Yes - All entities explicitly use standard biomedical identifiers and the structure is designed to support drug repurposing, target discovery, adverse reaction prediction, etc., in real-world biomedical tasks |
| Update frequency and versioning | No - There is no formal semantic versioning scheme mentioned for the dataset or codebase |
| Evaluation - Metrics and Fitness for Purpose | Yes - Provide detailed case studies for Alzheimer’s disease and Parkinson’s disease for drug repurposing and target discovery, with literature validation, top scored predictions, and visualized paths |
| License Information | No explicit license (restricted use). The paper notes: “© The Author(s) 2020. Published by Oxford University Press. All rights reserved.” But does not reveal license information (nor does the GitHub repo) |
