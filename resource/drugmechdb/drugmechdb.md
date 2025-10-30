---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://sulab.org/
    label: Su Lab
description: DrugMechDB is a curated database that captures mechanistic paths from a drug to a disease within a given indication. Expert curators normalize concepts and relationships to standard biomedical identifiers and represent each indication as a directed path through a biological knowledge graph, suitable for computational analysis and benchmarking.
domains:
  - biomedical
  - pharmacology
  - drug discovery
  - literature
homepage_url: https://sulab.github.io/DrugMechDB/
id: drugmechdb
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
    description: "Curated mechanistic drug–disease paths comprising the DrugMechDB dataset packaged as a downloadable archive."
    dump_format: other
    format: mixed
    id: drugmechdb.graph
    latest_version: 2.0.1
    name: DrugMechDB Graph Dataset
    original_source:
      - go
      - cl
      - mesh
      - chebi
      - drugbank
      - interpro
      - uberon
      - pr
      - ncbitaxon
      - reactome
      - hp
      - uniprot
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
    product_url: https://sulab.github.io/DrugMechDB/
publications:
  - doi: 10.1038/s41597-023-02534-z
    id: doi:10.1038/s41597-023-02534-z
    journal: Scientific Data
    title: "DrugMechDB — a curated database of drug mechanisms"
    year: '2023'
repository: https://github.com/SuLab/DrugMechDB
infores_id: drugmechdb
---

DrugMechDB

## Evaluation

- View the evaluation: [drugmechdb evaluation](drugmechdb_eval.html)
