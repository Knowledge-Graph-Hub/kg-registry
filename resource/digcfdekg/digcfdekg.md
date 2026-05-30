---
id: digcfdekg
name: CFDE REVEAL Knowledge Graph
description: CFDE REVEAL is a statistically inferred genomic evidence knowledge graph that links Common Fund gene sets, genes, inferred disease mechanisms, and human phenotypes to support mechanistic hypothesis generation within the Common Fund Data Ecosystem.
activity_status: active
homepage_url: https://cfdeknowledge.org/
collection:
- okn
domains:
- biomedical
- genomics
- health
- systems biology
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-05-09T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
contacts:
- category: Individual
  label: Jason Flannick
  contact_details:
  - contact_type: email
    value: flannick@broadinstitute.org
  - contact_type: github
    value: flannick
- category: Individual
  label: Noel Burtt
  contact_details:
  - contact_type: email
    value: burtt@broadinstitute.org
products:
- id: digcfdekg.portal
  name: CFDE REVEAL Portal
  description: CFDE Knowledge Center web application for natural-language exploration of mechanistic leads, evidence, and hypothesis-generation workflows backed by the CFDE REVEAL graph.
  category: GraphicalInterface
  format: http
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  original_source:
  - source: digcfdekg
    relation_type: prov:hadPrimarySource
---
CFDE REVEAL Knowledge Graph

## Description

CFDE REVEAL is a Common Fund Data Ecosystem knowledge graph that connects genes,
gene sets, inferred disease mechanisms, and human phenotypes to support
mechanistic interpretation of cross-program biomedical evidence. The graph uses
Bayesian inference workflows described on the OKN registry page, including
PIGEAN for gene-trait evidence and latent-factor modeling of disease
mechanisms, to turn integrated CFDE evidence into queryable associations.

The CFDE Knowledge Center presents REVEAL as a hypothesis-generation workflow
that combines semantic search, statistical genetics, and LLM-assisted reasoning
to connect Common Fund resources with plausible mechanistic leads.

*This resource was automatically synchronized from the FRINK OKN registry.*
