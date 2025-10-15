---
activity_status: active
category: DataSource
creation_date: '2025-07-17T00:00:00Z'
description: miRTarBase is a comprehensive database of experimentally validated microRNA-target interactions (MTIs). It collects and curates miRNA-target interactions with experimental evidence from the literature, including data from reporter assays, western blot, qPCR, microarray, and high-throughput experiments such as CLIP-Seq.
domains:
  - genomics
  - biological systems
id: mirtarbase
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: miRTarBase
products:
  - category: GraphicalInterface
    name: miRTarBase Web Portal
    id: mirtarbase.portal
    description: Web interface for searching and browsing experimentally validated microRNA-target interactions across multiple species.
    format: http
    product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/index.php
  - category: Product
    name: miRTarBase Complete MTI Dataset
    id: mirtarbase.mti
    description: Complete dataset of microRNA-target interactions (MTI) in CSV format containing all experimentally validated interactions.
    format: csv
    product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  - category: Product
    name: miRTarBase Target Sites Dataset
    id: mirtarbase.target_sites
    description: Dataset of microRNA target sites with detailed binding site information in CSV format.
    format: csv
    product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  - category: Product
    name: miRTarBase Species-Specific MTI Files
    id: mirtarbase.species_mti
    description: Species-specific microRNA-target interaction datasets in CSV format for human, mouse, rat, and 25+ other species.
    format: csv
    product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  - category: Product
    name: miRTarBase Strong Evidence Datasets
    id: mirtarbase.strong_evidence
    description: Curated datasets filtered for strong experimental evidence including reporter assays, western blot, qPCR, and CLIP-Seq data.
    format: csv
    product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  - category: Product
    name: miRTarBase Previous Releases Archive
    id: mirtarbase.archive
    description: Archive of previous miRTarBase releases for reproducibility and historical comparisons.
    format: http
    product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
publications:
  - id: "https://doi.org/10.1093/nar/gkae1072"
    preferred: true
    title: "miRTarBase 2025: updates to the collection of experimentally validated microRNA-target interactions"
    authors:
      - Cui S
      - Yu S
      - Huang HY
      - Lin YCD
      - Huang Y
      - Zhang B
      - Xiao J
      - Zuo H
      - Wang J
      - Li Z
    year: "2024"
    journal: "Nucleic Acids Research"
  - id: "https://doi.org/10.1093/nar/gkab1079"
    preferred: false
    title: "miRTarBase update 2022: an informative resource for experimentally validated miRNA-target interactions"
    authors:
      - Huang HY
      - Lin YCD
      - Cui S
      - Huang Y
      - Tang Y
      - Xu J
      - Bao J
      - Li Y
      - Wen J
      - Zuo H
    year: "2022"
    journal: "Nucleic Acids Research"
---

# miRTarBase

miRTarBase is a comprehensive database that curates experimentally validated microRNA-target interactions (MTIs) from published literature. Developed by the Warshel Institute for Computational Biology at The Chinese University of Hong Kong, Shenzhen, miRTarBase collects MTIs with experimental evidence from various methods including reporter assays, western blot, qPCR, microarray, and next-generation sequencing experiments such as CLIP-Seq and degradome sequencing. The database covers over 28 species and provides detailed information about target sites, experimental evidence, and validation methods. Users can browse and download complete datasets in CSV format, including species-specific files and subsets filtered by evidence strength. For more information, visit the [miRTarBase portal](https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/index.php).
