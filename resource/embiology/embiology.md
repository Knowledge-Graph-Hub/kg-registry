---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.elsevier.support/embiology
      - contact_type: url
        value: https://www.elsevier.support/embiology/contact
    label: Elsevier
description: EmBiology is a commercial, web-based knowledge graph platform from Elsevier that surfaces biological relationships across entities such as genes, proteins, diseases, cells, and more. It is powered by Elsevier's Biology Knowledge Graph, built from more than 7.2 million full-text journal articles (Elsevier and third-party publishers), 34.5 million abstracts, and 430,000 clinical trial records (with trial details drawn from ClinicalTrials.gov). EmBiology connects 1.4 million entities via 15.7 million relationships and provides 87.2 million referenced facts (figures reported by Elsevier), with weekly updates and annual rescans of the corpus. It uses NLP (including the TERMite engine) and expert curation to extract and quality-control relationships from full-text scientific literature and other sources, and offers interactive visualization (e.g., Sankey diagrams) and filtering to support discovery and decision-making in drug research and biology.
domains:
  - biomedical
  - drug discovery
  - literature
homepage_url: https://www.embiology.com/
id: embiology
infores_id: embiology
layout: resource_detail
license:
  id: https://www.elsevier.com/legal/elsevier-website-terms-and-conditions
  label: Elsevier Website Terms and Conditions
name: EmBiology
products:
  - category: GraphicalInterface
    description: Web interface for exploring biological relationships in EmBiology
    format: http
    id: embiology.web
    name: EmBiology Web Interface
    product_url: https://www.embiology.com/
    original_source:
      - source: embiology
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
taxon:
  - NCBITaxon:9606
creation_date: '2025-08-12T00:00:00Z'
last_modified_date: '2026-10-27T00:00:00Z'
---

# EmBiology

## Overview

EmBiology is a commercial Elsevier platform, launched in April 2023, for exploring relationships between biological entities such as genes, proteins, diseases, cells, and drugs. It is powered by Elsevier's Biology Knowledge Graph, which uses NLP and expert curation to extract relationships, including directionality and effect, from more than 7.2 million full-text journal articles from Elsevier and third-party publishers, 34.5 million abstracts, and 430,000 clinical trials. Clinical trial details in the interface are drawn from ClinicalTrials.gov. Elsevier reports 1.4 million entities connected by 15.7 million relationships, with weekly updates.

Results are summarized in interactive Sankey diagrams and heatmaps, with filters for narrowing results and links to supporting references.

## Access

- Web application (subscription required): [EmBiology](https://www.embiology.com/)
- Support center: [EmBiology Support Center](https://www.elsevier.support/embiology)
- Launch announcement: [Elsevier press release](https://www.elsevier.com/about/press-releases/elsevier-launches-embiology-to-deliver-the-unparalleled-insights-into-biological-activities-that-accelerate-drug-discovery)

## Evaluation

- View the evaluation: [embiology evaluation](embiology_eval.html)
