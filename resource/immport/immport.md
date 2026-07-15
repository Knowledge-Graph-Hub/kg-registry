---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://immport.niaid.nih.gov/home
  label: ImmPort
creation_date: '2026-07-02T00:00:00Z'
description: ImmPort (the Immunology Database and Analysis Portal) is a long-term,
  sustainable data repository funded by the NIAID Division of Allergy, Immunology,
  and Transplantation. It archives and freely distributes immunology research data
  from NIAID-funded clinical and mechanistic studies, including flow cytometry, gene
  expression, HLA typing, ELISA, and clinical trial data. ImmPort is one of the NIAID-sponsored
  repositories whose dataset metadata is harvested and indexed by the NIAID Data Ecosystem
  Discovery Portal.
domains:
- biomedical
- clinical
- immunology
homepage_url: https://immport.niaid.nih.gov/home
id: immport
last_modified_date: '2026-07-14T00:00:00Z'
layout: resource_detail
license:
  id: https://docs.immport.org/home/agreement/
  label: ImmPort User Agreement (custom data use agreement)
name: ImmPort
products:
- category: DataSource
  description: Web portal for searching, browsing, and downloading immunology research
    datasets shared through ImmPort.
  format: http
  id: immport.portal
  name: ImmPort Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: immport
  product_url: https://immport.niaid.nih.gov/home
- category: GraphicalInterface
  description: The ImmPort Shared Data browser (Updated Data Browser) for searching
    and browsing shared studies and downloading data as single files, download-cart
    ZIP archives, or complete study (ALL_DATA) packages.
  format: http
  id: immport.databrowser
  name: ImmPort Shared Data Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: immport
  product_url: https://www.immport.org/shared
- category: ProgrammingInterface
  description: The ImmPort Shared Data API, a REST API providing programmatic access
    to study manifests and file downloads. Requires a free ImmPort API key.
  format: http
  id: immport.api
  is_public: true
  name: ImmPort Shared Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: immport
  product_url: https://immport.org/data/query/swagger-ui/index.html
- category: ProgrammingInterface
  connection_url: drs.immport.org/ga4gh/drs/v1/
  description: The ImmPort GA4GH Data Repository Service (DRS) API, which resolves
    logical file identifiers to physical download URLs (S3 signed URLs or streaming
    URLs). Requires a free ImmPort API key.
  format: http
  id: immport.drs
  is_public: true
  name: ImmPort GA4GH DRS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: immport
  product_url: https://drs.immport.org/ga4gh/drs/v1/
- category: Product
  description: The ImmPort Download Client, a cross-platform (Linux, macOS, Windows)
    command-line tool that batch-downloads files from a manifest using GA4GH DRS standard
    transfer methods. Requires a free ImmPort API key.
  id: immport.download-client
  name: ImmPort Download Client
  original_source:
  - relation_type: prov:hadPrimarySource
    source: immport
  product_file_size: 0
  product_url: https://downloads.immport.org/immport-download-client/
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
  - Sanchita Bhattacharya
  - Patrick Dunn
  - Cristel G. Thomas
  - Barry Smith
  - Henry Schaefer
  - Jieming Chen
  - Zicheng Hu
  - Kelly A. Zalocusky
  - Ravi D. Shankar
  - Shai S. Shen-Orr
  - Elizabeth Thomson
  - Jeffrey Wiser
  - Atul J. Butte
  doi: 10.1038/sdata.2018.15
  id: https://www.ncbi.nlm.nih.gov/pubmed/29485622
  journal: Scientific Data
  preferred: true
  title: ImmPort, toward repurposing of open access immunological assay data for translational
    and clinical research
  year: '2018'
repository: https://github.com/ImmPortDB
taxon:
- NCBITaxon:9606
---
ImmPort

## Description

ImmPort (the Immunology Database and Analysis Portal) is a NIAID-sponsored data
repository that archives and shares immunology research data from NIAID-funded
clinical and mechanistic studies. It is one of the source repositories harvested by
the NIAID Data Ecosystem Discovery Portal.