---
activity_status: active
category: Ontology
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: joncison
  label: Jon Ison
- category: Individual
  contact_details:
  - contact_type: github
    value: matuskalas
  label: Matúš Kalaš
- category: Individual
  contact_details:
  - contact_type: github
    value: hmenager
  label: Hervé Ménager
description: EDAM is an ontology of bioscientific data analysis and data management,
  covering topics, operations, data, identifiers, and formats. It supports semantic
  annotation of tools, workflows, training, and provenance metadata across life sciences.
domains:
- information technology
- biological systems
homepage_url: https://edamontology.org/
id: edam
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: EDAM Ontology
products:
- category: OntologyProduct
  description: EDAM OWL release
  format: owl
  id: edam.owl
  name: EDAM OWL
  original_source:
  - edam
  - dc
  - skos
  product_file_size: 3373041
  product_url: http://edamontology.org/EDAM.owl
  secondary_source:
  - edam
- category: OntologyProduct
  description: EDAM TSV export
  format: tsv
  id: edam.tsv
  name: EDAM TSV
  original_source:
  - edam
  - dc
  - skos
  product_file_size: 1977072
  product_url: https://edamontology.org/EDAM.tsv
  secondary_source:
  - edam
- category: OntologyProduct
  description: EDAM CSV export
  format: csv
  id: edam.csv
  name: EDAM CSV
  original_source:
  - edam
  - dc
  - skos
  product_file_size: 1977072
  product_url: https://edamontology.org/EDAM.csv
  secondary_source:
  - edam
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
publications:
- authors:
  - Ison J
  - Kalaš M
  - Jonassen I
  - Bolser D
  - Uludag M
  - et al.
  doi: 10.1093/bioinformatics/btt113
  id: doi:10.1093/bioinformatics/btt113
  journal: Bioinformatics
  preferred: true
  title: 'EDAM: an ontology of bioinformatics operations, types of data and identifiers,
    topics and formats'
  year: '2013'
repository: https://github.com/edamontology/edamontology
---
EDAM provides a simple, four-branch structure (Topic, Operation, Data, Format) to organise
concepts prevalent in computational biology and bioinformatics, enabling consistent
annotation and discovery of resources.