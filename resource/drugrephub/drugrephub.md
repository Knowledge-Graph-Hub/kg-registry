---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/center-development-therapeutics-cdot
  id: broad-cdot
  label: Broad Institute Center for the Development of Therapeutics (CDoT)
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/
  id: broad-institute
  label: Broad Institute
creation_date: '2026-01-22T00:00:00Z'
description: Curated collection of approved, clinical, and pre-clinical compounds
  with detailed annotations and sample metadata to support drug repurposing screens
  and analyses.
domains:
- drug discovery
- pharmacology
- biomedical
homepage_url: https://repo-hub.broadinstitute.org/repurposing
id: drugrephub
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Drug Repurposing Hub
products:
- category: Product
  description: Latest drug-level annotations including compound names, clinical phase,
    mechanism of action, and protein targets (listed as version 2025-08-19 on the
    site).
  format: tsv
  id: drugrephub.drug-info.tsv
  name: Drug Repurposing Hub Drug Information TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  product_file_size: 661900
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-drug-annotation-20200324.txt
  warnings:
  - 'File was not able to be retrieved with default certificate verification when
    checked on 2026-06-01: SSL certificate verification failed; file responded with
    HTTP 200 when checked without local certificate verification'
- category: Product
  description: Latest physical sample-level metadata including Broad sample IDs, vendor
    catalog numbers, SMILES, InChIKey, and PubChem IDs (listed as version 2025-08-19
    on the site).
  format: tsv
  id: drugrephub.sample-info.tsv
  name: Drug Repurposing Hub Sample Information TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  product_file_size: 4072927
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-sample-annotation-20240610.txt
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubchem
  warnings:
  - 'File was not able to be retrieved with default certificate verification when
    checked on 2026-06-01: SSL certificate verification failed; file responded with
    HTTP 200 when checked without local certificate verification'
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Drug Repurposing Hub distributed via the
    NCATS Translator release site (release 2026_03_06; build drug_rep_hub_2025-08-19_99c18ef1_2025sep1_4.3.6;
    source version 2025-08-19; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 19389
  format: kgx-jsonl
  id: translator.drug_rep_hub.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Drug Repurposing Hub KGX Graph
  node_count: 8842
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/drug_rep_hub/latest/
  versions:
  - '2026_03_06'
  - drug_rep_hub_2025-08-19_99c18ef1_2025sep1_4.3.6
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
publications:
- authors:
  - Steven M Corsello
  - Joshua A Bittker
  - Zihan Liu
  - Joshua Gould
  - Patrick McCarren
  - Jodi E Hirschman
  - Stephen E Johnston
  - Anita Vrcic
  - Bang Wong
  - Mariya Khan
  - Jacob Asiedu
  - Rajiv Narayan
  - Christopher C Mader
  - Aravind Subramanian
  - Todd R Golub
  doi: 10.1038/nm.4306
  id: doi:10.1038/nm.4306
  journal: Nature Medicine
  preferred: true
  title: 'The Drug Repurposing Hub: a next-generation drug library and information
    resource'
  year: '2017'
---
Drug Repurposing Hub is a curated, annotated library of approved, clinical, and pre-clinical compounds for screening and repurposing research.
