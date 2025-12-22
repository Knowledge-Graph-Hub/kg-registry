---
activity_status: active
category: DataModel
description: SKOS (Simple Knowledge Organization System) is a W3C recommendation designed
  for representation of thesauri, classification schemes, taxonomies, subject-heading
  systems, or any other type of structured controlled vocabulary.
domains:
- upper
homepage_url: https://www.w3.org/2004/02/skos/
id: skos
layout: resource_detail
license:
  id: https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
  label: W3C Software and Document License
name: SKOS
products:
- category: DataModelProduct
  description: SKOS Namespace Document - RDF/XML Variant
  format: rdfxml
  id: skos.rdf
  name: SKOS RDF/XML
  product_file_size: 28966
  product_url: https://www.w3.org/2009/08/skos-reference/skos.rdf
- category: DataModelProduct
  description: SKOS Core Vocabulary Specification
  format: http
  id: skos.core
  name: SKOS Core
  product_url: https://www.w3.org/TR/swbp-skos-core-spec/
- category: DocumentationProduct
  description: SKOS Simple Knowledge Organization System Reference
  format: http
  id: skos.reference
  name: SKOS Reference
  product_url: https://www.w3.org/TR/skos-reference/
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
  description: Cell Line Ontology in OWL format
  format: owl
  id: clo.owl
  name: clo.owl
  product_file_size: 2121232
  product_url: http://purl.obolibrary.org/obo/clo.owl
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
- category: OntologyProduct
  description: OWL release of Monochrom Ontology
  format: owl
  id: chr.model.owl
  name: Monochrom Ontology OWL release
  original_source:
  - ro
  - go
  - ncbitaxon
  - iao
  - geno
  - skos
  - gff
  product_file_size: 102365
  product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
  secondary_source:
  - chr
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
  - File was not able to be retrieved when checked on 2025-12-18_ FTP error_ timed
    out
  - File was not able to be retrieved when checked on 2025-12-18_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2025-12-22: FTP error: timed
    out'
- category: OntologyProduct
  description: OpenBioDiv-O, the OpenBiodiv Ontology
  format: ttl
  id: openbiodiv.ontology.ttl
  is_public: true
  name: OpenBioDiv-O
  original_source:
  - skos
  - proton
  - fabio
  - doco
  - openbiodiv
  product_file_size: 8176
  product_url: https://raw.githubusercontent.com/pensoft/OpenBiodiv/refs/heads/master/ontology/openbiodiv-ontology-latest.ttl
  secondary_source:
  - openbiodiv
publications:
- authors:
  - Alistair Miles
  - Sean Bechhofer
  doi: 10.1016/j.websem.2009.06.001
  id: doi:10.1016/j.websem.2009.06.001
  journal: 'Web Semantics: Science, Services and Agents on the World Wide Web'
  title: SKOS Simple Knowledge Organization System Reference
  year: '2009'
repository: https://github.com/w3c/skos
version: SKOS Reference (August 18, 2009)
---
# SKOS (Simple Knowledge Organization System)

SKOS (Simple Knowledge Organization System) is a W3C recommendation designed for representation of thesauri, classification schemes, taxonomies, subject-heading systems, or any other type of structured controlled vocabulary. SKOS is built upon RDF and RDFS, and its main objective is to enable easy publication and use of such vocabularies as linked data.

## Overview

SKOS provides a model for expressing the basic structure and content of concept schemes such as thesauri, classification schemes, subject heading lists, taxonomies, folksonomies, and other similar types of controlled vocabulary. As an application of the Resource Description Framework (RDF), SKOS allows concepts to be composed and published on the World Wide Web, linked with data on the Web and integrated into other concept schemes.

## Core Features

- **Concepts and Concept Schemes**: SKOS is based around concepts, which can be identified with URIs, labeled with lexical strings, assigned notations, documented with notes, linked to other concepts, and organized into informal hierarchies and association networks.

- **Semantic Relationships**: SKOS provides properties for representing hierarchical (broader/narrower) and associative relations between concepts.

- **Multilingual Labels**: SKOS allows concepts to be labeled in multiple languages, with properties for preferred, alternative, and hidden labels.

- **Concept Collections**: Groups of concepts can be defined and labeled, with a loose notion of membership.

## Common Use Cases

SKOS is widely used in:
- Digital libraries for subject indexing
- Knowledge management systems
- Semantic Web applications
- Linked Data initiatives
- Vocabulary alignment and mapping projects

## Relationship to Other Standards

SKOS complements other semantic web standards like OWL (Web Ontology Language) and provides a simpler approach for many knowledge organization tasks. It bridges the gap between formal knowledge representation languages like OWL and the chaotic, informal world of unstructured information.

## Usage in Knowledge Graphs

SKOS is often used within knowledge graphs to organize concepts and provide a controlled vocabulary layer. Many domain-specific ontologies import SKOS concepts to support labeling and organizing their terms. It serves as a foundational vocabulary for semantic interoperability across different knowledge systems.

## More Information

- [SKOS Home Page](https://www.w3.org/2004/02/skos/)
- [SKOS Primer](https://www.w3.org/TR/skos-primer/)
- [SKOS Reference](https://www.w3.org/TR/skos-reference/)