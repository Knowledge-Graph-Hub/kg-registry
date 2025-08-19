---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: zfinadmn@zfin.org
  label: Zebrafish Information Network
description: Zebrafish Information Network, including the Zebrafish Anatomical Ontology
domains:
- biological systems
homepage_url: https://zfin.org/
id: zfin
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: ZFIN
products:
- category: Product
  description: Zebrafish Anatomical Ontology (OWL)
  id: zfin.zfa
  license:
    id: https://creativecommons.org/licenses/by/3.0/
    label: CC-BY-3.0
  name: ZFA
  original_source:
  - zfin
  product_file_size: 401588
  product_url: http://purl.obolibrary.org/obo/zfa.owl
  secondary_source:
  - zfin
- category: Product
  description: zfin OBO
  id: obo-db-ingest.zfin.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OBO
  original_source:
  - zfin
  product_file_size: 2643947
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: zfin OWL
  id: obo-db-ingest.zfin.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OWL
  original_source:
  - zfin
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.owl
  secondary_source:
  - obo-db-ingest
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
- category: Product
  description: zfin OBO Graph JSON
  id: obo-db-ingest.zfin.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OBO Graph JSON
  original_source:
  - zfin
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.json
  secondary_source:
  - obo-db-ingest
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
- category: MappingProduct
  description: zfin SSSOM
  id: obo-db-ingest.zfin.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin SSSOM
  original_source:
  - zfin
  product_file_size: 374627
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: Phenotype of Zebrafish Genes
  format: tsv
  id: zfin.gene-to-phenotype
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: ZFIN clean gene to phenotype
  original_source:
  - zfin
  product_file_size: 42545110
  product_url: https://zfin.org/downloads/phenoGeneCleanData_fish.txt
  secondary_source:
  - zfin
- category: Product
  description: Phenotype of Zebrafish Genes
  format: tsv
  id: zfin.gene-to-publication
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: ZFIN gene to publication
  original_source:
  - zfin
  product_file_size: 39531152
  product_url: https://zfin.org/downloads/gene_publication.txt
  secondary_source:
  - zfin
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
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
repository: https://github.com/ZFIN/
---
ZFIN