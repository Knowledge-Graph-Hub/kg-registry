---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: cellxgene@chanzuckerberg.com
  - contact_type: url
    value: https://cellxgene.cziscience.com/
  label: Chan Zuckerberg Initiative
creation_date: '2026-05-28T00:00:00Z'
description: CZ CELLxGENE is a platform for finding, downloading, exploring, and analyzing
  single-cell datasets through a public data portal, integrated analysis interfaces,
  and the CELLxGENE Census programmatic access layer.
domains:
- biomedical
- genomics
homepage_url: https://cellxgene.cziscience.com/
id: cellxgene
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: CZ CELLxGENE
repository: https://github.com/chanzuckerberg/single-cell-data-portal
products:
- category: GraphicalInterface
  description: Main CZ CELLxGENE Discover portal for browsing public single-cell collections,
    datasets, gene expression views, and analysis tools.
  format: http
  id: cellxgene.portal
  name: CZ CELLxGENE Discover
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellxgene.cziscience.com/
- category: GraphicalInterface
  description: Search and download interface for public curated collections and datasets
    available through CZ CELLxGENE Discover.
  format: http
  id: cellxgene.datasets
  name: CZ CELLxGENE Datasets Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellxgene.cziscience.com/datasets
- category: ProgrammingInterface
  description: Documentation and entry point for the CELLxGENE Census API and data
    object used to query standardized single-cell expression data in R and Python.
  format: http
  id: cellxgene.census
  is_public: true
  name: CZ CELLxGENE Census
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://chanzuckerberg.github.io/cellxgene-census/
- category: DocumentationProduct
  description: Official documentation for CZ CELLxGENE Discover, Explorer, Gene Expression,
    and Annotate workflows.
  format: http
  id: cellxgene.docs
  name: CZ CELLxGENE Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellxgene.cziscience.com/docs
- category: ProgrammingInterface
  connection_url: cl-kg-neo4j-db.cellgeni.sanger.ac.uk:443
  description: Publicly available Neo4j instance for CL-KG.
  id: cl-kg.api.neo4j
  is_neo4j: true
  is_public: true
  name: CL-KG Neo4j graph instance
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl-kg
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellular-semantics.sanger.ac.uk/browser/
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
  description: The NLM-CKN knowledge graph of cellular phenotypes. It is built from
    triple assertions (subject-predicate-object) that link single-cell genomics experimental
    data (from the CELLxGENE Census) and computationally derived NS-Forest marker
    genes to the Cell Ontology and other reference ontologies, augmented with literature-derived
    assertions from text mining/NLP. The graph is produced by the NLM-CKN ETL pipeline
    as an ArangoDB archive and served via the web application at https://nlm-ckn.org.
  format: http
  id: nlm-ckn.graph
  name: nlm-ckn-graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm-ckn
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://github.com/NIH-NLM/cell-kn-mvp
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: pato
  - relation_type: prov:wasInfluencedBy
    source: mondo
  - relation_type: prov:wasInfluencedBy
    source: hsapdv
publications:
- id: https://doi.org/10.1093/nar/gkae1142
  authors:
  - Shibla Abdulla
  - Brian Aevermann
  - CZI Cell Science Program
  doi: 10.1093/nar/gkae1142
  journal: Nucleic Acids Research
  preferred: true
  title: 'CZ CELLxGENE Discover: a single-cell data platform for scalable exploration,
    analysis and modeling of aggregated data'
  year: '2025'
---
# CZ CELLxGENE

CZ CELLxGENE is a single-cell data platform from the Chan Zuckerberg Initiative
that supports public data discovery, interactive exploration, and programmatic
access to a large harmonized corpus of single-cell expression datasets.