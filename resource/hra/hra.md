---
activity_status: active
category: DataModel
contacts:
- category: Individual
  label: "Katy B\xF6rner"
  orcid: 0000-0002-3321-6137
creation_date: '2025-11-05T00:00:00Z'
description: The Human Reference Atlas (HRA) is a comprehensive 3D spatial framework
  and data model for mapping the healthy human body at single-cell resolution. The
  HRA provides reference anatomical structures, cell types, biomarkers, and standardized
  spatial coordinates to enable integration and analysis of diverse biological data
  types across multiple scales from organs to cells.
domains:
- anatomy and development
- health
- biological systems
- biomedical
- precision medicine
homepage_url: https://humanatlas.io/
id: hra
infores_id: hra
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Human Reference Atlas
products:
- category: GraphicalInterface
  description: Web portal for exploring and visualizing the Human Reference Atlas
  format: http
  id: hra.portal
  latest_version: v2.4
  name: Human Reference Atlas Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra
  product_url: https://humanatlas.io/
- category: ProgrammingInterface
  connection_url: https://apps.humanatlas.io/api/
  description: Production HRA API for programmatic access to Common Coordinate Framework
    data, schemas, spatial relationships, and HRA services
  format: json
  id: hra.api
  latest_version: v2.4
  name: HRA API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra
  product_url: https://humanatlas.io/api
- category: DocumentationProduct
  description: OpenAPI specification for the production Human Reference Atlas API
  format: yaml
  id: hra.api-spec
  latest_version: v2.4
  name: HRA API OpenAPI Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra
  product_url: https://apps.humanatlas.io/api/hra-api-spec.yaml
- category: Product
  description: Downloadable data files including anatomical structures, cell types,
    and biomarkers
  format: mixed
  id: hra.data
  latest_version: v2.4
  name: HRA Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:used
    source: cl
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: fma
  - relation_type: prov:used
    source: hgnc
  - relation_type: prov:used
    source: uniprot
  product_url: https://humanatlas.io/overview-data
- category: GraphProduct
  description: HRA Knowledge Graph documentation and access information for querying
    the semantically rich graph that connects anatomical structures, cell types, biomarkers,
    spatial data, and HRA applications
  format: http
  id: hra.knowledge-graph
  latest_version: v2.4
  name: Human Reference Atlas Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:used
    source: cl
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: fma
  product_url: https://docs.humanatlas.io/apps/kg
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
  - Andreas Bueckle
  - Bruce W. Herr
  - Josef Hardi
  - Ellen M. Quardokus
  - Mark A. Musen
  - Katy Borner
  doi: 10.1038/s41597-025-05183-6
  id: doi:10.1038/s41597-025-05183-6
  journal: Scientific Data
  preferred: true
  title: Construction, Deployment, and Usage of the Human Reference Atlas Knowledge
    Graph
  year: '2025'
- authors:
  - Katy Borner
  - Sarah A. Teichmann
  - Ellen M. Quardokus
  - James C. Gee
  - Kristen Browne
  - David Osumi-Sutherland
  - Bruce W. Herr
  - Andreas Bueckle
  doi: 10.1038/s41556-021-00788-6
  id: doi:10.1038/s41556-021-00788-6
  journal: Nature Cell Biology
  preferred: false
  title: Anatomical structures, cell types and biomarkers of the Human Reference Atlas
  year: '2021'
repository: https://github.com/hubmapconsortium/ccf-ui
synonyms:
- HRA
taxon:
- NCBITaxon:9606
---
# Human Reference Atlas

## Overview

The Human Reference Atlas (HRA) is a comprehensive 3D spatial framework for mapping the healthy human body at single-cell resolution. Developed by the HuBMAP consortium and collaborators, the HRA provides standardized reference anatomical structures, cell type information, biomarkers, and spatial coordinates that enable integration and analysis of diverse biological data types.

## Key Components

### 3D Reference Organs
- High-resolution 2D and 3D reference objects across HRA release cycles
- Standardized anatomical structures and regions
- Common Coordinate Framework (CCF) for spatial registration

### Cell Type Annotations
- Comprehensive cell type taxonomies
- Cell type biomarkers and signatures
- Linkages to molecular data

### Biomarker Information
- Protein, gene, and lipid biomarkers
- Cell type-specific markers
- Spatial expression patterns

## Data Model Features

- **Common Coordinate Framework (CCF)**: 3D reference coordinate system for spatial data integration
- **Anatomical Structures, Cell Types, and Biomarkers (ASCT+B)**: Structured tables linking anatomy, cell types, and biomarkers
- **3D Reference Object Library**: Collection of validated 3D organ models
- **Crosswalks**: Mappings to standard ontologies (Uberon, CL, HGNC, etc.)

## Scope and Coverage

- **Release**: Current public portal reports the 10th release, v2.4
- **Organs**: Multi-organ reference objects, ASCT+B tables, OMAP tables, crosswalks,
  and vasculature CCF tables
- **Cell Types**: Comprehensive coverage of human cell types
- **Biomarkers**: Thousands of molecular biomarkers
- **Species**: Human (Homo sapiens, NCBITaxon:9606)
- **Resolution**: Single-cell to organ level

## Use Cases

- Spatially registering experimental datasets
- Cell type identification and validation
- Cross-dataset integration and comparison
- Atlas construction for healthy and diseased tissues
- Multi-omics data integration
- Precision medicine applications

## Integration with HuBMAP

The HRA serves as the spatial reference framework for the Human BioMolecular Atlas Program (HuBMAP), enabling:
- Registration of tissue samples to standard anatomical locations
- Integration of multi-modal imaging and omics data
- Cross-consortium data sharing and comparison
- Reproducible analysis workflows

## Information Resource ID

This resource has the Information Resource identifier: `infores:hra`

## License and Reuse

HRA data and resources are released under CC BY 4.0 license, allowing free use with appropriate attribution.
