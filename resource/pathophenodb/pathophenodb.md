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
creation_date: '2025-05-28T00:00:00Z'
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
last_modified_date: '2025-12-13T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  product_file_size: 203836895
  product_url: http://patho.phenomebrowser.net/media/downloads/patho_pheno_withsymbols.nt
- category: GraphicalInterface
  description: Web interface for querying and browsing PathoPhenoDB data
  id: pathophenodb.web
  name: PathoPhenoDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  product_url: http://patho.phenomebrowser.net/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
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
taxon:
- NCBITaxon:9606
---
PathoPhenoDB Knowledge Graph