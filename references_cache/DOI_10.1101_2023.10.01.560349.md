---
reference_id: DOI:10.1101/2023.10.01.560349
title: "SaProt: Protein Language Modeling with Structure-aware Vocabulary"
authors:
- Jin Su
- Chenchen Han
- Yuyang Zhou
- Junjie Shan
- Xibin Zhou
- Fajie Yuan
year: '2023'
doi: 10.1101/2023.10.01.560349
content_type: abstract_only
---

# SaProt: Protein Language Modeling with Structure-aware Vocabulary
**Authors:** Jin Su, Chenchen Han, Yuyang Zhou, Junjie Shan, Xibin Zhou, Fajie Yuan
**DOI:** [10.1101/2023.10.01.560349](https://doi.org/10.1101/2023.10.01.560349)

## Content

A
                  bstract


                  Large-scale protein language models (PLMs), such as the ESM family, have achieved remarkable performance in various downstream tasks related to protein structure and function by undergoing unsupervised training on residue sequences. They have become essential tools for researchers and practitioners in biology. However, a limitation of vanilla PLMs is their lack of
                  explicit
                  consideration for protein structure information, which suggests the potential for further improvement. Motivated by this, we introduce the concept of a “
                  s
                  tructure-
                  a
                  ware vocabulary” that integrates residue tokens with structure tokens. The structure tokens are derived by encoding the 3D structure of proteins using Foldseek. We then propose SaProt, a large-scale general-purpose PLM trained on an extensive dataset comprising approximately 40 million protein sequences and structures. Through extensive evaluation, our SaProt model surpasses well-established and renowned baselines across 10 significant downstream tasks, demonstrating its exceptional capacity and broad applicability. We have made the code
                  1
                  , pre-trained model, and all relevant materials available at
                  https://github.com/westlake-repl/SaProt
                  .