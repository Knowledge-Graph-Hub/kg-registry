---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: Comparative Toxicogenomics Database
description: CTD is a robust, publicly available database that aims to advance understanding
  about how environmental exposures affect human health.
domains:
- chemistry and biochemistry
homepage_url: https://ctdbase.org/
id: ctd
layout: resource_detail
license:
  id: https://ctdbase.org/about/legal.jsp
  label: Custom
name: Comparative Toxicogenomics Database
products:
- category: GraphProduct
  description: CTD Automat
  format: kgx-jsonl
  id: automat.ctd
  infores_id: automat-ctd
  name: ctd_automat
  original_source:
  - ctd
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/CTD_Automat/latest/kgx_files
  secondary_source:
  - automat
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
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
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - do
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  format: kgx
  id: kg-monarch.graph
  name: KGX Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl
  name: KGX JSON-L Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  format: rdfxml
  id: kg-monarch.graph.rdf
  name: RDF Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  id: kg-monarch.graph.neo4j
  name: Neo4j Dump of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  id: kg-monarch.graph.duckdb
  name: DuckDB database of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb.gz
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
---
