---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: SCKAN (SPARC Connectivity Knowledge base of the Autonomic Nervous system)
  is a curated knowledge base representing neural circuit connectivity in the autonomic
  nervous system, derived from SPARC data, anatomical expert interviews, and scientific
  literature. It supports reasoning and querying of central and peripheral nervous
  system-end organ circuitry, including detailed ApiNATOMY models for organs such
  as bladder, heart, colon, stomach, spleen, pancreas, and airways.
domains:
- biological systems
- anatomy and development
id: sckan
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: SCKAN
products:
- category: GraphicalInterface
  description: Interactive computational notebook (Org mode) for querying SCKAN via
    SPARQL and Cypher, supporting parameterized queries, code blocks, and graphical
    results. Distributed as a Docker image.
  format: http
  id: sckan.query_interface
  name: SCKAN Query Interface (Docker)
  product_url: https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan#download-docker-and-x11
- category: Product
  description: Detailed ApiNATOMY models of neural circuits for organs including bladder,
    heart, colon, stomach, spleen, pancreas, and airways. Models are available in
    open-physiology repositories.
  format: http
  id: sckan.apinatomy
  name: SCKAN ApiNATOMY Models
  product_url: https://github.com/open-physiology/apinatomy-models
- category: DocumentationProduct
  description: Documentation, setup instructions, tutorials, and example queries for
    using and exploring SCKAN.
  format: http
  id: sckan.docs
  name: SCKAN Documentation and Tutorials
  product_url: https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan
- category: Product
  description: Latest SCKAN data release, including curated knowledge and models,
    available via Zenodo.
  format: http
  id: sckan.data_release
  name: SCKAN Data Release
  product_url: https://doi.org/10.5281/zenodo.5337441
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
---
# SCKAN

SCKAN is the SPARC Connectivity Knowledge base of the Autonomic Nervous system, supporting reasoning and querying of neural circuit connectivity. It includes detailed ApiNATOMY models, a computational notebook interface, and extensive documentation. For more information, see the [SCKAN documentation](https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan).