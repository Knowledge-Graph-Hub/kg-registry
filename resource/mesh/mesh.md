---
activity_status: active
category: Ontology
creation_date: '2025-10-10T00:00:00Z'
description: The Medical Subject Headings (MeSH) is a hierarchically-organized controlled
  vocabulary produced by the National Library of Medicine (NLM). It serves as the
  standard thesaurus for indexing and cataloging biomedical and health-related information
  in MEDLINE/PubMed and other NLM databases.
domains:
- biomedical
- health
- literature
homepage_url: https://www.nlm.nih.gov/mesh/meshhome.html
id: mesh
infores_id: mesh
last_modified_date: '2025-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/databases/download/terms_and_conditions_mesh.html
  label: NLM Terms and Conditions for MeSH Data
name: Medical Subject Headings (MeSH)
products:
- category: GraphicalInterface
  description: The official MeSH Browser for searching and browsing the Medical Subject
    Headings vocabulary. Provides hierarchical navigation and term details.
  format: http
  id: mesh.browser
  name: MeSH Browser
  product_url: https://meshb.nlm.nih.gov/search
- category: OntologyProduct
  description: MeSH data in XML format containing descriptors, qualifiers, and supplemental
    concept records. Updated annually with daily updates for SCRs.
  format: xml
  id: mesh.xml
  name: MeSH XML Data
  product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/xmlmesh/
- category: OntologyProduct
  description: MeSH data in RDF (Resource Description Framework) format for semantic
    web applications. Updated daily Monday through Friday.
  format: rdfxml
  id: mesh.rdf
  name: MeSH RDF Data
  product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/rdf/2025/
- category: OntologyProduct
  description: MeSH data in ASCII text format containing descriptors, qualifiers,
    and supplemental concept records. Updated annually with daily SCR updates.
  format: txt
  id: mesh.ascii
  name: MeSH ASCII Data
  product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/asciimesh/
- category: OntologyProduct
  description: MeSH data in MARC 21 bibliographic format for library systems. Posted
    monthly.
  format: mixed
  id: mesh.marc
  name: MeSH MARC 21 Data
  product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/meshmarc/
- category: ProgrammingInterface
  description: E-utilities API for programmatic access to MeSH data through NCBI's
    Entrez system.
  format: http
  id: mesh.api.eutilities
  name: MeSH E-utilities API
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25500/
- category: ProgrammingInterface
  description: SPARQL endpoint and REST API for querying MeSH RDF data with semantic
    web technologies.
  format: http
  id: mesh.api.rdf
  name: MeSH RDF API
  product_url: https://id.nlm.nih.gov/mesh/swagger/ui
- category: GraphicalInterface
  description: SPARQL query editor interface for interactive querying of MeSH data
    using semantic web query language.
  format: http
  id: mesh.sparql.editor
  name: MeSH SPARQL Query Editor
  product_url: https://id.nlm.nih.gov/mesh/query
- category: Product
  description: MeSH on Demand service for suggesting MeSH terms for text or citations.
    Helps identify appropriate subject headings for indexing.
  format: http
  id: mesh.ondemand
  name: MeSH on Demand
  product_url: https://meshb.nlm.nih.gov/MeSHonDemand
- category: DocumentationProduct
  description: Comprehensive documentation about MeSH including tutorials, webinars,
    and user guides for understanding and using the vocabulary.
  format: http
  id: mesh.documentation
  name: MeSH Documentation and Tutorials
  product_url: https://www.nlm.nih.gov/bsd/disted/mesh.html
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
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
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
- category: ProgrammingInterface
  description: TRAPI web API for querying MicrobiomeKG
  format: http
  id: microbiomekg.api
  name: MicrobiomeKG Plover API
  original_source:
  - biolink
  - chebi
  - ncbitaxon
  - ncbigene
  - mesh
  - pubchem
  - go
  - mondo
  - ncit
  - efo
  - uniprot
  - rhea
  - pr
  - uberon
  - panther
  - hgnc
  - drugbank
  - eupathdb
  product_url: https://multiomics.transltr.io/mbkp
  secondary_source:
  - microbiomekg
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
- category: MappingProduct
  description: Concept mappings between different terminology systems
  format: csv
  id: athena.mappings
  name: Athena Concept Mappings
  original_source:
  - snomedct
  - icd10
  - icd10cm
  - mesh
  - loinc
  - cdiscvocab
  - ciel
  product_url: https://athena.ohdsi.org/search-terms/start
  secondary_source:
  - athena
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ Error connecting
    to URL_ Exceeded 30 redirects.
  - File was not able to be retrieved when checked on 2025-12-08_ Error connecting
    to URL_ Exceeded 30 redirects.
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete
    FORUM data
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
  original_source:
  - mesh
  - chebi
  - cito
  - fabio
  - dc
  - cheminf
  - skos
  - chemont
  - pubchem
  - pubmed
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  secondary_source:
  - forum
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ FTP error_ timed
    out
  - File was not able to be retrieved when checked on 2026-02-18_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2026-02-18: FTP error: timed
    out'
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
repository: https://nlmpubs.nlm.nih.gov/projects/mesh/
---
# Medical Subject Headings (MeSH)

The Medical Subject Headings (MeSH) is a hierarchically-organized controlled vocabulary developed and maintained by the National Library of Medicine (NLM). MeSH serves as the authoritative thesaurus for indexing, cataloging, and searching biomedical and health-related information across multiple NLM databases, most notably MEDLINE/PubMed.

## Overview

MeSH provides a consistent way to retrieve information that may use different terminology for the same concepts. It consists of descriptors arranged in a hierarchical structure that permits searching at various levels of specificity. The vocabulary is updated annually, with new descriptors added and existing ones modified to reflect advances in medical knowledge.

## Key Features

- **Hierarchical Structure**: MeSH terms are organized in a tree structure from general to specific, allowing both broad and narrow searches
- **Controlled Vocabulary**: Provides standardized terminology to improve search precision and recall
- **Cross-References**: Includes entry terms and see-also references to guide users to appropriate descriptors
- **Qualifiers**: Subheadings that can be combined with descriptors to specify particular aspects of a topic
- **Supplemental Concept Records (SCRs)**: Additional terms for chemicals, drugs, and other specific entities

## Applications

MeSH is primarily used for:
- Indexing articles in MEDLINE/PubMed and other biomedical databases
- Literature searching and systematic reviews
- Information retrieval in biomedical research
- Cataloging library materials in medical collections
- Supporting semantic web applications through RDF representation

## Data Formats and Access

MeSH data is available in multiple formats to support different use cases:
- **XML**: Structured data format with full hierarchical information
- **RDF**: Semantic web format for linked data applications
- **ASCII**: Plain text format for legacy systems
- **MARC 21**: Library cataloging format

The vocabulary is accessible through various interfaces including the MeSH Browser, programmatic APIs, and downloadable data files. Updates are provided annually for the main vocabulary, with daily updates for supplemental concept records.