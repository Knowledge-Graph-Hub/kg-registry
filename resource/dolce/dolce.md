---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.loa.istc.cnr.it/
  label: Laboratory for Applied Ontology (LOA), ISTC-CNR
creation_date: '2026-10-04T00:00:00Z'
description: DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering)
  is a foundational (upper-level) ontology developed and maintained by the Laboratory
  for Applied Ontology at ISTC-CNR. It distinguishes endurants, perdurants, qualities
  and abstracts, is axiomatized in first-order logic, and has been stable since its
  2002/2003 release in the WonderWeb project. Since 2023 it is part 3 of the ISO/IEC
  21838 standard for top-level ontologies, which ships OWL 2 and Common Logic axiomatizations.
  Lighter OWL re-engineerings, DOLCE-Lite and DOLCE+DnS Ultralite (DUL), are widely
  used to align domain ontologies.
domains:
- general
homepage_url: http://www.loa.istc.cnr.it/dolce/overview.html
id: dolce
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: DOLCE
products:
- category: OntologyProduct
  description: OWL 2 axiomatization of DOLCE (functional syntax) published as an electronic
    insert of ISO/IEC 21838-3:2023, engineered by Laure Vieu and Daniele Porello from
    DOLCE Simple in CASL. Use is governed by the ISO Customer Licence Agreement for
    electronic inserts.
  format: owl
  id: dolce.iso-owl
  name: DOLCE OWL (ISO/IEC 21838-3)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_file_size: 37374
  product_url: https://standards.iso.org/iso-iec/21838/-3/ed-1/en/Dolce.owl
- category: OntologyProduct
  description: Common Logic (CLIF) axiomatization of DOLCE Simple published as an
    electronic insert of ISO/IEC 21838-3:2023. Use is governed by the ISO Customer
    Licence Agreement for electronic inserts.
  format: txt
  id: dolce.iso-clif
  name: DOLCE Simple CLIF (ISO/IEC 21838-3)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_file_size: 16050
  product_url: https://standards.iso.org/iso-iec/21838/-3/ed-1/en/dolce_simple_clif.p
- category: OntologyProduct
  description: DOLCE-Lite, an OWL (RDF/XML) re-engineering of DOLCE by Aldo Gangemi
    and colleagues. It omits modality and temporal indexing.
  format: owl
  id: dolce.lite
  name: DOLCE-Lite OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_file_size: 106827
  product_url: http://www.loa.istc.cnr.it/ontologies/DOLCE-Lite.owl
- category: OntologyProduct
  compression: zip
  description: DOLCE Lite-Plus library (version 3.97), a zip of OWL modules extending
    DOLCE-Lite with Descriptions and Situations, plans, information objects and other
    modules.
  format: owl
  id: dolce.lite-plus
  name: DOLCE Lite-Plus 3.97 Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_file_size: 261017
  product_url: http://www.loa.istc.cnr.it/ontologies/DLP3971.zip
- category: OntologyProduct
  description: DOLCE+DnS Ultralite (DUL) version 4.2, a lightweight, pattern-based
    simplification and extension of DOLCE Lite-Plus by Aldo Gangemi, served as Turtle
    from the Ontology Design Patterns portal. Extensions such as IOLite, SystemsLite
    and PlansLite are published alongside it.
  format: ttl
  id: dolce.dul
  name: DOLCE+DnS Ultralite (DUL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_file_size: 186902
  product_url: http://www.ontologydesignpatterns.org/ont/dul/DUL.owl
- category: DocumentationProduct
  description: WonderWeb Deliverable D18, the final first-order axiomatization of
    DOLCE and the official reference documentation, together with the WonderWeb Foundational
    Ontologies Library.
  format: pdf
  id: dolce.d18
  name: WonderWeb Deliverable D18
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_file_size: 1789764
  product_url: http://www.loa.istc.cnr.it/old/Papers/D18.pdf
- category: DocumentationProduct
  description: LOA overview page for DOLCE, with links to its formalizations, documentation
    and related papers.
  format: http
  id: dolce.overview
  name: DOLCE Overview
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dolce
  product_url: http://www.loa.istc.cnr.it/dolce/overview.html
- category: DocumentationProduct
  description: PDF specification of PROTON 3.0 Beta, describing the System, Top, Extent
    and Knowledge Management modules and their classes and properties.
  format: pdf
  id: proton.ontology
  is_public: true
  name: PROTON 3.0 Beta Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  - relation_type: prov:wasInfluencedBy
    source: freebase
  - relation_type: prov:wasInfluencedBy
    source: wordnet
  - relation_type: prov:wasInfluencedBy
    source: dolce
  product_file_size: 725192
  product_url: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf
  warnings:
  - Could not be retrieved when checked on 2026-10-04 because the Ontotext site served
    a CAPTCHA page instead of the file.
- category: OntologyProduct
  compression: gzip
  description: PROTON Top module (version 3.0) in Turtle, as mirrored on TriplyDB,
    with core entity types such as Person, Location and Organization plus temporal,
    quantitative and abstract concepts.
  format: ttl
  id: proton.top
  is_public: true
  name: PROTON Top Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  - relation_type: prov:wasInfluencedBy
    source: dolce
  product_file_size: 12036
  product_url: https://api.triplydb.com/datasets/ontotext/proton/download.ttl.gz
publications:
- authors:
  - Stefano Borgo
  - Roberta Ferrario
  - Aldo Gangemi
  - Nicola Guarino
  - Claudio Masolo
  - Daniele Porello
  - Emilio M. Sanfilippo
  - Laure Vieu
  doi: 10.3233/AO-210259
  id: doi:10.3233/AO-210259
  journal: Applied Ontology
  preferred: true
  title: 'DOLCE: A descriptive ontology for linguistic and cognitive engineering1'
  year: '2022'
synonyms:
- Descriptive Ontology for Linguistic and Cognitive Engineering
- DOLCE-Lite
- DOLCE+DnS Ultralite
- DUL
- ISO/IEC 21838-3
---
# DOLCE

DOLCE, the Descriptive Ontology for Linguistic and Cognitive Engineering, is a foundational ontology from the Laboratory for Applied Ontology (LOA) at ISTC-CNR. It was the first module of the WonderWeb Foundational Ontologies Library, alongside OCHRE and BFO, and has been stable since its 2002/2003 release. Its official documentation is WonderWeb Deliverable D18, which gives the first-order axiomatization.

DOLCE has a cognitive bias: its categories follow distinctions found in natural language and common sense. Its top-level split separates endurants (objects), perdurants (events and processes), qualities and abstracts.

## Formalizations

- **ISO/IEC 21838-3:2023.** DOLCE is part 3 of the ISO/IEC 21838 standard on top-level ontologies. ISO publishes the OWL 2 and Common Logic axiomatizations as free electronic inserts at https://standards.iso.org/iso-iec/21838/-3/ed-1/en/, under the ISO Customer Licence Agreement. The standard text itself is sold by ISO.
- **DOLCE-Lite and DOLCE Lite-Plus.** OWL re-engineerings by Aldo Gangemi and colleagues. They do not cover modality or temporal indexing, and Lite-Plus adds modules such as Descriptions and Situations.
- **DOLCE+DnS Ultralite (DUL).** A simplified, pattern-based OWL ontology derived from DOLCE Lite-Plus, served from the Ontology Design Patterns portal. It is the version most often imported by domain ontologies.

## License

No single license is stated for DOLCE or its LOA-hosted OWL files. The ISO electronic inserts carry the ISO licence terms. The Crossref title of the 2022 Applied Ontology paper ends in a footnote marker ("engineering1"), and the page keeps it so the publication cache matches.