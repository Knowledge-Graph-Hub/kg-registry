---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: https://github.com/wikipathways
  - contact_type: url
    value: https://www.wikipathways.org/
  label: WikiPathways Team
- category: Individual
  contact_details:
  - contact_type: email
    value: apico@gladstone.ucsf.edu
  label: Alex Pico
- category: Individual
  contact_details:
  - contact_type: email
    value: martina.kutmon@maastrichtuniversity.nl
  label: Martina Kutmon
description: WikiPathways is an open, collaborative platform dedicated to the curation
  of biological pathways contributed, updated, and used by the research community.
domains:
- pathways
- genomics
- biomedical
homepage_url: https://www.wikipathways.org/
id: wikipathways
layout: resource_detail
license:
  id: https://creativecommons.org/share-your-work/public-domain/cc0/
  label: CC0 (Creative Commons Zero)
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: WikiPathways
products:
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
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
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
- category: Product
  description: Pathways in Graphical Pathway Markup Language (GPML) format, which
    is a custom XML format for biological pathways
  format: xml
  id: wikipathways.gpml
  name: WikiPathways GPML
  product_url: https://data.wikipathways.org/current/gpml/
- category: Product
  description: Pathways in Gene Matrix Transposed (GMT) format for Gene Set Enrichment
    Analysis
  format: tsv
  id: wikipathways.gmt
  name: WikiPathways GMT
  product_url: https://data.wikipathways.org/current/gmt/
- category: Product
  description: Pathways in RDF (Resource Description Framework) format
  format: ttl
  id: wikipathways.rdf
  name: WikiPathways RDF
  product_url: http://data.wikipathways.org/current/rdf/
- category: ProgrammingInterface
  description: SPARQL endpoint for querying WikiPathways content
  id: wikipathways.sparql
  name: WikiPathways SPARQL Endpoint
  product_url: https://sparql.wikipathways.org/
- category: ProgrammingInterface
  description: Web service API for programmatic access to WikiPathways content
  id: wikipathways.api
  name: WikiPathways API
  product_url: https://webservice.wikipathways.org/ui/
- category: GraphicalInterface
  description: The main web interface for browsing, viewing, and downloading pathways
  id: wikipathways.web
  name: WikiPathways Web Interface
  product_url: https://www.wikipathways.org/
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
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
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
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
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  secondary_source:
  - rna-kg
- category: Product
  description: Pathway information integrated from Reactome, WikiPathways and other
    pathway databases
  format: http
  id: genecards.pathway.data
  name: GeneCards Pathway Data
  original_source:
  - reactome
  - wikipathways
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-27_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-21_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-27: HTTP 403 error
    when accessing file'
publications:
- authors:
  - Agrawal A
  - et al.
  doi: doi:10.1093/nar/gkad960
  id: https://doi.org/10.1093/nar/gkad960
  journal: Nucleic Acids Research
  preferred: true
  title: WikiPathways 2024 - next generation pathway database
  year: '2024'
- authors:
  - Martens M
  - et al.
  doi: doi:10.1093/NAR/gkaa1024
  id: https://doi.org/10.1093/NAR/gkaa1024
  journal: Nucleic Acids Research
  title: WikiPathways - connecting communities
  year: '2021'
repository: https://github.com/wikipathways/wikipathways-database
---
# WikiPathways

WikiPathways is an open, collaborative platform dedicated to the curation of biological pathways. It was established to facilitate the contribution and maintenance of pathway information by the biology community. The platform provides intuitive views of the myriad interactions underlying biological processes using a familiar web-based format that reduces barriers to participation in pathway modeling.

## Features

- Community-curated biological pathway database
- Open science platform with CC0 licensing
- Multiple data formats: GPML (XML), GMT, RDF, SVG, PNG
- Programmatic access via API, SPARQL endpoint, R and Python packages
- Integration with pathway analysis tools like PathVisio and Cytoscape

## Access and Usage

Each pathway at WikiPathways has a dedicated page displaying the current diagram, description, authors, references, citations, annotations, download options, and component gene and protein lists. Pathways can be edited using the WikiPathways plugin for PathVisio.

The pathway content is freely available for download in various data and image formats, including:
- GPML: A custom XML format compatible with pathway visualization and analysis tools
- GMT: Gene Matrix Transposed format for Gene Set Enrichment Analysis
- RDF: Resource Description Framework for semantic web applications
- SVG and PNG: For visualization and publication

## Programmatic Access

- **rWikiPathways**: R package for programmatic access
- **pywikipathways**: Python package for the WikiPathways API
- **SPARQL endpoint**: For querying the WikiPathways RDF data
- **Web service API**: RESTful API for accessing WikiPathways data

## Citations

WikiPathways recommends citing their latest database article:
- Agrawal A, et al. (2024) WikiPathways 2024: next generation pathway database. NAR. https://doi.org/10.1093/nar/gkad960