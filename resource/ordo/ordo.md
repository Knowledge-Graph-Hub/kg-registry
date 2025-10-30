---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: contact.orphanet@inserm.fr
      - contact_type: url
        value: https://www.orpha.net/
    label: Orphanet
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.inserm.fr/
    label: INSERM
description: The Orphanet Rare Disease Ontology (ORDO) is an open-access ontology developed from the Orphanet information system, enabling complex queries of rare diseases and their epidemiological data (age of onset, prevalence, mode of inheritance) and gene-disorder functional relationships.
domains:
  - biomedical
  - health
  - clinical
  - genomics
  - phenotype
homepage_url: https://www.orphadata.com/ordo/
id: ordo
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0 (Creative Commons Attribution 4.0 International)
name: Orphanet Rare Disease Ontology (ORDO)
products:
  - category: DataModelProduct
    description: ORDO in OWL format in English (v4.7)
    format: owl
    id: ordo.owl
    name: ORDO OWL
    product_file_size: 49203440
    product_url: https://www.orphadata.com/data/ontologies/ordo/last_version/ORDO_en_4.7.owl
  - category: ProgrammingInterface
    description: SPARQL endpoint for querying the ORDO ontology
    id: ordo.sparql
    name: ORDO SPARQL Endpoint
    product_url: https://www.orphadata.com/ordo-sparql-endpoint/
  - category: DataModelProduct
    description: The Orphanet nomenclature pack provides ORPHAcodes (unique identifiers) for rare diseases, along with mappings to other terminologies, and is released annually in July.
    id: orphacode.nomenclature
    name: Orphanet Nomenclature Pack
    product_url: https://www.orphacode.org/pack-nomenclature/
    warnings: []
  - category: ProgrammingInterface
    description: API for accessing the Orphanet nomenclature pack data, allowing flexible implementation into various healthcare information systems.
    id: orphacode.api
    name: ORPHAcodes API
    product_url: https://api.orphacode.org/
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
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - hgnc
      - loinc
      - icd10
      - snomedct
      - uberon
      - pato
      - cl
      - doid
      - obi
      - obib
      - edam
      - hsapdv
      - sbo
      - mi
      - chebi
      - mp
      - ordo
      - uniprot
      - uo
      - mondo
      - efo
      - pgo
      - gencode
      - reactome
      - hra
      - hubmap
      - sennet
      - stellar
      - dct
      - clinvar
      - connectivitymap
      - hp
      - mp
      - msigdb
      - wikipathways
      - clingen
      - string
      - 4dn
      - erccrbp
      - erccreg
      - faldo
      - glycordf
      - glycocoo
      - gtex
      - kidsfirst
      - lincs
      - motrpac
      - mw
      - npo
      - sckan
      - disgenet
      - biomarker
      - opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - ubkg
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - hgnc
      - loinc
      - icd10
      - snomedct
      - uberon
      - pato
      - cl
      - doid
      - obi
      - obib
      - edam
      - hsapdv
      - sbo
      - mi
      - chebi
      - mp
      - ordo
      - uniprot
      - uo
      - mondo
      - efo
      - pgo
      - gencode
      - reactome
      - hra
      - hubmap
      - sennet
      - stellar
      - dct
      - clinvar
      - connectivitymap
      - hp
      - mp
      - msigdb
      - wikipathways
      - clingen
      - string
      - 4dn
      - erccrbp
      - erccreg
      - faldo
      - glycordf
      - glycocoo
      - gtex
      - kidsfirst
      - lincs
      - motrpac
      - mw
      - npo
      - sckan
      - disgenet
      - biomarker
      - opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - ubkg
infores_id: ordo
---

# Orphanet Rare Disease Ontology (ORDO)

The Orphanet Rare Disease Ontology (ORDO) is a comprehensive, structured vocabulary specifically designed for rare diseases. It integrates rare disease classification with relationships between diseases, genes, and other relevant features. ORDO has been developed and is maintained by Orphanet, a reference portal for information on rare diseases and orphan drugs.

## About ORDO

ORDO is an open-access ontology derived from the Orphanet knowledge base, enabling complex queries of rare disorders and their associated data. It was initially jointly developed by Orphanet and the European Bioinformatics Institute (EBI) to provide a structured vocabulary for rare diseases that captures relationships between diseases, genes, and other relevant features.

The ontology consists of over 11,000 classes and 70,000+ annotation assertion axioms. Each concept from the Orphanet database forms a distinct OWL (Web Ontology Language) class and is associated with other classes using defined object properties.

## Content and Structure

ORDO represents:
- A comprehensive classification of rare diseases
- Relationships between disorders and their genetic causes (when known)
- Mode of inheritance
- Associated epidemiological data (age of onset, age of death, prevalence)
- Cross-references to other terminologies:
  - International Classification of Diseases (ICD-10)
  - SNOMED CT
  - MeSH (Medical Subject Headings)
  - MedDRA (Medical Dictionary for Regulatory Activities)
  - OMIM (Online Mendelian Inheritance in Man)
  - UMLS (Unified Medical Language System)

An Evidence Code Ontology (ECO) is used to encode the provenance of assertions made in ORDO.

## ORPHAcodes

Central to ORDO is the Orphanet nomenclature, a multilingual, standardized, controlled medical terminology specific to rare diseases. Each clinical entity (disorder, group of disorders, or subtype) is associated with a unique numerical identifier called an ORPHAcode, along with a preferred term, synonyms, and a definition.

The Orphanet nomenclature is organized in a classification system structured around major medical specialties according to diagnostic and therapeutic relevance. This clinical coding system is mapped to main generic clinical and genetic terminologies, providing a common language across healthcare and research systems.

## Usage and Applications

ORDO is widely used for:
- Enabling precise identification of rare diseases in healthcare systems
- Supporting interoperability between different databases and registries
- Facilitating research on rare diseases
- Enhancing clinical coding in healthcare systems
- Supporting differential diagnosis

The ontology is particularly valuable for projects needing to integrate rare disease data with other biological and clinical information, as it provides a standardized framework for rare disease classification and annotation.

## Availability and Licensing

ORDO is available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. It is bi-annually released in July and December and can be accessed in multiple formats including OWL and OBO.

ORDO has been recognized as an ELIXIR Core Data Resource, a Global Core Biodata Resource, and an IRDiRC Recognized Resource, attesting to its quality and importance in the rare disease research community.
