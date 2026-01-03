---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: TarBase v9.0 is a comprehensive database of experimentally supported
  miRNA targets on protein-coding transcripts. It contains interactions identified
  via high-throughput methods (HITS-CLIP, PAR-CLIP, CLASH) and low-throughput experimental
  validation, all uniformly analyzed and manually curated with rich metadata.
domains:
- genomics
- biological systems
homepage_url: https://dianalab.e-ce.uth.gr/tarbasev9
id: tarbase
last_modified_date: '2025-10-27T00:00:00Z'
layout: resource_detail
name: TarBase
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing experimentally supported miRNA-gene
    interactions
  format: http
  id: tarbase.portal
  name: TarBase Portal
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9
- category: GraphicalInterface
  description: Interactive search interface for querying miRNA targets and gene miRNomes
    with advanced filtering options
  format: http
  id: tarbase.interactions
  name: Interactions Search
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/interactions
- category: GraphicalInterface
  description: Network visualization tool for assessing combinatorial effects of multiple
    miRNAs on common gene targets
  format: http
  id: tarbase.visualizations
  name: Visualizations
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/visualizations
- category: GraphicalInterface
  description: Statistics page showing database content and coverage metrics
  format: http
  id: tarbase.statistics
  name: Statistics
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/statistics
- category: GraphicalInterface
  description: Text-mining interface for literature-based interaction discovery
  format: http
  id: tarbase.textmining
  name: Text-Mining Interface
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/textmining
- category: Product
  compression: gzip
  description: Experimentally validated miRNA-gene interactions for Homo sapiens in
    tab-delimited format
  format: tsv
  id: tarbase.homo-sapiens
  name: Homo sapiens Interactions
  product_file_size: 111135987
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Homo_sapiens_TarBase-v9.tsv.gz
- category: Product
  compression: gzip
  description: Experimentally validated miRNA-gene interactions for Mus musculus in
    tab-delimited format
  format: tsv
  id: tarbase.mus-musculus
  name: Mus musculus Interactions
  product_file_size: 16498710
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Mus_musculus_TarBase-v9.tsv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-27_ Timeout connecting
    to URL
- category: Product
  compression: gzip
  description: Experimentally validated viral miRNA-gene interactions in tab-delimited
    format
  format: tsv
  id: tarbase.viral
  name: Viral Species Interactions
  product_file_size: 884524
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Viral_species_TarBase-v9.tsv.gz
- category: Product
  compression: gzip
  description: Experimentally validated miRNA-gene interactions for other species
    in tab-delimited format
  format: tsv
  id: tarbase.other-species
  name: Other Species Interactions
  product_file_size: 164821
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Other_species_TarBase-v9.tsv.gz
- category: DocumentationProduct
  description: Comprehensive help documentation with query examples and filtering
    options
  format: http
  id: tarbase.help
  name: Help Documentation
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/help
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-15_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-03_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: HTTP 404 error
    when accessing file'
- category: DocumentationProduct
  description: Downloads page with file format specifications and field descriptions
  format: http
  id: tarbase.downloads-doc
  name: Downloads Documentation
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/downloads
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-02_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: HTTP 404 error
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
  - Skoufos
  - Kakoulidis
  - Tastsoglou
  - Zacharopoulou
  - Kotsira
  - Miliotis
  - Mavromati
  - Grigoriadis
  - Zioga
  - Velli
  - Koutou
  - Karagkouni
  - Stavropoulos
  - Kardaras
  - Lifousi
  - Vavalou
  - Ovsepian
  - Skoulakis
  - Tasoulis
  - Georgakopoulos
  - Plagianakos
  - Hatzigeorgiou
  id: https://doi.org/10.1093/nar/gkad1071
  journal: Nucleic Acids Research
  preferred: true
  title: TarBase-v9.0 extends experimentally supported miRNA–gene interactions to
    cell-types and virally encoded miRNAs
  year: '2023'
---
# TarBase

TarBase v9.0 is the reference database of experimentally supported microRNA (miRNA) targets on protein-coding transcripts. Developed and maintained by the DIANA Lab at the University of Thessaly, TarBase provides researchers with a comprehensive, curated collection of validated miRNA-gene interactions.

## Overview

TarBase exclusively contains experimentally supported miRNA-gene interactions identified through both high-throughput and low-throughput methods. The database represents a critical resource for researchers studying post-transcriptional gene regulation mediated by microRNAs.

## Database Content

### Experimental Methods

TarBase integrates interactions from two main sources:

1. **High-Throughput Interactome Mapping**: Raw datasets from state-of-the-art methods including:
   - HITS-CLIP (High-throughput sequencing of RNA isolated by crosslinking immunoprecipitation)
   - PAR-CLIP (Photoactivatable ribonucleoside-enhanced crosslinking and immunoprecipitation)
   - CLASH (Crosslinking, ligation and sequencing of hybrids)
   - microCLIP (with super learner framework scoring)

2. **Low-Throughput Validation**: miRNA targets verified through manual curation of published literature and traditional experimental methods

All datasets are uniformly analyzed to maintain consistently high-quality standards across the database.

### Species Coverage

TarBase v9.0 provides interaction data for multiple species, organized into separate downloadable files:
- **Homo sapiens** (Human)
- **Mus musculus** (Mouse)
- **Viral species** (Including EBV and other virally-encoded miRNAs)
- **Other species**

### Annotations and Standards

TarBase uses standardized nomenclatures for consistency:
- **miRNA annotations**: miRBase v22
- **Gene annotations**: Ensembl 109
- **Genomic coordinates**: Absolute coordinate system relative to the entire genome

## Key Features

### Advanced Query Interface

Users can perform sophisticated searches with:
- **miRNA-to-target queries**: Find all experimentally validated targets for specific miRNAs
- **Gene-to-miRNA queries**: Identify all miRNAs that target specific genes
- **Autofill functionality**: Reduces mistyped entries when entering miRNA names/IDs or gene symbols/IDs

### Comprehensive Filtering Options

Refine searches based on:
- miRNA confidence level (according to miRBase annotation)
- DIANA-microT-CDS prediction scores
- Cell line, cell type, and tissue
- Experimental conditions and methods
- Species
- miRNA expression levels
- Binding site information
- microCLIP super learner framework scores

### Rich Metadata

Each miRNA-gene interaction includes detailed information:
- **Experimental context**: Method, technique, cell line, cell type, tissue, treatment conditions
- **Genomic details**: Binding site coordinates, transcript region (3'UTR, CDS, etc.), chromosome, strand
- **Validation details**: Regulation type (up/down-regulation), validation type, phenotype
- **Publication information**: PubMed ID linking to source literature
- **Confidence metrics**: Biological replicate consistency, interaction group rankings
- **Prediction scores**: DIANA-microT-CDS 2023 scores for experimental interactions

### Interactive Visualizations

TarBase provides network graph visualizations to explore:
- Combinatorial effects of multiple miRNAs on common targets
- Network structure requires genes interacting with at least two selected miRNAs
- Visual representation with miRNAs and target genes as distinct node types

### Integration with External Resources

TarBase is interconnected with:
- **PubMed**: Direct links to supporting publications
- **Ensembl**: Gene and transcript coordinate links
- **miRBase**: miRNA sequence and annotation details
- **DIANA-microT 2023**: Over 86 million in-silico predicted miRNA targets for complementary analysis

## Data Downloads

Complete interaction datasets are freely available in tab-delimited format (gzip-compressed) for:
- Homo sapiens
- Mus musculus
- Viral species
- Other species

Each download file includes 22 fields per interaction, providing comprehensive details about:
- Species, miRNA, and gene identifiers
- Binding site genomic coordinates
- Experimental methodology and conditions
- Regulation type and confidence metrics
- DIANA-microT-CDS prediction scores

## Accessibility

TarBase v9.0 is completely free and open to all users without any registration or login requirements, supporting the principles of open science and data sharing.

## Citation

If TarBase is helpful for your research, please cite:

Giorgos Skoufos, Panos Kakoulidis, Spyros Tastsoglou, Elissavet Zacharopoulou, Vasiliki Kotsira, Marios Miliotis, Galatea Mavromati, Dimitris Grigoriadis, Maria Zioga, Angeliki Velli, Ioanna Koutou, Dimitra Karagkouni, Steve Stavropoulos, Filippos S Kardaras, Anna Lifousi, Eustathia Vavalou, Armen Ovsepian, Anargyros Skoulakis, Sotiris K Tasoulis, Spiros V Georgakopoulos, Vassilis P Plagianakos, Artemis G Hatzigeorgiou (2023). "TarBase-v9.0 extends experimentally supported miRNA–gene interactions to cell-types and virally encoded miRNAs." Nucleic Acids Research, DOI: 10.1093/nar/gkad1071

## Funding

This research has been co-financed by the European Regional Development Fund of the European Union and Greek national funds through the Operational Program Competitiveness, Entrepreneurship and Innovation, under the call RESEARCH – CREATE – INNOVATE (project code: T2EDK-00391).

## Contact

TarBase is developed and maintained by the DIANA Lab at the University of Thessaly, Greece.