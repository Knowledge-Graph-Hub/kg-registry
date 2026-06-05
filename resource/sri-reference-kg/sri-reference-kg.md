---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: kevinschaper@gmail.com
      - contact_type: github
        value: kevinschaper
    label: Kevin Schaper
    orcid: 0000-0003-3311-7320
description: The Monarch Initiative's SRI reference knowledge graph is a biomedical
  KG distribution and service layer that supports Translator-style querying across
  genes, diseases, phenotypes, variants, and related entities.
domains:
  - biomedical
homepage_url: https://monarchinitiative.org/kg/about
id: sri-reference-kg
infores_id: sri-reference-kg
layout: resource_detail
name: SRI-Reference KG
products:
  - category: ProgrammingInterface
    connection_url: https://api-v3.monarchinitiative.org/v3/docs
    description: Public API documentation for querying the Monarch Initiative knowledge
      graph that underlies the SRI reference KG distribution.
    format: http
    id: sri-reference-kg.api
    is_public: true
    name: Monarch KG API
    product_url: https://api-v3.monarchinitiative.org/v3/docs
    original_source:
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Documentation and status pages describing the Monarch knowledge graph,
      source inventory, downloads, and quality-control process.
    format: http
    id: sri-reference-kg.docs
    is_public: true
    name: Monarch KG Documentation
    product_url: https://monarchinitiative.org/kg/documentation
    original_source:
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: KGX distribution of the SRI-Reference KG
    format: kgx
    id: sri-reference-kg.graph
    name: SRI-Reference KG (KGX distribution)
    product_file_size: 230046094
    product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
    original_source:
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
repository: https://github.com/monarch-initiative/monarch-app
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
---

The SRI-Reference KG is the Monarch Initiative's biomedical knowledge graph as
packaged for downstream querying, download, and service integration. It brings
together curated data about genes, diseases, phenotypes, variants, genotypes,
pathways, and supporting ontologies so that applications can traverse a shared
graph of cross-species and clinical-research knowledge.

In practice, this resource is exposed through downloadable KG artifacts and the
Monarch API and web stack. The current distribution hosted under the Monarch data
site provides KGX and database-oriented outputs, while the Monarch documentation
and API pages describe the source inventory, quality-control reports, and query
surfaces built over the same graph content.

## Automated Evaluation

- View the automated evaluation: [sri-reference-kg automated evaluation](sri-reference-kg_eval_automated.html)
