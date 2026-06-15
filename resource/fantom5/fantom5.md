---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: FANTOM5 (Functional Annotation of the Mammalian Genome 5) is a RIKEN-led international project that built a promoter-level mammalian expression atlas using Cap Analysis of Gene Expression (CAGE). It maps transcription start sites and quantifies promoter and enhancer activity across a broad collection of human and mouse primary cells, tissues, and cell lines. The resource provides genome-wide catalogues of CAGE peaks (promoters) and transcribed enhancers together with their expression profiles, supporting studies of gene regulation and cell-type-specific transcription.
domains:
  - genomics
  - systems biology
  - anatomy and development
homepage_url: https://fantom.gsc.riken.jp/5/
id: fantom5
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: FANTOM5
products:
  - category: Product
    description: Downloadable data files for the FANTOM5 promoter-level expression atlas, including CAGE peaks (promoters), transcribed enhancers, and associated expression matrices for human and mouse genome assemblies.
    format: tsv
    id: fantom5.atlas
    name: FANTOM5 Expression Atlas Data Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: fantom5
    product_url: https://fantom.gsc.riken.jp/5/datafiles/
  - category: GraphicalInterface
    description: SSTAR (Semantic catalogue of Samples, Transcription initiation, And Regulations) is the FANTOM5 web interface for browsing samples, CAGE peaks, co-expression clusters, and transcription factor annotations.
    format: http
    id: fantom5.sstar
    name: FANTOM5 SSTAR Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: fantom5
    product_url: https://fantom.gsc.riken.jp/5/sstar/
  - category: GraphicalInterface
    description: ZENBU is the interactive data integration and visualization system used to explore FANTOM5 promoter, enhancer, and time-course expression data in genomic context.
    format: http
    id: fantom5.zenbu
    name: FANTOM5 ZENBU Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: fantom5
    product_url: https://fantom.gsc.riken.jp/zenbu/
  - category: DocumentationProduct
    description: FANTOM5 project website with documentation, data access guidelines, tool descriptions, and citation information for the promoter-level mammalian expression atlas.
    format: http
    id: fantom5.docs
    name: FANTOM5 Project Website
    original_source:
      - relation_type: prov:hadPrimarySource
        source: fantom5
    product_url: https://fantom.gsc.riken.jp/5/
publications:
  - authors:
      - The FANTOM Consortium and the RIKEN PMI and CLST (DGT)
    doi: doi:10.1038/nature13182
    id: doi:10.1038/nature13182
    journal: Nature
    preferred: true
    title: A promoter-level mammalian expression atlas
    year: '2014'
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
---

# FANTOM5

FANTOM5 (Functional Annotation of the Mammalian Genome 5) is a RIKEN-led
international collaboration that produced a promoter-level mammalian expression
atlas. Using Cap Analysis of Gene Expression (CAGE), the project mapped
transcription start sites and quantified the activity of promoters and enhancers
across a large panel of human and mouse primary cells, tissues, and cell lines.

The resource provides genome-wide catalogues of CAGE peaks (promoters) and
transcribed enhancers, together with their expression profiles, and exposes the
data through downloadable files and interactive browsers (SSTAR and ZENBU). It is
a widely used reference for gene regulation, promoter and enhancer usage, and
cell-type-specific transcription. FANTOM5 data are distributed under a Creative
Commons Attribution 4.0 International (CC BY 4.0) license.
