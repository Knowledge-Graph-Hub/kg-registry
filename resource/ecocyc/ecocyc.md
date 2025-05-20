---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biocyc-support@sri.com
  - contact_type: url
    value: https://ecocyc.org/contact.shtml
  label: EcoCyc
description: EcoCyc captures information from 44,000 publications for Escherichia
  coli K-12 substr. MG1655. Use EcoCyc to search for knowledge on E. coli genes, regulation,
  and metabolism; analyze transcriptomics data; perform comparative analyses; and
  run a metabolic model.
domains:
- microbiology
- genomics
- biological systems
- pathways
- metabolomics
homepage_url: https://ecocyc.org/
id: ecocyc
layout: resource_detail
license:
  id: https://ecocyc.org/download.shtml
  label: Varies
name: EcoCyc
repository: https://biocyc.org/download.shtml
products:
- category: MappingProduct
  description: Rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: Rhea SSSOM
  original_source:
  - rhea
  - reactome
  - kegg
  - metacyc
  - m-csa
  - ecocyc
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: GraphicalInterface
  description: Web interface for EcoCyc database
  id: ecocyc.web
  name: EcoCyc Web Interface
  product_url: https://ecocyc.org/
  original_source:
  - ecocyc
- category: ProgrammingInterface
  description: Web services and APIs for programmatic access to EcoCyc data
  id: ecocyc.api
  name: EcoCyc Web Services
  product_url: https://ecocyc.org/web-services.shtml
  is_public: true
  connection_url: https://ecocyc.org/web-services.shtml
  original_source:
  - ecocyc
- category: ProcessProduct
  description: Metabolic model for E. coli K-12 derived from EcoCyc
  id: ecocyc.metabolic_model
  name: EcoCyc Metabolic Model
  product_url: http://www.biomedcentral.com/1752-0509/8/79
  original_source:
  - ecocyc
collection:
- translator
---

EcoCyc is a comprehensive database that captures information from over 44,000 publications for Escherichia coli K-12 substr. MG1655. It is part of the larger BioCyc collection of thousands of Pathway/Genome Databases for sequenced genomes. 

EcoCyc provides detailed information on:
- E. coli genes and their regulation
- Metabolic pathways and reactions
- Protein complexes and functions
- Transporters and small molecules

The database supports various analytical tools including:
- Transcriptomics and metabolomics data analysis
- Comparative genome analysis across more than 500 E. coli strains
- Metabolic pathway visualization and analysis
- Quantitative metabolic modeling