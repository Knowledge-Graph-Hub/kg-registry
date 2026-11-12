---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: tamerh
  label: Tamer Gur
  orcid: 0000-0001-5822-9201
creation_date: '2026-06-15T00:00:00Z'
description: BioBTree is a unified biomedical knowledge graph that integrates more
  than 95 public data sources, including Ensembl, UniProt, PDB, ChEMBL, Reactome,
  and ClinVar, into a single queryable graph of cross-reference edges spanning genes,
  proteins, compounds, diseases, pathways, and clinical data. The full graph holds
  about 3.5 billion entries and 9.3 billion bidirectional cross-references, plus 11.7
  billion position-level variant scores (as of November 2026). It lets users search,
  map, and traverse identifiers across databases with a chain-query syntax (for example,
  mapping a gene in Ensembl to UniProt proteins and on to PDB structures), and exposes
  the graph through a REST API, a Model Context Protocol (MCP) server, and a question-answering
  web interface for grounding LLM responses in structured biomedical data.
domains:
- biomedical
- genomics
- proteomics
- pathways
- drug discovery
- clinical
homepage_url: https://sugi.bio/biobtree/
id: biobtree
last_modified_date: '2026-11-12T00:00:00Z'
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
  description: Human-scoped, Neo4j-ready subgraph of the BioBTree knowledge graph,
    exported as a biolink-typed KGX graph (~47M nodes / ~151M edges, ~9.6 GB compressed
    across node and edge files in both TSV and JSON Lines, plus a manifest). A practical
    projection of the full graph for human-centric biomedical use. Sources without
    compatible redistribution terms are excluded (full OMIM data, CTD, PanelApp, miRDB,
    and the SpliceAI and AlphaMissense variant-prediction layers). Published on Zenodo.
  edge_count: 150949120
  format: kgx
  id: biobtree.graph.human-subgraph
  latest_version: v2-2026-11
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
  node_count: 47361928
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
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
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
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
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
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
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
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
  - relation_type: prov:hadPrimarySource
    source: wikipathways
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
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:transcribed_from
  - biolink:translates_to
  - biolink:treats_or_applied_or_studied_to_treat
  product_url: https://doi.org/10.5281/zenodo.20816741
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
    source: alliance
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
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
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
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
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
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mavedb
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
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:hadPrimarySource
    source: pangolin
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
    source: revel
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://sugi.bio/biobtree/api/
- category: ProgrammingInterface
  description: Model Context Protocol (MCP) server exposing BioBTree to AI and LLM
    clients for natural-language querying grounded in the integrated biomedical databases.
  format: http
  id: biobtree.mcp
  is_public: true
  name: BioBTree MCP Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  product_url: https://sugi.bio/biobtree/mcp
- category: GraphicalInterface
  description: Web-based question-and-answer interface that generates factual, identifier-anchored
    answers to biological questions, with each answer linked to the underlying REST
    API calls.
  format: http
  id: biobtree.qa
  name: BioBTree Q&A Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  product_url: https://sugi.bio/biobtree/
- category: DocumentationProduct
  description: Source code, dataset documentation, and usage instructions for BioBTree,
    including the list of integrated data sources and the local build and command-line
    tooling.
  format: http
  id: biobtree.docs
  name: BioBTree Repository and Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  product_url: https://github.com/tamerh/biobtree
- category: Product
  description: Benchmark harness, question sets and per-question results for evaluating
    BioBTree as an LLM tool set against no tools, web search and domain-specific MCP
    servers. Includes about 1,700 questions in the main sets, among them 900 GeneTuring
    and 160 LAB-Bench DbQA questions, and a cells.csv file of 9,391 result rows. Code
    is MIT; GeneTuring questions are CC BY-NC 4.0, LAB-Bench questions are CC BY-SA
    4.0, and other questions and results are CC BY 4.0.
  format: mixed
  id: biobtree.bench
  name: BioBTree Benchmark (biobtree-bench)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  product_url: https://github.com/tamerh/biobtree-bench
- category: GraphicalInterface
  description: Sugi Atlas web site with search and one static reference page per human
    gene, drug and disease (for example /atlas/gene/TP53/). Each page also has a Markdown
    version at index.md and embeds a schema.org JSON-LD record.
  format: http
  id: sugi-atlas.portal
  name: Sugi Atlas Web Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  - relation_type: prov:wasDerivedFrom
    source: biobtree
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: chembl
  product_url: https://sugi.bio/atlas/
- category: Product
  description: JSON manifest of the atlas corpus, mapping page slugs to canonical
    names and synonyms for genes, drugs, diseases and pathways (about 12.8 MB when
    checked on 2026-10-04).
  format: json
  id: sugi-atlas.manifest
  name: Sugi Atlas Manifest
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  - relation_type: prov:wasDerivedFrom
    source: biobtree
  product_file_size: 12797962
  product_url: https://sugi.bio/atlas/manifest.json
publications:
- authors:
  - Tamer Gür
  doi: doi:10.5281/zenodo.24144112
  id: doi:10.5281/zenodo.24144112
  journal: Zenodo
  preferred: true
  title: 'BioBTree: An Integrated Biomedical Graph Database for Researchers and LLM
    Agents'
  year: '2026'
- authors:
  - Tamer Gur
  doi: doi:10.5281/zenodo.18962899
  id: doi:10.5281/zenodo.18962899
  journal: Zenodo
  title: 'BioBTree v2: Grounding LLM Responses with Large-Scale Structured Biomedical
    Data'
  year: '2026'
- authors:
  - Tamer Gur
  doi: doi:10.12688/f1000research.17927.1
  id: doi:10.12688/f1000research.17927.1
  journal: F1000Research
  title: 'Biobtree: A tool to search, map and visualize bioinformatics identifiers
    and special keywords'
  year: '2019'
repository: https://github.com/tamerh/biobtree
---
# BioBTree

BioBTree is a unified biomedical knowledge graph that integrates more than 95
public data sources into a single queryable graph of cross-reference edges, about
3.5 billion entries and 9.3 billion cross-references as of November 2026. It
spans genes, proteins, compounds, diseases, pathways, and clinical data from
resources such as Ensembl, UniProt, PDB, ChEMBL, Reactome, and ClinVar.

Users can search identifiers and special keywords, map between databases using a
chain-query syntax, and traverse connections across resources in a single query.
BioBTree is accessible through a REST API, a Model Context Protocol (MCP) server
for AI and LLM integration, and a question-answering web interface designed to
ground LLM responses in authoritative, identifier-anchored biomedical data.