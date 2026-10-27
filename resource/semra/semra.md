---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: cthoyt
  label: Charles Tapley Hoyt
  orcid: 0000-0003-4423-4370
creation_date: '2026-10-27T00:00:00Z'
description: SeMRA (Semantic Mapping Reasoner and Assembler) is a Python package and
  dataset for assembling and reasoning over semantic mappings at scale. It provides
  an SSSOM-based object model for mappings, inference over chains of mappings, a provenance
  model for automatically generated mappings, and a confidence model at the curator,
  mapping-set, and community levels. The SeMRA Raw Semantic Mappings Database is a
  pre-assembled set of semantic mappings drawn from hundreds of ontologies and databases,
  published on Zenodo and rebuildable with `semra build`, alongside domain-specific
  processed mapping databases.
domains:
- metadata
- information technology
- biomedical
homepage_url: https://github.com/biopragmatics/semra
id: semra
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/biopragmatics/semra/blob/main/LICENSE
  label: MIT
name: SeMRA (Semantic Mapping Reasoner and Assembler)
products:
- category: MappingProduct
  description: SeMRA Raw Semantic Mappings Database, pre-assembled semantic mappings
    from ontologies indexed in the Bioregistry, databases integrated in PyOBO, Biomappings,
    Wikidata, and custom SeMRA resources, published on Zenodo under CC0.
  format: sssom
  id: semra.raw-mappings
  name: SeMRA Raw Semantic Mappings Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semra
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: wikidata
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  product_url: https://doi.org/10.5281/zenodo.11082038
- category: ProcessProduct
  description: SeMRA Python package for assembling, reasoning over, and processing
    semantic mappings.
  format: python
  id: semra.code
  name: SeMRA Python Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://github.com/biopragmatics/semra
- category: DocumentationProduct
  description: SeMRA documentation on Read the Docs.
  format: http
  id: semra.docs
  name: SeMRA Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://semra.readthedocs.io/
- category: GraphicalInterface
  description: OxO2 web interface for searching and browsing ontology cross-references
    and SSSOM mappings, including asserted mappings from OLS ontologies and curated
    mapping sets, plus inferred cross-set mappings
  format: http
  id: oxo.portal
  name: OxO Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://www.ebi.ac.uk/spot/oxo/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/spot/oxo/api/v2
  description: OxO2 REST API (OpenAPI 3) for querying mappings, mapping sets, and
    ontologies; supports SSSOM-shaped JSON and SSSOM TSV export of mapping search
    results. Also exposes legacy OxO v1-compatible endpoints.
  format: http
  id: oxo.api
  is_public: true
  name: OxO2 REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://www.ebi.ac.uk/spot/oxo/swagger-ui.html
repository: https://github.com/biopragmatics/semra
synonyms:
- SeMRA
- Semantic Mapping Reasoner and Assembler
---
# SeMRA (Semantic Mapping Reasoner and Assembler)

## Overview

SeMRA is a Python package for assembling semantic mappings from many sources and reasoning over them at scale. It provides an SSSOM-based object model, inference over chains of mappings, and models for provenance and confidence.

## Access

- SeMRA Raw Semantic Mappings Database on Zenodo: concept DOI 10.5281/zenodo.11082038. The latest version found is 10.5281/zenodo.15504009 (2025-05-24).
- Python package and source code (MIT license), with software releases archived at 10.5281/zenodo.8192828.
- Documentation: https://semra.readthedocs.io/

The Raw Semantic Mappings Database is released under CC0 and incorporates mappings from ontologies indexed in the Bioregistry, databases integrated in PyOBO, Biomappings, Wikidata, and custom SeMRA resources. OxO2 loads SeMRA mapping sets. No peer-reviewed SeMRA paper was found as of 2026-10-27.
