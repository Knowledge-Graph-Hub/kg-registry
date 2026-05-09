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
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: cob
        relation_type: prov:hadPrimarySource
      - source: dc
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: ecto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: fma
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hancestro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ido
        relation_type: prov:hadPrimarySource
      - source: ma
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: ogms
        relation_type: prov:hadPrimarySource
      - source: oio
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: omo
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: po
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: semapv
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: to
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
    product_file_size: 240665663
    product_url: https://www.ebi.ac.uk/efo/efo.owl
    secondary_source:
      - source: efo
        relation_type: prov:wasInfluencedBy
  - category: OntologyProduct
    description: The latest release of EFO in OBO format
    format: obo
    id: efo.obo
    name: EFO OBO
    original_source:
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: cob
        relation_type: prov:hadPrimarySource
      - source: dc
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: ecto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: fma
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hancestro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ido
        relation_type: prov:hadPrimarySource
      - source: ma
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: ogms
        relation_type: prov:hadPrimarySource
      - source: oio
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: omo
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: po
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: semapv
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: to
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
    product_file_size: 64058275
    product_url: https://www.ebi.ac.uk/efo/efo.obo
    secondary_source:
      - source: efo
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
infores_id: ordo
taxon:
  - NCBITaxon:9606
creation_date: '2025-06-04T00:00:00Z'
last_modified_date: '2025-12-13T00:00:00Z'
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
