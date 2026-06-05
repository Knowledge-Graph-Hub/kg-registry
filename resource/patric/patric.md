---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.bv-brc.org/
  label: BV-BRC
creation_date: '2025-11-05T00:00:00Z'
description: The Pathosystems Resource Integration Center (PATRIC) was a bacterial
  bioinformatics resource center providing integrated data and analysis tools for
  bacterial infectious disease research. PATRIC has been succeeded by the Bacterial
  and Viral Bioinformatics Resource Center (BV-BRC), which continues to provide comprehensive
  bacterial genomics data, comparative analysis tools, and molecular characterization
  resources. The legacy PATRIC data and functionality have been integrated into BV-BRC.
domains:
- genomics
- microbiology
- biomedical
homepage_url: https://www.bv-brc.org/
id: patric
infores_id: patric
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Pathosystems Resource Integration Center
products:
- category: GraphicalInterface
  description: BV-BRC web portal that hosts legacy PATRIC bacterial genomics data
    and tools alongside expanded viral resources
  format: http
  id: patric.web
  name: PATRIC/BV-BRC Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/
- category: Product
  description: Legacy PATRIC bacterial genome data and annotations now available through
    BV-BRC genome data views and services
  format: mixed
  id: patric.genomes
  name: PATRIC Genome Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/quick_start/data_functionality_overview.html
  warnings: []
- category: ProgrammingInterface
  description: BV-BRC REST Data API for querying and retrieving public data, including
    data inherited from PATRIC
  format: http
  id: patric.api
  name: BV-BRC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/system_documentation/system_architecture.html#data-api
- category: DocumentationProduct
  description: BV-BRC quick-start overview for PATRIC users, describing how legacy
    PATRIC data, tools, services, website, and infrastructure were incorporated into
    BV-BRC
  format: http
  id: patric.bv_brc_overview
  name: BV-BRC Overview for PATRIC Users
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/quick_start/data_functionality_overview.html
  warnings: []
publications:
- authors:
  - Wattam AR
  - Davis JJ
  - Assaf R
  - Boisvert S
  - Brettin T
  - Bun C
  - Conrad N
  - Dietrich EM
  - Disz T
  - Gabbard JL
  - Gerdes S
  - Henry CS
  - Kenyon RW
  - Machi D
  - Mao C
  - Nordberg EK
  - Olsen GJ
  - Murphy-Olson DE
  - Olson R
  - Overbeek R
  - Parrello B
  - Pusch GD
  - Shukla M
  - Vonstein V
  - Warren A
  - Xia F
  - Yoo H
  - Stevens RL
  doi: 10.1093/nar/gkw1017
  id: doi:10.1093/nar/gkw1017
  journal: Nucleic Acids Research
  preferred: true
  title: Improvements to PATRIC, the all-bacterial Bioinformatics Database and Analysis
    Resource Center
  year: '2017'
synonyms:
- PATRIC
- BV-BRC
- Bacterial and Viral Bioinformatics Resource Center
taxon:
- NCBITaxon:2
warnings:
- PATRIC has been succeeded by BV-BRC (Bacterial and Viral Bioinformatics Resource
  Center). The live products listed here are hosted by BV-BRC.
---
# Pathosystems Resource Integration Center

## Overview

The Pathosystems Resource Integration Center (PATRIC) was a bacterial bioinformatics resource center providing integrated data and analysis tools for bacterial infectious disease research.

**Important:** PATRIC has been succeeded by the Bacterial and Viral Bioinformatics Resource Center (BV-BRC), which continues and expands upon PATRIC's mission. All PATRIC data and functionality have been integrated into BV-BRC at https://www.bv-brc.org/

## Historical Context

PATRIC provided:
- Comprehensive bacterial genome databases
- Comparative genomics tools
- Protein family analyses
- Metabolic pathway reconstructions
- Gene expression data
- Antimicrobial resistance information
- Virulence factor databases

These capabilities are now available through BV-BRC, which has expanded to include viral pathogens as well.

## BV-BRC Successor

The Bacterial and Viral Bioinformatics Resource Center (BV-BRC) provides:
- All PATRIC bacterial data and tools
- Expanded viral pathogen resources
- Enhanced comparative analysis capabilities
- Modern web interface and APIs
- Integration with other NIAID resources

## Products

### BV-BRC Web Portal
Comprehensive web interface for accessing bacterial and viral genomics data, analysis tools, and resources (formerly PATRIC portal).

### Genome Data
Extensive collection of bacterial genome sequences, annotations, and functional characterizations.

### BV-BRC API
RESTful API providing programmatic access to public BV-BRC data, including legacy
PATRIC bacterial data.

## Information Resource ID

This resource has the Information Resource identifier: `infores:patric`

## Publications

- [PATRIC, the bacterial bioinformatics database and analysis resource](https://doi.org/10.1093/nar/gkw1017) (2017)

## Domains

- Genomics
- Microbiology
- Biomedical
- Health

## Taxon Coverage

Bacteria (NCBITaxon:2)

## Migration Notice

PATRIC has been succeeded by BV-BRC. Users should transition to BV-BRC for continued access to bacterial bioinformatics resources.