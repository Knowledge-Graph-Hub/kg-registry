---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: rxnorminfo@nlm.nih.gov
  - contact_type: url
    value: https://www.nlm.nih.gov/research/umls/rxnorm/
  label: National Library of Medicine
creation_date: '2025-11-08T00:00:00Z'
description: RxNorm is the National Library of Medicine's standardized nomenclature
  for clinical drugs, providing normalized names and unique concept identifiers (RxCUIs)
  for medications. Developed to support interoperability between healthcare systems,
  RxNorm links its standardized drug names to the vocabularies commonly used in pharmacy
  management and drug interaction software, including First Databank, Micromedex,
  Multum, and Gold Standard Drug Database. By providing links between these diverse
  vocabularies, RxNorm enables seamless communication between systems that do not
  use the same software or terminology. RxNorm organizes drug information into a hierarchy
  of term types representing different levels of specificity, from ingredients through
  clinical drug components to specific branded and generic products. The nomenclature
  covers prescription drugs, over-the-counter medications, and now includes the United
  States Pharmacopeia Compendial Nomenclature containing all Active Pharmaceutical
  Ingredients. RxNorm is updated monthly with new drug products, revisions to existing
  entries, and retirement of obsolete terms to maintain currency with the evolving
  pharmaceutical landscape. The system supports multiple use cases including electronic
  health records, e-prescribing, pharmacy management systems, drug interaction checking,
  clinical decision support, and public health surveillance.
domains:
- health
homepage_url: https://www.nlm.nih.gov/research/umls/rxnorm/
id: rxnorm
infores_id: rxnorm
last_modified_date: '2025-11-08T00:00:00Z'
layout: resource_detail
name: RxNorm
products:
- category: Product
  description: Monthly releases of RxNorm data files in multiple formats including
    RRF files for the full vocabulary and relationships
  format: http
  id: rxnorm.data_files
  name: RxNorm Data Files
  product_url: https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html
- category: ProgrammingInterface
  description: RESTful web services providing programmatic access to RxNorm drug terminology
    data including drug names, identifiers, relationships, and properties
  format: http
  id: rxnorm.api
  name: RxNorm API
  product_url: https://rxnav.nlm.nih.gov/RxNormAPIs.html
- category: GraphicalInterface
  description: Interactive web browser for searching and exploring RxNorm drug concepts,
    relationships, and properties with multiple viewing options
  format: http
  id: rxnorm.rxnav
  name: RxNav Browser
  product_url: https://mor.nlm.nih.gov/RxNav/
- category: GraphicalInterface
  description: Tool for exploring drug class hierarchies and finding RxNorm drug members
    associated with each class from multiple classification systems
  format: http
  id: rxnorm.rxclass
  name: RxClass
  product_url: https://mor.nlm.nih.gov/RxClass/
- category: ProgrammingInterface
  description: Interactive tool allowing users to combine multiple API functions to
    build custom drug information applications
  format: http
  id: rxnorm.rxmix
  name: RxMix
  product_url: https://mor.nlm.nih.gov/RxMix/
- category: Product
  description: Locally installable package containing RxNav, RxClass, RxMix tools
    and RESTful APIs for offline use
  format: http
  id: rxnorm.rxnav_in_a_box
  name: RxNav-in-a-Box
  product_url: https://lhncbc.nlm.nih.gov/RxNav/applications/RxNav-in-a-Box.html
- category: Product
  description: VANDF data integrated into RxNorm
  id: ndfrt.rxnorm
  name: VANDF in RxNorm
  original_source:
  - ndfrt
  product_url: https://www.nlm.nih.gov/research/umls/rxnorm/
  secondary_source:
  - rxnorm
taxon:
- NCBITaxon:9606
---
# RxNorm

## Overview

RxNorm is the National Library of Medicine's standardized nomenclature for clinical drugs, serving as a foundational terminology for drug information exchange in healthcare IT systems. As a free, publicly available resource, RxNorm provides normalized names and unique identifiers for clinical drugs and links these names to the vocabularies used by pharmacy management and drug interaction software systems.

## Information Resource ID

This resource has the Information Resource identifier: `infores:rxnorm`

## Purpose and Scope

RxNorm was developed to solve a critical interoperability problem in healthcare: different information systems use different drug naming conventions, making it difficult to communicate medication information across systems. By serving as a common language and providing links between proprietary drug vocabularies, RxNorm enables:

- Electronic health record systems to exchange medication information
- E-prescribing systems to communicate prescriptions accurately
- Pharmacy systems to process and dispense medications correctly
- Clinical decision support systems to check for drug interactions
- Public health systems to monitor medication usage and safety

## Drug Terminology Structure

RxNorm organizes drug information hierarchically through term types:

- **Ingredients**: Active pharmaceutical ingredients (e.g., acetaminophen)
- **Precise Ingredients**: Ingredients with specific form (e.g., acetaminophen oral)
- **Clinical Drug Components**: Ingredient + strength (e.g., acetaminophen 325 mg)
- **Clinical Drugs**: Generic formulations (e.g., acetaminophen 325 mg oral tablet)
- **Branded Drugs**: Brand name products (e.g., Tylenol 325 mg oral tablet)

Each concept receives a unique RxNorm Concept Unique Identifier (RxCUI) enabling consistent referencing across systems.

## Content and Coverage

- **Prescription medications**: Full coverage of FDA-approved prescription drugs
- **Over-the-counter products**: Common OTC medications
- **USP Compendial Nomenclature**: All Active Pharmaceutical Ingredients from the United States Pharmacopeia
- **Links to proprietary vocabularies**: Connections to First Databank, Micromedex, Multum, Gold Standard Drug Database, and others
- **Monthly updates**: New products, revisions, and retirements to maintain currency

## RxNav Suite of Tools

The RxNav ecosystem extends RxNorm with user-friendly tools and services:

### RxNav Browser
Interactive web application for searching and exploring RxNorm drug concepts, viewing relationships, properties, and status information with multiple visualization options.

### RxClass
Exploration of drug class hierarchies from multiple classification systems including ATC, MeSH, FMTSME, EPC, and disease-specific classes, showing RxNorm drug members for each class.

### RxMix
Interactive platform allowing users to combine multiple API functions to create custom drug information applications and workflows.

### RxNav-in-a-Box
Locally installable version of RxNav, RxClass, RxMix, and companion APIs for institutions requiring offline access or local deployment.

## Data Access

RxNorm data is freely available through:

- **Monthly data file releases**: Complete RxNorm vocabulary in RRF and other formats
- **RESTful APIs**: Comprehensive web services for programmatic access
- **Interactive browsers**: Web-based tools for human exploration
- **UMLS integration**: Available as part of the Unified Medical Language System

## Technical Integration

RxNorm is required by the U.S. Office of the National Coordinator for Health Information Technology (ONC) for use in certified EHR systems. The terminology supports:

- HL7 messaging standards
- FHIR resources for medications
- CDA documents
- NCPDP SCRIPT e-prescribing standards

## Maintenance and Updates

RxNorm is updated monthly following a regular release schedule, incorporating:

- New FDA-approved drug products
- Revisions to existing drug concepts
- Retirement of discontinued products
- Updates to linked vocabularies
- Improvements to relationships and hierarchies

## Support and Documentation

Comprehensive documentation, training materials, video tutorials, and technical support are available through the NLM. Users can access FAQs, technical documentation, learning resources, and direct support from the RxNorm team.

# RxNorm

## Overview

normalized names for clinical drugs and links its names to many of the drug vocabularies commonly used in pharmacy management and drug interaction software, including those of First Databank, Micromedex, and Gold Standard Drug Database

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:rxnorm`

## Curation Status

- **Stub**: Yes - needs manual curation
- **Creation Date**: 2025-10-30
- **Original Source**: Translator Information Resource Registry

## What Needs to be Curated

1. **Activity Status**: Verify if this resource is active, inactive, or deprecated
2. **Category**: Confirm the resource category is correct
3. **Description**: Expand and improve the description
4. **Homepage URL**: Verify and update if needed
5. **Products**: Add specific data products/files/APIs offered by this resource
6. **Contacts**: Add contact information
7. **Publications**: Add relevant publications
8. **Domains**: Add relevant domain tags
9. **Repository**: Add code repository if applicable

## Additional Notes