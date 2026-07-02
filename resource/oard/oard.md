---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: Department of Biomedical Informatics, Columbia University (Weng Lab)
  contact_details:
  - contact_type: url
    value: https://www.dbmi.columbia.edu/oard-rare-disease-research/
  - contact_type: email
    value: cw2384@cumc.columbia.edu
creation_date: '2026-07-01T00:00:00Z'
description: >-
  OARD (Open Annotations for Rare Diseases) is a web resource and RESTful API that
  provides data-driven associations between rare diseases and their phenotypes and
  co-morbidities, mined from large-scale de-identified electronic health records.
  Developed by the Weng Lab in the Department of Biomedical Informatics at Columbia
  University, OARD is built from more than 10 million de-identified patient records
  drawn from Columbia University Irving Medical Center (CUIMC) and Children's
  Hospital of Philadelphia (CHOP). Only aggregate frequency and co-occurrence
  statistics (no individual-level data) are stored, and disease-phenotype
  association analyses are computed on the fly per query. Diseases are represented
  using Mondo, OMIM, and Orphanet identifiers and phenotypes using the Human
  Phenotype Ontology (HPO), with clinical concepts grounded in the OMOP common
  data model.
domains:
- clinical
- biomedical
homepage_url: https://www.dbmi.columbia.edu/oard-rare-disease-research/
id: oard
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: OARD (Open Annotations for Rare Diseases)
products:
- category: ProgrammingInterface
  id: oard.api
  name: OARD Web Application and API
  description: OARD public web application and RESTful web API for querying
    data-driven associations between rare diseases and their phenotypes and
    co-morbidities derived from de-identified electronic health records. The public
    service is deployed at https://rare.cohd.io/ on NCATS AWS infrastructure; the
    application and API source are maintained on GitHub.
  format: http
  product_url: https://github.com/WengLab-InformaticsResearch/cohd-rare
  original_source:
  - source: oard
    relation_type: prov:hadPrimarySource
publications:
- id: https://doi.org/10.1016/j.ajhg.2022.08.002
  doi: 10.1016/j.ajhg.2022.08.002
  title: 'OARD: Open annotations for rare diseases and their phenotypes based on
    real-world data'
  journal: The American Journal of Human Genetics
  year: '2022'
  preferred: true
  authors:
  - Liu C
  - Ta CN
  - Havrilla JM
  - Nestor JG
  - Spotnitz ME
  - Geneslaw AS
  - Hu Y
  - Chung WK
  - Wang K
  - Weng C
repository: https://github.com/WengLab-InformaticsResearch/oard-react
---
# OARD (Open Annotations for Rare Diseases)

## Overview

OARD (Open Annotations for Rare Diseases) is a data-driven resource that surfaces
associations between rare diseases and their phenotypes and co-morbidities, derived
from real-world data in large-scale de-identified electronic health records. It was
developed by the Weng Lab in the Department of Biomedical Informatics at Columbia
University and is served to the public through a web application and a RESTful web
API at https://rare.cohd.io/.

## Data and methods

OARD is built from more than 10 million de-identified patient records from Columbia
University Irving Medical Center (CUIMC) and Children's Hospital of Philadelphia
(CHOP). Rather than storing individual-level data, OARD retains aggregate frequency
and co-occurrence statistics and computes disease-phenotype association measures on
the fly in response to each query. This EHR-driven approach was designed to be more
generalizable and scalable than expert-driven curation of rare-disease annotations.

## Vocabularies

Rare diseases are represented using Mondo, OMIM, and Orphanet identifiers, and
phenotypes are represented using the Human Phenotype Ontology (HPO). Clinical
concepts are grounded in the OMOP common data model, building on the Columbia Open
Health Data (COHD) infrastructure.

## Citation

Liu C, Ta CN, Havrilla JM, et al. OARD: Open annotations for rare diseases and their
phenotypes based on real-world data. The American Journal of Human Genetics. 2022.
doi:10.1016/j.ajhg.2022.08.002
