---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: westlake-repl
  - contact_type: url
    value: https://github.com/westlake-repl/SaProt/issues
  label: Westlake University (Fajie Yuan lab)
creation_date: '2026-11-12T00:00:00Z'
description: SaProt is a structure-aware protein language model from Westlake University.
  It uses a structure-aware vocabulary that combines each amino acid with a Foldseek
  3Di structure token, and was pre-trained on about 40 million AlphaFold2-predicted
  protein structures (UniRef50 clusters), with a 650M model further trained on PDB
  structures and a 1.3B model also trained on metagenomic and NCBI sequences. SaProt
  supports zero-shot prediction of mutational effects (including missense variant
  pathogenicity, benchmarked on ClinVar and ProteinGym) and fine-tuning for protein
  property prediction. The authors distribute the trained models (35M, 650M and 1.3B
  parameters) and the AF2_UniRef50 pre-training dataset on Hugging Face and the code
  on GitHub under the MIT license, along with ColabSaprot and the SaprotHub model-sharing
  platform. The authors do not distribute precomputed variant-effect scores.
domains:
- biomedical
- proteomics
- protein structure
- genomics
- genetic variation
- information technology
- machine learning
homepage_url: https://github.com/westlake-repl/SaProt
id: saprot
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/westlake-repl/SaProt/blob/main/LICENSE
  label: MIT
name: SaProt
products:
- category: ProcessProduct
  description: SaProt source code (Python, PyTorch) for pre-training, fine-tuning,
    zero-shot mutational effect prediction and benchmark evaluation (including ProteinGym
    and ClinVar), with Foldseek-based conversion of protein structures into structure-aware
    sequences.
  format: python
  id: saprot.software
  name: SaProt Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: saprot
  product_url: https://github.com/westlake-repl/SaProt
- category: Product
  description: Trained SaProt model checkpoint (650M parameters) pre-trained on about
    40 million AlphaFold2 structures, loadable with Hugging Face Transformers. Other
    released checkpoints include SaProt_35M_AF2, SaProt_650M_PDB, SaProt_1.3B_AF2 and
    SaProt_1.3B_AFDB_OMG_NCBI in the same organization.
  format: mixed
  id: saprot.models
  name: SaProt Models
  original_source:
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:wasInfluencedBy
    source: alphafold
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: pdb
  product_url: https://huggingface.co/westlake-repl/SaProt_650M_AF2
- category: Product
  description: AF2_UniRef50, the SaProt pre-training dataset of structure-aware sequences
    derived from AlphaFold2-predicted structures of UniRef50 representative proteins,
    in LMDB format with CSV train and validation splits.
  format: mixed
  id: saprot.af2-uniref50
  name: SaProt AF2_UniRef50 Pre-training Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://huggingface.co/datasets/westlake-repl/AF2_UniRef50
- category: ProcessProduct
  description: SaprotHub and ColabSaprot, a platform and Google Colab notebook for training,
    sharing and using fine-tuned SaProt models without programming, with a Hugging Face
    community hub for sharing models.
  format: python
  id: saprot.saprothub
  name: SaprotHub and ColabSaprot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: saprot
  product_url: https://github.com/westlake-repl/SaprotHub
publications:
- authors:
  - Jin Su
  - Chenchen Han
  - Yuyang Zhou
  - Junjie Shan
  - Xibin Zhou
  - Fajie Yuan
  doi: 10.1101/2023.10.01.560349
  id: doi:10.1101/2023.10.01.560349
  journal: bioRxiv
  preferred: true
  title: 'SaProt: Protein Language Modeling with Structure-aware Vocabulary'
  year: '2023'
- authors:
  - Jin Su
  - Zhikai Li
  - Tianli Tao
  - Chenchen Han
  - Yan He
  - Fengyuan Dai
  - Fajie Yuan
  doi: 10.1038/s41587-025-02859-7
  id: doi:10.1038/s41587-025-02859-7
  journal: Nature Biotechnology
  title: Democratizing protein language model training, sharing and collaboration
  year: '2026'
repository: https://github.com/westlake-repl/SaProt
---
# SaProt

SaProt is a protein language model developed by Fajie Yuan's group at Westlake University. Each residue is represented by a structure-aware token that pairs the amino acid with a Foldseek 3Di token describing its local structure. The model was pre-trained on about 40 million AlphaFold2-predicted structures and was presented at ICLR 2024 (spotlight). It can score the effect of amino acid substitutions without task-specific training and can be fine-tuned for protein property prediction.

## Access

- **Models**: 35M, 650M and 1.3B parameter checkpoints in the `westlake-repl` Hugging Face organization (MIT).
- **Pre-training data**: the AF2_UniRef50 dataset on Hugging Face.
- **Software**: the SaProt GitHub repository, with code for zero-shot mutational effect prediction and fine-tuning.
- **SaprotHub / ColabSaprot**: tools for training and sharing fine-tuned models, published in *Nature Biotechnology* (2025).

The authors do not distribute precomputed variant-effect scores.
