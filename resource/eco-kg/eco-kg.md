---
activity_status: active
category: KnowledgeGraph
collection:
- ber
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: diatomsRcool
  - contact_type: email
    value: annethessen@gmail.com
  label: Anne Thessen
- category: Organization
  contact_details:
  - contact_type: url
    value: https://kghub.org
  - contact_type: github
    value: Knowledge Graph Hub
  label: Knowledge Graph Hub
description: A knowledge graph of plant traits starting with Planteome and EOL TraitBank.
domains:
- organisms
- environment
- biological systems
homepage_url: https://kghub.org/eco-kg/index.html
id: eco-kg
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: eco-KG
products:
- category: GraphProduct
  compression: tar
  description: Knowledge graph containing plant traits data from Planteome and EOL
    TraitBank
  format: kgx
  id: eco-kg.graph
  name: eco-KG Graph
  original_source:
  - eco-kg
  product_url: https://kg-hub.berkeleybop.io/eco-kg/
- category: ProgrammingInterface
  connection_url: https://kghub.org/eco-kg/api
  description: API for accessing eco-KG data
  id: eco-kg.api
  is_public: true
  name: eco-KG API
  original_source:
  - eco-kg
  product_url: https://kghub.org/eco-kg/api
repository: https://github.com/Knowledge-Graph-Hub/eco-kg
tags:
- core
taxon:
- NCBITaxon:33090
---
eco-KG: a knowledge graph of plant traits starting with Planteome and EOL TraitBank. The graph integrates data from various sources related to plant phenotypes, traits, and ecological relationships.

## Automated Evaluation

- View the automated evaluation: [eco-kg automated evaluation](eco-kg_eval_automated.html)
