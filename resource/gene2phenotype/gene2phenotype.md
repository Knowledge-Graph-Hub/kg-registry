---
activity_status: active
category: DataSource
creation_date: '2026-01-23T00:00:00Z'
description: A curated gene-disease evidence resource linking genes, variant mechanisms,
  and clinical phenotypes to support rare disease interpretation.
domains:
- genomics
- phenotype
- biomedical
homepage_url: https://www.ebi.ac.uk/gene2phenotype/
id: gene2phenotype
infores_id: gene2phenotype
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: Gene2Phenotype
products:
- category: GraphicalInterface
  description: Main interface for searching curated gene-disease evidence and panels.
  format: http
  id: gene2phenotype.portal
  name: Gene2Phenotype Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  product_url: https://www.ebi.ac.uk/gene2phenotype/
- category: ProgrammingInterface
  description: API documentation interface for programmatic access to G2P records.
  format: http
  id: gene2phenotype.api
  name: Gene2Phenotype API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  product_url: https://www.ebi.ac.uk/gene2phenotype/api/
- category: ProgrammingInterface
  description: OpenAPI schema endpoint for the Gene2Phenotype API.
  format: http
  id: gene2phenotype.api.schema
  name: Gene2Phenotype API Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  product_url: https://www.ebi.ac.uk/gene2phenotype/api/schema/
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Gene2Phenotype distributed via the NCATS
    Translator release site (release 2026_03_27; build gene2phenotype_2026_03_27_4773272d_2025sep1_4.3.6;
    source version 2026_03_27; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 3022
  format: kgx-jsonl
  id: translator.gene2phenotype.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Gene2Phenotype KGX Graph
  node_count: 5424
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/gene2phenotype/latest/
  versions:
  - '2026_03_27'
  - gene2phenotype_2026_03_27_4773272d_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: GraphProduct
  description: KGX nodes file for EBI Gene2Phenotype KG
  format: kgx-jsonl
  id: kg-ebi-gene2pheno.nodes.kgx
  name: EBI gene2pheno KGX nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-ebi-gene2pheno
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  product_file_size: 62139
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/ebi_gene2phenotype/EBIgene2pheno_kgx_nodes.jsonl
- category: GraphProduct
  description: KGX edges file for EBI Gene2Phenotype KG
  format: kgx-jsonl
  id: kg-ebi-gene2pheno.edges.kgx
  name: EBI gene2pheno KGX edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-ebi-gene2pheno
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  product_file_size: 133106
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/ebi_gene2phenotype/EBIgene2pheno_kgx_edges.jsonl
- category: GraphProduct
  description: TRAPI edges file for EBI Gene2Phenotype KG
  format: trapi-jsonl
  id: kg-ebi-gene2pheno.edges.trapi
  name: EBI gene2pheno TRAPI edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-ebi-gene2pheno
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  product_file_size: 142045
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/ebi_gene2phenotype/EBIgene2pheno_trapi_edges.jsonl
repository: https://github.com/EBI-G2P/gene2phenotype_api
synonyms:
- G2P
- Gene2Phenotype
---
# Gene2Phenotype

Gene2Phenotype is a curated resource linking genes, variant consequences, molecular
mechanisms, and diseases to support rare disease interpretation.