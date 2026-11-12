---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: fimam@ucsd.edu
  label: Fahim T. Imam
- category: Organization
  contact_details:
  - contact_type: github
    value: SciCrunch
  - contact_type: url
    value: https://github.com/SciCrunch/sparc-curation
  label: SciCrunch
creation_date: '2025-09-09T00:00:00Z'
description: SCKAN (SPARC Connectivity Knowledge base of the Autonomic Nervous system)
  is a curated knowledge base representing neural circuit connectivity in the autonomic
  nervous system, derived from SPARC data, anatomical expert interviews, and scientific
  literature. It supports reasoning and querying of central and peripheral nervous
  system-end organ circuitry, including detailed ApiNATOMY models for organs such
  as bladder, heart, colon, stomach, spleen, pancreas, and airways.
domains:
- anatomy and development
- neuroscience
funding:
- National Institutes of Health (NIH) Common Fund, SPARC program (3OT2OD030541)
homepage_url: https://docs.sparc.science/docs/sckan
id: sckan
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: SCKAN
products:
- category: GraphicalInterface
  description: Interactive computational notebook (Org mode) for querying SCKAN via
    SPARQL and Cypher, supporting parameterized queries, code blocks, and graphical
    results. Distributed as a Docker image.
  format: http
  id: sckan.query_interface
  name: SCKAN Query Interface (Docker)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_url: https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan#download-docker-and-x11
- category: Product
  description: Detailed ApiNATOMY models of neural circuits for organs including bladder,
    heart, colon, stomach, spleen, pancreas, and airways. Models are available in
    open-physiology repositories.
  format: http
  id: sckan.apinatomy
  name: SCKAN ApiNATOMY Models
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_url: https://github.com/open-physiology/apinatomy-models
- category: DocumentationProduct
  description: Documentation, setup instructions, tutorials, and example queries for
    using and exploring SCKAN.
  format: http
  id: sckan.docs
  name: SCKAN Documentation and Tutorials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_url: https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan
- category: Product
  description: Latest SCKAN data release on Zenodo (concept DOI, resolving to the
    newest version), containing the raw data inputs with the Blazegraph journal file,
    the SciGraph database, and a Docker data image bundling both with server configuration
    files.
  format: http
  id: sckan.data_release
  name: SCKAN Data Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sparc
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: nif-ontology
  product_url: https://doi.org/10.5281/zenodo.5337441
- category: GraphicalInterface
  description: SCKAN Explorer, a query interface designed for SCKAN knowledge curators
    to check and verify connections without writing SPARQL, searchable by origin,
    destination, via location, phenotype, named model, neuron ID, species and target
    organ.
  format: http
  id: sckan.explorer
  name: SCKAN Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_url: https://services.scicrunch.io/sckan/explorer/
  rrid: SCR_026080
- category: DocumentationProduct
  description: Example SPARQL queries and Jupyter notebooks for SCKAN, including the
    code and results for the competency queries described in the SCKAN paper.
  format: http
  id: sckan.query-examples
  name: SCKAN Example Queries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_url: https://github.com/SciCrunch/sckan-query-examples
- category: DocumentationProduct
  description: SCKAN Curation Manual describing how neural connectivity knowledge
    is curated into SCKAN.
  format: http
  id: sckan.curation-manual
  name: SCKAN Curation Manual
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_url: https://doi.org/10.5281/zenodo.14774195
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  compression: zip
  description: Data Distillery SPARC subgraph (build of 2024-09-20) as CSV node and
    edge files. The SPARC Knowledge base of the Autonomic Nervous System (SCKAN).
  format: csv
  id: cfde-ddkg.sparc
  name: DDKG SPARC Subgraph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-ddkg
  - relation_type: prov:hadPrimarySource
    source: sparc
  - relation_type: prov:hadPrimarySource
    source: sckan
  product_file_size: 198292
  product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/SPARC.zip
publications:
- authors:
  - Imam FT
  - Gillespie TH
  - Ziogas I
  - Surles-Zeigler MC
  - Tappan S
  - Ozyurt BI
  - Boline J
  - de Bono B
  - Grethe JS
  - Martone ME
  doi: 10.3389/fninf.2025.1541184
  id: doi:10.3389/fninf.2025.1541184
  journal: Frontiers in Neuroinformatics
  preferred: true
  title: Developing a multiscale neural connectivity knowledgebase of the autonomic
    nervous system
  year: '2025'
repository: https://github.com/SciCrunch/sparc-curation
rrid: SCR_026088
synonyms:
- SPARC Connectivity Knowledgebase of the Autonomic Nervous System
- SPARC Connectivity Knowledge base of the Autonomic Nervous System
version: '2026-02-11'
---
# SCKAN

SCKAN is the SPARC Connectivity Knowledge base of the Autonomic Nervous system, supporting reasoning and querying of neural circuit connectivity. It includes detailed ApiNATOMY models, a computational notebook interface, and extensive documentation. For more information, see the [SCKAN documentation](https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan).