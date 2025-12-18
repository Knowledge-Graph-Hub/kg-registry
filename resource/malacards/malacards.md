---
activity_status: active
category: Aggregator
creation_date: '2025-09-09T00:00:00Z'
description: MalaCards is a comprehensive, searchable database integrating information
  about human diseases from 78 data sources. It provides integrated disease annotations
  including genes, symptoms, drugs, mutations, publications, clinical trials, and
  pathways for over 22,000 human disorders.
domains:
- health
- clinical
- genomics
- biomedical
id: malacards
last_modified_date: '2025-10-10T00:00:00Z'
layout: resource_detail
name: MalaCards
products:
- category: GraphicalInterface
  description: Searchable web interface for exploring human diseases with integrated
    data on genes, symptoms, drugs, mutations, clinical trials and more.
  format: http
  id: malacards.portal
  name: MalaCards Web Portal
  product_url: https://www.malacards.org/
- category: GraphicalInterface
  description: Browse diseases by global categories (cancer, genetic, rare, etc.)
    and anatomical categories (neuronal, cardiovascular, etc.).
  format: http
  id: malacards.categories
  name: MalaCards Disease Categories
  product_url: https://www.malacards.org/categories
- category: GraphicalInterface
  description: Advanced search interface for querying diseases by multiple criteria.
  format: http
  id: malacards.search
  name: MalaCards Advanced Search
  product_url: https://www.malacards.org/search/advanced
- category: DocumentationProduct
  description: Access to previous versions of the MalaCards database.
  format: http
  id: malacards.archive
  name: MalaCards Previous Version Archive
  product_url: https://previous.malacards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-17_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-18_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-18: HTTP 403 error
    when accessing file'
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
- category: Product
  description: Disease association data integrated from OMIM, MalaCards, ClinVar,
    Orphanet, DisGeNET and other disease databases
  format: http
  id: genecards.disease.associations
  name: GeneCards Disease Associations
  original_source:
  - omim
  - malacards
  - clinvar
  - orphanet
  - disgenet
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-18_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-17_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-18: HTTP 403 error
    when accessing file'
publications:
- authors:
  - Rappaport N
  - Nativ N
  - Stelzer G
  - Twik M
  - Guan-Golan Y
  - Stein TI
  - Bahir I
  - Belinky F
  - Morrey CP
  - Safran M
  - Lancet D
  id: https://doi.org/10.1093/database/bat018
  journal: Database
  preferred: true
  title: 'MalaCards: an integrated compendium for diseases and their annotation'
  year: '2013'
- authors:
  - Rappaport N
  - Twik M
  - Nativ N
  - Stelzer G
  - Bahir I
  - Stein TI
  - Safran M
  - Lancet D
  id: https://doi.org/10.1002/0471250953.bi0124s47
  journal: Current Protocols in Bioinformatics
  preferred: false
  title: 'MalaCards: A Comprehensive Automatically-Mined Database of Human Diseases'
  year: '2014'
taxon:
- NCBITaxon:9606
---
# MalaCards

MalaCards is a comprehensive, searchable database of human diseases developed by LifeMap Sciences and the Weizmann Institute of Science. It integrates information from 78 trusted data sources to provide comprehensive annotations for over 22,000 human disorders. MalaCards includes data on disease-associated genes, symptoms, drugs, mutations, publications, clinical trials, pathways, and related diseases. The database is organized into global categories (cancer, genetic, rare, infectious, metabolic, and fetal diseases) and anatomical categories (neuronal, cardiovascular, blood, bone, and other organ system diseases). For more information, visit the [MalaCards portal](https://www.malacards.org/).