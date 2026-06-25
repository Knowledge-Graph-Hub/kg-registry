---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://support.nlm.nih.gov/knowledgebase/category/?id=CAT-01231&category=medlineplus
  id: ncbi
  label: National Library of Medicine
creation_date: '2025-11-08T00:00:00Z'
description: MedlinePlus is the premier online health information resource from the
  National Library of Medicine, providing comprehensive, trusted health and wellness
  information for patients, families, and the general public. As a service of the
  world's largest medical library and part of the National Institutes of Health, MedlinePlus
  delivers high-quality, evidence-based health content that is easy to understand,
  free of advertising, and available in both English and Spanish. The resource covers
  over 1,000 health topics including diseases, conditions, wellness information, and
  prevention strategies, with content organized into multiple categories including
  health topics, medical encyclopedia, drugs and supplements information, medical
  tests, healthy recipes, and genetics resources. MedlinePlus provides detailed information
  on prescription drugs, over-the-counter medicines, herbs, and supplements through
  its comprehensive drug information database. The medical encyclopedia contains thousands
  of articles, images, and videos covering diseases, symptoms, tests, and treatments.
  MedlinePlus Genetics offers information on genetic conditions, genes, chromosomes,
  and how genetic variations affect health.
domains:
- biomedical
homepage_url: https://medlineplus.gov/
id: medlineplus
infores_id: medlineplus
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: MedlinePlus
products:
- category: GraphicalInterface
  description: Main MedlinePlus website providing consumer-friendly health information
    organized into health topics, medical encyclopedia, drug information, medical
    tests, and genetics resources in English and Spanish
  format: http
  id: medlineplus.website
  name: MedlinePlus Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_url: https://medlineplus.gov/
- category: ProgrammingInterface
  description: Web service providing search-based health topic data in XML format
    for integration with external applications
  format: xml
  id: medlineplus.web_service
  name: MedlinePlus Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_url: https://medlineplus.gov/about/developers/webservices/
- category: ProgrammingInterface
  description: MedlinePlus Connect API enabling electronic health record systems and
    patient portals to link patients to relevant MedlinePlus health information based
    on their diagnoses and medications
  format: http
  id: medlineplus.connect_api
  name: MedlinePlus Connect API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_url: https://medlineplus.gov/connect/overview.html
- category: Product
  description: Downloadable XML files containing complete records for all English
    and Spanish health topics on MedlinePlus
  format: xml
  id: medlineplus.xml_files
  name: MedlinePlus XML Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_url: https://medlineplus.gov/xml.html
- category: ProgrammingInterface
  description: API and data files for retrieving genetic condition and gene information
    from MedlinePlus Genetics in XML or JSON format
  format: json
  id: medlineplus.genetics_api
  name: MedlinePlus Genetics API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_url: https://medlineplus.gov/about/developers/geneticsdatafilesapi/
- category: Product
  description: General-interest and health-topic RSS feed directory for current MedlinePlus
    content updates
  format: http
  id: medlineplus.rss_feeds
  name: MedlinePlus RSS Feeds
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_url: https://medlineplus.gov/rss.html
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
- category: GraphProduct
  description: KGX nodes file for JensenLab DISEASES KG
  format: kgx-jsonl
  id: kg-jensenlab-diseases.nodes.kgx
  name: DISEASES KGX nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_file_size: 130
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_kgx_nodes.jsonl
- category: GraphProduct
  description: KGX edges file for JensenLab DISEASES KG
  format: kgx-jsonl
  id: kg-jensenlab-diseases.edges.kgx
  name: DISEASES KGX edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_file_size: 132
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_kgx_edges.jsonl
- category: GraphProduct
  description: TRAPI edges file for JensenLab DISEASES KG
  format: trapi-jsonl
  id: kg-jensenlab-diseases.edges.trapi
  name: DISEASES TRAPI edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  product_file_size: 132
  product_url: https://github.com/biothings/pending.api/blob/translator-output/plugins/DISEASES/DISEASES_trapi_edges.jsonl
taxon:
- NCBITaxon:9606
---
# MedlinePlus

## Overview

MedlinePlus is the National Library of Medicine's premier online health information resource, providing trusted, high-quality health and wellness information for patients, families, and the general public. As a service of the world's largest medical library and part of the National Institutes of Health, MedlinePlus has been a cornerstone of consumer health information since its launch in 1998.

## Information Resource ID

This resource has the Information Resource identifier: `infores:medlineplus`

## Mission and Scope

MedlinePlus presents evidence-based health and wellness information that is trusted, easy to understand, and free of advertising, available in both English and Spanish. The resource is accessible anywhere, anytime, on any device, completely free of charge. All content is carefully reviewed and updated regularly by health professionals and librarians to ensure accuracy and currency.

## Key Features and Content

### Health Topics
- Over 1,000 comprehensive health topics covering diseases, conditions, and wellness
- Information organized by body system, condition, and prevention strategies
- Links to relevant research, clinical trials, and latest health news

### Medical Encyclopedia
- Thousands of articles with medical images and videos
- Coverage of diseases, symptoms, medical tests, and treatments
- A.D.A.M. Medical Encyclopedia content with detailed medical illustrations

### Drug Information
- Comprehensive information on prescription medications
- Over-the-counter medicines, herbs, and supplements
- Drug images, side effects, interactions, and proper usage

### Medical Tests
- Information explaining why doctors order specific tests
- What results may mean and how to prepare for tests
- Understanding laboratory values and diagnostic procedures

### MedlinePlus Genetics
- Information on genetic conditions and genes
- How genetic variations affect health
- Resources for understanding inheritance patterns and genetic testing

### Multilingual and Accessible Content
- Health information available in over 40 languages
- Easy-to-read health information for those with limited health literacy
- Accessible design meeting Section 508 standards

## Technical Resources

### For Developers
MedlinePlus provides multiple technical resources for integration:

- **Web Services**: Search-based health topic data in XML format
- **MedlinePlus Connect**: API for EHR systems and patient portals to link patients to relevant health information
- **XML Data Files**: Downloadable complete records for all health topics
- **Genetics API**: Retrieve genetic condition data in XML or JSON
- **RSS Feeds**: General-interest and topic-specific content feeds

### MedlinePlus Connect for EHRs
A specialized API enabling electronic health record systems and patient portals to automatically link patients to relevant, authoritative health information based on their diagnoses, medications, and lab test results. This helps patients better understand their health conditions and treatments.

## Content Standards

- All information is reviewed by health professionals and medical librarians
- Content meets the highest standards for accuracy and currency
- Regular updates ensure information reflects current medical knowledge
- No advertising or commercial bias
- Clear distinction between information and medical advice

## Usage and Impact

MedlinePlus serves millions of users monthly, making it one of the most visited health websites in the United States. The resource is widely used by patients, caregivers, students, health professionals, and librarians seeking reliable health information.

## Support and Contact

Customer support is available through the National Library of Medicine's knowledge base and help desk for questions about MedlinePlus content, functionality, and technical integration.