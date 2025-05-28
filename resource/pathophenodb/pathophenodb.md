---
activity_status: active
category: DataSource
conntacts:
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
description: "PathoPhenoDB is a database of human pathogens, the diseases and phenotypes they elicit in human organisms, and information related to drug treatments and mechanisms of drug resistance. Specifically, PathoPhenoDB contains associations between pathogens and diseases, between pathogens and phenotypes, between drugs that are approved to treat particular pathogens, and it identifies genes or proteins within pathogens that can convey resistance to particular drugs."
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
  description: PathoPhenoDB data containing pathogen-disease and pathogen-phenotype associations
  format: nt
  id: pathophenodb.data
  name: PathoPhenoDB RDF Knowledge Graph, version 3
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
repository: https://github.com/bio-ontology-research-group/pathophenodb
publications:
- id: http://doi.org/10.1038/s41597-019-0090-x
  preferred: true
  title: "PathoPhenoDB, linking human pathogens to their phenotypes in support of infectious disease research"
  authors:
  - "Şenay Kafkas"
  - "Marwa Abdelhakim"
  - "Yasmeen Hashish"
  - "Maxat Kulmanov"
  - "Marwa Abdellatif"
  - "Paul N. Schofield"
  - "Robert Hoehndorf"
  year: "2019"
  journal: "Scientific Data"
---
PathoPhenoDB Knowledge Graph
