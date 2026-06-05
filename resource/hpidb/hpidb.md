---
activity_status: unresponsive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: hpidb@igbb.msstate.edu
  id: mississippi-state-university-college-of-veterinary-medicine
  label: Mississippi State University College of Veterinary Medicine
creation_date: '2026-05-04T00:00:00Z'
description: The Host-Pathogen Interaction Database (HPIDB) was a public resource
  for host-pathogen protein-protein interactions. HPIDB integrated experimentally
  verified interactions from public molecular interaction databases and targeted curation
  into a non-redundant resource for searching, downloading, visualizing, and inferring
  host-pathogen interaction networks, but its primary homepage was not accessible
  during curation checks on 2026-05-04 and 2026-06-02.
domains:
- biomedical
- immunology
- microbiology
- proteomics
fairsharing_id: FAIRsharing.fk0z49
homepage_url: https://hpidb.igbb.msstate.edu/
id: hpidb
infores_id: hpidb
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Host-Pathogen Interaction Database
products:
- category: GraphicalInterface
  description: Web interface for searching HPIDB by sequence, keyword, and homologous
    host-pathogen protein interaction.
  format: http
  id: hpidb.portal
  name: HPIDB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hpidb
  product_url: https://hpidb.igbb.msstate.edu/
  warnings:
  - The HPIDB homepage failed to establish HTTP and HTTPS connections during curation
    on 2026-06-02.
- category: Product
  description: Downloadable HPIDB host-pathogen interaction dataset in PSI-MITAB format.
  format: psi_mi_mitab
  id: hpidb.mitab
  name: HPIDB PSI-MITAB Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hpidb
  product_url: https://hpidb.igbb.msstate.edu/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-05: Error connecting
    to URL: HTTPSConnectionPool(host=''hpidb.igbb.msstate.edu'', port=443): Max retries
    exceeded with url: / (Caused by NewConnectionError("HTTPSConnection(host=''hpidb.igbb.msstate.edu'',
    port=443): Failed to establish a new connection: [Errno 111] Connection refused"))'
  - The HPIDB homepage failed to establish HTTP and HTTPS connections during curation
    on 2026-06-02.
  - The historical AgBase HPI downloads URL redirected and then returned HTTP 403
    during curation on 2026-06-02.
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/intact/ws
  description: IntAct web service and URL-based programmatic interface for retrieving
    molecular interaction networks in PSI-MI formats.
  format: http
  id: intact.api
  is_public: true
  name: IntAct Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://www.ebi.ac.uk/intact/ws
- category: Product
  description: IntAct data in PSI-MI XML 2.5 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi25
  name: IntAct PSI-MI XML 2.5
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi25/
- category: Product
  description: IntAct data in PSI-MI XML 3.0 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi30
  name: IntAct PSI-MI XML 3.0
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi30/
- category: Product
  description: IntAct data in PSI-MI MITAB format (directory)
  format: psi_mi_mitab
  id: intact.ftp.psimitab
  name: IntAct PSI-MI MITAB 2.7
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/
- category: Product
  description: Entire MITAB export of the database as a single archive (intact.zip)
  format: psi_mi_mitab
  id: intact.ftp.psimitab.all
  name: IntAct MITAB Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_file_size: 846305671
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/intact.zip
- category: Product
  description: Curated and computational datasets (disease-, method-, and species-specific)
    with per-dataset downloads
  format: http
  id: intact.datasets
  name: IntAct Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://www.ebi.ac.uk/intact/download/datasets
publications:
- authors:
  - Muna G. Ammari
  - Cathy R. Gresham
  - Fiona M. McCarthy
  - Bindu Nanduri
  doi: 10.1093/database/baw103
  id: doi:10.1093/database/baw103
  journal: Database
  preferred: true
  title: 'HPIDB 2.0: a curated database for host-pathogen interactions'
  year: '2016'
- authors:
  - Ranjit Kumar
  - Bindu Nanduri
  doi: 10.1186/1471-2105-11-S6-S16
  id: doi:10.1186/1471-2105-11-S6-S16
  journal: BMC Bioinformatics
  title: HPIDB--a unified resource for host-pathogen interactions
  year: '2010'
synonyms:
- HPIDB
- Host Pathogen Interaction Database
---
# Host-Pathogen Interaction Database

HPIDB provided curated and integrated host-pathogen protein-protein interaction
data for infectious disease and host-pathogen network analysis. Its primary
homepage was not reachable during curation checks on 2026-05-04 and 2026-06-02.