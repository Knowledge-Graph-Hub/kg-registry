---
reference_id: DOI:10.1093/bioinformatics/btab271
title: "KG4SL: knowledge graph neural network for synthetic lethality prediction in human cancers"
authors:
- Shike Wang
- Fan Xu
- Yunyang Li
- Jie Wang
- Ke Zhang
- Yong Liu
- Min Wu
- Jie Zheng
journal: Bioinformatics
year: '2021'
doi: 10.1093/bioinformatics/btab271
content_type: abstract_only
---

# KG4SL: knowledge graph neural network for synthetic lethality prediction in human cancers
**Authors:** Shike Wang, Fan Xu, Yunyang Li, Jie Wang, Ke Zhang, Yong Liu, Min Wu, Jie Zheng
**Journal:** Bioinformatics (2021)
**DOI:** [10.1093/bioinformatics/btab271](https://doi.org/10.1093/bioinformatics/btab271)

## Content

Abstract

Motivation
Synthetic lethality (SL) is a promising gold mine for the discovery of anti-cancer drug targets. Wet-lab screening of SL pairs is afflicted with high cost, batch-effect, and off-target problems. Current computational methods for SL prediction include gene knock-out simulation, knowledge-based data mining and machine learning methods. Most of the existing methods tend to assume that SL pairs are independent of each other, without taking into account the shared biological mechanisms underlying the SL pairs. Although several methods have incorporated genomic and proteomic data to aid SL prediction, these methods involve manual feature engineering that heavily relies on domain knowledge.


Results
Here, we propose a novel graph neural network (GNN)-based model, named KG4SL, by incorporating knowledge graph (KG) message-passing into SL prediction. The KG was constructed using 11 kinds of entities including genes, compounds, diseases, biological processes and 24 kinds of relationships that could be pertinent to SL. The integration of KG can help harness the independence issue and circumvent manual feature engineering by conducting message-passing on the KG. Our model outperformed all the state-of-the-art baselines in area under the curve, area under precision-recall curve and F1. Extensive experiments, including the comparison of our model with an unsupervised TransE model, a vanilla graph convolutional network model, and their combination, demonstrated the significant impact of incorporating KG into GNN for SL prediction.


Availability and implementation
: KG4SL is freely available at https://github.com/JieZheng-ShanghaiTech/KG4SL.


Supplementary information
Supplementary data are available at Bioinformatics online.