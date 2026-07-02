---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ntp.niehs.nih.gov/whatwestudy/niceatm
  label: NICEATM (NTP Interagency Center for the Evaluation of Alternative Toxicological
    Methods)
creation_date: '2026-07-01T00:00:00Z'
description: The Integrated Chemical Environment (ICE) is a resource developed by
  the NTP Interagency Center for the Evaluation of Alternative Toxicological Methods
  (NICEATM), part of the National Toxicology Program (NTP) at the National Institute
  of Environmental Health Sciences (NIEHS). ICE provides curated chemical data, in
  vitro assay data, and computational tools and workflows that support chemical safety
  assessment and toxicological evaluation, including predictions of in vivo toxicity
  from in vitro and in silico data. It is intended to help scientists develop and
  evaluate new approach methodologies (NAMs) for chemical hazard characterization.
domains:
- chemistry and biochemistry
- toxicology
- biomedical
- environment
homepage_url: https://ice.ntp.niehs.nih.gov/
id: ice
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: ICE (Integrated Chemical Environment)
products:
- category: Product
  description: The ICE data downloads and query interface, providing access to curated
    chemical data, in vitro assay data, and reference toxicity datasets, together
    with dataset descriptions and computational tools/workflows for chemical safety
    evaluation.
  format: http
  id: ice.data
  is_public: true
  name: ICE Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ice
  product_url: https://ice.ntp.niehs.nih.gov/DATASETDESCRIPTION
- category: GraphProduct
  description: RDF knowledge graph repackaging ICE (Integrated Chemical Environment)
    cheminformatics and chemical safety data, built and published from the biobricks-okg
    repository.
  format: ttl
  id: biobricks-ice.graph
  name: BioBricks ICE Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-ice
  - relation_type: prov:wasDerivedFrom
    source: ice
  product_url: https://github.com/biobricks-ai/biobricks-okg
publications:
- authors:
  - Shannon Bell
  - Jaleh Abedini
  - Patricia Ceger
  - Xiaoqing Chang
  - Bethany Cook
  - Agnes L. Karmaus
  - Isabel Lea
  - Kamel Mansouri
  - Jason Phillips
  - Eric McAfee
  - Ruhi Rai
  - John Rooney
  - Catherine Sprankle
  - Arpit Tandon
  - David Allen
  - Warren Casey
  - Nicole Kleinstreuer
  doi: 10.1016/j.tiv.2020.104916
  id: https://doi.org/10.1016/j.tiv.2020.104916
  journal: Toxicology in Vitro
  preferred: true
  title: An integrated chemical environment with tools for chemical safety testing
  year: '2020'
- authors:
  - Amber B. Daniel
  - Neepa Choksi
  - Jaleh Abedini
  - Shannon Bell
  - Patricia Ceger
  - Bethany Cook
  - Agnes L. Karmaus
  - John Rooney
  - Kimberly T. To
  - David Allen
  - Nicole Kleinstreuer
  doi: 10.3389/ftox.2022.987848
  id: https://doi.org/10.3389/ftox.2022.987848
  journal: Frontiers in Toxicology
  title: Data curation to support toxicity assessments using the Integrated Chemical
    Environment
  year: '2022'
---
# ICE (Integrated Chemical Environment)

## Overview

The Integrated Chemical Environment (ICE) is a resource from the NTP Interagency Center for the Evaluation of Alternative Toxicological Methods (NICEATM), part of the National Toxicology Program (NTP) at the U.S. National Institute of Environmental Health Sciences (NIEHS). ICE brings together curated chemical data, in vitro assay data, and computational tools and workflows to support chemical safety assessment and toxicological evaluation.

## Data Content

- Curated chemical characterization and physicochemical property data.
- In vitro and high-throughput screening assay data.
- Reference in vivo toxicity datasets for method evaluation.
- Computational tools and workflows supporting new approach methodologies (NAMs).

## Access

- Homepage and query interface: https://ice.ntp.niehs.nih.gov/
- Dataset descriptions and downloads: https://ice.ntp.niehs.nih.gov/DATASETDESCRIPTION

## License

As a work produced by a U.S. federal government program (NICEATM / NTP / NIEHS), ICE data is generally in the public domain (U.S. Government Work).
</content>
</invoke>