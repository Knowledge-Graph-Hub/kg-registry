---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bridge2ai.org/
  label: Bridge2AI Consortium
creation_date: '2026-07-01T00:00:00Z'
description: Bridge to Artificial Intelligence (Bridge2AI) is an NIH Common Fund program
  that generates new flagship biomedical and behavioral data sets that are ethically
  sourced, trustworthy, well-defined, and accessible for widespread use by researchers
  applying artificial intelligence and machine learning. The program produces AI/ML-ready
  data across multiple domains, together with standards, tools, and best practices
  for creating and using such data, and disseminates the resulting data, models, and
  ethical frameworks to the broader research community.
domains:
- biomedical
- clinical
- information technology
homepage_url: https://bridge2ai.org/
id: bridge2ai
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: Bridge to Artificial Intelligence (Bridge2AI)
products:
- category: GraphicalInterface
  description: Main Bridge2AI program portal providing access to program information,
    generated AI/ML-ready data sets, standards, and tools
  format: http
  id: bridge2ai.portal
  name: Bridge2AI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bridge2ai
  product_url: https://bridge2ai.org/
- category: GraphProduct
  description: Statistically inferred genomic evidence graph connecting genes, gene
    sets, inferred disease mechanisms, and human phenotypes. Gene sets are derived
    from eleven NIH Common Fund programs (GlyGen, GTEx, IDG, IMPC/KOMP2, LINCS, MoTrPAC,
    Bridge2AI, HuBMAP, Metabolomics Workbench, SenNet, and SPARC) and phenotype-gene
    set relationships are computed with PIGEAN (Priors Inferred from GEne ANnotations).
  format: http
  id: digcfdekg.graph
  name: CFDE REVEAL Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: digcfdekg
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: bridge2ai
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: sparc
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hubmap
- category: GraphProduct
  description: The CM4AI Talent Knowledge Graph connecting Bridge2AI and CM4AI researchers,
    projects, publications, datasets, and bio-entities.
  format: ttl
  id: cm4ai_talent_kg.graph
  name: CM4AI Talent Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cm4ai_talent_kg
  - relation_type: prov:hadPrimarySource
    source: pubmed-knowledge-graph
  - relation_type: prov:hadPrimarySource
    source: semantic-scholar
  product_url: https://cm4aikg.vercel.app/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: orcid
  - relation_type: prov:wasInfluencedBy
    source: bridge2ai
publications:
- authors:
  - Timothy Clark
  - Harry Caufield
  - Jillian A Parker
  - Sadnan Al Manir
  - Edilberto Amorim
  - James Eddy
  - Nayoon Gim
  - Brian Gow
  - Wesley Goar
  - Jan N Hansen
  - Nomi Harris
  - Henning Hermjakob
  - Marcin Joachimiak
  - Gianna Jordan
  - In-Hee Lee
  - Shannon K McWeeney
  - Camille Nebeker
  - Milen Nikolov
  - Sarah J Ratcliffe
  - Justin Reese
  - Jamie Shaffer
  - Nathan Sheffield
  - Gloria Sheynkman
  - James Stevenson
  - Jake Y Chen
  - Chris Mungall
  - Alex Wagner
  - Sek Won Kong
  - Satrajit S Ghosh
  - Bhavesh Patel
  - Andrew Williams
  - Monica C Munoz-Torres
  doi: 10.1101/2024.10.23.619844
  id: https://www.ncbi.nlm.nih.gov/pubmed/39484409
  journal: bioRxiv
  preferred: true
  title: 'AI-readiness for Biomedical Data: Bridge2AI Recommendations'
  year: '2024'
repository: https://github.com/bridge2ai
synonyms:
- Bridge2AI
- Bridge to Artificial Intelligence
---
# Bridge to Artificial Intelligence (Bridge2AI)

## Overview

Bridge to Artificial Intelligence (Bridge2AI) is an NIH Common Fund program that
propels biomedical research forward by generating new flagship data sets and best
practices for the ethical and rigorous application of artificial intelligence (AI)
and machine learning (ML).

The program brings together biomedical and behavioral researchers with experts in
AI, data science, and ethics to produce large, high-quality, AI/ML-ready data sets
that are ethically sourced, trustworthy, well-defined, and broadly accessible.

## Key Features

- **AI/ML-Ready Data**: Flagship data sets designed from the outset for machine
  learning use
- **Data Generation Projects**: Multiple grand-challenge data generation projects
  spanning diverse biomedical and behavioral domains
- **Standards and Tools**: Development of standards, software, and best practices
  for creating and using AI/ML-ready data
- **Ethics and Trustworthiness**: Emphasis on ethically sourced and well-documented
  data

## Products

### Bridge2AI Portal
Program portal providing access to information, generated data sets, standards, and
tools produced by the Bridge2AI consortium.