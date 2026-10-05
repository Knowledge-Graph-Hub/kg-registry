---
activity_status: inactive
category: Ontology
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jones@nceas.ucsb.edu
  - contact_type: github
    value: mbjones
  label: Matthew B. Jones
  orcid: 0000-0003-0077-4738
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nceas.ucsb.edu/
  label: National Center for Ecological Analysis and Synthesis (NCEAS)
creation_date: '2026-10-05T00:00:00Z'
description: The Extensible Observation Ontology (OBOE) is a formal OWL ontology from
  NCEAS for capturing the semantics of scientific observation and measurement. Its
  core concepts are Observation, Measurement, Entity, Characteristic, Standard (units
  and controlled vocabularies), and Protocol, and it includes an extensive set of
  unit definitions supporting unit conversion. OBOE is used for semantic annotation
  of ecological and environmental data and is designed to be extended with domain-specific
  Entities and Characteristics.
domains:
- ecology
- environment
- metadata
- information technology
homepage_url: https://github.com/NCEAS/oboe
id: oboe
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: 'OBOE: The Extensible Observation Ontology'
products:
- category: OntologyProduct
  description: Full OBOE 1.2 ontology in OWL (RDF/XML). This top-level file imports
    the core, characteristics, and standards modules.
  format: owl
  id: oboe.owl
  latest_version: '1.2'
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: OBOE OWL (full)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  product_file_size: 3699
  product_url: https://raw.githubusercontent.com/NCEAS/oboe/master/oboe.owl
- category: OntologyProduct
  description: OBOE core module in OWL, defining Observation, Measurement, Entity,
    Characteristic, Standard, Protocol, and their relationships.
  format: owl
  id: oboe.core
  latest_version: '1.2'
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: OBOE Core OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  product_file_size: 69407
  product_url: https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-core.owl
- category: OntologyProduct
  description: OBOE characteristics extension in OWL, defining measurable properties
    (Characteristics) used in observations.
  format: owl
  id: oboe.characteristics
  latest_version: '1.2'
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: OBOE Characteristics OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  product_file_size: 20695
  product_url: https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-characteristics.owl
- category: OntologyProduct
  description: OBOE standards extension in OWL, defining units of measurement and
    unit conversions used to interpret measured values.
  format: owl
  id: oboe.standards
  latest_version: '1.2'
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: OBOE Standards OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  product_file_size: 293793
  product_url: https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-standards.owl
- category: GraphicalInterface
  description: BioPortal page for OBOE (acronym OBOE), providing browsing, search,
    and download of the ontology. The latest submission is version 1.2, released 2019-09-17.
  format: http
  id: oboe.bioportal
  name: OBOE on BioPortal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.bioontology.org/ontologies/OBOE
- category: Product
  description: GitHub repository for OBOE, containing the OWL source files, design
    documentation, and branches for released versions 1.0 through 1.2.
  format: http
  id: oboe.repository
  name: OBOE GitHub repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  product_url: https://github.com/NCEAS/oboe
- category: OntologyProduct
  description: Current OWL release of ECSO (ECSO8.owl, version 0.10.0) in the DataONE sem-prov-ontologies
    repository, with merged imports of ENVO, PATO, CHEBI, RO, IAO and BFO terms
  format: owl
  id: ecso.owl
  name: ECSO OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecso
  product_file_size: 2310496
  product_url: https://raw.githubusercontent.com/DataONEorg/sem-prov-ontologies/main/ecso/ECSO8.owl
  secondary_source:
  - relation_type: prov:used
    source: oboe
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: pato
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ro
  - relation_type: prov:used
    source: iao
  - relation_type: prov:used
    source: bfo
publications:
- authors:
  - Joshua Madin
  - Shawn Bowers
  - Mark Schildhauer
  - Sergeui Krivov
  - Deana Pennington
  - Ferdinando Villa
  doi: 10.1016/j.ecoinf.2007.05.004
  id: doi:10.1016/j.ecoinf.2007.05.004
  journal: Ecological Informatics
  preferred: true
  title: An ontology for describing and synthesizing ecological observation data
  year: '2007'
repository: https://github.com/NCEAS/oboe
synonyms:
- OBOE
- Extensible Observation Ontology
---
## Description

The Extensible Observation Ontology (OBOE) is a formal OWL ontology from the National Center for Ecological Analysis and Synthesis (NCEAS) for capturing the semantics of scientific observation and measurement. Its main concepts are:

- **Observation**: an event in which one or more measurements are taken
- **Measurement**: the measured value of a property for a specific object or phenomenon
- **Entity**: an object or phenomenon on which measurements are made
- **Characteristic**: the property being measured
- **Standard**: units and controlled vocabularies for interpreting measured values
- **Protocol**: the procedures followed to obtain measurements

OBOE can describe observation context (such as space and time) and nested experimental observations, and includes an extensive set of unit definitions supporting automatic unit conversion. It is designed to be extended with domain-specific Entities and Characteristics; the Ecosystem Ontology (ECSO) maintained by DataONE builds on it.

The current release is version 1.2 (namespace `http://ecoinformatics.org/oboe/oboe.1.2/oboe.owl`), released in 2019; the repository has not been updated since September 2019. Citable release: doi:10.5063/F1125R0F (KNB Data Repository).

## Contacts

- Matthew B. Jones (jones@nceas.ucsb.edu) [ORCID: 0000-0003-0077-4738](https://orcid.org/0000-0003-0077-4738)
- National Center for Ecological Analysis and Synthesis (NCEAS)

## Products

### OBOE OWL (full)

Full OBOE 1.2 ontology in OWL, importing the core, characteristics, and standards modules.

**URL**: [https://raw.githubusercontent.com/NCEAS/oboe/master/oboe.owl](https://raw.githubusercontent.com/NCEAS/oboe/master/oboe.owl)

### OBOE Core OWL

**URL**: [https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-core.owl](https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-core.owl)

### OBOE Characteristics OWL

**URL**: [https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-characteristics.owl](https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-characteristics.owl)

### OBOE Standards OWL

**URL**: [https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-standards.owl](https://raw.githubusercontent.com/NCEAS/oboe/master/oboe-standards.owl)

### OBOE on BioPortal

**URL**: [https://bioportal.bioontology.org/ontologies/OBOE](https://bioportal.bioontology.org/ontologies/OBOE)

### OBOE GitHub repository

**URL**: [https://github.com/NCEAS/oboe](https://github.com/NCEAS/oboe)

## Publications

- [An ontology for describing and synthesizing ecological observation data](https://doi.org/10.1016/j.ecoinf.2007.05.004)
