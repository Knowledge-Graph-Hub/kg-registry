---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://naturalhistory.si.edu/research/eol
  id: smithsonian-nmnh
  label: Smithsonian Institution's National Museum of Natural History
creation_date: '2025-12-17T00:00:00Z'
description: Encyclopedia of Life (EOL) TraitBank is a searchable, comprehensive,
  open digital repository for organism traits, measurements, interactions, and other
  attributes aggregated from 50+ data sources. It covers 1.7 million taxa across the
  entire tree of life with 11 million+ trait records organized using semantic web
  standards and Darwin Core terminology.
domains: []
homepage_url: https://eol.org/pages/traitbank
id: eol-traitbank
infores_id: eol-traitbank
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Encyclopedia of Life (EOL) TraitBank
products:
- category: GraphicalInterface
  description: Interactive web interface for searching, browsing, and discovering
    organism trait data across all taxa with filtering by taxonomic group and attribute
    type
  format: http
  id: eol-traitbank.web
  name: TraitBank Web Portal
  product_url: https://eol.org/pages/traitbank
- category: ProgrammingInterface
  description: Neo4j Cypher query interface providing programmatic access to structured
    trait data, requiring authentication via EOL account
  format: http
  id: eol-traitbank.cypher
  is_public: true
  name: TraitBank Cypher Query Interface
  product_url: https://eol.org/services/authenticate
- category: ProgrammingInterface
  description: RESTful API endpoints for taxonomy, media, and text data access from
    Encyclopedia of Life
  format: http
  id: eol-traitbank.api
  is_public: true
  name: EOL API
  product_url: https://api.eol.org/
- category: ProgrammingInterface
  description: EOL Reconciliation Service API for resolving taxon names to EOL taxon
    IDs using OpenRefine-compatible reconciliation protocol
  format: http
  id: eol-traitbank.reconciliation
  is_public: true
  name: EOL Reconciliation API
  product_url: https://eol.org/api/reconciliation
- category: Product
  compression: zip
  description: Complete TraitBank bulk data export containing all 11 million+ trait
    records in CSV format with measurement details and source attribution
  format: csv
  id: eol-traitbank.bulk-csv
  name: TraitBank Bulk Data Export
  product_url: https://editors.eol.org/other_files/SDR/traits_all.zip
  warnings:
  - File was not able to be retrieved when checked on 2026-01-28_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-23_ Error connecting
    to URL_ HTTPSConnectionPool(host='editors.eol.org', port=443)_ Max retries exceeded
    with url_ /other_files/SDR/traits_all.zip (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='editors.eol.org', port=443)_ Max retries exceeded
    with url_ /other_files/SDR/traits_all.zip (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='editors.eol.org', port=443)_ Max retries exceeded
    with url_ /other_files/SDR/traits_all.zip (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-02-04: Error connecting
    to URL: HTTPSConnectionPool(host=''editors.eol.org'', port=443): Max retries exceeded
    with url: /other_files/SDR/traits_all.zip (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1000)'')))'
- category: DocumentationProduct
  description: Comprehensive documentation covering TraitBank data structure, API
    usage, authentication methods, and data formats
  format: http
  id: eol-traitbank.docs
  name: TraitBank Documentation
  product_url: https://eol.org/docs/what-is-eol/data-services
  warnings:
  - File was not able to be retrieved when checked on 2026-01-28_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-23_ Error connecting
    to URL_ HTTPSConnectionPool(host='eol.org', port=443)_ Max retries exceeded with
    url_ /docs/what-is-eol/data-services (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='eol.org', port=443)_ Max retries exceeded with
    url_ /docs/what-is-eol/data-services (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-30_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-02-04: Error connecting
    to URL: HTTPSConnectionPool(host=''eol.org'', port=443): Max retries exceeded
    with url: /docs/what-is-eol/data-services (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1000)'')))'
publications:
- authors:
  - Adams B
  - Franz N
  - König-Ries B
  - McGuinness D
  - Schildhauer M
  - Parr CS
  - Schulz KS
  - Hammock J
  - Wilson N
  - Leary P
  - Rice J
  - Corrigan RJ
  doi: 10.3233/SW-150190
  id: doi:10.3233/SW-150190
  journal: Semantic Web Journal
  preferred: true
  title: 'TraitBank: Practical semantics for organism attribute data'
  year: '2016'
- authors:
  - Parr CS
  - Wilson N
  - Leary P
  - Struzan GS
  - Ved P
  - Lans KA
  - Loyacano J
  - Brest M
  - Corrigan RJ
  - Hancher C
  - Helgen KM
  - Herrick J
  - Hammock J
  - Kataoka C
  - Lara MJ
  - Maney D
  - Martínez-Meyer E
  - Measey J
  - Rapp C
  - Sarkar I
  - Schulz KS
  - Seubert E
  - Wee B
  - Wyckoff M
  doi: 10.1371/journal.pone.0089965
  id: doi:10.1371/journal.pone.0089965
  journal: PLoS ONE
  title: 'The Encyclopedia of Life v2: Providing Global Access to Knowledge About
    Life on Earth'
  year: '2014'
repository: https://github.com/EOL
taxon:
- NCBITaxon:1
---
# Encyclopedia of Life (EOL) TraitBank

## Overview

Encyclopedia of Life (EOL) TraitBank is a comprehensive, open-access digital repository for organism traits and other attribute data aggregated from diverse sources across the entire tree of life. Launched in January 2014 as a core component of EOL v2, TraitBank represents a major effort to semantically structure and integrate biodiversity attribute data, making trait information discoverable and interoperable across the global biodiversity informatics community.

TraitBank serves as a central hub for aggregating, curating, and providing access to organism attributes spanning morphology, ecology, behavior, physiology, molecular data, and more—enabling researchers, educators, and conservationists to access curated trait data on any living organism with unprecedented ease.

## Data Content and Scale

### Scale and Coverage

TraitBank contains an extensive collection of biodiversity trait data:

- **11 million+ trait records** - Comprehensive coverage of organism attributes
- **1.7 million taxa** - Complete tree of life coverage including all major taxonomic groups
- **330+ distinct attributes** - Diverse trait categories covering physical, ecological, and behavioral characteristics
- **50+ data sources** - Integration of data from research databases, literature repositories, natural history collections, and citizen science projects
- **Multiple trait categories** - Distribution, physical description, ecology, life history, evolution, physiology, molecular biology, conservation status, and more

### Taxonomic Coverage

TraitBank provides comprehensive trait data across all domains of life:

- **Bacteria and Archaea** - Metabolic and physiological traits, habitat preferences
- **Protists** - Ecological roles, morphological characteristics, cellular attributes
- **Fungi** - Ecology, reproduction, substrate preferences, decomposition roles
- **Plants** - Physical characteristics, habitat requirements, reproduction, conservation status
- **Animals** - Comprehensive trait coverage across all major animal phyla including:
  - Invertebrates - Insecta, Mollusca, Echinodermata, Cnidaria, and others
  - Vertebrates - Fish, Amphibians, Reptiles, Birds, Mammals

Data is organized primarily at species and subspecies levels, with selective higher-taxon summaries available for key morphological, ecological, and life history attributes.

### Trait Categories

TraitBank organizes data across 11 broad subject categories:

1. **Distribution** - Geographic range, habitat type, ecosystem associations
2. **Physical Description** - Morphology, size, shape, coloration, physical attributes
3. **Ecology** - Trophic role, predator-prey relationships, habitat association, nesting behavior
4. **Life History** - Development, reproduction, lifespan, growth rates, phenology
5. **Evolution** - Evolutionary relationships, fossil record, taxonomic relationships
6. **Physiology** - Metabolism, temperature tolerance, biochemical adaptations
7. **Molecular Biology** - Genetic data, DNA sequences, molecular markers
8. **Conservation Status** - IUCN Red List classification, threat assessment, protected status
9. **Population Dynamics** - Population size, trends, breeding success
10. **Behavior** - Social structure, communication, foraging, movement patterns
11. **Interactions** - Ecological relationships, food webs, parasitism, mutualism

## Data Access and Formats

### Access Methods

TraitBank provides multiple mechanisms for accessing trait data:

**1. Web Portal Interface**
- Interactive search and browse functionality at https://eol.org/pages/traitbank
- User-friendly discovery of organism traits by taxon or attribute
- Filtering by trait type, data source, and quality levels
- Integration with EOL species pages for comprehensive organism information

**2. Neo4j Cypher Query Interface**
- Graph database backend enabling complex relational queries
- Direct database access for advanced users
- Requires authentication via EOL account at https://eol.org/services/authenticate
- Stores authentication key in .Renviron file as "EOL_CYPHER_KEY"
- Powerful querying of trait relationships and cross-taxonomic patterns

**3. RESTful APIs**
- Classic EOL APIs (https://api.eol.org/):
  - Taxonomy API - Retrieve taxonomic information
  - Media API - Access images and multimedia content
  - Text API - Retrieve text descriptions and content
- Structured Data API - Direct access to trait and measurement data
- Authentication required for some endpoints; contact Jen Hammock for access

**4. Reconciliation Service**
- OpenRefine-compatible reconciliation protocol
- Endpoint: https://eol.org/api/reconciliation
- Resolve taxon names to EOL identifiers
- Avoid homonym errors with available filters

**5. Bulk Data Downloads**
- Complete TraitBank export available as CSV files
- Download: `wget https://editors.eol.org/other_files/SDR/traits_all.zip`
- Filename: `traits.csv`
- Suitable for large-scale analytics and knowledge graph construction

### Data Formats

TraitBank supports multiple standard data formats:

- **CSV** (Comma-Separated Values) - For bulk exports and analysis
- **JSON** and **JSON-LD** - For programmatic access and semantic web applications
- **RDF** (Resource Description Framework) - Built on RDF triple store architecture for semantic interoperability
- **Darwin Core** - Standardized terminology and MeasurementOrFact standard implementation
- **SPARQL** - Query capability on Virtuoso backend for semantic queries

### Data Standards and Provenance

All TraitBank records include comprehensive metadata:

- **Darwin Core Terminology** - Standardized attribute naming and organization
- **Source Attribution** - Complete provenance including original data source and collector
- **Measurement Methods** - Documentation of how data was collected
- **Confidence Levels** - Quality indicators for varying data reliability
- **Reference Links** - Citations and links to primary literature

## Technical Infrastructure

### Technologies

- **Graph Database**: Neo4j for efficient relationship querying
- **Triple Store**: RDF backend for semantic web compatibility
- **Standards**: Darwin Core, SPARQL, JSON-LD, Linked Open Data principles
- **Authentication**: EOL account-based access control

### Key Features

**Semantic Integration**
- RDF-based implementation enabling Linked Open Data integration
- Darwin Core terminology ensuring interoperability with other biodiversity datasets
- Support for complex queries linking traits, taxa, and ecosystem properties

**Comprehensive Data Aggregation**
- Integration of 50+ diverse data sources into unified semantic structure
- Preservation of data provenance and attribution
- Support for data of varying quality from peer-reviewed to citizen science

**Flexible Query Capabilities**
- Find all traits for a given organism
- Compare traits across related species
- Identify organisms with specific trait combinations
- Trace trait values across evolutionary lineages
- Analyze trait distributions within habitats or ecosystems

**Global Accessibility**
- Free and open access to all data
- CC-BY 4.0 licensing enabling data reuse
- Multiple query interfaces for different user expertise levels
- Integration with major biodiversity informatics platforms

## Use Cases and Applications

### Research Applications

- **Comparative Biology** - Cross-species trait comparisons for evolutionary and physiological studies
- **Macroecology** - Large-scale analysis of trait patterns across biogeographic regions
- **Conservation Biology** - Identifying vulnerable species based on trait combinations and threat assessments
- **Ecosystem Function** - Linking organism traits to ecosystem services and processes
- **Evolutionary Biology** - Studying trait evolution and adaptive radiation patterns

### Practical Applications

- **Conservation Planning** - Species vulnerability assessment and habitat requirements documentation
- **Agricultural Research** - Trait data for crop and livestock improvement programs
- **Environmental Impact Assessment** - Understanding species vulnerability to environmental changes
- **Bioprospecting** - Identifying organisms with traits relevant to biotechnology applications
- **Education** - Open-access resources for biodiversity and conservation education

### Knowledge Graph Development

- **Integration with other KGs** - Semantic foundation for linking trait data to other biological and environmental datasets
- **Question Answering** - Powering systems that answer questions about organism characteristics
- **Data Interoperability** - Standard format for trait data across distributed data sources
- **Semantic Search** - Finding organisms by complex trait combinations

## Data Quality and Curation

TraitBank maintains data quality through multiple mechanisms:

- **Curated Data** - Manual review of high-priority trait assertions
- **Attributed Sources** - Every record tracks original source for accountability
- **Confidence Indicators** - Quality flags for data of varying certainty
- **Community Feedback** - Integration of corrections and suggestions from the user community
- **Regular Updates** - Ongoing incorporation of new data and corrections

## Funding and Support

**Lead Institution:**
- Smithsonian Institution's National Museum of Natural History

**Initial Funding:**
- John D. and Catherine T. MacArthur Foundation ($10 million)
- Alfred P. Sloan Foundation ($2.5 million + $5 million additional commitment)

**Organizational Support:**
- Biodiversity Informatics Group (Field Museum)
- Biodiversity Heritage Library
- Harvard University (Learning and Education)
- Distributed network of international biodiversity institutions

**Founding:**
- Established in 2008, launched May 2007
- Continuously developed and maintained since inception

## Citation and Usage

Encyclopedia of Life TraitBank data is freely available under the Creative Commons Attribution 4.0 (CC BY 4.0) license. Users are required to provide appropriate attribution to the original data sources when using TraitBank data in research, applications, or educational materials.

The system is maintained by the Smithsonian Institution's National Museum of Natural History in collaboration with the global biodiversity informatics community, dedicated to making comprehensive trait data freely available to support biodiversity research, conservation, and education worldwide.

### Recommended Citation

When citing TraitBank as a data source:

"Encyclopedia of Life TraitBank. Available at https://eol.org/pages/traitbank"

For the primary semantic web paper:
"Adams et al. (2016) TraitBank: Practical semantics for organism attribute data. Semantic Web, 7(6), 577-588. https://doi.org/10.3233/SW-150190"