---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: rxx@case.edu
    label: Rong Xu
description: A knowledge graph for drug repurposing
domains:
  - biomedical
homepage_url: http://nlp.case.edu/public/data/GPKG-Predict/
id: gp-kg
layout: resource_detail
name: GP-KG
products:
  - category: GraphProduct
    description: GP_KG.txt
    edge_count: 1246726
    id: gp-kg.graph
    name: GP-KG
    node_count: 61146
    original_source:
      - source: gp-kg
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: mgi
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: goa
        relation_type: prov:wasDerivedFrom
      - source: gtex
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: mp
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: umls
        relation_type: prov:wasDerivedFrom
      - source: uberon
        relation_type: prov:wasDerivedFrom
      - source: pubchem
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: faers
        relation_type: prov:wasDerivedFrom
      - source: phenomebrowser
        relation_type: prov:wasDerivedFrom
    product_file_size: 48397035
    product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  - category: ProcessProduct
    description: A computational framework for drug repurposing, used with GP-KG
    id: gp-kg.process.kg-predict
    name: KG-Predict
    original_source:
      - source: gp-kg
        relation_type: prov:hadPrimarySource
    product_url: http://nlp.case.edu/public/data/GPKG-Predict/code/
publications:
- authors:
  - Gao Z
  - Ding P
  - Xu R
  doi: 10.1016/j.jbi.2022.104133
  id: doi:10.1016/j.jbi.2022.104133
  journal: Journal of Biomedical Informatics
  title: 'KG-Predict: A knowledge graph computational framework for drug repurposing'
  year: '2022'
repository: http://nlp.case.edu/public/data/GPKG-Predict/
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---

GP-KG

## Automated Evaluation

- View the automated evaluation: [gp-kg automated evaluation](gp-kg_eval_automated.html)
