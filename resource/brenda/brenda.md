---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: BRENDA (BRaunschweig ENzyme DAtabase) is the main collection of enzyme
  functional data available to the scientific community. It provides comprehensive
  information on enzyme nomenclature, reaction mechanisms, specificity, functional
  parameters, and enzyme-related disease information. BRENDA integrates biochemical
  and molecular information from primary literature, patents, and data collections
  to support enzyme research and applications in biotechnology, medicine, and metabolic
  engineering. The database is curated at the Leibniz Institute DSMZ and is part of
  ELIXIR Core Data Resources and the German Network for Bioinformatics Infrastructure
  (de.NBI).
domains:
- chemistry and biochemistry
- pathways
- biomedical
homepage_url: https://www.brenda-enzymes.org/
id: brenda
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: BRENDA
products:
- category: GraphicalInterface
  description: Web-based search and browsing interface for enzyme data with advanced
    query capabilities including EC number classification, organism taxonomy, metabolic
    pathways, enzyme structures, and functional parameters
  format: http
  id: brenda.web
  name: BRENDA Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://www.brenda-enzymes.org/
- category: ProgrammingInterface
  description: SOAP web service API providing programmatic access to enzyme data with
    methods for querying kinetic parameters, substrates, products, organisms, sequences,
    and other enzyme properties
  format: http
  id: brenda.soap
  name: BRENDA SOAP API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://www.brenda-enzymes.org/soap.php
- category: ProgrammingInterface
  description: SPARQL endpoint for querying BRENDA knowledge graph with semantic web
    technologies
  format: http
  id: brenda.sparql
  name: BRENDA SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://sparql.dsmz.de/brenda
- category: Product
  description: Downloadable text files containing complete BRENDA enzyme data in structured
    format
  format: mixed
  id: brenda.textfile
  name: BRENDA Textfile Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://www.brenda-enzymes.org/download.php
- category: Product
  description: Downloadable JSON files containing complete BRENDA enzyme data with
    schema documentation
  format: json
  id: brenda.json
  name: BRENDA JSON Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://www.brenda-enzymes.org/download.php
- category: DocumentationProduct
  description: BRENDA help and tutorial resources covering support, usage guidance,
    FAQs, and tutorial videos.
  format: http
  id: brenda.docs
  name: BRENDA Help and Tutorials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://www.brenda-enzymes.org/help.php
  warnings: []
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
publications:
- authors:
  - Hauenstein, J.
  - Jeske, L.
  - "J\xE4de, A."
  - Krull, M.
  - "D\xFCmmer, K."
  - Koblitz, J.
  - Tietz, A.
  - Jahn, D.
  - Reimer, L. C.
  - Bunk, B.
  doi: 10.1093/nar/gkaf1113
  id: PMID:41206471
  journal: Nucleic Acids Research
  title: 'BRENDA in 2026: a Global Core Biodata Resource for functional enzyme and
    metabolic data within the DSMZ Digital Diversity'
  year: '2025'
- authors:
  - Chang, A.
  - Jeske, L.
  - Ulbrich, S.
  - Hofmann, J.
  - Koblitz, J.
  - Schomburg, I.
  - Neumann-Schaal, M.
  - Jahn, D.
  - Schomburg, D.
  doi: 10.1093/nar/gkaa1025
  id: PMID:33211880
  journal: Nucleic Acids Research
  title: 'BRENDA, the ELIXIR core data resource in 2021: new developments and updates'
  year: '2021'
taxon:
- NCBITaxon:131567
---
# BRENDA

BRENDA (BRaunschweig ENzyme DAtabase) is the most comprehensive enzyme information system worldwide. It serves as a Global Core Biodata Resource providing detailed functional data on enzymes including kinetic parameters, molecular properties, substrates, products, inhibitors, cofactors, and disease relationships.

## Key Features

- **Comprehensive Coverage**: Over 7,500 EC-classified enzymes with data from more than 150,000 literature references
- **Functional Parameters**: Extensive kinetic data including KM, Kcat, Ki, IC50 values, pH and temperature optima
- **Structural Information**: Links to 3D structures, protein sequences, and enzyme-ligand interactions
- **Organism Information**: Enzyme data across all domains of life with taxonomic classification
- **Disease Associations**: Links between enzymes and diseases with confidence classifications
- **Metabolic Context**: Integration with metabolic pathways and reaction networks

## Data Access

BRENDA provides multiple access methods:
- Web interface with advanced search capabilities
- SOAP API for programmatic access
- SPARQL endpoint for semantic queries
- Bulk downloads in text and JSON formats
- Integration with other biological databases

The database is curated at the Leibniz Institute DSMZ in Germany and is part of the ELIXIR Core Data Resources and de.NBI infrastructure.