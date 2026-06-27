---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.pmgenomics.ca/bhklab/
  - contact_type: github
    value: bhklab
  label: BHKLAB - Computational Oncology Lab
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.uhn.ca/PrincessMargaret
  label: Princess Margaret Cancer Centre
creation_date: '2025-01-10T00:00:00Z'
description: PharmacoDB is a comprehensive integrative pharmacogenomics database that
  aggregates and standardizes large-scale cancer drug screening studies to enable
  systematic exploration and comparison of drug response phenotypes across diverse
  cancer cell line models. The database addresses critical challenges in pharmacogenomics
  research by harmonizing disparate datasets that historically used heterogeneous
  formats for drug sensitivity measurements and lacked standardized identifiers for
  cell lines and compounds. PharmacoDB integrates multiple major cancer pharmacogenomic
  datasets including the Cancer Cell Line Encyclopedia (CCLE), Genomics of Drug Sensitivity
  in Cancer (GDSC), Cancer Therapeutics Response Portal (CTRP), and others, assembling
  them into a unified queryable resource. The database contains dose-response data
  for over 56,000 compounds tested across approximately 1,758 cancer cell lines representing
  30 different tissue types, with more than 6.3 million individual drug screening
  experiments profiling sensitivity measurements. Users can search across all integrated
  studies to identify instances where a specific compound or cell line has been characterized,
  visualize and compare dose-response curves for particular cell line-compound pairs
  from different datasets, and explore patterns of drug sensitivity across tissue
  types. PharmacoDB provides both a user-friendly web interface for interactive browsing
  and data visualization, as well as a RESTful JSON API for programmatic access enabling
  computational workflows and large-scale analyses. The database is designed to support
  biomarker discovery, drug repurposing investigations, and comparative pharmacogenomics
  studies by providing standardized access to otherwise fragmented cancer drug screening
  data.
domains:
- genomics
- pharmacology
homepage_url: https://pharmacodb.ca/
id: pharmacodb
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/gpl-3.0.en.html
  label: GPL-3.0
name: PharmacoDB
products:
- category: GraphicalInterface
  description: Primary web portal for searching and browsing cancer pharmacogenomics
    data across multiple integrated datasets with interactive dose-response curve
    visualization
  format: http
  id: pharmacodb.portal
  name: PharmacoDB Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  product_url: https://pharmacodb.ca/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ccle
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: ctrp
- category: ProgrammingInterface
  description: GraphQL API providing programmatic access to cell lines, compounds,
    tissues, datasets, experiments, and intersections data
  format: http
  id: pharmacodb.api
  is_public: true
  name: PharmacoDB API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  product_url: https://pharmacodb.ca/graphql
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ccle
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: ctrp
- category: DocumentationProduct
  description: Comprehensive user documentation covering search functionality, datasets,
    tissues, cell lines, experiments, genes, compounds, and biomarker discovery features
  format: http
  id: pharmacodb.documentation
  name: PharmacoDB Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  product_url: https://pharmacodb.ca/documentation
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ccle
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: ctrp
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
publications:
- authors:
  - Petr Smirnov
  - Victor Kofia
  - Alexander Maru
  - Mark Freeman
  - Chantal Ho
  - Nehme El-Hachem
  - George-Alexandru Adam
  - Wail Ba-alawi
  - Zhaleh Safikhani
  - Benjamin Haibe-Kains
  doi: 10.1093/nar/gkx911
  id: https://doi.org/10.1093/nar/gkx911
  journal: Nucleic Acids Research
  title: 'PharmacoDB: an integrative database for mining in vitro anticancer drug
    screening studies'
  year: '2018'
- authors:
  - Petr Smirnov
  - Zhaleh Safikhani
  - Nehme El-Hachem
  - Dong Wang
  - Adrian She
  - Catharina Olsen
  - Mark Freeman
  - Heather Selby
  - Deena M.A. Gendoo
  - Patrick Grossmann
  - Andrew H. Beck
  - Hugo J.W.L. Aerts
  - Mathieu Lupien
  - Anna Goldenberg
  - Benjamin Haibe-Kains
  doi: 10.1093/bioinformatics/btv723
  id: https://doi.org/10.1093/bioinformatics/btv723
  journal: Bioinformatics
  title: 'PharmacoGx: an R package for analysis of large pharmacogenomic datasets'
  year: '2016'
repository: https://github.com/bhklab/PharmacoDB
synonyms:
- PharmacoDB
- BHKLAB PharmacoDB
taxon:
- NCBITaxon:9606
---
# PharmacoDB

## Overview

PharmacoDB is an integrative cancer pharmacogenomics database that assembles and standardizes multiple large-scale in vitro drug screening studies into a unified resource, enabling researchers to mine dose-response data for compounds and cell lines across diverse cancer types.