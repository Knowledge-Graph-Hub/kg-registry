---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.healthdata.org/
  label: Institute for Health Metrics and Evaluation (IHME)
creation_date: '2026-10-21T00:00:00Z'
description: The Global Burden of Disease (GBD) study, led by the Institute for Health Metrics
  and Evaluation (IHME) at the University of Washington, produces comparable estimates of
  prevalence, incidence, mortality, and disability for hundreds of diseases, injuries, and
  risk factors across countries and over time. The most recent completed cycle, GBD 2021,
  covers 371 diseases and injuries and 88 risk factors across 204 countries and territories
  and 811 subnational locations for 1990–2021, and is the first cycle to incorporate the health
  impact of the COVID-19 pandemic.
domains:
- public health
- epidemiology
homepage_url: https://www.healthdata.org/research-analysis/gbd
id: gbd
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://www.healthdata.org/sites/default/files/files/free-of-charge_non-commercial_user_agreement.pdf
  label: IHME Free-of-Charge Non-Commercial User Agreement
name: Global Burden of Disease (IHME)
products:
- category: GraphicalInterface
  description: Interactive query and download tool for GBD estimates (deaths, DALYs, YLDs,
    YLLs, prevalence, incidence) by location, year, cause, risk, age, and sex.
  format: http
  id: gbd.results-tool
  name: GBD Results Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gbd
  product_url: https://vizhub.healthdata.org/gbd-results/
- category: GraphicalInterface
  description: Interactive visualization (treemaps, arrow diagrams, maps) for exploring and
    comparing causes of death and disability across locations and time.
  format: http
  id: gbd.compare
  name: GBD Compare
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gbd
  product_url: https://vizhub.healthdata.org/gbd-compare/
- category: Product
  description: IHME's data catalog cataloging GBD and other global health datasets with metadata
    and download links.
  format: http
  id: gbd.ghdx
  name: Global Health Data Exchange (GHDx)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gbd
  product_url: https://ghdx.healthdata.org/
publications:
- authors:
  - Alize J Ferrari
  - GBD 2021 Diseases and Injuries Collaborators
  doi: 10.1016/S0140-6736(24)00757-8
  id: doi:10.1016/S0140-6736(24)00757-8
  journal: The Lancet
  preferred: true
  title: 'Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted
    life-years (DALYs), and healthy life expectancy (HALE) for 371 diseases and injuries in
    204 countries and territories and 811 subnational locations, 1990-2021: a systematic analysis
    for the Global Burden of Disease Study 2021'
  year: '2024'
synonyms:
- GBD
- Global Burden of Disease Study
taxon:
- NCBITaxon:9606
---

# Global Burden of Disease (IHME)

## Overview

The Global Burden of Disease (GBD) study from the Institute for Health Metrics and Evaluation (IHME) estimates prevalence, incidence, mortality, and disability for diseases, injuries, and risk factors across countries and over time. The most recent cycle, GBD 2021, spans 204 countries and territories and 811 subnational locations.

## Access

- GBD Results Tool: query and download estimates.
- GBD Compare: interactive visualizations.
- GHDx: the IHME global health data catalog.

Data are released under the IHME Free-of-Charge Non-Commercial User Agreement.

## Citation

Please cite: GBD 2021 Diseases and Injuries Collaborators. Global incidence, prevalence, YLDs, DALYs, and HALE for 371 diseases and injuries in 204 countries and territories and 811 subnational locations, 1990-2021. Lancet. 2024;403(10440):2133–2161. doi:10.1016/S0140-6736(24)00757-8
