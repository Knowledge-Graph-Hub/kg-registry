---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pharos@mail.nih.gov
  - contact_type: url
    value: https://pharos.nih.gov/about
  label: NIH NCATS IDG Program
creation_date: '2025-10-31T00:00:00Z'
description: Pharos is the user interface to the Target Central Resource Database
  (TCRD), providing comprehensive information about protein targets with a focus on
  the druggable genome. Developed by the NIH Illuminating the Druggable Genome (IDG)
  program, Pharos classifies targets into four Target Development Levels (TDLs) -
  Tclin (targets with approved drugs), Tchem (targets with high-quality chemical probes),
  Tbio (targets with biological data), and Tdark (understudied targets with little
  functional knowledge). The platform integrates data from over 80 datasets covering
  protein structure, function, pathways, expression, diseases, drugs, ligands, and
  publications.
domains:
- drug discovery
- proteomics
- pharmacology
- health
- biomedical
homepage_url: https://pharos.nih.gov/
id: pharos
infores_id: pharos
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Pharos
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing, and analyzing protein target
    information with advanced filtering, visualizations, and data export capabilities
    across the druggable genome
  format: http
  id: pharos.portal
  name: Pharos Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://pharos.nih.gov/
- category: Product
  description: Target Central Resource Database (TCRD) downloadable database files
    containing comprehensive protein target information including druggability classifications,
    expression data, disease associations, and chemical probe information
  format: http
  id: pharos.tcrd.download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://opendata.ncats.nih.gov/public/pharos/
  warnings:
  - The Pharos footer still links the historical Juniper TCRD download host, but the
    about page points Pharos data downloads to NCATS OpenData; the registry uses the
    NCATS OpenData URL.
- category: ProgrammingInterface
  description: GraphQL API for programmatic access to Pharos and TCRD data enabling
    custom queries and integrations
  format: http
  id: pharos.api
  name: Pharos GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://pharos.nih.gov/graphql
- category: DocumentationProduct
  description: API documentation and usage examples for the Pharos GraphQL interface
  format: http
  id: pharos.api.docs
  name: Pharos API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://pharos.nih.gov/api-docs
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: PHAROS Automat
  format: kgx-jsonl
  id: automat.pharos
  infores_id: automat-pharos
  name: pharos_automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/PHAROS_Automat/d3068b509bf17ff3/
- category: DocumentationProduct
  description: Comprehensive documentation covering Pharos features, TCRD data structure,
    Target Development Levels, and data provenance
  format: http
  id: pharos.docs
  name: Pharos Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://pharos.nih.gov/about
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
- category: ProcessProduct
  description: Source repository for the Pharos web frontend maintained by NCATS
  format: http
  id: pharos.frontend_source
  license:
    id: https://opensource.org/license/mit
    label: MIT
  name: Pharos Frontend Source
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://github.com/ncats/pharos_frontend
  repository: https://github.com/ncats/pharos_frontend
- category: ProcessProduct
  description: Source repository for the Pharos GraphQL server referenced by the Pharos
    about page
  format: http
  id: pharos.graphql_server_source
  name: Pharos GraphQL Server Source
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  product_url: https://github.com/ncats/pharos-graphql-server
  repository: https://github.com/ncats/pharos-graphql-server
publications:
- authors:
  - Kelleher K
  - Sheils T
  - Mathias S
  - Yang JJ
  - Metzger VT
  - Siramshetty VB
  - Nguyen DT
  - Jensen LJ
  - Vidović D
  - Schürer SC
  - Holmes J
  - Sharma A
  - Pillai A
  - Bologa CG
  - Edwards L
  - Mathé E
  - Oprea TI
  doi: 10.1093/nar/gkac1033
  id: doi:10.1093/nar/gkac1033
  journal: Nucleic Acids Research
  preferred: true
  title: 'Pharos 2023: an integrated resource for the understudied human proteome'
  year: '2023'
- authors:
  - Nguyen DT
  - Mathias S
  - Bologa C
  - Brunak S
  - Fernandez N
  - Gaulton A
  - Hersey A
  - Holmes J
  - Jensen LJ
  - Karlsson A
  - Liu G
  - Ma'ayan A
  - Mandava G
  - Mani S
  - Mehta S
  - Overington J
  - Patel J
  - Rouillard AD
  - Schürer S
  - Sheils T
  - Simeonov A
  - Sklar LA
  - Southall N
  - Ursu O
  - Vidovic D
  - Waller A
  - Yang J
  - Jadhav A
  - Oprea TI
  - Guha R
  doi: 10.1093/nar/gkw1072
  id: doi:10.1093/nar/gkw1072
  journal: Nucleic Acids Research
  title: 'Pharos: Collating protein information to shed light on the druggable genome'
  year: '2017'
- authors:
  - Sheils TK
  - Mathias SL
  - Kelleher KJ
  - Siramshetty VB
  - Nguyen DT
  - Bologa CG
  - Jensen LJ
  - Vidović D
  - Koleti A
  - Schürer SC
  - Waller A
  - Yang JJ
  - Holmes J
  - Bocci G
  - Southall N
  - Dharuri H
  - Mathé E
  - Simeonov A
  - Oprea TI
  doi: 10.1093/nar/gkaa993
  id: doi:10.1093/nar/gkaa993
  journal: Nucleic Acids Research
  title: 'TCRD and Pharos 2021: mining the human proteome for disease biology'
  year: '2021'
repository: https://github.com/ncats/pharos_frontend
synonyms:
- Pharos
- TCRD
- Target Central Resource Database
- IDG Pharos
taxon:
- NCBITaxon:9606
version: Pharos 3.19.10; TCRD 6.13.5
warnings:
- The Pharos about page states data are publicly available from primary sources and
  asks users to respect individual source licenses; no single data license is asserted
  for all Pharos/TCRD content.
---
