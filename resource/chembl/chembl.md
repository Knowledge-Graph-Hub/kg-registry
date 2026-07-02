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
creation_date: '2025-03-09T00:00:00Z'
description: ChEMBL is a manually curated database of bioactive molecules with drug-like
  properties. It brings together chemical, bioactivity and genomic data to aid the
  translation of genomic information into effective new drugs.
domains:
- chemistry and biochemistry
homepage_url: https://www.ebi.ac.uk/chembl/
id: chembl
infores_id: chembl
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/3.0/
  label: CC-BY-SA-3.0
name: ChEMBL
products:
- category: GraphicalInterface
  description: Web interface for searching and exploring ChEMBL data
  format: http
  id: chembl.site
  is_public: true
  name: ChEMBL Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://www.ebi.ac.uk/chembl/
- category: ProgrammingInterface
  description: RESTful API for accessing ChEMBL data programmatically
  format: http
  id: chembl.api
  is_public: true
  name: ChEMBL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://www.ebi.ac.uk/chembl/api/data/docs
- category: Product
  compression: gzip
  description: PostgreSQL database dump of the complete ChEMBL database
  format: postgres
  id: chembl.postgres
  name: ChEMBL PostgreSQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
- category: Product
  compression: gzip
  description: MySQL database dump of the complete ChEMBL database
  format: mysql
  id: chembl.mysql
  name: ChEMBL MySQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
- category: Product
  compression: gzip
  description: SQLite database file containing the complete ChEMBL database
  format: sqlite
  id: chembl.sqlite
  name: ChEMBL SQLite
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
- category: Product
  compression: gzip
  description: Structure data files for all chemical compounds in ChEMBL
  format: sdf
  id: chembl.sdf
  name: ChEMBL SDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
- category: Product
  compression: gzip
  description: RDF version of the ChEMBL database
  format: ttl
  id: chembl.rdf
  name: ChEMBL RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBL-RDF/latest/
- category: Product
  compression: gzip
  description: RDF (Turtle) download of the ChEMBL data via the EBI ChEMBL-RDF FTP
    archive. The former EBI RDF Platform SPARQL endpoint has been retired, so ChEMBL
    RDF is now distributed as downloadable Turtle dumps.
  format: ttl
  id: chembl.sparql
  is_public: true
  name: ChEMBL RDF Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBL-RDF/latest/
- category: MappingProduct
  description: Mapping between chembl_35 target chembl_ids and UniProt accessions
  format: txt
  id: chembl.map_to_uniprot
  is_public: true
  name: ChEMBL map to UniProt
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 1012901
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
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
  format: http
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
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: python
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
  description: KGX distribution of the ICEES Exposures KP in Knowledge Graph Exchange
    (KGX) format, containing integrated clinical and environmental exposures data
    as a knowledge graph with 226 nodes and 14,342 edges
  format: kgx-jsonl
  id: icees-kg.graph
  name: KGX distribution of the ICEES Exposures KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/icees-kg/1.5.0/
- category: ProgrammingInterface
  description: Translator Reasoner API (TRAPI) endpoint for querying ICEES KG using
    standardized Translator protocols
  format: http
  id: icees-kg.trapi
  name: ICEES KG TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://robokop.renci.org/api-docs/docs/automat/icees-kg-trapi
- category: Product
  description: Meta knowledge graph and metadata describing the data sources, node
    types, edge types, and predicates available in ICEES KG
  format: json
  id: icees-kg.metadata
  name: ICEES KG Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://robokop.renci.org/api-docs/docs/automat/metadata-metadata-get-icees-kg
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  format: mixed
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
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for ChEMBL distributed via the NCATS Translator
    release site (release 2026_03_06; build chembl_36_76533eea_2025sep1_4.3.6; source
    version 36; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 267871
  format: kgx-jsonl
  id: translator.chembl.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator ChEMBL KGX Graph
  node_count: 153369
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/chembl/latest/
  versions:
  - '2026_03_06'
  - chembl_36_76533eea_2025sep1_4.3.6
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
- category: Product
  description: chembl.compound Nodes TSV
  format: tsv
  id: obo-db-ingest.chembl.compound.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/3.0/
    label: CC-BY-SA-3.0
  name: chembl.compound Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 411222
  product_url: https://w3id.org/biopragmatics/resources/chembl.compound/chembl.compound.tsv
- category: Product
  description: chembl.target Nodes TSV
  format: tsv
  id: obo-db-ingest.chembl.target.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/3.0/
    label: CC-BY-SA-3.0
  name: chembl.target Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 260194
  product_url: https://w3id.org/biopragmatics/resources/chembl.target/chembl.target.tsv
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: Product
  description: MySQL database dump files containing the complete TCRD relational database
    schema and data for local installation and analysis
  format: mysql
  id: tcrd.database_download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://unmtid-dbs.net/download/TCRD/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to TCRD data through Pharos
    for computational workflows and custom applications
  format: http
  id: tcrd.api
  is_public: true
  name: Pharos API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://pharos.nih.gov/api
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
- category: DocumentationProduct
  description: Comprehensive documentation describing TCRD data sources, schema structure,
    and usage guidelines
  format: http
  id: tcrd.documentation
  name: TCRD Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://unmtid-dbs.net/download/TCRD/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
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
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.1
  compression: gzip
  description: Human-scoped, Neo4j-ready subgraph of the BioBTree knowledge graph,
    exported as a biolink-typed KGX graph (~40M nodes / ~132M edges, ~8.3 GB compressed
    across separate node and edge files). A practical projection of the full graph
    for human-centric biomedical use. Published on Zenodo.
  edge_count: 132075627
  format: kgx
  id: biobtree.graph.human-subgraph
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC-BY-NC-SA-4.0
  name: BioBTree Knowledge Graph - Human Subgraph (KGX)
  node_categories:
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellLine
  - biolink:CellularComponent
  - biolink:CodingSequence
  - biolink:Disease
  - biolink:DiseaseOrPhenotypicFeature
  - biolink:Drug
  - biolink:Exon
  - biolink:Gene
  - biolink:GrossAnatomicalStructure
  - biolink:MacromolecularComplex
  - biolink:MolecularActivity
  - biolink:NoncodingRNAProduct
  - biolink:NucleicAcidSequenceMotif
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:ProteinDomain
  - biolink:ProteinFamily
  - biolink:Publication
  - biolink:RegulatoryRegion
  - biolink:SequenceVariant
  - biolink:SmallMolecule
  - biolink:Transcript
  node_count: 40160474
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
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
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  predicates:
  - biolink:actively_involved_in
  - biolink:affects
  - biolink:associated_with
  - biolink:close_match
  - biolink:derives_from
  - biolink:directly_physically_interacts_with
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:gene_product_of
  - biolink:has_adverse_event
  - biolink:has_gene_product
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:in_clinical_trials_for
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:member_of
  - biolink:mentions
  - biolink:orthologous_to
  - biolink:paralogous_to
  - biolink:participates_in
  - biolink:physically_interacts_with
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:transcribed_from
  - biolink:translates_to
  - biolink:treats_or_applied_or_studied_to_treat
  product_url: https://zenodo.org/records/20816742
- category: GraphProduct
  description: KGX nodes and edges for KG-COVID-19
  format: kgx
  id: kg-covid-19.graph
  name: KG-COVID-19 graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-covid-19
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cord-19
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://kghub.io/kg-covid-19/
  warnings:
  - 'Download offline as of 2026-07-01: the KG-Hub reorganization has taken this file
    offline. The kghub.io and kg-hub.berkeleybop.io hosts return HTTP 404 for all
    kg-covid-19 artifacts (current and dated) and the kg-hub-public-data S3 objects
    return HTTP 403. No replacement public download URL is available.'
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
- category: GraphProduct
  description: Integrated pharmacological knowledge graph (PharmDB-K) of drugs, targets,
    diseases, and associations
  format: http
  id: pharmdb.graph
  name: PharmDB-K Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: dcdb
  - relation_type: prov:hadPrimarySource
    source: gad
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: t3db
  - relation_type: prov:hadPrimarySource
    source: wipo-tkp
- category: GraphProduct
  description: RDF knowledge graph of the Experimental Natural Products Knowledge
    Graph, integrating experimental LC-MS/MS spectra and GNPS-based annotations, ISDB-LOTUS
    structural annotations, taxonomic and bioactivity metadata, cross-linked to Wikidata
    and served from the public GraphDB/SPARQL endpoint.
  format: ttl
  id: kg-enp.graph
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    label: CC0-1.0
  name: ENPKG RDF Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-enp
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: lotus
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://enpkg.commons-lab.org/graphdb
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: open-tree-of-life
  - relation_type: prov:wasInfluencedBy
    source: chembl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 406 error
    when accessing file'
- category: GraphProduct
  description: Integrated rare-disease knowledge graph produced by the RD-Clust workflow,
    connecting rare diseases to genes, phenotypes, Gene Ontology terms, drugs/ligands,
    and pathway interactions. Distributed as the processed disease ontograph within
    the RD-Clust repository.
  format: http
  id: ncatsgardkg.graph
  name: NCATS GARD Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncatsgardkg
  - relation_type: prov:hadPrimarySource
    source: gard
  product_url: https://github.com/ncats/RD-Clust/tree/main/data/processed
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hp
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: mondo
  - relation_type: prov:wasInfluencedBy
    source: orphanet
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: pharos
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: chebi
  - relation_type: prov:wasInfluencedBy
    source: pubchem
  - relation_type: prov:wasInfluencedBy
    source: pathwaycommons
- category: GraphProduct
  description: The SPOKE-OKN knowledge graph, an OKN-hosted RDF publication of the
    SPOKE biomedical and environmental health knowledge graph, served through FRINK
    query services.
  format: ttl
  id: spoke-okn.graph
  name: SPOKE-OKN Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke-okn
  - relation_type: prov:wasDerivedFrom
    source: spoke
  product_url: https://spoke.ucsf.edu
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bgee
  - relation_type: prov:wasInfluencedBy
    source: bindingdb
  - relation_type: prov:wasInfluencedBy
    source: bv-brc
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: civic
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: clinicaltrialsgov
  - relation_type: prov:wasInfluencedBy
    source: diseases
  - relation_type: prov:wasInfluencedBy
    source: doid
  - relation_type: prov:wasInfluencedBy
    source: drugbank
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: foodb
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: gwascatalog
  - relation_type: prov:wasInfluencedBy
    source: hpa
  - relation_type: prov:wasInfluencedBy
    source: interpro
  - relation_type: prov:wasInfluencedBy
    source: kegg
  - relation_type: prov:wasInfluencedBy
    source: lincs-l1000
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: metacyc
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: ncbitaxon
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pathophenodb
  - relation_type: prov:wasInfluencedBy
    source: pfam
  - relation_type: prov:wasInfluencedBy
    source: pid
  - relation_type: prov:wasInfluencedBy
    source: protcid
  - relation_type: prov:wasInfluencedBy
    source: pubmed
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: sider
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
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
  - Kizilören T
  - Gaulton A
  - Bento AP
  - Adasme MF
  - Monecke PM
  - Landrum GA
  - Leach AR
  doi: 10.1093/nar/gkad1004
  id: doi:10.1093/nar/gkad1004
  journal: Nucleic Acids Research
  preferred: true
  title: 'The ChEMBL Database in 2023: a drug discovery platform spanning multiple
    bioactivity data types and time periods'
  year: '2024'
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