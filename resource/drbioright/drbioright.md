---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@drbioright.org
  - contact_type: url
    value: https://drbioright.org/
  label: Han Liang Lab (MD Anderson Cancer Center) and Jun Li Lab (UNC Chapel Hill)
creation_date: '2026-10-27T00:00:00Z'
description: DrBioRight is a web platform for natural-language analysis of cancer omics
  data, backed by a large curated collection of cancer omics datasets. Users search
  datasets and pose questions in plain language; a large language model-based chatbot
  turns the questions into analyses, generating and running code and returning visualizations
  and interpretations. The platform hosts about 508,000 samples across about 4,200
  cohorts, spanning RNA expression, protein expression, DNA methylation, DNA mutations,
  and copy number variation, including molecular, clinical, and functional data from
  The Cancer Genome Atlas and the Cancer Cell Line Encyclopedia and the RPPA500 functional
  proteomics compendium of The Cancer Proteome Atlas. DrBioRight is developed by the
  Han Liang Lab (Department of Bioinformatics and Computational Biology, MD Anderson
  Cancer Center) and the Jun Li Lab (School of Data and Information Sciences, UNC Chapel
  Hill), with support from the NIH Informatics Technology for Cancer Research (ITCR)
  program.
domains:
- cancer
- proteomics
- genomics
- epigenomics
- biomedical
homepage_url: https://drbioright.org/
id: drbioright
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://drbioright.org/
  label: Custom (free for academic non-profit use; commercial license required otherwise)
name: DrBioRight
products:
- category: GraphicalInterface
  description: DrBioRight web platform and LLM-powered chatbot for searching curated
    cancer omics datasets and running analyses and visualizations through natural-language
    questions. Integrates molecular, clinical, and functional data from The Cancer Genome
    Atlas (via the GDC), the Cancer Cell Line Encyclopedia (via DepMap), and the RPPA500
    functional proteomics data of The Cancer Proteome Atlas.
  format: http
  id: drbioright.portal
  name: DrBioRight Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drbioright
  - relation_type: prov:hadPrimarySource
    source: tcga
  - relation_type: prov:hadPrimarySource
    source: gdc
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: tcpa
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://drbioright.org/
- category: DocumentationProduct
  description: DrBioRight user documentation describing datasets, query workflow, and
    analysis features of the platform.
  format: http
  id: drbioright.docs
  name: DrBioRight Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drbioright
  product_url: https://drbioright.org/docs
publications:
- authors:
  - Wei Liu
  - Jun Li
  - Yitao Tang
  - Yining Zhao
  - Chaozhong Liu
  - Meiyi Song
  - et al.
  doi: 10.1038/s41467-025-57430-4
  id: doi:10.1038/s41467-025-57430-4
  journal: Nature Communications
  preferred: true
  title: 'DrBioRight 2.0: an LLM-powered bioinformatics chatbot for large-scale cancer
    functional proteomics analysis'
  year: '2025'
- authors:
  - Jun Li
  - Hu Chen
  - Yumeng Wang
  - Mei-Ju May Chen
  - Han Liang
  doi: 10.1016/j.ccell.2020.09.002
  id: doi:10.1016/j.ccell.2020.09.002
  journal: Cancer Cell
  title: Next-Generation Analytics for Omics Data
  year: '2021'
taxon:
- NCBITaxon:9606
version: 3.2.41
---
# DrBioRight

## Overview

DrBioRight is a natural-language analytics platform for cancer omics data. Researchers search a curated collection of datasets and ask questions in plain language; an LLM-powered chatbot turns them into analyses, runs the code, and returns figures and interpretations. The platform covers about 508,000 samples in about 4,200 cohorts across RNA expression (170,808 samples / 3,880 cohorts), protein expression (35,982 / 131), DNA methylation (35,106 / 127), DNA mutations (313,698 / 539), and copy number variation (260,122 / 344).

DrBioRight 2.0 added a fine-tuned large language model and the RPPA500 pan-cancer functional proteomics compendium from The Cancer Proteome Atlas (about 7,800 TCGA tumors and 880 CCLE cell lines profiled for 447 protein markers). Molecular, functional, and clinical data come from TCGA (via the GDC) and CCLE (via DepMap); protein markers are linked to MSigDB hallmark gene sets.

## Access

- DrBioRight web platform (sign-in required for analysis).
- Documentation pages on the platform.

The platform is free for academic non-profit institutions; other users need a commercial license (contact support@drbioright.org). The current platform version is 3.2.41 (Platform v3.0 release).

## Citation

Liu W, Li J, Tang Y, et al. DrBioRight 2.0: an LLM-powered bioinformatics chatbot for large-scale cancer functional proteomics analysis. Nat Commun. 2025;16:2256. doi:10.1038/s41467-025-57430-4

Li J, Chen H, Wang Y, Chen MM, Liang H. Next-Generation Analytics for Omics Data. Cancer Cell. 2021. doi:10.1016/j.ccell.2020.09.002
