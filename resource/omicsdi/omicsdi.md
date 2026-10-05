---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/
  id: ebi
  label: EMBL-EBI
creation_date: '2025-10-30T00:00:00Z'
description: OmicsDI (Omics Discovery Index) is an EMBL-EBI index of dataset metadata
  from public omics repositories. As of October 2026 it indexes about 4.9 million
  datasets from 28 repositories, covering genomics, transcriptomics, proteomics, metabolomics,
  computational models and clinical studies, plus BioStudies literature records, and
  provides a unified search portal and REST API.
domains:
- genomics
- proteomics
- metabolomics
- chemistry and biochemistry
homepage_url: https://www.omicsdi.org/
id: omicsdi
infores_id: omicsdi
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use/
  label: EMBL-EBI Terms of Use
name: OmicsDI
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
- category: GraphProduct
  description: RDF (Turtle) knowledge graph of the NIAID Data Ecosystem, harmonizing
    dataset and computational-tool metadata harvested from NIAID-funded and globally-relevant
    infectious and immune-mediated disease repositories. Served through the Proto-OKN
    FRINK federated SPARQL platform.
  format: ttl
  id: nde.graph
  name: NIAID Data Ecosystem KG (graph)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nde
  - relation_type: prov:hadPrimarySource
    source: immport
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  product_url: https://frink.apps.renci.org/nde
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: omicsdi
  - relation_type: prov:wasInfluencedBy
    source: hubmap
  - relation_type: prov:wasInfluencedBy
    source: massive
  - relation_type: prov:wasInfluencedBy
    source: pdb
  - relation_type: prov:wasInfluencedBy
    source: lincs
publications:
- authors:
  - Yasset Perez-Riverol
  - Mingze Bai
  - Felipe da Veiga Leprevost
  - Silvano Squizzato
  - Young Mi Park
  - Kenneth Haug
  - Adam J Carroll
  - Dylan Spalding
  - Justin Paschall
  - Mingxun Wang
  - Noemi del-Toro
  - Tobias Ternent
  - Peng Zhang
  - Nicola Buso
  - Nuno Bandeira
  - Eric W Deutsch
  - David S Campbell
  - Ronald C Beavis
  - Reza M Salek
  - Ugis Sarkans
  - Robert Petryszak
  - Maria Keays
  - Eoin Fahy
  - Manish Sud
  - Shankar Subramaniam
  - Ariana Barbera
  - Rafael C Jiménez
  - Alexey I Nesvizhskii
  - Susanna-Assunta Sansone
  - Christoph Steinbeck
  - Rodrigo Lopez
  - Juan A Vizcaíno
  - Peipei Ping
  - Henning Hermjakob
  doi: 10.1038/nbt.3790
  id: doi:10.1038/nbt.3790
  journal: Nature Biotechnology
  preferred: true
  title: Discovering and linking public omics data sets using the Omics Discovery
    Index
  year: '2017'
- authors:
  - Gaurhari Dass
  - Manh-Tu Vu
  - Pan Xu
  - Enrique Audain
  - Marc-Phillip Hitz
  - Björn A Grüning
  - Henning Hermjakob
  - Yasset Perez-Riverol
  doi: 10.1093/nar/gkaa326
  id: doi:10.1093/nar/gkaa326
  journal: Nucleic Acids Research
  title: The omics discovery REST interface
  year: '2020'
- authors:
  - Yasset Perez-Riverol
  - Andrey Zorin
  - Gaurhari Dass
  - Manh-Tu Vu
  - Pan Xu
  - Mihai Glont
  - Juan Antonio Vizcaíno
  - Andrew F. Jarnuczak
  - Robert Petryszak
  - Peipei Ping
  - Henning Hermjakob
  doi: 10.1038/s41467-019-11461-w
  id: doi:10.1038/s41467-019-11461-w
  journal: Nature Communications
  title: Quantifying the impact of public omics data
  year: '2019'
synonyms:
- OmicsDI
- Omics Discovery Index
---
# OmicsDI

## Overview

OmicsDI (Omics Discovery Index) is an integrated resource developed by EMBL-EBI that provides a unified search and discovery platform for omics datasets. It aggregates metadata from multiple public omics repositories, enabling researchers to find and access genomics, proteomics, metabolomics, transcriptomics, and multi-omics datasets through a single interface.

## Key Features

- **Multi-Repository Search**: Unified access to datasets from multiple omics databases
- **Cross-Omics Coverage**: Genomics, proteomics, metabolomics, transcriptomics, and multi-omics data
- **Standardized Metadata**: Harmonized dataset descriptions using controlled vocabularies
- **Advanced Search**: Faceted search across organisms, tissues, diseases, and data types
- **Dataset Discovery**: Browse and explore related datasets and studies
- **API Access**: Programmatic access to dataset metadata
- **Citation Tracking**: Links to publications and citation information

## Integrated Repositories

OmicsDI aggregates data from major omics repositories:

### Genomics and Transcriptomics
- ArrayExpress
- GEO (Gene Expression Omnibus)
- ENA (European Nucleotide Archive)
- dbGaP
- EGA (European Genome-phenome Archive)
- EVA (European Variation Archive)
- NODE (National Omics Data Encyclopedia)
- LINCS

### Proteomics
- PRIDE (Proteomics Identifications Database)
- PeptideAtlas
- MassIVE
- jPOST
- iProX
- Panorama Public
- GPMDB
- PaxDb

### Metabolomics
- MetaboLights
- Metabolomics Workbench
- GNPS

### Models
- BioModels
- FAIRDOMHub
- Physiome Model Repository
- Cell Collective

### Other Data Types
- Expression Atlas
- BioStudies (including BioImages and literature records)
- ECRIN MDR (clinical studies)

## Data Content

### Dataset Metadata
- Dataset identifiers and accession numbers
- Study titles and descriptions
- Organism and tissue information
- Disease and phenotype annotations
- Experimental design details
- Technology and platform information
- Sample sizes and biological replicates
- Publication references
- Data availability and access information

### Standardization
- Ontology-based annotations (e.g., EFO, NCBI Taxonomy)
- Unified metadata schema across repositories
- Controlled vocabulary for data types and technologies
- Cross-references between related datasets

## Applications

- **Data Discovery**: Finding relevant omics datasets for research questions
- **Multi-Omics Integration**: Identifying complementary datasets across omics types
- **Meta-Analysis**: Discovering comparable datasets for large-scale analyses
- **Hypothesis Generation**: Exploring related studies and datasets
- **Data Reuse**: Accessing public omics data for secondary analyses
- **Literature Mining**: Connecting datasets to publications

## Search Capabilities

### Faceted Search
- Organism/species
- Tissue and cell type
- Disease and phenotype
- Omics type
- Technology platform
- Publication date
- Submitter institution

### Advanced Features
- Free-text search across metadata fields
- Boolean operators and filters
- Related dataset recommendations
- Export and download of search results

## API and Programmatic Access

OmicsDI provides:
- RESTful API for dataset queries
- Bulk metadata download
- Integration with computational workflows

## Information Resource ID

This resource has the Information Resource identifier: `infores:omicsdi`

## Access

- **Web Interface**: https://www.omicsdi.org/
- **API Documentation**: https://www.omicsdi.org/help/api
- **Help and Tutorials**: https://www.omicsdi.org/about

## Governance

OmicsDI is maintained by the European Bioinformatics Institute (EMBL-EBI) as part of their data integration and discovery services.

For more information, visit https://www.omicsdi.org/ or contact EMBL-EBI at https://www.ebi.ac.uk/