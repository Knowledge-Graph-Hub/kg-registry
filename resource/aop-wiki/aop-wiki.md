---
activity_status: active
category: DataSource
collection:
- aop
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://aopwiki.org/info_pages/10
  label: AOP-Wiki Coordination Group
description: The AOP-Wiki is the primary collaborative authoring and curation interface
  for the Adverse Outcome Pathway Knowledge Base (AOP-KB). It enables the community
  to develop, review, browse, and export Adverse Outcome Pathways (AOPs) linking molecular
  initiating events through key events to adverse outcomes relevant to human and ecological
  risk assessment. Structured exports (XML and tabular subsets) support computational
  toxicology, ontology mapping, and integration into predictive assessment workflows.
domains: []
homepage_url: https://aopwiki.org/
id: aop-wiki
last_modified_date: '2025-09-04T00:00:00Z'
layout: resource_detail
license:
  id: https://aopwiki.org/
  label: Varies
name: AOP-Wiki
products:
- category: GraphicalInterface
  description: Web portal for browsing, authoring, and reviewing AOPs, key events
    (KEs), key event relationships (KERs), stressors, and supporting documentation
  format: http
  id: aop-wiki.portal
  name: AOP-Wiki Portal
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/
- category: Product
  description: Quarterly permanent XML snapshot (versioned) of AOP-Wiki content suitable
    for citation and archival use
  format: xml
  id: aop-wiki.quarterly-xml
  name: AOP-Wiki Quarterly XML Snapshot
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/downloads
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /downloads (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED]
    certificate verify failed: unable to get local issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Nightly XML export (rolling) containing latest AOP-Wiki content (overwritten
    daily)
  format: xml
  id: aop-wiki.nightly-xml
  name: AOP-Wiki Nightly XML Export
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/downloads/aop-wiki-xml.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop-wiki-xml.gz (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop-wiki-xml.gz (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop-wiki-xml.gz (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /downloads/aop-wiki-xml.gz (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Tab-delimited subset listing AOP to Key Event (including MIE, intermediate
    KE, and Adverse Outcome) associations
  format: tsv
  id: aop-wiki.ke-overview
  name: AOP-Wiki Key Events TSV
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/downloads/aop_ke_mie_ao.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_mie_ao.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_mie_ao.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_mie_ao.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /downloads/aop_ke_mie_ao.tsv (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Tab-delimited subset listing Key Event Relationships (KERs) with evidence
    and quantitative understanding indicators
  format: tsv
  id: aop-wiki.ker
  name: AOP-Wiki Key Event Relationships TSV
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/downloads/aop_ke_ker.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_ker.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_ker.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_ker.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /downloads/aop_ke_ker.tsv (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Tab-delimited subset of Key Event Components (actions, biological objects/processes
    with ontology references)
  format: tsv
  id: aop-wiki.ke-components
  name: AOP-Wiki Key Event Components TSV
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/downloads/aop_ke_ec.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_ec.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_ec.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /downloads/aop_ke_ec.tsv (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /downloads/aop_ke_ec.tsv (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Per-AOP dynamic XML feed accessible via each AOP page (XML button)
    for up-to-minute content retrieval
  format: xml
  id: aop-wiki.dynamic-aop-xml
  name: AOP-Wiki Dynamic AOP XML Feed
  original_source:
  - aop-wiki
  product_url: https://aopwiki.org/aops
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /aops (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /aops (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /aops (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /aops (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED]
    certificate verify failed: unable to get local issuer certificate (_ssl.c:1017)'')))'
- category: DocumentationProduct
  description: This document is the AOP Developers' Handbook supplement to the Guidance
    Document for developing and assessing Adverse Outcome Pathways (AOPs). The Guidance
    Document provides a historical background for the AOP development programme, and
    outlines the elements required to construct an AOP as well as the principles of
    the AOP framework.
  format: http
  id: aop-wiki.devhandbook
  name: AOP Developers' Handbook
  product_url: https://aopwiki.org/handbooks/4
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /handbooks/4 (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /handbooks/4 (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='aopwiki.org', port=443)_ Max retries exceeded
    with url_ /handbooks/4 (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer
    certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''aopwiki.org'', port=443): Max retries exceeded
    with url: /handbooks/4 (Caused by SSLError(SSLCertVerificationError(1, ''[SSL:
    CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer
    certificate (_ssl.c:1017)'')))'
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - aop-wiki
  - ctd
  - toxcast
  - disgenet
  - ncbigene
  - string
  - 1000genomes
  - ensembl
  - gwascatalog
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
  secondary_source:
  - aop-db
---
# AOP-Wiki

## Overview

The AOP-Wiki is the collaborative platform of the Adverse Outcome Pathway Knowledge Base (AOP-KB). It captures structured mechanistic knowledge describing how molecular initiating events propagate through measurable key events to adverse outcomes of regulatory relevance. The resource supports transparent evidence organization, peer review, and reuse across chemical safety evaluation, risk prioritization, and method development.

## Data & Exports

Multiple export modalities enable programmatic reuse:

- Quarterly XML snapshots (stable, citable)
- Nightly rolling XML (latest content)
- Dynamic XML feed per AOP (on-demand freshness)
- Targeted TSV subsets (key events, key event relationships, key event components)

## Use Cases

- Mechanistic evidence mapping and visualization
- Integrating AOP structures into predictive toxicology pipelines
- Identifying knowledge gaps in AOP development
- Ontology alignment and cross-resource linking

## Governance & Community

Content is community-authored and coordinated via the AOP-Wiki Coordination Group with international participation (academia, government, and NGOs). Peer review pathways align with OECD processes for AOP endorsement.

## Access Notes

Dynamic per-AOP XML feeds are obtained directly from individual AOP pages (XML button). Nightly and quarterly exports plus TSV subsets are documented on the Download Options page.

## Citation

When reusing AOP-Wiki content, cite the AOP-Wiki (access date), relevant quarterly snapshot (if used), and any underlying ontologies or complementary resources referenced in analyses.