---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: glyconnect@sib.swiss
  - contact_type: url
    value: https://glyconnect.expasy.org/
  label: GlyConnect Team - SIB Swiss Institute of Bioinformatics
description: GlyConnect is a knowledgebase of glycoproteins spanning protein, glycosite
  and glycan information, with data on various species, tissues, and disease associations.
domains:
- biological systems
- chemistry and biochemistry
homepage_url: https://glyconnect.expasy.org/
id: glyconnect
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: GlyConnect
products:
- category: GraphicalInterface
  description: Web interface for exploring GlyConnect data
  id: glyconnect.site
  is_public: true
  name: GlyConnect Web Interface
  original_source:
  - glyconnect
  product_url: https://glyconnect.expasy.org/
  secondary_source:
  - glyconnect
- category: ProgrammingInterface
  description: RESTful API for accessing GlyConnect data
  id: glyconnect.api.rest
  is_public: true
  name: GlyConnect RESTful API
  original_source:
  - glyconnect
  product_url: https://glyconnect.expasy.org/api
  secondary_source:
  - glyconnect
- category: ProgrammingInterface
  description: SPARQL endpoint for querying GlyConnect RDF data
  id: glyconnect.api.sparql
  is_public: true
  name: GlyConnect SPARQL Endpoint
  original_source:
  - glyconnect
  product_url: https://glyconnect.expasy.org/rdf
  secondary_source:
  - glyconnect
- category: Product
  description: Compositions dataset containing glycan compositions
  format: csv
  id: glyconnect.compositions
  name: GlyConnect Glycan Compositions
  original_source:
  - glyconnect
  product_url: https://glyconnect.expasy.org/downloads/compositions/
  secondary_source:
  - glyconnect
- category: Product
  description: Immunoglobulins dataset containing glycans commonly found on immunoglobulins
  format: csv
  id: glyconnect.immunoglobulins
  name: GlyConnect Immunoglobulins Dataset
  original_source:
  - glyconnect
  product_url: https://glyconnect.expasy.org/downloads/Immunoglobulins/
  secondary_source:
  - glyconnect
- category: Product
  description: RDF version of the GlyConnect data for semantic web applications
  format: ttl
  id: glyconnect.rdf
  name: GlyConnect RDF Data
  original_source:
  - glyconnect
  product_url: https://glyconnect.expasy.org/downloads/rdf/
  secondary_source:
  - glyconnect
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-01: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
publications:
- authors:
  - Alocci D
  - Mariethoz J
  - Gastaldello A
  - Gasteiger E
  - Karlsson NG
  - Kolarich D
  - Packer NH
  - Lisacek F
  doi: doi:10.1021/acs.jproteome.8b00766
  id: doi:10.1021/acs.jproteome.8b00766
  title: 'GlyConnect: Glycoproteomics Goes Visual, Interactive, and Analytical'
  year: '2019'
---
GlyConnect is a comprehensive knowledgebase of glycoproteomics data maintained by the SIB Swiss Institute of Bioinformatics. It integrates information spanning three key levels of glycobiology: proteins, glycosites (the specific locations where glycans attach to proteins), and glycan structures.

The database provides curated glycoproteomic data from various species, tissues, and disease states, with a particular focus on human glycoproteins. GlyConnect uses the Symbol Nomenclature for Glycans (SNFG) standard for representing glycan structures in a visually consistent way.

Key features of GlyConnect include:

- Integration of glycoprotein data across multiple species
- Mapping of glycan structures to specific attachment sites on proteins
- Association of glycan profiles with diseases and tissues
- Specialized datasets for important glycoprotein families (e.g., immunoglobulins)
- Human milk oligosaccharide (HMO) data
- COVID-19 related glycosylation data
- O-linked monosaccharide information

GlyConnect serves as a valuable resource for researchers in glycobiology, proteomics, and biomedical sciences by providing a unified view of the complex relationships between proteins and their glycosylation patterns. The database is regularly updated and expanded to include new glycoproteomic data.

Access to GlyConnect is provided through a user-friendly web interface, programmatic access via RESTful and SPARQL APIs, and bulk downloads of specialized datasets.