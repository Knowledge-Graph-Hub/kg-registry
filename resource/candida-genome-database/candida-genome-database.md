---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.candidagenome.org/
  - contact_type: email
    value: candida-curator@lists.stanford.edu
  label: Candida Genome Database
creation_date: '2026-10-19T00:00:00Z'
description: The Candida Genome Database (CGD) is a community resource providing genomic
  sequence, gene structure and chromosomal-feature data, and functional annotation
  for Candida albicans and related pathogenic yeast species. It integrates manually
  curated Gene Ontology (GO) annotations, gene nomenclature and systematic identifiers,
  phenotype, pathway, protein, orthology, and literature data drawn from the published
  literature. CGD hosts the C. albicans Assembly 22 chromosome-level phased diploid
  assembly and offers search, BLAST, a JBrowse genome browser, and bulk downloads.
domains:
- genomics
- microbiology
- model organisms
- organisms
homepage_url: https://www.candidagenome.org/
id: candida-genome-database
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: Candida Genome Database (CGD)
products:
- category: GraphicalInterface
  description: PathoYeastract web interface with curated TF-target gene regulatory
    associations for pathogenic yeasts (Candida glabrata, C. albicans, C. tropicalis,
    C. parapsilosis, C. auris, and Cryptococcus neoformans). Associations are manually
    curated from the literature; GO annotations for Candida genes come from the Candida
    Genome Database.
  format: http
  id: yeastract.pathoyeastract
  name: PathoYeastract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yeastract
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  product_url: https://yeastract-plus.org/pathoyeastract/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: candida-genome-database
  - relation_type: prov:wasInformedBy
    source: go
- category: GraphicalInterface
  description: The CGD web portal, with gene pages, text and sequence search, BLAST,
    and a JBrowse genome browser for Candida albicans and related pathogenic yeast
    species.
  format: http
  id: candida-genome-database.portal
  name: CGD Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: candida-genome-database
  product_url: https://www.candidagenome.org/
- category: Product
  description: CGD bulk download area with per-species subdirectories for genome sequence
    (FASTA), gene models (GFF), chromosomal feature tables, GO annotations, homology,
    pathways, phenotype, and protein data.
  format: mixed
  id: candida-genome-database.downloads
  name: CGD Download Area
  original_source:
  - relation_type: prov:hadPrimarySource
    source: candida-genome-database
  product_url: https://www.candidagenome.org/download/
- category: Product
  description: Per-species GO gene-association (GAF) files, including the combined
    gene_association.cgd.gz, updated weekly.
  format: tsv
  compression: gzip
  id: candida-genome-database.go-annotations
  name: CGD GO Gene Association Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: candida-genome-database
  product_url: https://www.candidagenome.org/download/go/
publications:
- authors:
  - Marek S. Skrzypek
  - Jonathan Binkley
  - Gail Binkley
  - Stuart R. Miyasato
  - Matt Simison
  - Gavin Sherlock
  doi: 10.1093/nar/gkw924
  id: doi:10.1093/nar/gkw924
  journal: Nucleic Acids Research
  preferred: true
  title: 'The Candida Genome Database (CGD): incorporation of Assembly 22, systematic
    identifiers and visualization of high throughput sequencing data'
  year: '2017'
rrid: SCR_002036
taxon:
- NCBITaxon:5476
- NCBITaxon:5478
- NCBITaxon:5480
- NCBITaxon:5482
- NCBITaxon:42374
- NCBITaxon:498019
---
# Candida Genome Database (CGD)

## Overview

The Candida Genome Database (CGD) is the model organism database for Candida albicans and related pathogenic yeasts. It provides genome sequence, gene structure, and manually curated functional annotation — Gene Ontology terms, phenotypes, nomenclature, orthology, and literature references — and serves the C. albicans Assembly 22 phased diploid genome.

## Access

- Web portal: gene pages, search, BLAST, and a JBrowse genome browser.
- Download area: per-species sequence (FASTA), gene models (GFF), chromosomal feature tables, and functional annotation.
- GO gene-association files: per-species GAF files, updated weekly.

## Citation

Please cite: Skrzypek MS, Binkley J, Binkley G, Miyasato SR, Simison M, Sherlock G. The Candida Genome Database (CGD): incorporation of Assembly 22, systematic identifiers and visualization of high throughput sequencing data. Nucleic Acids Res. 2017;45(D1):D592–D596. doi:10.1093/nar/gkw924
