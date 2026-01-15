---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: gtex-help@broadinstitute.org
  - contact_type: url
    value: https://www.gtexportal.org/home/contact
  label: GTEx Consortium
description: The Genotype-Tissue Expression (GTEx) project provides a comprehensive
  resource to study tissue-specific gene expression and regulation. Samples were collected
  from 54 non-diseased tissue sites across nearly 1000 individuals, primarily for
  molecular assays including WGS, WES, and RNA-Seq.
domains:
- genomics
- biomedical
- anatomy and development
homepage_url: https://www.gtexportal.org/home/
id: gtex
infores_id: gtex
layout: resource_detail
name: GTEx
products:
- category: GraphicalInterface
  description: GTEx Portal web interface for exploring tissue-specific gene expression
    data, eQTLs, and other genomic analyses
  format: http
  id: gtex.portal
  name: GTEx Portal
  original_source:
  - gtex
  product_url: https://www.gtexportal.org/home/
- category: Product
  description: Complete GTEx v8 data including gene expression, transcript expression,
    exon expression, and junction data across tissues
  format: tsv
  id: gtex.bulk-data
  name: GTEx Bulk Data Downloads
  original_source:
  - gtex
  product_url: https://www.gtexportal.org/home/downloads/adult-gtex
- category: Product
  description: eQTL (expression quantitative trait loci) data linking genetic variants
    to gene expression across tissues
  format: tsv
  id: gtex.eqtl-data
  name: GTEx eQTL Data
  original_source:
  - gtex
  product_url: https://www.gtexportal.org/home/downloads/adult-gtex/qtl
- category: ProgrammingInterface
  description: GTEx REST API for programmatic access to gene expression and eQTL data
  format: json
  id: gtex.api
  name: GTEx REST API
  original_source:
  - gtex
  product_url: https://gtexportal.org/rest/
- category: Product
  description: Individual-level genotype and phenotype data available through dbGaP
  format: vcf
  id: gtex.dbgap-data
  name: GTEx dbGaP Data
  original_source:
  - gtex
  product_url: https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000424
- category: GraphProduct
  description: GTEx Automat
  format: kgx-jsonl
  id: automat.gtex
  infores_id: automat-gtex
  name: gtex_automat
  original_source:
  - gtex
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/GTEx_Automat/a6448b9092bb81a1/
  secondary_source:
  - automat
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
- category: Product
  description: Gene expression data aggregated from GTEx, BioGPS, Bgee and other expression
    databases
  format: http
  id: genecards.expression.data
  name: GeneCards Expression Data
  original_source:
  - gtex
  - biogps
  - bgee
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-07_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-15: HTTP 403 error
    when accessing file'
publications:
- authors:
  - GTEx Consortium
  doi: 10.1126/science.aaz1776
  id: doi:10.1126/science.aaz1776
  title: The GTEx Consortium atlas of genetic regulatory effects across human tissues
  year: '2020'
- authors:
  - GTEx Consortium
  doi: 10.1126/science.1262110
  id: doi:10.1126/science.1262110
  title: 'The Genotype-Tissue Expression (GTEx) pilot analysis: multitissue gene regulation
    in humans'
  year: '2015'
repository: https://github.com/broadinstitute/gtex-pipeline
taxon:
- NCBITaxon:9606
---
# GTEx (Genotype-Tissue Expression)

## Overview

The Genotype-Tissue Expression (GTEx) project is a comprehensive public resource to study tissue-specific gene expression and its regulation. GTEx provides insights into the mechanisms of gene regulation by analyzing human gene expression across diverse tissues and linking expression patterns to genetic variation.

## Data Collection

### Sample Collection
- **Donors**: Nearly 1,000 individuals (predominantly of European ancestry)
- **Tissues**: 54 non-diseased tissue sites
- **Quality Control**: Strict protocols for rapid tissue collection and processing
- **Sample Size**: Over 17,000 tissue samples analyzed

### Molecular Assays
- **RNA-Seq**: Comprehensive transcriptomic profiling across all tissue samples
- **Whole Genome Sequencing (WGS)**: High-coverage sequencing for genetic variant detection
- **Whole Exome Sequencing (WES)**: Focused sequencing of protein-coding regions
- **Genotyping Arrays**: Additional genotype data for population genetic analyses

## Key Features

### Expression Quantitative Trait Loci (eQTLs)
- Systematic mapping of genetic variants affecting gene expression
- Tissue-specific and cross-tissue eQTL analysis
- Fine-mapping of causal variants
- Integration with GWAS data for functional interpretation

### Tissue-Specific Expression Patterns
- Comparative analysis across 54 tissue types
- Identification of tissue-specific genes and isoforms
- Co-expression network analysis
- Developmental and physiological expression patterns

### Splicing Analysis
- Genome-wide splicing QTL (sQTL) mapping
- Alternative splicing patterns across tissues
- Splicing efficiency and regulation analysis
- Integration with protein-coding predictions

## Access and Usage

### Data Portal
The GTEx Portal provides user-friendly interfaces for:
- Gene expression visualization across tissues
- eQTL browsing and analysis tools
- Single tissue and cross-tissue analyses
- Data download capabilities

### Programmatic Access
- REST API for automated data retrieval
- Bulk data downloads in standard formats
- Integration with analysis pipelines
- R/Python package compatibility

### Data Sharing
- Open access to summary-level data
- Individual-level data available through dbGaP (phs000424)
- Standardized data formats for interoperability
- Regular data releases with expanded sample sizes

## Applications

### Functional Genomics
- Interpretation of GWAS findings
- Identification of target genes for disease variants
- Understanding of regulatory mechanisms
- Prioritization of therapeutic targets

### Comparative Biology
- Cross-tissue expression comparisons
- Evolutionary conservation of expression patterns
- Tissue-specific regulatory networks
- Development and aging studies

### Precision Medicine
- Pharmacogenomics applications
- Disease susceptibility prediction
- Treatment response biomarkers
- Population-specific analyses