---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/USEPA/CompTox-ExpoCast-httk/issues
  label: US EPA Center for Computational Toxicology and Exposure (CCTE)
creation_date: '2026-10-19T00:00:00Z'
description: High-Throughput Toxicokinetics (httk) is a US EPA R package that provides
  free, open-source data and models for toxicokinetics (TK). It pairs chemical-specific
  in vitro measurements and in silico predictions, available for thousands
  of chemicals, multiple exposure routes, and several species, with generic physiologically
  based (PBTK) and empirical TK models. The package supports traditional dosimetry
  and in vitro to in vivo extrapolation (IVIVE), including reverse dosimetry that
  converts high-throughput screening concentrations (e.g., from ToxCast and Tox21)
  into equivalent real-world exposures.
domains:
- toxicology
- pharmacology
- chemistry and biochemistry
- environmental exposure
- environment
- software
- information technology
homepage_url: https://CRAN.R-project.org/package=httk
id: httk
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT
name: httk (High-Throughput Toxicokinetics)
products:
- category: ProcessProduct
  description: The httk R package on CRAN, bundling chemical-specific in vitro TK
    data with generic PBTK and empirical TK models, a Monte Carlo sampler for population
    variability and parameter uncertainty, and IVIVE/reverse dosimetry functions.
  format: r
  id: httk.package
  is_public: true
  latest_version: 2.7.4
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: httk R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: httk
  product_url: https://CRAN.R-project.org/package=httk
- category: Product
  description: GitHub repository for the httk R package, used for bug reports and
    contributed enhancements.
  format: http
  id: httk.repository
  name: httk GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: httk
  product_url: https://github.com/USEPA/CompTox-ExpoCast-httk
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
- category: Product
  description: EPA's downloadable computational toxicology data page, collecting bulk
    downloads of the datasets surfaced in the Dashboard (e.g., DSSTox identifiers,
    invitrodb, ToxRefDB, ToxValDB, CPDat, HTTK).
  format: mixed
  id: comptox-dashboard.downloads
  name: Downloadable Computational Toxicology Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: dsstoxdb
  - relation_type: prov:wasDerivedFrom
    source: toxcast
  - relation_type: prov:wasDerivedFrom
    source: toxrefdb
  - relation_type: prov:wasDerivedFrom
    source: toxvaldb
  - relation_type: prov:wasDerivedFrom
    source: httk
  product_url: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data
publications:
- authors:
  - Robert G. Pearce
  - R. Woodrow Setzer
  - Cory L. Strope
  - John F. Wambaugh
  - Nisha S. Sipes
  doi: 10.18637/jss.v079.i04
  id: https://doi.org/10.18637/jss.v079.i04
  journal: Journal of Statistical Software
  preferred: true
  title: 'httk: R Package for High-Throughput Toxicokinetics'
  year: '2017'
repository: https://github.com/USEPA/CompTox-ExpoCast-httk
rrid: SCR_024702
---
# httk (High-Throughput Toxicokinetics)

## Overview

httk is a US EPA R package for high-throughput toxicokinetics (HTTK), the combination of chemical-specific in vitro data with generic toxicokinetic models. It links an external dose of a chemical to the resulting internal blood or tissue concentration. This lets users convert bioactive concentrations from in vitro high-throughput screens into estimated real-world exposures through in vitro to in vivo extrapolation (IVIVE). The CompTox Chemicals Dashboard's ADME/IVIVE data are generated with httk.

## Data Content

- Chemical-specific in vitro toxicokinetic data (e.g., measurements of distribution and metabolic clearance) and in silico predictions for thousands of chemicals, multiple exposure routes, and several species.
- Generic physiologically based (PBTK) and empirical (e.g., one-compartment) TK models, implemented as compiled ODE systems.
- A Monte Carlo sampler for human biological variability and parameter uncertainty.
- Calibrated methods for predicting tissue:plasma partition coefficients and volume of distribution.

## Access

- CRAN: https://CRAN.R-project.org/package=httk (version 2.7.4 at the time of curation)
- GitHub: https://github.com/USEPA/CompTox-ExpoCast-httk

## License

httk is distributed on CRAN under the MIT license (MIT + file LICENSE).