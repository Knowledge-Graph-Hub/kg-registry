---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://ccms.ucsd.edu/
    label: UC San Diego Center for Computational Mass Spectrometry
creation_date: '2026-06-02T00:00:00Z'
description: ReDU (Reanalysis of Data User Interface) is a metadata-driven resource for finding, selecting, and reanalyzing public tandem mass spectrometry data at repository scale. It bridges GNPS analysis workflows with MassIVE public mass spectrometry datasets and harmonized sample metadata.
domains:
  - chemistry and biochemistry
  - biomedical
  - microbiome
homepage_url: https://redu.gnps2.org/selection/
id: redu
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: ReDU
products:
  - category: GraphicalInterface
    description: Pan-ReDU dashboard and file-selection interface for exploring daily updated public metabolomics metadata and selecting public data for GNPS reanalysis.
    format: http
    id: redu.dashboard
    name: Pan-ReDU Dashboard
    original_source:
      - source: redu
        relation_type: prov:hadPrimarySource
    product_url: https://redu.gnps2.org/selection/
    secondary_source:
      - source: gnps
        relation_type: prov:wasInformedBy
      - source: massive
        relation_type: prov:wasInformedBy
  - category: DocumentationProduct
    description: ReDU documentation describing the ReDU file selector, sample information metadata, GNPS repository-scale molecular networking, chemical explorer, contribution process, and data/code availability.
    format: http
    id: redu.docs
    name: ReDU Documentation
    original_source:
      - source: redu
        relation_type: prov:hadPrimarySource
    product_url: https://mwang87.github.io/ReDU-MS2-Documentation/
    repository: https://github.com/mwang87/ReDU-MS2-Documentation
publications:
  - authors:
      - Alan K Jarmusch
      - Louis-Felix Nothias
      - Michael Petras
      - Wang Mingxun
      - Jennifer Koester
      - Melody Vargas
      - Nina van der Hooft
      - Pieter C Dorrestein
    doi: 10.1038/s41592-020-0916-7
    id: doi:10.1038/s41592-020-0916-7
    journal: Nature Methods
    preferred: true
    title: 'ReDU: a framework to find and reanalyze public mass spectrometry data'
    year: '2020'
repository: https://github.com/mwang87/ReDU-MS2-Documentation
synonyms:
  - ReDU
  - Reanalysis of Data User Interface
  - Pan-ReDU
---

# ReDU

ReDU organizes public tandem mass spectrometry data through harmonized sample metadata, enabling repository-scale file selection, GNPS reanalysis, and contextual exploration of public metabolomics data.
