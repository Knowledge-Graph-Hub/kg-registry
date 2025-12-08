---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: ask2164@cumc.columbia.edu
  label: Andrew S. Kanter, MD MPH
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.dbmi.columbia.edu/
  label: Columbia University Department of Biomedical Informatics
creation_date: '2025-11-05T00:00:00Z'
description: The Columbia International eHealth Laboratory (CIEL) dictionary is a
  shared open concept dictionary that provides comprehensive terminology services
  to OpenMRS and other health information systems. Based at Columbia University's
  Department of Biomedical Informatics, CIEL contains over 55,000 medical concepts
  mapped to standardized code systems including ICD, SNOMED CT, LOINC, RxNorm, and
  many others. CIEL supports open source health initiatives globally and has been
  recognized as both a Digital Public Good by the Digital Public Goods Alliance and
  a Content Public Good by Digital Square.
domains:
- clinical
- health
- biomedical
- information technology
homepage_url: https://openconceptlab.org/project/ciel/
id: ciel
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: CIEL
products:
- category: GraphicalInterface
  description: Web interface for browsing CIEL concept dictionary via Open Concept
    Lab
  format: http
  id: ciel.ocl
  name: CIEL on OCL Online
  original_source:
  - ciel
  product_url: https://app.openconceptlab.org/#/orgs/CIEL/sources/CIEL/
- category: Product
  description: CIEL concept dictionary with over 55,000 medical concepts
  format: mixed
  id: ciel.dictionary
  name: CIEL Concept Dictionary
  original_source:
  - ciel
  product_url: https://app.openconceptlab.org/#/orgs/CIEL/sources/CIEL/
- category: Product
  description: COVID-19 concept starter set for rapid implementation
  format: mixed
  id: ciel.covid19
  name: CIEL COVID-19 Starter Set
  original_source:
  - ciel
  product_url: https://app.openconceptlab.org/#/orgs/CIEL/collections/COVID-19-Starter-Set/
- category: Product
  description: Monkeypox (mpox) concept starter set
  format: mixed
  id: ciel.mpx
  name: CIEL Monkeypox Starter Set
  original_source:
  - ciel
  product_url: https://app.openconceptlab.org/#/orgs/CIEL/collections/MPX/
- category: MappingProduct
  description: Concept mappings between different terminology systems
  format: csv
  id: athena.mappings
  name: Athena Concept Mappings
  original_source:
  - snomedct
  - icd10
  - icd10cm
  - mesh
  - loinc
  - cdiscvocab
  - ciel
  product_url: https://athena.ohdsi.org/search-terms/start
  secondary_source:
  - athena
  warnings:
  - File was not able to be retrieved when checked on 2025-12-07_ Error connecting
    to URL_ Exceeded 30 redirects.
  - File was not able to be retrieved when checked on 2025-12-05_ Error connecting
    to URL_ Exceeded 30 redirects.
  - 'File was not able to be retrieved when checked on 2025-12-08: Error connecting
    to URL: Exceeded 30 redirects.'
synonyms:
- CIEL
- Columbia International eHealth Laboratory
- CIEL Concept Dictionary
taxon:
- NCBITaxon:9606
---
# CIEL - Columbia International eHealth Laboratory

## Overview

The Columbia International eHealth Laboratory (CIEL) is based in the Department of Biomedical Informatics at Columbia University in New York, USA. CIEL provides comprehensive terminology services to OpenMRS and other health information systems through its open concept dictionary.

Originally formed as a collaboration between Columbia's DBMI, the Department of Epidemiology at the Mailman School of Public Health, and the Earth Institute, CIEL was supported by the Rockefeller Foundation and the Canadian International Development Research Centre (IDRC). Under the direction of Andrew S. Kanter, MD MPH, CIEL initially helped develop and implement health information systems for the Millennium Villages Project (MVP) in ten countries in Sub-Saharan Africa.

## Key Features

- **Comprehensive Coverage**: Over 55,000 medical concepts
- **Standardized Mappings**: Concepts mapped to ICD, SNOMED CT, LOINC, RxNorm, and other standard terminologies
- **Monthly Updates**: Regular releases with community-driven content additions
- **Open Source**: Freely available for implementation in health information systems
- **Community Driven**: Content direction guided by community participation and needs
- **Disease-Specific Collections**: Curated starter sets for COVID-19, monkeypox, and other conditions

## Recognition

- **Digital Public Good**: Approved by the Digital Public Goods Alliance
- **Content Public Good**: Recognized by Digital Square
- **Global Impact**: Supports open source health initiatives worldwide through the OpenMRS community

## Products

### CIEL on OCL Online
Interactive web interface for browsing, searching, and accessing CIEL concepts through the Open Concept Lab platform.

### CIEL Concept Dictionary
The complete dictionary source containing over 55,000 concepts with mappings to standard code systems, distributed monthly via Open Concept Lab.

### COVID-19 Starter Set
Curated collection of COVID-19-related concepts for rapid implementation in health information systems responding to the pandemic.

### Monkeypox Starter Set
Specialized concept collection for monkeypox (mpox) surveillance and clinical management.

## Governance and Community

The CIEL concept dictionary is primarily edited by Dr. Andrew S. Kanter, with content creation and direction driven by community participation through:
- Weekly OCL squad calls (Wednesdays)
- Concept Management Office Hours (Thursdays)
- Bi-weekly OCL-CIEL coordination meetings (alternate Fridays)
- OpenMRS Talk forum
- OCL chat platform

## Update Frequency

CIEL is updated on a monthly basis and is primarily distributed via the Open Concept Lab. Release notes are posted on the OpenMRS Talk forum.

## License and Terms of Use

The CIEL dictionary is licensed under the Creative Commons Attribution 4.0 International Public License (CC BY 4.0). The dictionary contains lexical codes that may be subject to claims of ownership by third parties (IMO, IHTSDO, WHO, etc.), and no license is conveyed regarding those third party rights.

CIEL endeavors to exclude any terminology considered prejudicial or discriminatory, while including terminology in common medical use or required by governmental authorities for historical purposes.

## Domains

- Clinical
- Health
- Biomedical
- Information Technology

## Taxon Coverage

Human (NCBITaxon:9606)