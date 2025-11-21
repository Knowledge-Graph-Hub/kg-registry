---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: interpro-help@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/interpro/contact/
  label: InterPro
description: InterPro is a database of protein families, domains and functional sites
  in which identifiable features found in known proteins can be applied to unknown
  protein sequences.
domains:
- biological systems
- proteomics
- genomics
- drug discovery
homepage_url: https://www.ebi.ac.uk/interpro/
id: interpro
infores_id: interpro
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: InterPro
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching the InterPro database
  format: http
  id: interpro.web
  name: InterPro Web Interface
  original_source:
  - interpro
  product_url: https://www.ebi.ac.uk/interpro/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/interpro/api/
  description: RESTful API for programmatic access to InterPro data
  id: interpro.api
  is_public: true
  name: InterPro API
  original_source:
  - interpro
  product_url: https://www.ebi.ac.uk/interpro/api/
- category: ProcessProduct
  compression: targz
  description: Software package for scanning protein sequences against InterPro's
    signatures
  format: java
  id: interpro.interproscan
  name: InterProScan
  original_source:
  - interpro
  product_file_size: 7153864107
  product_url: http://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/5.74-105.0/interproscan-5.74-105.0-64-bit.tar.gz
- category: DataModelProduct
  description: Complete list of InterPro entries with their types and short names
  format: tsv
  id: interpro.entry_list
  name: InterPro Entry List
  original_source:
  - interpro
  product_file_size: 2670480
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/entry.list
- category: DataModelProduct
  compression: gzip
  description: Complete InterPro database in XML format containing entries, member
    database signatures, GO terms, and relationships
  format: xml
  id: interpro.xml
  name: InterPro XML
  original_source:
  - interpro
  product_file_size: 40445027
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro.xml.gz
- category: MappingProduct
  compression: gzip
  description: Complete set of matches between protein sequences and InterPro entries/signatures
  format: xml
  id: interpro.match_complete
  name: InterPro Match Complete
  original_source:
  - interpro
  product_file_size: 89253159090
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/match_complete.xml.gz
- category: MappingProduct
  compression: targz
  description: InterPro matches for UniParc protein sequences
  format: xml
  id: interpro.uniparc_match
  name: UniParc Match
  original_source:
  - interpro
  product_file_size: 331243597405
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/uniparc_match.tar.gz
- category: MappingProduct
  compression: gzip
  description: Mappings of protein sequences to InterPro entries in a tab-delimited
    format
  format: tsv
  id: interpro.protein2ipr
  name: Protein to InterPro Mappings
  original_source:
  - interpro
  product_file_size: 20975973462
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/protein2ipr.dat.gz
- category: DataModelProduct
  description: Hierarchical relationships between InterPro entries
  format: tsv
  id: interpro.parent_child_tree
  name: Parent-Child Tree
  original_source:
  - interpro
  product_file_size: 627613
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/ParentChildTreeFile.txt
- category: MappingProduct
  description: Mappings between InterPro entries and Gene Ontology (GO) terms
  format: tsv
  id: interpro.interpro2go
  name: InterPro to GO Mappings
  original_source:
  - go
  - interpro
  product_file_size: 3088718
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro2go
  secondary_source:
  - interpro
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - pubmed
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
  - pharmacodb
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
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - doid
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
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
  - go
  - cl
  - mesh
  - chebi
  - drugbank
  - interpro
  - uberon
  - pr
  - ncbitaxon
  - reactome
  - hp
  - uniprot
  product_url: https://doi.org/10.5281/zenodo.8139357
  repository: https://github.com/SuLab/DrugMechDB
  versions:
  - 2.0.1
  - 2.0.0
  - 1.0.2
  - '1.0'
- category: Product
  description: interpro OBO
  format: obo
  id: obo-db-ingest.interpro.obo
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: interpro OBO
  original_source:
  - interpro
  product_file_size: 1166198
  product_url: https://w3id.org/biopragmatics/resources/interpro/interpro.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: interpro OWL
  format: owl
  id: obo-db-ingest.interpro.owl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: interpro OWL
  original_source:
  - interpro
  product_file_size: 1347709
  product_url: https://w3id.org/biopragmatics/resources/interpro/interpro.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: interpro OBO Graph JSON
  format: json
  id: obo-db-ingest.interpro.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: interpro OBO Graph JSON
  original_source:
  - interpro
  product_file_size: 1116474
  product_url: https://w3id.org/biopragmatics/resources/interpro/interpro.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: Files containing transitive assignments of InterPro matches, UniProtKB
    keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected
    GO terms
  format: txt
  id: goa.mapping-files
  name: GO Mapping Files
  original_source:
  - interpro
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'
  - 'File was not able to be retrieved when checked on 2025-11-21: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'''
- category: GraphicalInterface
  description: Interactive web interface for exploring and visualizing kinase-substrate
    interactions
  format: http
  id: kinace.portal
  name: KinAce Web Portal
  original_source:
  - phosphositeplus
  - iptmnet
  - uniprot
  - epsd
  - kinhub
  - coralkinome
  - darkkinasekb
  - hgnc
  - kegg
  - interpro
  product_url: https://kinace.kinametrix.com/
  secondary_source:
  - kinace
publications:
- authors:
  - Blum M
  - Andreeva A
  - Florentino LC
  - Chuguransky SR
  - Grego T
  - Hobbs E
  - Pinto BL
  - Orr A
  - Paysan-Lafosse T
  - Ponamareva I
  - Salazar GA
  - Bordin N
  - Bork P
  - Bridge A
  - Colwell L
  - Gough J
  - Haft DH
  - Letunic I
  - Llinares-López F
  - Marchler-Bauer A
  - Meng-Papaxanthos L
  - Mi H
  - Natale DA
  - Orengo CA
  - Pandurangan AP
  - Piovesan D
  - Rivoire C
  - Sigrist CJA
  - Thanki N
  - Thibaud-Nissen F
  - Thomas PD
  - Tosatto SCE
  - Wu CH
  - Bateman A
  doi: doi:10.1093/nar/gkae1082
  id: doi:10.1093/nar/gkae1082
  preferred: true
  title: 'InterPro: the protein sequence classification resource in 2025'
  year: '2024'
repository: https://www.ebi.ac.uk/interpro/
---
InterPro is a database of protein families, domains and functional sites in which identifiable features found in known proteins can be applied to unknown protein sequences.

## Overview

InterPro is a comprehensive database hosted at the European Bioinformatics Institute (EMBL-EBI) that provides functional analysis of proteins by classifying them into families and predicting the presence of domains and important sites. It integrates predictive protein signatures from multiple partner databases into a unified resource.

## Database Components

InterPro integrates signatures from several member databases, including:

- Pfam: Protein families represented by multiple sequence alignments and hidden Markov models
- PROSITE: Patterns and profiles for protein families and domains
- SMART: Identification and annotation of genetically mobile domains
- PRINTS: Fingerprints for protein sequence classification
- PANTHER: Protein families classified by function
- CDD (Conserved Domain Database): Ancient conserved protein domains
- PIRSF: Hierarchical classification of complete proteins
- SUPERFAMILY: Structural and functional annotation based on SCOP superfamilies
- CATH-Gene3D: Protein domain assignments for genomes
- TIGRFAMs: Protein families based on hidden Markov models
- HAMAP: High-quality automated annotations of microbial proteins

## Features and Applications

InterPro provides:

- Comprehensive protein annotation
- Hierarchical classification of proteins
- Functional and structural insights
- GO (Gene Ontology) term mappings
- Pathway associations
- Taxonomic distribution information
- Cross-references to other biological databases

## Tools and Access

The primary tool for using InterPro signatures is InterProScan, which allows users to scan their protein sequences against all InterPro's signatures simultaneously. InterPro data can be accessed via:

- Web interface for interactive browsing and searching
- Programmatic access via REST API
- Downloadable datasets in various formats (OBO, OWL, JSON, XML)
- InterProScan software package for local installation and high-throughput analysis

InterPro is widely used in genome annotation projects, comparative genomics studies, structural biology research, and functional characterization of proteins across all taxonomic groups.