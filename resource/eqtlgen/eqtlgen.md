---
activity_status: active
category: DataSource
description: The eQTLGen Consortium conducts large-scale meta-analyses of expression
  quantitative trait loci (eQTLs) in blood samples to investigate the genetic architecture
  of gene expression and understand the genetic underpinnings of complex traits. Phase
  I analyzed 31,684 blood and PBMC samples from 37 cohorts, identifying thousands
  of cis-eQTLs, trans-eQTLs, and expression quantitative trait score (eQTS) associations.
  The consortium also includes a single-cell eQTLGen project. Phase II is expanding
  to genome-wide eQTL meta-analysis across even more blood-based cohorts. The resulting
  summary statistics provide a valuable resource for interpreting genome-wide association
  studies (GWAS), developing novel methods, and understanding molecular mechanisms
  of complex traits.
domains:
- genomics
- biological systems
homepage_url: https://www.eqtlgen.org/
id: eqtlgen
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: eQTLGen Consortium
products:
- category: Product
  description: Significant cis-eQTL associations from Phase I meta-analysis (FDR <
    0.05, tested in at least 2 cohorts), including Bonferroni-adjusted p-values.
  format: tsv
  id: eqtlgen.cis_eqtl_significant
  name: Significant cis-eQTLs
  product_file_size: 322775879
  product_url: https://molgenis26.gcc.rug.nl/downloads/eqtlgen/cis-eqtl/2019-12-11-cis-eQTLsFDR0.05-ProbeLevel-CohortInfoRemoved-BonferroniAdded.txt.gz
- category: Product
  description: Full cis-eQTL summary statistics from Phase I meta-analysis at the
    probe level, with cohort information removed and Bonferroni-adjusted p-values
    added.
  format: tsv
  id: eqtlgen.cis_eqtl_full
  name: Full cis-eQTL Summary Statistics
  product_file_size: 3880187026
  product_url: https://molgenis26.gcc.rug.nl/downloads/eqtlgen/cis-eqtl/2019-12-11-cis-eQTLsFDR-ProbeLevel-CohortInfoRemoved-BonferroniAdded.txt.gz
- category: Product
  description: Significant trans-eQTL associations from Phase I meta-analysis for
    ~10,000 known genetic risk variants (FDR < 0.05), including Bonferroni-adjusted
    p-values.
  format: tsv
  id: eqtlgen.trans_eqtl_significant
  name: Significant trans-eQTLs
  product_file_size: 1839918
  product_url: https://molgenis26.gcc.rug.nl/downloads/eqtlgen/trans-eqtl/2018-09-04-trans-eQTLsFDR0.05-CohortInfoRemoved-BonferroniAdded.txt.gz
- category: Product
  description: Full trans-eQTL summary statistics from Phase I meta-analysis for ~10,000
    known genetic risk variants, with cohort information removed and Bonferroni-adjusted
    p-values added.
  format: tsv
  id: eqtlgen.trans_eqtl_full
  name: Full trans-eQTL Summary Statistics
  product_file_size: 6090297103
  product_url: https://molgenis26.gcc.rug.nl/downloads/eqtlgen/trans-eqtl/2018-09-04-trans-eQTLsFDR-CohortInfoRemoved-BonferroniAdded.txt.gz
- category: Product
  compression: targz
  description: cis-eQTL results formatted for Summary-data-based Mendelian Randomization
    (SMR) analysis, enabling inference of putatively causal genes.
  format: txt
  id: eqtlgen.cis_eqtl_smr
  name: SMR-formatted cis-eQTLs
  product_file_size: 1372512049
  product_url: https://molgenis26.gcc.rug.nl/downloads/eqtlgen/cis-eqtl/SMR_formatted/cis-eQTL-SMR_20191212.tar.gz
- category: Product
  description: Allele frequencies for all tested SNPs based on 26,609 eQTLGen samples
    (excluding FHS), including combined allele counts and minor allele frequencies.
  format: tsv
  id: eqtlgen.allele_frequencies
  name: Allele Frequencies
  product_file_size: 240045342
  product_url: https://molgenis26.gcc.rug.nl/downloads/eqtlgen/cis-eqtl/2018-07-18_SNP_AF_for_AlleleB_combined_allele_counts_and_MAF_pos_added.txt.gz
- category: GraphicalInterface
  description: Web interface for browsing significant cis-eQTL, trans-eQTL, and eQTS
    results from Phase I, with SMR-prioritised gene lists for various traits.
  format: http
  id: eqtlgen.phase1_browser
  name: eQTLGen Phase I Browser
  product_url: https://www.eqtlgen.org/phase1.html
- category: DocumentationProduct
  description: Analysis cookbook and documentation for eQTLGen Phase II genome-wide
    eQTL meta-analysis in blood.
  format: http
  id: eqtlgen.phase2_cookbook
  name: eQTLGen Phase II Cookbook
  product_url: https://eqtlgen.github.io/eqtlgen-web-site/eQTLGen-p2-cookbook.html
- category: GraphicalInterface
  description: Website for the single-cell eQTLGen project, providing resources and
    publications for single-cell eQTL analysis.
  format: http
  id: eqtlgen.sc_website
  name: Single-cell eQTLGen Website
  product_url: https://www.eqtlgen.org/sc
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
publications:
- authors:
  - Võsa U
  - Claringbould A
  - Westra HJ
  - Bonder MJ
  - Deelen P
  - Zeng B
  - Franke L
  id: https://doi.org/10.1038/s41588-021-00913-z
  journal: Nature Genetics
  preferred: true
  title: Large-scale cis- and trans-eQTL analyses identify thousands of genetic loci
    and polygenic scores that regulate blood gene expression
  year: '2021'
repository: https://github.com/eqtlgen
---
# eQTLGen Consortium

The eQTLGen Consortium is a collaborative effort to map the genetic architecture of blood gene expression through large-scale meta-analyses of expression quantitative trait loci (eQTLs). By harmonizing data from dozens of cohorts worldwide, the consortium provides highly powered detection of genetic effects on gene expression.

## Key Features

- **Phase I**: Meta-analysis of 31,684 blood and PBMC samples from 37 cohorts
- **cis-eQTLs**: Thousands of local genetic variants affecting nearby gene expression
- **trans-eQTLs**: Targeted analysis of ~10,000 trait-related variants affecting distant genes
- **eQTS**: Expression quantitative trait scores for polygenic regulation
- **Single-cell eQTLGen**: Single-cell flavour of the consortium for cell-type-specific eQTL mapping
- **Phase II**: Expanded genome-wide eQTL meta-analysis currently underway

The summary statistics and analysis resources enable researchers to interpret GWAS findings, prioritize candidate genes, and understand molecular mechanisms underlying complex traits.