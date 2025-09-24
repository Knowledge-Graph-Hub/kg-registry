---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: damcdonald@ucsd.edu
  label: Daniel McDonald
- category: Organization
  contact_details:
  - contact_type: url
    value: https://greengenes2.ucsd.edu/
  label: University of California San Diego
creation_date: '2025-09-09T00:00:00Z'
description: Greengenes2 is a comprehensive reference database and phylogenetic tree
  for 16S rRNA gene sequences that unifies microbial data from multiple sources into
  a single coherent framework. It provides standardized taxonomic assignments and
  phylogenetic placement for microbiome research and enables consistent analysis across
  different studies and sequencing platforms.
domains:
- biomedical
- microbiome
- microbiology
- organisms
homepage_url: https://greengenes2.ucsd.edu/
id: greengenes
last_modified_date: '2025-09-24T00:00:00Z'
layout: resource_detail
name: Greengenes2
products:
- category: GraphicalInterface
  description: Web-based search interface for querying Greengenes2 database by species,
    ASV sequences, or clade names
  format: http
  id: greengenes.portal
  name: Greengenes2 Web Portal
  product_url: https://greengenes2.ucsd.edu/
- category: Product
  description: FTP archive containing Greengenes2 database files including phylogenetic
    trees, taxonomy, and sequence data
  format: http
  id: greengenes.ftp
  name: Greengenes2 FTP Archive
  product_url: http://ftp.microbio.me/greengenes_release/current/
- category: Product
  description: Reference phylogenetic tree in Newick format containing unified microbial
    phylogeny
  format: txt
  id: greengenes.phylogeny
  name: Greengenes2 Phylogenetic Tree
  product_url: http://ftp.microbio.me/greengenes_release/current/
- category: Product
  description: 16S rRNA gene sequences in FASTA format for all organisms in the database
  format: fasta
  id: greengenes.sequences
  name: Greengenes2 Sequences
  product_url: http://ftp.microbio.me/greengenes_release/current/
- category: Product
  description: Taxonomic assignments and metadata for all sequences in the database
  format: tsv
  id: greengenes.taxonomy
  name: Greengenes2 Taxonomy
  product_url: http://ftp.microbio.me/greengenes_release/current/
- category: ProcessProduct
  description: QIIME 2 plugin for integrating Greengenes2 data into microbiome analysis
    workflows
  format: python
  id: greengenes.qiime2-plugin
  name: q2-greengenes2 Plugin
  product_url: https://github.com/biocore/q2-greengenes2/
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
  - McDonald D
  - Jiang Y
  - Balaban M
  - Cantrell K
  - Zhu Q
  - Gonzalez A
  - Morton JT
  - Nicolaou G
  - Parks DH
  - Karst SM
  - Albertsen M
  - Hugenholtz P
  - Keller A
  - Knight R
  id: doi:10.1038/s41587-023-01845-1
  journal: Nature Biotechnology
  preferred: true
  title: Greengenes2 unifies microbial data in a single reference tree
  year: '2024'
repository: https://github.com/biocore/greengenes2/
---
# Greengenes2

Greengenes2 is a comprehensive reference database and phylogenetic framework for 16S rRNA gene sequences that addresses the fragmentation problem in microbial data analysis. By unifying sequences from multiple databases into a single coherent phylogenetic tree, Greengenes2 enables consistent taxonomic assignments and comparative analyses across different microbiome studies and sequencing platforms.

## Key Features

### Unified Phylogenetic Framework
- Single reference tree containing over 33 million 16S rRNA sequences
- Consistent phylogenetic placement for all sequences in the database
- Integration of data from multiple sources including SILVA, RDP, and NCBI
- Standardized taxonomy based on phylogenetic relationships

### Comprehensive Sequence Coverage
- Amplicon sequence variants (ASVs) from diverse environmental samples
- Full-length and partial 16S rRNA gene sequences
- Sequences from both cultured and uncultured microorganisms
- Regular updates incorporating new sequence data from public repositories

### Advanced Search and Query Capabilities
- Search by species name, genus, or higher taxonomic levels
- Query by ASV sequence or MD5 hash identifier
- Clade-based searches for phylogenetic groups
- Integration with QIIME 2 for streamlined analysis workflows

## Data Structure

### Phylogenetic Tree
- Newick format tree files with branch lengths and support values
- Multiple tree representations (full, backbone, and region-specific)
- Bootstrap support values for assessing phylogenetic confidence
- Time-calibrated molecular clock estimates where applicable

### Taxonomic Assignments
- Seven-level taxonomic hierarchy (Kingdom to Species)
- Confidence scores for taxonomic assignments
- Consistent naming conventions across all entries
- Cross-references to external taxonomic databases

### Sequence Data
- FASTA format files for all 16S rRNA sequences
- Quality-filtered sequences with length and ambiguity criteria
- Metadata including source database, collection information, and quality metrics
- MD5 hash identifiers for unique sequence identification

### Metadata Integration
- Environmental context information where available
- Host organism data for host-associated microbes
- Geographic origin and sampling metadata
- Publication and study references for sequence sources

## Applications

### Microbiome Analysis
- Taxonomic profiling of amplicon sequencing data
- Phylogenetic diversity calculations and community comparisons
- Identification of novel or rare microbial taxa
- Cross-study meta-analyses with consistent taxonomic framework

### Comparative Genomics
- Phylogenetic placement of newly sequenced organisms
- Evolutionary analysis of microbial communities
- Assessment of phylogenetic signal in functional traits
- Integration with whole-genome phylogenies

### Environmental Microbiology
- Biodiversity assessments across different ecosystems
- Tracking of microbial populations over time and space
- Identification of indicator species for environmental conditions
- Assessment of microbial community assembly processes

### Clinical and Applied Microbiology
- Pathogen identification and phylogenetic typing
- Microbiome-based diagnostic applications
- Probiotic strain identification and quality control
- Food safety and industrial microbiology applications

## Data Access and Integration

### Web Interface
- User-friendly search portal with autocomplete functionality
- Interactive phylogenetic tree visualization
- Sequence alignment and comparison tools
- Export capabilities for analysis results

### Programmatic Access
- Direct FTP download of database files
- QIIME 2 plugin for seamless workflow integration
- Command-line tools for batch processing
- API endpoints for automated data retrieval

### File Formats and Standards
- Standard bioinformatics formats (FASTA, Newick, TSV)
- QIIME 2 artifact formats (.qza) for reproducible analysis
- Compressed archives for efficient data transfer
- Detailed documentation and metadata schemas

### Quality Assurance
- Rigorous sequence quality filtering and validation
- Phylogenetic consistency checking across updates
- Cross-validation with established taxonomic databases
- Community feedback mechanisms for error reporting

## Technical Implementation
Greengenes2 is built using scalable phylogenetic inference methods that can accommodate the massive scale of modern sequence databases. The unified tree construction process involves careful alignment, phylogenetic placement algorithms, and iterative refinement to ensure consistency and accuracy across the entire phylogenetic framework.