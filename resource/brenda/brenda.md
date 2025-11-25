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
last_modified_date: '2025-11-19T00:00:00Z'
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
  - brenda
  product_url: https://www.brenda-enzymes.org/
- category: ProgrammingInterface
  description: SOAP web service API providing programmatic access to enzyme data with
    methods for querying kinetic parameters, substrates, products, organisms, sequences,
    and other enzyme properties
  format: http
  id: brenda.soap
  name: BRENDA SOAP API
  original_source:
  - brenda
  product_url: https://www.brenda-enzymes.org/soap.php
- category: Product
  description: SPARQL endpoint for querying BRENDA knowledge graph with semantic web
    technologies
  format: http
  id: brenda.sparql
  name: BRENDA SPARQL Endpoint
  original_source:
  - brenda
  product_url: https://sparql.dsmz.de/brenda
  warnings:
  - 'File was not able to be retrieved when checked on 2025-11-22: HTTP 403 error
    when accessing file'
  - File was not able to be retrieved when checked on 2025-11-21_ HTTP 403 error when
    accessing file
- category: Product
  description: Downloadable text files containing complete BRENDA enzyme data in structured
    format
  format: mixed
  id: brenda.textfile
  name: BRENDA Textfile Download
  original_source:
  - brenda
  product_url: https://www.brenda-enzymes.org/download.php
  warnings:
  - 'File was not able to be retrieved when checked on 2025-11-22: HTTP 403 error
    when accessing file'
  - File was not able to be retrieved when checked on 2025-11-21_ HTTP 403 error when
    accessing file
- category: Product
  description: Downloadable JSON files containing complete BRENDA enzyme data with
    schema documentation
  format: json
  id: brenda.json
  name: BRENDA JSON Download
  original_source:
  - brenda
  product_url: https://www.brenda-enzymes.org/download.php
  warnings:
  - 'File was not able to be retrieved when checked on 2025-11-22: HTTP 403 error
    when accessing file'
  - File was not able to be retrieved when checked on 2025-11-21_ HTTP 403 error when
    accessing file
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