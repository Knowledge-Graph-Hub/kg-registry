---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://druggablegenome.net/
  - contact_type: email
    value: idg.rdoc@gmail.com
  label: Illuminating the Druggable Genome (IDG) Program
- category: Organization
  contact_details:
  - contact_type: url
    value: https://druggablegenome.net/KMC_UNM
  label: Knowledge Management Center - University of New Mexico
- category: Individual
  contact_details:
  - contact_type: github
    value: tudoroprea
  label: Tudor I. Oprea
creation_date: '2025-01-10T00:00:00Z'
description: The Target Central Resource Database (TCRD) is a comprehensive multi-omics
  knowledge base developed by the NIH Common Fund Illuminating the Druggable Genome
  (IDG) program to catalog and illuminate the human proteome, with special focus on
  understudied proteins in four major druggable protein families G-protein coupled
  receptors (GPCRs), nuclear receptors, ion channels, and protein kinases. TCRD aggregates
  data from over 80 diverse sources including protein-protein interactions, disease
  associations, drug-target relationships, gene expression profiles, tissue specificity,
  pathway memberships, phenotype associations, and pharmacological data to create
  a unified resource for target prioritization and drug discovery research. The database
  employs a protein Target Development Level (TDL) classification system (Tclin, Tchem,
  Tbio, Tdark) that ranks proteins based on the amount of available knowledge, specifically
  highlighting understudied dark proteins that lack adequate characterization. TCRD
  contains extensive information on protein sequences, structures, functions, disease
  relationships, and chemical interactions, integrating data from resources such as
  UniProt, ChEMBL, DrugCentral, STRING, GTEx, OMIM, and many others. The database
  is designed to be machine-learning ready with structured data formats suitable for
  computational analysis and target prediction algorithms. TCRD serves as the backend
  data infrastructure for Pharos, the user-friendly web interface that enables researchers
  to browse, visualize, and analyze the integrated target data through interactive
  tools and visualizations. The resource is continuously updated with new data sources
  and releases, with current version 6.13.5 containing comprehensive annotations for
  the human proteome.
domains:
- drug discovery
- genomics
- biological systems
homepage_url: http://juniper.health.unm.edu/tcrd/
id: tcrd
infores_id: tcrd
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: Target Central Resource Database
products:
- category: Product
  description: MySQL database dump files containing the complete TCRD relational database
    schema and data for local installation and analysis
  format: mysql
  id: tcrd.database_download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: http://juniper.health.unm.edu/tcrd/download/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-02: Error connecting
    to URL: HTTPConnectionPool(host=''juniper.health.unm.edu'', port=80): Max retries
    exceeded with url: /tcrd/download/ (Caused by NameResolutionError("HTTPConnection(host=''juniper.health.unm.edu'',
    port=80): Failed to resolve ''juniper.health.unm.edu'' ([Errno -3] Temporary failure
    in name resolution)"))'
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to TCRD data through Pharos
    for computational workflows and custom applications
  format: http
  id: tcrd.api
  is_public: true
  name: Pharos API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://pharos.nih.gov/api
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
- category: DocumentationProduct
  description: Comprehensive documentation describing TCRD data sources, schema structure,
    and usage guidelines
  format: http
  id: tcrd.documentation
  name: TCRD Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: http://juniper.health.unm.edu/tcrd/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-02: Error connecting
    to URL: HTTPConnectionPool(host=''juniper.health.unm.edu'', port=80): Max retries
    exceeded with url: /tcrd/ (Caused by NameResolutionError("HTTPConnection(host=''juniper.health.unm.edu'',
    port=80): Failed to resolve ''juniper.health.unm.edu'' ([Errno -3] Temporary failure
    in name resolution)"))'
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: GraphProduct
  description: IDG/TCRD compound-protein nodes used in ProKN
  format: csv
  id: prokn.idgp.compound.nodes
  name: ProKN TCRD Compound-Protein Compound Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 83991029
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGP.Compound.nodes.csv
- category: GraphProduct
  description: TCRD compound bioactivity to protein edges
  format: csv
  id: prokn.idgp.compound.bioactivity.protein.edges
  name: ProKN TCRD Compound-Protein Bioactivity Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 128158013
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGP.Compound.BIOACTIVITY.Protein.edges.csv
- category: GraphProduct
  description: IDG/TCRD compound-disease nodes used in ProKN
  format: csv
  id: prokn.idgd.compound.nodes
  name: ProKN TCRD Compound-Disease Compound Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 105796
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGD.Compound.nodes.csv
- category: GraphProduct
  description: TCRD compound indication edges to disease and phenotype terms
  format: csv
  id: prokn.idgd.compound.indication.diseaseorphenotype.edges
  name: ProKN TCRD Compound-Disease Indication Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1686928
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGD.Compound.INDICATION.DiseaseOrPhenotype.edges.csv
publications:
- id: https://doi.org/10.1093/nar/gkaa993
  title: 'Pharos 2021: mining the human proteome for disease biology'
- id: https://doi.org/10.1093/nar/gkw1072
  title: Illuminating the druggable genome with Pharos
repository: https://github.com/unmtransinfo/TCRD
synonyms:
- TCRD
- Target Central Resource Database
- IDG TCRD
taxon:
- NCBITaxon:9606
---
# Target Central Resource Database

## Overview

The Target Central Resource Database (TCRD) is the central data repository for the NIH Common Fund's Illuminating the Druggable Genome (IDG) program. It integrates data from 80+ sources to provide comprehensive annotations for human protein targets, with emphasis on understudied proteins in GPCRs, ion channels, kinases, and nuclear receptors.

## Information Resource ID

This resource has the Information Resource identifier: `infores:tcrd`