---
reference_id: DOI:10.1186/s13059-020-1949-z
title: Robustness and applicability of transcription factor and pathway analysis tools on single-cell RNA-seq data
authors:
- Christian H. Holland
- Jovan Tanevski
- Javier Perales-Patón
- Jan Gleixner
- Manu P. Kumar
- Elisabetta Mereu
- Brian A. Joughin
- Oliver Stegle
- Douglas A. Lauffenburger
- Holger Heyn
- Bence Szalai
- Julio Saez-Rodriguez
journal: Genome Biology
year: '2020'
doi: 10.1186/s13059-020-1949-z
content_type: abstract_only
---

# Robustness and applicability of transcription factor and pathway analysis tools on single-cell RNA-seq data
**Authors:** Christian H. Holland, Jovan Tanevski, Javier Perales-Patón, Jan Gleixner, Manu P. Kumar, Elisabetta Mereu, Brian A. Joughin, Oliver Stegle, Douglas A. Lauffenburger, Holger Heyn, Bence Szalai, Julio Saez-Rodriguez
**Journal:** Genome Biology (2020)
**DOI:** [10.1186/s13059-020-1949-z](https://doi.org/10.1186/s13059-020-1949-z)

## Content

Abstract

Background
Many functional analysis tools have been developed to extract functional and mechanistic insight from bulk transcriptome data. With the advent of single-cell RNA sequencing (scRNA-seq), it is in principle possible to do such an analysis for single cells. However, scRNA-seq data has characteristics such as drop-out events and low library sizes. It is thus not clear if functional TF and pathway analysis tools established for bulk sequencing can be applied to scRNA-seq in a meaningful way.


Results
To address this question, we perform benchmark studies on simulated and real scRNA-seq data. We include the bulk-RNA tools PROGENy, GO enrichment, and DoRothEA that estimate pathway and transcription factor (TF) activities, respectively, and compare them against the tools SCENIC/AUCell and metaVIPER, designed for scRNA-seq. For the in silico study, we simulate single cells from TF/pathway perturbation bulk RNA-seq experiments. We complement the simulated data with real scRNA-seq data upon CRISPR-mediated knock-out. Our benchmarks on simulated and real data reveal comparable performance to the original bulk data. Additionally, we show that the TF and pathway activities preserve cell type-specific variability by analyzing a mixture sample sequenced with 13 scRNA-seq protocols. We also provide the benchmark data for further use by the community.


Conclusions
Our analyses suggest that bulk-based functional analysis tools that use manually curated footprint gene sets can be applied to scRNA-seq data, partially outperforming dedicated single-cell tools. Furthermore, we find that the performance of functional analysis tools is more sensitive to the gene sets than to the statistic used.