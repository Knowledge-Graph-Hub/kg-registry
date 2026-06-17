---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.aminode.org/
  label: Aminode
creation_date: '2026-06-17T00:00:00Z'
description: Aminode performs evolutionary profiling of proteins and provides a
  user-friendly web tool for the routine and rapid inference of evolutionarily
  constrained regions (ECRs) in the human proteome, based on comparisons across
  many species.
domains:
- proteomics
homepage_url: http://www.aminode.org/
id: aminode
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: Aminode
products:
- category: GraphicalInterface
  description: Web tool for inferring evolutionarily constrained regions in human
    proteins.
  format: http
  id: aminode.site
  is_public: true
  name: Aminode Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aminode
  product_url: http://www.aminode.org/
publications:
- authors:
  - Kevin T. Chang
  - Junyan Guo
  - Alberto di Ronza
  - Marco Sardiello
  doi: 10.1038/s41598-018-19744-w
  id: https://doi.org/10.1038/s41598-018-19744-w
  journal: Scientific Reports
  preferred: true
  title: 'Aminode: Identification of Evolutionary Constraints in the Human Proteome'
  year: '2018'
---
# Aminode

Aminode is a web tool for the evolutionary profiling of proteins. By aligning each human
protein against orthologs from many species, it identifies evolutionarily constrained
regions (ECRs) - stretches of amino acids that have changed little over evolutionary time
and are therefore likely to be functionally important.

Features include:

- Rapid inference of evolutionarily constrained regions for human proteins
- Per-residue evolutionary constraint profiles
- A simple web interface for routine analyses

GeneCards integrates evolutionary constraint profiles from Aminode.
