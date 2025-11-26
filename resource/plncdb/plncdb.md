---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: PLncDB (Plant Long noncoding RNA Database) is a comprehensive encyclopedia
  of plant long noncoding RNAs containing 1,246,372 lncRNAs from 80 plant species,
  ranging from chlorophytes to angiosperms. The database provides uniform lncRNA annotations
  using a standard pipeline across 13,834 RNA-Seq datasets, integrating expression
  patterns across tissues, developmental stages, and stress conditions. It includes
  epigenetic modification data (DNA methylation, histone modifications), predicted
  lncRNA targets (miRNA mimics and RNA-protein interactions), and tools for visualization
  (JBrowse, eFP Browser, EPexplorer). PLncDB also incorporates validated lncRNAs from
  EVLncRNAs and plant lncRNA candidates from RNAcentral.
domains:
- genomics
- biological systems
homepage_url: http://plncdb.tobaccodb.org/
id: plncdb
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: PLncDB
products:
- category: GraphicalInterface
  description: Web interface for browsing, searching, and accessing plant lncRNA data
    with multiple search engines and visualization tools
  format: http
  id: plncdb.portal
  name: PLncDB Web Portal
  original_source:
  - plncdb
  product_url: http://plncdb.tobaccodb.org/
- category: Product
  description: FTP download service providing bulk access to lncRNA sequences, annotations,
    expression data, and epigenetic information
  format: http
  id: plncdb.ftp
  name: PLncDB FTP Download
  original_source:
  - plncdb
  product_url: http://plncdb.tobaccodb.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 403 error
    when accessing file'
- category: GraphicalInterface
  description: JBrowse genome browser for visualizing lncRNA locations, expression
    patterns, and epigenetic modifications
  format: http
  id: plncdb.jbrowse
  name: PLncDB JBrowse
  original_source:
  - plncdb
  product_url: http://plncdb.tobaccodb.org/
- category: GraphicalInterface
  description: EPexplorer tool for batch analysis and visualization of lncRNA expression
    landscapes across tissues
  format: http
  id: plncdb.epexplorer
  name: PLncDB EPexplorer
  original_source:
  - plncdb
  product_url: http://plncdb.tobaccodb.org/
- category: GraphicalInterface
  description: eFP Browser for visualizing tissue-specific expression patterns of
    individual lncRNAs
  format: http
  id: plncdb.efp-browser
  name: PLncDB eFP Browser
  original_source:
  - plncdb
  product_url: http://plncdb.tobaccodb.org/
- category: GraphicalInterface
  description: BLAST search interface for sequence similarity searches against plant
    lncRNA database
  format: http
  id: plncdb.blast
  name: PLncDB BLAST
  original_source:
  - plncdb
  product_url: http://plncdb.tobaccodb.org/
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
  - Jingjing Jin
  - Peng Lu
  - Yalong Xu
  - Zefeng Li
  - Shizhou Yu
  - Jun Liu
  - Huan Wang
  - Nam-Hai Chua
  - Peijian Cao
  doi: 10.1093/nar/gkaa910
  id: doi:10.1093/nar/gkaa910
  journal: Nucleic Acids Research
  preferred: true
  title: 'PLncDB V2.0: a comprehensive encyclopedia of plant long noncoding RNAs'
  year: '2021'
- authors:
  - Jingjing Jin
  - Jun Liu
  - Huan Wang
  - Lance Wong
  - Nam-Hai Chua
  doi: 10.1093/bioinformatics/btt107
  id: doi:10.1093/bioinformatics/btt107
  journal: Bioinformatics
  preferred: false
  title: 'PLncDB: plant long non-coding RNA database'
  year: '2013'
---
# PLncDB

## Overview

PLncDB (Plant Long noncoding RNA Database) is a comprehensive encyclopedia of plant long noncoding RNAs, providing a centralized resource for plant lncRNA research. The database uses uniform annotation standards to systematically catalog lncRNAs across phylogenetically diverse plant species.

## Database Content

Current version (V2.0, released 2020) contains:

- **1,246,372 lncRNAs** annotated across 80 plant species
- Species ranging from **chlorophytes to angiosperms** (16 monocotyledons, 53 eudicotyledons)
- **13,834 RNA-Seq datasets** from diverse tissues, developmental stages, and stress treatments
- **456 epigenetic modification datasets** (H3K27me3, H3K4me3, H3K36me3, H3K9me3)
- Integration of validated lncRNAs from **EVLncRNAs**
- Plant lncRNA candidates from **RNAcentral**

## Annotation Pipeline

PLncDB uses a standardized pipeline for lncRNA identification:

- Transcriptome assembly using StringTie from HISAT2-aligned reads
- Filtering criteria: >200nt length, <120aa ORF
- Coding potential assessment using CPC, PLEK, RNAplonc, and CREMA (candidates must satisfy ≥2 criteria)
- High-confidence lncRNAs satisfy ≥3 criteria
- Removal of transcripts overlapping with rRNA, tRNA, sRNA, and miRNA

## Key Features

### Expression Analysis
- TPM-normalized expression values across all datasets
- Tissue-specific expression identification (ROKU method, cutoff 0.8)
- Expression patterns across different tissues, developmental stages, mutants, and stress treatments

### Target Prediction
- miRNA-mRNA interactions predicted by psRobot
- lncRNA-miRNA mimicry predicted by psMimic
- lncRNA-protein interactions predicted by IntaRNA

### Epigenetic Information
- Histone modification profiles (H3K27me3, H3K4me3, H3K36me3, H3K9me3)
- Expression changes in RdRM-related mutants (RDD, DCL1/2/3/4, AGO4, RDR2, DMS1)

## Visualization Tools

### JBrowse
Genome browser for exploring:
- lncRNA genomic locations
- Expression patterns
- Epigenetic modification signals
- Flanking genomic regions

### eFP Browser
Electronic Fluorescent Pictograph browser for visualizing tissue-specific expression patterns of individual lncRNAs.

### EPexplorer
Expression landscape visualization tool for:
- Batch lncRNA expression analysis
- Identification of tissue-specific candidates
- Heatmap visualization across samples

## Search Capabilities

PLncDB provides five search engines:
1. **Keyword search** - search all database fields
2. **Sequence BLAST** - similarity search against lncRNA sequences
3. **Genome coordinates** - search by genomic location
4. **Expression values** - search by expression level
5. **Tissue-specific search** - find tissue-specific lncRNAs

## Data Access

### Browse
- Hierarchical browsing by species
- Summary information (genome version, lncRNA counts, dataset numbers)
- Detailed lncRNA pages with 6 sections: basic info, sequence, secondary structure, genomic map, regulatory network, expression patterns

### Download
- FTP bulk download of all data
- User-defined download by species and data type
- Quick access for genome coordinates
- Backup copy available on Zenodo (ID: 4017591)
- Download formats: FASTA, CSV, GFF

### Submit
Community submission portal for plant lncRNAs with required information for inclusion in standard annotation pipeline.

## Model Plants Covered

Includes major model species:
- Arabidopsis thaliana
- Oryza sativa (rice)
- Zea mays (maize)
- Glycine max (soybean)
- Solanum lycopersicum (tomato)
- Solanum tuberosum (potato)
- Nicotiana tabacum (tobacco)

## Technical Implementation

Database built using:
- Python programming language
- Vue.js frontend framework
- ElementUI interface components
- Django web framework
- Nginx proxy services
- Echarts for graph visualization
- Cytoscape for network visualization

## Updates

PLncDB is updated semi-annually with:
- Integration of data from other databases
- Community submissions
- New plant species annotations
- Updated RNA-Seq datasets

## Citation

If using PLncDB in your research, please cite:

Jin J, Lu P, Xu Y, Li Z, Yu S, Liu J, Wang H, Chua NH, Cao P. PLncDB V2.0: a comprehensive encyclopedia of plant long noncoding RNAs. *Nucleic Acids Research*, 2021, 49(D1):D1489-D1495. doi:10.1093/nar/gkaa910