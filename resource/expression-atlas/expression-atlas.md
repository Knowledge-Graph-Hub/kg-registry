---
id: expression-atlas
name: Expression Atlas
description: >-
  Expression Atlas is EMBL-EBI's open resource for exploring gene and protein
  expression across species, tissues, cell types, developmental stages, and
  experimental conditions. It is organized into a Baseline Atlas, reporting
  where genes and proteins are expressed under normal conditions, and a
  Differential Atlas, reporting how expression changes between conditions
  (for example disease versus control or treatment versus control). Its content
  is built from thousands of curated and consistently reanalyzed RNA-seq and
  microarray studies, including single-cell RNA-seq experiments.
activity_status: active
homepage_url: https://www.ebi.ac.uk/gxa/home
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
contacts:
- category: Organization
  label: EMBL-EBI
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/
products:
- id: expression-atlas.downloads
  name: Expression Atlas Data Downloads
  description: >-
    Bulk data downloads for Expression Atlas experiments, providing per-study
    expression matrices and analytics as tab-separated files via the EMBL-EBI
    public FTP archive.
  category: Product
  format: tsv
  product_url: https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/
  original_source:
  - source: expression-atlas
    relation_type: prov:hadPrimarySource
publications:
- id: https://doi.org/10.1093/nar/gkz947
  title: 'Expression Atlas update: from tissues to single cells'
  authors:
  - Papatheodorou I
  - Moreno P
  - Manning J
  doi: doi:10.1093/nar/gkz947
  journal: Nucleic Acids Research
  year: '2019'
  preferred: true
domains:
- genomics
- biomedical
layout: resource_detail
category: DataSource
creation_date: '2026-07-02T00:00:00Z'
last_modified_date: '2026-07-02T00:00:00Z'
---
Expression Atlas

## Description

Expression Atlas is an open science resource maintained by EMBL-EBI that lets
users find out which genes and proteins are expressed in which biological
contexts. It combines a Baseline Atlas, describing expression in tissues, cell
types, and developmental stages under normal conditions, with a Differential
Atlas, describing gene expression changes between compared experimental
conditions.

All studies are manually curated and passed through consistent RNA-seq and
microarray analysis pipelines, so results can be compared across experiments
and species. The resource also includes single-cell expression data. Data are
available for interactive browsing on the website and for bulk download through
the EMBL-EBI FTP archive.
</content>
</invoke>
