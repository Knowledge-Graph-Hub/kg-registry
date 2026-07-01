---
activity_status: active
category: Aggregator
collection:
- aop
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/
  label: U.S. Environmental Protection Agency (EPA)
creation_date: '2025-06-24T00:00:00Z'
description: The Adverse Outcome Pathway Database (AOP-DB) is an EPA-developed integrative
  knowledgebase that connects chemicals and stressors to molecular initiating events,
  key events across biological organization levels, and adverse outcomes relevant
  to human health and ecological risk assessment. It harmonizes data from toxicology,
  high‑throughput screening, pathway, gene/protein, and phenotype resources to enable
  computational toxicology, mode-of-action analysis, and predictive risk prioritization.
domains:
- toxicology
- environment
- pathways
homepage_url: https://www.epa.gov/healthresearch/adverse-outcome-pathway-database-aop-db
id: aop-db
last_modified_date: '2026-06-22T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: aop-db
  product_url: https://www.epa.gov/healthresearch/adverse-outcome-pathway-database-aop-db
- category: ProgrammingInterface
  connection_url: https://aopdb.rdf.bigcat-bioinformatics.org/
  description: OpenRiskNet Virtuoso SPARQL endpoint loaded with RDF of the EPA AOP-DB
    for querying integrated AOP, gene, chemical, disease, tissue, pathway, orthology,
    ontology, and gene interaction relationships.
  format: http
  id: aop-db.sparql
  is_public: true
  name: AOP-DB SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://openrisknet.org/e-infrastructure/services/147/
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  format: http
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
- category: DocumentationProduct
  description: The EPA Adverse Outcome Pathway Database (Aop-DB) Application User
    Manual
  format: pdf
  id: aop-db.manual
  name: Manual
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-db
  product_url: https://ordspub.epa.gov/ords/eims/eimscomm.getfile?p_download_id=543383
  warnings:
  - File was not able to be retrieved when checked on 2025-12-05_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7f225f00d070>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7f7e93b00320>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7f9758bc2f20>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7fd84f0ad190>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-10-28_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7f4dcd859420>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-10-27_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7f1fbf9d1100>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-10-08_ Error connecting
    to URL_ HTTPSConnectionPool(host='ordspub.epa.gov', port=443)_ Max retries exceeded
    with url_ /ords/eims/eimscomm.getfile?p_download_id=543383 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7fca293233d0>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - 'File was not able to be retrieved when checked on 2026-06-27: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-26: Error connecting
    to URL: (''Connection aborted.'', RemoteDisconnected(''Remote end closed connection
    without response''))'
  - 'File was not able to be retrieved when checked on 2026-06-22: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-07-01: No Content-Length
    header found'
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  format: mixed
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
publications:
- authors:
  - Mortensen HM
  - Senn J
  - Levey T
  - Langley P
  - Williams AJ
  doi: 10.1038/s41597-021-00962-3
  id: doi:10.1038/s41597-021-00962-3
  journal: Scientific Data
  preferred: true
  title: The 2021 update of the EPA's adverse outcome pathway database
  year: '2021'
- authors:
  - Pittman ME
  - Edwards SW
  - Ives C
  - Mortensen HM
  doi: 10.1016/j.taap.2018.02.006
  id: doi:10.1016/j.taap.2018.02.006
  journal: Toxicology and Applied Pharmacology
  title: 'AOP-DB: A database resource for the exploration of Adverse Outcome Pathways
    through integrated association networks'
  year: '2018'
taxon:
- NCBITaxon:9606
version: '2'
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