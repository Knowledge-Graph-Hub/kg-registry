---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: DrugCentral
description: DrugCentral is online drug information resource created and maintained
  by Division of Translational Informatics at University of New Mexico.
domains:
- health
homepage_url: https://drugcentral.org/
id: drugcentral
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: DrugCentral
products:
- category: GraphProduct
  description: DrugCentral Automat
  format: kgx-jsonl
  id: automat.drugcentral
  infores_id: automat-drug-central
  name: drugcentral_automat
  original_source:
  - drugcentral
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/DrugCentral_Automat/latest/kgx_files
  secondary_source:
  - automat
- category: Product
  compression: gzip
  description: PostgreSQL (v14.5) database dump of all information in DrugCentral.
  format: postgres
  id: drugcentral.data
  name: DrugCentral Database dump
  original_source:
  - drugcentral
  product_url: https://unmtid-dbs.net/download/drugcentral.dump.11012023.sql.gz
  secondary_source:
  - drugcentral
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
publications:
- authors:
  - Ursu O
  - Holmes J
  - Knockel J
  - Bologa CG
  - Yang JJ
  - Mathias SL
  - Nelson SJ
  - Oprea TI
  doi: doi:10.1093/nar/gkw993
  id: doi:10.1093/nar/gkw993
  title: 'DrugCentral: online drug compendium'
  year: '2017'
---
DrugCentral