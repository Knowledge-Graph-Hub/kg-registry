---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cfpub.epa.gov/ecotox/
  label: U.S. Environmental Protection Agency (EPA), Office of Research and Development
creation_date: '2026-10-27T00:00:00Z'
description: The ECOTOXicology Knowledgebase (ECOTOX) is the U.S. EPA's curated knowledgebase
  of single-chemical toxicity test results for ecologically relevant aquatic and terrestrial
  species, abstracted from the peer-reviewed literature. Each record captures the
  chemical, test species, exposure conditions, and measured effects and endpoints.
  ECOTOX supports environmental research, chemical risk assessment, and the development
  of ecological models and QSARs.
domains:
- toxicology
- ecology
- environment
- environmental exposure
homepage_url: https://cfpub.epa.gov/ecotox/
id: ecotox
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: ECOTOX Knowledgebase
products:
- category: GraphicalInterface
  description: ECOTOX web interface for searching and exploring toxicity records by
    chemical, species, and effect, with result export.
  format: http
  id: ecotox.web
  name: ECOTOX Knowledgebase Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecotox
  product_url: https://cfpub.epa.gov/ecotox/
- category: DocumentationProduct
  description: ECOTOX help and user documentation.
  format: http
  id: ecotox.help
  name: ECOTOX Help
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecotox
  product_url: https://cfpub.epa.gov/ecotox/help.cfm
- category: Product
  description: TERA knowledge graph dataset snapshot version 1.1.0 hosted on Zenodo,
    including NT files and CSV mappings
  format: http
  id: tera.zenodo-dataset
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY 4.0
  name: TERA Knowledge Graph Dataset (Zenodo)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tera
  - relation_type: prov:hadPrimarySource
    source: ecotox
  product_file_size: 5905580032
  product_url: https://zenodo.org/records/4244313
- category: Product
  description: Chemical data from EPA ECOTOX in N-Triples RDF format
  format: ntriples
  id: tera.ecotox-chemical-nt
  name: ECOTOX Chemical Data (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tera
  - relation_type: prov:hadPrimarySource
    source: ecotox
  product_file_size: 680300
  product_url: https://zenodo.org/records/4244313/files/ecotox_chemical.nt
- category: Product
  description: Taxonomy data from EPA ECOTOX in N-Triples RDF format
  format: ntriples
  id: tera.ecotox-taxonomy-nt
  name: ECOTOX Taxonomy Data (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tera
  - relation_type: prov:hadPrimarySource
    source: ecotox
  product_file_size: 22800000
  product_url: https://zenodo.org/records/4244313/files/ecotox_taxonomy.nt
- category: Product
  description: Chemical effects data in N-Triples RDF format
  format: ntriples
  id: tera.effects-nt
  name: Effects Data (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tera
  - relation_type: prov:hadPrimarySource
    source: ecotox
  product_file_size: 1000000000
  product_url: https://zenodo.org/records/4244313/files/effects.nt
publications:
- authors:
  - Jennifer H. Olker
  - Colleen M. Elonen
  - Anne Pilli
  - Arne Anderson
  - et al.
  doi: 10.1002/etc.5324
  id: doi:10.1002/etc.5324
  journal: Environmental Toxicology and Chemistry
  preferred: true
  title: 'The ECOTOXicology Knowledgebase: A Curated Database of Ecologically Relevant
    Toxicity Tests to Support Environmental Research and Risk Assessment'
  year: '2022'
synonyms:
- ECOTOX
- ECOTOXicology Knowledgebase
---
# ECOTOX Knowledgebase

## Overview

The ECOTOXicology Knowledgebase (ECOTOX) is the U.S. EPA's curated source of single-chemical toxicity test results for aquatic and terrestrial species, abstracted from the peer-reviewed literature. Records describe the chemical, the test species, the exposure conditions, and the measured effects and endpoints.

## Access

- Web search and explore interface, with export of results.
- Help and user documentation.

ECOTOX is a work of the U.S. federal government and is in the public domain. The TERA knowledge graph repackages ECOTOX chemical, taxonomy, and effect data as RDF.

## Citation

Olker JH, Elonen CM, Pilli A, et al. The ECOTOXicology Knowledgebase: A Curated Database of Ecologically Relevant Toxicity Tests to Support Environmental Research and Risk Assessment. Environ Toxicol Chem. 2022. doi:10.1002/etc.5324
