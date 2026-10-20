---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://linkeddiscoveries.ncbi.nlm.nih.gov/
  id: ncbi
  label: National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-20T00:00:00Z'
description: Linked Discoveries is an experimental pilot tool from the National Library
  of Medicine, launched in September 2026 as part of the NIH replication and reproducibility
  initiative. Starting from a PubMed citation, it builds a neighborhood of closely
  related publications, including replication studies, and highlights shared conditions,
  genes, and chemicals, NIH funding, citation relationships, retractions, and reviews.
  It draws on PubMed together with linked data from NCBI Gene, MedGen, and PubChem,
  and covers more than 29 million PubMed publications.
domains:
- literature
- scholarly communication
- biomedical
homepage_url: https://linkeddiscoveries.ncbi.nlm.nih.gov/
id: linked-discoveries
last_modified_date: '2026-10-20T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain
name: Linked Discoveries
products:
- category: GraphicalInterface
  description: Interactive web interface for exploring the neighborhood of related
    publications around a PubMed citation as a graph or a timeline, with shared conditions
    (MedGen), genes (NCBI Gene), and chemicals (PubChem), NIH funding, citation links,
    retractions, and reviews.
  format: http
  id: linked-discoveries.site
  is_public: true
  name: Linked Discoveries Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: linked-discoveries
  product_url: https://linkeddiscoveries.ncbi.nlm.nih.gov/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: medgen
  - relation_type: prov:wasDerivedFrom
    source: pubchem
synonyms:
- NIH Linked Discoveries
- NLM Linked Discoveries
---
# Linked Discoveries

## Overview

Linked Discoveries is an experimental pilot resource developed by the National Library of Medicine (NLM) and hosted by NCBI. NIH launched it on September 24, 2026 as an early product of its agency-wide effort on replication and reproducibility. It helps users see how an individual research finding relates to the wider body of biomedical evidence, which conventional literature searches can obscure by favoring prominent or highly cited work.

## Data Content

Starting from an article with a PubMed abstract, Linked Discoveries assembles a "neighborhood" of closely related publications, including replication studies. Across the neighborhood it highlights:

- Shared conditions, genes, and chemicals, linked from MedGen, NCBI Gene, and PubChem
- NIH funding
- Citation relationships
- Retractions and reviews

More than 29 million PubMed publications are represented. The tool identifies connections between publications only; it does not judge study quality or decide whether a finding has been successfully replicated.

## Access

- Web interface: [linkeddiscoveries.ncbi.nlm.nih.gov](https://linkeddiscoveries.ncbi.nlm.nih.gov/), with graph and timeline views

No API or bulk download had been announced as of October 2026.
