---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://motrpac-data.org/contact
  label: MoTrPAC BioInformatics Center
creation_date: '2025-10-29T00:00:00Z'
description: The Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data
  Hub is a national research initiative that generates a comprehensive molecular map
  of the effects of exercise and physical activity training. The data repository provides
  multi-omics datasets documenting molecular changes from exercise across multiple
  tissues, including transcriptomics, proteomics, metabolomics, and epigenomics data.
  The complete young adult rat endurance training dataset is publicly available, featuring
  quantitative results and analyses from 20 tissues across 29 assays and 5 time points,
  studying male and female animals. The data hub provides both browsable study data
  and pre-bundled datasets organized by tissue type and omics platform, all released
  under CC BY 4.0 license. The resource includes phenotypic data, sample-level metadata,
  quality control metrics, and quantitative results to enable comprehensive analysis
  of the temporal dynamics of multi-omic responses to endurance exercise training.
domains:
- biological systems
- biomedical
- proteomics
- genomics
- systems biology
homepage_url: https://motrpac-data.org/
id: motrpac
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub
products:
- category: GraphicalInterface
  description: Interactive data browser for exploring and downloading MoTrPAC multi-omics
    datasets by tissue, ome, or assay type
  format: http
  id: motrpac.data-browser
  name: MoTrPAC Data Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: GraphicalInterface
  description: Data search interface for finding molecular features and study results
    across MoTrPAC data releases
  format: http
  id: motrpac.search
  name: MoTrPAC Data Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/search
- category: DocumentationProduct
  description: Data access information for using MoTrPAC public and controlled-access
    data
  format: http
  id: motrpac.data-access
  name: MoTrPAC Data Access Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-access
- category: DocumentationProduct
  description: MoTrPAC source-code and analysis repository index linked from the Data
    Hub
  format: http
  id: motrpac.code-repositories
  name: MoTrPAC Code Repositories
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/code-repositories
- category: DocumentationProduct
  description: Publication index for MoTrPAC marker, data-release, and analysis papers
  format: http
  id: motrpac.publications
  name: MoTrPAC Publications
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/publications
- category: Product
  description: Phenotypic data from young adult rats (6-month old) that performed
    endurance exercise training
  format: csv
  id: motrpac.phenotype
  name: Rat Young Adult Endurance Training - Phenotype Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: Product
  description: Epigenomics data including ATAC-seq and RRBS analyses, sample-level
    metadata, QC, and quantitative results across tissues
  format: csv
  id: motrpac.epigenomics
  name: Rat Young Adult Endurance Training - Epigenomics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: Product
  description: RNA-seq analyses, sample-level metadata, QC, and quantitative results
    across tissues
  format: csv
  id: motrpac.transcriptomics
  name: Rat Young Adult Endurance Training - Transcriptomics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: Product
  description: Untargeted proteomics data including Acetyl Proteomics, Global Proteomics,
    Phosphoproteomics, and Protein Ubiquitination analyses across tissues
  format: csv
  id: motrpac.proteomics-untargeted
  name: Rat Young Adult Endurance Training - Proteomics (Untargeted)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: Product
  description: Untargeted metabolomics analyses, sample-level metadata, QC, and quantitative
    results across tissues
  format: csv
  id: motrpac.metabolomics-untargeted
  name: Rat Young Adult Endurance Training - Metabolomics (Untargeted)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: Product
  description: Targeted metabolomics analyses, sample-level metadata, QC, and quantitative
    results across tissues
  format: csv
  id: motrpac.metabolomics-targeted
  name: Rat Young Adult Endurance Training - Metabolomics (Targeted)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: Product
  description: Targeted proteomics immunoassay data with analyses, sample-level metadata,
    QC, and quantitative results across tissues
  format: csv
  id: motrpac.proteomics-targeted
  name: Rat Young Adult Endurance Training - Proteomics (Targeted/Immunoassay)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/data-download
- category: DocumentationProduct
  description: Video tutorials demonstrating how to use the MoTrPAC Data Hub and access
    datasets
  format: http
  id: motrpac.video-tutorials
  name: MoTrPAC Data Hub Video Tutorials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/
- category: GraphicalInterface
  description: Main portal for the MoTrPAC Data Hub providing access to data downloads,
    documentation, and visualization tools
  format: http
  id: motrpac.data-hub
  name: MoTrPAC Data Hub Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://motrpac-data.org/
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Neo4j knowledge graph containing integrated gene sets from multiple
    Common Fund programs with cross-references
  dump_format: neo4j
  format: neo4j
  id: cfde-gse.graph
  name: CFDE-GSE Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
- category: Product
  description: Standardized gene set collections from Common Fund programs in GMT
    format
  id: cfde-gse.genesets
  name: CFDE Gene Set Collections
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://gse.cfde.cloud/downloads/
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
publications:
- authors:
  - MoTrPAC Study Group
  doi: 10.1016/j.cell.2020.06.004
  id: https://doi.org/10.1016/j.cell.2020.06.004
  journal: Cell
  preferred: true
  title: 'Molecular Transducers of Physical Activity Consortium (MoTrPAC): Mapping the Dynamic Responses to Exercise'
  year: '2020'
- authors:
  - MoTrPAC Study Group
  doi: 10.1038/s41586-023-06877-w
  id: https://doi.org/10.1038/s41586-023-06877-w
  journal: Nature
  preferred: false
  title: Temporal dynamics of the multi-omic response to endurance exercise training
  year: '2024'
taxon:
- NCBITaxon:10116
---
# Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub

## Overview

The Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub is a comprehensive data repository and resource center for a national research initiative aimed at generating a molecular map of the effects of exercise and physical activity training. The consortium brings together researchers to study how physical activity influences molecular changes across multiple tissues and biological systems.

## Mission and Goals

MoTrPAC's primary objective is to map the dynamic responses to exercise at the molecular level. The consortium generates multi-omics datasets that document comprehensive molecular changes resulting from exercise training, enabling researchers to understand the mechanisms by which physical activity promotes health and prevents disease.

## Data Resources

### Young Adult Rat Endurance Training Study

The complete young adult rat endurance training dataset is publicly available, representing a landmark study published in Nature (2024). This comprehensive dataset includes:

**Study Design:**
- **Animals**: Male and female young adult rats (6-month old)
- **Tissues**: 20 different tissue types
- **Assays**: 29 assays across multiple omics platforms
- **Time Points**: 5 time points throughout the training period
- **Exercise Modality**: Endurance training protocol

**Available Data Types:**

1. **Phenotypic Data**: Comprehensive phenotypic measurements and metadata from trained animals
2. **Epigenomics**: ATAC-seq and RRBS (Reduced Representation Bisulfite Sequencing) data
3. **Transcriptomics**: RNA-seq data across all tissues
4. **Proteomics (Untargeted)**:
   - Acetyl Proteomics
   - Global Proteomics
   - Phosphoproteomics
   - Protein Ubiquitination
5. **Metabolomics (Untargeted)**: Comprehensive metabolite profiling
6. **Metabolomics (Targeted)**: Focused metabolite measurements
7. **Proteomics (Targeted)**: Immunoassay-based protein quantification

### Tissue-Specific Datasets

Pre-bundled datasets are available for individual tissues, including:
- Gastrocnemius (skeletal muscle)
- Heart
- Liver
- Lung
- Kidney
- Brown adipose tissue
- White adipose tissue
- Blood RNA
- Plasma

Each tissue-specific dataset includes analyses, sample-level metadata, quality control metrics, and quantitative results across all relevant omics platforms.

## Data Organization and Access

### Data Structure

All datasets include:
- **Quantitative Results**: Processed and normalized molecular measurements
- **Sample-Level Metadata**: Detailed information about each biological sample
- **Quality Control Metrics**: QC assessments for each assay and sample
- **Analysis Results**: Statistical analyses and differential expression/abundance results

### Data Formats

Data are provided in standardized formats:
- CSV files for quantitative data and metadata
- Comprehensive documentation for data interpretation
- R objects for advanced analysis workflows

### Download Options

The MoTrPAC Data Hub offers flexible data access:
1. **Interactive Browser**: Browse and select specific data by tissue, ome, or assay type
2. **Pre-bundled Downloads**: Complete datasets organized by omics type or tissue
3. **Programmatic Access**: R packages for data retrieval and analysis

## Key Findings

The temporal dynamics study revealed:
- A network of genes functionally related to longevity, muscle system processes, and response to mechanical stimulus
- Training-differential features whose abundances significantly changed over the training time course
- Molecular adaptations occurring at different time points during the training period
- Cross-tissue coordination of molecular responses to exercise

## Technical Infrastructure

The MoTrPAC Data Hub is designed and maintained by the MoTrPAC BioInformatics Center at Stanford University. The infrastructure includes:

- **Data Processing Pipeline**: Standardized workflows from data ingestion to quality control, processing, and analysis
- **Visualization Tools**: Interactive tools for exploring molecular changes across tissues and time points
- **Documentation**: Comprehensive technical guides for data interpretation and analysis
- **Source Code Repository**: Open access to analysis code and processing pipelines

## Licensing and Data Sharing

All MoTrPAC data are released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license, promoting open science and data reuse. Users are required to:
- Cite the MoTrPAC Marker Paper (Cell, 2020)
- Cite dataset-specific publications when using particular datasets
- Acknowledge data from motrpac-data.org in resulting publications

## Publications

### Marker Paper
The foundational MoTrPAC publication describing the consortium's goals, structure, and approach:
- MoTrPAC Study Group (2020). "Molecular Transducers of Physical Activity Consortium (MoTrPAC): Mapping the Dynamic Responses to Exercise." *Cell* 181(7):1464-1474. https://doi.org/10.1016/j.cell.2020.06.004

### Major Data Release
The comprehensive analysis of the young adult rat endurance training study:
- MoTrPAC Study Group (2024). "Temporal dynamics of the multi-omic response to endurance exercise training." *Nature* 629:174-183. https://doi.org/10.1038/s41586-023-06877-w

## Community Engagement

MoTrPAC maintains active engagement with the research community through:
- **Monthly Virtual Office Hours**: Regular opportunities to learn about data and ask questions
- **Newsletter**: Updates on new data releases and available resources
- **Tutorial Videos**: Comprehensive guides for using the Data Hub
- **Contact Support**: Direct assistance for data access and interpretation

## Ongoing Studies

While the young adult rat endurance training dataset is currently publicly available, MoTrPAC has additional ongoing studies across:
- Different exercise modalities
- Various animal models and age groups
- Multiple tissue types and molecular platforms

Data from these studies will be released as they become available, expanding the molecular map of exercise responses.

## Funding

MoTrPAC is funded by the **NIH Common Fund**, supporting this large-scale collaborative effort to understand the molecular mechanisms underlying the health benefits of physical activity.