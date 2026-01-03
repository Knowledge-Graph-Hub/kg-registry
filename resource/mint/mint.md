---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  label: MINT Team - University of Rome Tor Vergata
creation_date: '2025-10-31T00:00:00Z'
description: MINT (The Molecular INTeraction database) is a public and open source
  database focusing on experimentally verified protein-protein interactions mined
  from the scientific literature by expert curators. Molecular interactions are annotated
  according to international PSI-MI standards and follow the PSI-MI controlled vocabulary.
  MINT is a founder and main member of the IMEx consortium and provides data that
  is integrated into the IntAct database as part of a single non-redundant open access
  dataset. As an ELIXIR Core Data Resource and Global Core Biodata Resource, MINT
  contains over 139,000 interactions involving 27,800+ interactors from 676 organisms
  extracted from 6,500+ publications.
domains:
- proteomics
- biomedical
- systems biology
- biological systems
homepage_url: https://mint.bio.uniroma2.it/
id: mint
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Mint
products:
- category: GraphicalInterface
  description: Web interface for browsing, searching, and visualizing protein-protein
    interaction data from MINT with advanced search capabilities.
  format: http
  id: mint.portal
  name: MINT Web Portal
  original_source:
  - mint
  product_url: https://mint.bio.uniroma2.it/
- category: Product
  description: Complete MINT dataset in PSI-MI MITAB 2.7 format accessible via PSICQUIC
    web service.
  format: psi_mi_mitab
  id: mint.mitab.all
  name: MINT MITAB Full Dataset
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/*
  warnings:
  - File was not able to be retrieved when checked on 2026-01-02_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-03_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-01-03: No Content-Length
    header found'
- category: Product
  description: Human protein interactions from MINT in PSI-MI MITAB format for Homo
    sapiens (NCBITaxon 9606).
  format: psi_mi_mitab
  id: mint.mitab.human
  name: MINT Human Interactions
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/species:human
  warnings:
  - File was not able to be retrieved when checked on 2026-01-02_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-03_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-01-03: No Content-Length
    header found'
- category: Product
  description: Mouse protein interactions from MINT in PSI-MI MITAB format for Mus
    musculus (NCBITaxon 10090).
  format: psi_mi_mitab
  id: mint.mitab.mouse
  name: MINT Mouse Interactions
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/species:mouse
  warnings:
  - File was not able to be retrieved when checked on 2026-01-02_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-03_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-01-03: No Content-Length
    header found'
- category: ProgrammingInterface
  description: PSICQUIC SOAP and REST web services for programmatic access to MINT
    data using Molecular Interactions Query Language (MIQL).
  id: mint.psicquic
  name: MINT PSICQUIC Web Service
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/
- category: GraphicalInterface
  description: Advanced search interface for querying MINT data with field-specific
    searches and boolean operators.
  format: http
  id: mint.advanced.search
  name: MINT Advanced Search
  product_url: https://mint.bio.uniroma2.it/index.php/advanced-search/
- category: Product
  description: Historical consolidated protein interaction index in PSI-MITAB 2.5
    format aggregating data from BIND, BioGrid, DIP, HPRD, IntAct, MINT, MPact, MPPI
    and OPHID
  format: psi_mi_mitab
  id: irefindex.database
  name: iRefIndex Database
  original_source:
  - bind
  - biogrid
  - dip
  - hprd
  - intact
  - mint
publications:
- doi: 10.1016/s0014-5793(01)03293-8
  id: PMID:11911893
  journal: FEBS Lett
  title: 'MINT: a Molecular INTeraction database'
  year: '2002'
- doi: 10.1093/nar/gkl950
  id: PMID:17135203
  journal: Nucleic Acids Res
  title: 'MINT: the Molecular INTeraction database'
  year: '2007'
- doi: 10.1093/nar/gkr930
  id: PMID:22096227
  journal: Nucleic Acids Res
  title: 'MINT, the molecular interaction database: 2012 update'
  year: '2012'
synonyms:
- MINT
- Molecular INTeraction Database
---
## Description

MINT (The Molecular INTeraction database) is a comprehensive public repository for experimentally verified protein-protein interactions curated from peer-reviewed scientific literature. Developed and maintained by the University of Rome Tor Vergata, MINT serves as a critical resource for researchers studying molecular interactions and protein networks.

## Key Features

### Expert Curation
- Manual curation by expert biologists
- Extraction of experimental details from published literature
- Focus on experimentally verified interactions
- Comprehensive annotation of interaction context and methods

### Standards Compliance
- Annotated according to PSI-MI (Proteomics Standards Initiative - Molecular Interactions) standards
- Uses PSI-MI controlled vocabulary for consistency
- Provides data in standard PSI-MI XML and MITAB formats
- Compatible with PSICQUIC query protocol

### Database Statistics (Current)
- **Publications**: 6,515 curated papers
- **Interactions**: 139,980 protein-protein interactions
- **Interactors**: 27,802 unique proteins
- **Organisms**: 676 species represented

### IMEx Consortium Member
MINT is a founder and one of the main members of the International Molecular Exchange (IMEx) consortium. IMEx resources have merged their efforts to provide comprehensively annotated molecular interaction data integrated into a single, non-redundant, open access dataset stored and available through the IntAct database at EBI.

## Core Resources Status

- **ELIXIR Core Data Resource**: Recognized as part of the European life sciences infrastructure
- **Global Core Biodata Resource**: Designated as essential resource for global biomedical research

## Data Access Methods

### Web Interface
Interactive portal for:
- Searching protein interactions
- Browsing by species, publication, or interaction type
- Visualizing interaction networks
- Advanced field-specific queries

### Downloads
- Complete dataset via PSICQUIC web service
- Species-specific datasets (human, mouse, fly, yeast)
- PSI-MI MITAB 2.7 format
- Integration with IntAct for complete IMEx data

### Programmatic Access
- PSICQUIC SOAP web service
- PSICQUIC REST API
- Molecular Interactions Query Language (MIQL) support
- Field-specific queries with boolean operators

## Query Capabilities

### MIQL Syntax
Based on Lucene's syntax with support for:
- **Terms**: Single words or phrases (`brca2`, `"pull down"`)
- **Fields**: Search specific columns (`species:human`, `detmethod:"two hybrid*"`)
- **Operators**: OR, AND, NOT, +, - (`brca2 AND rpa1`)
- **Modifiers**: Wildcards, fuzzy search, proximity, ranges
- **Grouping**: Complex queries with parentheses

### Searchable Fields
- Identifiers (A/B or both)
- Aliases and alternative names
- Publication authors and PMIDs
- Taxonomic IDs and species names
- Interaction types and detection methods
- Interaction sources and identifiers

## Data Format Standards

### PSI-MI MITAB 2.7
Tab-delimited format including:
- Interactor identifiers and types
- Interaction detection methods
- Publication references
- Organism information
- Confidence scores
- Cross-references to other databases

### PSI-MI XML
Structured XML format with comprehensive metadata and cross-references for integration with other tools and databases.

## Integration and Cross-References

MINT data includes extensive cross-references to:
- UniProtKB (protein sequences)
- PubMed (scientific literature)
- Gene Ontology (functional annotations)
- Taxonomy databases (organism information)
- Other interaction databases via IMEx

## Community and Support

### Citation Guidelines
Users are encouraged to cite:
- MINT database publications
- IMEx consortium for integrated data
- Individual datasets when used in analyses

### Data Reuse
All data available under Creative Commons Attribution 4.0 International (CC BY 4.0) license, allowing free use with proper attribution.

## Related Resources

- **IntAct**: Primary repository for integrated IMEx data including MINT
- **IMEx Consortium**: International consortium for molecular interaction data exchange
- **PSICQUIC**: Standardized web service protocol for accessing interaction databases
- **iRefIndex**: Historical consolidated index that included MINT data

## Technical Infrastructure

- Hosted at University of Rome Tor Vergata
- Part of ELIXIR distributed infrastructure
- Accessible via redundant web services (EBI PSICQUIC endpoint)
- Regular updates with new literature curation

## Historical Context

MINT was established as one of the first comprehensive protein interaction databases and has been continuously maintained and updated since 2002. As a founding member of IMEx, MINT has played a crucial role in establishing standards for molecular interaction data annotation and exchange.

## Future Development

MINT continues to:
- Expand literature coverage
- Improve curation workflows
- Enhance integration with IntAct
- Support emerging data types
- Maintain compliance with evolving standards