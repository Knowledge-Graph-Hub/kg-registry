---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: bgee@sib.swiss
  - contact_type: url
    value: https://www.bgee.org/contact/
  label: Bgee Team - SIB Swiss Institute of Bioinformatics
description: Bgee is a database for retrieval and comparison of gene expression patterns
  across multiple animal species, providing information about gene expression in different
  anatomical structures, developmental stages, and species.
domains:
- biological systems
- organisms
homepage_url: https://www.bgee.org/
id: bgee
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Bgee - Gene Expression Database
products:
- category: GraphicalInterface
  description: Web interface for exploring Bgee data
  id: bgee.site
  is_public: true
  name: Bgee Web Interface
  original_source:
  - bgee
  product_url: https://www.bgee.org/
  secondary_source:
  - bgee
- category: ProgrammingInterface
  description: SPARQL endpoint for querying Bgee RDF data
  id: bgee.sparql
  is_public: true
  name: Bgee SPARQL Endpoint
  original_source:
  - bgee
  product_url: https://www.bgee.org/sparql/
  secondary_source:
  - bgee
- category: Product
  compression: zip
  description: Complete data dump of Bgee expression data for all species
  format: tsv
  id: bgee.expr_calls
  name: Bgee Expression Calls
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/expr_calls/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: RNA-Seq data processed and formatted for the Bgee database
  format: tsv
  id: bgee.rnaseq
  name: Bgee RNA-Seq Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/rna_seq/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Processed Affymetrix microarray data for the Bgee database
  format: tsv
  id: bgee.affymetrix
  name: Bgee Affymetrix Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/affymetrix/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: In Situ Hybridization data in the Bgee database
  format: tsv
  id: bgee.in_situ
  name: Bgee In Situ Hybridization Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/in_situ/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: EST (Expressed Sequence Tag) expression data in the Bgee database
  format: tsv
  id: bgee.est
  name: Bgee EST Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/est/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Single-cell RNA-Seq processed data in the Bgee database
  format: tsv
  id: bgee.sc_rnaseq
  name: Bgee Single-cell RNA-Seq Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/sc_rnaseq/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Anatomical homology information used in Bgee
  format: tsv
  id: bgee.homology
  name: Bgee Anatomical Homology Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/homology/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: RDF version of the Bgee data for semantic web applications
  format: ttl
  id: bgee.rdf
  name: Bgee RDF Data
  original_source:
  - bgee
  product_url: https://www.bgee.org/download/data-dumps/current/rdf/
  secondary_source:
  - bgee
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-20: Timeout connecting
    to URL'
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  secondary_source:
  - spoke
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
  - gwas-catalog
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
  - gwas-catalog
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
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
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
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
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
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 404 error
    when accessing file'
publications:
- authors:
  - Bastian FB
  - Brandulas Cammarata A
  - Carsanaro S
  - Detering H
  - Huang W-T
  - Joye S
  - Niknejad A
  - Nyamari M
  - Mendes de Farias T
  - Moretti S
  - Tzivanopoulou M
  - Wollbrett J
  - Robinson-Rechavi M
  doi: doi:10.1093/nar/gkae1118
  id: doi:10.1093/nar/gkae1118
  preferred: true
  title: Bgee in 2024 - focus on curated single-cell RNA-seq datasets, and query tools
  year: '2025'
- authors:
  - Bastian FB
  - Roux J
  - Niknejad A
  - Comte A
  - Fonseca Costa SS
  - de Farias TM
  - Moretti S
  - Parmentier G
  - de Laval VR
  - Rosikiewicz M
  - Wollbrett J
  - Echchiki A
  - Escoriza A
  - Gharib WH
  - Gonzales-Porta M
  - Jarosz Y
  - Laurenczy B
  - Moret P
  - Person E
  - Roelli P
  - Sanjeev K
  - Seppey M
  - Robinson-Rechavi M
  doi: doi:10.1093/nar/gkaa793
  id: doi:10.1093/nar/gkaa793
  title: The Bgee suite - integrated curated expression atlas and comparative transcriptomics
    in animals
  year: '2021'
repository: https://github.com/BgeeDB/bgee_apps
---
Bgee (Background Expression) is a database for retrieval and comparison of gene expression patterns across multiple animal species. It integrates multiple data types (RNA-Seq, Affymetrix microarrays, in situ hybridization, EST data, and single-cell RNA-Seq) to provide a unified view of gene expression patterns across diverse anatomical structures, developmental stages, and species.

The key features of Bgee include:

- Integration of multiple expression data types from various sources
- Careful curation of expression data, including quality assessment and filtering
- Mapping of expression data to anatomical and developmental ontologies
- Cross-species comparisons of gene expression patterns using anatomical homology relationships
- Expression calls that indicate the presence/absence of gene expression in specific conditions
- Anatomical homology relationships between species to facilitate evolutionary comparisons
- Data processing pipelines that ensure standardized analysis across different data sources

Bgee is widely used in comparative genomics, evolutionary developmental biology, and functional genomics to understand gene expression patterns and their evolution across species. The database currently covers more than 29 animal species including key model organisms such as human, mouse, zebrafish, and Drosophila.

The data is available through a user-friendly web interface, a SPARQL endpoint for semantic web queries, programmatic access via R and Python packages, and bulk downloads of data dumps for large-scale analyses.