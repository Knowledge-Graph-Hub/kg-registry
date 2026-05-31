---
activity_status: active
category: DataSource
collection:
- translator
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biocyc-support@sri.com
  - contact_type: url
    value: https://ecocyc.org/contact.shtml
  label: EcoCyc
creation_date: '2025-03-17T00:00:00Z'
description: EcoCyc captures information from 44,000 publications for Escherichia
  coli K-12 substr. MG1655. Use EcoCyc to search for knowledge on E. coli genes, regulation,
  and metabolism; analyze transcriptomics data; perform comparative analyses; and
  run a metabolic model.
domains:
- microbiology
- genomics
- biological systems
- pathways
homepage_url: https://ecocyc.org/
id: ecocyc
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://ecocyc.org/download.shtml
  label: Varies
name: EcoCyc
products:
- category: MappingProduct
  description: rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: m-csa
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
- category: GraphicalInterface
  description: Web interface for EcoCyc database
  format: http
  id: ecocyc.web
  name: EcoCyc Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  product_url: https://ecocyc.org/
- category: ProgrammingInterface
  connection_url: https://ecocyc.org/web-services.shtml
  description: Web services and APIs for programmatic access to EcoCyc data
  format: http
  id: ecocyc.api
  is_public: true
  name: EcoCyc Web Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  product_url: https://ecocyc.org/web-services.shtml
- category: ProcessProduct
  description: Metabolic model for E. coli K-12 derived from EcoCyc
  format: http
  id: ecocyc.metabolic_model
  name: EcoCyc Metabolic Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  product_url: http://www.biomedcentral.com/1752-0509/8/79
repository: https://biocyc.org/download.shtml
---
# EcoCyc

EcoCyc is the curated BioCyc database for *Escherichia coli* K-12 substr. MG1655.
It integrates literature-backed knowledge about genes, gene regulation,
metabolism, transport, protein complexes, and cellular processes into a single
reference environment for microbial systems biology.

Beyond being a reference encyclopedia, EcoCyc exposes interactive pathway and
genome browsers, comparative analysis tools, omics-data visualization, web
services, and a published metabolic model. The shared `rhea` SSSOM mapping stays
on this page as a propagated downstream product because it reuses EcoCyc reaction
content in a cross-resource integration workflow.