---
activity_status: unknown
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://case.edu/medicine/aicenter/about/faculty-and-staff/rong-xu
    label: Xu Lab, Case Western Reserve University
creation_date: '2026-06-18T00:00:00Z'
description: TreatKB is a text-mined knowledge base of drug-treats-disease relationships developed by the Rong Xu lab at Case Western Reserve University. Treatment pairs are extracted by combining evidence from the FDA Adverse Event Reporting System (FAERS), FDA drug labels, MEDLINE/PubMed literature, and clinical trials. It has no standalone public homepage or portal and exists as a research-lab resource described in publications. TreatKB was used as a source to construct GP-KG.
domains:
  - drug discovery
  - clinical
  - literature
  - pharmacology
homepage_url: https://case.edu/medicine/aicenter/about/faculty-and-staff/rong-xu
id: treatkb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: TreatKB
products:
  - category: DocumentationProduct
    description: Peer-reviewed publication from the Xu lab describing the large-scale text-mining method used to extract accurate drug-disease treatment pairs from biomedical literature, the approach underlying TreatKB.
    id: treatkb.publication
    name: TreatKB Method Publication
    original_source:
      - relation_type: prov:hadPrimarySource
        source: treatkb
    product_url: https://doi.org/10.1186/1471-2105-14-181
publications:
  - authors:
      - Rong Xu
      - QuanQiu Wang
    doi: 10.1186/1471-2105-14-181
    id: doi:10.1186/1471-2105-14-181
    journal: BMC Bioinformatics
    preferred: true
    title: Large-scale extraction of accurate drug-disease treatment pairs from biomedical literature for drug repurposing
    year: '2013'
---

# TreatKB

## Overview

TreatKB is a text-mined knowledge base of drug-treats-disease relationships built by the Rong Xu lab at Case Western Reserve University. It compiles treatment pairs by integrating evidence from multiple biomedical sources, including the FDA Adverse Event Reporting System (FAERS), FDA drug labels, MEDLINE/PubMed literature, and clinical trials.

## Availability

TreatKB does not have a standalone public homepage or download portal. It is a research-lab resource described in Xu lab publications rather than a maintained, independently distributed database, so its current maintenance status is unknown. The Xu lab faculty page is listed as the best available point of reference.

## Use

TreatKB has been used as a source dataset in the construction of GP-KG.
