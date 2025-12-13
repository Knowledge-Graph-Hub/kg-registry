---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: chembl-help@ebi.ac.uk
  id: ebi
  label: ChEMBL
description: ChEMBL is a manually curated database of bioactive molecules with drug-like
  properties. It brings together chemical, bioactivity and genomic data to aid the
  translation of genomic information into effective new drugs.
domains:
- chemistry and biochemistry
homepage_url: https://www.ebi.ac.uk/chembl/
id: chembl
infores_id: chembl
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/3.0/
  label: CC-BY-SA-3.0
name: ChEMBL
products:
- category: GraphicalInterface
  description: Web interface for searching and exploring ChEMBL data
  id: chembl.site
  is_public: true
  name: ChEMBL Web Interface
  original_source:
  - chembl
  product_url: https://www.ebi.ac.uk/chembl/
  secondary_source:
  - chembl
- category: ProgrammingInterface
  description: RESTful API for accessing ChEMBL data programmatically
  id: chembl.api
  is_public: true
  name: ChEMBL API
  original_source:
  - chembl
  product_url: https://www.ebi.ac.uk/chembl/api/data/docs
  secondary_source:
  - chembl
- category: Product
  compression: gzip
  description: PostgreSQL database dump of the complete ChEMBL database
  format: postgres
  id: chembl.postgres
  name: ChEMBL PostgreSQL
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  compression: gzip
  description: MySQL database dump of the complete ChEMBL database
  format: mysql
  id: chembl.mysql
  name: ChEMBL MySQL
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  compression: gzip
  description: SQLite database file containing the complete ChEMBL database
  format: sqlite
  id: chembl.sqlite
  name: ChEMBL SQLite
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  compression: gzip
  description: Structure data files for all chemical compounds in ChEMBL
  format: sdf
  id: chembl.sdf
  name: ChEMBL SDF
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  compression: gzip
  description: RDF version of the ChEMBL database
  format: ttl
  id: chembl.rdf
  name: ChEMBL RDF
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBL-RDF/latest/
  secondary_source:
  - chembl
- category: ProgrammingInterface
  description: SPARQL endpoint for the ChEMBL RDF data
  id: chembl.sparql
  is_public: true
  name: ChEMBL SPARQL
  original_source:
  - chembl
  product_url: https://www.ebi.ac.uk/rdf/services/sparql
  secondary_source:
  - chembl
- category: MappingProduct
  description: Mapping between chembl_35 target chembl_ids and UniProt accessions
  id: chembl.map_to_uniprot
  is_public: true
  name: ChEMBL map to UniProt
  original_source:
  - chembl
  - uniprot
  product_file_size: 1012901
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
  secondary_source:
  - chembl
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
  - semmeddb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2
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
  - semmeddb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2
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
  - semmeddb
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2
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
  description: KGX distribution of the ICEES Exposures KP in Knowledge Graph Exchange
    (KGX) format, containing integrated clinical and environmental exposures data
    as a knowledge graph with 226 nodes and 14,342 edges
  format: kgx-jsonl
  id: icees-kg.graph
  name: KGX distribution of the ICEES Exposures KP
  original_source:
  - mesh
  - pubchem
  - chembl
  - mondo
  - chebi
  - hp
  - umls
  - hmdb
  - icees-kg
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/icees-kg/1.5.0/
  secondary_source:
  - icees-kg
- category: ProgrammingInterface
  description: Translator Reasoner API (TRAPI) endpoint for querying ICEES KG using
    standardized Translator protocols
  format: http
  id: icees-kg.trapi
  name: ICEES KG TRAPI API
  original_source:
  - mesh
  - pubchem
  - chembl
  - mondo
  - chebi
  - hp
  - umls
  - hmdb
  - icees-kg
  product_url: https://robokop.renci.org/api-docs/docs/automat/icees-kg-trapi
  secondary_source:
  - icees-kg
- category: Product
  description: Meta knowledge graph and metadata describing the data sources, node
    types, edge types, and predicates available in ICEES KG
  format: json
  id: icees-kg.metadata
  name: ICEES KG Metadata
  original_source:
  - mesh
  - pubchem
  - chembl
  - mondo
  - chebi
  - hp
  - umls
  - hmdb
  - icees-kg
  product_url: https://robokop.renci.org/api-docs/docs/automat/metadata-metadata-get-icees-kg
  secondary_source:
  - icees-kg
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - drkg
  - idisk
  - brenda
  - ctd
  - drugbank
  - kegg
  - pharmgkb
  - reactome
  - sider
  - tissues
  - bgee
  - doid
  - uberon
  - cl
  - hgnc
  - chembl
  - chebi
publications:
- authors:
  - Zdrazil B
  - Felix E
  - Hunter F
  - Manners EJM
  - Blackshaw J
  - Corbett S
  - de Veij M
  - Ioannidis H
  - Mendez Lopez DM
  - Mosquera JF
  - Magarinos MP
  - Bosc N
  - Arcila R
  - "Kizil\xF6ren T"
  - Gaulton A
  - Bento AP
  - Adasme MF
  - Monecke PM
  - Landrum GA
  - Leach AR
  doi: doi:10.1093/nar/gkad1004
  id: doi:10.1093/nar/gkad1004
  preferred: true
  title: 'The ChEMBL Database in 2023: a drug discovery platform spanning multiple
    bioactivity data types and time periods'
  year: '2023'
repository: https://github.com/chembl
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---

ChEMBL is a manually curated database of bioactive molecules with drug-like properties. It brings together chemical, bioactivity and genomic data to aid the translation of genomic information into effective new drugs.

The database contains detailed information on:
- Over 2 million compounds
- More than 1 million assays
- Binding, functional, and ADMET data
- Over 15,000 targets, including proteins, cells, and organisms
- Around 90,000 publications and documents

ChEMBL is widely used in drug discovery, pharmacology research, chemical biology, and medicinal chemistry. The database undergoes regular updates, with new data releases typically occurring 3-4 times per year.