---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@sleepdata.org
  - contact_type: url
    value: https://sleepdata.org/contact
  label: National Sleep Research Resource, Brigham and Women's Hospital
creation_date: '2026-10-05T00:00:00Z'
description: The National Sleep Research Resource (NSRR) is an NHLBI-supported repository,
  launched in April 2014, that shares de-identified sleep data from cohort studies,
  clinical trials and other sources. It hosts tens of thousands of polysomnography
  and actigraphy recordings (mostly as EDF signal files with annotations) plus questionnaire,
  demographic and clinical covariate data from more than 50 datasets, such as the
  Sleep Heart Health Study, MESA Sleep, MrOS Sleep and CHAT. Core variables are harmonized
  across datasets, and data are downloaded after an approved data access request.
  NSRR is integrating its data into NHLBI BioData Catalyst.
domains:
- biomedical
- clinical
homepage_url: https://sleepdata.org/
id: nsrr
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://sleepdata.org/datasets
  label: Controlled access; individual-level data require an approved NSRR Data Access
    and Use Agreement for each dataset
name: National Sleep Research Resource
products:
- category: GraphicalInterface
  description: NSRR web portal for browsing datasets, searching variables, reading
    documentation and forum posts, and requesting and downloading sleep study data.
  format: http
  id: nsrr.portal
  name: NSRR Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://sleepdata.org/
  warnings:
  - When checked on 2026-10-05, the server did not send its intermediate TLS certificate,
    so clients that verify certificates strictly (such as curl) failed with an unknown
    CA error. The site loaded when certificate verification was skipped.
- category: Product
  description: Catalog of more than 50 sleep datasets (polysomnography, actigraphy
    and questionnaire data from children and adults, plus a few animal studies), each
    with documentation, file listings, a variable data dictionary and a data access
    request link. Files can be downloaded only after an access request is approved.
  format: mixed
  id: nsrr.datasets
  is_public: false
  name: NSRR Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://sleepdata.org/datasets
  warnings:
  - When checked on 2026-10-05, the server did not send its intermediate TLS certificate,
    so clients that verify certificates strictly (such as curl) failed with an unknown
    CA error. The site loaded when certificate verification was skipped.
- category: GraphicalInterface
  description: NSRR Dataset Discovery tool (cohort matrix) for finding datasets by
    keyword or data modality, including subject type, sleep study data category and
    signal channel labels.
  format: http
  id: nsrr.dataset-discovery
  name: NSRR Dataset Discovery
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://matrix.sleepdata.org/
- category: ProcessProduct
  description: Online data access request process. Users sign in, complete a request
    describing the intended use, and agree to the dataset's Data Access and Use Agreement;
    the NSRR team reviews requests, which can take up to two weeks. This example URL
    starts a request for the Sleep Heart Health Study.
  format: http
  id: nsrr.data-request
  name: NSRR Data Access Request
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://sleepdata.org/data/requests/shhs/start
  warnings:
  - When checked on 2026-10-05, the server did not send its intermediate TLS certificate,
    so clients that verify certificates strictly (such as curl) failed with an unknown
    CA error. The site loaded when certificate verification was skipped.
- category: DocumentationProduct
  description: Documentation and scripts for NSRR harmonized variables, covering non-sleep
    phenotypes, polysomnography and polygraphy, actigraphy and sleep questionnaires,
    with JSON definitions of harmonized variables and coded domains.
  format: mixed
  id: nsrr.harmonization
  name: NSRR Data Harmonization
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://github.com/nsrr/nsrr_data_harmonization
- category: MappingProduct
  description: Version-controlled NSRR canonical data dictionary and mapping files
    linking variables across NSRR datasets.
  format: mixed
  id: nsrr.cross-dataset-mapping
  name: NSRR Cross-Dataset Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://github.com/nsrr/cross-dataset-mapping
- category: ProgrammingInterface
  description: NSRR Ruby gem and command-line tool for downloading NSRR files with
    a user token, integrating data dictionaries, and building custom Ruby applications.
  format: http
  id: nsrr.gem
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: NSRR Ruby Gem
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://github.com/nsrr/nsrr-gem
  repository: https://github.com/nsrr/nsrr-gem
- category: ProgrammingInterface
  description: R package, contributed by John Muschelli and Ciprian Crainiceanu, for
    listing and downloading NSRR files directly from R.
  format: http
  id: nsrr.r-package
  name: nsrr R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://cran.r-project.org/web/packages/nsrr/index.html
- category: GraphicalInterface
  description: Source code for the NSRR EDF Editor and Translator, a tool for working
    with European Data Format (EDF) sleep signal files and their annotations.
  format: http
  id: nsrr.edf-editor-translator
  name: NSRR EDF Editor and Translator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://github.com/nsrr/edf-editor-translator
  repository: https://github.com/nsrr/edf-editor-translator
- category: GraphicalInterface
  description: MATLAB viewer for EDF polysomnography signal files and their NSRR annotations.
  format: http
  id: nsrr.edf-viewer
  name: NSRR EDF Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://github.com/nsrr/edf-viewer
  repository: https://github.com/nsrr/edf-viewer
- category: ProgrammingInterface
  description: Luna, an open-source C/C++ library and command-line tool for analyzing
    large numbers of sleep studies, on which the NSRR signal processing pipeline is
    based.
  format: http
  id: nsrr.luna
  name: Luna
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://github.com/remnrem/luna-base
  repository: https://github.com/remnrem/luna-base
- category: DocumentationProduct
  description: NSRR tools page listing analysis software, the NSRR gem, Spout data
    dictionary tooling and other utilities for working with NSRR data.
  format: http
  id: nsrr.tools
  name: NSRR Tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://sleepdata.org/tools
  warnings:
  - When checked on 2026-10-05, the server did not send its intermediate TLS certificate,
    so clients that verify certificates strictly (such as curl) failed with an unknown
    CA error. The site loaded when certificate verification was skipped.
- category: DocumentationProduct
  description: About page describing the NSRR mission, datasets, data harmonization,
    analysis tools and the collaboration with NHLBI BioData Catalyst.
  format: http
  id: nsrr.docs
  name: About the NSRR
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nsrr
  product_url: https://sleepdata.org/pages/about
  warnings:
  - When checked on 2026-10-05, the server did not send its intermediate TLS certificate,
    so clients that verify certificates strictly (such as curl) failed with an unknown
    CA error. The site loaded when certificate verification was skipped.
publications:
- authors:
  - Guo-Qiang Zhang
  - Licong Cui
  - Remo Mueller
  - Shiqiang Tao
  - Matthew Kim
  - Michael Rueschman
  - Sara Mariani
  - Daniel Mobley
  - Susan Redline
  doi: 10.1093/jamia/ocy064
  id: doi:10.1093/jamia/ocy064
  journal: Journal of the American Medical Informatics Association
  preferred: true
  title: 'The National Sleep Research Resource: towards a sleep data commons'
  year: '2018'
- authors:
  - Dennis A. Dean
  - Ary L. Goldberger
  - Remo Mueller
  - Matthew Kim
  - Michael Rueschman
  - Daniel Mobley
  - Satya S. Sahoo
  - Catherine P. Jayapandian
  - Licong Cui
  - Michael G. Morrical
  - Susan Surovec
  - Guo-Qiang Zhang
  - Susan Redline
  doi: 10.5665/sleep.5774
  id: doi:10.5665/sleep.5774
  journal: Sleep
  title: 'Scaling Up Scientific Discovery in Sleep Medicine: The National Sleep Research
    Resource'
  year: '2016'
repository: https://github.com/nsrr
synonyms:
- NSRR
- sleepdata.org
taxon:
- NCBITaxon:9606
---
# National Sleep Research Resource

The National Sleep Research Resource (NSRR) is a repository for sharing sleep data, supported by the National Heart, Lung, and Blood Institute (NHLBI) and run from Brigham and Women's Hospital. It launched in April 2014 to support secondary analysis, algorithm development and signal processing research in sleep and circadian science.

## Data

NSRR hosts more than 50 datasets from cohort studies and clinical trials, including the Sleep Heart Health Study (SHHS), MESA Sleep, MrOS Sleep, the Childhood Adenotonsillectomy Trial (CHAT), HCHS/SOL and the Wisconsin Sleep Cohort. Data include overnight polysomnography and polygraphy signals (EDF files with annotations), actigraphy, questionnaires, and demographic and clinical covariates. Each dataset has a versioned data dictionary, managed with the Spout tool and published on GitHub. Core variables are harmonized across datasets.

## Access

Browsing dataset documentation and data dictionaries is open. Downloading individual-level data requires an NSRR account and an approved data access request, under a Data Access and Use Agreement for each dataset. Files can then be downloaded through the website, the NSRR Ruby gem, or the `nsrr` R package. NSRR is also integrating its data into NHLBI BioData Catalyst.

## Tools

The NSRR GitHub organization publishes its open-source tools: the EDF Editor and Translator, an EDF viewer, the `edfize` EDF validator, the Spout data dictionary tool, and harmonization and cross-dataset mapping files. NSRR's signal processing pipeline is based on the Luna library.
