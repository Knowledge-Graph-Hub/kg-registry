---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: reactome-help@reactome.org
  label: Reactome Support
  orcid: null
creation_date: '2025-03-17T00:00:00Z'
description: Reactome is a comprehensive, curated, and peer-reviewed pathway database
  representing human biological processes. It integrates information on biological
  molecules including proteins, small molecules, and RNA, organizing them into networks
  of functional interactions organized as pathways. With sophisticated graph database
  backend and multiple data access formats, Reactome is an essential resource for
  systems biology, functional genomics, drug discovery, and biomedical research, providing
  insights into gene function in the context of cellular and organismal processes.
domains:
- biological systems
- pathways
- systems biology
- biomedical
homepage_url: https://reactome.org
id: reactome
infores_id: reactome
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Reactome
products:
- category: Product
  description: Conversion from BioPAX, human subset
  format: sqlite
  id: reactome.data.human
  name: Reactome Human from BioPAX, sqlite
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 178009249
  product_url: https://s3.amazonaws.com/bbop-sqlite/reactome-hs.db.gz
- category: GraphProduct
  compression: zip
  description: Complete Reactome pathway data in BioPAX (Biological Pathway Exchange)
    format, the standard RDF/OWL-based language for representing biological pathways
    at molecular and cellular levels
  format: owl
  id: reactome.biopax
  name: Reactome BioPAX Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 172887692
  product_url: https://download.reactome.org/96/biopax.zip
- category: GraphProduct
  compression: targz
  description: Reactome pathway data in SBML (Systems Biology Markup Language) format
    for computational modeling and systems biology applications, including kinetic
    information
  format: sbml
  id: reactome.sbml
  name: Reactome SBML Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 219489949
  product_url: https://download.reactome.org/96/all_species.3.1.sbml.tgz
- category: GraphProduct
  description: Reactome data in RDF/XML format for semantic web integration and knowledge
    graph applications
  format: rdfxml
  id: reactome.rdf
  name: Reactome RDF/XML Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_url: https://reactome.org/download-data
- category: GraphProduct
  description: Complete Reactome pathway database in native Neo4j graph database format,
    supporting interactive exploration and complex relationship queries
  dump_format: neo4j
  format: neo4j
  id: reactome.neo4j
  name: Reactome Neo4j Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 533108259
  product_url: https://download.reactome.org/96/reactome.graphdb.dump
- category: GraphProduct
  compression: targz
  description: Reactome graph database archive package for local graph database deployment
  dump_format: neo4j
  format: neo4j
  id: reactome.graphdb.archive
  name: Reactome Graph Database Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 450783610
  product_url: https://download.reactome.org/96/reactome.graphdb.tgz
- category: GraphProduct
  description: Pathway hierarchy relationships in flat text format
  format: txt
  id: reactome.flat
  name: Reactome Pathway Hierarchy Flat File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 631240
  product_url: https://download.reactome.org/96/ReactomePathwaysRelation.txt
- category: Product
  compression: gzip
  description: Main MySQL database dump for the current Reactome release
  format: txt
  id: reactome.mysql.main
  name: Reactome Main MySQL Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 120092667
  product_url: https://download.reactome.org/96/databases/gk_current.sql.gz
- category: Product
  compression: gzip
  description: Stable identifiers MySQL database dump for the current Reactome release
  format: txt
  id: reactome.mysql.stable_ids
  name: Reactome Stable IDs MySQL Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 259536887
  product_url: https://download.reactome.org/96/databases/gk_stable_ids.sql.gz
- category: Product
  description: Complete list of Reactome pathways in flat text format
  format: txt
  id: reactome.pathways.txt
  name: Reactome Pathway List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 1583655
  product_url: https://download.reactome.org/96/ReactomePathways.txt
- category: Product
  compression: gzip
  description: Gene association file for Reactome GO annotations
  format: txt
  id: reactome.go-associations.txt
  name: Reactome Gene Association File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 835232
  product_url: https://download.reactome.org/96/gene_association.reactome.gz
- category: Product
  description: Mapping from Reactome pathways to Gene Ontology terms
  format: txt
  id: reactome.pathways.go-terms.txt
  name: Reactome Pathways to GO Terms
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 60582
  product_url: https://download.reactome.org/96/Pathways2GoTerms_human.txt
- category: ProgrammingInterface
  description: RESTful web service API for programmatic access to Reactome pathway
    data and content, supporting JSON responses for web applications and tools
  format: http
  id: reactome.api
  name: Reactome REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_url: https://reactome.org/ContentService/
- category: DocumentationProduct
  description: Developer guide for the Reactome Content Service, including API usage,
    examples, and links to the interactive endpoint documentation.
  format: http
  id: reactome.api.docs
  name: Reactome Content Service Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_url: https://reactome.org/dev/content-service
- category: GraphicalInterface
  description: Interactive pathway browser providing visual exploration of human biological
    pathways, reactions, and molecular interactions with integrated visualization
    tools
  format: http
  id: reactome.browser
  name: Reactome Pathway Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_url: https://reactome.org/PathwayBrowser/
- category: MappingProduct
  description: rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: m-csa
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
- category: MappingProduct
  description: bigg.metabolite SSSOM
  format: sssom
  id: obo-db-ingest.bigg.metabolite.sssom.tsv
  license:
    id: http://bigg.ucsd.edu/license#license
    label: Custom
  name: bigg.metabolite SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 400516
  product_url: https://w3id.org/biopragmatics/resources/bigg.metabolite/bigg.metabolite.sssom.tsv
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
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
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_url: https://arax.ncats.io/
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: clinicalkg
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  compatibility:
  - standard: biolink
  compression: zip
  description: Curated mechanistic drug–disease paths comprising the DrugMechDB dataset
    packaged as a downloadable archive.
  dump_format: other
  format: mixed
  id: drugmechdb.graph
  latest_version: 2.0.1
  name: DrugMechDB Graph Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://doi.org/10.5281/zenodo.8139357
  repository: https://github.com/SuLab/DrugMechDB
  versions:
  - 2.0.1
  - 2.0.0
  - 1.0.2
  - '1.0'
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  edge_count: 14998050
  format: kgx
  id: kg-monarch.graph
  name: KGX Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  edge_count: 14998050
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl
  name: KGX JSON-L Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 315667976
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  edge_count: 14998050
  format: rdfxml
  id: kg-monarch.graph.rdf
  name: RDF Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  edge_count: 14998050
  id: kg-monarch.graph.neo4j
  name: Neo4j Dump of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 1438250397
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  warnings: []
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  edge_count: 14998050
  id: kg-monarch.graph.duckdb
  name: DuckDB database of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 6827814912
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genemania
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vo
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
  edge_count: 14998050
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl.edges
  name: KGX JSON-L Distribution of KG-Monarch Edges
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 15279494795
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.jsonl
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch (Nodes)
  edge_count: 14998050
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl.nodes
  name: KGX JSON-L Distribution of KG-Monarch Nodes
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 1149505896
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.jsonl
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Edges
  edge_count: 14998050
  format: neo4j
  id: kg-monarch.graph.neo4j.edges
  name: Neo4j Dump of KG-Monarch Edges
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 4386388748
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.neo4j.csv
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Nodes
  edge_count: 14998050
  format: neo4j
  id: kg-monarch.graph.neo4j.nodes
  name: Neo4j Dump of KG-Monarch Nodes
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1460060
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 349573789
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.neo4j.csv
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epigraphdb
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: vectology
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  - relation_type: prov:hadPrimarySource
    source: eqtlgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cpic
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: Product
  description: Pathway information integrated from Reactome, WikiPathways and other
    pathway databases
  format: http
  id: genecards.pathway.data
  name: GeneCards Pathway Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drkg
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ibkh
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
- category: DatabaseProduct
  description: Multi-sourced relational database integrating metabolomic pathway information,
    biochemical reactions, ontologies, and chemical descriptors for genes, proteins,
    and metabolites with query and enrichment analysis capabilities.
  id: rampdb.database
  is_public: true
  name: RaMP-DB Integrated Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: rampdb
  product_url: https://rampdb.nih.gov/
- category: Product
  description: Causal Activity Model graphs automatically generated from Reactome
    pathways using the Pathways2GO tool, translating pathway reactions to causal relationships
  id: cam-kp.reactome-cams
  name: Reactome Pathway CAMs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cam-kp
  - relation_type: prov:hadPrimarySource
    source: reactome
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, scored links between proteins)
  format: txt
  id: string.protein.links
  name: STRING Protein Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 138154280240
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, incl. subscores per channel)
  format: txt
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 203534412387
  product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (full network, incl. distinction: direct vs.
    interologs)'
  format: txt
  id: string.protein.links.full
  name: STRING Protein Links Full
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 214269334954
  product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, scored links between proteins)
  format: txt
  id: string.protein.physical.links
  name: STRING Protein Physical Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 11867396121
  product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, incl. subscores per channel)
  format: txt
  id: string.protein.physical.links.detailed
  name: STRING Protein Physical Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 14859366689
  product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (physical subnetwork, incl. distinction: direct
    vs. interologs)'
  format: txt
  id: string.protein.physical.links.full
  name: STRING Protein Physical Links Full
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 15528028374
  product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores between orthologous groups
  format: txt
  id: string.cog.links
  name: STRING COG Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 185338269
  product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores (incl. subscores per channel)
  format: txt
  id: string.cog.links.detailed
  name: STRING COG Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 250279091
  product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'full database, part II: the networks (nodes, edges, scores,...)'
  id: string.database
  name: STRING Database Network Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 281505096430
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
- category: Product
  compression: 7z
  description: Compressed CSV file containing ProteomeHD v1.1, with 10,323 proteins
    measured across 294 SILAC ratios
  format: csv
  id: proteomehd.data
  name: ProteomeHD Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  product_file_size: 9427082
  product_url: https://raw.githubusercontent.com/Rappsilber-Laboratory/ProteomeHD/master/Data/ProteomeHD_v1_1.7z
- category: Product
  description: reactome Nodes TSV
  format: tsv
  id: obo-db-ingest.reactome.tsv
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: reactome Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 445199
  product_url: https://w3id.org/biopragmatics/resources/reactome/reactome.tsv
- category: GraphProduct
  description: Graph database dump and additional relationship files for the Clinical
    Knowledge Graph.
  format: neo4j
  id: ckg.graph
  latest_version: '1'
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: CKG Graph Database Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: ckg
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Reactome pathway event hierarchy edges
  format: csv
  id: prokn.reactome.pathway.event_of.pathway.edges
  name: ProKN Reactome Pathway Event Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1088495
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/Reactome.Pathway.PATHWAY_EVENT_OF.Pathway.edges.csv
- category: GraphProduct
  description: Reactome protein participates in pathway edges
  format: csv
  id: prokn.reactome.protein.participates_in.pathway.edges
  name: ProKN Reactome Protein Pathway Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 17112000
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/Reactome.Protein.PARTICIPATES_IN.Pathway.edges.csv
- category: GraphProduct
  description: Neo4j knowledge graph containing integrated gene sets from multiple
    Common Fund programs with cross-references
  dump_format: neo4j
  format: neo4j
  id: cfde-gse.graph
  name: CFDE-GSE Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
- category: Product
  description: Standardized gene set collections from Common Fund programs in GMT
    format
  id: cfde-gse.genesets
  name: CFDE Gene Set Collections
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://gse.cfde.cloud/downloads/
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
- category: GraphicalInterface
  description: Browser for complete Hetionet v1.0 graph database in Neo4j
  format: http
  id: hetionet.neo4j
  name: Hetionet v1.0 Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://neo4j.het.io/browser/
- category: GraphProduct
  description: Hetionet v1.0 in JSON format
  format: json
  id: hetionet.data.json
  name: Hetionet v1.0 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/json/hetionet-v1.0.json.bz2
- category: GraphProduct
  description: Hetionet v1.0 as a Neo4j database
  id: hetionet.data.neo4j
  name: Hetionet v1.0 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 132
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/neo4j/hetionet-v1.0.db.tar.bz2
- category: GraphProduct
  description: Hetionet v1.0 as SIF edges
  format: sif
  id: hetionet.data.edges
  name: Hetionet v1.0 edges (SIF)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-edges.sif.gz
- category: GraphProduct
  description: Hetionet v1.0 as TSV nodes
  format: tsv
  id: hetionet.data.nodes
  name: Hetionet v1.0 nodes (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 427128
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-nodes.tsv
- category: ProcessProduct
  description: Python package for creating, querying, and operating on hetnets (heterogeneous
    networks)
  id: hetnetpy
  name: hetnetpy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://github.com/hetio/hetnetpy
- category: GraphicalInterface
  description: Web application to search and explore connectivity between nodes in
    Hetionet
  format: http
  id: hetionet.search
  name: Hetnet Connectivity Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://het.io/search
- category: GraphicalInterface
  description: Graphical interface for MedKG
  id: medkb.site
  name: MedKG Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: http://pitools.niper.ac.in/medkg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: medkg
- category: GraphProduct
  description: The OREGANO knowledge graph dataset integrating drug, protein, gene,
    and disease information for drug repositioning.
  format: http
  id: oregano.graph
  name: OREGANO Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oregano
  product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cmaup
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: npass
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: bio2rdf
- category: GraphProduct
  compression: gzip
  description: PharMeBINet V2 JSON release published on February 6, 2024.
  format: json
  id: pharmebinet.json
  latest_version: v2
  name: PharMeBINet JSON Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1942958027
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 TSV release published on February 6, 2024.
  format: tsv
  id: pharmebinet.tsv
  latest_version: v2
  name: PharMeBINet TSV Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1922614551
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 GraphML release published on February 6, 2024.
  format: mixed
  id: pharmebinet.graphml
  latest_version: v2
  name: PharMeBINet GraphML Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 2027519087
  product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
  format: neo4j
  id: pharmebinet.neo4j
  latest_version: v2
  name: PharMeBINet Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3847978577
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
  dump_format: neo4j
  format: neo4j
  id: pharmebinet.neo4j.dump
  latest_version: v2
  name: PharMeBINet Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3598325722
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Downloadable GeneMANIA interaction network data organized by release
    and organism, with individual networks, combined default networks, metadata, and
    identifier mapping tables in plain tab-delimited text files
  format: txt
  id: genemania.networks
  latest_version: current
  name: GeneMANIA Interaction Network Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genemania
  product_url: https://genemania.org/data/current/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: hprd
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with Entrez Gene identifiers.
  edge_count: 1125494
  format: tsv
  id: humannet.network
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 12310221
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with gene symbols.
  edge_count: 1125494
  format: tsv
  id: humannet.network.symbol
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File (Gene Symbols)
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 13925784
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.symbol.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: Product
  description: Downloadable gene set files in GMT, XML, and other formats for human
    collections including hallmarks, curated pathways, ontologies, and computational
    signatures; free registration is required for downloads
  format: mixed
  id: msigdb.downloads.human
  name: MSigDB Human Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mirbase
  - relation_type: prov:used
    source: pid
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: wikipathways
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: Product
  description: Downloadable gene set files for mouse collections including mouse-ortholog
    hallmarks, curated pathways, ontologies, and cell type signatures; free registration
    is required for downloads
  format: mixed
  id: msigdb.downloads.mouse
  name: MSigDB Mouse Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mirbase
  - relation_type: prov:used
    source: pid
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: wikipathways
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: Product
  compression: gzip
  description: PC v14 integrated BioPAX Level 3 unified model containing normalized
    pathway data, molecular interactions, cross-database entity mappings, and metadata-derived
    content from 26 datasource rows.
  format: biopax
  id: pathwaycommons.biopax
  name: Integrated BioPAX Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 1700903742
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-biopax.owl.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: zip
  description: BioPAX3 format pathway data downloads organized by plant species
  format: biopax
  id: plant-reactome.biopax
  is_public: true
  name: Plant Reactome BioPAX3 Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: plant-reactome
  product_file_size: 117969665
  product_url: https://plantreactome.gramene.org/download/current/biopax3.zip
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: reactome
- category: Product
  compression: targz
  description: Scalable Vector Graphics (SVG) format pathway diagrams for interactive
    and high-quality pathway visualization
  format: svg
  id: plant-reactome.svg
  name: Plant Reactome SVG Diagrams
  original_source:
  - relation_type: prov:hadPrimarySource
    source: plant-reactome
  product_file_size: 1739267260
  product_url: https://plantreactome.gramene.org/download/current/diagrams.svg.tgz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: reactome
- category: Product
  compression: targz
  description: PNG raster image format pathway diagrams for static pathway visualization
  format: png
  id: plant-reactome.png
  name: Plant Reactome PNG Diagrams
  original_source:
  - relation_type: prov:hadPrimarySource
    source: plant-reactome
  product_file_size: 557312428
  product_url: https://plantreactome.gramene.org/download/current/diagrams.png.tgz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: reactome
- category: MappingProduct
  description: Tab-delimited identifier mapping file linking pathway identifiers with
    associated genes across plant species
  format: tsv
  id: plant-reactome.mappings
  name: Plant Reactome Identifier Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: plant-reactome
  product_file_size: 24388295
  product_url: https://plantreactome.gramene.org/download/current/gene_ids_by_pathway_and_species.tab
  secondary_source:
  - relation_type: prov:used
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: reactome
- category: Product
  compression: 7z
  description: Reactome-derived true-positive and false-positive protein-pair gold
    standard used in ProteomeHD analyses
  format: csv
  id: proteomehd.reactome_tp_fp
  name: ProteomeHD Reactome Gold Standard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  product_file_size: 12444513
  product_url: https://raw.githubusercontent.com/Rappsilber-Laboratory/ProteomeHD/master/Data/Reactome_TP_FP.7z
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: Product
  description: Download directory for Pathway Commons PC v14 integrated pathway and
    molecular interaction datasets, including BioPAX, SIF, GMT, TXT, and JSON-LD products.
  format: mixed
  id: pathwaycommons.downloads
  name: Pathway Commons Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Simple Interaction Format network file representing binary pairwise
    molecular relationships integrated from Pathway Commons upstream datasource rows.
  format: sif
  id: pathwaycommons.sif
  name: SIF Network Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 9810179
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.sif.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Gene Matrix Transposed gene sets for pathway enrichment analysis,
    derived from the integrated Pathway Commons pathway archive.
  id: pathwaycommons.gmt
  name: GMT Gene Set Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 262513
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.gmt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 tab-delimited extended SIF node and edge file using HGNC-oriented
    identifiers for integrated Pathway Commons interactions.
  format: txt
  id: pathwaycommons.txt
  name: Extended SIF TXT Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 115608500
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: GraphProduct
  description: Neo4j construction artifacts for CardioKG, including Cypher scripts
    to create graph nodes and add edges.
  dump_format: neo4j
  format: neo4j
  id: cardiokg.neo4j
  name: CardioKG Neo4j graph construction scripts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cardiokg
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: mondo
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: uniprot
  - relation_type: prov:used
    source: string
  - relation_type: prov:used
    source: opentargets
  product_url: https://github.com/ImperialCollegeLondon/cardioKG/tree/main/Building%20KG
publications:
- doi: doi:10.1093/nar/gkab1028
  id: doi:10.1093/nar/gkab1028
  preferred: true
  title: The Reactome pathway knowledgebase 2022
  year: '2022'
repository: https://github.com/reactome
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
## Overview

Reactome is the world's leading open-source, open access, manually curated and peer-reviewed knowledgebase of human biological pathways. It provides comprehensive, integrated representation of biological processes from molecular details to systems-level phenomena. Developed collaboratively by an international consortium of research institutions and databases, Reactome combines expert curation with data integration tools to create a foundation for computational biology research, systems biology analysis, and understanding human biology and disease.

The Reactome pathway database describes reactions and biological processes in a machine-readable format, integrating knowledge of how genes and their products participate in organized biological processes. This enables comparative genomics, drug target identification, functional genomics analysis, and personalized medicine approaches.

## Scope and Coverage

### Pathway Content

Reactome covers human biological pathways across multiple domains:

- **Signal Transduction**: Growth factors, cytokine signaling, receptor cascades
- **Metabolism**: Metabolic pathways including carbohydrate, lipid, and protein metabolism
- **Immunity**: Innate and adaptive immune responses, complement activation
- **Hemostasis**: Blood coagulation and platelet aggregation cascades
- **DNA Replication and Repair**: DNA synthesis, repair mechanisms, and cell cycle
- **Gene Expression**: Transcription, translation, and post-translational modifications
- **Transport**: Vesicular transport, ion transport, and membrane trafficking
- **Cell-Cell Interaction**: Adhesion, communication, and junction organization
- **Neuronal Systems**: Neurotransmission, synaptic plasticity, neurodegeneration

### Species Coverage

While primarily curated for human pathways:
- **Primary focus**: Homo sapiens (NCBITaxon:9606)
- **Secondary focus**: Mus musculus (house mouse, NCBITaxon:10090)
- **Cross-species mapping**: Ortholog-based projections for other organisms via Ensembl

### Data Scale

- Over 12,000 unique human reactions and pathways
- More than 250,000 individual reaction instances
- Coverage of approximately 10,000+ human genes
- Integration with multiple external databases and ontologies

## Data Organization and Structure

### Pathway Hierarchies

Reactome organizes biological knowledge in hierarchical pathways:

1. **Top-level** pathways representing major biological domains
2. **Intermediate-level** processes showing specific biological outcomes
3. **Reaction-level** detail describing specific molecular interactions

### Reaction Representation

Each reaction captures:
- **Input entities**: Proteins, small molecules, complexes involved
- **Catalysts**: Enzymes or proteins enabling the reaction
- **Output**: Products of the reaction
- **Requirements**: Cofactors, compartments, conditions
- **Regulation**: Positive and negative regulatory mechanisms

### Integration with External Data

Reactome integrates and cross-references:
- **Gene information**: HGNC, Ensembl, NCBI Gene
- **Protein data**: UniProtKB, PDB structures, InterPro
- **Chemical compounds**: ChEBI, PubChem
- **Disease information**: Disease Ontology, Ensembl phenotypes
- **Gene Ontology**: GO terms for functional annotation
- **Literature**: PubMed references for evidence traceability

## Data Access and Products

### Download Formats

Reactome is available in multiple standardized formats:

1. **BioPAX Format**: Standard pathway data exchange format
   - Supports pathway representation and computational analysis
   - Compatible with pathway analysis tools and integrated models

2. **SBML Format**: Systems Biology Markup Language
   - For computational modeling and systems biology applications
   - Includes detailed kinetic and mathematical information

3. **Graph Database (Neo4j)**: Native graph representation
   - Full interactive pathway exploration
   - Supports complex relationship queries and analysis

4. **RDF/OWL Format**: Semantic web representation
   - For knowledge graph integration and reasoning
   - Linked Data principles with dereferenceable URIs

5. **TSV/CSV Data**: Tabular format for spreadsheet analysis
   - Curated protein complex compositions
   - Pathway-gene associations and mappings

6. **JSON**: Modern programmatic data format
   - RESTful API access
   - Suitable for web applications and visualization

### Access Methods

- **Website Interface**: Interactive pathway browser with visual exploration
- **REST API**: Programmatic access with JSON responses
- **Graph Database**: Direct Neo4j graph queries
- **FTP/Download**: Bulk data downloads in various formats
- **SPARQL Endpoint**: Semantic web query language support
- **R/Bioconductor**: ReactomePA and ReactomeDB packages

## Curation and Quality Assurance

### Peer Review and Validation

- **Expert Curation**: Pathways curated by domain specialists
- **Peer Review**: Multiple rounds of review for quality assurance
- **Evidence Tracking**: PubMed references for all assertions
- **Version Control**: Detailed change history and release notes

### Update Frequency

- Regular quarterly releases with new pathway curation
- Continuous updates to human pathway knowledge
- Maintenance of links to external databases
- Sustainability through international consortium support

## Integration and Interoperability

### Standards Compliance

- **W3C Standards**: RDF, OWL, SPARQL compatibility
- **Systems Biology**: SBML and BioPAX compliance
- **Data Formats**: Standard exchange formats (TSV, JSON, XML)
- **Web Standards**: REST API, HTTP, linked data

### Cross-Database Integration

Reactome integrates with:
- **Pathway Databases**: WikiPathways, KEGG, PANTHER
- **Protein Resources**: STRING, UniProt, Ensembl
- **Ontologies**: Gene Ontology, Disease Ontology, ChEBI
- **Knowledge Graphs**: Various biomedical knowledge graphs

### Canonical Pathway Mapping

Reactome provides canonical human pathway representations that serve as:
- Reference pathways for cross-species comparative analysis
- Foundation for personalized pathway analysis
- Basis for pathway-based drug target identification
- Framework for systems biology modeling

## Use Cases and Applications

### Research Applications

- **Drug Discovery**: Identifying therapeutic targets and mechanisms of action
- **Functional Genomics**: Understanding gene function in biological context
- **Systems Biology**: Modeling complex biological networks and feedback loops
- **Precision Medicine**: Patient-specific pathway analysis
- **Biomarker Discovery**: Identifying pathway-based molecular signatures
- **Target Validation**: Understanding pathway context for therapeutic targets

### Clinical Applications

- **Disease Mechanism Analysis**: Understanding molecular basis of diseases
- **Variant Effect Prediction**: Interpreting genetic variants in pathway context
- **Therapy Response Prediction**: Pathway-based prediction of drug response
- **Clinical Trial Design**: Identifying relevant pathway biomarkers

### Data Integration

- **Multi-Omics Analysis**: Contextualizing omics data in pathways
- **Expression Analysis**: Understanding expression changes within pathway context
- **Mutation Analysis**: Interpreting genetic alterations in pathway networks
- **Knowledge Synthesis**: Aggregating pathway knowledge across studies

### Computational Biology

- **Pathway Analysis**: Over-representation and enrichment analysis
- **Network Analysis**: Graph-based pathway analysis and visualization
- **Systems Modeling**: Construction of computational biological models
- **Knowledge Curation**: Structured pathway representation for AI/ML

## Leadership and Community

### Reactome Consortium

International collaboration between:
- **New York University School of Medicine**: Lead institution
- **European Bioinformatics Institute (EMBL-EBI)**: Co-lead
- **Ontario Institute for Cancer Research**: Contributing institution
- **University of Toronto**: Contributing institution

### Scientific Steering Committee

Oversees strategic direction and quality standards for the resource.

### Community Contributions

- Open community curation model
- Expert review process
- Integration of externally-curated pathway data
- Collaborative enhancement of pathway coverage

## Citation and Usage

All Reactome data is freely available under Creative Commons Attribution 4.0 (CC BY 4.0) license.

### Recommended Citations

For Reactome knowledgebase use:
"Gillespie ME, et al. The Reactome pathway knowledgebase 2022. Nucleic Acids Research. 2022;50(D1):D687-D692. https://doi.org/10.1093/nar/gkab1028"

For specific pathway data:
"Reactome: A Knowledgebase of Biological Pathways. Available at: https://reactome.org"

### Key Resources

- **Website**: https://reactome.org/
- **Pathway Browser**: https://reactome.org/PathwayBrowser/
- **REST API**: https://reactome.org/ContentService/
- **FTP Server**: https://reactome.org/download/
- **GitHub Repository**: https://github.com/reactome
- **Citation Instructions**: https://reactome.org/about/cite

## Standards and Compliance

- **Peer-Reviewed**: Published in Nucleic Acids Research annually
- **Open Access**: CC BY 4.0 licensing with no access restrictions
- **Version Control**: Detailed release notes and change tracking
- **Quality Standards**: Expert curation with evidence documentation
- **FAIR Principles**: Designed for Findability, Accessibility, Interoperability, Reusability
- **Sustainability**: International consortium with stable funding

## Additional Notes

This registry includes alternative translations of Reactome data:

- Direct representations from BioPAX format
- Biopragmatics conversion and mappings
- Multiple graph database distributions
- Integrations with knowledge graph frameworks

For more information on Reactome's sister resources and related projects, see also the related entries in this registry.