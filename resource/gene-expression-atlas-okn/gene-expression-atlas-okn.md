---
id: "gene-expression-atlas-okn"
name: Gene Expression Atlas
description: Gene Expression Atlas OKN is a semantic knowledge graph representing selected EMBL-EBI Gene Expression Atlas studies, assays, differential-expression measurements, and study metadata.
activity_status: active
homepage_url: https://www.ebi.ac.uk/gxa/home
contacts:
  - category: Individual
    label: Andrew Su
    contact_details:
      - contact_type: email
        value: "asu@scripps.edu"
      - contact_type: github
        value: "andrewsu"
  - category: Individual
    label: Trish Whetzel
    contact_details:
      - contact_type: email
        value: "plwhetzel@gmail.com"
      - contact_type: github
        value: "twhetzel"
products:
  - id: "gene-expression-atlas-okn.sparql"
    name: Gene Expression Atlas SPARQL
    description: SPARQL endpoint for querying the Gene Expression Atlas OKN graph through the OKN FRINK service.
    category: ProgrammingInterface
    format: http
    product_url: https://apps.okn.us/gene-expression-atlas-okn/sparql
    original_source:
      - source: gene-expression-atlas-okn
        relation_type: prov:hadPrimarySource
  - id: "gene-expression-atlas-okn.tpf"
    name: Gene Expression Atlas TPF
    description: Triple Pattern Fragments endpoint for browsing the Gene Expression Atlas OKN graph through the OKN FRINK service.
    category: ProgrammingInterface
    format: http
    product_url: https://apps.okn.us/ldf/gene-expression-atlas-okn
    original_source:
      - source: gene-expression-atlas-okn
        relation_type: prov:hadPrimarySource
collection:
  - okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
domains:
  - biomedical
  - genomics
---

Gene Expression Atlas

## Description

Gene Expression Atlas OKN is a semantic knowledge graph derived from selected
EMBL-EBI Gene Expression Atlas studies. According to the OKN registry, it
captures 243 studies and 797 assays spanning differential expression
measurements across genes, anatomical entities, cell types, diseases,
developmental stages, and biological sex categories.

The graph is described as using Biolink-model-based structure to connect study
metadata, assays, and expression associations in a form suitable for systematic
cross-study exploration and integrative genomics analysis.

*This resource was automatically synchronized from the FRINK OKN registry.*
