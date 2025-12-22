---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.naturalis.nl/"
    id: "naturalis"
    label: "Naturalis Biodiversity Center"
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.inhs.illinois.edu/"
    id: "inhs"
    label: "Illinois Natural History Survey"
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.gbif.org/"
    id: "gbif"
    label: "Global Biodiversity Information Facility (GBIF)"
creation_date: '2025-12-20T00:00:00Z'
description: Catalogue of Life is the most comprehensive global taxonomic resource providing an authoritative checklist of all known species on Earth. It aggregates 2.2+ million living species and 153,000 extinct species from 165 peer-reviewed taxonomic databases representing 500+ expert taxonomists. It serves as the foundational taxonomic backbone for biodiversity research, conservation policy, and species identification worldwide, with both static annual releases and dynamic monthly updates.
domains: []
homepage_url: https://www.catalogueoflife.org/
id: "catalogue-of-life"
infores_id: "catalogue-of-life"
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: "CC-BY 4.0 (transitioning to CC-0)"
name: Catalogue of Life
products:
  - category: GraphicalInterface
    description: Interactive web portal for browsing hierarchical taxonomy from kingdom level through infraspecific ranks with expandable taxonomy tree and full-text search for species names and synonyms
    format: http
    id: "catalogue-of-life.web"
    is_public: true
    name: Catalogue of Life Web Portal
    product_url: "https://www.catalogueoflife.org/"
  - category: ProgrammingInterface
    description: RESTful JSON API providing programmatic access to species information, taxonomic names, classification hierarchies, and species identifiers with multiple endpoints
    format: http
    id: "catalogue-of-life.api"
    is_public: true
    name: Catalogue of Life API
    product_url: "https://api.catalogueoflife.org/"
  - category: Product
    description: Annual comprehensive Catalogue of Life releases (Base Release with expert curation and Extended Release with broader source integration) with permanent archiving and DOI assignment
    id: "catalogue-of-life.annual-releases"
    name: Annual Releases
    product_url: "https://www.catalogueoflife.org/"
  - category: Product
    description: Downloadable Catalogue of Life datasets in multiple standardized formats including Catalogue of Life Data Package (ColDP), Darwin Core Archive, ACEF, TextTree, and MySQL dumps
    id: "catalogue-of-life.downloads"
    name: Data Downloads
    product_url: "https://www.catalogueoflife.org/data/download"
  - category: Product
    description: ChecklistBank repository infrastructure for publishing, discovery, and management of taxonomic datasets with data standardization to ColDP format and quality control workflows
    id: "catalogue-of-life.checklistbank"
    name: ChecklistBank Repository
    product_url: "https://checklistbank.org/"
  - category: DocumentationProduct
    description: Comprehensive documentation including API specifications, data format standards (ColDP, DwC-A), usage guides, citation guidelines, and taxonomic contribution workflows
    format: http
    id: "catalogue-of-life.documentation"
    is_public: true
    name: Catalogue of Life Documentation
    product_url: "https://api.catalogueoflife.org/"
publications:
  - authors:
      - Bisby F
      - Roskov Y
      - Culham A
    doi: "10.1186/1471-2105-12-447"
    id: "doi:10.1186/1471-2105-12-447"
    journal: "BMC Bioinformatics"
    title: "Catalogue of Life — Relational Database Design and Implementation"
    year: "2011"
  - authors:
      - Rueda M
      - Hawkins BA
      - Moreno-Salas L
      - et al.
    doi: "10.1371/journal.pbio.2005053"
    id: "doi:10.1371/journal.pbio.2005053"
    journal: "PLOS Biology"
    title: "Species richness matches productivity in grassland and forest plots across the Americas"
    year: "2017"
repository: "https://github.com/CatalogueOfLife"
synonyms:
  - Catalogue of Life
  - CoL
  - Species 2000/ITIS
  - Catalogue of Life Checklist
taxon:
  - "NCBITaxon:1"
---

# Catalogue of Life

## Overview

The Catalogue of Life (CoL) is the most comprehensive global taxonomic resource, serving as the authoritative checklist of all known species on Earth. Built and maintained by a global consortium of 500+ taxonomic experts from 165 peer-reviewed taxonomic databases, it provides the foundational taxonomic backbone for biodiversity research, conservation, species identification, and environmental policy worldwide.

Since its creation in 2001 as a partnership between Species 2000 and ITIS, the Catalogue of Life has evolved into an essential infrastructure resource supporting major international biodiversity initiatives including IUCN Red List assessments, Convention on Biological Diversity implementation, and GBIF (Global Biodiversity Information Facility) operations. As of 2025, it documents 2.2+ million living species and 153,000 extinct species through integration of 59,668 global, regional, and specialist data sources.

## Data Content and Scale

### Species Coverage

**Catalogue of Life 2025 (Latest Release):**
- **2,238,246 living (extant) species** - Comprehensive global inventory
- **~153,000 extinct species** - Historical and paleontological data
- **5.9+ million scientific names** - Including accepted names, synonyms, and common names
- **59,668 data sources** - Global, regional, national, and specialized checklists
- **165 peer-reviewed taxonomic databases** - From specialist institutions worldwide

**Year-over-Year Growth:**
- **2% increase** in total names from previous year
- **48,766 newly accepted species names** added in 2025 release
- Continuous expansion reflecting ongoing taxonomic discovery and research

### Taxonomic Coverage by Kingdom

Catalogue of Life provides comprehensive coverage across all major organism groups:

**Animalia (Animals):**
- Vertebrates: fish, amphibians, reptiles, birds, mammals (~95% coverage)
- Arthropods: insects, arachnids, crustaceans
- Mollusks, echinoderms, cnidarians, sponges
- Other invertebrate phyla
- Coverage estimated at 95%+ for described vertebrates

**Plantae (Plants):**
- Vascular plants: flowering plants, ferns, gymnosperms (~95% coverage)
- Mosses, liverworts, hornworts
- Green and red algae
- Coverage estimated at 95%+ for described vascular plants

**Fungi:**
- Ascomycetes and basidiomycetes
- Other fungal groups
- Moderate coverage with ongoing expansion

**Chromista & other protists:**
- Algae-like organisms
- Marine protists
- Diatoms and other microalgae

**Bacteria & Archaea:**
- Prokaryotic organisms
- Lower coverage due to rapid discovery rates
- Expanding through specialist databases

**Protozoa:**
- Protist coverage expanding through integration of specialist resources

### Coverage Quality Assessment

**Well-Documented Groups (>95% coverage):**
- Vertebrates (mammals, birds, reptiles, amphibians, fish)
- Vascular plants (flowering plants, ferns, gymnosperms)
- Major arthropod orders
- Well-studied invertebrate groups

**Moderately Documented Groups:**
- Many marine organisms
- Fungal species
- Microorganisms

**Underrepresented Groups:**
- Many arthropod groups (nematodes, mites, parasitoids)
- Microorganisms (bacteria, archaea)
- Deep-sea organisms
- Undiscovered and poorly-documented taxa

## Data Sources and Integration

### Integration Model

The Catalogue operates through ChecklistBank, a sophisticated data repository infrastructure that ingests diverse taxonomic data sources in multiple formats and standardizes them into consistent data models.

### Contributing Databases

**Peer-Reviewed Taxonomic Databases:**
165 major global, regional, and thematic taxonomic databases representing specialist institutions worldwide, including:
- ITIS (Integrated Taxonomic Information System)
- World Flora Online
- Species Files Group databases
- World Register of Marine Species (WoRMS)
- Fauna Europaea
- Regional and national taxonomic authorities

**Data Source Diversity:**
- 59,668 total checklists and data sources
- Global databases for major organism groups
- Regional taxonomic compilations
- Specialist databases for specific taxa
- Museum specimen records
- Literature-derived taxonomic information

### Data Integration Pipeline

**Processing Workflow:**
1. Raw data ingestion from diverse sources in various formats
2. Conversion and standardization to Catalogue of Life Data Package (ColDP) format
3. Quality control and validation processes
4. Expert verification for Base Release (annual)
5. Programmatic integration for Extended Release
6. Publication via ChecklistBank and COL portals
7. DOI assignment and version control

**Quality Assurance:**
- Expert peer review for Base Release accuracy
- Automated validation and consistency checking
- Verification by 500+ global taxonomic specialists
- Citation tracking and reference linkage
- Version control and archival

## Data Access Methods

### Web Portal Interface

**Catalogue of Life Website:** https://www.catalogueoflife.org/
- Interactive hierarchical taxonomy browser starting from kingdom level
- Expandable taxonomy tree for visual exploration of classification
- Full-text search for species names, synonyms, and common names
- Multi-language support for common names
- Direct access to taxonomic relationships and parent-child linkages
- Free, public access without registration

### Application Programming Interfaces

**Primary API:** https://api.catalogueoflife.org/
- RESTful JSON-based API
- Multiple endpoints for different data queries
- Programmatic species lookup
- Taxonomic hierarchy navigation
- Synonym and common name searching
- Authentication via GBIF user accounts
- Documentation and examples provided

**ChecklistBank API:** http://webservice.catalogueoflife.org/
- Access to underlying checklist data
- Complex query support
- JSON responses
- Integration-ready for external applications

### Data Download Options

**Download Portal:** https://www.catalogueoflife.org/data/download

**Supported Formats:**
- **Catalogue of Life Data Package (ColDP)** - Recommended for data exchange
  - Tabular CSV/TSV format with metadata
  - Based on Frictionless Data principles
  - Specific support for taxonomic relationships
  - ZIP file structure

- **Darwin Core Archive (DwC-A)** - For compatibility with biodiversity systems
  - Star schema with core table
  - Metadata and EML documentation
  - Integration with GBIF and other biodiversity portals

- **Annual Checklist Exchange Format (ACEF)** - Legacy format
  - Text-based format for taxonomic data
  - Supported for compatibility

- **TextTree Format** - Simple hierarchy representation
  - Human-readable text format
  - Parent-child relationships

- **MySQL Database Dumps** - For technical users
  - Complete database structure
  - For local deployment and analysis

**Download Flexibility:**
- Complete Catalogue or specific taxonomic subtrees
- Kingdom-specific extracts
- Region-specific subsets
- Partial downloads with root taxon specification
- Historical versions from 2019 onward

### Release Management

**Release Types and Schedules:**

1. **Annual Releases:**
   - Full annual version released yearly (most recent: July 2025)
   - Base Release: Expert-curated, non-overlapping checklists emphasizing accuracy
   - Extended Release (COL XR): Broader coverage incorporating ~60,000 sources
   - Long-term archival with permanent DOI

2. **Monthly Updates:**
   - Regular releases between annual versions
   - Continuous improvements and updates
   - Maintained in ChecklistBank for approximately one year
   - Not guaranteed permanent archival

3. **Version Control:**
   - Unique DOI for every release (complete catalogue and individual checklists)
   - Individual species names have unique identifiers
   - Citation tracking and attribution

## Data Standards and Formats

### Catalogue of Life Data Package (ColDP)

**Primary Exchange Format:**
- Tabular CSV or tab-separated values (TSV)
- ZIP file structure with metadata
- Specifically designed for taxonomic data
- Based on Frictionless Data principles
- Overcomes limitations of Darwin Core Archive for taxonomy

**ColDP Components:**
- Three core object types: taxa, names, and references
- Support for accepted names and synonyms
- Nomenclatural status tracking
- Taxonomic rank designation
- Parent-child relationship definition
- Author and year attribution
- Literature citations (BibTeX and CSL-JSON)
- Common names in multiple languages

**Data Fields:**
- Taxon identifiers (taxonID)
- Scientific names
- Authorship information
- Nomenclatural status (accepted, synonym, etc.)
- Taxonomic rank (Kingdom through subspecies)
- Parent taxon reference
- Literature citations and references
- Common names (multiple languages)

### Taxonomic Standards

**Linnaean Classification:**
- Hierarchical ranks from domain (or superkingdom) to infraspecific levels
- Standard ranks: Kingdom, Phylum, Class, Order, Family, Genus, Species
- Infraspecific ranks: Subspecies and other sub-specific categories
- Support for non-standard ranks where needed

**Name Management:**
- Standardized scientific nomenclature
- Synonym tracking and linking
- Common names in multiple languages
- Literature citations for all names
- Full nomenclatural history

**Relationship to Darwin Core:**
- ColDP developed to overcome DwC-A limitations for taxonomy
- Compatible with Darwin Core terminology where applicable
- More intuitive for taxonomic specialists
- Better support for complex relationships

### Version Control and Citation

- Every release receives unique DOI identifier
- Every contributing checklist has its own DOI
- Individual species can be cited with specific identifiers
- Version history maintained and accessible
- Recommended for scholarly publications

## Technical Architecture

### Hosting and Infrastructure

**Administrative Host:** Global Biodiversity Information Facility (GBIF) Secretariat
- Primary institutional support as of January 2024
- Infrastructure and administrative services
- Long-term preservation and archival

**Co-Chair Institutions:**
- **Naturalis Biodiversity Center** (Leiden, Netherlands) - Operations and coordination
- **Illinois Natural History Survey** (Champaign-Urbana, USA) - Operations and technical support

**Physical Infrastructure:**
- Hosted on GBIF infrastructure
- Designed for global-scale access
- Scalable architecture supporting millions of species records
- High availability and reliability

### Technical Stack

**Backend Architecture:**
- **Framework:** Dropwizard Java application
- **Build System:** Maven-based modular structure
- **API Technology:** Shaded JARs using Dropwizard framework
- **Database:** Support for various backend databases
- **APIs:** RESTful JSON-based web services

**Software Components:**

1. **ChecklistBank System:**
   - Central repository for taxonomic datasets
   - Data standardization and validation
   - Publication and discovery platform
   - GitHub: github.com/CatalogueOfLife/checklistbank

2. **Backend Application:**
   - Core application logic
   - API generation and exposure
   - Data processing pipeline
   - GitHub: github.com/CatalogueOfLife/backend

3. **Data Format Specification:**
   - ColDP format documentation
   - Validation tools and schemas
   - GitHub: github.com/CatalogueOfLife/coldp

**Data Processing Pipeline:**
1. Raw checklist ingestion from diverse sources
2. Format standardization to ColDP
3. Quality control and validation
4. Expert review (for Base Release)
5. Programmatic integration (for Extended Release)
6. Publication via APIs and download services
7. DOI assignment and archival

## Use Cases and Applications

### Research Applications

**Taxonomy and Systematics:**
- Foundational reference for phylogenetic studies
- Standardized taxonomic nomenclature verification
- Species identification and classification
- Biodiversity inventory and assessment
- Comparative biology and systematics research

**Biodiversity Modeling:**
- Species richness estimation and comparison
- Habitat distribution prediction
- Ecological pattern analysis
- Extinction risk and threat modeling
- Biogeographic studies

**Genomic and Molecular Research:**
- Integration with DNA barcode databases (BOLD)
- Genomic data linking to taxonomic classification
- Molecular species identification
- Standardization for metabarcoding studies

### Conservation Applications

**IUCN Red List Integration:**
- Taxonomic reference for 172,000+ assessed species
- Species nomenclature standardization
- Threat assessment consistency
- Conservation priority identification

**Conservation Planning:**
- Species distribution mapping
- Biodiversity hotspot identification
- Habitat assessment and monitoring
- Protected area planning and evaluation
- Invasive species tracking

**Policy Implementation:**
- Convention on Biological Diversity (CBD) support
- Convention on International Trade in Endangered Species (CITES) enforcement
- Convention on Migratory Species (CMS) compliance
- IPBES (Biodiversity and Ecosystem Services) assessments
- Kunming-Montreal Global Biodiversity Framework implementation

### Data Integration Applications

**Global Biodiversity Platforms:**
- GBIF (Global Biodiversity Information Facility) - Backbone taxonomy
- Encyclopedia of Life (EOL) - Species information synthesis
- Biodiversity Heritage Library - Literature integration
- National and regional biodiversity portals

**Collection Management:**
- Museum specimen cataloging and standardization
- Herbarium organization and classification
- Taxonomic standards for institutional collections

**Environmental Management:**
- Government species regulation and enforcement
- Environmental impact assessments
- Biosecurity and quarantine applications
- Regulatory compliance with trade agreements

**Educational and Citizen Science:**
- Species identification tools and guides
- Biodiversity education and training
- Standardization for crowdsourced observations
- Public engagement in taxonomy and biodiversity

## Organizational Structure

### Governance

**Core Leadership:**
- **Naturalis Biodiversity Center** (Leiden, Netherlands) - Co-chair and operational coordination
- **Illinois Natural History Survey** (Champaign-Urbana, USA) - Co-chair and technical support
- **GBIF Secretariat** - Administrative host (as of 2024)

**Expert Community:**
- Over 500 global taxonomic experts
- Hundreds of specialist database contributors
- Expert committees for major organism groups
- Peer review for Base Release curation

**Contributing Institutions:**
- 165 peer-reviewed taxonomic database organizations
- Specialist institutions worldwide
- Regional taxonomic authorities
- University-based taxonomy programs

### Founding Organization: Species 2000

**History and Mission:**
- Created in 1997 by Frank Bisby and colleagues (University of Reading, UK)
- Consortium of taxonomic database organizations
- Parent organization that created Catalogue of Life (2001)
- Oversees COL strategic direction and governance

**Related Organizations:**
- **LifeWatch** - European research infrastructure partner
- **Smithsonian Institution** - Supporting organization
- **Chinese Academy of Sciences** - Supporting organization

## Maintenance and Development Status

### Active Development and Updates

**Release Cycle:**
- Annual comprehensive releases (most recent: July 2025)
- Monthly intermediate releases throughout the year
- Continuous data updates and improvements
- Regular quality assurance processes

**Current Version (2025):**
- Released: July 9, 2025
- 2,238,246 living species + 153,000 extinct species
- 5.9+ million scientific names
- 48,766 newly accepted species added

**Infrastructure Status:**
- Fully operational since December 2020
- Actively maintained with regular updates
- High availability and global accessibility
- Scalable to support growing species databases

### Future Development

- Continued transition toward open data licenses (CC-0, CC-BY)
- Expansion of API capabilities
- Increased integration with global biodiversity platforms
- Focus on completeness in underrepresented organism groups
- Development of advanced taxonomic name services
- Support for Kunming-Montreal Global Biodiversity Framework implementation

## Standards and Interoperability

- **Linnaean Taxonomy** - Hierarchical classification standard
- **Darwin Core** - Biodiversity data standard
- **Linked Data Principles** - Semantic interoperability
- **Open Data Standards** - FAIR (Findable, Accessible, Interoperable, Reusable)
- **Creative Commons Licensing** - Open science principles

## Citation and Usage

Catalogue of Life data and services are freely accessible with open licensing encouraging maximum reuse for research, conservation, and educational purposes.

### Recommended Citation

**For Complete Catalogue:**
"Catalogue of Life (2025). Available at: https://www.catalogueoflife.org/"

**With DOI:**
"Catalogue of Life 2025 annual release [version], released 2025-07-09. Digital Object Identifier: [DOI]"

**Three-Level Attribution:**
- Credit to complete Catalogue of Life work
- Credit to contributing database/checklist
- Credit to taxonomic expert providing verification

### Additional Resources

- **Main Website:** https://www.catalogueoflife.org/
- **API Documentation:** https://api.catalogueoflife.org/
- **ChecklistBank Repository:** https://checklistbank.org/
- **Data Downloads:** https://www.catalogueoflife.org/data/download
- **GitHub Organization:** https://github.com/CatalogueOfLife
- **Citation Guidelines:** https://www.catalogueoflife.org/howto/cite
- **Data Usage Policy:** https://www.catalogueoflife.org/about/colusage
- **Naturalis Biodiversity Center:** https://www.naturalis.nl/
- **Illinois Natural History Survey:** https://www.inhs.illinois.edu/
- **GBIF Secretariat:** https://www.gbif.org/

Catalogue of Life continues to serve as the global standard for species taxonomy and nomenclature, providing essential infrastructure for biodiversity research, conservation decision-making, and the implementation of international agreements to protect Earth's biological diversity.
