---
activity_status: active
category: Dataset
creation_date: '2026-01-15T00:00:00Z'
description: The TRY Plant Trait Database aggregates global plant trait measurements
  contributed by researchers and institutions, widely used for ecological and metabolomic
  analyses.
domains:
- biological systems
homepage_url: https://www.try-db.org/TryWeb/Home.php
id: try
infores_id: try
last_modified_date: '2026-01-15T00:00:00Z'
layout: resource_detail
name: TRY Plant Trait Database
products:
- category: Product
  description: Trait data available through the TRY data portal (access upon request/registration)
  format: http
  id: try.portal
  name: TRY Data Portal
  original_source:
  - try
  product_url: https://www.try-db.org/TryWeb/Home.php
  warnings:
  - File was not able to be retrieved when checked on 2026-02-20_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.try-db.org', port=443)_ Max retries exceeded
    with url_ /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-02-18_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.try-db.org', port=443)_ Max retries exceeded
    with url_ /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.try-db.org', port=443)_ Max retries exceeded
    with url_ /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2026-02-21: Error connecting
    to URL: HTTPSConnectionPool(host=''www.try-db.org'', port=443): Max retries exceeded
    with url: /TryWeb/Home.php (Caused by SSLError(SSLCertVerificationError(1, ''[SSL:
    CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer
    certificate (_ssl.c:1000)'')))'
- category: GraphProduct
  description: Graph version of the Earth Metabolome Initiative Ontology
  format: kgx
  id: emikg.kg
  name: EMI Knowledge Graph
  original_source:
  - emi
  - pf1600
  - globi
  - try
  product_url: https://doi.org/10.5281/zenodo.17079767
  repository: https://github.com/earth-metabolome-initiative/metrin-kg
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting
    to URL
- category: ProgrammingInterface
  description: SPARQL endpoint for programmatic access to the EMI Knowledge Graph
  format: http
  id: emikg.sparql
  name: EMI KG SPARQL Endpoint
  original_source:
  - emi
  - pf1600
  - globi
  - try
  product_url: https://qlever.earthmetabolome.org/api/metrin-kg
- category: GraphicalInterface
  description: Web-based SPARQL query editor for the EMI Knowledge Graph
  id: emikg.web
  name: EMI KG SPARQL Query Editor
  original_source:
  - emi
  - pf1600
  - globi
  - try
  product_url: https://sib-swiss.github.io/sparql-editor/emi
---
# TRY Plant Trait Database

## Overview

TRY provides harmonized plant trait data collected worldwide. Data access is provided through the TRY web portal and is commonly used as a source in ecological knowledge graphs such as METRIN-KG.