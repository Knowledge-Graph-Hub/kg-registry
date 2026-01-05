---
activity_status: active
category: DataSource
creation_date: '2025-10-27T00:00:00Z'
description: snoDB is a specialized database of human small nucleolar RNAs (snoRNAs),
  integrating data from established databases with manually curated literature. It
  provides comprehensive information on snoRNA genomic locations, sequences, conservation,
  host genes, snoRNA-RNA interactions, snoRNA-protein interactions, and abundance
  data across tissues and cancer cells.
domains:
- genomics
- biological systems
homepage_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
id: snodb
last_modified_date: '2025-10-27T00:00:00Z'
layout: resource_detail
name: snoDB
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and analyzing human snoRNA data
    with interactive tables and visualization tools
  format: http
  id: snodb.portal
  name: snoDB 2.0 Portal
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
- category: GraphicalInterface
  description: Interactive abundance viewer for visualizing snoRNA expression across
    tissues and cell lines
  format: http
  id: snodb.abundance-viewer
  name: Abundance Viewer
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
- category: GraphicalInterface
  description: Browser for exploring rRNA chemical modification sites and their guide
    snoRNAs
  format: http
  id: snodb.rrna-modifications
  name: rRNA Chemical Modifications Browser
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/rRNA_modifications/
- category: GraphicalInterface
  description: Statistics dashboard showing snoRNA type distributions, length distributions,
    and target biotypes
  format: http
  id: snodb.statistics
  name: Statistics Dashboard
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/statistics/
- category: GraphicalInterface
  description: Sequence similarity search tool for finding snoRNAs by sequence
  format: http
  id: snodb.sequence-search
  name: Sequence Search Tool
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/sequence_similarity_search/
- category: Product
  description: Database of human snoRNA sequences with GRCh38 genomic coordinates
  format: http
  id: snodb.sequences
  name: snoRNA Sequences
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Conservation data including PhastCons scores for 100 vertebrates from
    UCSC genome browser
  format: http
  id: snodb.conservation
  name: Conservation Data
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: snoRNA motif sequences and guide regions (boxes C, D, C', D' for C/D
    box snoRNAs; H and ACA boxes for H/ACA snoRNAs)
  format: http
  id: snodb.motifs
  name: Motif and Guide Region Data
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Host gene information with functional annotations from Gene Ontology
  format: http
  id: snodb.host-genes
  name: Host Gene Data
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Canonical snoRNA-rRNA and snoRNA-snRNA interactions from multiple sources
  format: http
  id: snodb.canonical-interactions
  name: Canonical snoRNA-RNA Interactions
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Non-canonical snoRNA-RNA interactions from RISE database
  format: http
  id: snodb.noncanonical-interactions
  name: Non-canonical snoRNA-RNA Interactions
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: snoRNA-protein interactions from ENCODE eCLIP data of 150 RNA binding
    proteins
  format: http
  id: snodb.protein-interactions
  name: snoRNA-Protein Interactions
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: snoRNA and host gene abundance data from TGIRT-Seq across tissues and
    cancer cell lines
  format: http
  id: snodb.abundance
  name: Abundance Data
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: rRNA modification positions with validation status and modification
    levels from multiple studies
  format: http
  id: snodb.rrna-mods
  name: rRNA Modification Data
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/rRNA_modifications/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/rRNA_modifications/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/rRNA_modifications/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/rRNA_modifications/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/rRNA_modifications/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: snoRNA copy information based on RFAM classification
  format: http
  id: snodb.copies
  name: snoRNA Copy Data
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Exportable data tables with advanced search and filtering capabilities
  format: http
  id: snodb.export
  name: Data Export
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: ProcessProduct
  description: Tool for integrating snoDB snoRNAs into Ensembl or RefSeq GTF annotation
    files
  format: http
  id: snodb.snorupdate
  name: snoRupdate
  product_url: https://github.com/scottgroup/snoRupdate
- category: DocumentationProduct
  description: Comprehensive documentation about data sources, methods, and curation
    processes
  format: http
  id: snodb.about
  name: About and Help Documentation
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/about/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/about/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/about/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/about/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/about/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: DocumentationProduct
  description: Interactive tutorial for navigating and using snoDB features
  format: http
  id: snodb.tutorial
  name: Tutorial
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/tutorial/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/tutorial/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/tutorial/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/tutorial/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/tutorial/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: DocumentationProduct
  description: Detailed information about TGIRT-Seq data processing and experimental
    methods
  format: http
  id: snodb.experiment-details
  name: Experiment Details
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/experiment_details/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/experiment_details/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-03_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/experiment_details/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='bioinfo-scottgroup.med.usherbrooke.ca', port=443)_
    Max retries exceeded with url_ /snoDB/experiment_details/ (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - 'File was not able to be retrieved when checked on 2026-01-05: Error connecting
    to URL: HTTPSConnectionPool(host=''bioinfo-scottgroup.med.usherbrooke.ca'', port=443):
    Max retries exceeded with url: /snoDB/experiment_details/ (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/help/public-database
publications:
- authors:
  - Bergeron
  - Paraqindes
  - Fafard-Couture
  - Deschamps-Francoeur
  - Faucher-Giguère
  - Bouchard-Bourelle
  - Abou Elela
  - Catez
  - Marcel
  - Scott
  id: https://pubmed.ncbi.nlm.nih.gov/36165892/
  journal: Nucleic Acids Research
  preferred: true
  title: 'snoDB 2.0: an enhanced interactive database, specializing in human snoRNAs'
  year: '2023'
taxon:
- NCBITaxon:9606
---
# snoDB

snoDB 2.0 is a specialized database dedicated to human small nucleolar RNAs (snoRNAs), providing comprehensive and up-to-date information in an interactive format. Developed at the Université de Sherbrooke, snoDB integrates data from multiple established databases with extensive manual curation from the literature.

## Overview

The database was created to address the need for accurate, centralized information about human snoRNAs. snoDB removes redundancy by merging snoRNA entries from multiple sources based on genomic location, prioritizing data from Ensembl, RefSeq, snoRNA Atlas, snOPY, and literature-based annotations.

## Key Features

### Genomic and Sequence Data
- **Genomic Locations**: All coordinates based on GRCh38 human genome assembly
- **Sequences**: Complete snoRNA sequences with nucleotide-level detail
- **Conservation**: PhastCons conservation scores for 100 vertebrates from UCSC genome browser
- **Host Genes**: Comprehensive host gene information with Gene Ontology functional annotations
- **snoRNA Copies**: Classification based on RFAM families

### snoRNA Structure and Function
- **Motifs and Guide Regions**: Box C, D, C', D' for C/D box snoRNAs; H and ACA boxes for H/ACA snoRNAs
- **Predicted Elements**: Custom algorithms for predicting boxes when not available in literature
- **Target Identification**: Both canonical (rRNA/snRNA) and non-canonical RNA targets

### Interaction Data
- **snoRNA-RNA Interactions**:
  - Canonical interactions with rRNA and snRNA from multiple validated sources
  - Non-canonical interactions from RISE database
  - snoDB-predicted interactions for unannotated snoRNA copies
  
- **snoRNA-Protein Interactions**:
  - Data from ENCODE eCLIP experiments
  - 150 RNA binding proteins analyzed
  - Filtered for high-confidence interactions (p-value < 0.001)

### Expression and Abundance
- **Tissue Expression**: TGIRT-Seq data from multiple normal tissues (brain, liver, testis, skeletal muscle, ovary, breast, prostate)
- **Cancer Cell Lines**: Expression in HCT116, MCF7, PC3, TOV112D, SKOV
- **Reference Samples**: Universal Human RNA (UHR) and Human Brain Reference (HBR)
- **Host Gene Abundance**: Parallel abundance measurements for host genes

### rRNA Modifications
- **Modification Sites**: Comprehensive catalog of human rRNA modification positions
- **Guide Mapping**: Links between snoRNAs and their target modification sites
- **Validation Status**: Positions marked as validated or predicted
- **Modification Levels**: Quantitative data from RiboMethSeq, HydraPsiSeq, and mass spectrometry studies
- **Multiple rRNA Versions**: Support for snoRNABase, Ensembl, and RefSeq rRNA reference sequences

## Data Sources

snoDB integrates data from:
- **Databases**: Ensembl, RefSeq, snoRNA Atlas, snOPY, RFAM, RISE
- **Literature**: Manually curated from publications
- **Functional Data**: Gene Ontology, ENCODE eCLIP
- **Sequencing Data**: TGIRT-Seq from GEO and SRA repositories
- **Conservation**: UCSC genome browser PhastCons scores
- **Modifications**: RiboMethSeq, HydraPsiSeq, SILNAS studies

## Interactive Features

- **Advanced Search**: Filter and search across multiple snoRNA attributes
- **Column Visibility**: Customize table views
- **Data Export**: Download filtered datasets
- **Abundance Viewer**: Interactive visualization of expression patterns
- **Sequence Search**: Find snoRNAs by sequence similarity
- **Statistics Dashboard**: Overview of database contents with distribution charts

## Associated Tools

### snoRupdate
A C++ tool for integrating snoDB snoRNAs into genome annotations. Compatible with both Ensembl and RefSeq GTF files, enabling incorporation of up-to-date snoRNA annotations into RNA-Seq analysis pipelines.

## Data Processing

- **Unique Entries**: Merged based on genomic overlap with prioritized source order
- **Motif Prediction**: Custom algorithms with Hamming distance-based degenerate sequence matching
- **Structure Prediction**: RNAfold (ViennaRNA) for H/ACA snoRNA hairpin regions
- **Host Gene Assignment**: Overlap analysis with manual curation to remove pseudogenes
- **Interaction Filtering**: Statistical thresholds and replicate consistency requirements

## Version History

Current version: 2.0.0. The previous version remains accessible for legacy analyses.

## Contact

- **Database Inquiries**: Danny Bergeron (danny.bergeron@usherbrooke.ca)
- **Principal Investigator**: Michelle Scott (Michelle.Scott@USherbrooke.ca)
- **Institution**: Université de Sherbrooke, Department of Biochemistry and Functional Genomics