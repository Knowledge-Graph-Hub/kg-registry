---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ntp.niehs.nih.gov/whatwestudy/niceatm
  label: NICEATM (NTP Interagency Center for the Evaluation of Alternative Toxicological
    Methods)
creation_date: '2026-07-01T00:00:00Z'
description: NICE, the NIH Integrated Chemical Environment (formerly the Integrated
  Chemical Environment, ICE), is a public web resource developed by the NTP Interagency
  Center for the Evaluation of Alternative Toxicological Methods (NICEATM), part of
  the National Toxicology Program (NTP) at the National Institute of Environmental
  Health Sciences (NIEHS). It brings together curated chemical characterization and
  physicochemical data, curated in vitro and high-throughput screening (cHTS) assay
  data, and reference in vivo toxicity datasets, together with computational tools
  and workflows (including in vitro to in vivo extrapolation, a dose-response Curve
  Surfer, and physiologically based pharmacokinetic modeling). NICE integrates data
  from established sources, including ToxCast and Tox21 high-throughput screening data,
  chemical identity and property data from the EPA CompTox Chemicals Dashboard and
  DSSTox, and OPERA-predicted physicochemical and ADME properties. It is designed to
  help scientists develop, evaluate, and apply new approach methodologies (NAMs) for
  chemical hazard characterization and next generation risk assessment.
domains:
- chemistry and biochemistry
- toxicology
- cheminformatics
- biomedical
- environment
- environmental exposure
homepage_url: https://ice.ntp.niehs.nih.gov/
id: nice
last_modified_date: '2026-10-28T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: NICE (NIH Integrated Chemical Environment)
products:
- category: GraphicalInterface
  description: NICE Search, the interactive query interface for exploring curated chemical,
    in vitro and high-throughput screening, physicochemical, and reference in vivo
    toxicity data by chemical, assay, endpoint, and mechanistic target, with filtering
    and export.
  format: http
  id: nice.search
  is_public: true
  name: NICE Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nice
  - relation_type: prov:hadPrimarySource
    source: toxcast
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: opera
  product_url: https://ice.ntp.niehs.nih.gov/search
- category: Product
  description: The NICE data downloads and dataset descriptions, providing access to
    curated chemical data, curated in vitro and high-throughput screening (cHTS) assay
    data, physicochemical and ADME property data, and reference in vivo toxicity datasets.
  format: http
  id: nice.data
  is_public: true
  name: NICE Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nice
  - relation_type: prov:hadPrimarySource
    source: toxcast
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: opera
  product_url: https://ice.ntp.niehs.nih.gov/DATASETDESCRIPTION
- category: GraphicalInterface
  description: NICE computational tools and workflows, including in vitro to in vivo
    extrapolation (IVIVE), a dose-response Curve Surfer, and physiologically based
    pharmacokinetic (PBPK) modeling, for applying NICE data to chemical safety evaluation.
  format: http
  id: nice.tools
  name: NICE Tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nice
  product_url: https://ice.ntp.niehs.nih.gov/Tools
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
    source: nice
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
synonyms:
- ICE
- Integrated Chemical Environment
- NIH Integrated Chemical Environment
---
# NICE (NIH Integrated Chemical Environment)

## Overview

NICE, the NIH Integrated Chemical Environment (formerly the Integrated Chemical Environment, ICE), is a public web resource from the NTP Interagency Center for the Evaluation of Alternative Toxicological Methods (NICEATM), part of the National Toxicology Program (NTP) at the U.S. National Institute of Environmental Health Sciences (NIEHS). It brings together curated chemical data, in vitro assay data, and computational tools and workflows to support chemical safety assessment and the development of new approach methodologies (NAMs).

## Data Content

- Curated chemical characterization and physicochemical property data, including OPERA-predicted physicochemical and ADME properties.
- Curated in vitro and high-throughput screening (cHTS) assay data, drawn from ToxCast and Tox21.
- Reference in vivo toxicity datasets (for example acute oral toxicity, skin sensitization, eye irritation, and endocrine activity) for method evaluation.
- Chemical identity and lists anchored to EPA CompTox Chemicals Dashboard / DSSTox (DTXSID) identifiers.

## Tools

- In vitro to in vivo extrapolation (IVIVE).
- Dose-response Curve Surfer.
- Physiologically based pharmacokinetic (PBPK) modeling.

## Access

- NICE Search query interface: https://ice.ntp.niehs.nih.gov/
- Dataset descriptions and downloads: https://ice.ntp.niehs.nih.gov/DATASETDESCRIPTION
- Tools: https://ice.ntp.niehs.nih.gov/Tools

The resource is reached at ice.ntp.niehs.nih.gov; NIH now refers to it as NICE.

## License

As a work produced by a U.S. federal government program (NICEATM / NTP / NIEHS), NICE data is generally in the public domain (U.S. Government Work).
