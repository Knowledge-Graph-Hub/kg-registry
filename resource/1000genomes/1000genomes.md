---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.internationalgenome.org/
  - contact_type: email
    value: info@1000genomes.org
  label: International Genome Sample Resource (EMBL-EBI)
creation_date: '2025-09-04T00:00:00Z'
description: The International Genome Sample Resource (IGSR) maintains and shares
  the open human genetic variation resources built by the 1000 Genomes Project, updates
  them to current reference assemblies (e.g., GRCh38), and incorporates new data sets
  and populations. IGSR provides a searchable data portal, bulk download methods,
  and guidance for proper reuse and citation.
domains:
- genomics
homepage_url: https://www.internationalgenome.org/
id: 1000genomes
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: https://www.internationalgenome.org/IGSR_disclaimer
  label: IGSR Data Disclaimer / Terms of Use
name: 1000 Genomes Project (IGSR)
products:
- category: GraphicalInterface
  description: Main IGSR website with links to data portal, help, and announcements
  format: http
  id: 1000genomes.portal
  name: IGSR Portal
  product_url: https://www.internationalgenome.org/
- category: GraphicalInterface
  description: Interactive data portal to browse IGSR/1000 Genomes data by sample,
    population, technology, data type, and collection
  format: http
  id: 1000genomes.data-portal
  name: IGSR Data Portal
  product_url: https://www.internationalgenome.org/data-portal
- category: Product
  description: Primary FTP site hosting IGSR and 1000 Genomes Project data collections
    and releases
  format: http
  id: 1000genomes.ftp
  name: IGSR FTP Site
  product_url: http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/
- category: DocumentationProduct
  description: Instructions for accessing IGSR data via Globus (recommended for bulk
    transfers)
  format: http
  id: 1000genomes.globus-docs
  name: Globus Access Instructions
  product_url: https://www.internationalgenome.org/faq/can-i-access-1000-genomes-data-globus-online
  warnings:
  - File was not able to be retrieved when checked on 2025-09-29_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.internationalgenome.org', port=443)_ Max
    retries exceeded with url_ /faq/can-i-access-1000-genomes-data-globus-online (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2025-09-29: Error connecting
    to URL: HTTPSConnectionPool(host=''www.internationalgenome.org'', port=443): Max
    retries exceeded with url: /faq/can-i-access-1000-genomes-data-globus-online (Caused
    by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: unable to get local issuer certificate (_ssl.c:1017)'')))'
  - File was not able to be retrieved when checked on 2025-09-27_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.internationalgenome.org', port=443)_ Max
    retries exceeded with url_ /faq/can-i-access-1000-genomes-data-globus-online (Caused
    by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate
    verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
- category: DocumentationProduct
  description: Instructions for downloading files using Aspera
  format: http
  id: 1000genomes.aspera-docs
  name: Aspera Download Instructions
  product_url: https://www.internationalgenome.org/faq/how-download-files-using-aspera
  warnings:
  - File was not able to be retrieved when checked on 2025-09-29_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.internationalgenome.org', port=443)_ Max
    retries exceeded with url_ /faq/how-download-files-using-aspera (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2025-09-29: Error connecting
    to URL: HTTPSConnectionPool(host=''www.internationalgenome.org'', port=443): Max
    retries exceeded with url: /faq/how-download-files-using-aspera (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
  - File was not able to be retrieved when checked on 2025-09-27_ Error connecting
    to URL_ HTTPSConnectionPool(host='www.internationalgenome.org', port=443)_ Max
    retries exceeded with url_ /faq/how-download-files-using-aspera (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
- category: Product
  description: Mirror of original 1000 Genomes Project data at NCBI
  format: http
  id: 1000genomes.ncbi-mirror
  name: NCBI Mirror
  product_url: https://ftp-trace.ncbi.nih.gov/1000genomes/ftp/
- category: Product
  description: Mirror of original 1000 Genomes Project data at DDBJ
  format: http
  id: 1000genomes.ddbj-mirror
  name: DDBJ Mirror
  product_url: https://ddbj.nig.ac.jp/public/mirror_database/1000genomes/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-09_ HTTP 502 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-06_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-12-05: HTTP 403 error
    when accessing file'
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
# 1000 Genomes Project (IGSR)

## Overview

The International Genome Sample Resource (IGSR) at EMBL-EBI maintains and extends the 1000 Genomes Project’s openly consented human variation resources. IGSR realigns data to current references (e.g., GRCh38), integrates high-coverage data sets (e.g., NYGC 30x), and adds collections from projects like HGDP, SGDP, GGVP, and HGSVC.

## Access

- Portal: main site with links to data and help
- Data Portal: browse by sample, population, technology, data type, and collection
- Bulk download: Globus (recommended), FTP, or Aspera
- Mirrors: NCBI and DDBJ, plus AWS Open Data

## Terms and citation

Use is governed by the IGSR Data Disclaimer/Terms of Use. Please cite the IGSR NAR publication and collection-specific publications as appropriate.