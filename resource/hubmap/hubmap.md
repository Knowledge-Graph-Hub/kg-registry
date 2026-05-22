---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://hubmapconsortium.org/
  - contact_type: email
    value: help@hubmapconsortium.org
  label: HuBMAP Consortium
creation_date: '2025-08-05T00:00:00Z'
description: The Human BioMolecular Atlas Program (HuBMAP) is a transformative NIH
  Common Fund initiative dedicated to creating an open, global atlas of the human
  body at the cellular level. HuBMAP develops the tools, technology, and infrastructure
  needed to map healthy human tissues in unprecedented molecular detail.
domains:
- biomedical
- anatomy and development
- biological systems
- health
- proteomics
- genomics
- systems biology
homepage_url: https://hubmapconsortium.org/
id: hubmap
last_modified_date: '2025-08-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: HuBMAP
products:
- category: Product
  description: HuBMAP Data Portal providing access to standardized single-cell and
    spatial tissue data from human donors
  format: mixed
  id: hubmap.data_portal
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: HuBMAP Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://portal.hubmapconsortium.org/
- category: Product
  description: Human Reference Atlas providing atlas data and reference functionality
  format: mixed
  id: hubmap.human_reference_atlas
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Human Reference Atlas
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://humanatlas.io/
- category: GraphicalInterface
  description: Interactive data visualization tool for spatial and single-cell multimodal
    datasets
  id: hubmap.vitessce
  name: Vitessce
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://vitessce.io/
- category: GraphicalInterface
  description: Interactive JupyterLab environments for analyzing HuBMAP data
  id: hubmap.workspaces
  name: HuBMAP Workspaces
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://portal.hubmapconsortium.org/workspaces
- category: GraphicalInterface
  description: Single-cell RNA-seq and ATAC-seq analysis using reference datasets
  id: hubmap.azimuth
  name: Azimuth
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://azimuth.hubmapconsortium.org/
- category: GraphProduct
  description: ProKN anatomy node set derived from HuBMAP Azimuth reference annotations
    for tissue-specific cell types.
  format: csv
  id: prokn.hmaz.anatomy.nodes
  name: ProKN HuBMAP Azimuth Anatomy Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 12730
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.nodes.csv
- category: GraphProduct
  description: ProKN marker-gene edges linking HuBMAP Azimuth anatomy terms to heart-enriched
    marker genes.
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_heart.gene.edges
  name: ProKN HuBMAP Azimuth Heart Marker Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 48364
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.HAS_MARKER_GENE_IN_HEART.Gene.edges.csv
- category: GraphProduct
  description: ProKN marker-gene edges linking HuBMAP Azimuth anatomy terms to kidney-enriched
    marker genes.
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_kidney.gene.edges
  name: ProKN HuBMAP Azimuth Kidney Marker Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 126963
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.HAS_MARKER_GENE_IN_KIDNEY.Gene.edges.csv
- category: GraphProduct
  description: ProKN marker-gene edges linking HuBMAP Azimuth anatomy terms to liver-enriched
    marker genes.
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_liver.gene.edges
  name: ProKN HuBMAP Azimuth Liver Marker Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 56732
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.HAS_MARKER_GENE_IN_LIVER.Gene.edges.csv
- category: GraphicalInterface
  description: Functional Unit State Identification and Navigation with Whole Slide
    Imaging
  id: hubmap.fusion
  name: FUSION
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: http://fusion.hubmapconsortium.org/
- category: Product
  description: Antibody validation reports for multiplex imaging assays
  id: hubmap.antibody_validation_reports
  name: Antibody Validation Reports
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://avr.hubmapconsortium.org/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 401 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 401 error when
    accessing file
- category: Product
  description: Data submission portal for registering and ingesting consortium data
  id: hubmap.data_ingest_portal
  name: Data Ingest Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap
  product_url: https://ingest.hubmapconsortium.org/
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
publications:
- authors:
  - "Katy B\xF6rner"
  - et al.
  doi: 10.1038/s41592-025-02120-1
  id: doi:10.1038/s41592-025-02120-1
  journal: Nature Methods
  preferred: true
  title: 'Human BioMolecular Atlas Program (HuBMAP): 3D Human Reference Atlas Construction
    and Usage'
  year: '2025'
- authors:
  - Mark S Keller
  - et al.
  doi: 10.1038/s41592-024-02497-x
  id: doi:10.1038/s41592-024-02497-x
  journal: Nature Methods
  title: 'Vitessce: integrative visualization of multimodal and spatially-resolved
    single-cell data'
  year: '2024'
repository: https://github.com/hubmapconsortium
taxon:
- NCBITaxon:9606
---
# HuBMAP - Human BioMolecular Atlas Program

The Human BioMolecular Atlas Program (HuBMAP) is a transformative initiative by the NIH Common Fund that aims to develop an open, global atlas of the human body at the cellular level. This ambitious program brings together a diverse consortium of researchers, institutions, and organizations to create comprehensive maps of healthy human tissues with unprecedented molecular detail.

## Overview

HuBMAP represents a paradigm shift in our understanding of human biology by providing spatially resolved maps of cellular organization and molecular signatures across diverse human tissues. The program integrates cutting-edge technologies in single-cell analysis, spatial biology, imaging, and data science to create a comprehensive reference atlas of the human body.

As of 2025, the HuBMAP Data Portal provides access to:
- **310 Donors** from diverse demographic backgrounds
- **3,118 Samples** across multiple tissue types
- **4,742 Datasets** representing various assay types
- **31 Organs** with detailed cellular characterization
- **21 Collections** of curated datasets

## Mission and Goals

HuBMAP's core mission is to:

1. **Develop and optimize technologies** for mapping human tissues at cellular resolution
2. **Create comprehensive reference atlases** of healthy human tissues
3. **Establish standardized protocols** for tissue processing, data generation, and analysis
4. **Build open data resources** accessible to the global research community
5. **Train the next generation** of scientists in spatial biology and atlas construction

## Key Features and Capabilities

### Data Portal
The HuBMAP Data Portal serves as the central hub for discovering, visualizing, and downloading standardized single-cell and spatial tissue data. The portal offers:

- **Faceted search functionality** for finding datasets by biological entities, organs, molecules, or cell types
- **Advanced data visualization** through integrated tools like Vitessce
- **Bulk download capabilities** via Globus and dbGaP
- **Interactive workspaces** with JupyterLab environments
- **Global data products** that aggregate datasets across multiple studies

### Technology and Assays
HuBMAP employs a diverse array of state-of-the-art technologies:

- **Single-cell RNA sequencing** (scRNA-seq)
- **Single-cell ATAC sequencing** (scATAC-seq)
- **Spatial transcriptomics** (Visium, MERFISH, seqFISH)
- **Multiplex imaging** (CODEX, Cell DIVE, CyCIF)
- **Mass spectrometry imaging**
- **Light sheet microscopy**
- **Electron microscopy**

### Human Reference Atlas (HRA)
The Human Reference Atlas provides:
- **3D reference organs** with detailed anatomical structures
- **Cell type annotations** and spatial relationships
- **Biomarker mappings** for tissue characterization
- **Cross-species comparative data**

## Research Impact and Applications

HuBMAP data and tools are advancing scientific discovery across multiple domains:

### Disease Research
- Understanding cellular changes in disease states
- Identifying therapeutic targets
- Developing precision medicine approaches

### Developmental Biology
- Mapping tissue development and aging
- Understanding cellular differentiation pathways
- Studying regenerative processes

### Drug Discovery
- Identifying drug targets at cellular resolution
- Understanding drug mechanisms and effects
- Predicting drug responses

### Computational Biology
- Developing new analytical methods
- Creating predictive models
- Advancing machine learning applications

## Data Standards and Interoperability

HuBMAP follows FAIR principles (Findable, Accessible, Interoperable, Reusable) and implements:

- **Standardized metadata schemas** for consistent data annotation
- **Quality control pipelines** ensuring data reliability
- **Controlled vocabularies** and ontology integration
- **Cross-platform compatibility** with other atlas initiatives

## Collaborative Network

The HuBMAP Consortium includes:

- **Tissue Mapping Centers (TMCs)** specializing in specific organ systems
- **Rapid Technology Implementation (RTI)** teams developing new methods
- **Integration, Visualization & Engagement (IVE)** teams building tools and resources
- **Technology Development Centers** advancing instrumentation and protocols

## Data Access and Usage

All HuBMAP data is made freely available under Creative Commons Attribution 4.0 (CC BY 4.0) licensing, supporting:

- **Open science principles** with unrestricted data access
- **Collaborative research** across institutions and disciplines
- **Educational applications** for training and outreach
- **Commercial applications** fostering innovation and translation

## Future Directions

HuBMAP continues to evolve with ongoing developments in:

- **Multi-modal data integration** combining diverse assay types
- **Temporal mapping** capturing dynamic cellular processes
- **Disease atlas construction** extending beyond healthy tissues
- **Cross-consortium collaboration** with international atlas initiatives
- **AI and machine learning** applications for automated analysis

The program represents a foundational resource for understanding human biology and disease, providing the research community with unprecedented insights into cellular organization and function across the human body.

---