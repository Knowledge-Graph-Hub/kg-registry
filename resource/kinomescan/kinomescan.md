---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: KINOMEscan is a biochemical kinase profiling assay that measures drug binding using a panel of approximately 440 purified kinases. The HMS LINCS Project provides a comprehensive table of all small molecules in the HMS LINCS collection that have been profiled by KINOMEscan, with links to raw binding data.
domains:
  - drug discovery
  - pharmacology
  - biomedical
id: kinomescan
infores_id: kinomescan
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
name: KINOMEscan
homepage_url: https://lincs.hms.harvard.edu/kinomescan/
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://lincs.hms.harvard.edu/
    label: HMS LINCS Project
products:
  - category: GraphicalInterface
    description: Web interface providing searchable table of all small molecules profiled by KINOMEscan
    format: http
    id: kinomescan.portal
    name: KINOMEscan Data Portal
    original_source:
      - kinomescan
    product_url: https://lincs.hms.harvard.edu/kinomescan/
  - category: DocumentationProduct
    description: Excel spreadsheet containing HMS LINCS KINOMEscan datasets with compound information and data links
    id: kinomescan.spreadsheet
    name: KINOMEscan Datasets Spreadsheet
    original_source:
      - kinomescan
    product_url: http://lincs.hms.harvard.edu/wordpress/wp-content/uploads/2013/11/HMS-LINCS_KinomeScan_Datasets_2018-01-18.xlsx
synonyms:
  - HMS LINCS KINOMEscan
---

# KINOMEscan

## Overview

KINOMEscan is a biochemical kinase profiling assay technology that measures drug binding using a panel of approximately 440 purified kinases. The data resource is maintained by the HMS LINCS (Harvard Medical School Library of Integrated Network-based Cellular Signatures) Project. The assay provides comprehensive profiling of small molecule compounds against a large kinase panel, enabling drug discovery and selectivity profiling studies.

## Data Content

The HMS LINCS KINOMEscan data collection includes:

- **Compound Coverage**: Small molecules from the HMS LINCS collection that have been profiled by KINOMEscan
- **Kinase Panel**: Approximately 440 purified kinases representing a broad coverage of the human kinome
- **Binding Data**: Raw binding data for each compound-kinase interaction
- **Compound Information**: HMSL identifiers, LSM numbers, common names, and synonyms for each profiled compound

The data includes kinase inhibitors, multi-kinase inhibitors, and other bioactive small molecules commonly used in drug discovery and chemical biology research.

## Key Features

- **Comprehensive Kinase Coverage**: ~440 kinases representing diverse families
- **Biochemical Assay**: Direct measurement of compound binding to purified kinases
- **Searchable Data**: Web interface with compound names and identifiers
- **Downloadable Datasets**: Excel spreadsheet format for offline analysis
- **HMS LINCS Integration**: Part of the broader HMS LINCS data ecosystem

## Access Methods

1. **Web Interface**: Browse and search KINOMEscan data through the HMS LINCS portal
2. **Spreadsheet Download**: Excel file containing complete dataset information and links (last updated January 18, 2018)

## Data Format

- **Online**: HTML table with compound information and data links
- **Downloadable**: Microsoft Excel (.xlsx) format

## Use Cases

- **Drug Discovery**: Kinase inhibitor profiling and selectivity assessment
- **Target Validation**: Understanding kinase inhibitor specificity
- **Polypharmacology Studies**: Identifying off-target kinase interactions
- **Structure-Activity Relationships**: Correlating compound structure with kinase binding profiles
- **Chemical Biology**: Tool compound characterization

## Management

The KINOMEscan data resource is managed and curated by the HMS LINCS Project at Harvard Medical School.

## Related Resources

- HMS LINCS Database: https://lincs.hms.harvard.edu/db/
- HMS LINCS Data Exploration Tools: https://lincs.hms.harvard.edu/explore/
- HMS LINCS Publications: https://lincs.hms.harvard.edu/about/publications/

## Last Update

The downloadable spreadsheet was last updated on January 18, 2018.
