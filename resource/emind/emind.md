---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://research.bioinformatics.udel.edu/"
    label: University of Delaware
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://proteininformationresource.org/"
    label: Protein Information Resource
creation_date: '2026-05-20T00:00:00Z'
description: eMIND is a University of Delaware and Protein Information Resource text-mining workflow for extracting protein-coding variant impacts in Alzheimer's disease and related dementias from the biomedical literature.
domains:
  - biomedical
  - genomics
homepage_url: https://research.bioinformatics.udel.edu/itextmine/emind
id: "emind"
last_modified_date: '2026-05-21T00:00:00Z'
layout: resource_detail
name: eMIND
products:
  - category: GraphicalInterface
    description: Web interface for browsing eMIND text-mined variant-impact annotations in Alzheimer's disease and related dementia literature
    format: http
    id: "emind.site"
    name: eMIND Web Interface
    original_source:
      - source: emind
        relation_type: prov:hadPrimarySource
      - source: pubtator
        relation_type: prov:wasDerivedFrom
    product_url: https://research.bioinformatics.udel.edu/itextmine/integrate/search/emind/medline/*
  - category: Product
    description: Gzipped JSON export of the eMIND text-mined literature annotations for variant impacts in Alzheimer's disease and related dementias
    format: json
    id: "emind.json"
    name: eMIND JSON Export
    original_source:
      - source: emind
        relation_type: prov:hadPrimarySource
      - source: pubtator
        relation_type: prov:wasDerivedFrom
    product_url: https://hershey.dbi.udel.edu/textmining/export/emind/eMIND_iTextmine.json.gz
publications:
  - authors:
      - Gupta S
      - Qin X
      - Wang Q
      - Cowart J
      - Huang H
      - Wu CH
      - Vijay-Shanker K
      - Arighi CN
    id: "doi:10.1101/2023.09.07.556602"
    journal: bioRxiv
    preferred: true
    title: 'eMIND: Enabling automatic collection of protein variation impacts in Alzheimer''s disease from the literature'
    year: "2023"
---

# eMIND

eMIND is a deep learning-based text-mining workflow for detecting and organizing variant-impact evidence from the Alzheimer’s disease and related dementias literature. The public site is hosted by the University of Delaware and states that the workflow was developed with support from an NIA supplement to UniProt focused on improving functional genomics data access for AD and dementia-related protein research communities.

The current public interface provides a browseable literature view and a direct JSON export. Public project documentation describes a pipeline that combines PubTator entity extraction, BERT-based impact classification, typed impact assignment, ontology mapping, and post-processing into a final structured output used to expand the UniProtKB computationally mapped bibliography.

## Access

- Browse annotations: [eMIND browse interface](https://research.bioinformatics.udel.edu/itextmine/integrate/search/emind/medline/*)
- Download JSON: [eMIND_iTextmine.json.gz](https://hershey.dbi.udel.edu/textmining/export/emind/eMIND_iTextmine.json.gz)

## Automated Evaluation

- View the automated evaluation: [emind automated evaluation](emind_eval_automated.html)
