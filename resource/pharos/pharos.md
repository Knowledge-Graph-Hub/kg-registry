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
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: Pharos
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing, and analyzing protein target
    information with advanced filtering, visualizations, and data export capabilities
    across the druggable genome
  format: http
  id: pharos.portal
  name: Pharos Web Portal
  product_url: https://pharos.nih.gov/
- category: Product
  description: Target Central Resource Database (TCRD) downloadable database files
    containing comprehensive protein target information including druggability classifications,
    expression data, disease associations, and chemical probe information
  id: pharos.tcrd.download
  name: TCRD Database Downloads
  product_url: http://juniper.health.unm.edu/tcrd/download/
  warnings:
  - File was not able to be retrieved when checked on 2026-02-15_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-02-18: Timeout connecting
    to URL'
- category: ProgrammingInterface
  description: GraphQL API for programmatic access to Pharos and TCRD data enabling
    custom queries and integrations
  format: http
  id: pharos.api
  name: Pharos GraphQL API
  product_url: https://pharos.nih.gov/api
- category: DocumentationProduct
  description: API documentation and usage examples for the Pharos GraphQL interface
  format: http
  id: pharos.api.docs
  name: Pharos API Documentation
  product_url: https://pharos.nih.gov/api-docs
  warnings:
  - File was not able to be retrieved when checked on 2026-02-15_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-18: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: PHAROS Automat
  format: kgx-jsonl
  id: automat.pharos
  infores_id: automat-pharos
  name: pharos_automat
  original_source:
  - pharos
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/PHAROS_Automat/d3068b509bf17ff3/
  secondary_source:
  - automat
- category: DocumentationProduct
  description: Comprehensive documentation covering Pharos features, TCRD data structure,
    Target Development Levels, and data provenance
  format: http
  id: pharos.docs
  name: Pharos Documentation
  product_url: https://pharos.nih.gov/about
  warnings:
  - File was not able to be retrieved when checked on 2026-02-15_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-18: HTTP 403 error
    when accessing file'
publications:
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
  doi: 10.1093/nar/gkaa993
  id: https://doi.org/10.1093/nar/gkaa993
  journal: Nucleic Acids Research
  preferred: true
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
  id: https://doi.org/10.1093/nar/gkaa993
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
---
