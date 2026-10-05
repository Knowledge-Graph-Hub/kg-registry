---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://report.nih.gov/contactus
  - contact_type: email
    value: report@mail.nih.gov
  label: NIH Office of Extramural Research
creation_date: '2025-07-20T00:00:00Z'
description: NIH Reporter (RePORTER) is a searchable repository of federally funded
  biomedical research projects, covering NIH intramural and extramural research as
  well as projects funded by CDC, AHRQ, HRSA, ACF and the VA. It links projects (from
  fiscal year 1985) to publications (from 1980), patents and clinical studies, and
  offers a web interface, a public REST API and bulk ExPORTER downloads refreshed
  weekly.
domains:
- biomedical
- clinical
homepage_url: https://reporter.nih.gov/
id: nihreporter
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: NIH Reporter
products:
- category: GraphicalInterface
  description: Web-based search interface for exploring NIH-funded research projects
    with advanced search capabilities
  format: http
  id: nihreporter.portal
  name: NIH Reporter Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/
- category: Product
  compression: zip
  description: Bulk download of NIH research project data in structured format
  format: csv
  id: nihreporter.projects
  name: NIH Reporter Exporter Projects
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/projects
- category: ProgrammingInterface
  description: Public REST API (no key required) returning JSON for searching projects
    (v2 projects endpoint) and project-linked publications
  format: http
  id: nihreporter.api
  name: NIH Reporter API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://api.reporter.nih.gov/
- category: Product
  compression: zip
  description: Database of abstracts linked to NIH-funded research projects
  format: csv
  id: nihreporter.abstracts
  name: NIH-Funded Project Abstracts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/abstracts
- category: Product
  description: Database of patents linked to NIH-funded research projects
  format: csv
  id: nihreporter.patents
  name: NIH-Funded Project Patents
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  - relation_type: prov:wasDerivedFrom
    source: iedison
  product_url: https://reporter.nih.gov/exporter/patents
- category: Product
  description: Database of clinical studies linked to NIH-funded research projects
  format: csv
  id: nihreporter.clinicalstudies
  name: NIH-Funded Project Clinical Studies
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/clinicalstudies
- category: Product
  compression: zip
  description: Database of publications linked to NIH-funded research projects
  format: csv
  id: nihreporter.publications
  name: NIH-Funded Publications Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/publications
- category: Product
  description: Database of publication link tables for NIH-funded research projects
  format: csv
  id: nihreporter.linktables
  name: NIH-Funded Publications Link Tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/linktables
- category: Product
  compression: zip
  description: Legacy CRISP (Computer Retrieval of Information on Scientific Projects)
    project and abstract data for fiscal years 1970 to 2009, in CSV and XML.
  format: csv
  id: nihreporter.crisp
  name: NIH Reporter Legacy CRISP Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/crisp
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: python
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: Product
  compression: gzip
  description: nihreporter.project Nodes TSV
  format: tsv
  id: obo-db-ingest.nihreporter.project.tsv
  name: nihreporter.project Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 65861949
  product_url: https://w3id.org/biopragmatics/resources/nihreporter.project/nihreporter.project.tsv.gz
- category: Product
  description: Web interface for searching and visualizing chemical-protein interactions
    across organisms
  format: http
  id: stitch.portal
  is_public: true
  name: STITCH Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/
- category: Product
  description: Downloadable data files containing chemical-protein interaction networks
  format: tsv
  id: stitch.downloads
  is_public: true
  name: STITCH Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/cgi/download.pl
- category: ProgrammingInterface
  description: API for programmatic access to STITCH chemical-protein interaction
    data
  format: http
  id: stitch.api
  is_public: true
  name: STITCH API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/cgi/access.pl?footer_active_subpage=apis
- category: Product
  compression: gzip
  description: nihreporter.project OBO
  format: obo
  id: obo-db-ingest.nihreporter.project.obo
  name: nihreporter.project OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  product_file_size: 69000371
  product_url: https://w3id.org/biopragmatics/resources/nihreporter.project/nihreporter.project.obo.gz
- category: Product
  compression: gzip
  description: nihreporter.project OWL
  format: owl
  id: obo-db-ingest.nihreporter.project.owl
  name: nihreporter.project OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  product_file_size: 91398017
  product_url: https://w3id.org/biopragmatics/resources/nihreporter.project/nihreporter.project.owl.gz
- category: Product
  compression: gzip
  description: nihreporter.project OBO Graph JSON
  format: json
  id: obo-db-ingest.nihreporter.project.json
  name: nihreporter.project OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  product_file_size: 81463463
  product_url: https://w3id.org/biopragmatics/resources/nihreporter.project/nihreporter.project.json.gz
- category: DocumentationProduct
  description: Description of the eRA reporting and analytics modules, including the
    public RePORT and RePORTER tools and the internal QVR, SPIRES and iRePORT modules
    built on IMPAC II data.
  format: http
  id: nih-era.reporting-docs
  name: eRA Reporting and Analytics Modules
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nih-era
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  product_url: https://www.era.nih.gov/about-era/services-for-agency-staff/reporting-analytics
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
- Historical funding patterns

### Financial Information
- Budget periods and funding amounts by fiscal year
- Direct and indirect cost breakdowns
- Funding trend analyses

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
- Assess research productivity
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
- Bulk ExPORTER files as zipped CSV (XML is also available for legacy CRISP data); the API returns JSON
- API endpoints for programmatic access to project data
- Integration capabilities with institutional research systems

### Quality Assurance
- Regular data updates and validation procedures
- Standardized data elements and controlled vocabularies
- Cross-referencing with external databases (PubMed, ClinicalTrials.gov)
- User feedback mechanisms for data quality improvement

## Technical Implementation
NIH Reporter is maintained by the NIH Office of Extramural Research and provides real-time access to the NIH grants database. The system integrates with multiple NIH administrative systems to ensure data accuracy and completeness, supporting both public transparency and internal research management needs.