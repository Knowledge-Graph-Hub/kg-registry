---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://fabric-cancer.huji.ac.il/
  label: FABRIC Cancer Portal - The Hebrew University of Jerusalem
creation_date: '2026-06-17T00:00:00Z'
description: The FABRIC (Functional Alteration Bias Recovery In Coding regions) Cancer
  Portal is a catalogue of human protein-coding genes ranked by the strength of
  positive selection acting on them in cancer. It quantifies, for each gene, the bias
  toward functional alteration of its protein across large somatic mutation datasets.
domains:
- genomics
- biomedical
homepage_url: https://fabric-cancer.huji.ac.il/
id: fabric
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: FABRIC Cancer Portal
products:
- category: GraphicalInterface
  description: Web portal for browsing genes ranked by protein functional alteration
    bias in cancer.
  format: http
  id: fabric.site
  is_public: true
  name: FABRIC Cancer Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fabric
  product_url: https://fabric-cancer.huji.ac.il/
- category: GraphicalInterface
  description: Browsable table of genes with their cancer functional alteration bias
    scores and statistics.
  format: http
  id: fabric.genes
  is_public: true
  name: FABRIC Gene Rankings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fabric
  product_url: https://fabric-cancer.huji.ac.il/genes
publications:
- authors:
  - Nadav Brandes
  - Nathan Linial
  - Michal Linial
  doi: 10.1093/nar/gkz546
  id: https://doi.org/10.1093/nar/gkz546
  journal: Nucleic Acids Research
  preferred: true
  title: Quantifying gene selection in cancer through protein functional alteration bias
  year: '2019'
---
# FABRIC Cancer Portal

The FABRIC Cancer Portal is a comprehensive catalogue of human protein-coding genes
ranked according to the strength of positive selection acting on them in cancer. The
underlying FABRIC method quantifies, for each gene, the bias toward functional alteration
of its encoded protein relative to a background expectation, using large somatic mutation
datasets.

Content includes:

- Genome-wide ranking of genes by cancer functional alteration bias
- Per-gene statistics and significance estimates
- A browsable portal for exploring candidate cancer genes

GeneCards integrates cancer gene-selection data from the FABRIC Cancer Portal.
