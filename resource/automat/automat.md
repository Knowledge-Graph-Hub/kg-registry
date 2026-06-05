---
activity_status: active
category: Aggregator
collection:
  - translator
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: kebedey@renci.org
      - contact_type: github
        value: YaphetKG
    label: Yaphet Kebede
    orcid: 0000-0002-5046-0246
description: A Translator Knowledge Provider offering multiple sub-graphs in KGX format.
domains:
  - biomedical
homepage_url: https://robokop.renci.org/api-docs/docs/category/automat
id: automat
layout: resource_detail
license:
  id: https://biopragmatics.github.io/obo-db-ingest/
  label: Varies
name: Automat
products:
  - category: GraphProduct
    description: Robokop KG (Automat)
    format: kgx-jsonl
    id: automat.robokopkg
    name: robokopkg
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: robokop
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/RobokopKG/4901b2bc764444ea/
  - category: GraphProduct
    description: Robokop Plus
    format: kgx-jsonl
    id: automat.robokopplus
    name: robokopplus
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: robokop
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-3.1.2/RobokopPlus/ad8cb4d0a7ccc923/kgx_files/
  - category: GraphProduct
    description: Biolink Automat
    format: kgx-jsonl
    id: automat.biolink
    name: biolink_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: biolink
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-3.1.2/Biolink_Automat/329f8c92051c18d4/
  - category: GraphProduct
    description: CTD Automat
    format: kgx-jsonl
    id: automat.ctd
    infores_id: automat-ctd
    name: ctd_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/CTD_Automat/f92c663160ec5e36/
  - category: GraphProduct
    description: DrugCentral Automat
    format: kgx-jsonl
    id: automat.drugcentral
    infores_id: automat-drug-central
    name: drugcentral_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/DrugCentral_Automat/dec0617490b49c7a/
  - category: GraphProduct
    description: GTEx Automat
    format: kgx-jsonl
    id: automat.gtex
    infores_id: automat-gtex
    name: gtex_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/GTEx_Automat/a6448b9092bb81a1/
  - category: GraphProduct
    description: GtoPdb Automat
    format: kgx-jsonl
    id: automat.gtopdb
    infores_id: automat-gtopdb
    name: gtopdb_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/GtoPdb_Automat/0ea6074c824c2236/
  - category: GraphProduct
    description: GWASCatalog Automat
    format: kgx-jsonl
    id: automat.gwascatalog
    infores_id: automat-gwas-catalog
    name: gwascatalog_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/GWASCatalog_Automat/e30aceb322a33462/
  - category: GraphProduct
    description: Hetio Automat
    format: kgx-jsonl
    id: automat.hetio
    name: hetio_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: hetionet
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/Hetio_Automat/85a5f53e63150e1e/
  - category: GraphProduct
    description: HGNC Automat
    format: kgx-jsonl
    id: automat.hgnc
    infores_id: automat-hgnc
    name: hgnc_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/HGNC_Automat/dee31cfce74e5944/
  - category: GraphProduct
    description: HMDB Automat
    format: kgx-jsonl
    id: automat.hmdb
    infores_id: automat-hmdb
    name: hmdb_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/HMDB_Automat/6715124699b6dbf0/
  - category: GraphProduct
    description: HumanGOA Automat
    format: kgx-jsonl
    id: automat.humangoa
    infores_id: automat-human-goa
    name: humangoa_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/HumanGOA_Automat/06f107a4e9e8e547/
  - category: GraphProduct
    description: IntAct Automat
    format: kgx-jsonl
    id: automat.intact
    infores_id: automat-intact
    name: intact_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/IntAct_Automat/e5b936f966a02c2c/
  - category: GraphProduct
    description: PANTHER Automat
    format: kgx-jsonl
    id: automat.panther
    infores_id: automat-panther
    name: panther_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/PANTHER_Automat/c0189f14ba41da6c/
  - category: GraphProduct
    description: PHAROS Automat
    format: kgx-jsonl
    id: automat.pharos
    infores_id: automat-pharos
    name: pharos_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: pharos
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/PHAROS_Automat/d3068b509bf17ff3/
  - category: GraphProduct
    description: STRING-DB Automat
    format: kgx-jsonl
    id: automat.stringdb
    name: stringdb_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/STRING-DB_Automat/4ca5a0ce557e2c18/
  - category: GraphProduct
    description: UberGraph Automat
    format: kgx-jsonl
    id: automat.ubergraph
    name: ubergraph_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/UbergraphRedundant_Automat/e6b3204fd3a04413/
repository: https://github.com/RobokopU24/
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2025-10-29T00:00:00Z'
---

A Translator Knowledge Provider offering multiple sub-graphs in KGX format.
