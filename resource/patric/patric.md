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
description: The Pathosystems Resource Integration Center (PATRIC) was a bacterial bioinformatics resource center providing integrated data and analysis tools for bacterial infectious disease research. PATRIC has been succeeded by the Bacterial and Viral Bioinformatics Resource Center (BV-BRC), which continues to provide comprehensive bacterial genomics data, comparative analysis tools, and molecular characterization resources. The legacy PATRIC data and functionality have been integrated into BV-BRC.
domains:
  - genomics
  - microbiology
  - biomedical
  - health
homepage_url: https://www.bv-brc.org/
id: patric
infores_id: patric
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: Pathosystems Resource Integration Center
products:
- category: GraphicalInterface
  description: Web portal for bacterial genomics (now at BV-BRC)
  format: http
  id: patric.web
  name: PATRIC/BV-BRC Web Portal
  original_source:
  - patric
  product_url: https://www.bv-brc.org/
- category: Product
  description: Bacterial genome data and annotations
  format: mixed
  id: patric.genomes
  name: PATRIC Genome Data
  original_source:
  - patric
  product_url: https://www.bv-brc.org/
- category: ProgrammingInterface
  description: API for programmatic access to bacterial data
  format: http
  id: patric.api
  name: BV-BRC API
  original_source:
  - patric
  product_url: https://www.bv-brc.org/docs/api/
publications:
- id: https://doi.org/10.1093/nar/gkw1017
synonyms:
  - PATRIC
  - BV-BRC
  - Bacterial and Viral Bioinformatics Resource Center
taxon:
- NCBITaxon:2
warnings:
- PATRIC has been succeeded by BV-BRC (Bacterial and Viral Bioinformatics Resource Center). All data and tools are now available at bv-brc.org
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
RESTful API providing programmatic access to all bacterial and viral data for computational analysis.

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

