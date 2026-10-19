---
activity_status: active
category: Aggregator
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.echemportal.org/echemportal/
  label: Organisation for Economic Co-operation and Development (OECD)
creation_date: '2026-10-19T00:00:00Z'
description: eChemPortal (The Global Portal to Information on Chemical Substances)
  is a free public portal run by the Organisation for Economic Co-operation and Development
  (OECD), developed in collaboration with the European Chemicals Agency (ECHA), that
  provides simultaneous search across chemical hazard and risk information prepared
  for government chemical programmes at national, regional, and international levels.
  It covers existing and new industrial chemicals, pesticides, and biocides, and supports
  search by substance name or number, by chemical property and endpoint data (structured
  according to the OECD Harmonised Templates), and by GHS or national hazard classification,
  linking to about 34 participating data sources.
domains:
- toxicology
- chemistry and biochemistry
- environment
- public health
homepage_url: https://www.echemportal.org/
id: echemportal
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://www.echemportal.org/echemportal/page/12
  label: eChemPortal Disclaimer (data remain subject to the terms of each participating
    source)
name: eChemPortal (The Global Portal to Information on Chemical Substances)
products:
- category: GraphicalInterface
  description: Web portal for searching participating chemical information sources
    by substance identifiers, by chemical property and endpoint values, and by GHS
    classification, with direct links to the corresponding records in each source.
  format: http
  id: echemportal.portal
  name: eChemPortal Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: echemportal
  - relation_type: prov:wasDerivedFrom
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  product_url: https://www.echemportal.org/echemportal/
- category: DocumentationProduct
  description: List of eChemPortal participating data sources, indicating which
    provide chemical property data and which provide classification data, with
    links to each source.
  format: http
  id: echemportal.sources
  name: eChemPortal Participating Sources
  original_source:
  - relation_type: prov:hadPrimarySource
    source: echemportal
  product_url: https://www.echemportal.org/echemportal/page/2
publications:
- authors:
  - Sally de Marcellus
  doi: 10.1016/B978-0-12-824315-2.01159-3
  id: https://doi.org/10.1016/B978-0-12-824315-2.01159-3
  journal: Encyclopedia of Toxicology
  preferred: true
  title: eChemPortal - The Global Portal to Information on Chemical Substances
  year: '2024'
synonyms:
- eChemPortal
- Global Portal to Information on Chemical Substances
---
# eChemPortal (The Global Portal to Information on Chemical Substances)

## Overview

eChemPortal provides free public access to information on chemical properties and direct links to collections of information prepared for government chemical programmes at national, regional, and international levels. It is an effort of the OECD with contributions from governments and other stakeholders, developed in collaboration with the European Chemicals Agency (ECHA), and was launched in 2007. Because it brings together regulatory hazard data on structurally related substances, it is widely used to gather source data for grouping and read-across.

## Data Content

- About 34 participating data sources, including ECHA REACH registration data and the ECHA C&L inventory, OECD Existing Chemicals (HPV / SIDS IUCLID), Canada's Categorization Results (CCR), Japan's J-CHECK and GHS classification results, US EPA IRIS, ECOTOX, and the CompTox Chemicals Dashboard, EFSA OpenFoodTox, HSDB at PubChem, ICSC, INCHEM, and IPCHEM.
- Substance search by name or identifier (for example CAS number) across all sources.
- Property search over physical-chemical, environmental fate, ecotoxicity, and toxicity endpoint data from sources that provide structured data (OECD Harmonised Templates).
- Classification search over GHS and national/regional hazard classification results.
- Exposure and use information on chemicals, and schedules of assessments from government programmes.

## Access

- Portal: https://www.echemportal.org/echemportal/
- Participating sources: https://www.echemportal.org/echemportal/page/2

## License

Access is free of charge. The data in eChemPortal are maintained by, and remain the responsibility of, the participating data sources, and have not been evaluated by the OECD. Reproduction or further distribution of information obtained via eChemPortal is subject to copyright and may require permission from the owner of that information; individual sources may carry their own disclaimers and terms. See the eChemPortal Disclaimer: https://www.echemportal.org/echemportal/page/12
