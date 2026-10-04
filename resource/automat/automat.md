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
description: A RENCI service that proxies Plater-based TRAPI endpoints for individual knowledge graphs (such as the ROBOKOP KG, Ubergraph, CAM-KP and COHD) and publishes per-source knowledge graphs, built with ORION, as KGX downloads. Part of NCATS Biomedical Data Translator.
domains:
  - biomedical
homepage_url: https://robokop.renci.org/api-docs/docs/category/automat
id: automat
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License (software; graph data carries the licenses of its sources)
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
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: drugmechdb
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: hetionet
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: monarchinitiative
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pharos
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: text-mining-kp
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/RobokopKG/4901b2bc764444ea/
  - category: GraphProduct
    description: 'Robokop Plus: the ROBOKOP KG extended with CORD-19 and text-mined assertions (2023 data, Biolink 3.1.2; legacy).'
    format: kgx-jsonl
    id: automat.robokopplus
    name: robokopplus
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: robokop
        relation_type: prov:hadPrimarySource
      - source: cord-19
        relation_type: prov:hadPrimarySource
      - source: text-mining-kp
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-3.1.2/RobokopPlus/ad8cb4d0a7ccc923/kgx_files/
  - category: GraphProduct
    description: 'Biolink Automat: graph based on the Monarch API, from the SRI Reference KG (2021 data, Biolink 3.1.2; legacy).'
    format: kgx-jsonl
    id: automat.biolink
    name: biolink_automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
      - source: monarchinitiative
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
  - category: GraphProduct
    description: 'BindingDB Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.binding
    name: BINDING_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/BINDING_Automat/
  - category: GraphProduct
    description: 'CAM-KP Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.camkp
    name: CAMKP_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: cam-kp
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/CAMKP_Automat/
  - category: GraphProduct
    description: 'COHD Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.cohd
    name: COHD_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: cohd
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/COHD_Automat/
  - category: GraphProduct
    description: 'Clinical Trials KP Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.ctkp
    name: CTKP_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: ctkp
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/CTKP_Automat/
  - category: GraphProduct
    description: 'EHR Clinical Connections Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.ehr-clinical-connections
    name: EHR_Clinical_Connections_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: multiomics-kp
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/EHR_Clinical_Connections_Automat/
  - category: GraphProduct
    description: 'EHR May Treat KP Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.maytreatkp
    name: MayTreatKP_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: multiomics-kp
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/MayTreatKP_Automat/
  - category: GraphProduct
    description: 'Alliance of Genome Resources Orthologs Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.alliance-orthologs
    name: GenomeAllianceOrthologs_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/GenomeAllianceOrthologs_Automat/
  - category: GraphProduct
    description: 'MolePro Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.molepro
    name: MolePro_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: molepro
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/MolePro_Automat/
  - category: GraphProduct
    description: 'Reactome Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.reactome
    name: Reactome_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/Reactome_Automat/
  - category: GraphProduct
    description: 'Text Mining KP Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.tmkp
    name: TMKP_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: text-mining-kp
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/TMKP_Automat/
  - category: GraphProduct
    description: 'Viral Proteome Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.viralproteome
    name: ViralProteome_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/ViralProteome_Automat/
  - category: GraphProduct
    description: 'CEBS Automat: per-source KGX knowledge graph download (Biolink 4.2.6).'
    format: kgx-jsonl
    id: automat.cebs
    name: CEBS_Automat
    original_source:
      - source: automat
        relation_type: prov:hadPrimarySource
      - source: cebs
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:wasInformedBy
    product_url: https://stars.renci.org/var/plater/bl-4.2.6/CEBS_Automat/
repository: https://github.com/RENCI-AUTOMAT/automat-server
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-10-04T00:00:00Z'
---

A Translator Knowledge Provider offering multiple sub-graphs in KGX format.
