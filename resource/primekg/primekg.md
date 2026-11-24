---
activity_status: active
category: KnowledgeGraph
collection:
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: marinka@hms.harvard.edu
  - contact_type: github
    value: marinkaz
  label: Marinka Zitnik
  orcid: 0000-0001-8530-7228
creation_date: '2025-03-09T00:00:00Z'
description: PrimeKG (Precision Medicine Knowledge Graph) integrates 20 high-quality
  biomedical resources to describe 17,080 diseases with over 4 million relationships
  across ten major biological scales.
domains:
- biomedical
- precision medicine
- pathways
- systems biology
homepage_url: https://zitniklab.hms.harvard.edu/projects/PrimeKG
id: primekg
infores_id: primekg
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0 (dataset on Harvard Dataverse); source-specific licenses apply; MIT
    License (code)
name: PrimeKG
products:
- category: GraphProduct
  description: The full PrimeKG edge list (kg.csv), with 4,050,249 undirected relationships.
    The node count is taken from the released node table.
  edge_count: 4050249
  format: csv
  id: primekg.graph
  latest_version: '2.1'
  name: PrimeKG Full Dataset
  node_count: 129375
  original_source:
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
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 981751236
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180620
- category: GraphProduct
  description: PrimeKG node table. Version 2.1 on Harvard Dataverse.
  format: tsv
  id: primekg.nodes
  latest_version: '2.1'
  name: PrimeKG Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  product_file_size: 8893757
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180617
- category: GraphProduct
  description: PrimeKG edge table. Version 2.1 on Harvard Dataverse.
  format: csv
  id: primekg.edges
  latest_version: '2.1'
  name: PrimeKG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  product_file_size: 386582390
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180616
- category: Product
  description: Text descriptions of diseases, including clinical descriptors from
    sources such as Mayo Clinic and Orphanet. Version 2.1 on Harvard Dataverse.
  format: tsv
  id: primekg.disease-features
  latest_version: '2.1'
  name: PrimeKG Disease Features
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_file_size: 113534270
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180618
- category: Product
  description: Text descriptions of drugs, including descriptors from DrugBank. Version
    2.1 on Harvard Dataverse.
  format: tsv
  id: primekg.drug-features
  latest_version: '2.1'
  name: PrimeKG Drug Features
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  - relation_type: prov:hadPrimarySource
    source: drugbank
  product_file_size: 10030011
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180619
- category: Product
  description: Harvard Dataverse dataset holding all PrimeKG release files, including
    raw, grouped, and giant-component versions of the graph.
  format: mixed
  id: primekg.dataverse
  name: PrimeKG on Harvard Dataverse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  product_url: https://doi.org/10.7910/DVN/IXA7BM
  warnings:
  - 'File was not able to be retrieved when checked on 2026-11-24: HTTP 202 error
    when accessing file'
- category: ProcessProduct
  description: Scripts and notebooks for building PrimeKG, with updates in July and
    December 2023 for newer source releases and fuller OMIM coverage.
  format: python
  id: primekg.code
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT License
  name: PrimeKG Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  product_url: https://github.com/mims-harvard/PrimeKG
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
  - Payal Chandak
  - Kexin Huang
  - Marinka Zitnik
  doi: 10.1038/s41597-023-01960-3
  id: doi:10.1038/s41597-023-01960-3
  journal: Scientific Data
  preferred: true
  title: Building a knowledge graph to enable precision medicine
  year: '2023'
repository: https://github.com/mims-harvard/PrimeKG
taxon:
- NCBITaxon:9606
warnings:
- The PrimeKG authors state that PrimeKG has been superseded by OptimusKG and recommend
  using OptimusKG in almost every case. The files on Harvard Dataverse have not changed
  since 2022.
---
### PrimeKG: A Knowledge Graph for Precision Medicine

PrimeKG is a large-scale Precision Medicine Knowledge Graph that provides a holistic view of diseases by integrating 20 high-quality biomedical resources. It describes 17,080 diseases with over 4 million relationships, enabling advanced network medicine and machine learning applications.

The authors now recommend [OptimusKG](https://optimuskg.ai) (`optimuskg`), which supersedes PrimeKG.
[PrimeKG-Plus](https://github.com/DSDD-UCPH/PrimeKG-Plus) (`primekg-plus`) is a separate
PrimeKG-compatible rebuild from newer source releases by another group.

## Evaluation

- View the evaluation: [primekg evaluation](primekg_eval.html)