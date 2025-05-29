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
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
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