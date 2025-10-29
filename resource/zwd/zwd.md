---
activity_status: active
category: DataSource
creation_date: '2025-10-29T00:00:00Z'
curators:
- category: Individual
  contact_details:
  - contact_type: url
    value: https://bitbucket.org/zashaw/
  label: Zasha Weinberg
description: The Zasha Weinberg Data repository is a collection of RNA sequence and
  structure data, including information about regulatory RNA elements, riboswitches,
  and non-coding RNAs. This data source contributes to the RNAcentral aggregator and
  focuses on structured RNA data from computational and comparative genomics analyses.
domains:
- genomics
- biological systems
homepage_url: https://bitbucket.org/zashaw/zashaweinbergdata/src/master/
id: zwd
last_modified_date: '2025-10-29T00:00:00Z'
layout: resource_detail
name: Zasha Weinberg Data
products:
- category: Product
  description: Multiple sequence alignments for RNA and ssDNA sequences
  format: http
  id: zwd.alignments
  name: Zasha Weinberg Data Repository Sequence Alignments
  product_url: https://bitbucket.org/zashaw/zashaweinbergdata/src/master/
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
# Zasha Weinberg Data

## Overview

The Zasha Weinberg Data (ZWD) repository is a collection of RNA sequence and structure data maintained by Zasha Weinberg. This data source provides curated information about RNA elements, particularly focusing on regulatory RNAs, riboswitches, and other structured non-coding RNA elements. The data is hosted on Bitbucket and contributes to the comprehensive RNAcentral non-coding RNA sequence database.

## Scope and Content

The repository contains RNA-related data derived from computational and comparative genomics analyses. As a contributor to RNAcentral, ZWD provides specialized RNA sequence and annotation data that complements other expert databases in the RNAcentral consortium. The focus is on structured RNA elements identified through computational methods and comparative sequence analysis.

## Data Organization

The data is organized in the Bitbucket repository at https://bitbucket.org/zashaw/zashaweinbergdata/ and is structured to support computational analysis of RNA sequences and structures. The repository serves as both a standalone resource and a data source for the broader RNAcentral aggregator.

## Integration with RNAcentral

ZWD data is integrated into RNAcentral, the international non-coding RNA sequence database. Through this integration, ZWD sequences and annotations become searchable and accessible via RNAcentral's web portal, REST API, FTP archive, and public PostgreSQL database. This ensures broad accessibility and interoperability with other RNA databases.

## Access and Availability

The primary access point for ZWD data is through the Bitbucket repository. Additionally, ZWD contributions can be accessed through RNAcentral's various interfaces, providing multiple pathways for researchers to utilize this data in their work.

## Research Applications

The data is particularly relevant for researchers studying:
- RNA structure and function
- Regulatory RNA elements
- Riboswitch mechanisms
- Comparative genomics of RNA
- Non-coding RNA identification and characterization

## Citation

When using data from this repository, please cite the Bitbucket repository and acknowledge the contribution to RNAcentral where applicable.