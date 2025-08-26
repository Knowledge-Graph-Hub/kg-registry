---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: kfecho@copperlineprofessionalsolutions.com
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
  product_file_size: 280
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
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-25: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
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
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-25: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
repository: https://github.com/NCATS-Gamma/robokop
---
### ROBOKOP: A Knowledge Graph System for Biomedical Question Answering

ROBOKOP (Reasoning Over Biomedical Objects linked in Knowledge Oriented Pathways) is an **open-source**, modular **biomedical knowledge graph system** that includes:
- The **ROBOKOP Knowledge Graph (KG)**
- A **user interface** for building and exploring queries
- Supporting tools and APIs for programmatic access

## Evaluation

- View the evaluation: [robokop evaluation](robokop_eval.html)