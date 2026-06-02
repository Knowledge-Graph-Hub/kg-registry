---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://ccms.ucsd.edu/
    label: UC San Diego Center for Computational Mass Spectrometry
creation_date: '2026-06-02T00:00:00Z'
description: Global Natural Products Social Molecular Networking (GNPS) is a web-based mass spectrometry ecosystem and open-access knowledge base for organizing, sharing, analyzing, and annotating raw, processed, or identified tandem mass spectrometry data.
domains:
  - chemistry and biochemistry
  - biomedical
  - microbiome
homepage_url: https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp
id: gnps
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Global Natural Products Social Molecular Networking
products:
  - category: GraphicalInterface
    description: GNPS web interface for molecular networking, library search, MASST search, public dataset browsing, spectral library curation, and related mass spectrometry analysis workflows.
    format: http
    id: gnps.portal
    name: GNPS Web Portal
    original_source:
      - source: gnps
        relation_type: prov:hadPrimarySource
    product_url: https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp
  - category: DocumentationProduct
    description: GNPS documentation covering the platform, analysis tools, data preparation, molecular networking, spectral library search, dataset sharing, and community features.
    format: http
    id: gnps.docs
    name: GNPS Documentation
    original_source:
      - source: gnps
        relation_type: prov:hadPrimarySource
    product_url: https://gnpsdocs.readthedocs.io/
  - category: Product
    description: GNPS public MS/MS reference spectral library browser and curation interface.
    format: http
    id: gnps.spectral_libraries
    name: GNPS Reference Spectral Libraries
    original_source:
      - source: gnps
        relation_type: prov:hadPrimarySource
    product_url: https://gnps-external.ucsd.edu/gnpslibrary
publications:
  - authors:
      - Mingxun Wang
      - Jeremy J Carver
      - Vanessa V Phelan
      - Laura M Sanchez
      - Neha Garg
      - Yao Peng
      - Don Duy Nguyen
    doi: 10.1038/nbt.3597
    id: doi:10.1038/nbt.3597
    journal: Nature Biotechnology
    preferred: true
    title: Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecular Networking
    year: '2016'
repository: https://github.com/CCMS-UCSD/GNPSDocumentation
synonyms:
  - GNPS
  - Global Natural Products Social Molecular Networking
---

# GNPS

GNPS is an open web ecosystem for tandem mass spectrometry analysis, molecular networking, spectral library search, dataset publication, and community curation of MS/MS reference spectra.
