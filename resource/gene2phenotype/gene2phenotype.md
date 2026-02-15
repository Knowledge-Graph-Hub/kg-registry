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
  description: KGX graph package for Gene2Phenotype (build gene2phenotype_2025_12_15_1.0_2025sep1_4.3.6;
    release 2025_12_15)
  format: kgx
  id: translator.gene2phenotype.graph
  name: Translator Gene2Phenotype KGX Graph
  original_source:
  - gene2phenotype
  product_url: https://stars.renci.org/var/translator/releases/gene2phenotype/2025_12_15/
  secondary_source:
  - translator
repository: https://github.com/EBI-G2P/gene2phenotype_api
synonyms:
- G2P
- Gene2Phenotype
---
# Gene2Phenotype

Gene2Phenotype is a curated resource linking genes, variant consequences, molecular
mechanisms, and diseases to support rare disease interpretation.
