---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biothings.ncats.io/gtrx
  label: NCATS Translator
creation_date: '2025-11-05T00:00:00Z'
description: Genome-to-Treatment (GTRx) is a NCATS Translator knowledge provider exposed
  through a BioThings API. It contains recommended acute treatments and interventions
  for seriously ill newborns, infants, and children with newly diagnosed genetic diseases,
  including therapeutics, dietary changes, surgery, medical devices, and other interventions.
domains:
- genomics
- pharmacology
- precision medicine
- translational
- biomedical
homepage_url: https://biothings.ncats.io/gtrx
id: gtrx
infores_id: gtrx
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Genome-to-Treatment
products:
- category: ProgrammingInterface
  connection_url: https://biothings.ncats.io/gtrx/query
  description: BioThings API for querying Genome-to-Treatment association records
    through `/query`, `/metadata`, and related BioThings endpoints
  format: json
  id: gtrx.api
  infores_id: biothings-gtrx
  is_public: true
  latest_version: '2022-02-01'
  name: gTRx API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrx
  product_url: https://biothings.ncats.io/gtrx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biothings
- category: Product
  description: BioThings GTRx association collection built from Genome-to-Treatment
    source records; the 20220802 build reports 695 association records
  format: mixed
  id: gtrx.data
  latest_version: '20220802'
  name: gTRx Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrx
  product_url: https://biothings.ncats.io/gtrx/metadata
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ncbigene
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: pubchem
  warnings:
  - The historical source website reported in the BioThings metadata, https://gtrx.rbsapp.net/about.html,
    returned HTTP 404 during curation on 2026-06-02.
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 405 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 405 error
    when accessing file'
publications:
- authors:
  - Mallory J. Owen
  - Sebastien Lefebvre
  - Christian Hansen
  - Chris M. Kunard
  - David P. Dimmock
  - Laurie D. Smith
  - Gunter Scharer
  - Rebecca Mardach
  doi: 10.1038/s41467-022-31446-6
  id: doi:10.1038/s41467-022-31446-6
  journal: Nature Communications
  preferred: true
  title: An automated 13.5 hour system for scalable diagnosis and acute management
    guidance for genetic diseases
  year: '2022'
repository: https://github.com/biothings/GTRx
synonyms:
- gTRx
- GTRx
- Genome-to-Treatment
tags:
- translator
taxon:
- NCBITaxon:9606
---
# Genome-to-Treatment

## Overview

Genome-to-Treatment (GTRx) is a NCATS Translator knowledge provider exposed through
the BioThings API framework. It provides association records for acute management
guidance in genetic diseases, including drugs, dietary changes, procedures, medical
devices, and other interventions.

## Key Features

- **Genomic-Drug Connections**: Links genetic variants to drug responses and treatment options
- **Precision Medicine Focus**: Supports personalized treatment recommendations based on genomic profiles
- **Multi-Source Integration**: Aggregates data from genomic databases, pharmacological resources, and clinical studies
- **Translator Integration**: Registered in the Translator ecosystem as `infores:gtrx`
  and exposed as the BioThings GTRx API
- **Evidence-Based**: Curates relationships with supporting evidence from literature and clinical data

## Use Cases

- Identifying potential drug treatments based on genomic alterations
- Exploring pharmacogenomic relationships
- Supporting clinical decision-making in precision oncology and other therapeutic areas
- Discovering drug repurposing opportunities based on genetic mechanisms

## Products

### gTRx API
BioThings API endpoint providing programmatic access to Genome-to-Treatment
association records for integration into Translator workflows.

### gTRx Data
Integrated BioThings association records connecting genetic diseases with acute
management interventions.

## Information Resource ID

This resource has the Information Resource identifier: `infores:gtrx`

## Domains

- Genomics
- Pharmacology
- Precision Medicine
- Translational
- Biomedical

## Tags

- NCATS Translator