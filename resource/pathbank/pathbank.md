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
  - relation_type: prov:hadPrimarySource
    source: pathbank
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
  - relation_type: prov:hadPrimarySource
    source: pathbank
  product_url: https://pathbank.org/downloads
  warnings: []
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
  - relation_type: prov:hadPrimarySource
    source: pathbank
  product_url: https://pathbank.org/downloads
  warnings: []
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
  - relation_type: prov:hadPrimarySource
    source: pathbank
  product_url: https://pathbank.org/downloads
  warnings: []
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
  - relation_type: prov:hadPrimarySource
    source: pathbank
  product_url: https://pathbank.org/downloads
  warnings: []
- category: Product
  description: pathbank Nodes TSV
  format: tsv
  id: obo-db-ingest.pathbank.tsv
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: pathbank Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pathbank
  product_file_size: 727666
  product_url: https://w3id.org/biopragmatics/resources/pathbank/pathbank.tsv
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
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/pathbank/latest/
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
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: Product
  compression: gzip
  description: PC v14 integrated BioPAX Level 3 unified model containing normalized
    pathway data, molecular interactions, cross-database entity mappings, and metadata-derived
    content from 26 datasource rows.
  format: biopax
  id: pathwaycommons.biopax
  name: Integrated BioPAX Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 1700903742
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-biopax.owl.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: GraphicalInterface
  description: Public library of pathway diagrams that can be browsed, viewed, and
    used as templates for creating new pathways
  format: http
  id: pathwhiz.pathways
  name: PathWhiz Pathway Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwhiz
  product_url: https://pathbank.org/pathwhiz/pathways
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: drugbank
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pathbank
- category: Product
  description: Download directory for Pathway Commons PC v14 integrated pathway and
    molecular interaction datasets, including BioPAX, SIF, GMT, TXT, and JSON-LD products.
  format: mixed
  id: pathwaycommons.downloads
  name: Pathway Commons Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Simple Interaction Format network file representing binary pairwise
    molecular relationships integrated from Pathway Commons upstream datasource rows.
  format: sif
  id: pathwaycommons.sif
  name: SIF Network Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 9810179
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.sif.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Gene Matrix Transposed gene sets for pathway enrichment analysis,
    derived from the integrated Pathway Commons pathway archive.
  id: pathwaycommons.gmt
  name: GMT Gene Set Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 262513
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.gmt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 tab-delimited extended SIF node and edge file using HGNC-oriented
    identifiers for integrated Pathway Commons interactions.
  format: txt
  id: pathwaycommons.txt
  name: Extended SIF TXT Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 115608500
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
publications:
- authors:
  - David S Wishart
  - Ray Kruger
  - Aadhavya Sivakumaran
  - Karxena Harford
  - Selena Sanford
  - Rahil Doshi
  - Nitya Khetarpal
  - Omolola Fatokun
  - Daphnee Doucet
  - Ashley Zubkowski
  - Hayley Jackson
  - Gina Sykes
  - Miguel Ramirez-Gaona
  - Ana Marcu
  - Carin Li
  - Kristen Yee
  - Christiana Garros
  - Dorsa Yahya Rayat
  - Jeanne Coleongco
  - Tharuni Nandyala
  - Vasuk Gautam
  - Eponine Oler
  doi: 10.1093/nar/gkad1041
  id: doi:10.1093/nar/gkad1041
  journal: Nucleic Acids Research
  preferred: true
  title: PathBank 2.0-the pathway database for model organism metabolomics
  year: '2024'
- authors:
  - David S Wishart
  - Carin Li
  - Ana Marcu
  - Hasan Badran
  - Allison Pon
  - Zachary Budinski
  - Jonas Patron
  - Debra Lipton
  - Xuan Cao
  - Eponine Oler
  - Krissa Li
  - Maïlys Paccoud
  - Chelsea Hong
  - An C Guo
  - Christopher Chan
  - William Wei
  - Miguel Ramirez-Gaona
  doi: 10.1093/nar/gkz861
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