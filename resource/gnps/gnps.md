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
description: Global Natural Products Social Molecular Networking (GNPS) is a web-based
  mass spectrometry ecosystem and open-access knowledge base for organizing, sharing,
  analyzing, and annotating raw, processed, or identified tandem mass spectrometry
  data.
domains:
- chemistry and biochemistry
- biomedical
- microbiology
homepage_url: https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp
id: gnps
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Global Natural Products Social Molecular Networking
products:
- category: GraphicalInterface
  description: GNPS web interface for molecular networking, library search, MASST
    search, public dataset browsing, spectral library curation, and related mass spectrometry
    analysis workflows.
  format: http
  id: gnps.portal
  name: GNPS Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnps
  product_url: https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp
- category: DocumentationProduct
  description: GNPS documentation covering the platform, analysis tools, data preparation,
    molecular networking, spectral library search, dataset sharing, and community
    features.
  format: http
  id: gnps.docs
  name: GNPS Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnps
  product_url: https://gnpsdocs.readthedocs.io/
- category: Product
  description: GNPS public MS/MS reference spectral library browser and curation interface.
  format: http
  id: gnps.spectral_libraries
  name: GNPS Reference Spectral Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnps
  product_url: https://gnps-external.ucsd.edu/gnpslibrary
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-15: Timeout connecting
    to URL'
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
  id: metabokg.graph
  latest_version: arXiv v1 demonstration
  name: MetaboKG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://github.com/HolobiomicsLab/MetaBoKG
  secondary_source:
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: ncit
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: prov-o
  - relation_type: prov:used
    source: dcat
  - relation_type: prov:used
    source: afo
  warnings:
  - No static public graph release or hosted endpoint was available in the GitHub
    repository when curated on 2026-06-02; the repository documents local Turtle materialization
    and Virtuoso loading.
- category: MappingProduct
  description: RML mappings and configuration templates used to transform GNPS, molecular
    networking, feature-based molecular networking, and ReDU data into RDF.
  format: http
  id: metabokg.rml_mappings
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG RML Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/mapping/rml
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gnps
  - relation_type: prov:wasInformedBy
    source: massive
  - relation_type: prov:wasInformedBy
    source: redu
- category: GraphicalInterface
  description: Pan-ReDU dashboard and file-selection interface for exploring daily
    updated public metabolomics metadata and selecting public data for GNPS reanalysis.
  format: http
  id: redu.dashboard
  name: Pan-ReDU Dashboard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://redu.gnps2.org/selection/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gnps
  - relation_type: prov:wasInformedBy
    source: massive
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
  title: Sharing and community curation of mass spectrometry data with Global Natural
    Products Social Molecular Networking
  year: '2016'
repository: https://github.com/CCMS-UCSD/GNPSDocumentation
synonyms:
- GNPS
- Global Natural Products Social Molecular Networking
---
# GNPS

GNPS is an open web ecosystem for tandem mass spectrometry analysis, molecular networking, spectral library search, dataset publication, and community curation of MS/MS reference spectra.