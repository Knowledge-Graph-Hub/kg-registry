---
activity_status: active
category: DataSource
creation_date: '2018-01-05T00:00:00Z'
description: EVLncRNAs is a comprehensive database of experimentally validated functional
  long non-coding RNAs (lncRNAs) curated manually from low-throughput experimental
  studies. The database covers functional lncRNAs from 162 species, including disease
  associations, biological functions, interaction partners, structures, circular RNAs,
  exosomal lncRNAs, peptide-coding lncRNAs, and resistant lncRNAs. EVLncRNAs provides
  functional classifications based on Gene Ontology categories (biological processes,
  cellular components, molecular functions, and clinical applications), detailed interaction
  pathways, and integration with homologous lncRNAs, subcellular localization, phase
  separation, COVID-19, and organoid-related data.
domains:
- genomics
- biological systems
homepage_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/
id: evlncrnas
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: EVLncRNAs
products:
- category: GraphicalInterface
  description: Web portal for browsing and searching experimentally validated functional
    lncRNAs
  format: http
  id: evlncrnas.portal
  name: EVLncRNAs Web Portal
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/
- category: GraphicalInterface
  description: Browse functional lncRNAs by species with sortable entries
  format: http
  id: evlncrnas.species
  name: Species Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/species
- category: GraphicalInterface
  description: Browse lncRNAs by associated diseases including cancers and other pathologies
  format: http
  id: evlncrnas.diseases
  name: Disease Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/diseases
- category: GraphicalInterface
  description: Interactive network visualization of lncRNA interactions with proteins,
    RNAs, and DNAs
  format: http
  id: evlncrnas.interactions
  name: Interaction Network Viewer
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/interactions
- category: GraphicalInterface
  description: Browse lncRNA structural information from experimental studies
  format: http
  id: evlncrnas.structures
  name: Structure Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/structures
- category: GraphicalInterface
  description: Browse peptide-coding lncRNAs validated by experiments
  format: http
  id: evlncrnas.peptide
  name: Peptide-Coding lncRNA Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/peptide-coding
- category: GraphicalInterface
  description: Browse circular RNA (circRNA) entries with functional validation
  format: http
  id: evlncrnas.circrnas
  name: CircRNA Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/circrnas
- category: GraphicalInterface
  description: Browse exosomal lncRNAs from extracellular vesicles
  format: http
  id: evlncrnas.exosomal
  name: Exosomal lncRNA Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/exosomal
- category: GraphicalInterface
  description: Browse resistant lncRNAs including drug resistance-associated entries
  format: http
  id: evlncrnas.resistant
  name: Resistant lncRNA Browser
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/resistant
- category: DocumentationProduct
  description: Help documentation and usage instructions for EVLncRNAs database
  format: http
  id: evlncrnas.help
  name: Help Documentation
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/help
- category: Product
  description: Download page for bulk data access to EVLncRNAs database content
  format: http
  id: evlncrnas.download
  name: Download Data
  product_url: https://www.sdklab-biophysics-dzu.net/EVLncRNAs3/#/download
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/help/public-database
publications:
- authors:
  - Bailing Zhou
  - Baohua Ji
  - Congcong Shen
  - Xia Zhang
  - Xue Yu
  - Pingping Huang
  - Ru Yu
  - Hongmei Zhang
  - Xianghua Dou
  - Qingshuai Chen
  - Gang Hu
  - Keren Wang
  - Fengcui Qian
  - Fengxia Chen
  - Xiaojuan Zhi
  - Chunqing Wang
  - Jian Ren
  - Yan Wang
  id: https://doi.org/10.1093/nar/gkad1057
  journal: Nucleic Acids Research
  preferred: true
  title: 'EVLncRNAs 3.0: an updated comprehensive database for manually curated functional
    long non-coding RNAs validated by low-throughput experiments'
  year: '2024'
taxon:
- NCBITaxon:9606
---
# EVLncRNAs

EVLncRNAs is the first and exclusive comprehensive database of all experimentally validated functional long non-coding RNAs (lncRNAs) from various species. Version 3.0 contains 6,195 functional lncRNAs from 162 species, representing a 154% increase from the previous version through exhaustive manual curation of nearly 25,000 publications from May 2020 to May 2023.

The database focuses on functional lncRNAs validated by low-throughput experimental methods (qRT-PCR, knockdown, northern blot, luciferase reporter assays) and excludes predictions from high-throughput sequencing alone. Coverage includes 1,726 diseases, 20,917 disease associations, 14,692 interactions, 87 peptide-coding lncRNAs, 11 structures, 440 circRNAs, 2,540 resistant lncRNAs, and 1,559 exosomal RNAs.

New features in version 3.0 include functional classifications following Gene Ontology categories, detailed interaction pathways, 765 homologous lncRNAs, 327 subcellular location entries, 32 COVID-19-related lncRNAs, 14 phase separation-associated lncRNAs, and 41 organoid-related lncRNAs. The database also features ChatGPT-generated summaries for the top 100 most frequently studied lncRNAs (with appropriate caution notes).

The most frequently studied lncRNAs include MALAT1, NEAT1, H19, and HOTAIR, which continue to show novel functions across various diseases and biological processes. The database demonstrates that functional lncRNA research remains a highly active field with over 3,000 related publications annually.