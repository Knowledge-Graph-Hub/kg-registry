---
activity_status: active
category: Aggregator
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://qsartoolbox.org/
  label: OECD QSAR Toolbox (OECD, European Chemicals Agency, and Laboratory of Mathematical
    Chemistry)
creation_date: '2026-10-19T00:00:00Z'
description: The OECD QSAR Toolbox is a free software application, owned by the
  Organisation for Economic Co-operation and Development (OECD) and the European Chemicals
  Agency (ECHA) and developed by the Laboratory of Mathematical Chemistry (LMC, Bourgas,
  Bulgaria), that supports transparent and reproducible chemical hazard assessment.
  It bundles about 63 databases with experimental data for more than 140,000 chemical
  structures, together with profilers, metabolism simulators, and QSAR models, to
  find structurally and mechanistically defined analogues, build and assess chemical
  categories, and fill data gaps by read-across and trend analysis as an alternative
  to animal testing.
domains:
- toxicology
- chemistry and biochemistry
- cheminformatics
- environment
homepage_url: https://qsartoolbox.org/
id: oecd-qsar-toolbox
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://qsartoolbox.org/license-agreement/
  label: OECD QSAR Toolbox End User Licence Agreement (free of charge)
name: OECD QSAR Toolbox
products:
- category: ProcessProduct
  description: Windows installation package for the QSAR Toolbox client and server
    (current release v4.9), including the bundled experimental databases, profilers,
    metabolism simulators, and QSAR models; previous versions are also available
    for reproducing earlier results.
  format: http
  id: oecd-qsar-toolbox.software
  name: QSAR Toolbox Installer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oecd-qsar-toolbox
  product_url: https://qsartoolbox.org/download/
- category: ProgrammingInterface
  description: Self-hosted Toolbox WebAPI exposing services for chemical search,
    structure information, profiling, parameter calculation, metabolite generation,
    and data retrieval, run locally via the Toolbox WebSuite or the Toolbox Server.
  format: http
  id: oecd-qsar-toolbox.webapi
  is_public: true
  name: QSAR Toolbox WebAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oecd-qsar-toolbox
  product_url: https://qsartoolbox.org/developers/webapi/
- category: DocumentationProduct
  description: Description of the experimental databases bundled with the QSAR Toolbox,
    grouped into physical-chemical properties, environmental fate and transport,
    ecotoxicological information, human health hazards, and intermediate (mechanistic)
    effects.
  format: http
  id: oecd-qsar-toolbox.databases
  name: QSAR Toolbox Databases Overview
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oecd-qsar-toolbox
  product_url: https://qsartoolbox.org/resources/databases/
publications:
- authors:
  - S. D. Dimitrov
  - R. Diderich
  - T. Sobanski
  - T. S. Pavlov
  - G. V. Chankov
  - A. S. Chapkanov
  - Y. H. Karakolev
  - S. G. Temelkov
  - R. A. Vasilev
  - K. D. Gerova
  - C. D. Kuseva
  - N. D. Todorova
  - A. M. Mehmed
  - M. Rasenberg
  - O. G. Mekenyan
  doi: 10.1080/1062936X.2015.1136680
  id: https://doi.org/10.1080/1062936X.2015.1136680
  journal: SAR and QSAR in Environmental Research
  preferred: true
  title: QSAR Toolbox - workflow and major functionalities
  year: '2016'
- authors:
  - Terry W. Schultz
  - Robert Diderich
  - Chanita D. Kuseva
  - Ovanes G. Mekenyan
  doi: 10.1007/978-1-4939-7899-1_2
  id: https://doi.org/10.1007/978-1-4939-7899-1_2
  journal: Methods in Molecular Biology
  title: The OECD QSAR Toolbox Starts Its Second Decade
  year: '2018'
synonyms:
- QSAR Toolbox
- (Q)SAR Application Toolbox
---
# OECD QSAR Toolbox

## Overview

The OECD QSAR Toolbox is a free software application that supports reproducible and transparent chemical hazard assessment. It is owned by the OECD and the European Chemicals Agency (ECHA) and developed by the Laboratory of Mathematical Chemistry (LMC) in Bourgas, Bulgaria. The Toolbox is designed to promote assessment methods alternative to animal testing, for use by governments, the chemical industry, and other stakeholders. Version 4.5 is the version referenced by OECD Guideline No. 497 (Defined Approaches on Skin Sensitisation).

## Data Content

- About 63 bundled databases with roughly 3.4 million experimental data points for more than 142,000 chemical structures (as of v4.9), covering physical-chemical properties, environmental fate and transport, ecotoxicity, human health hazards, and mechanistic (intermediate effect) information.
- Profilers encoding structural alerts and mechanisms (including covalent binding mechanisms with macromolecules) for grouping chemicals.
- Metabolism and (a)biotic transformation simulators and experimental metabolic maps.
- Embedded external QSAR models, a data matrix wizard, and customisable prediction reports for read-across and trend analysis.
- A docking API for third-party add-ins and the TEDRA plugin for exchanging data with IUCLID 6.

## Access

- Homepage: https://qsartoolbox.org/
- Download (Windows installer and previous versions): https://qsartoolbox.org/download/
- WebAPI: https://qsartoolbox.org/developers/webapi/

## License

The Toolbox is provided free of charge under the OECD (Q)SAR Application Toolbox End User Licence Agreement, which every user must accept during installation: https://qsartoolbox.org/license-agreement/
