---
activity_status: active
category: Aggregator
creation_date: '2025-09-09T00:00:00Z'
description: MGnify is an active aggregator and analysis platform for microbiome and
  metagenomic data, providing tools for submission, analysis, visualization, and discovery
  of microbiome datasets from diverse biomes and environments. It is operated by EMBL-EBI
  and is an ELIXIR Core Data Resource.
domains:
- biological systems
- genomics
- environment
- clinical
id: mgnify
last_modified_date: '2025-10-10T00:00:00Z'
layout: resource_detail
name: MGnify
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and analyzing microbiome and metagenomic
    datasets, including studies, analyses, genomes, and biomes.
  format: http
  id: mgnify.portal
  name: MGnify Web Portal
  product_url: https://www.ebi.ac.uk/metagenomics
- category: ProgrammingInterface
  description: REST API for programmatic access to MGnify data, including studies,
    analyses, genomes, and metadata.
  format: http
  id: mgnify.api
  name: MGnify REST API
  product_url: https://www.ebi.ac.uk/metagenomics/api
- category: Product
  description: FTP archive with current and archived release files, including sequences,
    annotations, and genome catalogues.
  format: http
  id: mgnify.ftp
  name: MGnify FTP Archive
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/metagenomics
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/metagenomics'
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/metagenomics'
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/metagenomics'''
- category: Product
  description: Biome-specific microbial genome catalogues, including marine, human
    gut, and other environments.
  format: http
  id: mgnify.genomes
  name: MGnify Genomes Catalogue
  product_url: https://www.ebi.ac.uk/metagenomics/browse
- category: Product
  description: Protein database derived from metagenomic analyses, including protein
    families and annotations.
  format: http
  id: mgnify.proteins
  name: MGnify Proteins Database
  product_url: https://www.ebi.ac.uk/metagenomics/proteins
- category: DocumentationProduct
  description: Documentation and help resources for MGnify, including user guides
    and API documentation.
  format: http
  id: mgnify.docs
  name: MGnify Documentation
  product_url: https://www.ebi.ac.uk/metagenomics/help
- category: DocumentationProduct
  description: On-demand and live training resources for MGnify users, including webinars
    and tutorials.
  format: http
  id: mgnify.training
  name: MGnify Training
  product_url: https://www.ebi.ac.uk/training/online/courses/mgnify-quick-tour
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
  - Richardson LJ
  - Allen B
  - Baldi G
  - Beracochea M
  - Bileschi M
  - Burdett T
  - Burgin J
  - Caballero-Pérez J
  - Cochrane G
  - Colwell L
  - Curtis T
  - Escobar-Zepeda A
  - Gurbich T
  - Kale V
  - Korobeynikov A
  - Raj S
  - Rogers AB
  - Sakharova E
  - Sanchez S
  - Wilkinson D
  - Finn RD
  id: https://doi.org/10.1093/nar/gkac1080
  journal: Nucleic Acids Research
  preferred: true
  title: 'MGnify: the microbiome sequence data analysis resource in 2023'
  year: '2023'
---
# MGnify

MGnify is an active aggregator and analysis platform for microbiome and metagenomic data, operated by EMBL-EBI. It provides tools for submission, analysis, visualization, and discovery of microbiome datasets from diverse biomes and environments. For more information, visit the [MGnify Web Portal](https://www.ebi.ac.uk/metagenomics) or see the [documentation](https://www.ebi.ac.uk/metagenomics/help).