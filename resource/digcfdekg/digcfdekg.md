---
id: digcfdekg
name: CFDE REVEAL Knowledge Graph
description: The CFDE REVEAL Knowledge Graph is a statistically inferred genomic evidence
  graph to integrate and disseminate knowledge within the Common Fund Data Ecosystem
  (CFDE).
activity_status: active
homepage_url: https://cfdeknowledge.org/
collection:
- okn
domains:
- biomedical
- genomics
- systems biology
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-05-09T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
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
  description: CFDE Knowledge Center web application for natural-language exploration
    of mechanistic leads, evidence, and hypothesis-generation workflows backed by
    the CFDE REVEAL graph.
  category: GraphicalInterface
  format: http
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  original_source:
  - source: digcfdekg
    relation_type: prov:hadPrimarySource
- id: digcfdekg.graph
  name: CFDE REVEAL Knowledge Graph
  description: Statistically inferred genomic evidence graph connecting genes, gene
    sets, inferred disease mechanisms, and human phenotypes. Gene sets are derived
    from eleven NIH Common Fund programs (GlyGen, GTEx, IDG, IMPC/KOMP2, LINCS, MoTrPAC,
    Bridge2AI, HuBMAP, Metabolomics Workbench, SenNet, and SPARC) and phenotype-gene
    set relationships are computed with PIGEAN (Priors Inferred from GEne ANnotations).
  category: GraphProduct
  format: http
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  original_source:
  - source: digcfdekg
    relation_type: prov:hadPrimarySource
  - source: glygen
    relation_type: prov:hadPrimarySource
  - source: gtex
    relation_type: prov:hadPrimarySource
  - source: tcrd
    relation_type: prov:hadPrimarySource
  - source: impc
    relation_type: prov:hadPrimarySource
  - source: lincs
    relation_type: prov:hadPrimarySource
  - source: motrpac
    relation_type: prov:hadPrimarySource
  - source: bridge2ai
    relation_type: prov:hadPrimarySource
  - source: mw
    relation_type: prov:hadPrimarySource
  - source: sennet
    relation_type: prov:hadPrimarySource
  - source: sparc
    relation_type: prov:hadPrimarySource
  secondary_source:
  - source: hubmap
    relation_type: prov:wasInfluencedBy
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
