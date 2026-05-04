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
homepage_url: http://www.signaling-gateway.org/molecule
id: afcs
last_modified_date: '2026-05-04T00:00:00Z'
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
  - afcs
  product_url: http://www.signaling-gateway.org/molecule
  warnings:
  - The original Signaling Gateway Molecule Pages URL was not reachable during curation
    on 2026-05-04.
- category: Product
  compression: zip
  description: IntAct-hosted AFCS protein interaction dataset in PSI-MI MITAB format.
  format: psi_mi_mitab
  id: afcs.intact.mitab
  name: AFCS IntAct MITAB Dataset
  original_source:
  - afcs
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/datasets/AFCS.zip
  secondary_source:
  - intact
publications:
- id: https://doi.org/10.1038/nature01304
  title: Overview of the Alliance for Cellular Signaling
  authors:
  - Participating investigators and scientists of the Alliance for Cellular Signaling
  journal: Nature
  year: '2002'
  doi: 10.1038/nature01304
- id: https://doi.org/10.1038/nature01307
  title: The Molecule Pages database
  authors:
  - Joshua Li
  - Yuhong Ning
  - Warren Hedley
  - Brian Saunders
  - Yongsheng Chen
  - Nicole Tindill
  - Timo Hannay
  - Shankar Subramaniam
  journal: Nature
  year: '2002'
  doi: 10.1038/nature01307
- id: https://doi.org/10.1093/nar/gkm907
  title: The Molecule Pages database
  authors:
  - Brian Saunders
  - Stephen Lyon
  - Matthew Day
  - Brenda Riley
  - Emily Chenette
  - Shankar Subramaniam
  - Ilango Vadivelu
  journal: Nucleic Acids Research
  year: '2008'
  doi: 10.1093/nar/gkm907
synonyms:
- AfCS
---

# Alliance for Cellular Signaling

The Alliance for Cellular Signaling was a collaborative signaling biology project
and data source. Its interaction data are preserved in IntAct as an AFCS dataset.
