---
reference_id: DOI:10.1093/gigascience/giad047
title: Hetnet connectivity search provides rapid insights into how biomedical entities are related
authors:
- Daniel S Himmelstein
- Michael Zietz
- Vincent Rubinetti
- Kyle Kloster
- Benjamin J Heil
- Faisal Alquaddoomi
- Dongbo Hu
- David N Nicholson
- Yun Hao
- Blair D Sullivan
- Michael W Nagle
- Casey S Greene
journal: GigaScience
year: '2022'
doi: 10.1093/gigascience/giad047
content_type: abstract_only
---

# Hetnet connectivity search provides rapid insights into how biomedical entities are related
**Authors:** Daniel S Himmelstein, Michael Zietz, Vincent Rubinetti, Kyle Kloster, Benjamin J Heil, Faisal Alquaddoomi, Dongbo Hu, David N Nicholson, Yun Hao, Blair D Sullivan, Michael W Nagle, Casey S Greene
**Journal:** GigaScience (2022)
**DOI:** [10.1093/gigascience/giad047](https://doi.org/10.1093/gigascience/giad047)

## Content

Abstract

Background
Hetnets, short for “heterogeneous networks,” contain multiple node and relationship types and offer a way to encode biomedical knowledge. One such example, Hetionet, connects 11 types of nodes—including genes, diseases, drugs, pathways, and anatomical structures—with over 2 million edges of 24 types. Previous work has demonstrated that supervised machine learning methods applied to such networks can identify drug repurposing opportunities. However, a training set of known relationships does not exist for many types of node pairs, even when it would be useful to examine how nodes of those types are meaningfully connected. For example, users may be curious about not only how metformin is related to breast cancer but also how a given gene might be involved in insomnia.


Findings
We developed a new procedure, termed hetnet connectivity search, that proposes important paths between any 2 nodes without requiring a supervised gold standard. The algorithm behind connectivity search identifies types of paths that occur more frequently than would be expected by chance (based on node degree alone). Several optimizations were required to precompute significant instances of node connectivity at the scale of large knowledge graphs.


Conclusion
We implemented the method on Hetionet and provide an online interface at https://het.io/search. We provide an open-source implementation of these methods in our new Python package named hetmatpy.