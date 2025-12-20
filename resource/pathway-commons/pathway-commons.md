---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.mskcc.org/"
    id: "mskcc"
    label: "Memorial Sloan Kettering Cancer Center"
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.utoronto.ca/"
    id: "utoronto"
    label: "University of Toronto"
creation_date: '2025-12-20T00:00:00Z'
description: Pathway Commons is a centralized web resource that aggregates biological pathway and molecular interaction data from 22 major public databases into standardized BioPAX format. It provides 4,794 pathways and over 2.3 million molecular interactions accessible through multiple interfaces including web portal, REST API, and downloadable datasets, supporting systems biology research, pathway analysis, and network visualization.
domains:
  - pathways
  - systems biology
homepage_url: https://www.pathwaycommons.org/
id: "pathway-commons"
infores_id: "pathway-commons"
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/3.0/"
  label: "CC BY 3.0 (aggregated content)"
name: Pathway Commons
products:
  - category: ProgrammingInterface
    description: RESTful web service API for programmatic access to Pathway Commons data with multiple query capabilities including search, pathway retrieval, and network analysis
    format: http
    id: "pathway-commons.api"
    is_public: true
    name: Pathway Commons REST API
    product_url: "http://www.pathwaycommons.org/pc/webservice.do"
  - category: GraphicalInterface
    description: Interactive web-based interface for browsing, searching, and visualizing biological pathways and molecular interactions
    format: http
    id: "pathway-commons.web"
    is_public: true
    name: Pathway Commons Web Interface
    product_url: "https://www.pathwaycommons.org/"
  - category: Product
    description: Downloadable integrated pathway datasets in multiple standardized formats including BioPAX, SIF, GMT, and JSON-LD
    id: "pathway-commons.downloads"
    name: Pathway Commons Data Downloads
    product_url: "https://www.pathwaycommons.org/"
  - category: Product
    description: Integrated BioPAX Level 3 unified model containing normalized pathway data, molecular interactions, and cross-database entity mappings from 22 sources
    id: "pathway-commons.biopax"
    name: Integrated BioPAX Model
  - category: Product
    description: Simple Interaction Format (SIF) network files representing binary pairwise molecular relationships for network analysis and visualization
    id: "pathway-commons.sif"
    name: SIF Network Format
  - category: Product
    description: Gene Matrix Transposed (GMT) format gene sets for pathway enrichment analysis with tools like GSEA (Gene Set Enrichment Analysis)
    id: "pathway-commons.gmt"
    name: GMT Gene Set Format
  - category: Product
    description: JSON-LD format for linked data web applications with semantic context and programmatic access to pathway information
    id: "pathway-commons.jsonld"
    name: JSON-LD Linked Data Format
  - category: DocumentationProduct
    description: Comprehensive API documentation, data format specifications, and tutorials for using Pathway Commons data and services
    format: http
    id: "pathway-commons.documentation"
    is_public: true
    name: Pathway Commons Documentation
    product_url: "https://pathwaycommons.github.io/pcapi/"
publications:
  - authors:
      - Rodchenkov I
      - Babur O
      - Luna A
      - et al.
    doi: "10.1093/nar/gkz946"
    id: "doi:10.1093/nar/gkz946"
    journal: "Nucleic Acids Research"
    preferred: true
    title: "Pathway Commons 2019 Update: integration, analysis and exploration of pathway data"
    year: "2020"
  - authors:
      - Cerami EG
      - Gross BE
      - Demir E
      - et al.
    doi: "10.1093/nar/gkq1016"
    id: "doi:10.1093/nar/gkq1016"
    journal: "Nucleic Acids Research"
    title: "Pathway Commons, a web resource for biological pathway data"
    year: "2011"
  - authors:
      - Cerami E
      - Bader GD
      - Gross BE
      - Sander C
    doi: "10.1186/1471-2105-7-497"
    id: "doi:10.1186/1471-2105-7-497"
    journal: "BMC Bioinformatics"
    title: "cPath: open source software for collecting, storing, and querying biological pathways"
    year: "2006"
repository: "https://github.com/PathwayCommons"
synonyms:
  - Pathway Commons
  - PathwayCommons
  - PC
taxon:
  - "NCBITaxon:9606"
---

# Pathway Commons

## Overview

Pathway Commons is a centralized web resource that aggregates biological pathway and molecular interaction data from 22 major public databases into standardized BioPAX (Biological Pathway Exchange) format. The resource is dedicated to collecting, integrating, and disseminating publicly available information about biological pathways, molecular interactions, and gene regulation networks, making this critical data easily accessible to researchers worldwide.

Pathway Commons serves as a foundational infrastructure for systems biology research, enabling researchers to perform integrated pathway analysis, network visualization, and hypothesis generation across consolidated knowledge from the world's major pathway and interaction databases.

## Data Content and Scale

### Data Volume and Coverage

**Pathway Commons Version 11 (Released February 2019):**
- **4,794 biological pathways** - Increase from 1,477 in initial release
- **2.3+ million molecular interactions** - Increase from 687,883 in original version
- **18,490 genes** with HGNC (Human Gene Nomenclature Committee) identifiers
- **11,437 small molecules** with identifiers from ChEBI, HMDB, KEGG Compound, and DrugBank
- **22 integrated data sources** with continuous updates

### Integrated Data Types

Pathway Commons provides comprehensive coverage of:
- **Biochemical reactions and metabolic pathways**
- **Signaling pathways and signal transduction**
- **Molecular interactions:**
  - Protein-protein interactions
  - Protein-DNA interactions
  - Protein-small molecule interactions
  - RNA interactions
  - Biomolecular complex assembly
- **Post-translational modifications and protein states**
- **Gene regulatory networks**
- **Genetic interactions and dependencies**
- **Drug-target interactions**

### Primary Organism Focus

Pathway Commons **intentionally prioritizes human pathway data** from its partner databases. The resource specifies that it integrates pathway data only for explicitly supported species, with human as the primary focus. Additional organisms are included when they interact with human entities, but comprehensive curation is focused on supported species to maintain data quality and accuracy.

## Data Sources and Integration

### Integrated Databases

Pathway Commons consolidates data from **22 major public databases:**

**Core Interaction and Pathway Sources:**
- BioGRID (biological interactions)
- CORUM (protein complexes)
- CTD (Chemical-Gene interactions)
- DIP (Database of Interacting Proteins)
- DrugBank (drug information)
- HPRD (Human Protein Reference Database)
- HumanCyc (metabolic pathways)
- IntAct (molecular interactions)
- KEGG (metabolic and signaling pathways)
- MSKCC Cancer Cell Map (cancer pathways)
- MINT (Molecular Interaction Database)
- MirTarBase (miRNA targets)
- NCI/Nature PID (Pathway Interaction Database)
- PhosphoSitePlus (post-translational modifications)
- Reactome (human biochemical reactions)
- RECON (metabolic reconstruction)
- SBCNY IMID (cancer signaling)
- TRANSFAC (transcription factor data)

**Additional Linked Sources:**
- UniProt, Ensembl, GenBank, PubChem, PubMed, and others via cross-database references

### Data Processing Pipeline

**Integration Workflow:**
1. Download BioPAX or PSI-MI files from data providers
2. Validation and normalization of data
3. Cross-database entity mapping using centralized registry
4. Merging into unified BioPAX Level 3 model
5. Reference object consolidation for identical interactors
6. Quality assurance and consistency checking

**Identifier Mapping:**
- Canonical molecule representation
- Cross-database entity linking
- HGNC gene identifiers
- ChEBI, HMDB, KEGG Compound, and DrugBank chemical identifiers
- Automated IRI generation for consistent entity references

## Data Access Methods

### Web Interface

**Pathway Commons Portal:** https://www.pathwaycommons.org/
- Interactive browsing of pathways and interactions
- Full-text keyword search
- Pathway visualization
- Gene and protein neighborhood discovery
- Interactive network exploration
- Data filtering and export capabilities

### RESTful Web Service API

**API Endpoint:** http://www.pathwaycommons.org/pc/webservice.do
**API Documentation:** https://pathwaycommons.github.io/pcapi/

**Core API Capabilities:**
- Full-text keyword search
- Pathway retrieval and querying
- Network neighbor discovery (immediate and multi-step)
- Entity parents and relationships
- XPath-like data access patterns
- Advanced graph pattern searching
- Result format conversion on-the-fly

**Supported Query Commands:**
- `search` - Full-text and structured search
- `get_pathways` - Retrieve pathway information
- `get_neighbors` - Find connected entities in networks
- `get_parents` - Navigate entity hierarchy
- `get_record_by_cpath_id` - Direct entity retrieval

**Result Formats:**
- BioPAX (complete data)
- SIF (network format)
- Extended SIF (with attributes)
- JSON (for web applications)
- JSON-LD (linked data)

### Data Download Services

**Download Portal:** https://www.pathwaycommons.org/
- Bulk dataset downloads in multiple formats
- Version-controlled releases
- Compressed files for efficient transfer
- Complete BioPAX models
- Gene set collections

### Software Libraries and Integration Tools

**Programmatic Access Libraries:**
- **Paxtools (Java)** - Core library for BioPAX object models and manipulation
- **paxtoolsr (R/Bioconductor)** - R interface to Paxtools
- **pybiopax (Python)** - Python library for BioPAX data manipulation
- **Cytoscape plugins** - Direct Pathway Commons querying from Cytoscape

**Visualization and Analysis Tools:**
- **Cytoscape** - Network analysis and visualization (multiple apps available)
- **ChiBE** - Pathway visualization with genomics data overlay
- **PCViz** - Interactive network visualization
- **Enrichment Map** - Pathway enrichment visualization for GSEA
- **cBioPortal** - Cancer genomics portal integration

## Data Formats and Standards

### BioPAX (Biological Pathway Exchange)

**Primary Storage Format:** BioPAX Level 3
- **Level 1:** Metabolic pathway data
- **Level 2:** Molecular interactions and modifications
- **Level 3:** Complete signaling, gene regulation, genetic interactions
- Captures cellular locations and molecular states
- Community-standard format for pathway data sharing
- Full support for complex biological knowledge representation

**Advantages:**
- Expressive representation of biological complexity
- Support for semantic reasoning
- Enables sophisticated data integration
- Compatible with multiple tools and databases

### Additional Supported Formats

**Simple Interaction Format (SIF):**
- Binary pairwise relationship format
- Compatible with network analysis tools
- Lossy conversion from BioPAX
- Suitable for Cytoscape and other network tools

**GMT (Gene Matrix Transposed):**
- Gene set format for pathway enrichment analysis
- Compatible with GSEA (Gene Set Enrichment Analysis)
- Enables statistical pathway enrichment detection

**JSON-LD (Linked Data JSON):**
- Semantic web format with JSON convenience
- Suitable for web applications
- Enables programmatic access with semantic context
- RESTful API responses

**Additional Formats:**
- **SBGN-ML** (Systems Biology Graphical Notation) - Diagram notation
- **SBML** (Systems Biology Markup Language) - Computational modeling

## Technical Architecture

### Core Technology Stack

**Primary Platform:** **cPath2**
- Open-source database and web application
- Purpose-built for pathway data collection and querying
- Written in Java
- Available on GitHub (PathwayCommons/cpath2)
- RESTful web service architecture

**Key Library:** **Paxtools**
- Java library for BioPAX object models
- In-memory data representation
- Rich APIs for data manipulation and querying
- Advanced graph-theoretic query engine
- Pattern search for biologically relevant connections
- Support for all BioPAX levels with upgrade functionality
- Modular Maven-based architecture

**Infrastructure Components:**

1. **Warehouse Layer:**
   - Canonical molecule representation
   - Controlled vocabularies
   - Ontologies
   - BioPAX utility classes (EntityReference, ControlledVocabulary)

2. **Data Integration Layer:**
   - Normalization of diverse formats
   - Cross-database merging
   - Reference object consolidation
   - Identifier mapping

3. **Query Engine:**
   - Full-text search
   - Graph-based querying
   - Pattern matching
   - Network neighborhood analysis

4. **API Layer:**
   - RESTful web services
   - Multiple output format support
   - JSON-LD for linked data
   - Fine-grained data retrieval

### Technologies Used

- **Java** - Core platform development
- **OpenLink Virtuoso** (optional) - RDF triple store deployment
- **Docker** - Containerization and deployment
- **Maven** - Build and dependency management
- **Git/GitHub** - Version control and collaboration

### Data Storage and Infrastructure

- Normalized BioPAX database
- Support for billions of molecular interactions
- Efficient graph storage and querying
- Version control and archival

## Use Cases and Applications

### Network Analysis and Systems Biology

- **Interactive Pathway Exploration** - Discover molecular mechanisms and pathway interactions
- **Network Module Definition** - Automated identification of functional pathway modules
- **Gene and Protein Neighborhood Discovery** - Find connected entities in biological networks
- **Systems-level Integration** - Combine multi-omics data with pathway context

### Cancer Genomics and Precision Medicine

- **NetBox Algorithm** - Data-driven pathway module detection from genomic alterations
- **CausalPath** - Identify potentially causal relations from proteomics data
- **Mutex Method** - Detect mutual exclusivity to nominate cancer driver genes
- **cBioPortal Integration** - Overlay cancer genomics with pathway information
- **Drug-Target Discovery** - Identify therapeutic targets

### Pathway Enrichment and Gene Set Analysis

- **GSEA Integration** - Gene Set Enrichment Analysis workflows
- **Enrichment Map Analysis** - Visualization of pathway enrichment results
- **Statistical Significance Testing** - Identify over-represented pathways
- **Multi-omics Integration** - Genomics, transcriptomics, and proteomics correlation

### Research and Discovery

- **Hypothesis Generation** - Discover pathway interactions and dependencies
- **Signal Transduction Analysis** - Understand signaling mechanisms
- **Post-translational Modification Tracking** - Map protein state changes
- **Publication-quality Visualization** - Create detailed pathway diagrams
- **Data Mining** - Discover novel associations and cross-talk

### Educational and Training

- **Systems Biology Learning** - Understand biological network organization
- **Pathway Biology Documentation** - Comprehensive mechanism representation
- **Algorithm Development** - Benchmark and test graph algorithms

## Organizational Structure

### Host Institutions

**Memorial Sloan Kettering Cancer Center (MSKCC)**
- New York City, USA
- National Cancer Institute-designated Comprehensive Cancer Center
- Sloan Kettering Institute for Cancer Research
- Primary institutional home for Pathway Commons
- Focus on cancer pathway and interaction data

**University of Toronto**
- Toronto, Canada
- Collaborative institutional partner
- Development and maintenance support

### Leadership and Development

- **C. Sander group** (originally at MSKCC) - Scientific direction
- **G. Bader group** (University of Toronto) - Development and collaboration
- **Community developers** - Open-source contributions

### Development Status

- **Active and Maintained** - Continuous updates and improvements
- **Open-Source Model** - Community-driven development
- **GitHub Organization:** https://github.com/PathwayCommons
- Multiple actively maintained repositories (cpath2, paxtools, paxtoolsr, chibe, etc.)

## Standards and Interoperability

- **BioPAX Community Standard** - International standard for pathway data representation
- **W3C Standards** - RDF, Linked Data principles
- **Open Science Initiative** - Free and open access to all data
- **FAIR Data Principles** - Findable, Accessible, Interoperable, Reusable
- **Tool Ecosystem Support** - 40+ active tools support BioPAX format

## Citation and Usage

Pathway Commons data and services are completely free and open access. All data from integrated sources is freely available with attribution to source databases.

### Recommended Citation

For Pathway Commons:
"Rodchenkov I, Babur O, Luna A, et al. Pathway Commons 2019 Update: integration, analysis and exploration of pathway data. Nucleic Acids Research. 2020;48(D1):D489-D497."

Alternative citation:
"Pathway Commons. Available at: https://www.pathwaycommons.org/"

### Additional Resources

- **Main Website:** https://www.pathwaycommons.org/
- **Web Service API:** http://www.pathwaycommons.org/pc/webservice.do
- **API Documentation:** https://pathwaycommons.github.io/pcapi/
- **GitHub Organization:** https://github.com/PathwayCommons
- **cPath2 Repository:** https://github.com/PathwayCommons/cpath2
- **Paxtools Library:** https://github.com/BioPAX/Paxtools
- **R Package (paxtoolsr):** https://bioconductor.org/packages/release/bioc/html/paxtoolsr.html
- **Data Downloads:** https://www.pathwaycommons.org/
- **FAQ:** http://www.pathwaycommons.org/pc/faq.do
- **Cytoscape Integration:** http://www.pathwaycommons.org/pc/cytoscape.do

Pathway Commons continues to serve as a critical infrastructure resource for systems biology research, providing researchers with integrated access to the world's major pathway and molecular interaction databases through standardized formats, multiple interfaces, and sophisticated analysis tools.
