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
creation_date: '2025-06-04T00:00:00Z'
description: The Genotype-Tissue Expression (GTEx) project provides a comprehensive resource to study tissue-specific gene expression and regulation. Samples were collected from 54 non-diseased tissue sites across nearly 1000 individuals, primarily for molecular assays including WGS, WES, and RNA-Seq.
domains:
  - genomics
  - biomedical
  - anatomy and development
homepage_url: https://www.gtexportal.org/home/
id: gtex
infores_id: gtex
last_modified_date: '2026-04-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gtexportal.org/home/license
  label: GTEx Portal Data License
name: GTEx
products:
  - category: GraphicalInterface
    description: GTEx Portal web interface for exploring tissue-specific gene expression data, eQTLs, and other genomic analyses
    format: http
    id: gtex.portal
    name: GTEx Portal
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://www.gtexportal.org/home/
  - category: Product
    description: Complete GTEx v8 data including gene expression, transcript expression, exon expression, and junction data across tissues
    format: tsv
    id: gtex.bulk-data
    name: GTEx Bulk Data Downloads
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://www.gtexportal.org/home/downloads/adult-gtex
  - category: Product
    description: eQTL (expression quantitative trait loci) data linking genetic variants to gene expression across tissues
    format: tsv
    id: gtex.eqtl-data
    name: GTEx eQTL Data
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://www.gtexportal.org/home/downloads/adult-gtex/qtl
  - category: ProgrammingInterface
    description: GTEx REST API for programmatic access to gene expression and eQTL data
    format: json
    id: gtex.api
    name: GTEx REST API
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://gtexportal.org/rest/
  - category: Product
    description: Individual-level genotype and phenotype data available through dbGaP
    format: vcf
    id: gtex.dbgap-data
    name: GTEx dbGaP Data
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000424
  - category: GraphProduct
    description: GTEx Automat
    format: kgx-jsonl
    id: automat.gtex
    infores_id: automat-gtex
    name: gtex_automat
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/GTEx_Automat/a6448b9092bb81a1/
    secondary_source:
      - source: automat
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: achilles
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ccle
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: cellosaurus
        relation_type: prov:hadPrimarySource
      - source: clue
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pharmacodb
        relation_type: prov:hadPrimarySource
      - source: prism
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: offsides
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: repohub
        relation_type: prov:hadPrimarySource
      - source: chemicalchecker
        relation_type: prov:hadPrimarySource
      - source: repodb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: creeds
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: dorothea
        relation_type: prov:hadPrimarySource
      - source: progeny
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: huri
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: omnipath
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - source: bioteque
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Integrated graph knowledge base combining Mendelian randomization causal estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships (Neo4j backend)
    format: neo4j
    id: epigraphdb.graph
    name: EpiGraphDB Graph Database
    original_source:
      - source: epigraphdb
        relation_type: prov:hadPrimarySource
      - source: kg-monarch
        relation_type: prov:hadPrimarySource
      - source: vectology
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: prsatlas
        relation_type: prov:hadPrimarySource
      - source: eqtlgen
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: cpic
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: mrbase
        relation_type: prov:hadPrimarySource
    product_url: https://docs.epigraphdb.org/graph-database/
    secondary_source:
      - source: epigraphdb
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Gene expression data aggregated from GTEx, BioGPS, Bgee and other expression databases
    format: http
    id: genecards.expression.data
    name: GeneCards Expression Data
    original_source:
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: biogps
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
    product_url: https://www.genecards.org/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
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
    title: 'The Genotype-Tissue Expression (GTEx) pilot analysis: multitissue gene regulation in humans'
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
