---
activity_status: orphaned
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: The Amyloidoses Collection (AmyCo) database contains manually curated data from biomedical literature on amyloidoses and other diseases related to amyloid deposition. It classifies 75 diseases and provides disease-gene associations. The resource is no longer independently accessible but is integrated into the DISEASES database.
domains:
  - biomedical
  - clinical
  - health
id: amyco
infores_id: amyco
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: The Amyloidoses Collection (AmyCo) Database
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/AmyCo
synonyms:
  - AmyCo
products:
- id: amyco.annotations
  name: AmyCo Curated Annotations
  description: Manually curated disease-gene associations and annotations for amyloidoses and amyloid deposition-related diseases extracted from biomedical literature.
  category: Product
  original_source:
  - pubmed
  - amyco
  secondary_source:
  - diseases
publications:
- authors:
  - Nastou KC
  - Nasi GI
  - Tsiolaki PL
  - Litou ZI
  - Iconomidou VA
  id: doi:10.1080/13506129.2019.1603143
  doi: 10.1080/13506129.2019.1603143
  journal: Amyloid
  title: "AmyCo: the amyloidoses collection"
  year: '2019'
---

# The Amyloidoses Collection (AmyCo) Database

## Overview

The Amyloidoses Collection (AmyCo) is a specialized database containing manually curated data from biomedical literature focused on amyloidoses and other diseases related to amyloid deposition. Amyloid diseases represent a group of disorders characterized by abnormal protein folding and accumulation, including conditions such as Alzheimer's disease, amyloid light-chain (AL) amyloidosis, and other systemic and localized amyloidoses.

AmyCo provides manually curated disease-gene associations extracted from scientific articles, focusing specifically on the complex molecular mechanisms underlying amyloid formation and deposition in various tissues and organs. It classifies 75 diseases associated with amyloid deposition into two categories: amyloidosis and clinical conditions associated with amyloidosis.

## Key Features

### Manual Curation

- **Literature-based Annotations**: Curated data extracted from peer-reviewed biomedical publications
- **Disease-gene Associations**: Focus on genetic factors involved in amyloid diseases
- **Specialized Domain**: Concentrated expertise in amyloidoses and related pathologies

### Coverage

- Systemic amyloidoses
- Localized amyloidoses
- Hereditary and acquired forms
- Associated molecular pathways and genetic factors

## Integration

AmyCo data has been integrated into the [DISEASES database](https://diseases.jensenlab.org/) maintained by Jensen Lab at the Novo Nordisk Foundation Center for Protein Research. DISEASES aggregates disease-gene associations from multiple sources including text mining, manual curation, cancer mutations, and GWAS studies, providing a unified confidence-scored resource.

## Applications

### Research Support

- Understanding genetic basis of amyloid diseases
- Identifying candidate genes for amyloid-related disorders
- Supporting translational research in protein folding diseases

### Clinical Relevance

- Informing genetic testing strategies for hereditary amyloidoses
- Supporting differential diagnosis of amyloid conditions
- Guiding precision medicine approaches

## Current Status

The AmyCo database is not directly accessible as an independent resource as of 2025 (previously at `http://bioinformatics.biol.uoa.gr/amyco`). Its manually curated content has been incorporated into downstream resources, particularly the DISEASES database which provides weekly updated disease-gene associations.

The Translator All Knowledge Provider Wiki page serves as the primary reference for this resource within the NCATS Biomedical Data Translator ecosystem.

## References

- **Primary Publication**: Nastou KC, Nasi GI, Tsiolaki PL, Litou ZI, Iconomidou VA. AmyCo: the amyloidoses collection. Amyloid. 2019 Sep;26(3):112-117. doi: 10.1080/13506129.2019.1603143. PMID: 31094220.

## Related Resources

- **DISEASES**: Weekly updated database integrating AmyCo data with other disease-gene association sources
- **NCATS Translator**: Biomedical Data Translator project where AmyCo is registered as an information resource

## Information Resource ID

This resource has the Information Resource identifier: `infores:amyco`
