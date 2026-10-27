---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://github.com/NCATSTranslator/Translator-All/wiki/ARAGORN
    label: NCATS Translator
  - category: Individual
    contact_details:
      - contact_type: email
        value: bizon@renci.org
      - contact_type: github
        value: cbizon
    label: Chris Bizon
creation_date: '2025-11-05T00:00:00Z'
description: ARAGORN (Autonomous Relay Agent for Generation Of Ranked Networks) is an NCATS Translator Autonomous Relay Agent (ARA) that performs query operations by compiling and ranking data from multiple ARAGORN-affiliated knowledge provider services. ARAGORN acts as an intermediary between user queries and underlying knowledge providers, aggregating results, performing inference, and ranking answers based on evidence and confidence scores. It implements the Translator Reasoner API (TRAPI) standard for biomedical question-answering.
domains:
  - biomedical
  - information technology
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/ARAGORN
id: aragorn
infores_id: aragorn
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/mit/
  label: MIT
name: ARAGORN
products:
- category: ProgrammingInterface
  description: RENCI-hosted TRAPI endpoint (/query, /asyncquery) for the ARAGORN ARA,
    with Swagger documentation. Queries are answered by Strider over the knowledge
    providers it has registered (here including the Automat ROBOKOP KG, CAM-KP, ICEES,
    Ubergraph, GeLiNEA, Genetics KP, MolePro, OpenPredict and Text Mining KP co-occurrence),
    plus direct ROBOKOP KG lookups for inferred queries, SRI Node Normalizer identifier
    normalization and OmniCorp literature co-occurrence overlays for scoring.
  format: http
  id: aragorn.api
  name: ARAGORN API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: omnicorp
  - relation_type: prov:hadPrimarySource
    source: node-normalizer
  - relation_type: prov:hadPrimarySource
    source: cam-kp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: openpredict
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: strider
  product_url: https://aragorn.renci.org/docs
- category: ProgrammingInterface
  description: Production (NCATS ITRB) deployment of the ARAGORN TRAPI endpoint, with
    Swagger documentation. Like the RENCI deployment it queries knowledge providers
    through Strider, looks up the ROBOKOP KG via Automat, normalizes identifiers with
    the SRI Node Normalizer and scores answers with OmniCorp literature co-occurrence.
  format: http
  id: aragorn.api.itrb
  is_public: true
  name: ARAGORN Production API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: omnicorp
  - relation_type: prov:hadPrimarySource
    source: node-normalizer
  - relation_type: prov:hadPrimarySource
    source: cam-kp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: connections-hypothesis-kp
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: microbiomekg
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: strider
  product_url: https://aragorn.transltr.io/aragorn/docs
- category: GraphicalInterface
  description: The NCATS Translator user interface, which submits questions through
    the Autonomous Relay System (ARS) and displays merged, ranked answers from ARAGORN
    and the other Translator ARAs.
  format: http
  id: aragorn.ui
  name: ARAGORN User Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
  - relation_type: prov:hadPrimarySource
    source: ars
  product_url: https://ui.transltr.io/
- category: GraphicalInterface
  description: JSON index of the ARS production relay server and its registered agent
    endpoints.
  format: http
  id: ars.portal
  name: ARS Production Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ars
  - relation_type: prov:wasInformedBy
    source: aragorn
  - relation_type: prov:wasInformedBy
    source: arax
  - relation_type: prov:wasInformedBy
    source: cqs
  - relation_type: prov:wasInformedBy
    source: molepro
  - relation_type: prov:wasInformedBy
    source: cam-kp
  - relation_type: prov:wasInformedBy
    source: openpredict
  - relation_type: prov:wasInformedBy
    source: cohd
  - relation_type: prov:wasInformedBy
    source: icees-kg
  - relation_type: prov:wasInformedBy
    source: genetics-kp
  - relation_type: prov:wasInformedBy
    source: connections-hypothesis-kp
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  product_url: https://ars-prod.transltr.io/
- category: ProgrammingInterface
  connection_url: https://ars-prod.transltr.io/ars/api
  description: TRAPI-compatible ARS endpoint for asynchronous query submission.
  format: http
  id: ars.api
  is_public: true
  name: ARS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ars
  - relation_type: prov:wasInformedBy
    source: aragorn
  - relation_type: prov:wasInformedBy
    source: arax
  - relation_type: prov:wasInformedBy
    source: cqs
  - relation_type: prov:wasInformedBy
    source: molepro
  - relation_type: prov:wasInformedBy
    source: cam-kp
  - relation_type: prov:wasInformedBy
    source: openpredict
  - relation_type: prov:wasInformedBy
    source: cohd
  - relation_type: prov:wasInformedBy
    source: icees-kg
  - relation_type: prov:wasInformedBy
    source: genetics-kp
  - relation_type: prov:wasInformedBy
    source: connections-hypothesis-kp
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  product_url: https://ars-prod.transltr.io/ars/api/
- category: ProcessProduct
  description: Source code and templates implementing Curated Query Service inference
    logic.
  format: http
  id: cqs.code
  name: CQS Source Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cqs
  - relation_type: prov:wasInformedBy
    source: aragorn
  - relation_type: prov:wasInformedBy
    source: cohd
  - relation_type: prov:wasInformedBy
    source: molepro
  - relation_type: prov:wasInformedBy
    source: openpredict
  - relation_type: prov:wasInformedBy
    source: rtx-kg2
  - relation_type: prov:wasInformedBy
    source: cam-kp
  - relation_type: prov:wasInformedBy
    source: icees-kg
  - relation_type: prov:wasInformedBy
    source: text-mining-kp
  - relation_type: prov:wasInformedBy
    source: service-kp
  - relation_type: prov:wasInformedBy
    source: ctkp
  - relation_type: prov:wasInformedBy
    source: multiomics-kp
  product_url: https://github.com/TranslatorSRI/CQS
  warnings:
  - As of 2026-10-04 no CQS deployment responded (the transltr.io production host
    was unreachable; ci, test and RENCI dev hosts returned HTTP 404) and the repository
    had no commits since 2024-11-15, although the ARS production configuration still
    lists ara-cqs as an active agent.
- category: ProgrammingInterface
  description: TRAPI query endpoint for the ARAGORN ARA implementation within Shepherd (/query
    and /asyncquery), which answers queries with lookup, Omnicorp literature co-occurrence
    support and scoring operations over knowledge from Retriever.
  format: http
  id: shepherd.aragorn.api
  infores_id: shepherd-aragorn
  name: Shepherd ARAGORN TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasInfluencedBy
    source: aragorn
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/aragorn/docs
repository: https://github.com/ranking-agent/aragorn
synonyms:
- ARAGORN
- Autonomous Relay Agent for Generation Of Ranked Networks
tags:
- translator
---
# ARAGORN

## Overview

ARAGORN (Autonomous Relay Agent for Generation Of Ranked Networks) is an NCATS Translator Autonomous Relay Agent (ARA) that performs query operations by compiling and ranking data from multiple knowledge provider services.

As a key component of the Translator ecosystem, ARAGORN acts as an intelligent intermediary that receives biomedical questions, queries multiple underlying knowledge providers, aggregates results, performs inference reasoning, and returns ranked answers with supporting evidence.

## Key Features

- **Multi-Source Integration**: Queries multiple knowledge providers simultaneously
- **Answer Ranking**: Ranks and scores results based on evidence quality and confidence
- **Inference Reasoning**: Performs logical inference to discover indirect relationships
- **TRAPI Compliance**: Implements the Translator Reasoner API standard
- **Result Provenance**: Tracks and reports evidence sources for all answers
- **Subgraph Construction**: Builds knowledge graphs connecting query concepts

## Architecture

ARAGORN passes each query through a chain of sub-services
([source](https://github.com/ranking-agent/aragorn), [Translator wiki](https://github.com/NCATSTranslator/Translator-All/wiki/ARAGORN)):

- **Strider** builds a query plan and sends one-hop queries to the knowledge providers registered in SmartAPI (the live list is at https://strider.renci.org/kps and https://strider.transltr.io/kps), then assembles results.
- **ROBOKOP KG lookup**: for inferred ("creative") queries, ARAGORN applies mined rules and queries the ROBOKOP KG directly through Automat.
- **SRI Node Normalizer** supplies preferred identifiers and equivalents.
- **Answer Coalesce** (optional) groups answers by property, graph or ontology.
- **ARAGORN Ranker** adds OmniCorp literature co-occurrence overlays and scores results (0 to 1).

## Products

### ARAGORN API
TRAPI endpoint hosted at RENCI (https://aragorn.renci.org/docs).

### ARAGORN Production API
NCATS ITRB production deployment (https://aragorn.transltr.io/aragorn/docs).

### ARAGORN User Interface
The Translator UI (https://ui.transltr.io/), which shows ARAGORN answers alongside those of the other ARAs via the ARS.

## Information Resource ID

This resource has the Information Resource identifier: `infores:aragorn`

## Repository

Source code and documentation: https://github.com/ranking-agent/aragorn (MIT License)

## Contacts

- Chris Bizon (RENCI), responsible developer: bizon@renci.org

## Domains

- Biomedical
- Information Technology

## Tags

- NCATS Translator
