---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: NCICCGenomics@mail.nih.gov
      - contact_type: url
        value: https://www.cancer.gov/ccg/research/functional-genomics/ctd2
    label: National Cancer Institute Center for Cancer Genomics
creation_date: '2026-06-02T00:00:00Z'
description: The Cancer Target Discovery and Development Network is an NCI functional genomics initiative that releases cancer target discovery, validation, perturbation, and screening data for precision oncology research.
domains:
  - biomedical
  - genomics
  - precision medicine
  - drug discovery
homepage_url: https://www.cancer.gov/ccg/research/functional-genomics/ctd2
id: ctd2
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
name: Cancer Target Discovery and Development Network
products:
  - category: GraphicalInterface
    description: NCI CTD2 Data Portal listing CTD2 Network study datasets in the Index of NCI Studies for community access and reuse.
    id: ctd2.data-portal
    name: CTD2 Data Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ctd2
    product_url: https://www.cancer.gov/ccg/research/functional-genomics/ctd2/data-portal
  - category: GraphicalInterface
    description: Searchable CTD2 Dashboard interface for Network-generated observations and validated experimental findings associated with genes, proteins, compounds, biomarkers, and other studied subjects.
    id: ctd2.dashboard
    name: CTD2 Dashboard
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ctd2
    product_url: https://ctd2-dashboard.nci.nih.gov/
    warnings:
      - 'Dashboard host ctd2-dashboard.nci.nih.gov no longer resolves (no DNS record) as checked on 2026-06-27; the standalone CTD2 Dashboard application appears to have been decommissioned. NCI has consolidated CTD2 data access into the Index of NCI Studies / Study Catalog (https://studycatalog.cancer.gov), reachable via the CTD2 Data Portal product. No live replacement for the dashboard application itself was found.'
  - category: DocumentationProduct
    description: NCI guidance for accessing, using, and acknowledging CTD2 Network data and associated raw and analyzed datasets.
    id: ctd2.usage-guide
    name: Using CTD2 Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ctd2
    product_url: https://www.cancer.gov/ccg/research/functional-genomics/ctd2/using-ctd2-data
  - category: Product
    description: Drug screening data from various platforms including GDSC, PRISM, and CTD2
    format: csv
    id: depmap.drug_sensitivity
    name: DepMap Drug Sensitivity Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: depmap
    product_url: https://depmap.org/portal/data_page/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: gdsc
      - relation_type: prov:wasDerivedFrom
        source: prism
      - relation_type: prov:wasDerivedFrom
        source: ctd2
publications:
  - authors:
      - Bulent Aksoy
      - Vlado Dancik
      - Kenneth Smith
      - Jessica Mazerik
      - Zhou Ji
      - Benjamin Gross
    doi: 10.1093/database/bax054
    id: doi:10.1093/database/bax054
    journal: Database
    preferred: true
    title: 'CTD2 Dashboard: a searchable web interface to connect validated results from the Cancer Target Discovery and Development Network'
    year: '2017'
synonyms:
  - CTD2
  - CTD^2
  - CTD²
---

# Cancer Target Discovery and Development Network

The Cancer Target Discovery and Development Network is an NCI functional genomics
program that releases data from high-throughput experimental and computational
studies aimed at connecting cancer genomic findings to therapeutic target
discovery and validation.
