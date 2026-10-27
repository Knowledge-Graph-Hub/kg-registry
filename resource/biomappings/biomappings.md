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
  product_url: https://github.com/biopragmatics/biomappings/raw/main/src/biomappings/resources/negative.sssom.tsv
- category: MappingProduct
  description: Automatically predicted mappings awaiting curation, in SSSOM TSV format.
  format: sssom
  id: biomappings.predictions
  name: Biomappings Predicted Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomappings
  product_url: https://github.com/biopragmatics/biomappings/raw/main/src/biomappings/resources/predictions.sssom.tsv
- category: ProcessProduct
  description: Biomappings Python package (MIT) for accessing, predicting, and curating
    mappings.
  format: python
  id: biomappings.code
  name: Biomappings Python Package
  license:
    id: https://github.com/biopragmatics/biomappings/blob/main/LICENSE
    label: MIT
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomappings
  product_url: https://github.com/biopragmatics/biomappings
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
