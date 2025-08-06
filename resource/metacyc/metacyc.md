---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biocyc-support@sri.com
  label: MetaCyc
description: MetaCyc is a curated database of experimentally elucidated metabolic
  pathways from all domains of life. MetaCyc contains pathways involved in both primary
  and secondary metabolism, as well as associated metabolites, reactions, enzymes,
  and genes. The goal of MetaCyc is to catalog the universe of metabolism by storing
  a representative sample of each experimentally elucidated pathway.
domains:
- biological systems
homepage_url: https://metacyc.org/
id: metacyc
layout: resource_detail
license:
  id: https://metacyc.org/download.shtml
  label: Varies
name: MetaCyc
products:
- category: MappingProduct
  description: Rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: Rhea SSSOM
  original_source:
  - rhea
  - reactome
  - kegg
  - metacyc
  - m-csa
  - ecocyc
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
  secondary_source:
  - obo-db-ingest
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
---
MetaCyc