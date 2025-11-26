---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: The Translator Curated Query Service (CQS) is an SRI service providing ARA-like reasoning capabilities through customizable inference rules captured as templates, generating predicted edges with provenance metadata and scoring.
domains:
  - biomedical
id: "cqs"
infores_id: "cqs"
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: Translator Curated Query Service
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Translator-Curated-Query-Service
synonyms:
  - CQS
  - Curated Query Service
contacts:
  - category: Organization
    label: NCATS Biomedical Data Translator
    contact_details:
      - contact_type: url
        value: "https://ncats.nih.gov/translator"
---

# Translator Curated Query Service

## Overview

The Translator Curated Query Service (CQS) is a Standards and Reference Implementation (SRI) service within the NCATS Biomedical Data Translator program. It provides Autonomous Reasoning Agent (ARA)-like capabilities through customizable inference rules, generating predicted biomedical relationships with comprehensive provenance tracking and confidence scoring.

## Key Features

- **Template-Based Inference**: Customizable inference rules captured as CQS templates
- **Predicted Edge Generation**: Creates inferred relationships from existing knowledge
- **Provenance Tracking**: Links predictions to supporting auxiliary graphs
- **Metadata Attachment**: Comprehensive provenance and evidence metadata
- **Result Scoring**: Confidence scoring for generated predictions
- **TRAPI-Compatible**: Implements Translator Reasoner API standard
- **Query Pattern Support**: Handles complex multi-hop reasoning queries

## Core Capabilities

### Inference Templates

- **Customizable Rules**: Domain experts define inference patterns
- **Pattern Matching**: Identifies applicable inference rules for queries
- **Multi-Hop Reasoning**: Chains multiple inference steps
- **Evidence Aggregation**: Combines support from multiple knowledge sources

### Prediction Generation

- **Edge Prediction**: Infers new biomedical relationships not explicitly stated in data
- **Confidence Assessment**: Scores predictions based on evidence strength
- **Support Graph Construction**: Builds auxiliary graphs showing reasoning chains
- **Result Ranking**: Orders predictions by confidence and evidence quality

### Provenance and Metadata

- **Source Attribution**: Tracks data sources supporting each prediction
- **Reasoning Path**: Documents the inference steps taken
- **Evidence Codes**: Standardized codes indicating evidence types
- **Confidence Scores**: Quantitative measures of prediction reliability

## Use Cases

### Hypothesis Generation

- Discovering novel drug-disease associations
- Identifying potential drug repurposing opportunities
- Finding mechanistic connections between entities
- Exploring indirect relationships in biomedical knowledge

### Knowledge Gap Filling

- Inferring missing relationships from existing knowledge
- Predicting unknown mechanisms of action
- Connecting disparate areas of biomedical knowledge
- Generating testable hypotheses for experimental validation

### Clinical Translation

- Supporting precision medicine decisions
- Identifying potential therapeutic interventions
- Understanding disease mechanisms
- Predicting treatment outcomes

## Technical Architecture

### Query Processing

1. **Query Reception**: Receives TRAPI-formatted queries
2. **Template Matching**: Identifies applicable inference templates
3. **Rule Application**: Applies inference rules to generate predictions
4. **Graph Construction**: Builds auxiliary graphs showing reasoning
5. **Scoring**: Computes confidence scores for predictions
6. **Response Formatting**: Returns TRAPI-compliant results

### Template System

- **Rule Definition**: Expert-curated inference patterns
- **Pattern Syntax**: Structured representation of reasoning rules
- **Condition Specification**: Criteria for rule applicability
- **Action Definition**: Operations to perform when rules match

### Integration Points

- **Knowledge Providers (KPs)**: Queries underlying data sources
- **Other ARAs**: Can be chained with other reasoning services
- **ARS**: Integrated with Autonomous Relay System
- **User Interfaces**: Accessible through Translator UIs

## Information Resource ID

This resource has the Information Resource identifier: `infores:cqs`

## Access

- **Documentation**: https://github.com/NCATSTranslator/Translator-All/wiki/Translator-Curated-Query-Service
- **API**: Available through Translator infrastructure
- **TRAPI Endpoint**: Implements standard Translator Reasoner API

For more information about the NCATS Biomedical Data Translator, visit https://ncats.nih.gov/translator
