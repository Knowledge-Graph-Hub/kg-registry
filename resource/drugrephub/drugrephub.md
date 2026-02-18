---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/center-development-therapeutics-cdot
  id: broad-cdot
  label: Broad Institute Center for the Development of Therapeutics (CDoT)
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/
  id: broad-institute
  label: Broad Institute
creation_date: '2026-01-22T00:00:00Z'
description: Curated collection of approved, clinical, and pre-clinical compounds
  with detailed annotations and sample metadata to support drug repurposing screens
  and analyses.
domains:
- drug discovery
- pharmacology
- biomedical
homepage_url: https://repo-hub.broadinstitute.org/repurposing
id: drugrephub
last_modified_date: '2026-01-22T00:00:00Z'
layout: resource_detail
name: Drug Repurposing Hub
products:
- category: Product
  description: Latest drug-level annotations including compound names, clinical phase,
    mechanism of action, and protein targets (listed as version 2025-08-19 on the
    site).
  format: tsv
  id: drugrephub.drug-info.tsv
  name: Drug Repurposing Hub Drug Information TSV
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-drug-annotation-20200324.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-02-15: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
  - File was not able to be retrieved when checked on 2026-02-13_ Error connecting
    to URL_ HTTPSConnectionPool(host='repo-hub.broadinstitute.org', port=443)_ Max
    retries exceeded with url_ /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
- category: Product
  description: Latest physical sample-level metadata including Broad sample IDs, vendor
    catalog numbers, SMILES, InChIKey, and PubChem IDs (listed as version 2025-08-19
    on the site).
  format: tsv
  id: drugrephub.sample-info.tsv
  name: Drug Repurposing Hub Sample Information TSV
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-sample-annotation-20240610.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-02-15: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
  - File was not able to be retrieved when checked on 2026-02-13_ Error connecting
    to URL_ HTTPSConnectionPool(host='repo-hub.broadinstitute.org', port=443)_ Max
    retries exceeded with url_ /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
- category: GraphProduct
  description: KGX graph package for Drug Repurposing Hub (build drug_rep_hub_2025-08-19_1.0_2025sep1_4.3.6;
    release 2025_12_15)
  format: kgx
  id: translator.drug_rep_hub.graph
  name: Translator Drug Repurposing Hub KGX Graph
  original_source:
  - drugrephub
  product_url: https://stars.renci.org/var/translator/releases/drug_rep_hub/2025_12_15/
  secondary_source:
  - translator
---
Drug Repurposing Hub is a curated, annotated library of approved, clinical, and pre-clinical compounds for screening and repurposing research.