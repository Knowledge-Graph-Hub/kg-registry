---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: trung.trinh@sund.ku.dk
  label: Trinh Trung Duong Nguyen
  orcid: 0000-0001-5793-649X
- category: Individual
  contact_details:
  - contact_type: email
    value: albert.kooistra@sund.ku.dk
  label: Albert J. Kooistra
  orcid: 0000-0001-5514-6021
creation_date: '2026-11-24T00:00:00Z'
description: PrimeKG-Plus is an updated, PrimeKG-compatible precision medicine knowledge graph.
  It rebuilds the 20 original PrimeKG sources from releases available as of December 2025, adds
  Open Targets, RepurposeDrugs, and nSIDES, and includes a version with expert-validated literature
  relations for Canavan disease, Batten disease, Niemann-Pick disease type C, and Tay-Sachs
  disease.
domains:
- biomedical
- precision medicine
- rare disease
- drug discovery
- drug repositioning
funding:
- Lundbeck Foundation (R449-2023-1394)
homepage_url: https://github.com/DSDD-UCPH/PrimeKG-Plus
id: primekg-plus
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0 (Zenodo release); source-specific licenses apply; MIT License (code)
name: PrimeKG-Plus
products:
- category: GraphProduct
  compression: targz
  description: Zenodo archive with the PrimeKG-Plus graph (primekg_plus.csv; 129,317 nodes and
    7,683,206 directed edges), the literature-augmented PrimeKG-Plus-RD graph (primekg_plus_rd.csv;
    129,353 nodes and 7,683,756 directed edges), a copy of the original PrimeKG, supplementary
    tables, curation inputs, and rebuild scripts. Counts on this product are for primekg_plus.csv.
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
- category: Product
  description: Zenodo record for the PrimeKG-Plus release.
  format: http
  id: primekg-plus.zenodo
  latest_version: '1.0'
  name: PrimeKG-Plus on Zenodo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg-plus
  product_url: https://zenodo.org/records/20796545
- category: ProcessProduct
  description: Scripts and notebooks for preparing sources, building the graph, and integrating
    literature-derived relations.
  format: python
  id: primekg-plus.code
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT License
  name: PrimeKG-Plus Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg-plus
  product_url: https://github.com/DSDD-UCPH/PrimeKG-Plus
publications:
- authors:
  - Trinh Trung Duong Nguyen
  - Thuy Nguyen-Phuong
  - Quy-Hoai Nguyen
  - Amna Mumtaz Abbasi
  - Hanh-Dung Le Phan
  - Luong Bao-Anh Nguyen
  - Nhat-Thien Phan
  - Nurettin Nusret Curabaz
  - Alexander S. Hauser
  - Ziaurrehman Tanoli
  - Dinh Truong Nguyen
  - Albert J. Kooistra
  doi: 10.64898/2026.07.14.738415
  id: doi:10.64898/2026.07.14.738415
  journal: bioRxiv
  preferred: true
  title: 'PrimeKG-Plus: a refreshed and rare-disease-enriched precision medicine knowledge graph'
  year: '2026'
repository: https://github.com/DSDD-UCPH/PrimeKG-Plus
synonyms:
- PrimeKG Plus
taxon:
- NCBITaxon:9606
version: '1.0'
warnings:
- The manuscript describing PrimeKG-Plus is a preprint that the authors report is under revision
  after peer review.
---

# PrimeKG-Plus

PrimeKG-Plus is an independent rebuild of `primekg` led from the University of Copenhagen. It is
not produced by the original PrimeKG authors, whose own successor to PrimeKG is `optimuskg`.

The literature layer comes from 637 PubMed abstracts and PubMed Central articles on four rare
neurological disorders, with language-model-assisted extraction and expert review. It adds 550 novel
edges to the graph built from databases alone. The DisGeNET data comes by way of the PrimeKG authors.

The Zenodo record gives CC BY 4.0, while the GitHub README gives CC0 1.0 for the data, with upstream
databases keeping their own licenses.
