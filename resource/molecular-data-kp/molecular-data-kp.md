---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  label: Sandrine Muller
  orcid: 0000-0001-5998-3003
description: MolePro is a Molecular Data Provider translating molecular scale to systems
  scale through a Reasoner API. It is a Translator Knowledge Provider.
domains:
- health
homepage_url: https://github.com/broadinstitute/molecular-data-provider/
id: molecular-data-kp
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: MolePro
products:
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - molecular-data-kp
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
  secondary_source:
  - molecular-data-kp
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - molecular-data-kp
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
  secondary_source:
  - molecular-data-kp
- category: ProgrammingInterface
  connection_url: https://translator.broadinstitute.org/molecular_data_provider/api
  description: Open API for Molecular Data KP
  id: molecular-data-kp.api
  is_public: true
  name: Open API for Molecular Data KP
  original_source:
  - molecular-data-kp
  product_url: https://translator.broadinstitute.org/molecular_data_provider/api
  secondary_source:
  - molecular-data-kp
repository: https://github.com/broadinstitute/molecular-data-provider/
---
A Translator Knowledge Provider for molecular data.

contacts:
- category: Individual
 Sandrine Muller, Vlado Dancik, and Larry Chung

## Automated Evaluation

- View the automated evaluation: [molecular-data-kp automated evaluation](molecular-data-kp_eval_automated.html)
