---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@dgidb.org
  - contact_type: url
    value: http://www.griffithlab.com
  label: Griffith Lab
description: The Drug Gene Interaction Database (DGIdb) is a resource that consolidates
  disparate data sources describing drug-gene interactions and gene druggability to
  help researchers identify actionable drug targets or repurposable drugs for genes
  of interest.
domains:
- health
- pharmacology
- drug discovery
- genomics
- precision medicine
homepage_url: https://dgidb.org
id: dgidb
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT
name: DGIdb
products:
- category: ProgrammingInterface
  description: API for programmatically accessing the Drug Gene Interaction Database
  id: dgidb.api
  is_public: true
  name: DGIdb API
  product_url: https://dgidb.org/api
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
publications:
- authors:
  - Cotto KC
  - Wagner AH
  - Feng YY
  - Kiwala S
  - Coffman AC
  - Spies G
  - Wollam A
  - Spies NC
  - Griffith OL
  - Griffith M
  doi: doi:10.1093/nar/gkx1143
  id: https://doi.org/10.1093/nar/gkx1143
  journal: Nucleic Acids Research
  preferred: true
  title: 'DGIdb 3.0: a redesign and expansion of the drug-gene interaction database'
  year: '2018'
- authors:
  - Wagner AH
  - Coffman AC
  - Ainscough BJ
  - Spies NC
  - Skidmore ZL
  - Campbell KM
  - Krysiak K
  - Pan D
  - McMichael JF
  - Eldred JM
  - Walker JR
  - Wilson RK
  - Mardis ER
  - Griffith M
  - Griffith OL
  doi: doi:10.1093/nar/gkv1165
  id: https://doi.org/10.1093/nar/gkv1165
  journal: Nucleic Acids Research
  title: 'DGIdb 2.0: mining clinically relevant drug-gene interactions'
  year: '2016'
- authors:
  - Griffith M
  - Griffith OL
  - Coffman AC
  - Weible JV
  - McMichael JF
  - Spies NC
  - Koval J
  - Das I
  - Callaway MB
  - Eldred JM
  - Miller CA
  - Subramanian J
  - Govindan R
  - Kumar RD
  - Bose R
  - Ding L
  - Walker JR
  - Larson DE
  - Dooling DJ
  - Smith SM
  - Ley TJ
  - Mardis ER
  - Wilson RK
  doi: doi:10.1038/nmeth.2689
  id: https://doi.org/10.1038/nmeth.2689
  journal: Nature Methods
  title: DGIdb - mining the druggable genome
  year: '2013'
repository: https://github.com/griffithlab/dgi-db
---
## DGIdb: Drug Gene Interaction Database

The Drug Gene Interaction Database (DGIdb) is a web resource that consolidates disparate data sources describing drug-gene interactions and gene druggability information. DGIdb helps researchers to prioritize the investigation of drug-gene interactions and identify actionable drug targets or repurposable drugs for genes of interest.

### Key Features

- **Comprehensive Integration**: Combines data from multiple sources of drug-gene interactions and druggable gene categories
- **Advanced Search**: Search for drug-gene interactions involving genes or drugs of interest
- **Druggable Gene Categories**: Browse druggable gene categories to identify genes that are potentially druggable
- **API Access**: Programmatically access DGIdb data through a JSON-based API
- **Regular Updates**: Continually updated with new drug-gene interaction sources

### Applications

DGIdb can be used to:

- Identify potential drug targets among a set of genes
- Find existing drugs that might interact with genes of interest
- Identify druggable genes within disease-specific gene sets
- Prioritize genes for experimental follow-up
- Support precision medicine initiatives by connecting genomic data to potential therapeutic options

### Data Sources

DGIdb integrates data from various sources including:

- Drug databases
- Gene interaction databases
- Clinical trial repositories
- Pharmaceutical knowledge bases
- Literature mining resources

This integration provides researchers with a comprehensive resource for drug-gene interaction information to support drug discovery and repurposing efforts in genomic medicine.