---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://sennetconsortium.org/
  label: SenNet Consortium
creation_date: '2025-11-05T00:00:00Z'
description: The Cellular Senescence Network (SenNet) is an NIH Common Fund program
  that aims to comprehensively identify and characterize senescent cells across the
  human lifespan and in various disease states. SenNet provides spatial molecular
  maps of senescent cells in tissues, developing and applying cutting-edge technologies
  for detecting cellular senescence. The consortium generates multi-omics data, imaging
  data, and develops computational tools to advance understanding of how senescent
  cells contribute to aging and age-related diseases.
domains:
- biomedical
- anatomy and development
- genomics
- precision medicine
homepage_url: https://sennetconsortium.org/
id: sennet
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: SenNet
products:
- category: GraphicalInterface
  description: Data portal for browsing and accessing SenNet datasets
  format: http
  id: sennet.portal
  name: SenNet Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sennet
  product_url: https://data.sennetconsortium.org/
- category: Product
  description: Multi-omics datasets of senescent cells
  format: mixed
  id: sennet.data
  name: SenNet Multi-Omics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sennet
  product_url: https://data.sennetconsortium.org/
- category: ProgrammingInterface
  description: API for programmatic access to SenNet data
  format: http
  id: sennet.api
  name: SenNet API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sennet
  product_url: https://sennetconsortium.org/
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
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
- category: GraphProduct
  description: Statistically inferred genomic evidence graph connecting genes, gene
    sets, inferred disease mechanisms, and human phenotypes. Gene sets are derived
    from eleven NIH Common Fund programs (GlyGen, GTEx, IDG, IMPC/KOMP2, LINCS, MoTrPAC,
    Bridge2AI, HuBMAP, Metabolomics Workbench, SenNet, and SPARC) and phenotype-gene
    set relationships are computed with PIGEAN (Priors Inferred from GEne ANnotations).
  format: http
  id: digcfdekg.graph
  name: CFDE REVEAL Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: digcfdekg
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: bridge2ai
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: sparc
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hubmap
publications:
- authors:
  - SenNet Consortium
  - Lee PJ
  - Benz CC
  - Blood P
  - "B\xF6rner K"
  - Campisi J
  - Chen F
  - Daldrup-Link H
  - De Jager P
  - Ding L
  - Duncan FE
  - Eickelberg O
  - Fan R
  - Finkel T
  - Furman D
  doi: 10.1038/s43587-022-00326-5
  id: https://www.ncbi.nlm.nih.gov/pubmed/36936385
  journal: Nat Aging
  preferred: true
  title: NIH SenNet Consortium to map senescent cells throughout the human lifespan
    to understand physiological health
  year: '2022'
synonyms:
- SenNet
- Cellular Senescence Network
taxon:
- NCBITaxon:9606
---
# SenNet - Cellular Senescence Network

## Overview

The Cellular Senescence Network (SenNet) is an NIH Common Fund program that aims to comprehensively identify and characterize senescent cells across the human lifespan and in various disease states.

Launched in 2021, SenNet develops and applies cutting-edge technologies to create spatial molecular maps of senescent cells in human tissues, advancing understanding of how these cells contribute to aging and age-related diseases.

## Key Features

- **Senescence Biomarkers**: Development and validation of markers for detecting senescent cells
- **Multi-Omics Profiling**: Genomics, transcriptomics, proteomics, and metabolomics of senescent cells
- **Spatial Mapping**: Tissue-level spatial distribution of senescent cells
- **Technology Development**: Novel methods for senescence detection and characterization
- **Public Data**: Open access to datasets, protocols, and analysis tools
- **Cross-Tissue Studies**: Comprehensive mapping across multiple human tissues

## Research Applications

- Aging biology research
- Age-related disease mechanisms
- Therapeutic target identification
- Senolytic drug development
- Biomarker discovery
- Understanding tissue-specific aging

## Products

### SenNet Data Portal
Web-based portal for exploring, visualizing, and downloading SenNet datasets including imaging, omics, and metadata.

### SenNet Multi-Omics Data
Comprehensive molecular datasets characterizing senescent cells across tissues and conditions, including transcriptomics, proteomics, and metabolomics.

### SenNet API
Programmatic interface for accessing SenNet data and integrating with computational workflows.

## Information Resource ID

This resource has the Information Resource identifier: `infores:sennet`

## Domains

- Health
- Biomedical
- Anatomy and Development
- Genomics
- Precision Medicine

## Taxon Coverage

Human (NCBITaxon:9606)