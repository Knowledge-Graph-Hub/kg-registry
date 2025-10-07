---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@oncokb.org
  - contact_type: url
    value: https://www.oncokb.org/
  label: OncoKB Team
creation_date: '2025-08-12T00:00:00Z'
description: OncoKB is a precision oncology knowledge base developed at Memorial Sloan
  Kettering Cancer Center that contains biological and clinical information about
  genomic alterations in cancer. It provides alteration- and tumor type-specific therapeutic
  implications classified using the OncoKB Levels of Evidence system, which assigns
  clinical actionability to individual mutational events. The platform integrates
  data from 945 genes, 7967 alterations, 143 cancer types, and 156 drugs with FDA-recognized
  human genetic variant database status.
domains:
- precision medicine
- clinical
- genomics
- biomedical
- health
homepage_url: https://www.oncokb.org/
id: oncokb
last_modified_date: '2025-09-24T00:00:00Z'
layout: resource_detail
name: OncoKB
products:
- category: GraphicalInterface
  description: Interactive web interface for exploring OncoKB precision oncology knowledge
    base, including gene and variant information, therapeutic implications, and evidence
    levels
  format: http
  id: oncokb.web_interface
  name: OncoKB Web Interface
  original_source:
  - oncokb
  product_url: https://www.oncokb.org/
- category: ProgrammingInterface
  description: RESTful web API providing programmatic access to OncoKB data including
    gene annotations, variant classifications, therapeutic implications, and evidence
    levels
  format: json
  id: oncokb.api
  name: OncoKB Web API
  original_source:
  - oncokb
  product_url: https://www.oncokb.org/swagger-ui/index.html
- category: ProcessProduct
  description: Python-based annotation tool for annotating MAF files, copy number
    alterations, fusions, and structural variants with OncoKB therapeutic and biological
    annotations
  format: python
  id: oncokb.annotator
  name: OncoKB Annotator
  original_source:
  - oncokb
  product_url: https://github.com/oncokb/oncokb-annotator
- category: GraphicalInterface
  description: Demo version of OncoKB containing full data for BRAF, TP53, and ROS1
    genes for evaluation purposes before licensing
  format: http
  id: oncokb.demo
  name: OncoKB Demo
  original_source:
  - oncokb
  product_url: https://demo.oncokb.org/
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
- authors:
  - Debyani Chakravarty
  - Jianjiong Gao
  - Sarah M. Phillips
  - Ritika Kundra
  - Hongxin Zhang
  - Jiaojiao Wang
  - Julia E. Rudolph
  - Ramdan Yaeger
  - Tara Soumerai
  - Ahmet H. Nissan
  - Matthew T. Chang
  - Sarah Adalsteinsson
  - Barry S. Taylor
  - Gregory J. Riely
  - Marc Ladanyi
  - David B. Solit
  - Nikolaus Schultz
  doi: 10.1200/PO.17.00011
  id: doi:10.1200/PO.17.00011
  title: 'OncoKB: A Precision Oncology Knowledge Base'
  year: '2017'
- authors:
  - Samuel P. Suehnholz
  - Ritika Kundra
  - Hongxin Zhang
  - Jianjiong Gao
  - Angelica M. Camargo
  - Isabell Schulze
  - Matthew T. Chang
  - Sarah Adalsteinsson
  - Brie Kezlarian
  - Kendra A. Famiglietti
  - Tara Soumerai
  - Barry S. Taylor
  - Gregory J. Riely
  - Marc Ladanyi
  - David B. Solit
  - Nikolaus Schultz
  - Debyani Chakravarty
  doi: 10.1158/2159-8290.CD-23-0467
  id: doi:10.1158/2159-8290.CD-23-0467
  title: Quantifying the Expanding Landscape of Clinical Actionability for Patients
    with Cancer
  year: '2023'
repository: https://github.com/oncokb
---
# OncoKB

OncoKB is a precision oncology knowledge base developed at Memorial Sloan Kettering Cancer Center that serves as a comprehensive resource for understanding the clinical actionability of genomic alterations in cancer. The platform provides expertly curated information about the biological and therapeutic implications of cancer variants, enabling clinicians and researchers to make informed decisions in precision oncology.

## Overview

OncoKB is an FDA-recognized human genetic variant database that integrates biological and clinical information about genomic alterations across various cancer types. The knowledge base systematically categorizes therapeutic implications using the OncoKB Levels of Evidence system, which assigns clinical actionability to individual mutational events based on the strength of available evidence.

## Key Features

### Comprehensive Coverage
OncoKB currently encompasses:
- **945 genes** with curated cancer relevance
- **7,967 alterations** with detailed annotations
- **143 cancer types** with specific therapeutic contexts  
- **156 drugs** with associated therapeutic implications

### Evidence-Based Classification System
The OncoKB Levels of Evidence system provides a standardized framework for interpreting the clinical significance of genomic alterations:

**Therapeutic Levels:**
- **Level 1**: FDA-approved drugs with biomarker-specific indications
- **Level 2**: Standard care biomarkers recommended by NCCN or expert panels
- **Level 3A**: Compelling clinical evidence for biomarker-drug associations in specific tumor types
- **Level 3B**: Standard care or investigational biomarkers in other indications
- **Level 4**: Compelling biological evidence
- **Level R1/R2**: Resistance implications with varying levels of evidence

**Diagnostic and Prognostic Levels:**
- **Dx1-Dx3**: Diagnostic implications with FDA-approved, guideline-recommended, or investigational evidence
- **Px1-Px3**: Prognostic implications with similar evidence gradations

### Expert Curation Process
All annotations in OncoKB undergo rigorous expert curation following standardized operating procedures. The curation team systematically reviews literature evidence and clinical trial data to ensure accuracy and clinical relevance. The curation process is version-controlled and regularly updated to reflect new evidence and regulatory approvals.

## Applications and Use Cases

### Clinical Decision Support
OncoKB serves as a critical resource for:
- Interpreting genomic testing results in clinical practice
- Identifying FDA-approved targeted therapies for specific alterations
- Understanding resistance mechanisms and alternative treatment options
- Supporting molecular tumor boards and precision oncology programs

### Research Applications
The platform enables:
- Large-scale genomic analysis with standardized annotation
- Clinical trial design and patient stratification
- Biomarker discovery and validation studies
- Pharmacogenomic research and drug development

### Bioinformatics Integration
OncoKB provides multiple access methods for computational workflows:
- RESTful web API for programmatic data access
- OncoKB Annotator for batch annotation of genomic data
- Integration with popular analysis platforms and pipelines
- Standardized output formats compatible with clinical systems

## Data Access and Licensing

OncoKB operates under a tiered licensing model:
- **Academic Research**: Free access for non-commercial academic research
- **Commercial Use**: Licensing fees required for commercial applications
- **Demo Access**: Limited demo version available for evaluation

All programmatic access requires registration and API token authentication. The platform maintains strict data use agreements to ensure appropriate use of curated knowledge while supporting both academic research and clinical implementation.

## Integration with Broader Ecosystem

OncoKB is deeply integrated with the Memorial Sloan Kettering computational oncology ecosystem, including:
- **cBioPortal**: Cancer genomics data visualization and analysis
- **OncoTree**: Standardized cancer type classification system
- **IMPACT**: MSK's targeted sequencing panel and analysis pipeline

The knowledge base also contributes to and aligns with broader precision oncology initiatives, supporting standardized approaches to genomic interpretation across institutions and healthcare systems.