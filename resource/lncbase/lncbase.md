---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: DIANA-LncBase is a comprehensive repository of experimentally supported miRNA-lncRNA interactions. Version 3.0 contains ~500,000 entries corresponding to ~240,000 unique tissue and cell type specific miRNA-lncRNA pairs in human and mouse. Data derived from manual curation and analysis of >300 high-throughput datasets including AGO-CLIP-Seq, microarrays, and low-yield experiments across 192 cell types and 51 tissues. Includes lncRNA expression profiles and subcellular localization data.
domains:
- genomics
- biological systems
homepage_url: http://www.microrna.gr/LncBase
id: lncbase
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: DIANA-LncBase
synonyms:
- LncBase
- DIANA LncBase
products:
- category: GraphicalInterface
  description: Main web portal for searching experimentally supported miRNA-lncRNA interactions with interactive visualizations
  format: http
  id: lncbase.portal
  name: DIANA-LncBase Portal
  original_source:
  - lncbase
  product_url: http://www.microrna.gr/LncBase
- category: Product
  description: Interactive correlation plots showing clustering of miRNA-lncRNA interactions across cell types and tissues
  format: http
  id: lncbase.correlation-viz
  name: LncBase Correlation Visualizations
  original_source:
  - lncbase
  product_url: http://www.microrna.gr/LncBase
- category: Product
  description: Interactive bar plots showing lncRNA expression profiles and subcellular localization (nucleus/cytoplasm)
  format: http
  id: lncbase.expression-viz
  name: LncBase Expression Visualizations
  original_source:
  - lncbase
  product_url: http://www.microrna.gr/LncBase
- category: Product
  description: UCSC Genome Browser integration for visualizing miRNA binding events and variant locations on lncRNAs
  format: http
  id: lncbase.ucsc-browser
  name: LncBase UCSC Browser Integration
  original_source:
  - lncbase
  product_url: http://www.microrna.gr/LncBase
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
  - Karagkouni D
  - Paraskevopoulou MD
  - Tastsoglou S
  - Skoufos G
  - Karavangeli A
  - Pierros V
  - Zacharopoulou E
  - Hatzigeorgiou AG
  id: https://doi.org/10.1093/nar/gkz1036
  journal: Nucleic Acids Research
  preferred: true
  title: 'DIANA-LncBase v3: indexing experimentally supported miRNA targets on non-coding transcripts'
  year: '2020'
---

# DIANA-LncBase

## Overview

DIANA-LncBase is a reference repository cataloging experimentally supported miRNA-lncRNA interactions. The database serves researchers investigating the complex interplay between microRNAs and long non-coding RNAs, which plays crucial roles in post-transcriptional gene regulation, competing endogenous RNA (ceRNA) networks, and various physiological and pathological processes.

## Database Content

### Interaction Data (v3.0)
- **~500,000 total entries**
- **~240,000 unique miRNA-lncRNA pairs** (tissue and cell type specific)
- **Species**: Human and mouse
- **1,551 miRNAs** targeting lncRNAs
- **24,618 targeted lncRNAs**
- **192 cell types** and **51 tissues**
- **162 experimental conditions**

### Experimental Support
- **14 experimental methodologies**:
  - **Low-yield**: Reporter genes, northern blot, qPCR, RIP-qPCR, biotin miRNA tagging (242 interactions)
  - **High-throughput**: ~239,000 interactions from:
    - **AGO-CLIP-Seq**: 236 libraries analyzed with microCLIP algorithm (~370,000 binding events)
    - **CLEAR-CLIP & chimeric fragments**: 2,924 miRNA-lncRNA chimeras
    - **Microarray perturbation**: 86 experiments analyzed (2,155 interactions)

### Data Sources
- **Manual curation**: 159 publications with 730+ interactions
- **High-throughput analysis**: >300 datasets from GEO, ENCODE, DDBJ
- **236 AGO-CLIP-Seq libraries** (88 PAR-CLIP, 148 HITS-CLIP) analyzed with microCLIP framework

## Key Features

### lncRNA Sequences
- **53,250 lncRNA transcripts**: GENCODE v30, RefSeq 109-106, Cabili et al.
- **27,009 pseudogene transcripts**
- Categories: sense, antisense, lincRNAs, processed transcripts, bidirectional promoter lncRNAs, 3' overlapping ncRNAs, macro lncRNA

### Expression Profiles
- **103 RNA-Seq libraries** analyzed (~19.3 billion reads)
- **48 whole transcriptome datasets** (22 cell types/tissues)
- **55 subcellular localization datasets** (15 cell types/tissues)
- Nucleus vs. cytoplasm expression with Relative Concentration Index (RCI)
- TPM (Transcripts Per Million) values for abundance quantification

### Variant Annotation
- **67,966 MREs** with known short variant information
- **9,940 lncRNA transcripts** with variant-related MREs
- **34,438 unique variants** from:
  - dbSNP (48.6% of variant-MRE pairs)
  - COSMIC (47.5% - somatic mutations)
  - ClinVar (3.9% - clinical variants)

### Advanced Analysis
- **microCLIP algorithm**: CLIP-Seq-guided framework using 131 descriptors including:
  - AGO-CLIP features (substitution ratios, coverage metrics)
  - Binding characteristics (binding type, flanking AU content)
  - Energy-related metrics and sequence-based characteristics
- **~90,000 intronic miRNA binding events** appropriately labeled
- **2,220 viral miRNA binding events** (EBV, KSHV) on host lncRNAs

## Database Interface

### Query Capabilities
- Search by miRNA/gene names or identifiers (ENSEMBL, miRBase, RefSeq, Cabili)
- Genomic location search for MREs on lncRNA transcripts
- Filtering by:
  - Species, cell types, tissues
  - Experimental methodologies
  - Transcript biotype
  - miRNA confidence level (from miRBase)
  - Short variant information

### Interactive Visualizations
- **Correlation plots**: Explore clustering of miRNA-lncRNA interactions across cell types/tissues (Pearson's r coefficient)
- **Expression bar plots**: View lncRNA abundance in different cell types and subcellular compartments
- **UCSC Genome Browser integration**: Visualize miRNA binding events and MRE-overlapping variant locations

### Inter-connections
- **RNAcentral**: Integrated since 2015, interactions viewable per miRNA
- **DIANA-TarBase**: ~1 million experimentally supported miRNA-mRNA pairs
- **DIANA-microT-CDS**: In silico predicted miRNA targets
- **DIANA-miRPath**: miRNA functional analysis

## Methodological Advances (v3.0 vs. v2.0)
- **2-fold increase** in high-throughput datasets (322 vs. 153)
- First database using **microCLIP CLIP-Seq-guided algorithm** for AGO-CLIP-Seq analysis
- **subcellular localization** data in nucleus/cytoplasm
- **Short variant annotation** on miRNA target sites
- Enhanced interface with **advanced filtering** and **interactive visualizations**

## Research Applications
- Study of miRNA-lncRNA regulatory networks
- Investigation of lncRNA sponge functions in ceRNA networks
- Analysis of tissue and cell type specific interactions
- Understanding subcellular localization effects on lncRNA function
- Variant analysis on miRNA-lncRNA binding sites

## Website Updates
The database was completely redesigned using Angular v.8 frontend, Java Spring/.NET Core 2.2 backend, and PostgreSQL with optimized indices for fast query execution.

## Funding
Supported by ELIXIR-GR Infrastructure [MIS-5002780], co-financed by Greece and the European Union (European Regional Development Fund).

## Citation
Karagkouni D, Paraskevopoulou MD, Tastsoglou S, et al. DIANA-LncBase v3: indexing experimentally supported miRNA targets on non-coding transcripts. Nucleic Acids Research. 2020;48(D1):D101-D110. doi:10.1093/nar/gkz1036