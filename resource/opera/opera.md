---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ntp.niehs.nih.gov/whatwestudy/niceatm/comptox/ct-opera/opera
  - contact_type: github
    value: NIEHS
  label: NICEATM (NTP Interagency Center for the Evaluation of Alternative Toxicological
    Methods)
creation_date: '2026-10-19T00:00:00Z'
description: OPERA (OPEn structure-activity/property Relationship App) is a free and
  open-source, open-data suite of QSAR models that predicts physicochemical properties,
  environmental fate, ADME/toxicokinetic parameters and toxicity endpoints for chemicals,
  together with an applicability domain and accuracy assessment for each prediction.
  Endpoints include logP, logD, pKa, water solubility, melting and boiling point, vapor
  pressure, Henry's law constant, bioconcentration factor, biodegradation, soil adsorption
  (Koc), hepatic intrinsic clearance, plasma fraction unbound, Caco-2 permeability,
  estrogen and androgen receptor activity (CERAPP and CoMPARA consensus models) and
  acute oral systemic toxicity (CATMoS). The models were built following OECD principles
  for QSAR validation and are developed through a collaboration between NIEHS NICEATM
  and the U.S. EPA. OPERA runs as a command-line or graphical application for Windows
  and Linux, and its predictions are also served through the EPA CompTox Chemicals
  Dashboard and the NICEATM Integrated Chemical Environment (ICE).
domains:
- cheminformatics
- chemistry and biochemistry
- toxicology
- pharmacology
- environment
- machine learning
- information technology
homepage_url: https://github.com/NIEHS/OPERA
id: opera
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: OPERA (OPEn structure-activity/property Relationship App)
products:
- category: ProcessProduct
  description: Compiled OPERA application, as command-line (including a parallel
    version) and graphical user interface builds for Windows and Linux, plus a Python
    library build, for batch prediction of physicochemical, environmental fate, ADME
    and toxicity endpoints with applicability domain and accuracy estimates.
  format: mixed
  id: opera.application
  name: OPERA application releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opera
  product_url: https://github.com/NIEHS/OPERA/releases
- category: Product
  description: OPERA source code repository, with the model code, data, and QSAR
    Model Reporting Format (QMRF) reports for the models.
  format: mixed
  id: opera.repository
  name: OPERA source code and data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opera
  product_url: https://github.com/NIEHS/OPERA
publications:
- authors:
  - Kamel Mansouri
  - Chris M. Grulke
  - Richard S. Judson
  - Antony J. Williams
  doi: 10.1186/s13321-018-0263-1
  id: https://doi.org/10.1186/s13321-018-0263-1
  journal: Journal of Cheminformatics
  preferred: true
  title: OPERA models for predicting physicochemical properties and environmental
    fate endpoints
  year: '2018'
- authors:
  - Kamel Mansouri
  - José T. Moreira-Filho
  - Charles N. Lowe
  - Nathaniel Charest
  - Todd Martin
  - Valery Tkachenko
  - Richard Judson
  - Mike Conway
  - Nicole C. Kleinstreuer
  - Antony J. Williams
  doi: 10.1186/s13321-024-00814-3
  id: https://doi.org/10.1186/s13321-024-00814-3
  journal: Journal of Cheminformatics
  title: Free and open-source QSAR-ready workflow for automated standardization of
    chemical structures in support of QSAR modeling
  year: '2024'
---
# OPERA (OPEn structure-activity/property Relationship App)

## Overview

OPERA is a free, open-source and open-data suite of quantitative structure-activity/property
relationship (QSAR) models. It predicts physicochemical properties, environmental fate,
ADME/toxicokinetic parameters and toxicity endpoints for chemical structures, and reports
an applicability domain and accuracy estimate alongside each prediction. The models
follow OECD principles for QSAR validation and are intended as a regulatory-oriented
alternative to experimental measurement. OPERA is developed through a collaboration
between the NTP Interagency Center for the Evaluation of Alternative Toxicological
Methods (NICEATM) at NIEHS and the U.S. Environmental Protection Agency.

## Data Content

- Physicochemical properties: logP, logD, pKa, water solubility, melting point, boiling
  point, vapor pressure, Henry's law constant, octanol-air partition coefficient and HPLC
  retention time.
- Environmental fate: bioconcentration factor, biodegradation half-life, ready
  biodegradability, soil adsorption coefficient (Koc), atmospheric hydroxyl radical rate
  constant and fish biotransformation half-life.
- ADME/toxicokinetics: hepatic intrinsic clearance, plasma fraction unbound and Caco-2
  permeability.
- Toxicity and bioactivity: estrogen receptor (CERAPP) and androgen receptor (CoMPARA)
  activity, and acute oral systemic toxicity (CATMoS).
- Model data and QMRF reports for the models, in the GitHub repository.

## Access

- Source code, data and compiled releases: https://github.com/NIEHS/OPERA
- NICEATM OPERA page: https://ntp.niehs.nih.gov/whatwestudy/niceatm/comptox/ct-opera/opera
- OPERA predictions are also available through the EPA CompTox Chemicals Dashboard, the
  NICEATM Integrated Chemical Environment (ICE), precisionFDA and an OECD QSAR Toolbox
  extension.

## License

OPERA is released under the MIT License.
