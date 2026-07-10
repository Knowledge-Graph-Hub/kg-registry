---
activity_status: active
category: Dataset
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jkattge@bgc-jena.mpg.de
  label: Jens Kattge
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.bgc-jena.mpg.de/
  label: Max Planck Institute for Biogeochemistry
creation_date: '2026-01-15T00:00:00Z'
description: The TRY Plant Trait Database aggregates global plant trait measurements
  contributed by researchers and institutions, widely used for ecological and metabolomic
  analyses.
domains:
- biological systems
homepage_url: https://www.try-db.org/TryWeb/Home.php
id: try
infores_id: try
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.try-db.org/TryWeb/TRY_Intellectual_Property_Guidelines.pdf
  label: CC BY (TRY Data Intellectual Property Guidelines)
name: TRY Plant Trait Database
products:
- category: Product
  description: Trait data available through the TRY data portal (access upon request/registration)
  format: http
  id: try.portal
  name: TRY Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: try
  product_url: https://www.try-db.org/TryWeb/Home.php
  warnings:
  - File was not able to be retrieved when checked on 2026-03-08_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.try-db.org', port=443)_ Max retries exceeded
    with url_ /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-02-24_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.try-db.org', port=443)_ Max retries exceeded
    with url_ /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.try-db.org', port=443)_ Max retries exceeded
    with url_ /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1017)')))
- category: GraphProduct
  description: Graph version of the Earth Metabolome Initiative Ontology
  format: kgx
  id: emikg.kg
  name: EMI Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emi
  - relation_type: prov:hadPrimarySource
    source: emikg
  - relation_type: prov:hadPrimarySource
    source: globi
  - relation_type: prov:hadPrimarySource
    source: pf1600
  - relation_type: prov:hadPrimarySource
    source: try
  product_url: https://doi.org/10.5281/zenodo.17079767
  repository: https://github.com/earth-metabolome-initiative/metrin-kg
  warnings: []
- category: ProgrammingInterface
  description: SPARQL endpoint for programmatic access to the EMI Knowledge Graph
  format: http
  id: emikg.sparql
  name: EMI KG SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emi
  - relation_type: prov:hadPrimarySource
    source: emikg
  - relation_type: prov:hadPrimarySource
    source: globi
  - relation_type: prov:hadPrimarySource
    source: pf1600
  - relation_type: prov:hadPrimarySource
    source: try
  product_url: https://qlever.earthmetabolome.org/api/metrin-kg
- category: GraphicalInterface
  description: Web-based SPARQL query editor for the EMI Knowledge Graph
  id: emikg.web
  name: EMI KG SPARQL Query Editor
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emi
  - relation_type: prov:hadPrimarySource
    source: emikg
  - relation_type: prov:hadPrimarySource
    source: globi
  - relation_type: prov:hadPrimarySource
    source: pf1600
  - relation_type: prov:hadPrimarySource
    source: try
  product_url: https://sib-swiss.github.io/sparql-editor/emi
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/31891233
  authors:
  - Jens Kattge
  - Gerhard Bönisch
  - Sandra Díaz
  - Sandra Lavorel
  - Iain Colin Prentice
  doi: 10.1111/gcb.14904
  journal: Global Change Biology
  preferred: true
  title: TRY plant trait database – enhanced coverage and open access
  year: '2020'
- id: doi:10.1111/j.1365-2486.2011.02451.x
  authors:
  - Jens Kattge
  - Sandra Díaz
  - Sandra Lavorel
  - Iain Colin Prentice
  - Paul Leadley
  doi: 10.1111/j.1365-2486.2011.02451.x
  journal: Global Change Biology
  title: TRY – a global database of plant traits
  year: '2011'
---
# TRY Plant Trait Database

## Overview

TRY provides harmonized plant trait data collected worldwide. Data access is provided through the TRY web portal and is commonly used as a source in ecological knowledge graphs such as METRIN-KG.