---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.wishartlab.com/
  label: Wishart Research Group, University of Alberta
creation_date: '2026-02-26T00:00:00Z'
description: PathBank is an interactive, visual pathway database that provides more
  than 600,000 machine-readable pathways across 10 model organisms. It supports metabolomics,
  transcriptomics, proteomics, and systems biology workflows through searchable pathway
  diagrams, pathway analysis tools, and downloads in tabular, image, sequence, and
  pathway-exchange formats.
domains:
- biological systems
- pathways
- systems biology
- biomedical
fairsharing_id: FAIRsharing.3xwMon
homepage_url: https://pathbank.org/
id: pathbank
last_modified_date: '2026-04-02T00:00:00Z'
layout: resource_detail
license:
  id: https://opendatacommons.org/licenses/odbl/1-0/
  label: ODbL-1.0
name: PathBank
products:
- category: GraphicalInterface
  description: Interactive web portal for browsing, searching, and analyzing PathBank
    pathways.
  format: http
  id: pathbank.portal
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: PathBank Portal
  original_source:
  - pathbank
  product_url: https://pathbank.org/
- category: Product
  compression: zip
  description: Download catalog for PathBank tabular pathway files, pathway exchange
    files, images, and sequence files.
  format: http
  id: pathbank.downloads
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: PathBank Downloads
  original_source:
  - pathbank
  product_url: https://pathbank.org/downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2026-04-07: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: CSV download of PathBank pathway subjects and descriptions from the
    official downloads page.
  format: csv
  id: pathbank.pathways.csv
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: PathBank Pathways CSV
  original_source:
  - pathbank
  product_url: https://pathbank.org/downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2026-04-07: Timeout connecting
    to URL'
- category: GraphProduct
  compression: zip
  description: BioPAX archive of PathBank pathway data from the official downloads
    page.
  format: biopax
  id: pathbank.biopax
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: PathBank BioPAX Archive
  original_source:
  - pathbank
  product_url: https://pathbank.org/downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2026-04-07: Timeout connecting
    to URL'
- category: GraphProduct
  compression: zip
  description: SBML archive of PathBank pathway models from the official downloads
    page.
  format: sbml
  id: pathbank.sbml
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: PathBank SBML Archive
  original_source:
  - pathbank
  product_url: https://pathbank.org/downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2026-04-07: Timeout connecting
    to URL'
- category: Product
  description: pathbank Nodes TSV
  format: tsv
  id: obo-db-ingest.pathbank.tsv
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: pathbank Nodes TSV
  original_source:
  - pathbank
  product_file_size: 727666
  product_url: https://w3id.org/biopragmatics/resources/pathbank/pathbank.tsv
  secondary_source:
  - obo-db-ingest
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Pathbank distributed via the NCATS Translator
    release site (release 2026_03_27; build pathbank_2019-09-13_4589e2d2_2025sep1_4.3.6;
    source version 2019-09-13; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 1465291
  format: kgx-jsonl
  id: translator.pathbank.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator PathBank KGX Graph
  node_count: 33443
  original_source:
  - pathbank
  product_url: https://kgx-storage.rtx.ai/releases/pathbank/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - pathbank_2019-09-13_4589e2d2_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - alliance
  - bgee
  - bindingdb
  - chembl
  - cohd
  - ctd
  - ctkp
  - drug-approvals-kp
  - dgidb
  - diseases
  - drugrephub
  - drugcentral
  - gtopdb
  - gene2phenotype
  - geneticskp
  - go-cam
  - goa
  - hp
  - icees-kg
  - intact
  - ncbigene
  - panther
  - pathbank
  - semmeddb
  - sider
  - signor
  - text-mining-kp
  - ttd
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - 423af7989cac
publications:
- doi: 10.1093/nar/gkad1041
  id: doi:10.1093/nar/gkad1041
  journal: Nucleic Acids Research
  preferred: true
  title: PathBank 2.0-the pathway database for model organism metabolomics
  year: '2024'
- doi: 10.1093/nar/gkz861
  id: doi:10.1093/nar/gkz861
  journal: Nucleic Acids Research
  title: 'PathBank: A Comprehensive Pathway Database for Model Organisms'
  year: '2020'
synonyms:
- PathBank 2.0
---
# PathBank

PathBank is a curated pathway database focused on model-organism biology and metabolomics.
According to the PathBank site, the current release contains more than 600,000 machine-readable
pathways and provides browsing, search, pathway enrichment, and download workflows for pathway,
compound, and protein data.

Official downloads include pathway tables plus BioPAX, SBGN, SBML, PWML, image, and sequence
exports. The 2024 PathBank 2.0 update in *Nucleic Acids Research* reports expansion from
110,234 to 605,359 total pathways and from 1,720 to 6,951 primary pathways.