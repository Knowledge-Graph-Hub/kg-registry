---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://lncipedia.org/
    label: LncIPedia Team
creation_date: '2025-10-30T00:00:00Z'
description: LncIPedia is a comprehensive public database for human long non-coding RNA (lncRNA) sequences and annotations, containing manually curated literature and detailed transcript information.
domains:
  - genomics
  - literature
homepage_url: https://lncipedia.org/
id: lncipedia
last_modified_date: '2026-04-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.lncipedia.org/download
  label: Non-Commercial Use Only
name: LncIPedia
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing human lncRNA sequences and annotations
    format: http
    id: lncipedia.search
    name: LncIPedia Search
    original_source:
      - source: lncipedia
        relation_type: prov:hadPrimarySource
    product_url: https://lncipedia.org/db/search
  - category: Product
    description: Downloadable database files in FASTA, GFF, and BED formats for both GRCh37/hg19 and GRCh38/hg38 genome assemblies
    format: fasta
    id: lncipedia.downloads
    name: LncIPedia Downloads
    product_url: https://lncipedia.org/download
    original_source:
      - source: lncipedia
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: UCSC Genome Browser trackhub for directly displaying LncIPedia annotations
    id: lncipedia.trackhub
    name: LncIPedia UCSC Trackhub
    original_source:
      - source: lncipedia
        relation_type: prov:hadPrimarySource
    product_url: https://www.lncipedia.org/trackhub/hub.txt
  - category: Product
    description: Integration files for Integrative Genomics Viewer (IGV) to visualize lncRNA annotations
    format: http
    id: lncipedia.igv
    name: LncIPedia IGV Integration
    original_source:
      - source: lncipedia
        relation_type: prov:hadPrimarySource
    product_url: https://lncipedia.org/download#anchor-igv
  - category: Product
    description: Metadata files including locus conservation across species (chimpanzee, mouse, Drosophila, zebrafish) and conversion tables to Ensembl and RefSeq IDs
    format: tsv
    id: lncipedia.metadata
    name: LncIPedia Metadata
    product_url: https://lncipedia.org/download#anchor-metadata
    original_source:
      - source: lncipedia
        relation_type: prov:hadPrimarySource
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
publications:
  - category: Publication
    id: PMID:30371849
    preferred: true
  - category: Publication
    id: PMID:25378313
  - category: Publication
    id: PMID:23042674
taxon:
  - NCBITaxon:9606
warnings:
  - LncIPedia download files are for non-commercial use only. Any other use should be approved in writing from Ghent University.
---

# LncIPedia

## Overview

LncIPedia is a comprehensive public database for human long non-coding RNA (lncRNA) sequences and annotations. The database integrates lncRNA transcript data from multiple sources and provides manually curated literature associations, making it a valuable reference resource for lncRNA research.

## Data Content

Current release (version 5.2, August 2018) contains:

- **127,802 transcripts** (107,039 in high-confidence set)
- **56,946 genes** (49,372 in high-confidence set)
- **2,482 manually curated lncRNA articles** with gene-specific annotations

The database provides:
- Complete sequence information in FASTA format
- Genomic annotations in GFF and BED formats
- Both full database and high-confidence subset (excluding putative protein-coding genes)
- Coverage for GRCh37/hg19 and GRCh38/hg38 genome assemblies

## Key Features

- **Comprehensive Coverage**: Aggregates lncRNA data from multiple sources into a unified resource
- **Literature Curation**: Manual curation of publications describing lncRNA function and biology
- **Cross-species Conservation**: Locus conservation data for chimpanzee, mouse, Drosophila, and zebrafish
- **Database Cross-references**: Conversion tables to Ensembl and RefSeq identifiers
- **Version Tracking**: Conversion tables between LncIPedia versions for maintaining consistent identifiers

## Access Methods

- **Web Search Interface**: Interactive search and browse functionality
- **Bulk Downloads**: Complete database exports in multiple formats (FASTA, GFF, BED)
- **Custom Exports**: User-defined data subsets via the search interface
- **Genome Browser Integration**: UCSC Genome Browser trackhub and IGV visualization support
- **FTP Archive**: Historical versions available for reproducible research

## Visualization Tools

- **UCSC Genome Browser Trackhub**: Direct integration for viewing lncRNA annotations in genome context
- **IGV Integration**: Pre-configured files for the Integrative Genomics Viewer
- **BED Format Files**: Compatible with standard genome visualization tools

## Use Cases

- Identifying and characterizing novel lncRNAs
- Literature mining for lncRNA functional information
- Comparative genomics of lncRNA loci across species
- Integrating lncRNA annotations into genomic analyses
- Training datasets for lncRNA prediction and classification methods
- Reference annotations for transcriptome studies

## Data Organization

- **Full Database**: Complete set of all lncRNA transcripts
- **High Confidence Set**: Curated subset excluding putative protein-coding genes
- **Metadata Files**: Conservation data and identifier mappings
- **Multiple Genome Builds**: Parallel annotations for hg19 and hg38

## Management

LncIPedia is developed and maintained by researchers at:
- Ghent University
- VIB (Vlaams Instituut voor Biotechnologie / Flanders Institute for Biotechnology)

## Licensing

LncIPedia download files are for non-commercial use only. Commercial use requires written approval from Ghent University.

## Citation

If using LncIPedia, cite: Volders PJ, Anckaert J, Verheggen K, Nuytens J, Martens L, Mestdagh P, Vandesompele J. "LncIPedia 5: towards a reference set of human long non-coding RNAs." Nucleic Acids Research. 2019. PMID:30371849
