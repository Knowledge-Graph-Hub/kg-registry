---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: amos.bairoch@sib.swiss
  label: Amos Bairoch
  orcid: 0000-0002-2261-7130
- category: Organization
  contact_details:
  - contact_type: url
    value: https://web.expasy.org/groups/calipho/
  - contact_type: email
    value: cellosaurus@sib.swiss
  id: sib
  label: CALIPHO Group - SIB Swiss Institute of Bioinformatics
creation_date: '2025-05-07T00:00:00Z'
description: Cellosaurus is a knowledge resource on cell lines providing information
  on cell lines from vertebrates, invertebrates, and plants, including standardized
  nomenclature, cross-references to other databases, and information on problematic
  cell lines.
domains:
- biological systems
- health
homepage_url: https://www.cellosaurus.org/
id: cellosaurus
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Cellosaurus
products:
- category: GraphicalInterface
  description: Web interface for searching and exploring Cellosaurus data
  format: http
  id: cellosaurus.site
  is_public: true
  name: Cellosaurus Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_url: https://www.cellosaurus.org/
- category: Product
  description: Complete Cellosaurus data in flat text format
  format: tsv
  id: cellosaurus.txt
  name: Cellosaurus Text
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_file_size: 117036445
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus.txt
- category: Product
  description: Cellosaurus data in XML format
  format: xml
  id: cellosaurus.xml
  name: Cellosaurus XML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_file_size: 634465764
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus.xml
- category: MappingProduct
  description: Cellosaurus cross-references in tab-delimited format
  format: tsv
  id: cellosaurus.xrefs
  name: Cellosaurus Cross-references
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus_xrefs.tsv
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 404 error
    when accessing file'
- category: Product
  description: Complete Cellosaurus data in RDF format using the Turtle syntax
  format: ttl
  id: cellosaurus.rdf
  name: Cellosaurus RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus.ttl
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 404 error
    when accessing file'
- category: ProgrammingInterface
  description: RESTful API for programmatic access to Cellosaurus data
  id: cellosaurus.api.rest
  is_public: true
  name: Cellosaurus API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_url: https://api.cellosaurus.org/
- category: ProgrammingInterface
  description: SPARQL endpoint for querying Cellosaurus RDF data
  id: cellosaurus.api.sparql
  is_public: true
  name: Cellosaurus SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_url: https://api.cellosaurus.org/sparql-editor
- category: ProcessProduct
  description: CLASTR tool for STR similarity search across cell lines
  format: javascript
  id: cellosaurus.clastr
  name: CLASTR STR Similarity Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  product_url: https://www.cellosaurus.org/str-search/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
publications:
- authors:
  - Bairoch A
  doi: doi:10.7171/jbt.18-2902-002
  id: doi:10.7171/jbt.18-2902-002
  preferred: true
  title: The Cellosaurus, a cell-line knowledge resource
  year: '2018'
repository: https://github.com/calipho-sib/cellosaurus
taxon:
- NCBITaxon:9606
---
Cellosaurus is a comprehensive knowledge resource on cell lines from vertebrates, invertebrates, and plants. It serves as a reference for cell line information, providing researchers with standardized nomenclature, cross-references to other relevant databases, and detailed information about cell line characteristics, authentication, and potential problems.

As of Release 52 (April 2025), Cellosaurus documents 163,868 cell lines, including 121,295 human, 29,536 mouse, and 3,115 rat cell lines. The database provides extensive information for each cell line entry, including:

- Standardized nomenclature and aliases
- Species of origin and cell type
- Transforming techniques used to establish the cell line
- Microbiological status (mycoplasma testing)
- Authentication information (STR profiles, karyotypes)
- Cross-references to other databases and literature
- Doubling time and culture conditions
- Genome sequence data availability
- Special designations and identifiers (e.g., RRID, CVCL)

A particularly important feature of Cellosaurus is its documentation of problematic (misidentified or contaminated) cell lines, helping researchers avoid using compromised cell lines in their experiments.

The database is recognized as a Global Core Biodata Resource (GCBR), an ELIXIR Core Data Resource, and an IRDiRC Recognized Resource. It is developed and maintained by the CALIPHO group at the SIB Swiss Institute of Bioinformatics.

Cellosaurus data is available through a user-friendly web interface, a RESTful API for programmatic access, a SPARQL endpoint for semantic web queries, and downloadable data files in various formats including text, XML, and RDF.