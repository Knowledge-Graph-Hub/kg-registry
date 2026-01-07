---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.gbif.org/
  - contact_type: email
    value: info@gbif.org
  id: gbif-secretariat
  label: GBIF Secretariat
creation_date: '2025-12-17T00:00:00Z'
description: Global Biodiversity Information Facility (GBIF) is an international network
  and data infrastructure providing open access to over 3.1 billion species occurrence
  records from 81,000+ datasets contributed by 2,500+ publishing institutions worldwide.
  GBIF aggregates species distribution and biodiversity data using Darwin Core standards.
domains: []
homepage_url: https://www.gbif.org/
id: gbif
infores_id: gbif
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 and CC BY (mixed)
name: Global Biodiversity Information Facility (GBIF)
products:
- category: GraphicalInterface
  description: Web portal for searching, filtering, and discovering occurrence records,
    species information, datasets, and organizations with interactive mapping and
    download capabilities
  format: http
  id: gbif.portal
  name: GBIF.org Portal
  product_url: https://www.gbif.org/
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to registry, species, occurrence,
    and map data with JSON responses and support for complex queries
  format: http
  id: gbif.api
  is_public: true
  name: GBIF REST API
  product_url: https://api.gbif.org/v1/
- category: ProgrammingInterface
  description: Raster tile maps API providing global occurrence distribution maps
    in PNG and Mapbox Vector Tile (MVT) formats
  format: http
  id: gbif.maps-api
  is_public: true
  name: GBIF Maps API
  product_url: https://api.gbif.org/maps/
- category: Product
  compression: zip
  description: Darwin Core Archive format occurrence downloads from 81,000+ datasets
    with interpreted and verbatim data, metadata, and multimedia information
  id: gbif.dwc-archive
  name: GBIF Darwin Core Archive Downloads
  product_url: https://www.gbif.org/occurrence/download
  warnings:
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-07: HTTP 403 error
    when accessing file'
- category: Product
  compression: zip
  description: Simple CSV format occurrence downloads with interpreted data and commonly
    used columns, suitable for spreadsheet and programming analysis
  id: gbif.csv-download
  name: GBIF Simple CSV Downloads
  product_url: https://www.gbif.org/occurrence/download
  warnings:
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-07: HTTP 403 error
    when accessing file'
- category: DocumentationProduct
  description: Comprehensive technical documentation, API reference, developer guides,
    and data formats documentation
  format: http
  id: gbif.documentation
  is_public: true
  name: GBIF Technical Documentation
  product_url: https://techdocs.gbif.org/
- category: Product
  description: Integrated Publishing Toolkit (IPT) - free, open-source Java software
    for publishing Darwin Core formatted biodiversity datasets with web interface
    and automated data management capabilities
  id: gbif.ipt
  name: GBIF Integrated Publishing Toolkit (IPT)
  product_url: https://www.gbif.org/ipt
  warnings:
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-07: HTTP 403 error
    when accessing file'
publications:
- authors:
  - Robertson T
  - Döring M
  - Guralnick R
  - Bloom D
  - Wieczorek J
  - Braak K
  - Otegui J
  - Russell L
  - Desmet P
  doi: 10.1371/journal.pone.0102623
  id: doi:10.1371/journal.pone.0102623
  journal: PLOS ONE
  title: 'The GBIF Integrated Publishing Toolkit: Facilitating the Efficient Publishing
    of Biodiversity Data on the Internet'
  year: '2014'
repository: https://github.com/gbif
taxon:
- NCBITaxon:1
---
# Global Biodiversity Information Facility (GBIF)

## Overview

The Global Biodiversity Information Facility (GBIF) is an international network and data infrastructure coordinated through its Secretariat in Copenhagen and hosted by The Natural History Museum of Denmark. It provides anyone, anywhere with open access to data about all types of life on Earth. As of 2025, GBIF aggregates and provides access to over 3.1 billion species occurrence records from 81,000+ datasets contributed by 2,500+ publishing institutions worldwide, making it the largest biodiversity data portal globally.

GBIF operates as a collaborative network of governments and organizations that share a commitment to enabling anyone to access data about life on Earth, removing barriers between data holders and data users, and supporting biodiversity research, conservation, and sustainable development globally.

## Data Content and Scale

### Overall Scale

GBIF represents the most comprehensive aggregation of biodiversity occurrence data available globally:

- **3.1 billion species occurrence records** - All types of life across all continents and time periods
- **81,000+ datasets** - From natural history museums, citizen science networks, research institutions, and monitoring programs
- **2,500+ publishing institutions** - Contributing data from diverse sources
- **All major organism groups** - Plants, animals, fungi, protists, bacteria, and archaea
- **Temporal coverage** - From 18th-19th century museum specimens to recent citizen science observations
- **50% of records** - Sourced from citizen science (primarily iNaturalist)

### Growth Trajectory

- **2018**: Reached 1 billion records milestone
- **Recent decade**: Grown by over 1,150%
- **Daily growth**: Continuous addition of new occurrence data
- **2023**: 1,700+ research papers published using GBIF data
- **Q1 2025**: 27% increase in papers using GBIF data compared to 2024

### Data Distribution

**License Distribution:**
- **82%+ of records** - Under CC0 or CC-BY (most openly licensed)
- **83% of datasets** - CC-BY (requires attribution)
- **5% of datasets** - CC0 (unrestricted use)
- **12% of datasets** - CC-BY-NC (non-commercial use restrictions)

## Taxonomic Coverage

GBIF provides comprehensive coverage of all domains of life:

- **Bacteria and Archaea** - Microbial occurrence records from environmental surveys
- **Protists** - Single-celled eukaryotes and related organisms
- **Fungi** - All fungal groups from diverse sources
- **Plants** - Global coverage from herbaria, botanical surveys, and field observations
- **Animals** - Complete animal diversity including:
  - Invertebrates (insects dominate - iNaturalist primary source)
  - Vertebrates (birds, mammals, reptiles, amphibians, fish)

## Data Access and Formats

### Interactive Web Portal

**GBIF.org Portal**
- Global occurrence search and discovery
- Dataset browsing and characterization
- Publishing organization information
- Interactive mapping and visualization
- Download interface for custom occurrence selections
- Free registration for advanced features
- Data quality filtering and assessment

### Programmatic Access via APIs

**v1 REST API** (https://api.gbif.org/v1/)

**Registry API** - Manage and search:
- Datasets (81,000+ indexed)
- Publishing organizations
- Networks
- Technical endpoints
- DOI registration

**Species API** - Discover and access:
- Species/taxa information
- Taxonomic name interpretation
- GBIF Backbone Taxonomy lookups
- Scientificname fuzzy matching
- Higher-level taxonomic lookups

**Occurrence API** - Search and download:
- Indexed occurrence data (3.1+ billion records)
- Complex queries with Darwin Core field filtering
- Download API for bulk occurrence downloads
- Range queries (e.g., year=1800,1899)
- Geospatial and taxonomic filtering

**Maps API** - Raster tile maps:
- Global occurrence distribution maps
- PNG tile format for web applications
- Mapbox Vector Tile (MVT) format
- Style customization options

**Response Format:**
- JSON (primary format)
- Pagination support for large result sets
- Comprehensive metadata in responses

### Data Formats

**Primary Standards:**
- **Darwin Core** - International standard for biodiversity data
- **Darwin Core Archive (DwC-A)** - Compressed ZIP containing:
  - `occurrence.txt` - Interpreted occurrence data (tab-separated)
  - `verbatim.txt` - Original uninterpreted source data
  - `multimedia.txt` - Associated images and multimedia
  - `meta.xml` - Metadata describing file structure
- **Simple CSV** - Spreadsheet-compatible tab or comma-delimited format
- **JSON** - Via API responses

### Bulk Downloads

**Download Methods:**
- Web interface for custom queries
- REST API for programmatic downloads
- Large datasets (>100GB) via cloud storage (AWS, Azure)

**Download Features:**
- Filter by Darwin Core fields
- Customize column selection
- Quality control options
- License filtering
- DOI-based citation support
- Email notification upon completion

**Availability:**
- Individual species downloads
- Dataset-specific downloads
- Regional/geographic downloads
- Temporal filtering (date ranges)
- Full Darwin Core Archive or Simple CSV formats

## Data Processing and Quality

### Data Standardization

GBIF processes all incoming data through a standardized pipeline:

1. **Normalization** - Converts data fragments to Darwin Core terms
2. **Verbatim Stage** - Records marked as "verbatim" after initial normalization
3. **Interpretation** - Quality control and data enrichment
4. **Validation** - Taxonomic and spatial validation

### Quality Control Mechanisms

**Taxonomic Processing:**
- Validation against GBIF Backbone Taxonomy
- Automatic gap-filling for missing higher taxonomic levels
- Fuzzy name matching for misspelled taxa
- Authority file linkage (Catalogue of Life, NCBI, etc.)

**Data Quality Flags & Issues:**
- 30+ quality flags for checklist datasets
- Taxonomic match status indicators
- Coordinate precision and accuracy assessments
- Temporal validity checks
- Missing field detection
- Data entry error detection

**Publisher Support:**
- Validator tool for pre-publication quality checks
- Guidance for publishers to improve data quality
- Quality metrics and issue reporting
- Training and documentation

### Dataset Types

GBIF processes three primary dataset types:

1. **Occurrence Datasets** - Evidence of species at place/date
2. **Checklist Datasets** - Taxonomic inventories and catalogs
3. **Sampling-Event Datasets** - Standardized surveys with effort metadata

## Data Sources and Publishers

### Primary Contributors

**Citizen Science Networks:**
- **iNaturalist** - Dominant source (42% of all species have 100% records from iNaturalist)
- Other citizen observation platforms
- Community science initiatives

**Institutional Contributors:**
- Natural history museums (specimen data from centuries)
- Herbaria (plant specimens)
- Research institutions
- Government agencies
- Academic universities

**Monitoring and Surveys:**
- Environmental monitoring schemes
- Biodiversity monitoring programs
- Field surveys and expeditions
- DNA barcoding projects

**Data Integration:**
- eBird (bird observations)
- iDigBio (specimen data)
- Smithsonian Institution networks
- International museum networks
- Regional and national biodiversity databases

### Publishing Infrastructure

**Integrated Publishing Toolkit (IPT):**
- Free, open-source Java software
- Web interface for data and metadata management
- Darwin Core term mapping
- Database integration
- DOI assignment for citations
- Manual and automated publishing
- Hosted by GBIF nodes and the Secretariat

## Technical Infrastructure

### Technologies

- **Distributed Occurrence Indexing** - Elasticsearch for rapid search
- **REST API** - Stable v1 API (backwards compatible)
- **Cloud Infrastructure** - AWS and Microsoft Azure mirror datasets
- **Mapping** - Vector tile and raster tile generation
- **Backbone Taxonomy** - Merged taxonomy from multiple sources

### Standards and Frameworks

- **Darwin Core** - International biodiversity standard
- **Darwin Core Backbone Taxonomy** - Authoritative taxonomy source
- **Data Quality Framework** - Dataset type-specific quality requirements
- **ISO 19115** - Geographic information metadata

## Key Features

### Global Data Integration

- Real-time indexing of new datasets
- Common search interface across 81,000+ datasets
- Registry system for standardized discoverability
- Cross-institutional occurrence linking

### Advanced Query Capabilities

- Darwin Core field-based filtering
- Geographic/spatial queries
- Temporal range queries
- Complex boolean searches
- Taxonomic name resolution
- License-based filtering

### Data Accessibility

- Multiple access methods (web, API, downloads)
- Client libraries in multiple languages (Python, R, Ruby, PHP)
- Cloud-hosted datasets (AWS, Azure)
- Open data registry participation

### Research Support

- Citation support with DOIs
- Data quality metrics
- Download statistics
- Academic and conservation institution partnerships

## Use Cases and Applications

### Research Applications

**Climate Change & Biogeography** (31% of literature)
- Species distribution modeling under climate scenarios
- Tropical forest climate resilience assessment
- Invasive species climate interaction modeling
- Phylogeographic analysis

**Conservation & Extinction Risk** (significant portion of IUCN Red List)
- Create species range maps
- Threat assessment and extinction risk evaluation
- Conservation priority setting
- Protected area planning

**Invasive Species Management**
- Model spread potential
- Risk assessment for policy makers
- Prevention and control strategy development
- Early detection support

**Agriculture & Food Security**
- Wild crop relative identification
- Crop cultivation suitability assessment
- Biofuel crop distribution analysis
- Agrobiodiversity characterization

### Applied Uses

- Local and national agency decision support
- Species discovery and taxonomy
- Environmental monitoring and assessment
- Ecosystem research and understanding
- Biodiversity synthesis and analysis
- Trait-evolution and biogeographic studies

### Policy & Governance

- **IPCC Reports** - Data used in climate assessment reports
- **IPBES Reports** - Biodiversity assessments for policy makers
- **IUCN Red List** - Supporting extinction risk assessments for thousands of species
- **National Strategies** - Support for biodiversity planning and conservation policy
- **Environmental Regulation** - Informing environmental impact assessments

## Client Libraries and Tools

**Python:**
- pygbif - Official Python client library
- Programmatic API access

**R:**
- rgbif - Official R client library
- Integration with R statistical ecosystem

**Other Languages:**
- Ruby (gbifrb)
- PHP (php-gbif)
- JavaScript/Node.js clients
- Shell/curl examples

## Funding and Support

### Organizational Structure

**Voting Members:**
- Governments making financial contributions
- Governing Board meets annually in Participant countries

**Hosting:**
- The Natural History Museum of Denmark
- Secretariat Location: Copenhagen, Denmark

**Support Teams:**
- Participation and Engagement (GBIF network support)
- Data Products (quality and scientific value)

### International Recognition

- **10,000+ scientific papers** enabled by GBIF-mediated data
- **~34 papers per week** published using GBIF data (2023 average)
- **4,000+ research papers** cite iNaturalist observations on GBIF
- Integral to international biodiversity assessments

## Citation and Usage

Global Biodiversity Information Facility data is freely available with mixed Creative Commons licenses. When using GBIF data in research or applications, proper attribution and citation are essential.

### Recommended Citation

For GBIF portal:
"GBIF.org (year of access). Global Biodiversity Information Facility. Available at: https://www.gbif.org"

For specific downloads:
"GBIF (year). Dataset name. https://doi.org/[download DOI]"

For the IPT paper:
"Robertson et al. (2014). The GBIF Integrated Publishing Toolkit: Facilitating the Efficient Publishing of Biodiversity Data on the Internet. PLOS ONE 9(12): e102623. https://doi.org/10.1371/journal.pone.0102623"

### Additional Resources

- **Main Website**: https://www.gbif.org
- **Technical Documentation**: https://techdocs.gbif.org
- **API Documentation**: https://techdocs.gbif.org/en/openapi/
- **IPT Manual**: https://ipt.gbif.org/manual
- **Contact Form**: https://www.gbif.org/contact-us
- **GitHub Organization**: https://github.com/gbif

GBIF continues to grow as a critical infrastructure for global biodiversity data, supporting research, conservation, and sustainable development worldwide through open access to the world's biodiversity knowledge.