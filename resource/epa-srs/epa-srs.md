---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.epa.gov/
    label: U.S. Environmental Protection Agency
creation_date: '2026-06-02T00:00:00Z'
description: EPA Substance Registry Services is the U.S. Environmental Protection Agency's central system for information about substances tracked or regulated by EPA or other sources, including chemicals, biological organisms, and substance lists.
domains:
  - environment
  - chemistry and biochemistry
homepage_url: https://cdxapps.epa.gov/oms-substance-registry-services/about-srs
id: epa-srs
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://edg.epa.gov/epa_data_license.html
  label: EPA Standard Open Data License
name: EPA Substance Registry Services
products:
  - category: GraphicalInterface
    description: Public EPA Substance Registry Services search interface for looking up substances tracked or regulated by EPA programs and other sources.
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
    description: EPA SRS widget service for embedding a Substance Registry Services search box in external web pages.
    format: http
    id: epa-srs.widget
    is_public: true
    name: EPA SRS Widget
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epa-srs
    product_url: https://www.epa.gov/developers/data-data-products-substance-registry-services-widget
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
---

# EPA Substance Registry Services

EPA Substance Registry Services provides identifiers and descriptive information
for substances tracked by EPA programs and other environmental regulatory sources.
Downstream chemical resources such as DSSTox use SRS as contextual source
information for substance identifiers and names.
