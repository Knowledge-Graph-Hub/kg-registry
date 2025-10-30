---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://rnacentral.org/contact
    label: RNAcentral Consortium (EMBL-EBI)
creation_date: '2025-07-17T00:00:00Z'
description: RNAcentral is the international non-coding RNA (ncRNA) sequence database that aggregates and harmonizes ncRNA sequences and annotations from expert databases across all domains of life. It provides comprehensive search, browse, programmatic access, and bulk downloads for sequences, secondary structures, and cross-references.
domains:
  - genomics
homepage_url: https://rnacentral.org/
id: rnacentral
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: RNAcentral
products:
  - category: GraphicalInterface
    description: Web portal for searching and browsing ncRNA sequences, structures, and annotations
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
    description: FTP archive with current and archived release files (sequences and annotations)
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
  - description: The MechRepoNet knowledge graph in its original format
    id: mechreponet.kg
    name: MechRepoNet Knowledge Graph
    original_source:
      - ctd
      - doid
      - go
      - chebi
      - reactome
      - interpro
      - hp
      - cl
      - pr
      - uberon
      - ncbitaxon
      - hetionet
      - complexportal
      - rnacentral
      - mirtarbase
      - unii
      - biolink
    product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
    secondary_source:
      - mechreponet
  - category: GraphProduct
    description: RNA-KG as a Neo4j Dump
    format: neo4j
    id: rna-kg.kg.neo4j
    name: RNA-KG Neo4j Dump
    original_source:
      - dbsnp
      - cosmic
      - rnacentral
      - ensembl
      - circbase
      - chebi
      - pr
      - ncbigene
      - cl
      - go
      - mondo
      - hp
      - uberon
      - vo
      - pw
      - reactome
      - wikipathways
    product_file_size: 3976840239
    product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
    secondary_source:
      - rna-kg
  - category: GraphProduct
    description: RNA-KG Nodes in CSV format
    format: csv
    id: rna-kg.kg.nodes
    name: RNA-KG Nodes
    original_source:
      - dbsnp
      - cosmic
      - rnacentral
      - ensembl
      - circbase
      - chebi
      - pr
      - ncbigene
      - cl
      - go
      - mondo
      - hp
      - uberon
      - vo
      - pw
      - reactome
      - wikipathways
    product_file_size: 4424633304
    product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
    secondary_source:
      - rna-kg
  - category: GraphProduct
    description: RNA-KG Edges in CSV format
    format: csv
    id: rna-kg.kg.edges
    name: RNA-KG Edges
    original_source:
      - dbsnp
      - cosmic
      - rnacentral
      - ensembl
      - circbase
      - chebi
      - pr
      - ncbigene
      - cl
      - go
      - mondo
      - hp
      - uberon
      - vo
      - pw
      - reactome
      - wikipathways
    product_file_size: 18370248815
    product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
    secondary_source:
      - rna-kg
infores_id: rnacentral
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
