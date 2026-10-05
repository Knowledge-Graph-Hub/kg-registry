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
  can browse ontologies through the website and programmatically via the OLS REST
  API and an MCP server. As of 2026-09-30 it served 287 ontologies with about 10.8
  million classes, loaded from the OBO Foundry registry plus ontologies curated by
  EMBL-EBI. Maintained by the Samples, Phenotypes and Ontologies Team (SPOT) at EMBL-EBI.
domains:
- biomedical
- biological systems
- information technology
homepage_url: https://www.ebi.ac.uk/ols4/
id: ols
infores_id: ols
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0 (software; loaded ontologies carry their own licenses)
name: Ontology Lookup Service
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching biomedical ontologies with
    exact match and obsolete term filtering
  format: http
  id: ols.portal
  is_public: true
  name: OLS Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  product_url: https://www.ebi.ac.uk/ols4/
- category: ProgrammingInterface
  description: RESTful API for programmatic access to ontology data including terms,
    properties, and relationships
  format: http
  id: ols.api
  is_public: true
  name: OLS REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  product_url: https://www.ebi.ac.uk/ols4/api-docs
- category: Product
  compression: targz
  description: Gzipped tar archive (ontology_jsons.tgz, about 2 GB) of all ontologies
    loaded into OLS, in OLS JSON format.
  format: json
  id: ols.json
  name: OLS Ontologies JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/
- category: Product
  compression: targz
  description: Gzipped tar archive (ontology_jsons_linked.tgz) of OLS ontology JSON
    with added cross-ontology and external database links.
  format: json
  id: ols.json-linked
  name: OLS Linked Ontology JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/
- category: Product
  description: Precomputed ontology term embeddings (full, PCA and UMAP projections)
    from multiple language models, used for semantic search in OLS.
  format: parquet
  id: ols.embeddings
  name: OLS Term Embeddings
  original_source: &id001
  - relation_type: prov:hadPrimarySource
    source: ols
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/embeddings/
- category: ProgrammingInterface
  description: Model Context Protocol (MCP) server for querying OLS from AI assistants
    over Streamable HTTP.
  format: http
  id: ols.mcp
  is_public: true
  name: OLS MCP Server
  original_source: *id001
  product_url: https://www.ebi.ac.uk/ols4/mcp
- category: MappingProduct
  compression: targz
  description: Ontology mappings extracted from all ontologies in SSSOM TSV format
  format: sssom
  id: ols.mappings
  name: OLS SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
publications:
- authors:
  - James McLaughlin
  - Josh Lagrimas
  - Haider Iqbal
  - Helen Parkinson
  - Henriette Harmse
  doi: 10.1093/bioinformatics/btaf279
  id: PMID:40323307
  journal: Bioinformatics
  preferred: true
  title: 'OLS4: a new Ontology Lookup Service for a growing interdisciplinary knowledge
    ecosystem'
  year: '2025'
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
- **Multiple Formats**: Data available as OLS JSON, linked JSON, SSSOM mappings and term embeddings
- **Regular Updates**: Continuous integration of latest ontology versions
- **SSSOM Mappings**: Standardized ontology-to-ontology mappings

## Access Methods

- **Web Portal**: Browse and search through https://www.ebi.ac.uk/ols4/
- **REST API**: Programmatic access documented at https://www.ebi.ac.uk/ols4/api-docs
- **FTP Downloads**: Data dumps available at https://ftp.ebi.ac.uk/pub/databases/spot/ols/
- **MCP Server**: Model Context Protocol access for AI assistants
- **MCP Server**: Model Context Protocol server for AI integration

## Data Formats

OLS provides data in multiple formats:

1. **JSON**: Internal ontology representation (~50 GB uncompressed)
2. **Linked JSON**: With cross-references added (~150 GB uncompressed)
3. **Embeddings**: Precomputed term embeddings in Parquet format
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

Please cite: OLS4: a new Ontology Lookup Service for a growing interdisciplinary knowledge ecosystem. *Bioinformatics*, Volume 41, Issue 5, May 2025, btaf279. PMID: 40323307