---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-11-22T00:00:00Z'
description: A semantic web-based knowledge graph integrating cancer registry data
  from multiple U.S. state registries with external datasets to enable advanced analytics,
  complex queries, hypothesis generation, and visualization for cancer surveillance
  and research
domains:
- clinical
- biomedical
- health
- translational
homepage_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
id: cancer-registry-kg
last_modified_date: '2025-11-22T00:00:00Z'
layout: resource_detail
license:
  id: https://www.hhs.gov/open/public-access-guiding-principles/index.html
  label: NIHMS Public Access
name: Cancer Registry Knowledge Graph
products:
- category: GraphProduct
  description: RDF-based knowledge graph containing 374,682 unique tumor records from
    Louisiana Tumor Registry (2000-2016) with 240 columns of NAACCR-standardized cancer
    data including demographics, tumor characteristics, treatment, and outcomes. Contains
    90,673,527 triples stored in Virtuoso triplestore with SPARQL endpoint access.
  id: cancer-registry-kg.ltr
  name: Louisiana Tumor Registry Knowledge Graph
  original_source:
  - cancer-registry-kg
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: RDF-based knowledge graph containing 207,766 unique tumor records from
    Kentucky Cancer Registry (2010-2016) with 232 columns of cancer data. Contains
    48,409,945 triples demonstrating the framework's ability to dynamically integrate
    multiple registry datasets without code changes.
  id: cancer-registry-kg.kcr
  name: Kentucky Cancer Registry Knowledge Graph
  original_source:
  - cancer-registry-kg
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 403 error
    when accessing file'
- category: Product
  description: Linked neighborhood concentrated disadvantage index (CDI) dataset for
    Louisiana and Kentucky census tracts, enabling socioeconomic analysis of cancer
    incidence patterns and disparities. Demonstrates knowledge graph capability for
    third-party data integration to explain variation in cancer outcomes.
  id: cancer-registry-kg.cdi
  name: Concentrated Disadvantage Index Integration
  original_source:
  - cancer-registry-kg
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 403 error
    when accessing file'
- category: ProgrammingInterface
  description: Python-based API using RDFLib for parameterized SPARQL query execution
    against cancer registry knowledge graph. Provides template-based queries for hypothesis
    generation, treatment sequence analysis, and multi-dataset integration without
    requiring users to write SPARQL directly.
  id: cancer-registry-kg.api
  name: Cancer Registry Query API
  original_source:
  - cancer-registry-kg
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
- category: GraphicalInterface
  description: Interactive graph visualization service using Gephi with Semantic Web
    Importer plugin to query Virtuoso SPARQL endpoint. Provides high-level and low-level
    visualizations with graph algorithms (PageRank, connected components, modularity)
    for pattern discovery and anomaly detection.
  id: cancer-registry-kg.visualization
  name: Gephi-Based KG Visualization
  original_source:
  - cancer-registry-kg
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
publications:
- authors:
  - S.M. Shamimul Hasan
  - Donna Rivera
  - Xiao-Cheng Wu
  - Eric B. Durbin
  - J. Blair Christian
  - Georgia Tourassi
  doi: 10.1109/JBHI.2020.2990797
  id: PMID:32386166
  journal: IEEE Journal of Biomedical and Health Informatics
  title: Knowledge Graph-Enabled Cancer Data Analytics
  year: '2020'
---
## Overview

The Cancer Registry Knowledge Graph is a semantic web-based digital library framework designed to address major challenges in the secondary use of cancer registry data for research and analytics. Built on Resource Description Framework (RDF) technology, this knowledge graph approach transforms traditional relational database cancer registry data into a flexible, queryable graph structure that enables complex analyses, dynamic data linking, and iterative schema evolution.

The system was developed using patient-level data from the Louisiana Tumor Registry (LTR) and Kentucky Cancer Registry (KCR), demonstrating a scalable approach to organizing cancer surveillance data that overcomes limitations of traditional relational database management systems (RDBMS). The knowledge graph integrates heterogeneous datasets including tumor characteristics, demographics, treatment information, socioeconomic factors, and geographic data to support comprehensive cancer research.

## Key Features

- **Massive Scale Integration**: Louisiana KG contains 90.6 million triples from 374,682 tumor records; Kentucky KG contains 48.4 million triples from 207,766 tumor records
- **Query Performance**: Up to 76% improvement in query runtime compared to traditional SQL-based approaches for complex hierarchical queries
- **Standard Data Model**: Built on W3C RDF standard enabling easy mapping from relational, tree, key-value, and graph data models
- **Dynamic Schema Evolution**: Flexible structure allows schema changes without code redesign, demonstrated through anomaly flagging for data quality analysis
- **Third-Party Data Linking**: Seamlessly integrates external datasets (CDI, Rural-Urban Continuum Codes) sharing common keys like FIPS codes
- **SPARQL Endpoint**: Enables graph-based queries with equivalent expressive power to relational algebra but optimized for graph patterns
- **Semantic Enrichment**: Integrates ontologies and vocabularies to model domain concepts and enable reasoning
- **Scenario-Specific Queries**: Hierarchical query support for treatment sequence analysis representing 60% of physician-directed clinical queries
- **Multi-Registry Support**: Framework tested across two state registries demonstrating generalizability without API code changes

## Data Sources

### Primary Cancer Registry Data

- **Louisiana Tumor Registry (LTR)**: 374,682 unique tumor records, 240 columns, 207 MB CSV file, diagnoses 2000-2016, NAACCR data standards
- **Kentucky Cancer Registry (KCR)**: 207,766 unique tumor records, 232 columns, 118 MB CSV file, diagnoses 2010-2016
- **Data Elements**: Patient demographics (age, gender, race, marital status), tumor characteristics (site, stage, histology, laterality), treatment information (surgery, chemotherapy, radiation, hormone therapy dates), vital status, date of last contact

### External Linked Datasets

- **Neighborhood Concentrated Disadvantage Index (CDI)**: Six census variables (poverty, public assistance, female-headed families, unemployment, age <18, percent Black) for Louisiana and Kentucky census tracts
- **Rural-Urban Continuum Codes**: USDA classification codes for metropolitan/non-metropolitan county classifications (1974, 1983, 1993, 2003, 2013)
- **2010 U.S. Census Data**: Population demographics by age group, race, and state for incidence rate calculations

## Technical Implementation

### Knowledge Graph Creation Pipeline

**Stage 1: Data Loading**
- CSV cancer registry data loaded into PostgreSQL 9.5.9 relational database
- Schema derived from column headers with null value standardization
- Column datatypes inherited from raw data

**Stage 2: RDF Mapping Generation**
- D2RQ 0.8.1 tool generates mapping files from PostgreSQL database
- Maps database table names to RDF classes and attributes to RDF properties
- Louisiana mapping: 56 KB, 1,467 triples, <1 minute creation time
- Kentucky mapping: 56 KB, 1,420 triples, <1 minute creation time

**Stage 3: Knowledge Graph Materialization**
- D2RQ dump-rdf service creates materialized RDF graphs from mappings
- Louisiana KG: 16 GB, 90,673,527 triples, ~75 minutes creation time
- Kentucky KG: 8.1 GB, 48,409,945 triples, ~52 minutes creation time

**Stage 4: Triplestore Deployment**
- Graphs loaded into Virtuoso Open-Source Edition 7.2.4 triplestore
- Infrastructure: CentOS 7.4, 2.0 GHz Intel Xeon E7 4850 CPU, 128 GB RAM, 1 TB storage
- SPARQL endpoint provides graph query execution interface

### Data Quality and Cleaning

**Validation Checks:**
- Data type validation (integer, string, float)
- Range checks (e.g., marital status 1-9, percent Black ≤100)
- Cross-field consistency (e.g., chemotherapy date ≥ diagnosis date)
- Mandatory field verification (Patient ID, Tumor Record Number)
- Uniqueness checks (FIPS codes)
- Format validation (8-digit YYYYMMDD dates)

**Data Normalization:**
- Missing month/day information padded with zeros for date uniformity
- Null value standardization across datasets (space, NA, NR → database null)
- Gene identifier mapping to reference genomes (Zm-B73, Sorghum v3.1.1, etc.)

## Applications and Use Cases

### Application 1: Treatment Sequence Analysis

**Breast Cancer Treatment Patterns:**
- Hierarchical query structure for middle-aged (40-64) female breast cancer patients
- 64 treatment sequence combinations analyzed across four therapy types (Surgery, Chemotherapy, Radiation, Hormone therapy)
- Sequences evaluated by length (1-4 treatments) and order
- Results stratified by breast cancer subsites (C50.0-C50.9) and vital status (right-censored/deceased)
- Findings: Upper-outer quadrant (C50.4) most common site (10,262 tumors), length-3 sequences most prevalent
- Query performance: 76% average improvement over PostgreSQL SQL queries (Tables XII-XV)

### Application 2: Triple Negative Breast Cancer (TNBC) Disparities

**Replication of Hossain et al. 2019 Study:**
- Louisiana analysis: 1,299 TNBC cases (2010-2012) vs. 1,216 in original study
- Kentucky analysis: 1,096 TNBC cases demonstrating framework generalizability
- Age-specific incidence rates by race showing African American women have higher rates than European American women across age groups
- CDI distribution analysis revealing African American women disproportionately live in disadvantaged neighborhoods (CDI values 0 to 4 standard deviations above mean)
- Statistical validation: Two-sample t-tests confirm no significant difference (p>0.05) between our results and published findings for age, race, and SEER Summary Stage distributions

**API-Based Hypothesis Testing:**
- `getCDI` API enables parameterized queries by state, disease, stage, race, sex, diagnosis years, and CDI range
- Template-based SPARQL queries with placeholders for dynamic parameter substitution
- Zero code changes required to apply Louisiana queries to Kentucky data
- Supports iterative hypothesis generation and validation across multiple registries

### Application 3: Schema Evolution for Anomaly Detection

**Data Discrepancy Identification:**
- Prostate cancer laterality anomalies: 118 cases with paired organ codes (value=2) despite prostate being single organ
- Breast cancer histology outliers: 88 cases with codes 9590-9992 (outside expected range per SEER standards)
- Solution: Dynamic addition of `isValidLaterality` flag nodes/edges without core software redesign
- Demonstrates knowledge graph flexibility for iterative quality analysis

### Application 4: Graph Visualization

**High-Level Visualization (Rural-Urban Continuum Codes):**
- Node degree-based layout showing state nodes (degree >100, red/gray) connected to county nodes (degree 5-2, green/black/blue/orange)
- Yifan Hu layout algorithm for node aggregation and spatial organization
- Edge colors indicate connections between colored node pairs
- Enables rapid identification of important nodes and structural patterns

**Low-Level Visualization (Patient-County Relationships):**
- Detailed view of four hypothetical patients linked to common county
- Displays primary site, diagnosis date, and county properties
- Supports hypothesis generation about geographic clustering and unusual trends
- HIPAA-compliant simulated data maintains underlying schema consistency

## Performance Metrics

### Query Performance Comparison

- Treatment sequence queries: 64 distinct combinations tested
- SQL queries (PostgreSQL): 307-360 milliseconds average
- SPARQL queries (Virtuoso): 72-105 milliseconds average
- Overall improvement: 76% faster on knowledge graph vs. RDBMS
- Best case: Query 3.4 (S-R-H) 79.7% improvement (360ms → 73ms)
- Worst case: Query 3.16 (R-C-H) 65.9% improvement (308ms → 105ms)

### Scalability Validation

- Louisiana to Kentucky generalization: APIs executed without code modifications
- Dynamic data integration: Multiple state registries supported through common NAACCR standards
- Schema evolution: Anomaly flags added without GUI-level code changes
- Multi-dataset linking: CDI and Rural-Urban Continuum Codes integrated via FIPS codes

## Advantages Over Traditional Approaches

### Flexibility
- **RDBMS**: Rigid schema requiring extensive code changes for modifications
- **Knowledge Graph**: Graph-based structure easily accommodates new data types and relationships

### Complex Queries
- **RDBMS**: Expensive JOIN operations for multi-table queries, difficult recursive/transitive queries
- **SPARQL**: Graph patterns naturally express tree, long path traversal, and transitivity queries

### Data Integration
- **RDBMS**: Tedious linking process requiring customized software for each format
- **Knowledge Graph**: Dynamic linking through common identifiers, easy integration of heterogeneous sources

### Semantics
- **RDBMS**: Limited ontology integration capabilities
- **Knowledge Graph**: Native support for ontologies, vocabularies, and reasoning through description logic

### Visualization
- **RDBMS**: Requires custom GUI development, difficult to reflect schema changes
- **Knowledge Graph**: Open-source tools (Gephi, D3, Cytoscape) provide free faceted browsing, graph algorithms, and automatic schema reflection

### Cost
- **RDBMS**: Significant programming effort for analysis tools and visualization
- **Knowledge Graph**: Freely available linked data browsers, semantic search, and visualization tools

## Framework Architecture (5S Digital Library)

**Streams**: Input/output data flows including cancer registry extracts, external datasets, query results, visualizations

**Structures**: Knowledge graph organization with class hierarchy (data organization layer) and instances (patient/tumor level)

**Spaces**: Indexing and information retrieval algorithms from Virtuoso graph repository

**Scenarios**: Services including treatment sequence analysis, hypothesis generation/testing, data discrepancy analysis, visualization

**Societies**: User communities including researchers, cancer registrars, healthcare providers, policymakers

## Future Directions

### Planned Enhancements

1. **Additional External Datasets**: BioPortal, GeoNames, DrugBank, LinkedCT, DBpedia, Bio2RDF, SemMed integration
2. **Advanced Analytics**: Graph pattern mining algorithms for clinically meaningful hypothesis generation
3. **Treatment Evaluation**: Longitudinal treatment sequence and outcome analysis using linked data
4. **Clinical Trial Matching**: Eligibility identification through integrated knowledge base
5. **Drug Treatment Analysis**: Evaluation using linked pharmacological databases
6. **Geographic Risk Factors**: Patient geographic variation analysis with environmental exposures
7. **Domain-Specific Language**: Integration of cancer-specific ontologies to support researcher needs

### Broader Impact

The framework demonstrates that cancer registry data management and analysis benefit significantly from knowledge graph approaches, offering a scalable solution for multi-state and potentially national cancer surveillance systems. The 5S digital library framework connects diverse stakeholder communities through integrated information services while maintaining data quality and enabling iterative research workflows.

## Validation and Replication

### Statistical Rigor

- Two-sample t-tests validate consistency with published literature
- 95% confidence intervals reported for mean differences
- Significance level α=0.05 for hypothesis testing
- Descriptive statistics (sample size, means) provided for all comparisons

### Reproducibility Considerations

Small discrepancies (1.6-6.8%) between our results and Hossain et al. attributed to:
- Census tract exclusions in original study
- Dataset version differences (updated records)
- Missing lower-level experimental details (normalization strategies)
- Data changes between analysis timeframes

## Citation

Hasan SMS, Rivera D, Wu XC, Durbin EB, Christian JB, Tourassi G. Knowledge Graph-Enabled Cancer Data Analytics. IEEE J Biomed Health Inform. 2020 Jul;24(7):1952-1967. doi: 10.1109/JBHI.2020.2990797. PMID: 32386166; PMCID: PMC8324069.