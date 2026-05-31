---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: mduby@broadinstitute.org
  label: Marc Duby
- category: Individual
  label: Jason Flannick
- category: Individual
  label: Noel Burt
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
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: Genetics KP
products:
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Genetics KP distributed via the NCATS Translator
    release site (release 2026_03_27; build geneticskp_2026-03-27_1f1ad62b_2025sep1_4.3.6;
    source version 2026-03-27; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 653544
  format: kgx-jsonl
  id: translator.geneticskp.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Genetics KP KGX Graph
  node_count: 28023
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/geneticskp/latest/
  versions:
  - '2026_03_27'
  - geneticskp_2026-03-27_1f1ad62b_2025sep1_4.3.6
- category: DocumentationProduct
  description: Translator wiki overview for Genetics KP, including team contacts,
    public API entrypoint, upstream data resources, and method references.
  format: http
  id: geneticskp.docs
  name: Genetics KP Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Genetics-Knowledge-Provider
- category: ProgrammingInterface
  description: Translator Reasoner API endpoint for Genetics KP.
  format: http
  id: geneticskp.trapi
  name: Genetics KP TRAPI Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://genetics-kp.transltr.io/genetics_provider/trapi/v1.4/
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
repository: https://github.com/broadinstitute/genetics-kp-dev
tags:
- translator
---
# Genetics KP

Genetics KP contributes Translator-compatible genetic evidence and associations
for gene-disease analysis, with a focus on integrating GWAS-derived signals and
other curated genetic evidence into a unified framework. The Translator wiki
describes the provider as combining disease-specific GWAS datasets with curated
resources such as GeneBass, GenCC, ClinVar, and ClinGen while using supporting
computational methods to prioritize gene-disease associations.

The public Genetics KP repository further documents the current method mix used
to populate the graph, including MAGMA gene and pathway associations,
Richards-method associations, ABC-method associations, and integrated genetics
associations layered over curated public sources. That gives the graph a clearer
provenance trail than the page previously recorded, even though several method
inputs are Broad-hosted workflows rather than standalone registry resources.

The provider is designed to supply computation-ready genetic evidence to
Translator reasoning systems while preserving provenance across its integrated
association sources.

## Evaluation

- View the evaluation: [geneticskp evaluation](geneticskp_eval_automated.html)