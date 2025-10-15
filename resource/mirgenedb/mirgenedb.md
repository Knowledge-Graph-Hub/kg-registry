---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: MirGeneDB is a manually curated database of microRNA genes, providing
  validated and annotated microRNA gene entries for over 21,000 genes from 114 metazoan
  species. It offers uniform nomenclature, evolutionary context, and downloadable
  data for all species and families.
domains:
- genomics
- biological systems
id: mirgenedb
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: MirGeneDB
products:
- category: GraphicalInterface
  description: Web interface for browsing, searching, and exploring curated microRNA
    gene entries and families across 114 metazoan species.
  format: http
  id: mirgenedb.portal
  name: MirGeneDB Web Portal
  product_url: https://mirgenedb.org/
- category: Product
  description: Downloadable FASTA, GFF, BED, and tabular files for microRNA genes
    from individual species.
  format: http
  id: mirgenedb.species_downloads
  name: MirGeneDB Species-Specific Downloads
  product_url: https://mirgenedb.org/download
- category: Product
  description: Downloadable covariance models for more than 700 conserved microRNA
    families.
  format: http
  id: mirgenedb.covariance
  name: MirGeneDB Covariance Models
  product_url: https://mirgenedb.org/covariance
- category: Product
  description: Downloadable processed FASTA files of all read data used in MirGeneDB
    annotations.
  format: fasta
  id: mirgenedb.reads
  name: MirGeneDB Processed Read Data
  product_url: https://mirgenedb.org/download
- category: Product
  description: Bulk download ZIP archives for all microRNA gene data across species.
  format: http
  id: mirgenedb.bulk
  name: MirGeneDB Bulk Data Archive
  product_url: https://mirgenedb.org/download
- category: DocumentationProduct
  description: Documentation and information about MirGeneDB nomenclature, annotation
    standards, and database usage.
  format: http
  id: mirgenedb.info
  name: MirGeneDB Information and Help
  product_url: https://mirgenedb.org/information
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
  - Clarke AW
  - "H\xF8ye E"
  - Hembrom AA
  - Paynter VM
  - Vinther J
  - "Wyro\u017Cemski \u0141"
  - Biryukova I
  - Formaggioni A
  - Ovchinnikov V
  - Herlyn H
  id: https://doi.org/10.1093/nar/gkae1094
  journal: Nucleic Acids Research
  preferred: true
  title: 'MirGeneDB 3.0: improved taxonomic sampling, uniform nomenclature of novel
    conserved microRNA families and updated covariance models'
  year: '2024'
---
# MirGeneDB

MirGeneDB is a manually curated database of microRNA genes, providing validated and annotated entries for over 21,000 genes from 114 metazoan species. The database offers uniform nomenclature, evolutionary context, and downloadable data for all species and families. Users can browse, search, and download microRNA gene data in multiple formats (FASTA, GFF, BED, tabular, ZIP) and access covariance models for conserved families. For more information, visit the [MirGeneDB portal](https://mirgenedb.org/).