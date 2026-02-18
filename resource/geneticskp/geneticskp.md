---
activity_status: active
category: KnowledgeGraph
collection:
- translator
creation_date: '2026-02-18T00:00:00Z'
description: Genetics KP is a Translator knowledge provider focused on integrating
  genetic association evidence (including GWAS-derived signals) into a unified framework
  for gene-disease relationship analysis.
domains:
- genomics
- health
- translational
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Genetics-Knowledge-Provider
id: geneticskp
last_modified_date: '2026-02-18T00:00:00Z'
layout: resource_detail
name: Genetics KP
products:
- category: GraphProduct
  description: KGX graph package for Genetics KP (build geneticskp_2025-12-15_1.0_2025sep1_4.3.6;
    release 2025_12_15)
  format: kgx
  id: translator.geneticskp.graph
  name: Translator Genetics KP KGX Graph
  original_source:
  - geneticskp
  product_url: https://stars.renci.org/var/translator/releases/geneticskp/2025_12_15/
  secondary_source:
  - translator
- category: ProgrammingInterface
  description: Translator Reasoner API endpoint for Genetics KP.
  format: http
  id: geneticskp.trapi
  name: Genetics KP TRAPI Endpoint
  original_source:
  - geneticskp
  product_url: https://genetics-kp.transltr.io/genetics_provider/trapi/v1.4/
repository: https://github.com/broadinstitute/genetics-kp-dev
tags:
- translator
---
# Genetics KP

Genetics KP contributes Translator-compatible genetic evidence and associations.