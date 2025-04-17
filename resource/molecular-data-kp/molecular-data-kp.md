---
layout: resource_detail
activity_status: active
id: molecular-data-kp
name: MolePro
description: >-
  MolePro is a Molecular Data Provider translating molecular scale to systems scale through a Reasoner API.
  It is a Translator Knowledge Provider.
domains:
- health
category: KnowledgeGraph
contacts:
- category: Individual
  label: "Sandrine Muller"
  orcid: 0000-0001-5998-3003
homepage_url: https://github.com/broadinstitute/molecular-data-provider/
repository: https://github.com/broadinstitute/molecular-data-provider/
products:
- id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  description: KGX nodes for Molecular Data KP
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
  category: GraphProduct
  format: kgx
  secondary_source:
  - molecular-data-kp
  original_source:
  - molecular-data-kp
- id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  description: KGX edges for Molecular Data KP
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
  category: GraphProduct
  format: kgx
  secondary_source:
  - molecular-data-kp
  original_source:
  - molecular-data-kp
- id: molecular-data-kp.api
  name: Open API for Molecular Data KP
  description: Open API for Molecular Data KP
  product_url: https://translator.broadinstitute.org/molecular_data_provider/api
  category: ProgrammingInterface
  is_public: true
  connection_url: https://translator.broadinstitute.org/molecular_data_provider/api
  secondary_source:
  - molecular-data-kp
  original_source:
  - molecular-data-kp
license:
  label: MIT License
  id: https://opensource.org/licenses/MIT
collection:
- translator
---

A Translator Knowledge Provider for molecular data.

contacts:
- category: Individual
 Sandrine Muller, Vlado Dancik, and Larry Chung
