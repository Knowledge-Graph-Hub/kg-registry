---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://dip.doe-mbi.ucla.edu/
  - contact_type: email
    value: dip@mbi.ucla.edu
  label: UCLA-DOE Institute for Genomics and Proteomics
- category: Individual
  contact_details:
  - contact_type: url
    value: https://www.chem.ucla.edu/~eisenberg/
  label: David Eisenberg
creation_date: '2025-11-10T00:00:00Z'
description: The Database of Interacting Proteins (DIP) is a curated biological database
  that catalogs experimentally determined interactions between proteins, developed
  and maintained by the research group of David Eisenberg at the University of California
  Los Angeles (UCLA). Established in 2002, DIP combines information from diverse sources
  to create a unified, consistent set of protein-protein interactions with both manual
  expert curation and automated computational approaches that leverage knowledge extracted
  from the most reliable core subset of the data. DIP serves as a member of the International
  Molecular Exchange (IMEx) Consortium, an international collaboration of major public
  providers of protein interaction data including IntAct, MINT, BioGRID, and others
  that work together to avoid duplication of curation efforts by collecting data from
  non-overlapping sources and sharing curated interaction data. The database enables
  searches through its web interface based on multiple criteria including interactions
  described in specific journal articles, interactions supported by particular types
  of experimental evidence, and protein identifiers or sequences. DIP data have been
  curated using both manual approaches by expert biologists and automated computational
  methods that utilize machine learning and network analysis of the high-confidence
  core interaction data. The IMEx consortium developed the HUPO Proteomics Standards
  Initiative Molecular Interaction (HUPO-PSI-MI) XML format, which has become widely
  implemented for standardizing molecular interaction data representation. All information
  within DIP is freely available under a Creative Commons Attribution-NoDerivatives
  3.0 license. DIP provides downloads of complete datasets and specialized subsets,
  supporting integration with other protein interaction databases and serving as a
  foundational resource for systems biology, network analysis, and protein function
  prediction studies.
domains:
- biological systems
homepage_url: https://dip.doe-mbi.ucla.edu/
id: dip
infores_id: dip
last_modified_date: '2025-11-10T00:00:00Z'
layout: resource_detail
name: Database of Interacting Proteins
products:
- category: GraphicalInterface
  description: Web-based search interface for exploring protein-protein interactions
    by journal article, experimental evidence, or protein identifiers
  id: dip.search
  name: DIP Search Interface
  product_url: https://dip.doe-mbi.ucla.edu/dip/Search.cgi
- category: Product
  description: Complete DIP dataset and specialized subsets available for download
    in PSI-MI formats (registration required)
  format: psi_mi_mitab
  id: dip.downloads
  name: DIP Data Downloads
  product_url: https://dip.doe-mbi.ucla.edu/dip/Download.cgi
  warnings:
  - File was not able to be retrieved when checked on 2025-11-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='dip.doe-mbi.ucla.edu', port=443)_ Max retries
    exceeded with url_ /dip/Download.cgi (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-11-19_ Error connecting
    to URL_ HTTPSConnectionPool(host='dip.doe-mbi.ucla.edu', port=443)_ Max retries
    exceeded with url_ /dip/Download.cgi (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-19: Error connecting
    to URL: HTTPSConnectionPool(host=''dip.doe-mbi.ucla.edu'', port=443): Max retries
    exceeded with url: /dip/Download.cgi (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
    issuer certificate (_ssl.c:1017)'')))'
- category: Product
  description: Historical consolidated protein interaction index in PSI-MITAB 2.5
    format aggregating data from BIND, BioGrid, DIP, HPRD, IntAct, MINT, MPact, MPPI
    and OPHID
  format: psi_mi_mitab
  id: irefindex.database
  name: iRefIndex Database
  original_source:
  - bind
  - biogrid
  - dip
  - hprd
  - intact
  - mint
publications:
- id: https://doi.org/10.1093/nar/30.1.303
  title: 'DIP, the Database of Interacting Proteins: a research tool for studying
    cellular networks of protein interactions'
- id: https://doi.org/10.1093/nar/gkh086
  title: 'The Database of Interacting Proteins: 2004 update'
- id: https://doi.org/10.1038/nmeth.1931
  title: 'Protein interaction data curation: The International Molecular Exchange
    (IMEx) consortium'
synonyms:
- DIP
- Database of Interacting Proteins
---
# Database of Interacting Proteins

The Database of Interacting Proteins (DIP) is a curated resource for experimentally validated protein-protein interactions, maintained by UCLA as part of the IMEx consortium.