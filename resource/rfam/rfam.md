---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: rfam-help@ebi.ac.uk
      - contact_type: url
        value: https://docs.rfam.org/en/latest/contact-us.html
    label: Rfam Team at EMBL-EBI
creation_date: '2025-10-29T00:00:00Z'
description: Rfam is a comprehensive database of RNA families, each represented by multiple sequence alignments, consensus secondary structures and covariance models. The database provides curated information for over 4,000 non-coding RNA families and is widely used for RNA annotation, genome analysis, and as training data for machine learning models. Release 15.0 includes expanded coverage with 26,106 genomes, improved 3D structure integration, complete microRNA synchronization with miRBase, enhanced Gene Ontology annotations, and comprehensive viral RNA families.
domains:
  - genomics
  - biological systems
homepage_url: https://rfam.org/
id: rfam
last_modified_date: '2025-10-29T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0 (Creative Commons Zero)
name: Rfam
products:
  - category: GraphicalInterface
    description: Web portal for searching and browsing RNA families
    format: http
    id: rfam.portal
    name: Rfam Web Portal
    product_url: https://rfam.org/
  - category: ProgrammingInterface
    description: REST API for programmatic access to Rfam data
    format: http
    id: rfam.api
    name: Rfam REST API
    product_url: https://rfam.org/api
  - category: Product
    description: FTP archive with covariance models, sequence alignments, and database files
    format: http
    id: rfam.ftp
    name: Rfam FTP Archive
    product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT
  - category: DataModelProduct
    description: Public MySQL database for direct SQL access to Rfam data
    format: mysql
    id: rfam.public-db
    name: Rfam Public MySQL Database
    product_url: https://docs.rfam.org/en/latest/database.html
  - category: Product
    description: Covariance models for all RNA families in CM format
    format: txt
    id: rfam.cm-models
    name: Rfam Covariance Models
    product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/Rfam.cm.gz
  - category: Product
    description: SEED alignments for all RNA families in Stockholm format
    format: stockholm
    id: rfam.seed-alignments
    name: Rfam SEED Alignments
    product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/Rfam.seed.gz
  - category: Product
    description: FULL alignments for all RNA families
    format: txt
    id: rfam.full-alignments
    name: Rfam FULL Alignments
    product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/full_alignments/
  - category: Product
    description: FASTA format sequences for all RNA families
    format: fasta
    id: rfam.fasta
    name: Rfam FASTA Sequences
    product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/
  - category: MappingProduct
    description: PDB structure mappings showing RNA families with 3D structures
    format: txt
    id: rfam.pdb-mappings
    name: Rfam PDB Mappings
    product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/.preview/pdb_full_region.txt.gz
  - category: DocumentationProduct
    description: Comprehensive documentation for Rfam database and tools
    format: http
    id: rfam.docs
    name: Rfam Documentation
    product_url: https://docs.rfam.org/
publications:
  - authors:
      - Ontiveros-Palacios N
      - Cooke E
      - Nawrocki EP
      - Triebel S
      - Marz M
      - Rivas E
      - Griffiths-Jones S
      - Petrov AI
      - Bateman A
      - Sweeney B
    category: Publication
    id: https://doi.org/10.1093/nar/gkae1023
    journal: Nucleic Acids Research
    preferred: true
    title: 'Rfam 15: RNA families database in 2025'
    year: '2024'
  - authors:
      - Kalvari I
      - Nawrocki EP
      - Ontiveros-Palacios N
      - Argasinska J
      - Lamkiewicz K
      - Marz M
      - Griffiths-Jones S
      - Toffano-Nioche C
      - Gautheret D
      - Weinberg Z
      - Rivas E
      - Eddy SR
      - Finn RD
      - Bateman A
      - Petrov AI
    category: Publication
    id: https://doi.org/10.1093/nar/gkaa1047
    journal: Nucleic Acids Research
    preferred: false
    title: 'Rfam 14: expanded coverage of metagenomic, viral and microRNA families'
    year: '2021'
---

# Rfam

## Overview

Rfam (RNA families) is a comprehensive database and collection of non-coding RNA families, each represented by multiple sequence alignments, consensus secondary structures, and covariance models (CMs). Established in 2002, Rfam has become an authoritative resource for RNA research, genome annotation, and computational biology, providing curated information for over 4,000 RNA families.

## Mission and Scope

Rfam's primary mission is to provide a centralized repository of non-coding RNA families that enables accurate genome annotation and supports RNA research worldwide. The database serves multiple communities, from experimental biologists seeking functional information about ncRNAs to computational researchers training machine learning models for RNA structure prediction, including tools like AlphaFold 3.

## Database Content

### Release 15.0 (September 2024)

The current release includes:
- **4,178 RNA families**: Comprehensive coverage across all domains of life
- **26,106 genomes in Rfamseq**: 76% increase from previous release, including 23,158 UniProt reference proteomes and 2,985 viral genomes
- **1,603 microRNA families**: Complete synchronization with miRBase
- **10,736,534 Rfam hits**: Matches across the entire Rfamseq database
- **143 families with 3D structures**: Including 65 families improved using experimentally determined structures

### Key Components

Each RNA family in Rfam consists of three essential elements:

1. **SEED Alignment**: Curated multiple sequence alignment of homologous RNA sequences with consensus secondary structure annotation
2. **Covariance Model**: Statistical profile built using Infernal software, trained on the SEED alignment for homology searches
3. **FULL Hits**: Complete set of sequences matching the family's covariance model above the gathering threshold

## Major Features and Improvements

### 3D Structure Integration

Rfam has implemented an automated pipeline that:
- Maps RNA 3D structures from PDB to SEED alignments weekly using Infernal
- Integrates base-pairing information from FR3D analysis
- Updates consensus secondary structures to include pseudoknots and additional structural features
- Has improved 65 families with 298 chains from 3D structures, including 42 families with pseudoknots

### R-scape Analysis

Using R-scape covariation analysis, Rfam has:
- Systematically reviewed all families for structural improvements
- Updated 26 families using R-scape CaCoFold structures
- Enhanced consensus secondary structures with statistically significant covarying base pairs

### Gene Ontology and Sequence Ontology Annotations

Rfam provides structured functional annotations:
- **75% of families** now have Gene Ontology (GO) term coverage (increased from 60%)
- **4,446 GO terms** across all families (increased from 3,752)
- Updated Sequence Ontology (SO) terms to reflect latest ontology changes
- Ensures all families have at least one up-to-date SO term

### Viral RNA Families

Collaboration with the Marz group has produced:
- 14 new Hepatitis C Virus (HCV) families
- Comprehensive Flaviviridae and Coronaviridae families
- Families built from whole genome alignments
- Dedicated viral families landing page at https://rfam.org/viruses

### MicroRNA Synchronization

Complete synchronization with miRBase includes:
- 1,603 microRNA families aligned with miRBase sequences
- RNAcentral Unique RNA Sequence identifiers for each sequence
- Manually curated gathering thresholds for accurate genome annotation
- 722 new families, 881 updated families since last major publication

## Data Organization and Access

### Search and Browse

Rfam offers multiple ways to explore the database:
- **Text search**: Search by family name, RNA type, organism, author
- **Sequence search**: Annotate sequences using Infernal and visualize with R2DT
- **Genome search**: Browse families by taxonomic distribution
- **3D structure search**: Find families with experimentally determined structures

### Download Options

All data available through:
- **FTP Archive**: Complete database dumps, CM files, alignments, FASTA sequences
- **Public MySQL Database**: Direct SQL access to all Rfam data
- **REST API**: Programmatic access with comprehensive documentation
- **GitHub**: All code under Apache 2.0 license

### Rfamseq Database

The sequence database underlying Rfam includes:
- **26,106 species**: Representing phylogenetic diversity across all domains
  - 2,613 eukaryotes
  - 370 archaea
  - 9,601 bacteria
  - 13,552 viruses
- **1.46 × 10¹² nucleotides**: Total sequence length
- **772 GB**: Uncompressed size on disk

## Technical Infrastructure

### Tools and Software

- **Infernal**: For building covariance models and searching sequences (100-fold faster in version 1.1)
- **R-scape**: For covariation analysis and structure prediction
- **R2DT**: For RNA 2D structure visualization
- **FR3D**: For analyzing RNA 3D structural motifs

### Integration with Other Resources

Rfam integrates with:
- **RNAcentral**: As a member database providing RNA family annotations
- **Ensembl**: For genome annotation with Rfam families
- **miRBase**: Complete synchronization of microRNA families
- **PDB**: Weekly mapping of 3D structures to families
- **UniProt**: Reference proteomes as basis for Rfamseq
- **APICURON**: For curator attribution and activity tracking

## Applications and Impact

### Genome Annotation

Rfam is extensively used for:
- Automatic annotation of ncRNAs in genomic resources like Ensembl
- Identification of functional RNA elements in newly sequenced genomes
- Transfer of annotations between model organisms and other species

### Machine Learning and AI

Rfam serves as:
- Training dataset for RNA structure prediction tools (AlphaFold 3, RNAfold)
- Source data for large language models (ChatGPT, Claude)
- Benchmark for evaluating new RNA analysis methods

### Functional Research

Researchers use Rfam for:
- Understanding RNA regulatory mechanisms (riboswitches, ribozymes)
- Studying RNA evolution and phylogenetic relationships
- Identifying disease-associated microRNAs and other ncRNAs
- Discovering novel RNA families and motifs

### Annotation Statistics

Rfam provides:
- Over 10 million sequences with Rfam-based GO annotations
- Largest source of GO annotations for functional information
- Comprehensive taxonomic coverage across all domains of life

## Website Features

### Enhanced User Experience

Recent improvements include:
- **Project landing pages**: Dedicated pages for 3D structures, viruses, microRNAs
- **LitScan widget**: Integration showing open access literature mentioning each family
- **Riboswitch clarifications**: Clear descriptions indicating aptamer domains
- **Improved navigation**: Easy access to family-specific information

### Documentation

Comprehensive help available at https://docs.rfam.org/ including:
- Getting started guides
- API documentation
- Genome annotation tutorials
- Database schema information
- Contact information and support

## Quality and Curation

### Curation Process

Each family undergoes:
- Manual review by expert curators
- Validation using covariance models
- Threshold optimization for accurate genome annotation
- Regular updates with new sequences and structures
- Integration of community submissions

### Data Quality

Rfam ensures:
- All SEED sequences traceable to public databases (GenBank, RNAcentral)
- Consensus structures validated against experimental data where available
- GO and SO annotations kept up-to-date with ontology changes
- Regular rescanning against updated Rfamseq database

## Community and Collaboration

### Curator Attribution

Through APICURON integration:
- Individual curator contributions tracked and credited
- ORCID records updated for curator activities
- Public recognition of biocuration work

### Community Contributions

Rfam actively encourages:
- Submission of new RNA family alignments
- Reporting of families needing updates
- Sharing of experimental data and structures
- Feedback on families and annotations

## Funding and Support

Rfam is supported by:
- Wellcome Trust [218302/Z/19/Z]
- Biotechnology and Biological Sciences Research Council [BB/S020462/1]
- NIH Intramural Research Program
- ELIXIR infrastructure
- EMBL-EBI Core Funds

## Future Directions

Planned developments include:
- **Pfam-B equivalent**: Automatic generation of candidate families
- **Comprehensive genome annotation pipeline**: Including pseudo-gene detection
- **Expanded Rfamseq**: Better phylogenetic coverage
- **Continued 3D integration**: Connecting all families with available structures
- **Faster curation**: Supporting RNA structure prediction advances

## Historical Impact

Since establishment in 2002, Rfam has:
- Grown to over 4,000 families
- Received 3,162,948+ visits to the website
- Published regular updates in leading journals
- Supported countless research projects worldwide
- Celebrated 20 years of open access in 2022

## Citation

When using Rfam, please cite:

Ontiveros-Palacios N, Cooke E, Nawrocki EP, et al. Rfam 15: RNA families database in 2025. Nucleic Acids Research. 2024;53(D1):D258-D267. doi:10.1093/nar/gkae1023

## Additional Resources

- **Rfam Blog**: https://xfam.wordpress.com/tag/rfam/
- **GitHub**: https://github.com/Rfam
- **Twitter**: @RfamDB
- **APICURON page**: https://apicuron.org/databases/rfam
- **20th Anniversary**: https://rfam.org/rfam20
