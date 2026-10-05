---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/pride/
  - contact_type: github
    value: PRIDE-Archive
  id: ebi
  label: EMBL-EBI PRIDE Team
creation_date: '2026-10-04T00:00:00Z'
description: The PRIDE (PRoteomics IDEntifications) Archive is EMBL-EBI's public repository
  for mass spectrometry-based proteomics data and a founding member of the ProteomeXchange
  consortium. It stores raw files, peptide and protein identifications, quantification
  results and experimental metadata for submitted datasets, each identified by a ProteomeXchange
  accession (PXD). The archive held 41,886 public projects when checked on 2026-10-04.
domains:
- proteomics
- biomedical
fairsharing_id: FAIRsharing.e1byny
homepage_url: https://www.ebi.ac.uk/pride/
id: pride
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
name: PRIDE Archive
products:
- category: GraphicalInterface
  description: PRIDE Archive web portal for searching, browsing and downloading public
    proteomics datasets by accession, keyword, organism, instrument and other metadata.
  format: http
  id: pride.portal
  name: PRIDE Archive Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://www.ebi.ac.uk/pride/archive/
- category: ProgrammingInterface
  description: PRIDE Archive REST API (version 3) for project, file, protein and peptide
    metadata, with Swagger documentation.
  format: http
  id: pride.api
  name: PRIDE Archive REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://www.ebi.ac.uk/pride/ws/archive/v3/webjars/swagger-ui/index.html
- category: Product
  description: FTP archive of all public PRIDE datasets, organized by publication
    year and month and then by PXD accession, holding raw instrument files, peak lists,
    search engine results and other submitted files.
  format: mixed
  id: pride.ftp
  name: PRIDE Archive FTP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://ftp.pride.ebi.ac.uk/pride/data/archive/
- category: DocumentationProduct
  description: PRIDE documentation covering data submission, the submission tool,
    dataset access, the REST API and related PRIDE resources.
  format: http
  id: pride.docs
  name: PRIDE Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://www.ebi.ac.uk/pride/markdownpage/documentationpage
- category: ProcessProduct
  description: GitHub organization holding the source code of the PRIDE Archive web
    services, web interface, submission tool and supporting libraries.
  format: mixed
  id: pride.code
  name: PRIDE Archive Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://github.com/PRIDE-Archive
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: pride
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Yasset Perez-Riverol
  - Chakradhar Bandla
  - Deepti J Kundu
  - Selvakumar Kamatchinathan
  - Jingwen Bai
  - Suresh Hewapathirana
  - Nithu Sara John
  - Ananth Prakash
  - Mathias Walzer
  - Shengbo Wang
  - Juan Antonio Vizcaíno
  doi: 10.1093/nar/gkae1011
  id: doi:10.1093/nar/gkae1011
  journal: Nucleic Acids Research
  preferred: true
  title: 'The PRIDE database at 20 years: 2025 update'
  year: '2025'
- authors:
  - Yasset Perez-Riverol
  - Jingwen Bai
  - Chakradhar Bandla
  - David García-Seisdedos
  - Suresh Hewapathirana
  - Selvakumar Kamatchinathan
  - Deepti J Kundu
  - Ananth Prakash
  - Anika Frericks-Zipper
  - Martin Eisenacher
  - Mathias Walzer
  - Shengbo Wang
  - Alvis Brazma
  - Juan Antonio Vizcaíno
  doi: 10.1093/nar/gkab1038
  id: doi:10.1093/nar/gkab1038
  journal: Nucleic Acids Research
  title: 'The PRIDE database resources in 2022: a hub for mass spectrometry-based
    proteomics evidences'
  year: '2022'
repository: https://github.com/PRIDE-Archive
synonyms:
- PRIDE
- PRoteomics IDEntifications Database
- PRIDE database
---
# PRIDE Archive

PRIDE (PRoteomics IDEntifications) is EMBL-EBI's repository for mass spectrometry-based proteomics data. It was started in 2004 and is a founding member of the ProteomeXchange consortium, which coordinates proteomics data submission across repositories such as PRIDE, MassIVE, PeptideAtlas, jPOST and iProX.

## Data

Each public dataset has a ProteomeXchange accession (PXD followed by six digits). Datasets include raw instrument files, processed peak lists, search engine results, quantification tables and sample metadata, often in SDRF format. On 2026-10-04 the REST API reported 41,886 public projects.

## Access

- **Web portal**: search and browse datasets at https://www.ebi.ac.uk/pride/archive/.
- **REST API**: version 3 of the PRIDE Archive web services at https://www.ebi.ac.uk/pride/ws/archive/v3/.
- **FTP**: files for every public dataset under https://ftp.pride.ebi.ac.uk/pride/data/archive/, arranged by year and month of publication.

## License

The PRIDE site falls under the EMBL-EBI Terms of Use. Each dataset also carries its own license in its metadata. Of the 100 most recently submitted projects checked on 2026-10-04, 81 listed "EBI terms of use" and 19 listed "Creative Commons Public Domain (CC0)".