---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@thebiogrid.org
  - contact_type: url
    value: https://thebiogrid.org/
  label: BioGRID
creation_date: '2025-08-13T00:00:00Z'
description: The Biological General Repository for Interaction Datasets (BioGRID) is an open, curated database of genetic, protein, and chemical interaction data, post-translational modifications (PTMs), CRISPR screen results (ORCS), and themed curation project datasets spanning model organisms and human, freely available under the MIT License.
domains:
- biomedical
- proteomics
- genomics
- systems biology
homepage_url: https://thebiogrid.org/
id: biogrid
last_modified_date: '2025-08-23T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: BioGRID
products:
- category: GraphicalInterface
  description: Web interface for browsing, searching, and visualizing BioGRID interaction and project data
  format: http
  id: biogrid.web
  name: BioGRID Website
  original_source:
  - biogrid
  product_url: https://thebiogrid.org/
- category: ProgrammingInterface
  description: REST-based web service for programmatic access to BioGRID interaction, chemical association, PTM, and CRISPR (ORCS) data
  format: http
  id: biogrid.api
  is_public: true
  name: BioGRID REST API
  original_source:
  - biogrid
  product_url: https://wiki.thebiogrid.org/doku.php/biogridrest
- category: GraphProduct
  compression: zip
  description: Latest complete BioGRID interaction dataset in PSI-MI MITAB format (non-redundant and raw interactions combined)
  format: psi_mi_mitab
  id: biogrid.interactions.mitab
  latest_version: 4.4.248
  name: BIOGRID-ALL-LATEST.mitab.zip
  secondary_source:
  - biogrid
  product_url: https://downloads.thebiogrid.org/BioGRID/Latest-Release/BIOGRID-ALL-LATEST.mitab.zip
- category: GraphProduct
  compression: zip
  description: Latest complete BioGRID interaction dataset in TAB3 (tab-delimited) format
  format: tsv
  id: biogrid.interactions.tab3
  latest_version: 4.4.248
  name: BIOGRID-ALL-LATEST.tab3.zip
  secondary_source:
  - biogrid
  product_url: https://downloads.thebiogrid.org/BioGRID/Latest-Release/BIOGRID-ALL-LATEST.tab3.zip
- category: GraphProduct
  compression: zip
  description: Post-translational modification (PTM) site dataset curated by BioGRID
  format: tsv
  id: biogrid.ptm
  latest_version: 4.4.248
  name: BIOGRID-PTMS-LATEST.ptm.zip
  secondary_source:
  - biogrid
  product_url: https://downloads.thebiogrid.org/BioGRID/Latest-Release/BIOGRID-PTMS-LATEST.ptm.zip
publications:
- id: https://doi.org/10.1002/pro.3978
  journal: Protein Science
  preferred: true
  title: "The BioGRID database – a comprehensive biomedical resource of curated protein, genetic, and chemical interactions"
  year: '2020'
- id: https://doi.org/10.1093/nar/gky1079
  journal: Nucleic Acids Research
  title: "The BioGRID interaction database: 2019 update"
  year: '2019'
- id: https://doi.org/10.1093/nar/gkj109
  journal: Nucleic Acids Research
  title: "BioGRID: a general repository for interaction datasets"
  year: '2006'
---
# BioGRID

BioGRID (Biological General Repository for Interaction Datasets) is an open, curated repository of genetic, protein, and chemical interaction data, PTMs, CRISPR screen results (ORCS), and themed biological curation projects across multiple species including human, budding yeast (S. cerevisiae), fission yeast (S. pombe), and Arabidopsis (A. thaliana). Monthly releases (e.g., 4.4.248) incorporate newly curated interactions and annotations. Data are available via a REST API and downloadable archives in multiple formats (MITAB, PSI-XML, TAB, project-specific subsets, PTM sites). All data are freely reusable under the MIT License with required citation of contributing authors and BioGRID publications.