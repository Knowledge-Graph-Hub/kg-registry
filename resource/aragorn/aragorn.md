---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://github.com/NCATSTranslator/Translator-All/wiki/ARAGORN
    label: NCATS Translator
creation_date: '2025-11-05T00:00:00Z'
description: ARAGORN (Autonomous Relay Agent for Generation Of Ranked Networks) is an NCATS Translator Autonomous Relay Agent (ARA) that performs query operations by compiling and ranking data from multiple ARAGORN-affiliated knowledge provider services. ARAGORN acts as an intermediary between user queries and underlying knowledge providers, aggregating results, performing inference, and ranking answers based on evidence and confidence scores. It implements the Translator Reasoner API (TRAPI) standard for biomedical question-answering.
domains:
  - biomedical
  - information technology
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/ARAGORN
id: aragorn
infores_id: aragorn
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/mit/
  label: MIT
name: ARAGORN
products:
- category: ProgrammingInterface
  description: TRAPI-compliant API documentation for biomedical question answering
  format: http
  id: aragorn.api
  name: ARAGORN API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
  product_url: https://aragorn.renci.org/docs
- category: GraphicalInterface
  description: Web interface for querying ARAGORN
  format: http
  id: aragorn.ui
  name: ARAGORN User Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
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

ARAGORN operates as an intermediary layer in the Translator architecture:
- Receives biomedical questions in TRAPI format
- Distributes queries to affiliated knowledge providers
- Aggregates and normalizes results
- Applies ranking algorithms based on evidence
- Returns structured answers with provenance

## Products

### ARAGORN API
TRAPI-compliant RESTful API endpoint for submitting biomedical questions and receiving ranked answers from integrated knowledge sources.

### ARAGORN User Interface
Web-based interface accessible through the Translator UI for interactive exploration of ARAGORN query capabilities.

## Information Resource ID

This resource has the Information Resource identifier: `infores:aragorn`

## Repository

Source code and documentation: https://github.com/ranking-agent/aragorn

Live API documentation: https://aragorn.renci.org/docs

## Domains

- Biomedical
- Translational
- Information Technology

## Tags

- NCATS Translator