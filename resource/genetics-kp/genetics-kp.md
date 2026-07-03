---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  label: Jason Flannick
creation_date: '2025-03-09T00:00:00Z'
description: A Translator Knowledge Provider focusing on genetic data.
domains:
- biomedical
id: genetics-kp
infores_id: genetics-data-provider
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Genetics KP
products:
- category: GraphProduct
  description: TRAPI knowledge graph served by the Genetics KP, exposing gene/disease
    and gene/phenotype associations computed from large-scale human genetics data
    (e.g. Genebass exome association statistics aggregated with methods such as MAGMA
    and the HuGE calculator) and integrated curated gene-condition resources. The
    linked endpoint returns the meta knowledge graph describing the served node and
    edge types.
  format: json
  id: genetics-kp.graph
  name: Genetics KP Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  - relation_type: prov:hadPrimarySource
    source: genebass
  product_file_size: 3538
  product_url: https://genetics-kp.transltr.io/genetics_provider/trapi/v1.5/meta_knowledge_graph
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gencc
  - relation_type: prov:wasInfluencedBy
    source: clinvar
  - relation_type: prov:wasInfluencedBy
    source: clingen
- category: DocumentationProduct
  description: Team overview and data source documentation for the Genetics Knowledge
    Provider.
  format: http
  id: genetics-kp.docs
  name: Genetics KP Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Genetics-Knowledge-Provider
- category: ProcessProduct
  description: Source code repository for the Genetics Knowledge Provider implementation.
  format: http
  id: genetics-kp.code
  name: Genetics KP Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_url: https://github.com/broadinstitute/genetics-kp-dev
---
A Translator Knowledge Provider focusing on genetic data.

## Automated Evaluation

- View the automated evaluation: [genetics-kp automated evaluation](genetics-kp_eval_automated.html)