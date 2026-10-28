---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://tox21.gov/
  label: NIH National Center for Advancing Translational Sciences (NCATS) / Tox21
    Consortium
creation_date: '2026-07-01T00:00:00Z'
description: Tox21 (Toxicology in the 21st Century) is a US federal collaboration
  among the National Institutes of Health (NIH) National Center for Advancing Translational
  Sciences (NCATS), the US Environmental Protection Agency (EPA), the National Toxicology
  Program at the National Institute of Environmental Health Sciences (NTP/NIEHS),
  and the US Food and Drug Administration (FDA). The consortium uses quantitative
  high-throughput screening to test a library of approximately 10,000 chemicals, including
  environmental compounds and approved drugs, against a panel of biological assays
  that probe nuclear-receptor signaling and cellular stress-response pathways. The
  resulting data are used to predict potential toxicity and to prioritize chemicals
  for further, more targeted testing.
domains:
- toxicology
- chemistry and biochemistry
- biomedical
- environment
- drug discovery
- high-throughput screening
homepage_url: https://tox21.gov/
id: tox21
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: Tox21 (Toxicology in the 21st Century)
products:
- category: Product
  description: Tox21 data and resources, including quantitative high-throughput screening
    results for approximately 10,000 chemicals across nuclear-receptor and stress-response
    pathway assays, along with associated tools and documentation published by the
    Tox21 consortium.
  format: mixed
  id: tox21.data
  name: Tox21 Data and Resources
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tox21
  product_url: https://tox21.gov/resources/
- category: GraphProduct
  description: RDF knowledge graph repackaging EPA/NIH Tox21 high-throughput toxicology
    screening data, distributed via the biobricks-okg repository.
  format: ttl
  id: biobricks-tox21.graph
  name: BioBricks Tox21 Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-tox21
  - relation_type: prov:wasDerivedFrom
    source: tox21
  product_url: https://github.com/biobricks-ai/biobricks-okg
- category: GraphicalInterface
  description: Web interface to the CompTox Chemicals Dashboard, supporting search
    by chemical identifiers (e.g., DTXSID, CASRN), product use categories, and assays/genes,
    plus advanced (mass/formula) and batch searches, with per-chemical pages covering
    chemistry, hazard, bioactivity, ADME/IVIVE, and exposure data.
  format: http
  id: comptox-dashboard.portal
  is_public: true
  name: CompTox Chemicals Dashboard Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: dsstoxdb
  - relation_type: prov:wasDerivedFrom
    source: toxcast
  - relation_type: prov:wasDerivedFrom
    source: tox21
  - relation_type: prov:wasDerivedFrom
    source: toxvaldb
  - relation_type: prov:wasDerivedFrom
    source: toxrefdb
  - relation_type: prov:wasDerivedFrom
    source: httk
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  product_url: https://comptox.epa.gov/dashboard
- category: GraphicalInterface
  description: DTT Data Collections Guided Search, providing filterable, downloadable
    tables for curated NIEHS Division of Translational Toxicology (DTT) data collections
    (e.g., clinical chemistry, hematology, and other individual animal data; treatment-related
    findings; DTT publications; and a Tox21 p53 activator dataset)
  format: http
  id: cebs.dtt-data-collections
  name: DTT Data Collections Guided Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs-ext.niehs.nih.gov/datasets
- category: GraphicalInterface
  description: NICE Search, the interactive query interface for exploring curated
    chemical, in vitro and high-throughput screening, physicochemical, and reference
    in vivo toxicity data by chemical, assay, endpoint, and mechanistic target, with
    filtering and export.
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
  description: The NICE data downloads and dataset descriptions, providing access
    to curated chemical data, curated in vitro and high-throughput screening (cHTS)
    assay data, physicochemical and ADME property data, and reference in vivo toxicity
    datasets.
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
publications:
- authors:
  - Tice RR
  - Austin CP
  - Kavlock RJ
  - Bucher JR
  doi: 10.1289/ehp.1205784
  id: https://www.ncbi.nlm.nih.gov/pubmed/23603828
  journal: Environ Health Perspect
  preferred: true
  title: 'Improving the Human Hazard Characterization of Chemicals: A Tox21 Update'
  year: '2013'
---
# Tox21 (Toxicology in the 21st Century)

## Description

Tox21 (Toxicology in the 21st Century) is a collaboration among US federal agencies -- NIH/NCATS, the EPA, NTP/NIEHS, and the FDA -- that applies quantitative high-throughput screening to characterize the potential toxicity of chemicals. The program screens a library of roughly 10,000 chemicals against assays measuring activity in nuclear-receptor signaling and cellular stress-response pathways, generating data used to predict human health effects and prioritize compounds for further testing.

## Products

- **Tox21 Data and Resources** — high-throughput screening data, tools, and documentation published by the Tox21 consortium.