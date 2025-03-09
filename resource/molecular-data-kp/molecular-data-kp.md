---
layout: resource_detail
activity_status: active
id: molecular-data-kp
name: MolePro
description: >-
  MolePro is a Molecular Data Provider translating molecular scale to systems scale through a Reasoner API.
  It is a Translator Knowledge Provider.
domain: health
category: KnowledgeGraph
contacts:
- category: Individual
  label: "Sandrine Muller"
  orcid: 0000-0001-5998-3003
homepage_url: https://github.com/broadinstitute/molecular-data-provider/
repository: https://github.com/broadinstitute/molecular-data-provider/
products:
- id: molecular-data-kp.nodes
  name: Nodes for Molecular Data KP
  compatibility:
  - standard: kgx
  description: KGX nodes for Molecular Data KP
  url: https://molepro.s3.amazonaws.com/nodes.tsv
  category: GraphProduct
- id: molecular-data-kp.edges
  name: Edges for Molecular Data KP
  compatibility:
  - standard: kgx
  description: KGX edges for Molecular Data KP
  url: https://molepro.s3.amazonaws.com/edges.tsv
  category: GraphProduct
- id: molecular-data-kp.api
  name: Open API for Molecular Data KP
  description: Open API for Molecular Data KP
  url: https://translator.broadinstitute.org/molecular_data_provider/api
  category: ProgrammingInterface
  is_public: true
  connection_url: https://translator.broadinstitute.org/molecular_data_provider/api
license:
  label: MIT License
  id: https://opensource.org/licenses/MIT
---

A Translator Knowledge Provider for molecular data.

contacts:
- category: Individual
 Sandrine Muller, Vlado Dancik, and Larry Chung
