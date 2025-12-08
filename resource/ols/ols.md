---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: EBISPOT/ols4
  - contact_type: email
    value: ols-support@ebi.ac.uk
  id: ebi
  label: EMBL-EBI Samples, Phenotypes and Ontologies Team
creation_date: '2025-10-30T00:00:00Z'
description: The Ontology Lookup Service (OLS) is a repository for biomedical ontologies
  that aims to provide a single point of access to the latest ontology versions. Users
  can browse ontologies through the website and programmatically via the OLS API.
  Maintained by the Samples, Phenotypes and Ontologies Team (SPOT) at EMBL-EBI.
domains:
- biomedical
- upper
- biological systems
homepage_url: https://www.ebi.ac.uk/ols4/
id: ols
infores_id: ols
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: Ontology Lookup Service
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching biomedical ontologies with
    exact match and obsolete term filtering
  format: http
  id: ols.portal
  name: OLS Web Portal
  product_url: https://www.ebi.ac.uk/ols4/
- category: ProgrammingInterface
  description: RESTful API for programmatic access to ontology data including terms,
    properties, and relationships
  format: http
  id: ols.api
  name: OLS REST API
  product_url: https://www.ebi.ac.uk/ols4/api-docs
- category: Product
  compression: gzip
  description: Internal JSON representation of all loaded ontologies (approximately
    50 GB uncompressed)
  format: json
  id: ols.json
  name: OLS Ontologies JSON
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/
- category: GraphProduct
  compression: tar
  description: Neo4j database with linked ontology data including cross-references
    between ontologies and external databases (approximately 150 GB)
  dump_format: neo4j
  format: neo4j
  id: ols.neo4j
  name: OLS Neo4j Database
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/
- category: Product
  compression: tar
  description: Solr search index database for ontology searching (requires Solr 9.0.0)
  id: ols.solr
  name: OLS Solr Database
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/
- category: MappingProduct
  compression: gzip
  description: Ontology mappings extracted from all ontologies in SSSOM TSV format
  format: tsv
  id: ols.mappings
  name: OLS SSSOM Mappings
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/
publications:
- id: PMID:39913645
  preferred: true
repository: https://github.com/EBISPOT/ols4
synonyms:
- OLS
- OLS4
---

# Ontology Lookup Service

## Overview

The Ontology Lookup Service (OLS) is a comprehensive repository for biomedical ontologies maintained by EMBL-EBI. It provides a single point of access to the latest versions of numerous biomedical ontologies, making it easier for researchers to browse, search, and access ontology data. OLS supports both human browsing through its web interface and programmatic access through its REST API.

## Data Content

OLS aggregates and provides access to numerous biomedical ontologies from various sources, including:

- **Anatomy and Development**: Uberon, Cell Ontology (CL), and others
- **Diseases**: Disease Ontology (DOID), Mondo, Human Phenotype Ontology (HPO)
- **Chemistry**: ChEBI
- **Molecular Biology**: Gene Ontology (GO), Sequence Ontology (SO)
- **And many more** biomedical domain ontologies

The service provides:
- Latest ontology versions with automatic updates
- Cross-references between ontologies
- Links to external databases
- Ontology metadata and provenance information
- Term definitions, synonyms, and hierarchical relationships

## Key Features

- **Web Interface**: User-friendly browsing and searching with filtering options
- **REST API**: Comprehensive programmatic access to all ontology data
- **Search Capabilities**: Full-text search with exact match and obsolete term options
- **Cross-References**: Linked data between different ontologies and external databases
- **Multiple Formats**: Data available in JSON, Neo4j, Solr, and SSSOM formats
- **Regular Updates**: Continuous integration of latest ontology versions
- **SSSOM Mappings**: Standardized ontology-to-ontology mappings

## Access Methods

- **Web Portal**: Browse and search through https://www.ebi.ac.uk/ols4/
- **REST API**: Programmatic access documented at https://www.ebi.ac.uk/ols4/api-docs
- **FTP Downloads**: Data dumps available at https://ftp.ebi.ac.uk/pub/databases/spot/ols/
- **Database Exports**: Neo4j and Solr databases for local deployment
- **MCP Server**: Model Context Protocol server for AI integration

## Data Formats

OLS provides data in multiple formats:

1. **JSON**: Internal ontology representation (~50 GB uncompressed)
2. **Linked JSON**: With cross-references added (~150 GB uncompressed)
3. **Neo4j**: Graph database format (requires Neo4j community 2025.03.0)
4. **Solr**: Search index database (requires Solr 9.0.0)
5. **SSSOM**: Standard Simple Standard for Ontology Mappings format

## Use Cases

1. **Ontology Browsing**: Explore biomedical ontologies interactively
2. **Programmatic Integration**: Access ontology data in applications via API
3. **Local Deployment**: Set up local OLS instances for development
4. **Mapping Analysis**: Study cross-ontology mappings and relationships
5. **Data Annotation**: Use ontology terms for standardized data annotation
6. **AI Integration**: Access ontology knowledge through MCP server

## Related Services

The SPOT team also provides complementary services:

- **OxO**: Cross-ontology mapping service between terms from different ontologies
- **ZOOMA**: Service to assist in mapping data to ontologies in OLS

## Management

**Organization**: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)

**Repository**: https://github.com/EBISPOT/ols4

**Contact**:
- GitHub Issues: https://github.com/EBISPOT/ols4/issues
- Email: ols-support@ebi.ac.uk
- Mailing List: ols-announce@ebi.ac.uk (for announcements)

## Funding

OLS has been supported by:
- EMBL-EBI Core Funds
- European Union HORIZON program (grant 101131959)
- Chan-Zuckerberg Initiative (Human Cell Atlas Data Coordination Platform)
- NIH Office of the Director (R24-OD011883, OT2OD033756)
- NIH National Human Genome Research Institute (5RM1 HG010860)
- European Union's Horizon 2020 (grants 824087, 825575, 654248)
- EVORA project (grant 101131959)

## Privacy and Terms

- **Privacy Policy**: Available at https://www.ebi.ac.uk/ols4/Privacy_notice_for_EMBL-EBI_Public_Website.pdf
- **Terms of Use**: https://www.ebi.ac.uk/about/terms-of-use
- **License**: EMBL-EBI licensing terms apply

## Citation

Please cite: OLS4: a new Ontology Lookup Service for a growing interdisciplinary knowledge ecosystem. *Bioinformatics*, Volume 41, Issue 5, May 2025, btaf279. PMID: 39913645

# Ontology Lookup Service API

## Overview

The OLS REST API provides access to key biological data from OLS. The services provide a unified interface to query information about ontology terms from GO (the Gene Ontology) and ECO (the Evidence & Conclusion Ontology), Gene Ontology annotations from the EBI's GOA database, and gene products (proteins from UniProt, RNA from RNAcentral and complexes from ComplexPortal).

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:ols`

## Curation Status

- **Stub**: Yes - needs manual curation
- **Creation Date**: 2025-10-30
- **Original Source**: Translator Information Resource Registry

## What Needs to be Curated

1. **Activity Status**: Verify if this resource is active, inactive, or deprecated
2. **Category**: Confirm the resource category is correct
3. **Description**: Expand and improve the description
4. **Homepage URL**: Verify and update if needed
5. **Products**: Add specific data products/files/APIs offered by this resource
6. **Contacts**: Add contact information
7. **Publications**: Add relevant publications
8. **Domains**: Add relevant domain tags
9. **Repository**: Add code repository if applicable

## Additional Notes