---
activity_status: active
category: KnowledgeGraph
collection:
- translator
creation_date: '2026-02-18T00:00:00Z'
description: Clinical Trials Knowledge Provider (CTKP) is a Translator knowledge provider
  maintained by the Multiomics Provider that exposes clinical trial-derived associations
  from ClinicalTrials.gov (via AACT), including trial interventions, conditions, and
  related biomedical entities.
domains:
- clinical
- health
- translational
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Clinical-Trials-KP
id: ctkp
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: Clinical Trials KP
contacts:
- category: Individual
  label: Gwênlyn Glusman
  contact_details:
  - contact_type: github
    value: gglusman
products:
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for CTKP distributed via the NCATS Translator
    release site (release 2026_03_27; build ctkp_3.1.37_a99268cc_2025sep1_4.3.6; source
    version 3.1.37; Biolink 4.3.6; Node Normalizer 2025sep1). The Translator wiki
    describes the graph as exposing trial identifiers, interventions,
    diseases/conditions, and adverse events derived from ClinicalTrials.gov via
    AACT, using predicates including biolink:in_clinical_trials_for,
    biolink:mentioned_in_trials_for, and biolink:treats.
  edge_count: 438575
  format: kgx-jsonl
  id: translator.ctkp.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator CTKP KGX Graph
  node_count: 41243
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:wasDerivedFrom
    source: clinicaltrialsgov
  product_url: https://kgx-storage.rtx.ai/releases/ctkp/latest/
  versions:
  - '2026_03_27'
  - ctkp_3.1.37_a99268cc_2025sep1_4.3.6
- category: DocumentationProduct
  description: Translator wiki documentation for Clinical Trials KP, including source
    and access details.
  format: http
  id: ctkp.docs
  name: Clinical Trials KP Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Clinical-Trials-KP
- category: DocumentationProduct
  description: SmartAPI registry entry for the Multiomics Clinical Trials KP TRAPI
    1.5 endpoint.
  format: http
  id: ctkp.smartapi
  name: Clinical Trials KP SmartAPI Registration
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://smart-api.info/registry?q=e51073371d7049b9643e1edbdd61bcbd
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
repository: https://github.com/multiomicsKP/clinical_trials_kp
tags:
- translator
---
# Clinical Trials KP

CTKP provides Translator-facing clinical trial associations derived from
ClinicalTrials.gov submissions through the AACT database. The Translator wiki
describes the graph as exposing trial identifiers, interventions,
diseases/conditions, adverse events, and other trial-linked biomedical entities
using Biolink predicates such as clinical-trial and treatment associations.

The public CTKP repository and SmartAPI registration provide additional detail
about how this provider is exposed inside Translator: the service is maintained
by the Multiomics Provider, published as a TRAPI 1.5 knowledge provider, and
built around AACT-mediated extracts of ClinicalTrials.gov content rather than
direct registry scraping.

The resource is maintained by the Multiomics Provider and distributed as a
Translator release artifact for integration into broader NCATS Translator
reasoning workflows.

## Evaluation

- View the evaluation: [ctkp evaluation](ctkp_eval_automated.html)