---
activity_status: active
category: Aggregator
creation_date: '2025-07-17T00:00:00Z'
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://rnacentral.org/contact"
    label: RNAcentral Consortium (EMBL-EBI)
description: RNAcentral is the international non-coding RNA (ncRNA) sequence database that aggregates and harmonizes ncRNA sequences and annotations from expert databases across all domains of life. It provides comprehensive search, browse, programmatic access, and bulk downloads for sequences, secondary structures, and cross-references.
domains:
  - genomics
homepage_url: https://rnacentral.org/
id: "rnacentral"
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/publicdomain/zero/1.0/"
  label: CC0 1.0
name: RNAcentral
products:
  - category: GraphicalInterface
    description: Web portal for searching and browsing ncRNA sequences, structures, and annotations
    format: http
    id: "rnacentral.portal"
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
    id: "rnacentral.api"
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
    description: FTP archive with current and archived release files (sequences and annotations)
    format: http
    id: "rnacentral.ftp"
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
    id: "rnacentral.public-db"
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

# RNAcentral

## Overview

RNAcentral is a comprehensive repository of non-coding RNA sequences and related annotations aggregated from dozens of expert databases. It supports search, sequence similarity, genome browsing, secondary structure visualisation, and programmatic/API access.

## Access

- Portal: search, browse, and visual tools at the main website
- Downloads: bulk files via the FTP archive (current and archived releases)
- API: web-browsable REST API for programmatic queries
- Public DB: access via a public PostgreSQL database for advanced querying

## Citation

Please cite the latest RNAcentral publication and acknowledge specific expert databases where appropriate.
