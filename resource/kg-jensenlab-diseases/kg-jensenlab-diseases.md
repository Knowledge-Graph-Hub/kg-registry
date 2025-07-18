---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: colxu@scripps.edu
  - contact_type: github
    value: colleenXu
  label: "Colleen Xu"
description: >-
  An ingest of Jensen Lab's DISEASES resource, for Translator use
  (output in Translator standards and NodeNormed, using own custom pipeline)
domains:
- health
id: kg-jensenlab-diseases
layout: resource_detail
name: JensenLab DISEASES KG
repository: https://github.com/biothings/pending.api/tree/translator-output/plugins/DISEASES
products:
- category: GraphProduct
  description: KGX nodes file for JensenLab DISEASES KG
  format: kgx-jsonl
  id: kg-jensenlab-diseases.nodes.kgx
  name: DISEASES KGX nodes
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_kgx_nodes.jsonl
- category: GraphProduct
  description: KGX edges file for JensenLab DISEASES KG
  format: kgx-jsonl
  id: kg-jensenlab-diseases.edges.kgx
  name: DISEASES KGX edges
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_kgx_edges.jsonl
- category: GraphProduct
  description: TRAPI edges file for JensenLab DISEASES KG
  format: trapi-jsonl
  id: kg-jensenlab-diseases.edges.trapi
  name: DISEASES TRAPI edges
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_trapi_edges.jsonl
---
