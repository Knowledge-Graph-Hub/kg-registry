---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.epa.gov/
      - contact_type: url
        value: https://www.epa.gov/data/forms/contact-us-about-system-registries
    label: U.S. Environmental Protection Agency
creation_date: '2026-06-02T00:00:00Z'
description: EPA Substance Registry Services (SRS) is the U.S. Environmental Protection Agency's central registry for information about regulated and monitored substances, including chemicals, biological organisms, and other substances listed in environmental statutes and EPA data systems, as well as substances of interest from other federal agencies, international organizations, and states. SRS supports EPA's Chemical Identification and Biological Taxonomy data standards, records the names and synonyms each EPA program or statute uses for a substance, and is a component of EPA's System of Registries.
domains:
  - environment
  - chemistry and biochemistry
homepage_url: https://cdxapps.epa.gov/oms-substance-registry-services/about-srs
id: epa-srs
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://edg.epa.gov/epa_data_license.html
  label: EPA Standard Open Data License
name: EPA Substance Registry Services
products:
  - category: GraphicalInterface
    description: Public EPA Substance Registry Services search interface for looking up substances tracked or regulated by EPA programs and other sources, by name, CAS number, and other identifiers, with basic, advanced, and multi-substance search. Search results and substance lists can be exported as Excel, JSON, or XML files.
    format: http
    id: epa-srs.search
    name: EPA SRS Search
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-srs
    product_url: https://cdxapps.epa.gov/oms-substance-registry-services/search
  - category: DocumentationProduct
    description: EPA overview page explaining Substance Registry Services as the central EPA system for substance information and program-list membership.
    format: http
    id: epa-srs.about
    name: About EPA Substance Registry Services
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-srs
    product_url: https://cdxapps.epa.gov/oms-substance-registry-services/about-srs
  - category: ProgrammingInterface
    description: EPA SRS widget service for embedding a Substance Registry Services search box in external web pages using a JavaScript file served from ofmpub.epa.gov.
    format: http
    id: epa-srs.widget
    is_public: true
    name: EPA SRS Widget
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-srs
    product_url: https://www.epa.gov/developers/data-data-products-substance-registry-services-widget
  - category: ProgrammingInterface
    description: SRS REST web services (OpenAPI/Swagger documented, version v1.2) returning JSON records for substances queried by CAS number, name or synonym, EPA ID, internal tracking number, ITIS taxonomic serial number, CompTox DTXSID, substance list acronym, classification, or characteristic, plus lookups of TSCA generic substances by PMN or accession number. Records include identifiers such as CAS numbers, DTXSIDs, InChI, and SMILES, and the synonyms used by each EPA list.
    format: http
    id: epa-srs.rest_api
    is_public: true
    name: SRS REST Web Services
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-srs
    product_url: https://cdxapps.epa.gov/oms-substance-registry-services/swagger-ui/
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: dsstoxdb
      - relation_type: prov:wasInformedBy
        source: itis
  - category: ProgrammingInterface
    description: Exchange Network data exchange for SRS (version 3.0), providing services for Exchange Network partners to retrieve full SRS records for a single substance, pull substance lists, and submit substances and synonyms to SRS lists. The page offers the full exchange package for download.
    format: http
    id: epa-srs.exchange_network
    name: SRS Exchange Network Data Exchange
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-srs
    product_url: https://exchangenetwork.net/data-exchange/srs/
  - category: MappingProduct
    description: Downloadable Excel and CSV files containing DSSTox identifiers mapped to CAS numbers, InChIKeys, SMILES, molecular formulas, and other chemical identifiers for over 1.2 million substances
    format: mixed
    id: dsstoxdb.downloads
    latest_version: 10.23645/epacomptox.5588566.v8
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0
    name: DSSTox Data Downloads
    original_source:
      - relation_type: prov:hadPrimarySource
        source: dsstoxdb
    product_url: https://epa.figshare.com/articles/dataset/Chemistry_Dashboard_Data_DSSTox_Identifiers_Mapped_to_CAS_Numbers_and_Names/5588566
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: epa-srs
      - relation_type: prov:wasInformedBy
        source: chemid
      - relation_type: prov:wasInformedBy
        source: pubchem
synonyms:
  - EPA SRS
  - Substance Registry Services
  - Substance Registry System
  - SRS
---

# EPA Substance Registry Services

EPA Substance Registry Services (SRS) is the U.S. Environmental Protection Agency's
central registry for information about regulated and monitored substances. It provides
a common basis for identifying chemicals, biological organisms, and other substances
listed in environmental statutes and EPA data systems, and it records which EPA program
or statute tracks each substance and the name or synonym that program uses.

SRS supports EPA's Chemical Identification Data Standard and Biological Taxonomy Data
Standard. Each chemical record carries a systematic name and, where one exists, a
common SRS Registry Name, along with identifiers such as the CAS Registry Number and
the CompTox DTXSID; biological organisms are identified by ITIS taxonomic serial
numbers. SRS is part of EPA's System of Registries (SoR).

## Access

- **Web application**: basic, advanced, and multi-substance search, substance detail
  pages, and substance list pages, with Excel, JSON, and XML export of results and lists.
- **SRS REST web services**: a public JSON API documented with Swagger, covering lookups
  by CAS number, name, EPA ID, internal tracking number, TSN, DTXSID, and list acronym.
- **Exchange Network services**: single-substance, substance-list, and add-to-list
  services for Exchange Network partners.
- **SRS widget**: an embeddable search box for external web pages.

Downstream chemical resources such as DSSTox use SRS as contextual source
information for substance identifiers and names.
