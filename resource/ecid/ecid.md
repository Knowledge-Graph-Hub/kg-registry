---
activity_status: active
category: DataSource
collection:
- ber
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
description: ECID is a biomedical knowledgebase of curated inter-chemical correlations
  from the core chemical datasets in exposomics. These datasets are prioritized from
  human biomonitoring studies using targeted and untargeted assays. ECID has applications
  in characterizing and understanding the effects of exposome chemicals on the human
  health.
domains:
- environment
- health
- chemistry and biochemistry
- public health
- social determinants
- biomedical
homepage_url: https://www.ecidbase.org/
id: ecid
layout: resource_detail
name: ECID
repository: https://github.com/idslme/ecid
publications:
- id: doi:10.1016/j.envint.2022.107240
  title: 'CCDB: A database for exploring inter-chemical correlations in metabolomics
    and exposomics datasets'
  authors:
  - Barupal DK
  - Mahajan P
  - Fakouri-Baygi S
  - Wright RO
  - Arora M
  - Teitelbaum SL
  year: '2022'
  doi: doi:10.1016/j.envint.2022.107240
products:
- category: GraphicalInterface
  description: Interface for the Chemical Correlation Database for exploring curated
    inter-chemical correlations
  id: ecid.ccdb.site
  name: CCDB
  is_public: true
  original_source:
  - ecid
  product_url: https://ccdb.ecidbase.org/
  secondary_source:
  - ecid
- category: GraphicalInterface
  description: Interface for Exposome Data Interpretation Resource for interpreting
    inter-chemical correlations
  id: ecid.edir.site
  is_public: true
  name: EDIR
  original_source:
  - ecid
  product_url: https://edir.ecidbase.org/
  secondary_source:
  - ecid
- category: Product
  description: Compound lists from 73 untargeted datasets with 3,329 unique 2D structures.
  id: ecid.compound.lists
  name: ECID Compound Lists
  is_public: true
  product_url: https://zenodo.org/records/15204234
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: Analytes measured by targeted assays for the NIEHS HHEAR program.
  id: ecid.hhear.analyte.list
  name: HHEAR Analyte List
  is_public: true
  product_url: https://zenodo.org/records/15127651
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: Chemical analytes reported for the ECHO cohort measured by targeted
    assays.
  id: ecid.echo.analyte.list
  name: ECHO Analyte List
  is_public: true
  product_url: https://zenodo.org/records/15127650
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: Selected datasets (n=289) for computing and curating inter-chemical
    correlations.
  id: ecid.dataset.list
  name: ECID Dataset List
  is_public: true
  product_url: https://zenodo.org/records/15122961
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: Chemical analytes reported by the NHANES biomonitoring survey.
  id: ecid.nhanes.analyte.list
  name: NHANES Analyte List
  is_public: true
  product_url: https://zenodo.org/records/11528668
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: Metabolite and chemical names reported by Metabolon Inc. in PMC articles.
  id: ecid.metabolomics.data.dictionary
  name: Metabolomics Data Dictionary
  is_public: true
  product_url: https://zenodo.org/records/10974865
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: mwTAB files processed to yield curated compound names and identifiers.
  id: ecid.metabolomics.workbench.dictionary
  name: Metabolomics WorkBench Compound Dictionary
  is_public: true
  product_url: https://zenodo.org/records/10963201
  original_source:
  - ecid
  secondary_source:
  - ecid
- category: Product
  description: Catalogues chemicals expected and detected in human blood specimens.
  id: ecid.bloodexposome.data
  name: Blood Exposome Database
  is_public: true
  product_url: https://zenodo.org/records/8146024
  original_source:
  - ecid
  secondary_source:
  - ecid
  format: csv
taxon:
- NCBITaxon:9606
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