---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/bio-ontology-research-group
  label: Bio-Ontology Research Group
- category: Individual
  contact_details:
  - contact_type: github
    value: bio-ontology-research-group
  label: Bio-Ontology Research Group
description: PathoPhenoDB is a database of human pathogens, the diseases and phenotypes
  they elicit in human organisms, and information related to drug treatments and mechanisms
  of drug resistance. Specifically, PathoPhenoDB contains associations between pathogens
  and diseases, between pathogens and phenotypes, between drugs that are approved
  to treat particular pathogens, and it identifies genes or proteins within pathogens
  that can convey resistance to particular drugs.
domains:
- health
- microbiology
- pharmacology
- drug discovery
homepage_url: http://patho.phenomebrowser.net/
id: pathophenodb
layout: resource_detail
name: PathoPhenoDB
products:
- category: GraphProduct
  description: PathoPhenoDB data containing pathogen-disease and pathogen-phenotype
    associations
  format: ntriples
  id: pathophenodb.data
  name: PathoPhenoDB RDF data, version 3
  original_source:
  - pathophenodb
  product_url: http://patho.phenomebrowser.net/media/downloads/patho_pheno_withsymbols.nt
- category: GraphicalInterface
  description: Web interface for querying and browsing PathoPhenoDB data
  id: pathophenodb.web
  name: PathoPhenoDB Web Interface
  original_source:
  - pathophenodb
  product_url: http://patho.phenomebrowser.net/
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
  - "\u015Eenay Kafkas"
  - Marwa Abdelhakim
  - Yasmeen Hashish
  - Maxat Kulmanov
  - Marwa Abdellatif
  - Paul N. Schofield
  - Robert Hoehndorf
  id: http://doi.org/10.1038/s41597-019-0090-x
  journal: Scientific Data
  preferred: true
  title: PathoPhenoDB, linking human pathogens to their phenotypes in support of infectious
    disease research
  year: '2019'
repository: https://github.com/bio-ontology-research-group/pathophenodb
---
PathoPhenoDB Knowledge Graph