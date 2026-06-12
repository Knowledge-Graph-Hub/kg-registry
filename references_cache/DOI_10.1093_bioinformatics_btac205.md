---
reference_id: DOI:10.1093/bioinformatics/btac205
title: Design and application of a knowledge network for automatic prioritization of drug mechanisms
authors:
- Michael Mayers
- Roger Tu
- Dylan Steinecke
- Tong Shu Li
- Núria Queralt-Rosinach
- Andrew I Su
journal: Bioinformatics
year: '2022'
doi: 10.1093/bioinformatics/btac205
content_type: abstract_only
---

# Design and application of a knowledge network for automatic prioritization of drug mechanisms
**Authors:** Michael Mayers, Roger Tu, Dylan Steinecke, Tong Shu Li, Núria Queralt-Rosinach, Andrew I Su
**Journal:** Bioinformatics (2022)
**DOI:** [10.1093/bioinformatics/btac205](https://doi.org/10.1093/bioinformatics/btac205)

## Content

Abstract

Motivation
Drug repositioning is an attractive alternative to de novo drug discovery due to reduced time and costs to bring drugs to market. Computational repositioning methods, particularly non-black-box methods that can account for and predict a drug’s mechanism, may provide great benefit for directing future development. By tuning both data and algorithm to utilize relationships important to drug mechanisms, a computational repositioning algorithm can be trained to both predict and explain mechanistically novel indications.


Results
In this work, we examined the 123 curated drug mechanism paths found in the drug mechanism database (DrugMechDB) and after identifying the most important relationships, we integrated 18 data sources to produce a heterogeneous knowledge graph, MechRepoNet, capable of capturing the information in these paths. We applied the Rephetio repurposing algorithm to MechRepoNet using only a subset of relationships known to be mechanistic in nature and found adequate predictive ability on an evaluation set with AUROC value of 0.83. The resulting repurposing model allowed us to prioritize paths in our knowledge graph to produce a predicted treatment mechanism. We found that DrugMechDB paths, when present in the network were rated highly among predicted mechanisms. We then demonstrated MechRepoNet’s ability to use mechanistic insight to identify a drug’s mechanistic target, with a mean reciprocal rank of 0.525 on a test set of known drug–target interactions. Finally, we walked through repurposing examples of the anti-cancer drug imatinib for use in the treatment of asthma, and metolazone for use in the treatment of osteoporosis, to demonstrate this method’s utility in providing mechanistic insight into repurposing predictions it provides.


Availability and implementation
The Python code to reproduce the entirety of this analysis is available at: https://github.com/SuLab/MechRepoNet (archived at https://doi.org/10.5281/zenodo.6456335).


Supplementary information
Supplementary data are available at Bioinformatics online.