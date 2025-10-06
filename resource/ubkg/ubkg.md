---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ubkg@pitt.edu
  label: University of Pittsburgh
- category: Organization
  contact_details:
  - contact_type: github
    value: x-atlas-consortia
  label: x-atlas-consortia
description: The Unified Biomedical Knowledge Graph (UBKG) is a knowledge graph infrastructure
  that represents a set of interrelated concepts from biomedical ontologies and vocabularies.
  It combines information from the National Library of Medicine's Unified Medical
  Language System (UMLS) with sets of assertions from ontologies outside the UMLS
  to establish connections between different sets of assertions that can enable discovery
  of previously unknown relationships.
domains:
- biomedical
- health
- genomics
homepage_url: https://ubkg.docs.xconsortia.org/
id: ubkg
layout: resource_detail
license:
  id: https://uts.nlm.nih.gov/uts/assets/LicenseAgreement.pdf
  label: UMLS License Agreement
name: Unified Biomedical Knowledge Graph
products:
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
  - cmap
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
  - nposckan
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
  - cmap
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
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: ProgrammingInterface
  description: REST API with endpoints that abstract common types of queries against
    a UBKG neo4j knowledge graph database. Requires UMLS API key to access.
  id: ubkg.api
  is_public: false
  name: UBKG API
  product_url: https://smart-api.info/ui/96e5b5c0b0efeef5b93ea98ac2794837
- category: GraphicalInterface
  description: Guesdt (Graphing UMLS Enables Search In Dynamic Trees) application
    used to represent the UBKG in a tree view.
  id: ubkg.guesdt
  name: UBKG Guesdt Interface
  product_url: https://x-atlas-consortia.github.io/Guesdt/
- category: GraphProduct
  description: A comprehensive multi-omics biomedical knowledge graph connecting genomic,
    transcriptomic, proteomic, and clinical data. Contains over 32 million nodes and
    118 million relationships.
  dump_format: neo4j
  edge_count: 118000000
  id: petagraph.graph
  name: Petagraph Knowledge Graph (Neo4J)
  node_count: 32000000
  original_source:
  - ubkg
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - petagraph
repository: https://github.com/x-atlas-consortia
usages:
- description: The Petagraph Knowledge Graph is built using UBKG as a scaffold.
  id: ubkg.part_of.petagraph
  label: UBKG is part of Petagraph
  type: actual
  url: https://doi.org/10.1038/s41597-024-04070-w
---
test test