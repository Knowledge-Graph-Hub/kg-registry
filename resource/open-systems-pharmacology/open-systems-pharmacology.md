---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.open-systems-pharmacology.org/
  - contact_type: github
    value: Open-Systems-Pharmacology
  label: Open Systems Pharmacology community
creation_date: '2026-10-19T00:00:00Z'
description: Open Systems Pharmacology (OSP) is an open-source, community-governed
  platform for physiologically based pharmacokinetic (PBPK) and quantitative systems
  pharmacology (QSP) modeling. Its OSP Suite comprises PK-Sim, for whole-body PBPK
  modeling, and MoBi, for multiscale physiological modeling and model extension, along
  with the ospsuite R package and reporting tools. The project also maintains the OSP
  PBPK Model Library, a set of released PBPK models for individual compounds, including
  small-molecule drugs and antibodies, each with an evaluation report and a PK-Sim
  project file, and qualification documents for the suite. The OSP management team includes
  members from pharmaceutical companies and academic and service organizations.
domains:
- pharmacology
- drug interactions
- biomedical
- software
- information technology
homepage_url: https://www.open-systems-pharmacology.org/
id: open-systems-pharmacology
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/Open-Systems-Pharmacology/Suite/blob/master/LICENSE
  label: GPL-2.0 with clarifying addendum
name: Open Systems Pharmacology (OSP)
products:
- category: Product
  description: OSP PBPK Model Library of released PBPK models for individual compounds,
    including antibiotics, antivirals, anesthetics, sedatives, anticonvulsants, cardiovascular
    agents and antibodies, each with an HTML and PDF model evaluation report and PK-Sim
    project files (some with pediatric versions).
  format: http
  id: open-systems-pharmacology.pbpk-model-library
  name: OSP PBPK Model Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-systems-pharmacology
  product_url: https://www.open-systems-pharmacology.org/OSP-PBPK-Model-Library/
- category: ProcessProduct
  description: OSP Suite installers for PK-Sim (whole-body PBPK modeling) and MoBi
    (multiscale physiological modeling and simulation).
  format: mixed
  id: open-systems-pharmacology.suite
  name: OSP Suite (PK-Sim and MoBi)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-systems-pharmacology
  product_url: https://github.com/Open-Systems-Pharmacology/Suite/releases
- category: ProcessProduct
  description: ospsuite R package for loading, running and analysing OSP Suite simulations
    from R.
  format: r
  id: open-systems-pharmacology.ospsuite-r
  name: ospsuite R package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-systems-pharmacology
  product_url: https://github.com/Open-Systems-Pharmacology/OSPSuite-R
- category: DocumentationProduct
  description: OSP Suite manual covering mechanistic PK/PD modeling concepts, PK-Sim
    and MoBi use, shared tools, qualification and the ospsuite R package.
  format: http
  id: open-systems-pharmacology.docs
  name: OSP Suite documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-systems-pharmacology
  product_url: https://docs.open-systems-pharmacology.org/
publications:
- authors:
  - Jörg Lippert
  - Rolf Burghaus
  - Andrea Edginton
  - Sebastian Frechen
  - Mats Karlsson
  - Andreas Kovar
  - Thorsten Lehr
  - Peter Milligan
  - Valerie Nock
  - Sergej Ramusovic
  - Matthew Riggs
  - Stephan Schaller
  - Jan Schlender
  - Stephan Schmidt
  - Michaël Sevestre
  - Erik Sjögren
  - Juri Solodenko
  - Alexander Staab
  - Donato Teutonico
  doi: 10.1002/psp4.12473
  id: https://doi.org/10.1002/psp4.12473
  journal: 'CPT: Pharmacometrics & Systems Pharmacology'
  preferred: true
  title: Open Systems Pharmacology Community-An Open Access, Open Source, Open Science
    Approach to Modeling and Simulation in Pharmaceutical Sciences
  year: '2019'
---
# Open Systems Pharmacology (OSP)

## Overview

Open Systems Pharmacology is an open-source, open-science community project for
physiologically based pharmacokinetic (PBPK) and quantitative systems pharmacology
(QSP) modeling. Its software, the OSP Suite, is free to download and use. The project
is governed by a management team with members from pharmaceutical companies (including
Bayer, Boehringer Ingelheim, Novartis and Sanofi) and from academic and service
organizations.

## Data Content

- OSP PBPK Model Library: released PBPK models for 41 compounds, grouped by
  therapeutic class, each with an HTML and PDF evaluation report and PK-Sim project
  files (`.pksim5`), some with pediatric models.
- Qualification documents for the OSP Suite.

## Access

- Homepage: https://www.open-systems-pharmacology.org/
- Model library: https://www.open-systems-pharmacology.org/OSP-PBPK-Model-Library/
- Software releases: https://github.com/Open-Systems-Pharmacology/Suite/releases
- Documentation: https://docs.open-systems-pharmacology.org/
- Source code: https://github.com/Open-Systems-Pharmacology

## License

The OSP Suite is distributed under the GNU General Public License version 2 with a
clarifying addendum on liability. The OSP PBPK Model Library repository does not state
a separate license.
