---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://report.nih.gov/contactus
  - contact_type: email
    value: reporter@od.nih.gov
  label: NIH Office of Extramural Research
creation_date: '2025-07-20T00:00:00Z'
description: NIH Reporter (RePORTER) is a comprehensive data source providing access
  to information about NIH-funded research projects, including both intramural and
  extramural research activities. It serves as an electronic repository for NIH research
  project data, publications, and patents resulting from NIH funding since fiscal
  year 1985.
domains:
- biomedical
- health
- clinical
- translational
homepage_url: https://reporter.nih.gov/
id: nihreporter
last_modified_date: '2025-09-24T00:00:00Z'
layout: resource_detail
name: NIH Reporter
products:
- category: GraphicalInterface
  description: Web-based search interface for exploring NIH-funded research projects
    with advanced search capabilities
  format: http
  id: nihreporter.portal
  name: NIH Reporter Web Portal
  product_url: https://reporter.nih.gov/
- category: Product
  description: Bulk download of NIH research project data in structured format
  format: csv
  id: nihreporter.projects
  name: NIH Reporter Exporter Projects
  product_url: https://reporter.nih.gov/exporter/projects
- category: ProgrammingInterface
  description: API access to NIH research project data and search functionality
  format: http
  id: nihreporter.api
  name: NIH Reporter API
  product_url: https://reporter.nih.gov/
- category: Product
  description: Database of abstracts linked to NIH-funded research projects
  format: json
  id: nihreporter.abstracts
  name: NIH-Funded Project Abstracts
  product_url: https://reporter.nih.gov/exporter/abstracts
- category: Product
  description: Database of patents linked to NIH-funded research projects
  id: nihreporter.patents
  name: NIH-Funded Project Patents
  product_url: https://reporter.nih.gov/exporter/patents
- category: Product
  description: Database of clinical studies linked to NIH-funded research projects
  id: nihreporter.clinicalstudies
  name: NIH-Funded Project Clinical Studies
  product_url: https://reporter.nih.gov/exporter/clinicalstudies
- category: Product
  description: Database of publications linked to NIH-funded research projects
  format: json
  id: nihreporter.publications
  name: NIH-Funded Publications Database
  product_url: https://reporter.nih.gov/exporter/publications
- category: Product
  description: Database of publication link tables for NIH-funded research projects
  id: nihreporter.linktables
  name: NIH-Funded Publications Link Tables
  product_url: https://reporter.nih.gov/exporter/linktables
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
taxon:
- NCBITaxon:9606
---
# NIH Reporter

NIH Reporter (RePORTER - RePORT Expenditures and Results) is a comprehensive data source that provides access to information about NIH-funded research projects and their outcomes. As part of the Research Portfolio Online Reporting Tools (RePORT) suite, it serves as the primary electronic repository for NIH research funding data, supporting transparency and accountability in biomedical research funding.

## Key Features

### Comprehensive Research Project Database
- Contains records of NIH-funded research projects since fiscal year 1985
- Covers both intramural (conducted within NIH) and extramural (external institutions) research
- Includes grants, contracts, cooperative agreements, and other funding mechanisms
- Provides detailed project information including abstracts, aims, and funding amounts

### Advanced Search Capabilities
- Quick search functionality for broad queries across all fields
- Advanced search with configurable filters for precise project discovery
- Search by principal investigator, institution, project number, or keywords
- Geographic search capabilities for projects by state or region
- Fiscal year filtering for temporal analysis of funding patterns

### Publications and Patents Tracking
- Links NIH-funded projects to resulting publications in PubMed
- Tracks patents and intellectual property arising from NIH funding
- Provides impact metrics and citation tracking for research outcomes
- Enables assessment of research productivity and translation

## Data Coverage

### Project Information
- Project titles, abstracts, and specific aims
- Principal investigator and institutional details
- Funding amounts, duration, and administrative details
- Activity codes and funding mechanism classifications
- NIH Institute/Center assignments and program officer contacts

### Institutional Data
- Grantee organization information and contact details
- Geographic distribution of funding by state and institution
- Institutional capacity and research focus areas
- Historical funding patterns and success rates

### Financial Information
- Budget periods and funding amounts by fiscal year
- Direct and indirect cost breakdowns
- Cost sharing and matching fund requirements
- Success rates and funding trend analyses

### Research Outcomes
- Publications linked to specific grant numbers
- Patent applications and awards resulting from NIH funding
- Clinical trial registrations and outcomes
- Technology transfer and commercialization activities

## Applications

### Research Planning and Discovery
- Identify ongoing research in specific scientific areas
- Discover potential collaborators and research partnerships
- Assess funding landscape and competition in research domains
- Track research trends and emerging scientific priorities

### Grant Management and Compliance
- Monitor active grants and their progress
- Track publication and reporting requirements
- Assess research productivity and impact metrics
- Support grant renewal and continuation applications

### Policy Analysis and Oversight
- Analyze NIH spending patterns across scientific areas
- Evaluate geographic distribution of research funding
- Assess diversity and inclusion in research funding
- Support evidence-based policy development

### Academic and Industry Intelligence
- Market research for pharmaceutical and biotechnology companies
- Academic benchmarking and strategic planning
- Technology scouting and licensing opportunities
- Research impact assessment and evaluation

## Data Access and Integration

### Web Interface
- User-friendly search interface with guided tutorials
- Interactive visualizations of funding patterns and trends
- Export capabilities for search results and data analysis
- Mobile-responsive design for accessibility

### Data Export and APIs
- Bulk data downloads through ExPORTER functionality
- Structured data formats (CSV, XML, JSON) for analysis
- API endpoints for programmatic access to project data
- Integration capabilities with institutional research systems

### Quality Assurance
- Regular data updates and validation procedures
- Standardized data elements and controlled vocabularies
- Cross-referencing with external databases (PubMed, ClinicalTrials.gov)
- User feedback mechanisms for data quality improvement

## Technical Implementation
NIH Reporter is maintained by the NIH Office of Extramural Research and provides real-time access to the NIH grants database. The system integrates with multiple NIH administrative systems to ensure data accuracy and completeness, supporting both public transparency and internal research management needs.