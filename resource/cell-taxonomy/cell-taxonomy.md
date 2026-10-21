---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ngdc.cncb.ac.cn/celltaxonomy/
  label: National Genomics Data Center, CNCB
creation_date: '2026-10-21T00:00:00Z'
description: Cell Taxonomy is a manually curated repository of cell types and their associated
  marker genes across species, tissues, and conditions, hosted by the China National Center
  for Bioinformation (CNCB) / National Genomics Data Center. It integrates cell markers with
  multifaceted characterization including marker and cluster quality assessment, cross-species
  comparison, tissue cell composition, and marker-based cellular similarity. The release described
  in its 2023 paper spans 3,143 cell types and 26,613 cell markers across 34 species, drawing
  on 4,299 publications and single-cell profiles of about 3.5 million cells.
domains:
- cell biology
- single-cell analysis
- biological systems
homepage_url: https://ngdc.cncb.ac.cn/celltaxonomy/
id: cell-taxonomy
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: Cell Taxonomy
products:
- category: GraphicalInterface
  description: Web interface to browse and search curated cell types, markers, tissues, species,
    and single-cell studies, with Cell Type Comparator and Predictor tools.
  format: http
  id: cell-taxonomy.portal
  name: Cell Taxonomy Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cell-taxonomy
  product_url: https://ngdc.cncb.ac.cn/celltaxonomy/
- category: Product
  description: Bulk download of the curated cell types and their associated marker genes as
    a single tab-delimited plain-text table.
  format: txt
  id: cell-taxonomy.download
  name: Cell Taxonomy Cell Types and Markers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cell-taxonomy
  product_url: https://download.cncb.ac.cn/celltaxonomy/Cell_Taxonomy_resource.txt
publications:
- authors:
  - Shuai Jiang
  - Qiheng Qian
  - Tongtong Zhu
  - Wenting Zong
  - Yunfei Shang
  - et al.
  doi: 10.1093/nar/gkac816
  id: doi:10.1093/nar/gkac816
  journal: Nucleic Acids Research
  preferred: true
  title: 'Cell Taxonomy: a curated repository of cell types with multifaceted characterization'
  year: '2023'
---

# Cell Taxonomy

## Overview

Cell Taxonomy is a curated repository of cell types and their marker genes across species and tissues, hosted by the China National Center for Bioinformation (CNCB). It pairs cell markers with quality assessment, cross-species comparison, and tissue composition analyses.

## Access

- Cell Taxonomy browser: search cell types, markers, tissues, and single-cell studies.
- Bulk download: the curated cell types and markers as a tab-delimited table.

## Citation

Please cite: Jiang S, Qian Q, Zhu T, et al. Cell Taxonomy: a curated repository of cell types with multifaceted characterization. Nucleic Acids Res. 2023;51(D1):D853–D860. doi:10.1093/nar/gkac816
