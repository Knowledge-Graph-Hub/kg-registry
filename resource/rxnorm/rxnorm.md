---
activity_status: active
category: DataSource
collection:
- omop
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: rxnorminfo@nlm.nih.gov
  - contact_type: url
    value: https://www.nlm.nih.gov/research/umls/rxnorm/
  id: ncbi
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
- biomedical
homepage_url: https://www.nlm.nih.gov/research/umls/rxnorm/
id: rxnorm
infores_id: rxnorm
last_modified_date: '2026-04-10T00:00:00Z'
layout: resource_detail
name: RxNorm
products:
- category: Product
  description: Monthly releases of RxNorm data files in multiple formats including
    RRF files for the full vocabulary and relationships
  format: http
  id: rxnorm.data_files
  name: RxNorm Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  product_url: https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html
- category: ProgrammingInterface
  description: RESTful web services providing programmatic access to RxNorm drug terminology
    data including drug names, identifiers, relationships, and properties
  format: http
  id: rxnorm.api
  is_public: true
  name: RxNorm API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  product_url: https://rxnav.nlm.nih.gov/RxNormAPIs.html
- category: GraphicalInterface
  description: Interactive web browser for searching and exploring RxNorm drug concepts,
    relationships, and properties with multiple viewing options
  format: http
  id: rxnorm.rxnav
  is_public: true
  name: RxNav Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  product_url: https://mor.nlm.nih.gov/RxNav/
- category: GraphicalInterface
  description: Tool for exploring drug class hierarchies and finding RxNorm drug members
    associated with each class from multiple classification systems
  format: http
  id: rxnorm.rxclass
  is_public: true
  name: RxClass
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  product_url: https://mor.nlm.nih.gov/RxClass/
- category: ProgrammingInterface
  description: Interactive tool allowing users to combine multiple API functions to
    build custom drug information applications
  format: http
  id: rxnorm.rxmix
  is_public: true
  name: RxMix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  product_url: https://mor.nlm.nih.gov/RxMix/
- category: Product
  description: Locally installable package containing RxNav, RxClass, RxMix tools
    and RESTful APIs for offline use
  format: http
  id: rxnorm.rxnav_in_a_box
  name: RxNav-in-a-Box
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  product_url: https://lhncbc.nlm.nih.gov/RxNav/applications/RxNav-in-a-Box.html
- category: Product
  description: VANDF data integrated into RxNorm
  id: ndfrt.rxnorm
  name: VANDF in RxNorm
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndfrt
  product_url: https://www.nlm.nih.gov/research/umls/rxnorm/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: rxnorm
- category: Product
  description: Downloadable standardized vocabulary bundles for OMOP CDM assembled
    through the authenticated Athena web application
  format: csv
  id: athena.vocabularies
  name: Athena Vocabulary Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: cdiscvocab
  - relation_type: prov:hadPrimarySource
    source: ciel
  - relation_type: prov:hadPrimarySource
    source: gemscript
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: medispan-gpi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: snomedct
  product_url: https://athena.ohdsi.org/vocabulary/list
  warnings:
  - Athena vocabulary downloads are prepared through the logged-in web application;
    stable direct public file URLs are not exposed.
- category: Product
  description: Downloadable SPL files for all drug labels in the DailyMed database,
    updated daily
  format: xml
  id: dailymed.spl_files
  name: DailyMed SPL Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: unii
  - relation_type: prov:wasInformedBy
    source: ndcd
- category: Product
  description: Standardized and deduplicated version of FDA FAERS data with drug names
    mapped to RxNorm and adverse event outcomes mapped to SNOMED-CT, including pre-computed
    summary statistics for drug-outcome relationships.
  id: aeolus.standardized_data
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: AEOLUS Standardized FAERS Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: aeolus
  product_url: https://datadryad.org/dataset/doi:10.5061/dryad.8q0s4
- category: Product
  compression: zip
  description: Current MED-RT DTS release archive from the NCI EVS MED-RT distribution.
  id: med-rt.core_dts
  name: Core MED-RT DTS Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: med-rt
  product_file_size: 2479793
  product_url: https://evs.nci.nih.gov/ftp1/MED-RT/Core_MEDRT_DTS.zip
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: mesh
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: snomedct
  - relation_type: prov:wasInformedBy
    source: umls
- category: Product
  compression: zip
  description: Current MED-RT XML release archive from the NCI EVS MED-RT distribution.
  format: xml
  id: med-rt.core_xml
  name: Core MED-RT XML Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: med-rt
  product_file_size: 2558768
  product_url: https://evs.nci.nih.gov/ftp1/MED-RT/Core_MEDRT_XML.zip
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: mesh
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: snomedct
  - relation_type: prov:wasInformedBy
    source: umls
- category: Product
  compression: zip
  description: Structured Product Labeling subset archive from the current MED-RT
    distribution.
  id: med-rt.core_spl
  name: Core MED-RT SPL Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: med-rt
  product_file_size: 40677
  product_url: https://evs.nci.nih.gov/ftp1/MED-RT/Core_MEDRT_SPL.zip
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: umls
- category: Product
  description: Flexible drug list CSV from the medic v1.0.1 release
  format: csv
  id: medi.drug_list_flexible
  latest_version: v1.0.1
  name: MeDI Flexible Drug List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 4428523
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/drug_list_flexible.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
- category: Product
  description: Stringent drug list CSV from the medic v1.0.1 release
  format: csv
  id: medi.drug_list_stringent
  latest_version: v1.0.1
  name: MeDI Stringent Drug List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 3672087
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/drug_list_stringent.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
- category: Product
  description: LabeledIn indication corpus described in the source publication, containing
    human-reviewed drug-disease treatment relationships with links back to source
    drug labels.
  format: http
  id: labeledin.indications
  name: LabeledIn Drug Indication Corpus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: labeledin
  product_url: https://doi.org/10.1016/j.jbi.2014.08.004
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:used
    source: rxnorm
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
publications:
- authors:
  - Nelson SJ
  - Zeng K
  - Kilbourne J
  - Powell T
  - Moore R
  category: Publication
  doi: 10.1136/amiajnl-2011-000116
  id: PMID:21515544
  journal: J Am Med Inform Assoc
  preferred: true
  title: 'Normalized names for clinical drugs: RxNorm at 6 years.'
  year: '2011'
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