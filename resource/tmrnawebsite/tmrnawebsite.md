---
activity_status: inactive
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: The tmRNA Website is a comprehensive database of transfer-messenger RNA
  (tmRNA) and SmpB protein sequences involved in bacterial trans-translation. Contains
  1,716 unique tmRNA sequences from bacteria and organelles, 2,258 unique SmpB sequences,
  with 9,387 tmRNA instances across public databases. Provides sequence alignments,
  structural annotations, BLAST search tools, and Krona-based phylogenetic visualization.
domains:
- genomics
homepage_url: http://bioinformatics.sandia.gov/tmrna/
id: tmrnawebsite
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: The tmRNA Website
products:
- category: GraphicalInterface
  description: Main web portal for searching and browsing tmRNA and SmpB sequences
    with phylogenetic navigation
  format: http
  id: tmrnawebsite.portal
  name: tmRNA Website Portal
  original_source:
  - tmrnawebsite
  product_url: http://bioinformatics.sandia.gov/tmrna/
- category: Product
  description: BLAST search interface for tmRNA and SmpB sequence similarity searches
  format: http
  id: tmrnawebsite.blast
  name: tmRNA Website BLAST
  original_source:
  - tmrnawebsite
  product_url: http://bioinformatics.sandia.gov/tmrna/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 404 error
    when accessing file'
- category: Product
  description: Multiple sequence alignments for 632 tmRNA and 2,258 distinct SmpB
    sequences
  format: http
  id: tmrnawebsite.alignments
  name: tmRNA and SmpB Alignments
  original_source:
  - tmrnawebsite
  product_url: http://bioinformatics.sandia.gov/tmrna/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 404 error
    when accessing file'
- category: Product
  description: Krona-based interactive phylogenetic visualization tool for 9,387 tmRNA
    instances
  format: http
  id: tmrnawebsite.krona-viewer
  name: tmRNA Krona Phylogenetic Viewer
  original_source:
  - tmrnawebsite
  product_url: http://bioinformatics.sandia.gov/tmrna/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 404 error
    when accessing file'
- category: Product
  description: Software tools (tFind.pl, rFind.pl) for identifying tmRNA genes in
    genomic sequences
  format: http
  id: tmrnawebsite.software
  name: tmRNA Identification Software
  original_source:
  - tmrnawebsite
  product_url: http://bioinformatics.sandia.gov/tmrna/software.html
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 404 error
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
publications:
- authors:
  - Hudson CM
  - Williams KP
  id: https://doi.org/10.1093/nar/gku1109
  journal: Nucleic Acids Research
  preferred: true
  title: The tmRNA website
  year: '2015'
synonyms:
- tmRNA website
- tmRNA-SmpB database
warnings:
- Website appears to be inactive (http://bioinformatics.sandia.gov/tmrna/ not accessible
  as of 2025-11-13). Data has been contributed to RNAcentral.
---
# The tmRNA Website

## Overview

The tmRNA Website is a comprehensive resource for transfer-messenger RNA (tmRNA) and its partner protein SmpB, which together resolve problems arising when bacterial ribosomes reach the end of mRNA with no stop codon through a process called trans-translation.

## Database Content

### tmRNA Sequences
- **1,716 unique tmRNA sequences**: 1,454 one-piece and 262 two-piece tmRNAs
- **9,387 instances** across public databases (RefSeq, GenBank, etc.)
- **Phylogenetic breakdown**: 1,594 bacterial, 0 archaeal, 122 organellar (79 oomycete/jakoid mitochondria, 42 algal plastids, 1 chromatophore)
- **734 unique proteolysis tag sequences**

### SmpB Sequences
- **2,258 unique SmpB sequences**
- **4,125 instances** including 24 potentially pseudogenized/frameshifted/truncated sequences
- SmpB proteins linked with their corresponding tmRNA partners

## Trans-Translation Biology

### tmRNA Function
tmRNA uses both tRNA-like and mRNA-like properties during trans-translation:
1. When a ribosome stalls on non-stop mRNA, alanine-charged tmRNA enters as substrate for peptidyl transfer
2. Ribosome switches from defective mRNA to the 'resume codon' of tmRNA
3. Translation continues, adding a peptide tag that signals proteolysis
4. Frees stalled ribosome and marks non-stop mRNA for degradation

### SmpB Role
The protein SmpB is a partner throughout trans-translation, bound to tmRNA and occupying space normally occupied by the anticodon stem-loop.

## Key Features

### Sequence Discovery Pipeline
- **Detection tools**: tRNAscan-SE, BRUCE, ARAGORN, plus custom rFind.pl
- **Processing**: tFind.pl wrapper for comprehensive tmRNA identification
- **Software availability**: Tools freely available for public download

### Annotations
- **tmRNA features**: Length, sequence, genomic location, proteolysis tag, CCA coordinates, introns (when present), two-piece tmRNA structural details
- **SmpB annotations**: Amino acid sequence, genomic coordinates, orientation relative to ssrA gene
- **Secondary structures**: Images provided where available

### Search and Analysis Tools
- **BLAST searches**: Available for both tmRNA and SmpB
- **Sequence alignments**: 632 tmRNA and 2,258 SmpB distinct alignments
- **Krona visualization**: Modified metagenome taxonomy viewer enabling navigation to individual tmRNA pages while displaying phylogenetic distribution

## Data Distribution
- Found in nearly all bacterial genomes (except six recalcitrant genomes)
- Present in some organelles
- SmpB genes found in all bacterial genomes studied (sometimes with severe defects) and in eukaryotic nuclear genomes with signals targeting transport to organelles encoding tmRNA

## Data Sources
- **Primary genomic data**: RefSeq (2,168 organisms plus 1,755 plasmids and 581 viruses)
- **Additional sequence databases**: NCBI est, gss, htgs, nt, other_genomic, patnt, refseq_genome, tsa_nt, wgs
- **Contributions to**: RNAcentral, International Nucleotide Sequence Database Archive (GenBank/ENA/DDBJ) as third-party annotation

## Related Resources
- **tmRDB**: Additional tmRNA database
- **Rfam**: RNA families database including tmRNA
- **RNAcentral**: Central repository receiving tmRNA Website contributions

## Website Status
The tmRNA Website was hosted at Sandia National Laboratories (http://bioinformatics.sandia.gov/tmrna/) but appears to be inactive as of 2025. The database content has been contributed to RNAcentral for continued access.

## Funding
Research fully supported by the Laboratory Directed Research and Development program at Sandia National Laboratories.

## Citation
Hudson CM, Williams KP. The tmRNA website. Nucleic Acids Research. 2015;43(D1):D138-D140. doi:10.1093/nar/gku1109