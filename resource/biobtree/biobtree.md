---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: tamerh
    label: Tamer Gur
creation_date: '2026-06-15T00:00:00Z'
description: BioBTree is a unified biomedical knowledge graph that integrates more than 70 primary data sources, including Ensembl, UniProt, PDB, ChEMBL, Reactome, and ClinVar, into a single queryable graph of cross-reference edges spanning genes, proteins, compounds, diseases, pathways, and clinical data. It lets users search, map, and traverse identifiers across databases with a chain-query syntax (for example, mapping a gene in Ensembl to UniProt proteins and on to PDB structures), and exposes the graph through a REST API, a Model Context Protocol (MCP) server, and a question-answering web interface for grounding LLM responses in structured biomedical data.
domains:
  - biomedical
  - genomics
  - proteomics
  - pathways
  - drug discovery
  - clinical
homepage_url: https://sugi.bio/biobtree/
id: biobtree
last_modified_date: '2026-06-24T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/agpl-3.0.en.html
  label: AGPL-3.0
name: BioBTree
products:
  - category: GraphProduct
    compatibility:
      - standard: biolink
        version: 4.2.1
    compression: gzip
    description: Human-scoped, Neo4j-ready subgraph of the BioBTree knowledge graph, exported as a biolink-typed KGX graph (~40M nodes / ~132M edges, ~8.3 GB compressed across separate node and edge files). A practical projection of the full graph for human-centric biomedical use. Published on Zenodo.
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
  - category: ProgrammingInterface
    description: REST API for searching identifiers and special keywords, mapping between data sources with a chain-query syntax, and retrieving entries across the integrated BioBTree databases.
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
  - category: ProgrammingInterface
    description: Model Context Protocol (MCP) server exposing BioBTree to AI and LLM clients for natural-language querying grounded in the integrated biomedical databases.
    format: http
    id: biobtree.mcp
    is_public: true
    name: BioBTree MCP Server
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biobtree
    product_url: https://sugi.bio/biobtree/mcp
  - category: GraphicalInterface
    description: Web-based question-and-answer interface that generates factual, identifier-anchored answers to biological questions, with each answer linked to the underlying REST API calls.
    format: http
    id: biobtree.qa
    name: BioBTree Q&A Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biobtree
    product_url: https://sugi.bio/biobtree/
  - category: DocumentationProduct
    description: Source code, dataset documentation, and usage instructions for BioBTree, including the list of integrated data sources and the local build and command-line tooling.
    format: http
    id: biobtree.docs
    name: BioBTree Repository and Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biobtree
    product_url: https://github.com/tamerh/biobtree
publications:
  - authors:
      - Tamer Gur
    doi: doi:10.5281/zenodo.18962899
    id: doi:10.5281/zenodo.18962899
    journal: Zenodo
    preferred: true
    title: 'BioBTree v2: Grounding LLM Responses with Large-Scale Structured Biomedical Data'
    year: '2026'
  - authors:
      - Tamer Gur
    doi: doi:10.12688/f1000research.17927.1
    id: doi:10.12688/f1000research.17927.1
    journal: F1000Research
    title: 'Biobtree: A tool to search, map and visualize bioinformatics identifiers and special keywords'
    year: '2019'
repository: https://github.com/tamerh/biobtree
---

# BioBTree

BioBTree is a unified biomedical knowledge graph that integrates more than 70
primary data sources into a single queryable graph of cross-reference edges. It
spans genes, proteins, compounds, diseases, pathways, and clinical data from
resources such as Ensembl, UniProt, PDB, ChEMBL, Reactome, and ClinVar.

Users can search identifiers and special keywords, map between databases using a
chain-query syntax, and traverse connections across resources in a single query.
BioBTree is accessible through a REST API, a Model Context Protocol (MCP) server
for AI and LLM integration, and a question-answering web interface designed to
ground LLM responses in authoritative, identifier-anchored biomedical data.
