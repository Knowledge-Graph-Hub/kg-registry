---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://labs.icahn.mssm.edu/maayanlab/
    label: Ma'ayan Laboratory
creation_date: '2026-05-21T00:00:00Z'
description: Enrichr is a Ma'ayan Lab web-based gene set enrichment analysis resource that accepts gene lists and related inputs, tests them against hundreds of curated and crowd-sourced gene set libraries, and provides ranked enrichment results, visualizations, and programmatic access.
domains:
  - biomedical
  - genomics
  - systems biology
homepage_url: https://maayanlab.cloud/Enrichr/
id: enrichr
last_modified_date: '2026-05-21T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Enrichr
products:
  - category: GraphicalInterface
    description: Main Enrichr web interface for submitting gene sets, exploring enrichment results, browsing libraries, and viewing interactive visualizations
    format: http
    id: enrichr.portal
    name: Enrichr Web Portal
    original_source:
      - source: enrichr
        relation_type: prov:hadPrimarySource
    product_url: https://maayanlab.cloud/Enrichr/
  - category: ProgrammingInterface
    description: REST API for submitting gene lists, retrieving enrichment results, exporting analyses, and querying Enrichr programmatically
    format: json
    id: enrichr.api
    is_public: true
    name: Enrichr API
    original_source:
      - source: enrichr
        relation_type: prov:hadPrimarySource
    product_url: https://maayanlab.cloud/Enrichr/help#api
  - category: Product
    description: JSON endpoint listing Enrichr gene set libraries with category assignments, term counts, gene coverage, and source links
    format: json
    id: enrichr.library-statistics
    name: Enrichr Library Statistics
    original_source:
      - source: enrichr
        relation_type: prov:hadPrimarySource
    product_url: https://maayanlab.cloud/Enrichr/datasetStatistics
publications:
  - authors:
      - Chen EY
      - Tan CM
      - Kou Y
      - Duan Q
      - Wang Z
      - Meirelles GV
      - Clark NR
      - Ma'ayan A
    id: doi:10.1186/1471-2105-14-128
    journal: BMC Bioinformatics
    preferred: true
    title: 'Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool'
    year: '2013'
  - authors:
      - Kuleshov MV
      - Jones MR
      - Rouillard AD
      - Fernandez NF
      - Duan Q
      - Wang Z
      - Koplev S
      - Jenkins SL
      - Jagodnik KM
      - Lachmann A
      - McDermott MG
      - Monteiro CD
      - Ma'ayan A
    id: doi:10.1093/nar/gkw377
    journal: Nucleic Acids Research
    preferred: false
    title: 'Enrichr: a comprehensive gene set enrichment analysis web server 2016 update'
    year: '2016'
repository: https://github.com/MaayanLab/enrichr_issues
taxon:
  - NCBITaxon:9606
---

# Enrichr

Enrichr is a widely used web-based enrichment analysis platform for interpreting gene lists against a large collection of curated and derived gene set libraries. The current public deployment provides interactive submission and result views, library browsing, multiple scoring schemes, and a documented REST API for automated workflows.

Current Enrichr documentation describes support for crisp and fuzzy gene sets, optional background-aware enrichment through the linked Speedrichr service, downloadable enrichment result exports, and a large catalog of libraries spanning transcription, pathways, ontologies, diseases, drugs, cell types, and crowd-contributed signatures. The public site also exposes library statistics as structured JSON.

## Access

- Main portal: [Enrichr](https://maayanlab.cloud/Enrichr/)
- API documentation: [Enrichr API](https://maayanlab.cloud/Enrichr/help#api)
- Library statistics: [datasetStatistics](https://maayanlab.cloud/Enrichr/datasetStatistics)

## Automated Evaluation

- View the automated evaluation: [enrichr automated evaluation](enrichr_eval_automated.html)
