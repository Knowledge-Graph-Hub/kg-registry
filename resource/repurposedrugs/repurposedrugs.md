---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: url
    value: https://repurposedrugs.org/
  label: Ziaurrehman Tanoli
  orcid: 0000-0003-2435-9862
creation_date: '2026-11-24T00:00:00Z'
description: RepurposeDrugs is a web portal that combines a database of drug indications with
  a machine learning predictor of new drug-indication associations for approved and investigational
  single drugs and drug combinations. The published version covers 4,314 compounds and 161 drug
  combinations linked to 1,756 indications, for 28,148 drug-disease pairs.
domains:
- pharmacology
- drug discovery
- drug repositioning
- clinical
- clinical trials
funding:
- Academy of Finland (351507, 345803, 340141, 344698)
- European Union's Horizon Europe Research & Innovation (101057442, REMEDi4ALL)
- Sigrid Jusélius Foundation
- Cancer Society of Finland
- Norwegian Health Authority South-East (2020026)
homepage_url: https://repurposedrugs.org/
id: repurposedrugs
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
name: RepurposeDrugs
products:
- category: GraphicalInterface
  description: Interactive portal for browsing drug indications, treatment status, and clinical
    trials, and for predicting approval likelihood of drug-indication pairs.
  format: http
  id: repurposedrugs.portal
  name: RepurposeDrugs Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repurposedrugs
  product_url: https://repurposedrugs.org/
- category: GraphProduct
  compression: targz
  description: Zenodo archive with the PrimeKG-Plus graph (primekg_plus.csv; 129,317
    nodes and 7,683,206 directed edges), the literature-augmented PrimeKG-Plus-RD
    graph (primekg_plus_rd.csv; 129,353 nodes and 7,683,756 directed edges), a copy
    of the original PrimeKG, supplementary tables, curation inputs, and rebuild scripts.
    Counts on this product are for primekg_plus.csv.
  edge_count: 7683206
  format: mixed
  id: primekg-plus.bundle
  latest_version: '1.0'
  name: PrimeKG-Plus Release Bundle
  node_count: 129317
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg-plus
  - relation_type: prov:hadPrimarySource
    source: primekg
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: nsides
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repurposedrugs
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 596295144
  product_url: https://zenodo.org/records/20796545/files/zenodo_bundle.tar.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: pmc
publications:
- authors:
  - Aleksandr Ianevski
  - Aleksandr Kushnir
  - Kristen Nader
  - Mitro Miihkinen
  - Henri Xhaard
  - Tero Aittokallio
  - Ziaurrehman Tanoli
  doi: 10.1093/bib/bbae328
  id: doi:10.1093/bib/bbae328
  journal: Briefings in Bioinformatics
  preferred: true
  title: 'RepurposeDrugs: an interactive web-portal and predictive platform for repurposing
    mono- and combination therapies'
  year: '2024'
synonyms:
- RepoDrug
---

# RepurposeDrugs

RepurposeDrugs brings together approved and failed drug indications and uses them to predict which new
drug-disease pairs are likely to be approved. It is one of the sources of `primekg-plus`.
