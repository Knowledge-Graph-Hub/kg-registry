---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: webmaster@signaling-gateway.org
  id: university-of-california-san-diego
  label: University of California San Diego
creation_date: '2026-05-04T00:00:00Z'
description: The Alliance for Cellular Signaling (AfCS) was a large-scale collaborative
  signaling biology project that generated and disseminated data about cellular signaling
  networks, including protein-protein interaction data from high-throughput screens
  in B lymphocytes and cardiac myocytes. AfCS also supported the UCSD-Nature Signaling
  Gateway Molecule Pages, a peer-reviewed database of mammalian signaling proteins
  with structured information about protein interactions, protein states, state transitions,
  and function. IntAct preserves an AFCS interaction dataset as part of its computationally
  maintained datasets.
domains:
- biological systems
- proteomics
- systems biology
homepage_url: https://web.archive.org/web/20220315092731/http://www.signaling-gateway.org/molecule/
id: afcs
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
name: Alliance for Cellular Signaling
products:
- category: GraphicalInterface
  description: Historical Signaling Gateway Molecule Pages web interface for curated
    mammalian signaling protein information.
  format: http
  id: afcs.molecule-pages
  name: AfCS-Nature Molecule Pages
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  product_url: https://web.archive.org/web/20220315092731/http://www.signaling-gateway.org/molecule/
- category: Product
  compression: zip
  description: IntAct-hosted AFCS protein interaction dataset in PSI-MI MITAB format.
  format: psi_mi_mitab
  id: afcs.intact.mitab
  name: AFCS IntAct MITAB Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  product_file_size: 720961
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/datasets/AFCS.zip
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
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
  - Participating investigators and scientists of the Alliance for Cellular Signaling
  doi: 10.1038/nature01304
  id: https://doi.org/10.1038/nature01304
  journal: Nature
  title: Overview of the Alliance for Cellular Signaling
  year: '2002'
- authors:
  - Joshua Li
  - Yuhong Ning
  - Warren Hedley
  - Brian Saunders
  - Yongsheng Chen
  - Nicole Tindill
  - Timo Hannay
  - Shankar Subramaniam
  doi: 10.1038/nature01307
  id: https://doi.org/10.1038/nature01307
  journal: Nature
  title: The Molecule Pages database
  year: '2002'
- authors:
  - Brian Saunders
  - Stephen Lyon
  - Matthew Day
  - Brenda Riley
  - Emily Chenette
  - Shankar Subramaniam
  - Ilango Vadivelu
  doi: 10.1093/nar/gkm907
  id: https://doi.org/10.1093/nar/gkm907
  journal: Nucleic Acids Research
  title: The Molecule Pages database
  year: '2008'
synonyms:
- AfCS
- AfCS-Nature Molecule Pages
- Signaling Gateway Molecule Pages
- UCSD-Nature Signaling Gateway
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# Alliance for Cellular Signaling

The Alliance for Cellular Signaling was a collaborative signaling biology project
and data source. Its Signaling Gateway Molecule Pages described mammalian signaling
proteins, and its interaction data are preserved in IntAct as an AFCS dataset.
