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
homepage_url: https://www.ebi.ac.uk/gene2phenotype/
license:
  id: https://www.ebi.ac.uk/about/terms-of-use/
  label: EMBL-EBI Terms of Use
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
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/39506859
    authors:
      - T Michael Yates
      - Morad Ansari
      - Louise Thompson
      - Sarah E Hunt
      - Elena Cibrian Uhalte
      - Rachel J Hobson
      - Joseph A Marsh
      - Caroline F Wright
      - Helen V Firth
    doi: 10.1186/s13073-024-01398-1
    journal: Genome Medicine
    preferred: true
    title: Curating genomic disease-gene relationships with Gene2Phenotype (G2P)
    year: '2024'
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31147538
    authors:
      - Anja Thormann
      - Mihail Halachev
      - William McLaren
      - David J Moore
      - Victoria Svinti
      - Archie Campbell
      - Shona M Kerr
      - Marc Tischkowitz
      - Sarah E Hunt
      - Malcolm G Dunlop
      - Matthew E Hurles
      - Caroline F Wright
      - Helen V Firth
      - Fiona Cunningham
      - David R FitzPatrick
    doi: 10.1038/s41467-019-10016-3
    journal: Nature Communications
    title: Flexible and scalable diagnostic filtering of genomic variants using G2P
      with Ensembl VEP
    year: '2019'
creation_date: '2025-05-07T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---

## Automated Evaluation

- View the automated evaluation: [kg-ebi-gene2pheno automated evaluation](kg-ebi-gene2pheno_eval_automated.html)
