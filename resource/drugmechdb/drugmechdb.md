---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://sulab.org/
  label: Su Lab
creation_date: '2025-08-12T00:00:00Z'
description: DrugMechDB is a curated database that captures mechanistic paths from
  a drug to a disease within a given indication. Expert curators normalize concepts
  and relationships to standard biomedical identifiers and represent each indication
  as a directed path through a biological knowledge graph, suitable for computational
  analysis and benchmarking. Release 2.0.1 contains 4,846 curated paths covering 4,664
  drug-disease indications, with 32,641 edges. Indications were sampled from DrugCentral,
  and paths were derived from descriptions in DrugBank, Wikipedia and the literature.
domains:
- biomedical
- pharmacology
- drug discovery
- literature
homepage_url: https://sulab.github.io/DrugMechDB/
id: drugmechdb
infores_id: drugmechdb
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0 Universal
name: DrugMechDB
products:
- category: GraphProduct
  compatibility:
  - standard: biolink
  compression: zip
  description: Curated mechanistic drug–disease paths comprising the DrugMechDB dataset
    packaged as a downloadable archive.
  dump_format: other
  format: mixed
  id: drugmechdb.graph
  latest_version: 2.0.1
  name: DrugMechDB Graph Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:wasInformedBy
    source: drugcentral
  - relation_type: prov:wasInformedBy
    source: wikipedia
  product_url: https://doi.org/10.5281/zenodo.8139357
  repository: https://github.com/SuLab/DrugMechDB
  versions:
  - 2.0.1
  - 2.0.0
  - 1.0.2
  - '1.0'
- category: GraphicalInterface
  description: Web interface for exploring curated DrugMechDB paths by drug and disease.
  format: http
  id: drugmechdb.web
  name: DrugMechDB Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  product_url: https://sulab.github.io/DrugMechDB/
- category: GraphProduct
  description: Robokop KG (Automat)
  format: kgx-jsonl
  id: automat.robokopkg
  name: robokopkg
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/RobokopKG/4901b2bc764444ea/
publications:
- authors:
  - Adriana Carolina Gonzalez-Cavazos
  - Anna Tanska
  - Michael Mayers
  - Denise Carvalho-Silva
  - Brindha Sridharan
  - Patrick A. Rewers
  - Umasri Sankarlal
  - Lakshmanan Jagannathan
  - Andrew I. Su
  doi: 10.1038/s41597-023-02534-z
  id: doi:10.1038/s41597-023-02534-z
  journal: Scientific Data
  title: 'DrugMechDB: A Curated Database of Drug Mechanisms'
  year: '2023'
repository: https://github.com/SuLab/DrugMechDB
taxon:
- NCBITaxon:9606
---
DrugMechDB

## Evaluation

- View the evaluation: [drugmechdb evaluation](drugmechdb_eval.html)