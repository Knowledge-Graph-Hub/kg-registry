---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: tkzeng
  label: Tony Zeng
- category: Individual
  contact_details:
  - contact_type: url
    value: https://zenodo.org/records/15649338
  label: Nils Wagner (Technical University of Munich; precomputed scores)
creation_date: '2026-11-12T00:00:00Z'
description: Pangolin is a deep learning model that predicts splice site usage from
  DNA sequence and the effect of genetic variants on splicing. Trained on splice site
  usage measured in RNA-seq from multiple tissues of human, rhesus macaque, mouse and
  rat, it reports, for a window around each variant, the maximum increase (gain) and
  decrease (loss) in splice site usage and their positions, optionally masked using
  a gene annotation. The Pangolin software is distributed on GitHub under GPL-3.0.
  Precomputed hg38 scores for all SNVs in protein-coding genes, masked using GENCODE
  splice site annotations, were computed with default parameters by researchers at
  the Technical University of Munich and published on Zenodo under CC BY 4.0.
domains:
- biomedical
- genomics
- genetic variation
- information technology
- machine learning
homepage_url: https://github.com/tkzeng/Pangolin
id: pangolin
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/gpl-3.0.html
  label: GPL-3.0
name: Pangolin
products:
- category: ProcessProduct
  description: Pangolin source code and trained models, a Python (PyTorch) tool that
    annotates variants in a VCF or CSV file with splice gain and loss scores, using
    a gene annotation database (GENCODE-based databases are provided) for masking.
    A Google Colab notebook is also provided.
  format: python
  id: pangolin.software
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: Pangolin Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:wasInfluencedBy
    source: gencode
  product_url: https://github.com/tkzeng/Pangolin
- category: Product
  compression: zip
  description: Pangolin precomputed scores for all SNVs in protein-coding genes on hg38,
    computed with default parameters (window size 50 nt) and masked using GENCODE splice
    site annotations, as per-gene TSV files with chromosome, position, reference and
    alternate alleles, gain and loss scores and their relative positions. Computed by
    Nils Wagner and Aleksandr Neverov (Technical University of Munich) and published
    on Zenodo on 2025-06-12.
  format: tsv
  id: pangolin.hg38-snvs-masked
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Pangolin Precomputed hg38 SNV Scores (Masked)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:wasInfluencedBy
    source: gencode
  product_file_size: 12988141317
  product_url: https://zenodo.org/records/15649338
publications:
- authors:
  - Tony Zeng
  - Yang I Li
  doi: 10.1186/s13059-022-02664-4
  id: doi:10.1186/s13059-022-02664-4
  journal: Genome Biology
  preferred: true
  title: Predicting RNA splicing from DNA sequence using Pangolin
  year: '2022'
repository: https://github.com/tkzeng/Pangolin
---
# Pangolin

Pangolin is a deep learning model for predicting RNA splicing from DNA sequence, developed by Tony Zeng and Yang I. Li at the University of Chicago. It was trained on splice site usage quantified from RNA-seq data across four tissues in four mammalian species (human, rhesus macaque, mouse and rat), and predicts both whether a position is a splice site and how strongly it is used. For a variant, Pangolin reports the largest predicted gain and loss in splice site usage within a window around the variant.

## Access

- **Software**: the Pangolin Python package on GitHub (GPL-3.0), which scores VCF or CSV input and can mask scores using a GENCODE-based annotation database. A Colab notebook is provided.
- **Precomputed scores**: masked Pangolin scores for all hg38 SNVs in protein-coding genes, as a 13 GB zip of per-gene TSV files on Zenodo (CC BY 4.0). These were computed by Nils Wagner and Aleksandr Neverov at the Technical University of Munich, not by the original authors.
- Pangolin predictions are also available for single variants through the Broad Institute SpliceAI-lookup web tool (see the SpliceAI page).
