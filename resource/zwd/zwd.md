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
description: The Zasha Weinberg Data repository is a collection of RNA sequence and structure data, including information about regulatory RNA elements, riboswitches, and non-coding RNAs. This data source contributes to the RNAcentral aggregator and focuses on structured RNA data from computational and comparative genomics analyses.
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
    description: Web portal for searching and browsing ncRNA sequences, structures, and annotations
    format: http
    id: rnacentral.portal
    name: RNAcentral Portal
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/
  - category: ProgrammingInterface
    description: REST API for programmatic access to RNAcentral data
    format: http
    id: rnacentral.api
    name: RNAcentral REST API
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/api
  - category: Product
    description: FTP archive with current and archived release files (sequences and annotations)
    format: http
    id: rnacentral.ftp
    name: RNAcentral FTP Archive
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
  - category: DataModelProduct
    description: Public PostgreSQL database for direct SQL access to RNAcentral data
    format: postgres
    id: rnacentral.public-db
    name: RNAcentral Public Postgres Database
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
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
