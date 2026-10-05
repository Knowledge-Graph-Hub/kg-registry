---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biodatacatalyst.nhlbi.nih.gov/contact
  label: National Heart, Lung, and Blood Institute
creation_date: '2026-10-05T00:00:00Z'
description: NHLBI BioData Catalyst (BDC) is the cloud data ecosystem of the National
  Heart, Lung, and Blood Institute. It hosts more than 500 heart, lung, blood and sleep
  datasets (over 5 PB), including TOPMed whole-genome sequencing with linked phenotypes,
  RECOVER, HeartShare and National Sleep Research Resource studies, and links them to
  data discovery (PIC-SURE), a Gen3 data commons, cloud analysis workspaces (Seven Bridges
  and Terra) and the TOPMed Imputation Server. Most individual-level data are controlled
  access and require an eRA Commons login and an approved dbGaP data access request;
  a small set of open-access studies can be explored without authorization.
domains:
- biomedical
- genomics
- clinical
- precision medicine
- cardiovascular disease
homepage_url: https://biodatacatalyst.nhlbi.nih.gov/
id: biodata-catalyst
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: 1000genomes. Not accounted for, no known license:
    topmed.'
  id: https://www.internationalgenome.org/IGSR_disclaimer
  inferred_from:
  - 1000genomes
  label: IGSR Data Disclaimer / Terms of Use
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - topmed
name: NHLBI BioData Catalyst
products:
- category: GraphicalInterface
  description: BioData Catalyst portal, the entry point to the ecosystem's data catalog,
    data access instructions, analysis platforms and training resources.
  format: http
  id: biodata-catalyst.portal
  name: BioData Catalyst Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  - relation_type: prov:hadPrimarySource
    source: topmed
  product_url: https://biodatacatalyst.nhlbi.nih.gov/
- category: GraphicalInterface
  description: BDC PIC-SURE (Patient Information Commons Standard Unification of Research
    Elements) web interface for searching, filtering and exporting harmonized clinical
    and genomic variables across hosted studies. Open-access studies (such as 1000 Genomes
    and BioLINCC training data) need no authorization; authorized access to controlled
    studies requires an approved dbGaP data access request.
  format: http
  id: biodata-catalyst.picsure
  name: BDC PIC-SURE
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  product_url: https://picsure.biodatacatalyst.nhlbi.nih.gov/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: dbgap
- category: ProgrammingInterface
  description: PIC-SURE REST API for programmatic query and export of BDC study variables,
    used through the PicSureClient and PicSureBdcAdapter Python packages (and an R client)
    with a personal access token from the PIC-SURE interface.
  format: http
  id: biodata-catalyst.picsure-api
  is_public: false
  name: BDC PIC-SURE API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  - relation_type: prov:hadPrimarySource
    source: topmed
  product_url: https://picsure.biodatacatalyst.nhlbi.nih.gov/picsure/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: dbgap
  warnings:
  - API endpoint returned HTTP 401 Unauthorized for anonymous requests when checked
    on 2026-10-05; a PIC-SURE access token is required.
- category: GraphicalInterface
  description: BDC Gen3 data commons for browsing study metadata, checking authorized
    data access and exporting controlled-access TOPMed and other NHLBI study files to
    the analysis workspaces.
  format: http
  id: biodata-catalyst.gen3
  name: BDC Gen3 Data Commons
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  - relation_type: prov:hadPrimarySource
    source: topmed
  product_url: https://gen3.biodatacatalyst.nhlbi.nih.gov/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: dbgap
- category: ProcessProduct
  description: TOPMed Imputation Server, a web service that imputes missing genotypes
    in user-submitted GWAS data using the TOPMed haplotype reference panel.
  format: http
  id: biodata-catalyst.imputation-server
  name: TOPMed Imputation Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  - relation_type: prov:hadPrimarySource
    source: topmed
  product_url: https://imputation.biodatacatalyst.nhlbi.nih.gov/
- category: GraphicalInterface
  description: Cloud analysis workspaces available within BDC, the Seven Bridges BDC
    platform (https://platform.sb.biodatacatalyst.nhlbi.nih.gov/) and BDC Terra, where
    authorized users run workflows, notebooks and genomic tools on hosted data. Both
    require login.
  format: http
  id: biodata-catalyst.analysis-platforms
  name: BDC Analysis Platforms (Terra and Seven Bridges)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  - relation_type: prov:hadPrimarySource
    source: topmed
  product_url: https://terra.biodatacatalyst.nhlbi.nih.gov/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: dbgap
- category: DocumentationProduct
  description: BDC user documentation covering account setup, data access checks, PIC-SURE,
    Gen3, Seven Bridges, Terra and other ecosystem components.
  format: http
  id: biodata-catalyst.docs
  name: BioData Catalyst Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodata-catalyst
  product_url: https://bdcatalyst.gitbook.io/biodata-catalyst-documentation
publications:
- authors:
  - Stan Ahalt
  - Paul Avillach
  - Rebecca Boyles
  - Kira Bradford
  - Steven Cox
  - Brandi Davis-Dusenbery
  - Robert L Grossman
  - Ashok Krishnamurthy
  - Alisa Manning
  - Benedict Paten
  - Anthony Philippakis
  - Ingrid Borecki
  - Shu Hui Chen
  - Jon Kaltman
  - Sweta Ladwa
  - Chip Schwartz
  - Alastair Thomson
  - Sarah Davis
  - Alison Leaf
  - Jessica Lyons
  - Elizabeth Sheets
  - Joshua C Bis
  - Matthew Conomos
  - Alessandro Culotti
  - Thomas Desain
  - Jack Digiovanna
  - Milan Domazet
  - Stephanie Gogarten
  - Alba Gutierrez-Sacristan
  - Tim Harris
  - Ben Heavner
  - Deepti Jain
  - Brian O'Connor
  - Kevin Osborn
  - Danielle Pillion
  - Jacob Pleiness
  - Ken Rice
  - Garrett Rupp
  - Arnaud Serret-Larmande
  - Albert Smith
  - Jason P Stedman
  - Adrienne Stilp
  - Teresa Barsanti
  - John Cheadle
  - Christopher Erdmann
  - Brandy Farlow
  - Allie Gartland-Gray
  - Julie Hayes
  - Hannah Hiles
  - Paul Kerr
  - Chris Lenhardt
  - Tom Madden
  - Joanna O Mieczkowska
  - Amanda Miller
  - Patrick Patton
  - Marcie Rathbun
  - Stephanie Suber
  - Joe Asare
  doi: 10.1093/jamia/ocad048
  id: doi:10.1093/jamia/ocad048
  journal: Journal of the American Medical Informatics Association
  preferred: true
  title: Building a collaborative cloud platform to accelerate heart, lung, blood, and sleep research
  year: '2023'
synonyms:
- BDC
- BioData Catalyst
- NHLBI BDC
taxon:
- NCBITaxon:9606
---

# NHLBI BioData Catalyst

## Overview

NHLBI BioData Catalyst (BDC) is a cloud-based ecosystem in which researchers find, access,
share, store and compute on large heart, lung, blood and sleep (HLBS) datasets. It brings
together separately developed platforms under shared authentication and authorization.

## Data

- More than 500 datasets and over 5 PB of data, many multi-modal
- TOPMed whole-genome sequencing with linked clinical and omics data (over 100 datasets)
- RECOVER (Long COVID), HeartShare and National Sleep Research Resource studies
- Open-access studies (e.g. 1000 Genomes, BioLINCC training datasets) for exploration

## Components

- **PIC-SURE**: search and export of harmonized phenotype and genotype variables (web and API)
- **Gen3**: data commons for study metadata and authorized file access
- **Seven Bridges** and **Terra**: cloud analysis workspaces
- **TOPMed Imputation Server**: genotype imputation against the TOPMed reference panel

## Access

Most individual-level data are controlled access. Users sign in with an eRA Commons
account, and access to each study follows its approved dbGaP data access request and
data use limitations. No open license applies to hosted data.
