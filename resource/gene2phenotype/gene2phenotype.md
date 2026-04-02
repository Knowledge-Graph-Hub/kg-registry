---
activity_status: active
category: DataSource
creation_date: '2026-01-23T00:00:00Z'
description: A curated gene-disease evidence resource linking genes, variant mechanisms,
  and clinical phenotypes to support rare disease interpretation.
domains:
- genomics
- phenotype
- health
homepage_url: https://www.ebi.ac.uk/gene2phenotype/
id: gene2phenotype
last_modified_date: '2026-02-15T00:00:00Z'
layout: resource_detail
name: Gene2Phenotype
products:
- category: GraphicalInterface
  description: Main interface for searching curated gene-disease evidence and panels.
  format: http
  id: gene2phenotype.portal
  name: Gene2Phenotype Portal
  product_url: https://www.ebi.ac.uk/gene2phenotype/
- category: ProgrammingInterface
  description: API documentation interface for programmatic access to G2P records.
  format: http
  id: gene2phenotype.api
  name: Gene2Phenotype API
  product_url: https://www.ebi.ac.uk/gene2phenotype/api/
- category: ProgrammingInterface
  description: OpenAPI schema endpoint for the Gene2Phenotype API.
  format: http
  id: gene2phenotype.api.schema
  name: Gene2Phenotype API Schema
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
  - gene2phenotype
  product_url: https://kgx-storage.rtx.ai/releases/gene2phenotype/latest/
  secondary_source:
  - translator
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
  - alliance
  - bgee
  - bindingdb
  - chembl
  - cohd
  - ctd
  - ctkp
  - drug-approvals-kp
  - dgidb
  - diseases
  - drugrephub
  - drugcentral
  - gtopdb
  - gene2phenotype
  - geneticskp
  - go-cam
  - goa
  - hp
  - icees-kg
  - intact
  - ncbigene
  - panther
  - pathbank
  - semmeddb
  - sider
  - signor
  - text-mining-kp
  - ttd
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - 423af7989cac
repository: https://github.com/EBI-G2P/gene2phenotype_api
synonyms:
- G2P
- Gene2Phenotype
---
# Gene2Phenotype

Gene2Phenotype is a curated resource linking genes, variant consequences, molecular
mechanisms, and diseases to support rare disease interpretation.