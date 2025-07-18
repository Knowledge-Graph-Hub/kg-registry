---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://string-db.org/
  label: STRING Consortium
description: STRING is a database of known and predicted protein-protein interactions.
  The interactions include direct (physical) and indirect (functional) associations
  derived from computational prediction, knowledge transfer between organisms, and
  interactions aggregated from other primary databases.
domains:
- genomics
- biomedical
- proteomics
homepage_url: https://string-db.org/
id: string
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International (CC BY 4.0)
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: STRING
products:
- category: GraphProduct
  compression: gzip
  description: Complete protein-protein interaction network data with confidence scores
  format: tsv
  id: string.protein.links
  name: STRING Protein Links
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: Detailed protein network data including subscores per evidence channel
  format: tsv
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: Complete database dump containing all network nodes, edges, and scores
  id: string.database
  name: STRING Database Dump
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
- category: ProgrammingInterface
  description: RESTful API for programmatic access to STRING data
  id: string.api
  name: STRING REST API
  product_url: https://string-db.org/cgi/help?subpage=api
- category: GraphicalInterface
  description: Web interface for searching, visualizing, and analyzing protein-protein
    interaction networks
  id: string.web
  name: STRING Web Interface
  product_url: https://string-db.org/
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
  - do
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
  - cmap
  - hp
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
  - nposckan
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
  - do
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
  - cmap
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
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
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
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmdb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- authors:
  - Szklarczyk D
  - Kirsch R
  - Koutrouli M
  - Nastou K
  - Mehryary F
  - Hachilif R
  - Annika GL
  - Fang T
  - Doncheva NT
  - Pyysalo S
  - Bork P
  - Jensen LJ
  - von Mering C
  doi: doi:10.1093/nar/gkac1000
  id: https://doi.org/10.1093/nar/gkac1000
  journal: Nucleic Acids Research
  preferred: true
  title: The STRING database in 2023 - protein-protein association networks and functional
    enrichment analyses for any sequenced genome of interest
  year: '2023'
version: '12.0'
---
# STRING - Protein-Protein Interaction Networks

STRING (Search Tool for the Retrieval of Interacting Genes/Proteins) is a database of known and predicted protein-protein interactions. The database contains information from numerous sources, including experimental repositories, computational prediction methods, and public text collections.

## Overview

The STRING database currently covers:
- 59,309,604 proteins from 12,535 organisms
- Over 20 billion interactions
- Confidence scores for all protein interactions

## Data Sources

STRING integrates and scores interactions from five main sources:
1. **Genomic Context Predictions**: Interactions predicted from genome analysis
2. **High-throughput Lab Experiments**: Experimentally determined interactions
3. **(Conserved) Co-Expression**: Proteins that show similar expression patterns
4. **Automated Textmining**: Interactions extracted from scientific literature
5. **Previous Knowledge in Databases**: Curated interactions from existing databases

## Access and Usage

STRING data is available through multiple formats:
- Web interface for interactive visualization and analysis
- Downloadable datasets in various formats (TSV, SQL dumps)
- REST API for programmatic access
- Cytoscape plugin for network analysis

All data in STRING is freely available under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Citations

When using STRING, please cite:
- Szklarczyk D, et al. (2023) The STRING database in 2023 - protein-protein association networks and functional enrichment analyses for any sequenced genome of interest. Nucleic Acids Res. 51(D1):D638-646.