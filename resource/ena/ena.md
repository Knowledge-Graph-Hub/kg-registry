---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: The European Nucleotide Archive (ENA) is a comprehensive database providing
  free and open access to nucleotide sequence data, functional genomics data, and
  associated metadata. It is operated by EMBL-EBI and serves as an ELIXIR Core Data
  Resource and a Global Core Biodata Resource.
domains:
- genomics
- biological systems
id: ena
last_modified_date: '2025-10-10T00:00:00Z'
layout: resource_detail
name: European Nucleotide Archive (ENA)
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and viewing nucleotide sequence
    data and metadata.
  format: http
  id: ena.browser
  name: ENA Browser
  product_url: https://www.ebi.ac.uk/ena/browser/home
- category: ProgrammingInterface
  description: REST API for programmatic access to ENA data, including sequence retrieval
    and metadata queries.
  format: http
  id: ena.api
  name: ENA REST API
  product_url: https://www.ebi.ac.uk/ena/browser/api
- category: Product
  description: FTP archive with nucleotide sequences, assemblies, and associated data
    files.
  format: http
  id: ena.ftp
  name: ENA FTP Archive
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/ena
  warnings:
  - File was not able to be retrieved when checked on 2025-11-04_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/ena'
  - File was not able to be retrieved when checked on 2025-11-05_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/ena'
  - 'File was not able to be retrieved when checked on 2025-11-06: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/ena'''
- category: GraphicalInterface
  description: Interface for setting up and managing pre-release and public Data Hubs
    for pathogen and other sequence data.
  format: http
  id: ena.datahubs
  name: ENA Data Hubs Portal
  product_url: https://www.ebi.ac.uk/ena/browser/data-hubs
- category: DocumentationProduct
  description: Documentation and help resources for ENA, including submission guidelines
    and API documentation.
  format: http
  id: ena.docs
  name: ENA Documentation
  product_url: https://www.ebi.ac.uk/ena/browser/support
- category: DocumentationProduct
  description: Training resources for ENA users, including tutorials and webinars.
  format: http
  id: ena.training
  name: ENA Training
  product_url: https://www.ebi.ac.uk/training/services/ena
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
---
# European Nucleotide Archive (ENA)

The European Nucleotide Archive (ENA) is a comprehensive database providing free and open access to nucleotide sequence data, functional genomics data, and associated metadata. It is operated by EMBL-EBI and serves as an ELIXIR Core Data Resource and a Global Core Biodata Resource. For more information, visit the [ENA Browser](https://www.ebi.ac.uk/ena/browser/home) or see the [documentation](https://www.ebi.ac.uk/ena/browser/support).