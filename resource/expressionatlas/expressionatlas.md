---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/about/contact
  - contact_type: email
    value: atlas-help@ebi.ac.uk
  id: ebi
  label: European Bioinformatics Institute (EMBL-EBI)
- category: Individual
  contact_details:
  - contact_type: other
    value: Lead, Gene Expression Team, EMBL-EBI
  label: Irene Papatheodorou
creation_date: '2025-09-09T00:00:00Z'
description: Expression Atlas is EMBL-EBI's open science resource that provides information
  about gene and protein expression across species and biological conditions. It aggregates,
  processes, and visualizes gene expression data from thousands of manually curated
  experiments spanning multiple species, tissue types, developmental stages, diseases,
  and experimental perturbations. Both bulk RNA-sequencing and single-cell RNA-sequencing
  datasets are supported, offering baseline expression profiles and differential gene
  expression analysis results through standardized processing pipelines.
domains:
- genomics
- biological systems
- organisms
homepage_url: https://www.ebi.ac.uk/gxa/home
id: expressionatlas
last_modified_date: '2025-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Expression Atlas
products:
- category: GraphicalInterface
  description: Main web portal for searching and exploring gene expression data across
    species, tissues, and experimental conditions with interactive heatmaps and visualizations
  format: http
  id: expressionatlas.portal
  name: Expression Atlas Portal
  product_url: https://www.ebi.ac.uk/gxa/home
- category: GraphicalInterface
  description: Single Cell Expression Atlas portal for exploring single-cell RNA-seq
    data with interactive t-SNE/UMAP plots, cell type annotations, and marker gene
    analysis
  format: http
  id: expressionatlas.single-cell
  name: Single Cell Expression Atlas
  product_url: https://www.ebi.ac.uk/gxa/sc
- category: ProgrammingInterface
  description: REST API for programmatic access to expression data, experiment metadata,
    and differential expression results
  format: http
  id: expressionatlas.api
  name: Expression Atlas REST API
  product_url: https://www.ebi.ac.uk/gxa/help/api.html
- category: Product
  description: FTP archive containing processed expression data files, experiment
    metadata, and analysis results for bulk RNA-seq experiments
  format: http
  id: expressionatlas.ftp-bulk
  name: Expression Atlas FTP (Bulk Data)
  product_url: https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/
- category: Product
  description: Individual experiment data downloads in TSV format containing expression
    matrices and statistical results
  format: tsv
  id: expressionatlas.experiment-downloads
  name: Expression Atlas Experiment Downloads
  product_url: https://www.ebi.ac.uk/gxa/download
- category: Product
  description: Normalized gene expression data and raw count matrices in R data object
    format for computational analysis
  format: mixed
  id: expressionatlas.r-objects
  name: Expression Atlas R Data Objects
  product_url: https://www.ebi.ac.uk/gxa/help/r-data-objects.html
  warnings:
  - File was not able to be retrieved when checked on 2026-02-15_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ HTTP 500 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-18: HTTP 500 error
    when accessing file'
- category: Product
  description: Baseline expression summary data across human tissues and cell types
    from GTEx, Human Protein Atlas and other major studies
  format: tsv
  id: expressionatlas.baseline-summary
  name: Expression Atlas Baseline Summary
  product_url: https://www.ebi.ac.uk/gxa/baseline/experiments
- category: Product
  description: Differential gene expression results across diseases, perturbations,
    and comparative studies with statistical significance metrics
  format: tsv
  id: expressionatlas.differential-results
  name: Expression Atlas Differential Results
  product_url: https://www.ebi.ac.uk/gxa/experiments?experimentType=differential
- category: DocumentationProduct
  description: Comprehensive help documentation covering data access, analysis methods,
    API usage, and interpretation guidelines
  format: http
  id: expressionatlas.documentation
  name: Expression Atlas Help Documentation
  product_url: https://www.ebi.ac.uk/gxa/help/index.html
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
  - Nancy George
  - Silvie Fexova
  - Alfonso Munoz Fuentes
  - Pedro Madrigal
  - Yalan Bi
  - Haider Iqbal
  - Upendra Kumbham
  - Nadja Francesca Nolte
  - Lingyun Zhao
  - Anil S Thanki
  - Iris D Yu
  - Jose C Marugan Calles
  - Karoly Erdos
  - Liora Vilmovsky
  - Sandeep R Kurri
  - Anna Vathrakokoili-Pournara
  - David Osumi-Sutherland
  - Ananth Prakash
  - Shengbo Wang
  - Marcela K Tello-Ruiz
  - Sunita Kumari
  - Doreen Ware
  - Damien Goutte-Gattat
  - Yanhui Hu
  - Nick Brown
  - Norbert Perrimon
  - Juan Antonio Vizcaíno
  - Tony Burdett
  - Sarah Teichmann
  - Alvis Brazma
  - Irene Papatheodorou
  doi: 10.1093/nar/gkad1021
  id: https://doi.org/10.1093/nar/gkad1021
  journal: Nucleic Acids Research
  preferred: true
  title: 'Expression Atlas update: insights from sequencing data at both bulk and
    single cell level'
  year: '2024'
- authors:
  - Irene Papatheodorou
  - Nancy George
  - Silvie Fexova
  - Alfonso Munoz-Fuentes
  - Pedro Madrigal
  - Haider Iqbal
  - Upendra Kumbham
  - Nadja F Nolte
  - Lingyun Zhao
  - Anil S Thanki
  - David Osumi-Sutherland
  - Ananth Prakash
  - Shengbo Wang
  - Marcela K Tello-Ruiz
  - Sunita Kumari
  - Doreen Ware
  - Juan Antonio Vizcaíno
  - Tony Burdett
  - Sarah A Teichmann
  - Alvis Brazma
  doi: 10.1093/nar/gkz947
  id: https://doi.org/10.1093/nar/gkz947
  journal: Nucleic Acids Research
  title: 'Expression Atlas update: from tissues to single cells'
  year: '2020'
repository: https://github.com/ebi-gene-expression-group
---
# Expression Atlas

Expression Atlas is EMBL-EBI's comprehensive knowledgebase for gene and protein expression data, serving as a major aggregator of transcriptomic information across the tree of life. The resource provides curated, standardized, and re-analyzed gene expression data from thousands of experiments covering multiple species, developmental stages, tissues, cell types, diseases, and experimental perturbations.

## Key Features

### Multi-Species Coverage
Expression Atlas covers over 40 different organisms including human, mouse, rat, and various plant species, with data from more than 4,500 studies encompassing over 160,000 assays.

### Dual Analysis Platforms
- **Bulk Expression Atlas**: Traditional RNA-seq and microarray data analysis with baseline and differential expression results
- **Single Cell Expression Atlas**: Single-cell RNA-seq data with advanced clustering, dimensionality reduction, and cell type annotation

### Standardized Processing
All data undergo consistent reanalysis using standardized pipelines including:
- RNA-seq processing with tools like Alevin, kallisto, and STARsolo
- Quality control and batch effect correction
- Statistical analysis for differential gene expression
- Integration with ontologies for consistent metadata annotation

### Interactive Visualizations
- Gene expression heatmaps with hierarchical clustering
- t-SNE and UMAP plots for single-cell data exploration  
- Interactive anatomograms for tissue-specific expression
- Cell type wheel search interface for single-cell datasets

The resource enables researchers to investigate baseline gene expression patterns, discover differentially expressed genes across conditions, and explore expression at single-cell resolution through an intuitive web interface and programmatic API access.