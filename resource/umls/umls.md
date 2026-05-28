---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/research/umls/support.html
  id: ncbi
  label: NLM UMLS Customer Support
creation_date: '2025-10-30T00:00:00Z'
description: The Unified Medical Language System (UMLS) integrates and distributes
  over 200 biomedical vocabularies, terminologies, and classification standards to
  enable interoperability between information systems. It includes the Metathesaurus
  (terms and codes from vocabularies like CPT, ICD-10-CM, LOINC, MeSH, RxNorm, SNOMED
  CT), Semantic Network (broad categories and relationships), and SPECIALIST Lexicon
  (biomedical and general English lexicon with normalization tools).
domains:
- biomedical
- clinical
- literature
homepage_url: https://www.nlm.nih.gov/research/umls/index.html
id: umls
infores_id: umls
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://uts.nlm.nih.gov/uts/
  label: UMLS License (free for individuals)
name: Unified Medical Language System
products:
- category: GraphicalInterface
  description: Web interface for browsing UMLS Metathesaurus concepts, CUIs, semantic
    types, and synonymous terms
  format: http
  id: umls.browser
  name: UMLS Metathesaurus Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://uts.nlm.nih.gov/uts/umls/home
- category: GraphicalInterface
  description: Web interface for viewing semantic types, definitions, and hierarchical
    structure of the UMLS Semantic Network
  format: http
  id: umls.semantic_network_browser
  name: UMLS Semantic Network Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://uts.nlm.nih.gov/uts/umls/semantic-network/root
- category: ProgrammingInterface
  description: REST API providing programmatic access to UMLS Metathesaurus, Semantic
    Network, and related terminology services
  id: umls.api
  is_public: true
  name: UMLS Terminology Services API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://documentation.uts.nlm.nih.gov/rest/home.html
- category: Product
  description: Full UMLS Knowledge Sources release including Metathesaurus, Semantic
    Network, and SPECIALIST Lexicon for local installation with MetamorphoSys customization
    tool
  id: umls.release
  name: UMLS Knowledge Sources Release Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html
- category: ProcessProduct
  description: MetamorphoSys tool for customizing UMLS subsets by vocabulary, language,
    or semantic type and loading data into local databases
  id: umls.metamorphosys
  name: MetamorphoSys Customization Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://www.nlm.nih.gov/research/umls/implementation_resources/metamorphosys/help.html
- category: ProcessProduct
  description: SPECIALIST Lexicon and Lexical Tools for normalizing strings, generating
    lexical variants, and creating indexes for biomedical text processing
  id: umls.specialist_lexicon
  name: SPECIALIST Lexicon and Lexical Tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://lhncbc.nlm.nih.gov/LSG/index.html
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
- category: Product
  description: VANDF drug terminology data distributed through UMLS Metathesaurus
  id: ndfrt.umls
  name: VANDF in UMLS
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndfrt
  product_url: https://www.nlm.nih.gov/research/umls/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: umls
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
  compression: gzip
  description: Rich Release Format (RRF) file containing concept names and source
    identifiers with gzip compression
  format: txt
  id: medgen.mgconso
  name: MGCONSO (Concept Names)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 15843494
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGCONSO.RRF.gz
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing definitions and descriptions
    with gzip compression
  format: txt
  id: medgen.mgdef
  name: MGDEF (Definitions)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 5062289
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGDEF.RRF.gz
- category: MappingProduct
  compression: gzip
  description: Rich Release Format (RRF) file containing relationships between concepts
    with gzip compression
  format: txt
  id: medgen.mgrel
  name: MGREL (Relationships)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 15661303
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGREL.RRF.gz
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing attributes and properties
    with gzip compression
  format: txt
  id: medgen.mgsat
  name: MGSAT (Attributes)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 11710268
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSAT.RRF.gz
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing semantic type assignments
    with gzip compression
  format: txt
  id: medgen.mgsty
  name: MGSTY (Semantic Types)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 1644564
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSTY.RRF.gz
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing concept names for search
    with gzip compression
  format: txt
  id: medgen.names
  name: NAMES
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 3097271
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/NAMES.RRF.gz
- category: Product
  compression: gzip
  description: Merged CUI mappings showing concept consolidations with gzip compression
  format: txt
  id: medgen.merged
  name: MERGED (Merged CUIs)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 47602
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MERGED.RRF.gz
- category: GraphicalInterface
  description: Interactive web interface for browsing and querying Data Distillery
    Knowledge Graph resources.
  format: http
  id: cfde-ddkg.portal
  name: DDKG Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-ddkg
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://dd-kg-ui.cfde.cloud/
- category: Product
  description: JSON manifest listing downloadable DDKG resources and files.
  format: json
  id: cfde-ddkg.downloads
  name: DDKG Downloads Manifest
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-ddkg
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  product_file_size: 5216
  product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/minio/downloads.json
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
- category: GraphProduct
  description: Training data for the MIND knowledge graph containing 9,651,040 edges
  format: tsv
  id: mind.train
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Training Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_url: https://zenodo.org/records/8117748/files/train.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-18_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-05-28: No Content-Length
    header found'
- category: GraphProduct
  description: Test data for the MIND knowledge graph containing DrugCentral indications
  format: tsv
  id: mind.test
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Test Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_url: https://zenodo.org/records/8117748/files/test.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-18_ HTTP 429 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-05-28: No Content-Length
    header found'
- category: GraphProduct
  description: Validation data for the MIND knowledge graph containing DrugCentral
    indications
  format: tsv
  id: mind.valid
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Validation Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_url: https://zenodo.org/records/8117748/files/valid.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-30_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-05-28: No Content-Length
    header found'
- category: Product
  description: Dictionary of entities in the MIND knowledge graph
  format: tsv
  id: mind.entities
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Entities Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_file_size: 5629618
  product_url: https://zenodo.org/records/8117748/files/entities.dict
- category: Product
  description: Dictionary of relations in the MIND knowledge graph
  format: tsv
  id: mind.relations
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Relations Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_file_size: 1648
  product_url: https://zenodo.org/records/8117748/files/relations.dict
- category: GraphProduct
  description: A comprehensive multi-omics biomedical knowledge graph connecting genomic,
    transcriptomic, proteomic, and clinical data. Contains over 32 million nodes and
    118 million relationships.
  dump_format: neo4j
  edge_count: 118000000
  id: petagraph.graph
  name: Petagraph Knowledge Graph (Neo4J)
  node_count: 32000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: petagraph
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: lincs
  product_url: https://ubkg-downloads.xconsortia.org/
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for RDKG
  format: http
  id: rdkg.tpf
  name: RDKG TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://apps.okn.us/ldf/rdkg
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
- category: GraphProduct
  description: Weighted heterogeneous knowledge graph extracted from MEDLINE corpus
    containing 1,179 tumors, 2,550 biomarkers, 1,806 drugs, and 756 ADRs with 139,254
    relationship edges (Tumor-Biomarker, Tumor-Drug, Tumor-ADR, Drug-Biomarker, Drug-ADR,
    Biomarker-ADR). Includes correlation weights calculated using naive Bayesian model.
  id: tbkg.data
  name: TBKG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tbkg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
- category: Product
  description: Clinical validation dataset with calculated ADRs for osimertinib ranked
    by importance, biomarker pathways explaining drug-ADR relationships, and clinical
    data from 8 lung adenocarcinoma patients. Model achieved Kappa=0.68 concordance
    with official manual and 0.81 three-fold cross-validation accuracy.
  id: tbkg.osimertinib_case_study
  name: TBKG Osimertinib ADR Case Study Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tbkg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
- category: ProgrammingInterface
  description: REST API with endpoints that abstract common types of queries against
    a UBKG neo4j knowledge graph database. Requires UMLS API key to access.
  id: ubkg.api
  is_public: false
  name: UBKG API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://smart-api.info/ui/96e5b5c0b0efeef5b93ea98ac2794837
- category: GraphicalInterface
  description: Guesdt (Graphing UMLS Enables Search In Dynamic Trees) application
    used to represent the UBKG in a tree view.
  id: ubkg.guesdt
  name: UBKG Guesdt Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://x-atlas-consortia.github.io/Guesdt/
publications:
- id: PMID:14681409
  preferred: true
  title: 'The Unified Medical Language System (UMLS): integrating biomedical terminology.'
synonyms:
- UMLS
taxon:
- NCBITaxon:9606
---
# Unified Medical Language System (UMLS)

## Overview

The Unified Medical Language System (UMLS) is a comprehensive set of files and software developed by the U.S. National Library of Medicine (NLM) that brings together over 200 health and biomedical vocabularies and standards to facilitate interoperability between computer systems. The UMLS enables linking of different medical terminologies and codes used by physicians, pharmacies, insurance companies, hospitals, and research institutions.

## Three Knowledge Sources

### 1. Metathesaurus
The Metathesaurus is the largest component, containing:
- Terms and codes from many vocabularies including:
  - CPT (Current Procedural Terminology)
  - ICD-10-CM (International Classification of Diseases)
  - LOINC (Logical Observation Identifiers Names and Codes)
  - MeSH (Medical Subject Headings)
  - RxNorm (normalized drug names)
  - SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms)
- Hierarchical relationships
- Definitions and other attributes
- Concept Unique Identifiers (CUIs) linking synonymous terms across vocabularies

### 2. Semantic Network
Provides a consistent categorization of all concepts represented in the Metathesaurus through:
- 133 broad categories (semantic types) such as "Disease or Syndrome," "Pharmacologic Substance"
- 54 relationships (semantic relations) defining interactions between semantic types

### 3. SPECIALIST Lexicon and Lexical Tools
- Large syntactic lexicon covering biomedical and general English
- Tools for normalizing strings, generating lexical variants, and creating indexes
- Supports natural language processing of biomedical text

## Use Cases

The UMLS can be used to:
- Link terminology between healthcare providers, pharmacies, and insurance companies
- Coordinate patient care across hospital departments
- Process clinical texts to extract concepts and relationships
- Map between different terminologies
- Develop information retrieval systems
- Extract custom terminologies from the Metathesaurus
- Build and maintain local terminology services
- Research terminologies and ontologies

## Access Methods

### Web Browsers
- Metathesaurus Browser for searching concepts and relationships
- Semantic Network Browser for exploring semantic types and relations

### Local Installation
- Download full UMLS release files
- Customize using MetamorphoSys tool
- Load into local database systems (MySQL, Oracle, etc.)

### Programmatic Access
- REST API for querying UMLS data within applications
- Comprehensive API documentation available

## Licensing

- Free licensing for individuals (not groups or organizations)
- UMLS Terminology Services (UTS) account required
- No charge for SNOMED CT use in United States and member countries
- Some vocabularies may require additional agreements with vendors

## Maintained By

National Library of Medicine, National Institutes of Health, U.S. Department of Health and Human Services