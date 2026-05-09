---
activity_status: active
category: DataSource
collection:
  - omop
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.who.int/
      - contact_type: email
        value: classifications@who.int
    id: who
    label: World Health Organization
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.who.int/standards/classifications
    id: who
    label: WHO Family of International Classifications
creation_date: '2025-11-10T00:00:00Z'
description: The International Classification of Diseases, 10th Revision (ICD-10) is a standardized system for classifying diseases, injuries, and causes of death maintained by the World Health Organization (WHO). Originating in the 19th century with over 150 years of continuous development, ICD-10 came into effect on January 1, 1993, following adoption by the World Health Assembly in May 1990. ICD-10 provides a comprehensive hierarchical classification system with alphanumeric codes that allow systematic recording, analysis, interpretation, and comparison of mortality and morbidity data collected across countries and time periods. The system is used globally for health recording and statistics, including cause of death certification, morbidity coding in primary through tertiary care, resource allocation, reimbursement systems, quality and safety assessment, and epidemiological research. ICD-10 serves as the foundation for diagnostic-related grouping (DRG), cancer registries, and clinical trials that require standardized disease classification. The classification has been translated into dozens of languages and adapted by many countries for national use, with variants like ICD-10-CM (Clinical Modification) used in the United States and ICD-10-CA used in Canada. While ICD-11 officially came into effect in January 2022, ICD-10 remains widely used during the transition period as countries implement the newer revision. ICD-10 continues to be maintained with periodic updates and
  serves as the basis for various mapping projects to other terminology systems including SNOMED CT, MedDRA, and LOINC.
domains:
  - clinical
homepage_url: https://icd.who.int/browse10
id: icd10
infores_id: icd10
last_modified_date: '2026-04-10T00:00:00Z'
layout: resource_detail
name: ICD-10
products:
  - category: GraphicalInterface
    description: Web-based browser for exploring the ICD-10 classification hierarchy and codes
    id: icd10.browser
    name: ICD-10 Browser
    product_url: https://icd.who.int/browse10
    original_source:
      - source: icd10
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Official ICD-10 classification files and documentation available for download
    format: txt
    id: icd10.downloads
    name: ICD-10 Downloads
    product_url: https://www.who.int/standards/classifications/classification-of-diseases
    original_source:
      - source: icd10
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Training materials and courses for learning ICD-10 coding and classification
    format: http
    id: icd10.training
    name: ICD-10 Training
    product_url: https://icd.who.int/training/icd10training/
    warnings:
      - File was not able to be retrieved when checked on 2025-12-07_ Error connecting to URL_ HTTPSConnectionPool(host='icd.who.int', port=443)_ Max retries exceeded with url_ /training/icd10training/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
      - File was not able to be retrieved when checked on 2025-12-05_ Error connecting to URL_ HTTPSConnectionPool(host='icd.who.int', port=443)_ Max retries exceeded with url_ /training/icd10training/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
    original_source:
      - source: icd10
        relation_type: prov:hadPrimarySource
  - category: MappingProduct
    description: The biannual release of the SNOMED CT to ICD-10-CM Map, which maps SNOMED CT concepts to ICD-10-CM codes.
    id: snomedct.icd10cm.map
    name: SNOMED CT to ICD-10-CM Map
    original_source:
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
    product_url: https://download.nlm.nih.gov/mlb/utsauth/ICD10CM/SNOMED_CT_to_ICD-10-CM_Resources_20250301.zip
  - category: MappingProduct
    description: Concept mappings between different terminology systems
    format: csv
    id: athena.mappings
    name: Athena Concept Mappings
    original_source:
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: icd10cm
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: cdiscvocab
        relation_type: prov:hadPrimarySource
      - source: ciel
        relation_type: prov:hadPrimarySource
    product_url: https://athena.ohdsi.org/search-terms/start
    secondary_source:
      - source: athena
        relation_type: prov:wasInfluencedBy
    warnings:
      - Athena mapping exports are accessed through the authenticated Athena web application; stable direct public file URLs are not exposed.
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: icd10 Nodes TSV
    format: tsv
    id: obo-db-ingest.icd10.tsv
    license:
      id: https://cdn.who.int/media/docs/default-source/publishing-policies/copyright/who-faq-licensing-icd-10.pdf
      label: Custom
    name: icd10 Nodes TSV
    original_source:
      - source: icd10
        relation_type: prov:hadPrimarySource
    product_file_size: 40794
    product_url: https://w3id.org/biopragmatics/resources/icd10/icd10.tsv
    secondary_source:
      - source: obo-db-ingest
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Downloadable standardized vocabulary bundles for OMOP CDM assembled through the authenticated Athena web application
    format: csv
    id: athena.vocabularies
    name: Athena Vocabulary Downloads
    original_source:
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: icd10cm
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: cdiscvocab
        relation_type: prov:hadPrimarySource
      - source: ciel
        relation_type: prov:hadPrimarySource
      - source: rxnorm
        relation_type: prov:hadPrimarySource
      - source: ndcd
        relation_type: prov:hadPrimarySource
      - source: gemscript
        relation_type: prov:hadPrimarySource
      - source: medispan-gpi
        relation_type: prov:hadPrimarySource
    product_url: https://athena.ohdsi.org/vocabulary/list
    secondary_source:
      - source: athena
        relation_type: prov:wasInfluencedBy
    warnings:
      - Athena vocabulary downloads are prepared through the logged-in web application; stable direct public file URLs are not exposed.
publications:
  - id: https://doi.org/10.1186/s12911-021-01534-6
    title: ICD-11 - an international classification of diseases for the twenty-first century
repository: https://github.com/ICD-Codes
synonyms:
  - ICD-10
  - ICD10
  - International Classification of Diseases 10th Revision
taxon:
  - NCBITaxon:9606
---

# ICD-10

The International Classification of Diseases, 10th Revision (ICD-10), is the WHO's standardized system for disease classification used worldwide for over 30 years.
