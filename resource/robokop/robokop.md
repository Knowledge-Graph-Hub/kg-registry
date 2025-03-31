---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  email: kfecho@copperlineprofessionalsolutions.com
  label: Karamarie Fecho
description: ROBOKOP (Reasoning Over Biomedical Objects linked in Knowledge Oriented
  Pathways) is an open-source biomedical knowledge graph system that enables complex
  queries over a large-scale integrated knowledge graph.
domains:
- health
homepage_url: http://robokop.renci.org
id: robokop
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: ROBOKOP
products:
- category: Product
  description: A biomedical knowledge graph containing ~10 million nodes and ~250
    million edges from ~30 biological data sources and bio-ontologies.
  id: robokop.graph
  name: ROBOKOP Knowledge Graph (KG)
  original_source:
  - robokop
  product_url: http://robokopkg.renci.org
  secondary_source:
  - robokop
- category: GraphProduct
  description: Robokop KG (Automat)
  format: kgx-jsonl
  id: automat.robokopkg
  name: robokopkg
  original_source:
  - robokop
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/RobokopKG/latest/kgx_files
  secondary_source:
  - automat
- category: GraphProduct
  description: Robokop Plus
  format: kgx-jsonl
  id: automat.robokopplus
  name: robokopplus
  original_source:
  - robokop
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/RobokopPlus/latest/kgx_files
  secondary_source:
  - automat
repository: https://github.com/NCATS-Gamma/robokop
---
### ROBOKOP: A Knowledge Graph System for Biomedical Question Answering

ROBOKOP (Reasoning Over Biomedical Objects linked in Knowledge Oriented Pathways) is an **open-source**, modular **biomedical knowledge graph system** that includes:
- The **ROBOKOP Knowledge Graph (KG)**
- A **user interface** for building and exploring queries
- Supporting tools and APIs for programmatic access