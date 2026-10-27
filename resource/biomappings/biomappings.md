---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: cthoyt
  label: Charles Tapley Hoyt
  orcid: 0000-0003-4423-4370
creation_date: '2026-10-27T00:00:00Z'
description: Biomappings is a community-curated repository of semantic mappings between
  biomedical identifiers (equivalences and related relations) that are missing from
  primary sources. It holds human-curated positive mappings, curated non-trivial negative
  (incorrect) mappings, and automatically predicted mappings awaiting review, all
  in SSSOM TSV format. Contributors curate predictions through a web curation interface
  or by pull request, and the mappings are released under CC0.
domains:
- metadata
- information technology
- biomedical
homepage_url: https://biopragmatics.github.io/biomappings/
id: biomappings
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Biomappings
products:
- category: MappingProduct
  description: Human-curated true (positive) semantic mappings between biomedical
    identifiers, in SSSOM TSV format.
  format: sssom
  id: biomappings.positive
  name: Biomappings Positive Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomappings
  product_file_size: 288990
  product_url: https://github.com/biopragmatics/biomappings/raw/main/src/biomappings/resources/positive.sssom.tsv
- category: MappingProduct
  description: Human-curated non-trivial false (incorrect) mappings, in SSSOM TSV
    format.
  format: sssom
  id: biomappings.negative
  name: Biomappings Negative Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomappings
  product_file_size: 45640
  product_url: https://github.com/biopragmatics/biomappings/raw/main/src/biomappings/resources/negative.sssom.tsv
- category: MappingProduct
  description: Automatically predicted mappings awaiting curation, in SSSOM TSV format.
  format: sssom
  id: biomappings.predictions
  name: Biomappings Predicted Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomappings
  product_file_size: 2556770
  product_url: https://github.com/biopragmatics/biomappings/raw/main/src/biomappings/resources/predictions.sssom.tsv
- category: ProcessProduct
  description: Biomappings Python package (MIT) for accessing, predicting, and curating
    mappings.
  format: python
  id: biomappings.code
  license:
    id: https://github.com/biopragmatics/biomappings/blob/main/LICENSE
    label: MIT
  name: Biomappings Python Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomappings
  product_url: https://github.com/biopragmatics/biomappings
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
- category: MappingProduct
  description: SeMRA Raw Semantic Mappings Database, pre-assembled semantic mappings
    from ontologies indexed in the Bioregistry, databases integrated in PyOBO, Biomappings,
    Wikidata, and custom SeMRA resources, published on Zenodo under CC0.
  format: sssom
  id: semra.raw-mappings
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
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
  product_url: https://doi.org/10.5281/zenodo.11082038
publications:
- authors:
  - Charles Tapley Hoyt
  - Amelia L. Hoyt
  - Benjamin M. Gyori
  doi: 10.1093/bioinformatics/btad130
  id: doi:10.1093/bioinformatics/btad130
  journal: Bioinformatics
  preferred: true
  title: Prediction and curation of missing biomedical identifier mappings with Biomappings
  year: '2023'
repository: https://github.com/biopragmatics/biomappings
---
# Biomappings

## Overview

Biomappings is a community-curated repository of semantic mappings between biomedical identifiers that are missing from the primary sources. It keeps human-curated positive mappings, curated incorrect (negative) mappings, and automatically predicted mappings waiting for review, all as SSSOM TSV files. Anyone can curate predictions through the web curation interface or by pull request.

## Access

- Positive, negative, and predicted mapping files (SSSOM TSV) in the GitHub repository.
- Python package for accessing, predicting, and curating mappings.

Mappings are released under CC0 1.0; the code is MIT-licensed. Software releases are archived on Zenodo (concept DOI 10.5281/zenodo.4323555). OxO2 and SeMRA both load Biomappings as a curated mapping set.

## Citation

Hoyt CT, Hoyt AL, Gyori BM. Prediction and curation of missing biomedical identifier mappings with Biomappings. Bioinformatics. 2023;39(4):btad130. doi:10.1093/bioinformatics/btad130