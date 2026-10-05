---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.dataone.org/
  - contact_type: github
    value: DataONEorg
  label: DataONE
- category: Individual
  contact_details:
  - contact_type: email
    value: jones@nceas.ucsb.edu
  label: Matt Jones
creation_date: '2026-10-05T00:00:00Z'
description: The Ecosystem Ontology (ECSO) is DataONE's ontology of ecosystem-level
  measurements and characteristics, originally developed for carbon flux measurements
  in the MsTMIP and LTER use cases. It is built on the OBOE observation model and reuses
  terms from ENVO, PATO, CHEBI and other OBO ontologies, and is used to semantically
  annotate datasets in the DataONE federation.
domains:
- ecology
- environment
homepage_url: https://github.com/DataONEorg/sem-prov-ontologies
id: ecso
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: The Ecosystem Ontology
products:
- category: OntologyProduct
  description: Current OWL release of ECSO (ECSO8.owl, version 0.10.0) in the DataONE
    sem-prov-ontologies repository, with merged imports of ENVO, PATO, CHEBI, RO, IAO
    and BFO terms
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
- category: GraphicalInterface
  description: NCBO BioPortal entry for browsing and searching ECSO
  format: http
  id: ecso.bioportal
  name: ECSO BioPortal Entry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecso
  product_url: https://bioportal.bioontology.org/ontologies/ECSO
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  warnings:
  - Page returned HTTP 403 to automated requests when checked on 2026-10-05. The BioPortal
    REST API still lists the ontology.
- category: GraphicalInterface
  description: GitHub repository for DataONE semantic and provenance ontologies, containing
    ECSO source files, development notes and term practices
  format: http
  id: ecso.github
  name: DataONE sem-prov-ontologies GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecso
  product_url: https://github.com/DataONEorg/sem-prov-ontologies
repository: https://github.com/DataONEorg/sem-prov-ontologies
---
# The Ecosystem Ontology (ECSO)

ECSO is an ontology of ecosystem measurements and characteristics developed by
DataONE. It extends the Extensible Observation Ontology (OBOE) and reuses terms
from ENVO, PATO, CHEBI and other OBO Foundry ontologies. DataONE uses ECSO to
annotate dataset attributes so that measurements can be found across member
repositories. Terms use URIs of the form `http://purl.dataone.org/odo/ECSO_%08d`.
The ontology is also browsable in NCBO BioPortal and LifeWatch EcoPortal.
