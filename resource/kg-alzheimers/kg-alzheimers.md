---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jhc@lbl.gov
  - contact_type: github
    value: caufieldjh
  label: J. Harry Caufield
  orcid: 0000-0001-5705-7831
creation_date: '2025-03-18T00:00:00Z'
description: A Knowledge Graph for integrating data related to Alzheimer's disease,
  supporting Retrieval-Augmented Generation (RAG) and AI assistant development for
  Alzheimer's disease research.
domains:
- biomedical
- neuroscience
homepage_url: https://kghub.org/kg-alzheimers/index.html
id: kg-alzheimers
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: KG-Alzheimers
products:
- category: GraphProduct
  compression: targz
  description: KGX Distribution of KG-Alzheimers
  format: kgx
  id: kg-alzheimers.graph
  name: KGX Distribution of KG-Alzheimers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-alzheimers
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_file_size: 210868256
  product_url: https://kg-hub.berkeleybop.io/kg-alzheimers/current/kg-alzheimers.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-07-01; no live download
    location was found (GitHub releases, kghub.io/current, and Zenodo all return
    404 or have no published artifact).
repository: https://github.com/Knowledge-Graph-Hub/kg-alzheimers
taxon:
- NCBITaxon:9606
---
KG-Alzheimers is a knowledge graph created in collaboration between Lawrence Berkeley National
Lab and Washington University, designed to integrate data related to Alzheimer's
disease. The purpose is to support use cases including retrieval augmented generation (RAG)
and the creation of an AI-assistant. It is built with a strong emphasis on provenance,
transparency, and interoperability with existing biomedical knowledge graphs. Learn more
about the project and its developments on our [documentation pages](https://kghub.org/kg-alzheimers/).

## Automated Evaluation

- View the automated evaluation: [kg-alzheimers automated evaluation](kg-alzheimers_eval_automated.html)