---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.ioc.unesco.org/"
      - contact_type: email
        value: "obis@vliz.be"
    id: "UNESCO-IOC"
    label: "UNESCO Intergovernmental Oceanographic Commission (IOC)"
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.vliz.be/"
    id: "vliz"
    label: "Flanders Marine Institute (VLIZ)"
creation_date: '2025-12-18T00:00:00Z'
description: Ocean Biodiversity Information System (OBIS) is a global open-access data and information system providing free access to information about the distribution and abundance of living species in the ocean. It aggregates 161 million biodiversity records covering 160,000+ marine species from 600+ institutions across 56+ countries, using Darwin Core standards and World Register of Marine Species (WoRMS) as the authoritative taxonomic backbone.
domains: []
homepage_url: https://obis.org/
id: "obis"
infores_id: "obis"
layout: resource_detail
license:
  id: "https://creativecommons.org/publicdomain/zero/1.0/"
  label: "CC0, CC BY, and CC BY-NC (mixed)"
name: Ocean Biodiversity Information System (OBIS)
products:
  - category: GraphicalInterface
    description: Interactive web mapper for searching, filtering, and visualizing marine species distributions across geographic areas, depth ranges, and time periods with multi-parameter search capabilities
    format: http
    id: "obis.mapper"
    name: OBIS Web Mapper
    product_url: "https://portal.obis.org/"
  - category: ProgrammingInterface
    description: RESTful API providing programmatic access to marine biodiversity records, species information, and occurrence data with filtering by taxonomy, location, depth, and time
    format: http
    id: "obis.api"
    is_public: true
    name: OBIS API
    product_url: "https://api.obis.org/"
  - category: ProgrammingInterface
    description: R package robis for programmatic data access and querying of OBIS data from R environment
    format: http
    id: "obis.robis"
    is_public: true
    name: robis R Package
    product_url: "https://cran.r-project.org/web/packages/robis/"
  - category: Product
    description: Complete biodiversity record exports in Darwin Core Archive format containing occurrence data with standardized metadata and EML documentation
    id: "obis.dca"
    name: OBIS Darwin Core Archive Downloads
    product_url: "https://portal.obis.org/"
  - category: Product
    description: Cloud-native GeoParquet format biodiversity records available on AWS S3 for efficient large-scale spatial analysis without local downloads
    id: "obis.geoparquet"
    name: OBIS GeoParquet on AWS
    product_url: "https://registry.opendata.aws/obis/"
  - category: Product
    description: OBIS-SEAMAP specialized database for marine megavertebrates containing distribution, abundance, and telemetry data for marine mammals, seabirds, and sea turtles
    id: "obis.seamap"
    name: OBIS-SEAMAP Marine Megavertebrates Database
    product_url: "https://seamap.env.duke.edu/"
  - category: DocumentationProduct
    description: Comprehensive OBIS manual covering data standards, quality control procedures, Darwin Core implementation, publication guidelines, and API usage documentation
    format: http
    id: "obis.manual"
    is_public: true
    name: OBIS Manual
    product_url: "https://manual.obis.org/"
publications:
  - authors:
      - OBIS Contributors
    id: "obis-data"
    title: "Ocean Biodiversity Information System - Global Marine Biodiversity Dataset"
    year: "2025"
repository: "https://github.com/iobis/"
taxon:
  - "NCBITaxon:2157"
  - "NCBITaxon:2158"
  - "NCBITaxon:2159"
---

# Ocean Biodiversity Information System (OBIS)

## Overview

The Ocean Biodiversity Information System (OBIS) is the first global open-access data and information system dedicated to marine biodiversity. Established in 2001 as the information management component of the Census of Marine Life and formally adopted as a project of UNESCO's Intergovernmental Oceanographic Commission (IOC) in June 2009, OBIS provides anyone, anywhere with free access to information about the distribution and abundance of living species in the ocean.

OBIS operates as a collaborative alliance of 27 regional, national, and thematic nodes representing 600+ institutions across 56+ countries, all working to facilitate integrated, standardized access to marine biodiversity data. It serves as the foundation for understanding global marine species distributions, ecosystem health, and ocean conservation priorities.

## Data Content and Scale

### Overall Scale

OBIS represents the most comprehensive aggregation of marine biodiversity data available globally:

- **161 million biodiversity records** - Occurrence, distribution, and abundance data for marine organisms
- **160,000+ marine species covered** - Comprehensive global marine biodiversity representation
- **27 million DNA sequences** - eDNA metabarcoding and molecular data (51 eDNA datasets with 19.8 million records)
- **600+ institutions** - Contributing data from research institutions, museums, government agencies, and citizen science networks
- **56+ countries** - Geographic representation from tropics to poles
- **Depth range**: Surface waters to 10,900 meters (hadal zone)
- **93,106 marine species documented within Marine Protected Areas**

### Growth and Impact

- **Continuous growth**: Daily addition of new occurrence data from contributing institutions
- **UN World Ocean Assessment**: Three chapters of the first UN World Ocean Assessment utilized OBIS data
- **Expanding DNA data**: 51 publicly available eDNA datasets representing 5,226 species
- **OBIS-SEAMAP**: 1,526 datasets covering over 700 marine megavertebrate species (mammals, birds, turtles)

### Taxonomic Coverage

OBIS provides comprehensive coverage of all organisms with association to marine or estuarine environments:

- **Bacteria and Archaea** - Marine microorganisms and prokaryotic diversity
- **Protists** - Marine protistan organisms and dinoflagellates
- **Fungi** - Marine fungal species
- **Plants** - Marine algae, seagrasses, and marine vegetation
- **Animals** - Complete marine animal diversity:
  - Invertebrates (crustaceans, mollusks, echinoderms, cnidarians, sponges)
  - Fish species (all marine fish groups)
  - Marine mammals (whales, dolphins, seals, sea lions, manatees)
  - Seabirds (cormorants, penguins, albatrosses)
  - Sea turtles and marine reptiles

## Data Access and Formats

### Interactive Web Portal

**OBIS Web Mapper** (https://portal.obis.org/)
- Interactive mapping interface with multiple visualization layers
- Multi-parameter search capabilities:
  - By species name or higher taxonomic levels
  - By geographic area (using interactive map)
  - By depth range (surface to 10,900 meters)
  - By time period and observation date
  - By environmental parameters
  - By data quality metrics
- Filtering by OBIS nodes, institutions, and data providers
- Export of filtered results in CSV format
- Layered visualization for combined analysis
- Species distribution mapping across spatial and temporal scales

### Programmatic Access via APIs

**OBIS RESTful API** (https://api.obis.org/)
- Programmatic access to marine biodiversity records
- Query capabilities:
  - Species occurrence data filtering
  - Taxonomic queries with WoRMS validation
  - Geographic/spatial queries
  - Depth-based filtering
  - Temporal range queries
- JSON response format
- Integration with GBIF systems
- Documentation and interactive documentation available

**robis R Package**
- Official R interface to OBIS API
- Facilitates programmatic data access from R environment
- Species search and filtering functions
- Data export using standard R functions (write.csv)
- Integrated workflow for biodiversity research in R

### Data Formats

**Primary Standards:**
- **Darwin Core** - International standard for biodiversity data
- **Darwin Core Archive (DwC-A)** - Compressed ZIP containing:
  - `occurrence.txt` - Standardized occurrence records
  - `event.txt` - Event/sampling information (when applicable)
  - `eMoF.txt` - Extended Measurement or Facts (extended data)
  - `meta.xml` - Metadata describing file structure
  - EML (Ecological Metadata Language) - Comprehensive metadata documentation
- **CSV** - Comma-separated values for spreadsheet analysis
- **GeoParquet** - Cloud-native columnar format for efficient spatial analysis

### Bulk Download Options

**Darwin Core Archive**
- Complete dataset exports in standardized format
- Available through OBIS Web Mapper
- Enables offline analysis and archival
- Full version control and metadata preservation

**GeoParquet on AWS**
- Cloud-native format for large-scale analysis
- AWS Open Data Program integration
- Available at s3://obis-open-data/occurrence
- One file per source dataset for easy filtering
- Recommended for datasets >1GB
- Enables serverless, cloud-based analysis workflows
- No local download required for large-scale studies

**OBIS-SEAMAP Specialized Portal**
- Specialized database for marine megavertebrate data
- Includes georeferenced distribution data, abundance estimates, telemetry data
- Data from surveys, satellite telemetry, acoustic monitoring, Photo-ID
- Geographic and temporal filtering capabilities

## Data Processing and Quality

### Data Standardization Pipeline

OBIS processes all incoming data through a standardized workflow:

1. **Data Submission** - Via Integrated Publishing Toolkit (IPT) by GBIF
2. **Darwin Core Mapping** - Conversion to standard Darwin Core terms
3. **Initial Validation** - Verification of required fields and data types
4. **Taxonomic Standardization** - All species names matched against WoRMS

### Quality Control Mechanisms

**Taxonomic Processing:**
- Validation against World Register of Marine Species (WoRMS) - only authoritative source
- Automatic species name standardization and synonymy resolution
- Flagging and exclusion of non-marine species
- Taxonomic hierarchy verification
- 514,088 marine species names tracked; 247,418 valid marine species (98% verified)

**Data Quality Control - Three-Step Process:**

1. **Initial Automated Checks:**
   - Required field verification
   - Value range validation
   - Impossible value detection
   - Species name validation against WoRMS

2. **Systematic Automated Validation:**
   - Taxonomic consistency checking
   - Geographic impossibility detection
   - Temporal validity verification
   - Species identification inconsistency flagging

3. **Manual Review by Specialists:**
   - Human expert evaluation of high-value data
   - Species identification verification
   - Sampling methodology assessment
   - Metadata quality evaluation
   - Subtle error identification

**Community Feedback:**
- Users can provide peer review feedback
- Reports identify technical, geographic, and taxonomic errors
- Regular communication of discrepancies to data providers
- Systematic incorporation of corrections

### Compliance Standards

- **FAIR Principles** - Findable, Accessible, Interoperable, Reusable
- **CARE Principles** - Collective Benefit, Authority to Decide, Responsibility, Ethics
- **Transparent Attribution** - All data ownership and provenance clearly documented
- **Standardization Requirements** - All datasets must be standardized, traceable, and transparent

## Data Sources and Publishers

### Contributing Network

**27 OBIS Nodes** - Regional, national, and thematic nodes coordinating data:
- National OBIS nodes providing country-level marine biodiversity data
- Regional nodes coordinating multiple countries
- Thematic nodes focusing on specialized data types (eDNA, telemetry, etc.)

**600+ Contributing Institutions** Including:
- Research institutions and universities
- Natural history museums
- Government agencies and marine research centers
- Citizen science networks and observation platforms
- Environmental monitoring programs

**Data Types and Sources:**
- Survey and sampling event data with effort metadata
- Museum specimen records with historical data
- Telemetry and tracking data (satellite, acoustic monitoring)
- Photo-identification and individual tracking records
- eDNA metabarcoding and DNA sequence data
- Citizen science observations and monitoring data
- Remote sensing and acoustic monitoring data

### Publishing Infrastructure

**Integrated Publishing Toolkit (IPT):**
- Manages dataset publication and versioning
- Darwin Core term mapping and validation
- Metadata configuration and EML generation
- Database integration and automated publishing
- DOI assignment for data citations
- Integration with GBIF network

## Technical Infrastructure

### Technologies

- **Taxonomic Authority**: World Register of Marine Species (WoRMS) - exclusively used
- **Cloud Infrastructure**: AWS Open Data Program participation
- **Geospatial Format**: GeoParquet for efficient spatial analysis
- **Data Management**: Version control and distributed archival
- **API Infrastructure**: RESTful services with GBIF integration
- **Publishing System**: IPT (Integrated Publishing Toolkit) by GBIF

### Standards and Frameworks

- **Darwin Core** - International biodiversity data standard
- **World Register of Marine Species (WoRMS)** - Marine taxonomic authority
- **EML (Ecological Metadata Language)** - Metadata documentation
- **GeoSPARQL** - Geospatial semantic queries
- **FAIR Data Principles** - Open data standards

## Key Features

### Global Open Access

- Free access to all data for any user
- No registration required for basic searching and downloads
- Follows principles of equitable access and benefit sharing
- Preference for CC0 (most open) licenses
- Clear license requirements for users

### Comprehensive Species Coverage

- All marine and estuarine organisms included
- Global taxonomic coverage from bacteria to whales
- Spanning full depth range (0-10,900 meters)
- Temporal coverage from historical museum specimens to current observations

### Multi-Parameter Search and Discovery

- Query by species, taxonomy, geography, depth, and time
- Filter by data quality, institution, data provider, or OBIS node
- Combined layer visualization for comparative analysis
- Advanced spatial and temporal filtering

### Cloud-Native Data Access

- GeoParquet format for efficient cloud-based analysis
- AWS S3 direct access for large datasets
- Serverless analysis without local downloads
- Integration with cloud computing workflows

### Specialized Data Types

- eDNA metabarcoding and DNA sequence data (27 million sequences)
- Telemetry and tracking data (satellite, acoustic)
- Photo-identification and individual tracking
- Survey and abundance data
- Presence/absence records

### OBIS-SEAMAP Integration

- Specialized portal for marine megavertebrates
- 1,526 datasets covering 700+ mammal, bird, and turtle species
- Integrated distribution, abundance, and telemetry data
- Georeferenced observations with quality control

## Use Cases and Applications

### Conservation Applications

- **Species Distribution Modeling** - Endangered species recovery planning (Nassau Grouper, giant manta rays)
- **Marine Protected Area Design** - Identifying ocean areas with highest biodiversity
- **Conservation Priority Setting** - Directing limited conservation resources to high-value areas
- **Threat Assessment** - Risk evaluation for vulnerable marine species
- **Species Recovery Planning** - Supporting population management decisions

### Research Applications

- **Climate Change Impacts** - Predicting species distribution shifts under climate scenarios
- **Marine Connectivity** - Understanding species movement and population links
- **Ecosystem Modeling** - Projecting ecosystem change and biodiversity loss
- **Biogeographic Patterns** - Global species richness and diversity studies
- **Metabarcoding Validation** - Confirming eDNA species detection accuracy

### Ecosystem Monitoring

- **Species Distribution Changes** - Tracking temporal shifts in marine populations
- **Ecosystem Health Assessment** - Monitoring indicator species and communities
- **Recovery Capacity Evaluation** - Assessing ecological resilience to environmental change
- **Environmental Change Detection** - Identifying ecosystem-level biodiversity changes

### Policy and Governance

- **UN World Ocean Assessment** - Informing international policy decisions
- **Fisheries Management** - Supporting sustainable harvest estimates
- **Coastal Zone Management** - Guiding regional development and conservation
- **Marine Spatial Planning** - Informing ocean zoning and protection strategies
- **Policy-Relevant Research** - Providing evidence base for conservation policy

## Data Access Standards and Policy

### License and Access Policy

**Preferred License Order:**
1. **CC0** - Most permissive; waives all copyright; maximizes reuse potential
2. **CC BY** - Attribution required; enables open access with accountability
3. **CC BY-NC** - Non-commercial restrictions applied

**User Obligations:**
- Data must be clearly linked to license terms
- Attribution provided where required by license
- Users can build products based on OBIS data without cost when licenses allow
- Citations required for scholarly performance evaluation

### Citation Requirements

- All use of OBIS data, products, software, and workflows must be properly cited
- Citation practices tracked in OBIS publications library (obis.org/library/)
- Dataset citations recognized as scholarly metrics
- Important for demonstrating project impact and securing funding

## Organizational Structure and Governance

### Governance

- **Adopting Organization**: UNESCO Intergovernmental Oceanographic Commission (IOC)
- **Programme**: International Oceanographic Data and Information Exchange (IODE)
- **OBIS Steering Group (SG-OBIS)**: Strategic oversight and direction
- **OBIS Executive Committee (OBIS-EC)**: Operational decision-making
- **OBIS Task Teams**: Specialized working groups for specific functions

### Operational Support

- **Host Institution**: Flanders Marine Institute (VLIZ), Oostende, Belgium
- **Secretariat Location**: UNESCO/IOC Project Office for IODE, Belgium
- **Technical Support**: Managed by VLIZ

### International Network

- **27 OBIS Nodes** - Regional, national, and thematic data coordination
- **600+ Institutions** - Contributing data and expertise
- **56+ Countries** - Geographic representation and participation

## Citation and Usage

Ocean Biodiversity Information System data is freely available with mixed Creative Commons licenses (CC0, CC BY, CC BY-NC). When using OBIS data in research, applications, or conservation efforts, proper attribution and citation are essential.

### Recommended Citation

For OBIS as a data source:
"Ocean Biodiversity Information System (OBIS). Available at: https://obis.org"

For specific dataset downloads:
"[Dataset Title]. Ocean Biodiversity Information System. Available at: https://portal.obis.org/"

For OBIS-SEAMAP:
"OBIS-SEAMAP. Marine Megavertebrate Database. Available at: https://seamap.env.duke.edu/"

### Additional Resources

- **Main Website**: https://obis.org/
- **OBIS Manual**: https://manual.obis.org/
- **OBIS Web Mapper**: https://portal.obis.org/
- **OBIS API Documentation**: https://api.obis.org/
- **OBIS on GitHub**: https://github.com/iobis/
- **OBIS-SEAMAP**: https://seamap.env.duke.edu/
- **Contact Information**: obis@vliz.be
- **World Register of Marine Species (WoRMS)**: https://www.marinespecies.org/

OBIS continues to grow as a critical infrastructure for global marine biodiversity data, supporting conservation, research, and sustainable ocean management worldwide through open access to the world's marine biodiversity knowledge.
