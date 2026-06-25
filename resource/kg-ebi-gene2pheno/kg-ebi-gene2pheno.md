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
    label: Colleen Xu
description: An ingest of EMBL-EBI's Gene2Phenotype resource, for Translator use (output in Translator standards and NodeNormed, using own custom pipeline)
domains:
  - biomedical
id: kg-ebi-gene2pheno
layout: resource_detail
name: EBI Gene2Phenotype KG
products:
  - category: GraphProduct
    description: KGX nodes file for EBI Gene2Phenotype KG
    format: kgx-jsonl
    id: kg-ebi-gene2pheno.nodes.kgx
    name: EBI gene2pheno KGX nodes
    product_file_size: 62139
    product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/ebi_gene2phenotype/EBIgene2pheno_kgx_nodes.jsonl
    original_source:
      - source: kg-ebi-gene2pheno
        relation_type: prov:hadPrimarySource
      - source: gene2phenotype
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: orphanet
        relation_type: prov:wasDerivedFrom
  - category: GraphProduct
    description: KGX edges file for EBI Gene2Phenotype KG
    format: kgx-jsonl
    id: kg-ebi-gene2pheno.edges.kgx
    name: EBI gene2pheno KGX edges
    product_file_size: 133106
    product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/ebi_gene2phenotype/EBIgene2pheno_kgx_edges.jsonl
    original_source:
      - source: kg-ebi-gene2pheno
        relation_type: prov:hadPrimarySource
      - source: gene2phenotype
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: orphanet
        relation_type: prov:wasDerivedFrom
  - category: GraphProduct
    description: TRAPI edges file for EBI Gene2Phenotype KG
    format: trapi-jsonl
    id: kg-ebi-gene2pheno.edges.trapi
    name: EBI gene2pheno TRAPI edges
    product_file_size: 142045
    product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/ebi_gene2phenotype/EBIgene2pheno_trapi_edges.jsonl
    original_source:
      - source: kg-ebi-gene2pheno
        relation_type: prov:hadPrimarySource
      - source: gene2phenotype
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: orphanet
        relation_type: prov:wasDerivedFrom
repository: https://github.com/biothings/pending.api/tree/translator-output/plugins/ebi_gene2phenotype
creation_date: '2025-05-07T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---

## Automated Evaluation

- View the automated evaluation: [kg-ebi-gene2pheno automated evaluation](kg-ebi-gene2pheno_eval_automated.html)
