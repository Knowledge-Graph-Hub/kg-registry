---
reference_id: DOI:10.1093/nar/gkz546
title: Quantifying gene selection in cancer through protein functional alteration bias
authors:
- Nadav Brandes
- Nathan Linial
- Michal Linial
journal: Nucleic Acids Research
year: '2019'
doi: 10.1093/nar/gkz546
content_type: abstract_only
---

# Quantifying gene selection in cancer through protein functional alteration bias
**Authors:** Nadav Brandes, Nathan Linial, Michal Linial
**Journal:** Nucleic Acids Research (2019)
**DOI:** [10.1093/nar/gkz546](https://doi.org/10.1093/nar/gkz546)

## Content

Abstract
Compiling the catalogue of genes actively involved in cancer is an ongoing endeavor, with profound implications to the understanding and treatment of the disease. An abundance of computational methods have been developed to screening the genome for candidate driver genes based on genomic data of somatic mutations in tumors. Existing methods make many implicit and explicit assumptions about the distribution of random mutations. We present FABRIC, a new framework for quantifying the selection of genes in cancer by assessing the effects of de-novo somatic mutations on protein-coding genes. Using a machine-learning model, we quantified the functional effects of ∼3M somatic mutations extracted from over 10 000 human cancerous samples, and compared them against the effects of all possible single-nucleotide mutations in the coding human genome. We detected 593 protein-coding genes showing statistically significant bias towards harmful mutations. These genes, discovered without any prior knowledge, show an overwhelming overlap with known cancer genes, but also include many overlooked genes. FABRIC is designed to avoid false discoveries by comparing each gene to its own background model using rigorous statistics, making minimal assumptions about the distribution of random somatic mutations. The framework is an open-source project with a simple command-line interface.