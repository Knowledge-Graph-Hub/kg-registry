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
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='repo-hub.broadinstitute.org', port=443)_ Max
    retries exceeded with url_ /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='repo-hub.broadinstitute.org', port=443)_ Max
    retries exceeded with url_ /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-04-10: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
  - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-drug-annotation-20200324.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
- category: Product
  description: Latest physical sample-level metadata including Broad sample IDs, vendor
    catalog numbers, SMILES, InChIKey, and PubChem IDs (listed as version 2025-08-19
    on the site).
  format: tsv
  id: drugrephub.sample-info.tsv
  name: Drug Repurposing Hub Sample Information TSV
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-sample-annotation-20240610.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='repo-hub.broadinstitute.org', port=443)_ Max
    retries exceeded with url_ /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='repo-hub.broadinstitute.org', port=443)_ Max
    retries exceeded with url_ /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-04-10: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
  - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting
    to URL: HTTPSConnectionPool(host=''repo-hub.broadinstitute.org'', port=443): Max
    retries exceeded with url: /public/data/repo-sample-annotation-20240610.txt (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Drug Repurposing Hub distributed via the
    NCATS Translator release site (release 2026_03_06; build drug_rep_hub_2025-08-19_99c18ef1_2025sep1_4.3.6;
    source version 2025-08-19; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 19389
  format: kgx-jsonl
  id: translator.drug_rep_hub.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Drug Repurposing Hub KGX Graph
  node_count: 8842
  original_source:
  - drugrephub
  product_url: https://kgx-storage.rtx.ai/releases/drug_rep_hub/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_06'
  - drug_rep_hub_2025-08-19_99c18ef1_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - alliance
  - bgee
  - bindingdb
  - chembl
  - cohd
  - ctd
  - ctkp
  - drug-approvals-kp
  - dgidb
  - diseases
  - drugrephub
  - drugcentral
  - gtopdb
  - gene2phenotype
  - geneticskp
  - go-cam
  - goa
  - hp
  - icees-kg
  - intact
  - ncbigene
  - panther
  - pathbank
  - semmeddb
  - sider
  - signor
  - text-mining-kp
  - ttd
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - 423af7989cac
---
Drug Repurposing Hub is a curated, annotated library of approved, clinical, and pre-clinical compounds for screening and repurposing research.