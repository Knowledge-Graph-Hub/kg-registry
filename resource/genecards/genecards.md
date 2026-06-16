---
activity_status: active
category: Aggregator
creation_date: '2025-09-09T00:00:00Z'
description: GeneCards is a comprehensive, integrative database that aggregates gene-centric
  information from over 200 web sources. It provides searchable access to genomic,
  transcriptomic, proteomic, genetic, clinical and functional information for all
  annotated and predicted human genes. GeneCards automatically integrates data on
  gene function, pathways, diseases, variants, expression patterns, protein interactions,
  and more. The database includes over 443,000 gene entries with rich annotations
  from sources including HGNC, OMIM, Ensembl, UniProt, NCBI Gene, GTEx, PubMed, and
  many other major biomedical databases. GeneCards serves as a central hub for human
  gene information, making it accessible to researchers worldwide.
domains:
- genomics
- biomedical
- clinical
- proteomics
- pathways
homepage_url: https://www.genecards.org/
id: genecards
last_modified_date: '2025-10-08T00:00:00Z'
layout: resource_detail
name: GeneCards
products:
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  product_url: https://www.genecards.org/
- category: Product
  description: Integrated gene annotation data aggregated from HGNC, OMIM, Ensembl,
    NCBI Gene, UniProt and other genomic databases
  format: http
  id: genecards.gene.annotations
  name: GeneCards Gene Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Disease association data integrated from OMIM, MalaCards, ClinVar,
    Orphanet, DisGeNET and other disease databases
  format: http
  id: genecards.disease.associations
  name: GeneCards Disease Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Gene expression data aggregated from GTEx, BioGPS, Bgee and other expression
    databases
  format: http
  id: genecards.expression.data
  name: GeneCards Expression Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Pathway information integrated from Reactome, WikiPathways and other
    pathway databases
  format: http
  id: genecards.pathway.data
  name: GeneCards Pathway Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Protein interaction data aggregated from IntAct, STRING, BioGRID and
    other interaction databases
  format: http
  id: genecards.protein.interactions
  name: GeneCards Protein Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Genetic variant data from ClinVar, dbSNP, GWAS Catalog and other variant
    databases
  format: http
  id: genecards.variant.data
  name: GeneCards Variant Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Literature references from PubMed automatically associated with genes
  format: http
  id: genecards.literature
  name: GeneCards Literature References
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Gene ontology annotations from the Gene Ontology Consortium
  format: http
  id: genecards.gene.ontology
  name: GeneCards Gene Ontology Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Pharmacogenomics data from PharmGKB, DrugBank and other pharmacogenomics
    sources
  format: http
  id: genecards.pharmacogenomics
  name: GeneCards Pharmacogenomics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Model organism data from FlyBase, SGD, ZFIN and other model organism
    databases
  format: http
  id: genecards.model.organisms
  name: GeneCards Model Organism Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Protein structure data from PDB Europe and other structural databases
  format: http
  id: genecards.protein.structures
  name: GeneCards Protein Structure Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: Product
  description: Clinical trial information from ClinicalTrials.gov
  format: http
  id: genecards.clinical.trials
  name: GeneCards Clinical Trials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: genecards
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://rnacentral.org/help/public-database
repository: null
taxon:
- NCBITaxon:9606
---
# GeneCards

## Overview

GeneCards is a comprehensive, searchable database that provides integrative, gene-centric information on all annotated and predicted human genes. Developed by the Weizmann Institute of Science and maintained by LifeMap Sciences, GeneCards automatically integrates data from over 200 authoritative web sources to create unified gene cards for each human gene.

## Key Features

- **Comprehensive Integration**: Aggregates data from ~200 databases including HGNC, OMIM, Ensembl, UniProt, NCBI Gene, and many others
- **Gene Coverage**: Over 443,000 gene entries including protein-coding genes, ncRNAs, pseudogenes, and other functional elements
- **Multi-Dimensional Data**: Genomic, transcriptomic, proteomic, genetic, clinical and functional information
- **Disease Associations**: Extensive disease-gene relationships from clinical and research databases
- **Expression Patterns**: Tissue and cell-type specific expression data from multiple sources
- **Pathway Integration**: Comprehensive pathway and biological process annotations
- **Variant Information**: Genetic variant data including clinical significance
- **Literature Mining**: Automatically associated PubMed references
- **User-Friendly Interface**: Intuitive search and browsing capabilities

## Data Sources

GeneCards integrates information from major categories including:

### Genomic Databases
- HGNC (gene nomenclature)
- Ensembl (genome annotation)
- NCBI Gene
- GenBank and RefSeq
- GENCODE

### Disease Databases
- OMIM (Online Mendelian Inheritance in Man)
- MalaCards
- ClinVar
- Orphanet
- Disease Ontology

### Expression Databases
- GTEx (Genotype-Tissue Expression)
- Human Protein Atlas
- BioGPS
- Bgee

### Protein Databases
- UniProt (Swiss-Prot and TrEMBL)
- InterPro
- AlphaFold Protein Structure Database
- PDB (Protein Data Bank)

### Pathway Databases
- Reactome
- PathCards
- WikiPathways
- Pathway Commons

### Interaction Databases
- IntAct
- STRING
- BioGRID
- MINT

### Variant Databases
- ClinVar
- dbSNP
- gnomAD
- GWAS Catalog
- BRCA Exchange

### Model Organism Databases
- MGI (Mouse Genome Informatics)
- FlyBase
- WormBase
- SGD (Saccharomyces Genome Database)
- ZFIN (Zebrafish)

### Clinical Databases
- ClinicalTrials.gov
- PharmGKB
- DrugBank
- Genetic Testing Registry

### And many more specialized resources

## Gene Statistics (Version 5.25)

- **Total genes**: 443,494
- **HGNC approved**: 44,232
- **Disease genes**: 22,595
- **Protein-coding**: 21,618
- **ncRNA genes**: 269,303
  - lncRNAs: 137,345
  - piRNAs: 111,811
  - miRNAs: 1,950
  - Other ncRNA types
- **Pseudogenes**: 21,793
- **Functional elements**: 128,261

## Associated Products

The GeneCards Suite includes related databases and tools:

- **MalaCards**: Integrated database of human diseases
- **GeneHancer**: Genome-wide enhancer-to-gene associations
- **GeneCarNa**: Non-coding RNA human genes database
- **PathCards**: Human biological pathways database
- **GeneAnalytics**: Gene set analysis tool
- **GeneALaCart**: Bulk gene annotation downloads
- **VarElect**: Gene prioritization based on disease phenotypes

## Research Applications

GeneCards supports:
- Gene function and annotation research
- Disease gene discovery and validation
- Biomarker identification
- Drug target discovery
- Pathway analysis
- Clinical genetics and diagnostics
- Comparative genomics
- Systems biology studies
- Precision medicine applications

## Access

GeneCards is freely available for academic non-profit institutions. Commercial users require a license. The database is regularly updated with new data sources and improved integration methods.