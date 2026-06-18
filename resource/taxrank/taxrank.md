---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Jim Balhoff
  orcid: 0000-0002-8688-6599
  contact_details:
  - contact_type: email
    value: balhoff@renci.org
  - contact_type: github
    value: balhoff
creation_date: '2025-09-29T00:00:00Z'
description: A vocabulary of taxonomic ranks (species, family, phylum, etc)
domains:
- biological systems
- organisms
homepage_url: https://github.com/phenoscape/taxrank
id: taxrank
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Taxonomic rank vocabulary
products:
- category: OntologyProduct
  description: Taxonomic rank vocabulary in OWL format
  format: owl
  id: taxrank.owl
  name: taxrank.owl
  product_file_size: 3843
  product_url: http://purl.obolibrary.org/obo/taxrank.owl
  original_source:
  - source: taxrank
    relation_type: prov:hadPrimarySource
- category: OntologyProduct
  description: Taxonomic rank vocabulary in OBO format
  format: obo
  id: taxrank.obo
  name: taxrank.obo
  product_file_size: 2271
  product_url: http://purl.obolibrary.org/obo/taxrank.obo
  original_source:
  - source: taxrank
    relation_type: prov:hadPrimarySource
repository: https://github.com/phenoscape/taxrank
publications:
- authors:
  - Peter E Midford
  - Thomas Alex Dececchi
  - James P Balhoff
  - Wasila M Dahdul
  - Nizar Ibrahim
  - Hilmar Lapp
  - John G Lundberg
  - Paula M Mabee
  - Paul C Sereno
  - Monte Westerfield
  - Todd J Vision
  - David C Blackburn
  doi: 10.1186/2041-1480-4-34
  id: https://doi.org/10.1186/2041-1480-4-34
  journal: Journal of Biomedical Semantics
  title: 'The vertebrate taxonomy ontology: a framework for reasoning across model
    organism and species phenotypes'
  year: '2013'
---
## Description

Taxrank provides a compact ontology of biological taxonomic ranks such as
species, genus, family, order, and phylum, along with additional ranks and
pseudoranks needed to align with real-world taxonomy practice. The current OWL
release includes mappings to NCBI Taxonomy rank labels and TDWG rank terms where
available, making it useful as a shared normalization layer across biodiversity
and phenotype resources.

The Phenoscape-maintained repository is the authoritative source for editable
ontology files and published releases. In addition to standard Linnaean ranks,
the ontology now includes special cases such as no-rank, clade, strain, isolate,
serotype, and other rank tokens used in contemporary biological classification.

## Contacts

- Jim Balhoff (balhoff@renci.org) [ORCID: 0000-0002-8688-6599](https://orcid.org/0000-0002-8688-6599)

## Products

### taxrank.owl

Taxonomic rank vocabulary in OWL format

**URL**: [http://purl.obolibrary.org/obo/taxrank.owl](http://purl.obolibrary.org/obo/taxrank.owl)

**Format**: owl

### taxrank.obo

Taxonomic rank vocabulary in OBO format

**URL**: [http://purl.obolibrary.org/obo/taxrank.obo](http://purl.obolibrary.org/obo/taxrank.obo)

**Format**: obo

## Publications

- [The vertebrate taxonomy ontology: a framework for reasoning across model organism and species phenotypes](https://doi.org/10.1186/2041-1480-4-34)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*
