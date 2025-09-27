---
layout: resource_detail
activity_status: active
collection:
- ber
- translator
id: eco-kg
name: eco-KG
description: A knowledge graph of plant traits starting with Planteome and EOL TraitBank.
domains:
- organisms
- environment
- biological systems
contacts:
- category: Individual
  label: Anne Thessen
  contact_details:
  - contact_type: github
    value: diatomsRcool
  - contact_type: email
    value: annethessen@gmail.com
- category: Organization
  label: Knowledge Graph Hub
  contact_details:
  - contact_type: url
    value: https://kghub.org
  - contact_type: github
    value: Knowledge Graph Hub
homepage_url: https://kghub.org/eco-kg/index.html
repository: https://github.com/Knowledge-Graph-Hub/eco-kg
category: KnowledgeGraph
tags:
- core
license:
  label: CC BY 4.0
  id: https://creativecommons.org/licenses/by/4.0/
products:
- id: eco-kg.graph
  name: eco-KG Graph
  description: Knowledge graph containing plant traits data from Planteome and EOL TraitBank
  product_url: https://kg-hub.berkeleybop.io/eco-kg/
  category: GraphProduct
  format: kgx
  original_source:
  - eco-kg
  compression: tar
- id: eco-kg.api
  name: eco-KG API
  description: API for accessing eco-KG data
  product_url: https://kghub.org/eco-kg/api
  category: ProgrammingInterface
  is_public: true
  connection_url: https://kghub.org/eco-kg/api
  original_source:
  - eco-kg
---

eco-KG: a knowledge graph of plant traits starting with Planteome and EOL TraitBank. The graph integrates data from various sources related to plant phenotypes, traits, and ecological relationships.
