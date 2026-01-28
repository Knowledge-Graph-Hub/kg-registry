---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.orpha.net/en/institutions/get-in-touch/
  label: Orphanet
creation_date: '2025-07-10T00:00:00Z'
description: Orphanet is a unique resource for information and data on rare diseases
  and orphan drugs, aimed at improving diagnosis, care, and treatment of patients
  with rare diseases. It maintains the Orphanet rare disease nomenclature (ORPHAcodes),
  which is essential for improving the visibility of rare diseases in health and research
  information systems.
domains:
- biomedical
- clinical
homepage_url: https://www.orpha.net/
id: orphanet
infores_id: orphanet
last_modified_date: '2025-07-10T00:00:00Z'
layout: resource_detail
name: Orphanet
products:
- category: Product
  description: XML dataset containing information on expert centers dedicated to the
    medical management and/or genetic counselling for rare diseases.
  format: xml
  id: orphanet.expertcenters
  name: Expert Centers Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on expert center networks for rare
    diseases.
  format: xml
  id: orphanet.expertcentersnetworks
  name: Expert Centers Networks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on diagnostic tests and clinical
    laboratories for rare diseases.
  format: xml
  id: orphanet.diagnostictests
  name: Diagnostic Tests and Laboratories Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient organizations dedicated
    to rare diseases.
  format: xml
  id: orphanet.patientorganizations
  name: Patient Organizations Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient organization networks
    for rare diseases.
  format: xml
  id: orphanet.patientorganizationsnetworks
  name: Patient Organizations Networks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on national research projects focused
    on rare diseases.
  format: xml
  id: orphanet.researchprojects
  name: National Research Projects Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on multinational research project
    networks for rare diseases.
  format: xml
  id: orphanet.researchprojectsnetworks
  name: Multinational Research Projects Networks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on national clinical trials for
    rare diseases.
  format: xml
  id: orphanet.clinicaltrials
  name: National Clinical Trials Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on multinational clinical trial
    networks for rare diseases.
  format: xml
  id: orphanet.clinicaltrialsnetworks
  name: Multinational Clinical Trials Networks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient registries for rare diseases.
  format: xml
  id: orphanet.patientregistries
  name: Patient Registries Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient registry networks for
    rare diseases.
  format: xml
  id: orphanet.patientregistriesnetworks
  name: Patient Registries Networks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on biobanks dedicated to rare diseases.
  format: xml
  id: orphanet.biobanks
  name: Biobanks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on biobank networks for rare diseases.
  format: xml
  id: orphanet.biobanksnetworks
  name: Biobanks Networks Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on orphan drugs for rare diseases,
    including substances with orphan designation and/or marketing authorization.
  format: xml
  id: orphanet.orphandrugs
  name: Orphan Drugs Dataset
  product_url: https://www.orphadata.com/expert-resources/
- category: ProgrammingInterface
  description: APIs providing access to Orphanet scientific knowledge, ORPHAcodes,
    and expert resources data.
  id: orphanet.orphadataapi
  is_public: true
  name: Orphadata API
  product_url: https://www.orphadata.com/contact/
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - clingen
  - clinvar
  - mgd
  - rgd
  - orphanet
  - psygenet
  - uniprot
  - disgenet
  - hp
  - gwascatalog
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
- category: Product
  description: Disease association data integrated from OMIM, MalaCards, ClinVar,
    Orphanet, DisGeNET and other disease databases
  format: http
  id: genecards.disease.associations
  name: GeneCards Disease Associations
  original_source:
  - omim
  - malacards
  - clinvar
  - orphanet
  - disgenet
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-23_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-15_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-28: HTTP 403 error
    when accessing file'
repository: https://github.com/Orphanet
taxon:
- NCBITaxon:9606
version: July 2025
---
# Orphanet

Orphanet is a unique resource gathering and improving knowledge on rare diseases to enhance diagnosis, care, and treatment of patients with rare diseases. It aims to provide high-quality information on rare diseases and ensure equal access to knowledge for all stakeholders.

## Overview

Established in France by INSERM (French National Institute for Health and Medical Research) in 1997, Orphanet has evolved into a European endeavor, gradually growing to a Consortium of 40 countries worldwide. The Orphanet database contains information on:

- 6,528+ rare diseases
- 4,512+ genes
- 8,722+ expert centers
- 36,595+ diagnostic tests
- 30,456+ professionals

## Key Resources

### Orphanet Rare Disease Ontology (ORDO)

ORDO is a structured vocabulary for rare diseases derived from the Orphanet database. It captures relationships between diseases, genes, and other relevant features, providing integrated, re-usable data for computational analysis. The ontology is maintained by Orphanet and follows OBO guidelines.

### ORPHAcodes - Orphanet Nomenclature

The Orphanet nomenclature is a multilingual, standardized, controlled medical terminology specific to rare diseases. Each clinical entity is associated with a unique numerical identifier (ORPHAcode), preferred term, synonyms, and definition. The nomenclature pack includes files for implementing ORPHAcodes in health information systems.

### Orphanet Scientific Knowledge Base

This comprehensive collection of datasets provides structured information about rare diseases, including:
- Disease alignments with other terminologies (ICD-10, ICD-11, OMIM, UMLS, MONDO, MeSH, MedDRA, GARD)
- Classifications of rare diseases
- Gene associations
- Clinical signs and symptoms
- Functional consequences
- Epidemiological data
- Natural history information

## Recognition

Orphadata Science (which includes ORDO and the scientific knowledge files) has been recognized as:
- An ELIXIR Core Data Resource
- A Global Core Biodata Resource
- An IRDiRC Recognized Resource

## Data Access

All Orphanet data resources are available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license, making them freely accessible for research and implementation. Data are updated bi-annually in July and December.