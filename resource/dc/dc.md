---
activity_status: active
category: DataModel
description: Dublin Core Metadata Initiative (DCMI) Metadata Terms is an authoritative
  specification of metadata terms for resource description. It includes the fifteen
  elements of the Dublin Core Metadata Element Set plus several dozen properties,
  classes, datatypes, and vocabulary encoding schemes. The terms are intended for
  use in combination with metadata terms from other vocabularies in application profiles.
  DCMI metadata terms are expressed in RDF vocabularies for use in Linked Data and
  are published as ISO standards (ISO 15836-1:2017 for the original 15 elements, ISO
  15836-2:2019 for extended terms).
domains:
- information technology
- literature
homepage_url: https://www.dublincore.org/
id: dc
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: Dublin Core Metadata Terms
products:
- category: DocumentationProduct
  description: The DCMI Metadata Terms specification document, providing comprehensive
    documentation of all properties in the /terms/ namespace including abstract, accessRights,
    contributor, coverage, creator, date, description, format, identifier, language,
    publisher, relation, rights, subject, title, type, and many others.
  format: http
  id: dc.terms_spec
  name: DCMI Metadata Terms Specification
  product_url: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- category: DocumentationProduct
  description: Documentation for the fifteen core Dublin Core elements in the /elements/1.1/
    namespace (contributor, coverage, creator, date, description, format, identifier,
    language, publisher, relation, rights, source, subject, title, type).
  format: http
  id: dc.elements_spec
  name: Dublin Core Elements 1.1 Specification
  product_url: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-3
- category: DataModelProduct
  description: RDF schema for Dublin Core terms in the /terms/ namespace.
  format: rdfxml
  id: dc.terms_rdf
  name: Dublin Core Terms RDF Schema
  product_url: http://purl.org/dc/terms/
- category: DataModelProduct
  description: RDF schema for Dublin Core elements in the /elements/1.1/ namespace.
  format: rdfxml
  id: dc.elements_rdf
  name: Dublin Core Elements RDF Schema
  product_url: http://purl.org/dc/elements/1.1/
- category: DataModelProduct
  description: RDF schema for the DCMI Type Vocabulary, defining classes for basic
    types (Collection, Dataset, Event, Image, InteractiveResource, MovingImage, PhysicalObject,
    Service, Software, Sound, StillImage, Text).
  format: rdfxml
  id: dc.dcmitype_rdf
  name: DCMI Type Vocabulary RDF Schema
  product_url: http://purl.org/dc/dcmitype/
- category: DocumentationProduct
  description: Documentation for vocabulary encoding schemes (DCMIType, DDC, IMT,
    LCC, LCSH, MESH, NLM, TGN, UDC) and syntax encoding schemes (Box, ISO3166, ISO639-2,
    ISO639-3, Period, Point, RFC standards, URI, W3CDTF).
  format: http
  id: dc.encoding_schemes
  name: Dublin Core Encoding Schemes
  product_url: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-4
- category: DocumentationProduct
  description: Documentation for Dublin Core classes including Agent, BibliographicResource,
    FileFormat, Frequency, Jurisdiction, LicenseDocument, LinguisticSystem, Location,
    MediaType, and others.
  format: http
  id: dc.classes
  name: Dublin Core Classes
  product_url: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-6
- category: OntologyProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - doid
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 240665663
  product_url: https://www.ebi.ac.uk/efo/efo.owl
  secondary_source:
  - efo
- category: OntologyProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - doid
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 64058275
  product_url: https://www.ebi.ac.uk/efo/efo.obo
  secondary_source:
  - efo
- category: OntologyProduct
  description: EDAM OWL release
  format: owl
  id: edam.owl
  name: EDAM OWL
  original_source:
  - edam
  - dc
  - skos
  product_file_size: 3373041
  product_url: http://edamontology.org/EDAM.owl
  secondary_source:
  - edam
- category: OntologyProduct
  description: EDAM TSV export
  format: tsv
  id: edam.tsv
  name: EDAM TSV
  original_source:
  - edam
  - dc
  - skos
  product_file_size: 1977072
  product_url: https://edamontology.org/EDAM.tsv
  secondary_source:
  - edam
- category: OntologyProduct
  description: EDAM CSV export
  format: csv
  id: edam.csv
  name: EDAM CSV
  original_source:
  - edam
  - dc
  - skos
  product_file_size: 1977072
  product_url: https://edamontology.org/EDAM.csv
  secondary_source:
  - edam
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete
    FORUM data
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
  original_source:
  - mesh
  - chebi
  - cito
  - fabio
  - dc
  - cheminf
  - skos
  - chemont
  - pubchem
  - pubmed
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  secondary_source:
  - forum
  warnings:
  - File was not able to be retrieved when checked on 2025-12-11_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2025-12-11: FTP error: timed
    out'
publications:
- id: https://www.iso.org/standard/71339.html
  preferred: true
  title: 'ISO 15836-1:2017 Information and documentation — The Dublin Core metadata
    element set — Part 1: Core elements'
  year: '2017'
- id: https://www.iso.org/standard/71341.html
  title: 'ISO 15836-2:2019 Information and documentation — The Dublin Core metadata
    element set — Part 2: DCMI Properties and classes'
  year: '2019'
repository: https://github.com/dcmi/
---
# Dublin Core Metadata Terms

Dublin Core Metadata Initiative (DCMI) Metadata Terms provides a standardized vocabulary for resource description. The specification includes the foundational fifteen-element Dublin Core Metadata Element Set, widely used for over two decades, plus an extensive collection of properties, classes, and encoding schemes maintained for RDF and Linked Data applications.

The metadata terms are organized into four namespaces:
- `/elements/1.1/` - The original 15 core elements (published as ISO 15836-1:2017)
- `/terms/` - Extended properties and refined versions of core elements (ISO 15836-2:2019)
- `/dcmitype/` - DCMI Type Vocabulary for categorizing resource types
- `/dcam/` - Terms for vocabulary description

Dublin Core terms are designed to be used in combination with other vocabularies in application profiles, supporting interoperability across diverse metadata communities.