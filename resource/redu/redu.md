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
description: ReDU (Reanalysis of Data User Interface) is a metadata-driven resource
  for finding, selecting, and reanalyzing public tandem mass spectrometry data at
  repository scale. It bridges GNPS analysis workflows with MassIVE public mass spectrometry
  datasets and harmonized sample metadata.
domains:
- chemistry and biochemistry
- biomedical
- microbiology
homepage_url: https://redu.gnps2.org/selection/
id: redu
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: ReDU
products:
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
- category: DocumentationProduct
  description: ReDU documentation describing the ReDU file selector, sample information
    metadata, GNPS repository-scale molecular networking, chemical explorer, contribution
    process, and data/code availability.
  format: http
  id: redu.docs
  name: ReDU Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://mwang87.github.io/ReDU-MS2-Documentation/
  repository: https://github.com/mwang87/ReDU-MS2-Documentation
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