---
activity_status: active
category: Aggregator
collection:
- aop
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/
  label: U.S. Environmental Protection Agency (EPA)
description: The Adverse Outcome Pathway Database (AOP-DB) is an EPA-developed integrative
  knowledgebase that connects chemicals and stressors to molecular initiating events,
  key events across biological organization levels, and adverse outcomes relevant
  to human health and ecological risk assessment. It harmonizes data from toxicology,
  high‑throughput screening, pathway, gene/protein, and phenotype resources to enable
  computational toxicology, mode-of-action analysis, and predictive risk prioritization.
domains: []
homepage_url: https://www.epa.gov/healthresearch/adverse-outcome-pathway-database-aop-db
id: aop-db
last_modified_date: '2025-09-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.epa.gov/healthresearch/adverse-outcome-pathway-database-aop-db
  label: EPA AOP-DB Use & Access
name: AOP-DB
products:
- category: GraphicalInterface
  description: Public information portal describing the AOP-DB scope, data integration
    approach, and access points
  format: http
  id: aop-db.portal
  name: AOP-DB Information Portal
  original_source:
  - aop-db
  product_url: https://www.epa.gov/healthresearch/adverse-outcome-pathway-database-aop-db
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - aop-wiki
  - ctd
  - toxcast
  - disgenet
  - ncbigene
  - string
  - 1000genomes
  - ensembl
  - gwascatalog
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
  secondary_source:
  - aop-db
- category: DocumentationProduct
  description: The EPA Adverse Outcome Pathway Database (Aop-DB) Application User
    Manual
  format: pdf
  id: aop-db.manual
  name: Manual
  original_source:
  - aop-db
  product_url: https://ordspub.epa.gov/ords/eims/eimscomm.getfile?p_download_id=543383
  warnings:
  - File was not able to be retrieved when checked on 2025-09-09_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-10_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-10: No Content-Length
    header found'
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
---
# AOP-DB

## Overview

The Adverse Outcome Pathway Database (AOP-DB) supports chemical safety evaluation by integrating data that link molecular initiating events (MIEs) through key events (KEs) to adverse outcomes (AOs). By bridging multi-omic, pathway, and phenotypic evidence, the AOP-DB facilitates hypothesis generation, mode-of-action elucidation, and prioritization of chemicals for further testing.

## Scope & Content

- Molecular initiating events and downstream key events across biological levels
- Linkages between genes/proteins, pathways, phenotypes, and adverse outcomes
- Chemical associations and stressor mappings relevant to toxicological assessment
- Cross-references to public pathway, gene, and ontology resources (e.g., GO, Reactome)

## Use Cases

- Computational toxicology modeling and read-across
- Building structured Adverse Outcome Pathways for regulatory submissions
- Identifying data gaps in mechanistic evidence chains
- Prioritizing chemicals for targeted testing strategies

## Access

The current public EPA portal provides documentation and background on the AOP-DB. Additional programmatic or bulk access mechanisms may be added in future releases and can be incorporated here as products when available.

## Citation & Attribution

When using AOP-DB information, cite the EPA AOP-DB portal and any underlying pathway or ontology resources referenced in your analyses.

## Contact

General inquiries can be directed via the EPA website. Additional contact details will be added if dedicated AOP-DB communication channels are published.