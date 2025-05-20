---
layout: resource_detail
activity_status: active
id: drugbank
name: DrugBank
description: DrugBank Online is a comprehensive, publicly accessible database containing detailed information on drugs and drug targets, combining chemical, pharmacological, pharmaceutical data with drug target information including sequence, structure, and pathway details.
domains:
- health
- chemistry and biochemistry
- pharmacology
- genomics
- proteomics
contacts:
- category: Organization
  label: DrugBank
  contact_details:
  - contact_type: email
    value: info@drugbank.com
  - contact_type: url
    value: https://www.drugbank.com/contact
homepage_url: https://www.drugbank.com/
repository: https://go.drugbank.com/releases/latest
license:
  id: https://go.drugbank.com/legal/terms_of_use
  label: Custom (free for academic research with license)
category: DataSource
tags:
- core
- biopragmatics
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching the DrugBank database
  id: drugbank.web
  name: DrugBank Online
  product_url: https://go.drugbank.com/
  original_source:
  - drugbank
  format: http
- category: DataModelProduct
  description: Academic access to DrugBank database dumps in XML and other formats
  id: drugbank.academic
  name: DrugBank Academic Downloads
  product_url: https://go.drugbank.com/releases/latest
  original_source:
  - drugbank
  license:
    id: https://go.drugbank.com/legal/terms_of_use
    label: Academic License
  format: xml
- category: ProgrammingInterface
  description: Clinical API for integrating DrugBank data into healthcare applications
  id: drugbank.clinical.api
  name: DrugBank Clinical API
  product_url: https://www.drugbank.com/clinical
  is_public: true
  connection_url: https://www.drugbank.com/clinical
  original_source:
  - drugbank
publications:
- id: https://doi.org/10.1093/nar/gkad976
  title: DrugBank 6.0 - The DrugBank Knowledgebase for 2024
  journal: Nucleic Acids Research
  year: '2024'
  preferred: true
- id: https://doi.org/10.1093/nar/gkx1037
  title: DrugBank 5.0 - A major update to the DrugBank database for 2018
  journal: Nucleic Acids Research
  year: '2018'
---

DrugBank is a comprehensive knowledge base combining detailed drug information (chemical, pharmacological, and pharmaceutical) with extensive drug target information (sequence, structure, and pathway). 

The database was started in 2006 in Dr. David Wishart's lab at the University of Alberta and is widely used by the pharmaceutical industry, medicinal chemists, pharmacists, physicians, researchers, and students.

## Content
As of version 5.1.13 (January 2025), DrugBank contains:
- 17,467 drug entries
- 2,992 approved small molecule drugs
- 1,729 approved biologics (proteins, peptides, vaccines, allergenics)
- 135 nutraceuticals
- 6,879+ experimental (discovery-phase) drugs
- 5,463 non-redundant protein sequences (drug targets, enzymes, transporters, carriers)
- 200+ data fields per entry

## Applications
DrugBank supports various research and clinical applications:
- Drug discovery and repurposing
- Precision medicine
- Pharmacovigilance
- In silico testing
- Clinical trial matching
- Electronic medical records
- Telehealth applications

## Access
DrugBank offers several access options:
- Free access to DrugBank Online for basic browsing and searching
- Free academic licenses for researchers meeting specific criteria
- Commercial licenses for industry users and developers
- Clinical API for healthcare software integration

All usage of DrugBank data requires proper citation in any resulting publications.
