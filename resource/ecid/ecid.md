---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ecidbase.org/contact
  label: Integrated Data Science Laboratory for Metabolomics and Exposomics (IDSL-ME)
- category: Individual
  contact_details:
  - contact_type: email
    value: dinesh.barupal@mssm.edu
  label: Dinesh Kumar Barupal
description: >-
    ECID is a biomedical knowledgebase of curated inter-chemical correlations from the core chemical datasets in exposomics. These datasets are prioritized from human biomonitoring studies using targeted and untargeted assays. ECID has applications in characterizing and understanding the effects of exposome chemicals on the human health.
domains:
  - environment
  - health
  - chemistry and biochemistry
homepage_url: https://www.ecidbase.org/
id: ecid
layout: resource_detail
name: ECID
repository: https://github.com/idslme/ecid
publications:
- id: "doi:10.1016/j.envint.2022.107240"
  title: "CCDB: A database for exploring inter-chemical correlations in metabolomics and exposomics datasets"
  authors:
    - Barupal DK
    - Mahajan P
    - Fakouri-Baygi S
    - Wright RO
    - Arora M
    - Teitelbaum SL
  year: "2022"
  doi: "doi:10.1016/j.envint.2022.107240"
products:
- category: GraphicalInterface
  description: Interface for the Chemical Correlation Database for exploring curated inter-chemical correlations
  id: ecid.ccdb.site
  name: CCDB
  is_public: true
  original_source:
  - ecid
  product_url: https://ccdb.ecidbase.org/
  secondary_source:
  - ecid
- category: GraphicalInterface
  description: Interface for Exposome Data Interpretation Resource for interpreting inter-chemical correlations
  id: ecid.edir.site
  is_public: true
  name: EDIR
  original_source:
  - ecid
  product_url: https://edir.ecidbase.org/
  secondary_source:
  - ecid
---

# Exposome Correlation and Interpretation Database (ECID)

ECID (Exposome Correlation and Interpretation Database) is a comprehensive biomedical knowledgebase focused on curated inter-chemical correlations from core chemical datasets in exposomics research. These datasets are prioritized from human biomonitoring studies using both targeted and untargeted assays. ECID serves as a valuable resource for characterizing and understanding the effects of exposome chemicals on human health.

## Main Components

ECID is comprised of three main online modules:

1. **CCDB (Chemical Correlation DataBase)**: Allows users to explore curated inter-chemical correlations, providing insights into relationships between various environmental chemicals.

2. **EDIR (Exposome Data Interpretation Resource)**: Offers informatics resources designed to interpret the inter-chemical correlations, helping researchers make sense of complex chemical relationship data.

3. **EWS (Exposomics WorkSpace)**: Provides tools for analysis and mapping of new data into ECID resources, enabling researchers to integrate their own findings with existing knowledge.

## Development and Maintenance

ECID is developed and maintained by the Integrated Data Science Laboratory for Metabolomics and Exposomics (IDSL-ME) at the Department of Environmental Medicine and Public Health, Icahn School of Medicine at Mount Sinai, New York, USA.

## Funding

The ECID Biomedical Knowledgebase is supported (2023-2028) by the National Institute of Environmental Health Sciences (NIEHS), National Institute of Health (NIH), USA through grant U24ES035386.