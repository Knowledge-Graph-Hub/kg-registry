---
id: "oard-kg"
name: Open Annotations for Rare Diseases (OARD) Knowledge Graph
description: OARD-KG is an RDF knowledge graph of clinical associations between rare diseases and phenotypes derived from electronic health records.
activity_status: active
homepage_url: https://github.com/WengLab-InformaticsResearch/oard-react
products:
  - id: "oard-kg.sparql"
    name: Open Annotations for Rare Diseases (OARD) Knowledge Graph SPARQL
    description: SPARQL endpoint for Open Annotations for Rare Diseases (OARD) Knowledge Graph
    category: ProgrammingInterface
    product_url: https://apps.okn.us/oard-kg/sparql
    original_source:
      - source: oard-kg
        relation_type: prov:hadPrimarySource
  - id: "oard-kg.tpf"
    name: Open Annotations for Rare Diseases (OARD) Knowledge Graph TPF
    description: Triple Pattern Fragments endpoint for Open Annotations for Rare Diseases (OARD) Knowledge Graph
    category: ProgrammingInterface
    product_url: https://apps.okn.us/ldf/oard-kg
    original_source:
      - source: oard-kg
        relation_type: prov:hadPrimarySource
collection:
  - okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
contacts:
  - category: Individual
    label: Casey Ta
    contact_details:
      - contact_type: email
        value: "ct2865@cumc.columbia.edu"
      - contact_type: github
        value: "CaseyTa"
  - category: Individual
    label: Chunhua Weng
    contact_details:
      - contact_type: email
        value: "cw2384@cumc.columbia.edu"
      - contact_type: github
        value: "ChunhuaWeng"
domains:
  - biomedical
  - clinical
---

Open Annotations for Rare Diseases (OARD) Knowledge Graph

## Description

OARD-KG is an RDF triplestore that exposes clinical associations between rare diseases and phenotypes derived from electronic health records.

The associated OARD project couples a React-based exploration interface with an API-backed service for browsing and querying rare-disease phenotype associations.

Within the OKN ecosystem, the graph provides a public SPARQL and triple-pattern-fragments view over this rare-disease annotation layer.

*This resource was automatically synchronized from the FRINK OKN registry.*
