---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: CACAO is a Gene Ontology annotation competition from Texas A&M University in which students curate GO annotations for UniProt proteins from published papers, with evidence codes from the Evidence and Conclusion Ontology. Run from 2010 to 2020 as the Community Assessment of Community Annotation with Ontologies on the GONUTS wiki, it relaunched in 2024 as Creating Annotations through Critical Analysis of Original research at cacao.wiki. Accepted annotations are contributed to the Gene Ontology Consortium; QuickGO lists 4,373 annotations assigned by CACAO.
domains:
  - genomics
id: "cacao"
infores_id: "cacao"
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: CACAO
homepage_url: https://cacao.wiki/
synonyms:
  - CACAO
  - Community Assessment of Community Annotation with Ontologies
  - Creating Annotations through Critical Analysis of Original research
products:
  - category: GraphicalInterface
    description: CACAO annotation competition platform (relaunched 2024), where students create and review GO annotations.
    format: http
    id: cacao.portal
    name: CACAO Platform
    original_source:
      - source: cacao
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: eco
        relation_type: prov:hadPrimarySource
    product_url: https://cacao.wiki/
  - category: Product
    description: GO annotations contributed by CACAO curators and distributed through the Gene Ontology and GOA (assigned_by CACAO); browsable in QuickGO.
    format: http
    id: cacao.go-annotations
    name: CACAO GO Annotations
    original_source:
      - source: cacao
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: eco
        relation_type: prov:hadPrimarySource
    product_url: https://www.ebi.ac.uk/QuickGO/annotations?assignedBy=CACAO
  - category: GraphicalInterface
    description: Archived GONUTS wiki category for the original CACAO competitions (2010-2020).
    format: http
    id: cacao.gowiki
    name: CACAO GO Wiki Page
    original_source:
      - source: cacao
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: eco
        relation_type: prov:hadPrimarySource
    product_url: https://gowiki.tamu.edu/wiki/index.php/Category:CACAO
  - category: ProgrammingInterface
    connection_url: https://gowiki.tamu.edu/wiki/api.php
    description: MediaWiki API endpoint for accessing CACAO and related GO Wiki content programmatically.
    format: http
    id: cacao.api
    is_public: true
    name: GONUTS MediaWiki API
    original_source:
      - source: cacao
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: eco
        relation_type: prov:hadPrimarySource
    product_url: https://gowiki.tamu.edu/wiki/api.php
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://cacao.wiki/
      - contact_type: email
        value: ecoliwiki@gmail.com
    label: CACAO, Texas A&M University
  - category: Individual
    contact_details:
      - contact_type: github
        value: dsiegele
    label: Deborah A. Siegele
  - category: Individual
    contact_details:
      - contact_type: github
        value: jrr-cpt
    label: Jolene Ramsey
publications:
  - authors:
      - Jolene Ramsey
      - Brenley McIntosh
      - Daniel Renfro
      - Deborah A Siegele
      - James C Hu
    doi: 10.1371/journal.pcbi.1009463
    id: doi:10.1371/journal.pcbi.1009463
    journal: PLoS Computational Biology
    preferred: true
    title: 'Crowdsourcing biocuration: The Community Assessment of Community Annotation with Ontologies (CACAO)'
    year: '2021'
  - authors:
      - Daniel P Renfro
      - Brenley K McIntosh
      - Anand Venkatraman
      - Deborah A Siegele
      - James C Hu
    doi: 10.1093/nar/gkr907
    id: doi:10.1093/nar/gkr907
    journal: Nucleic Acids Research
    title: 'GONUTS: the Gene Ontology Normal Usage Tracking System'
    year: '2012'
---

# Community Assessment of Community Annotation with Ontologies

## Overview

CACAO (Community Assessment of Community Annotation with Ontologies) was an educational and collaborative annotation project that engaged undergraduate students in the process of biological curation using the Gene Ontology (GO). Students learned to annotate proteins by extracting evidence from scientific literature and applying standardized ontology terms.

## Project Goals

- **Education**: Train undergraduate students in biocuration and scientific literature analysis
- **Community Engagement**: Involve the broader scientific community in annotation efforts
- **Quality Assessment**: Evaluate the quality of community-contributed annotations
- **GO Annotation**: Contribute to the Gene Ontology annotation corpus

## Methodology

- Students read and analyzed scientific papers
- Extracted evidence for protein function
- Applied appropriate Gene Ontology terms
- Documented evidence codes and supporting references
- Annotations were reviewed for quality and consistency

## Educational Value

- Hands-on experience with scientific literature
- Understanding of controlled vocabularies and ontologies
- Critical thinking about biological evidence
- Contribution to real scientific resources
- Introduction to bioinformatics and data curation

## Activity Status

The CACAO project appears to be inactive. The project website at gowiki.tamu.edu is no longer accessible, and recent updates or publications are not available. The project represents an important historical effort in community-based biocuration and educational outreach.

## Related Resources

- **Gene Ontology**: The ontology system used for annotations
- **GOC (Gene Ontology Consortium)**: Maintains GO and coordinates curation efforts
- **GONUTS**: Related community annotation project

## Legacy

CACAO demonstrated the potential for engaging students and community members in scientific annotation while providing valuable educational experiences in biocuration and biological data standards.
