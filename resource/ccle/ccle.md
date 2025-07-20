---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: CCLE
description: CCLE is the Cancer Cell Line Encyclopedia, a collaboration between the
  Broad Institute and the Novartis Institutes for Biomedical Research.
domains:
- health
homepage_url: https://sites.broadinstitute.org/ccle/
id: ccle
layout: resource_detail
name: CCLE
products:
- category: Product
  description: ccle OBO
  format: obo
  id: obo-db-ingest.ccle.obo
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle OBO
  original_source:
  - ccle
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: ccle OWL
  format: owl
  id: obo-db-ingest.ccle.owl
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle OWL
  original_source:
  - ccle
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: ccle OBO Graph JSON
  format: json
  id: obo-db-ingest.ccle.json
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle OBO Graph JSON
  original_source:
  - ccle
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: ccle SSSOM
  format: sssom
  id: obo-db-ingest.ccle.sssom.tsv
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle SSSOM
  original_source:
  - ccle
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmdb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
---
CCLE