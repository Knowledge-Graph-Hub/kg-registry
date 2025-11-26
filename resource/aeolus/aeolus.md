---
activity_status: active
category: DataSource
contacts:
- category: Individual
  label: Juan M. Banda
- category: Individual
  label: Lee Evans
- category: Individual
  label: Rami S. Vanguri
- category: Individual
  label: Nicholas P. Tatonetti
- category: Individual
  label: Patrick B. Ryan
creation_date: '2025-10-30T00:00:00Z'
description: AEOLUS (Adverse Event Open Learning through Universal Standardization) is a curated and standardized version of the FDA Adverse Event Reporting System (FAERS) that removes duplicate case records and applies standardized vocabularies, with drug names mapped to RxNorm concepts and outcomes mapped to SNOMED-CT concepts, providing pre-computed summary statistics about drug-outcome relationships.
domains:
- clinical
- pharmacology
- drug discovery
- health
- biomedical
homepage_url: https://datadryad.org/stash/dataset/doi:10.5061/dryad.8q0s4
id: aeolus
infores_id: aeolus
last_modified_date: '2025-11-22T00:00:00Z'
layout: resource_detail
name: Adverse Event Open Learning through Universal Standardization (AEOLUS)
products:
- category: Product
  description: Standardized and deduplicated version of FDA FAERS data with drug names mapped to RxNorm and adverse event outcomes mapped to SNOMED-CT, including pre-computed summary statistics for drug-outcome relationships.
  id: aeolus.standardized_data
  name: AEOLUS Standardized FAERS Data
  original_source:
  - faers
  - aeolus
  product_url: https://datadryad.org/stash/dataset/doi:10.5061/dryad.8q0s4
publications:
- authors:
  - Banda JM
  - Evans L
  - Vanguri RS
  - Tatonetti NP
  - Ryan PB
  id: doi:10.1038/sdata.2016.26
  doi: 10.1038/sdata.2016.26
  journal: Scientific Data
  title: A curated and standardized adverse drug event resource to accelerate drug safety research
  year: '2016'
synonyms:
- AEOLUS
---

# Adverse Event Open Learning through Universal Standardization (AEOLUS)

## Overview

AEOLUS (Adverse Event Open Learning through Universal Standardization) is a curated and standardized version of the FDA Adverse Event Reporting System (FAERS) database. FAERS is the FDA's post-marketing surveillance system that collects reports of adverse events and medication errors involving drugs and therapeutic biologics.

AEOLUS addresses key data quality challenges in the raw FAERS data by removing duplicates, standardizing drug and outcome terminologies, and providing pre-computed statistical summaries, making adverse event data more accessible and usable for research and drug safety applications.

## Key Features

### Data Standardization

- **Duplicate Removal**: Eliminates duplicate case records to prevent biased signal detection
- **RxNorm Mapping**: Drug names standardized to RxNorm concepts for consistent drug identification
- **SNOMED-CT Mapping**: Adverse event outcomes mapped to SNOMED-CT concepts for standardized clinical terminology
- **Vocabulary Harmonization**: Unified terminology system enabling cross-database integration

### Pre-computed Statistics

- **Drug-Outcome Relationships**: Summary statistics quantifying associations between drugs and adverse events
- **Signal Detection Metrics**: Pre-calculated measures supporting pharmacovigilance analyses
- **Ready-to-Use Format**: Processed data optimized for computational analysis and consumption

## Applications

### Pharmacovigilance

- Post-market drug safety surveillance
- Adverse event signal detection
- Drug safety profile characterization
- Comparative safety assessments

### Research Applications

- Drug repurposing through adverse event analysis
- Understanding drug mechanism of action via side effect patterns
- Identifying drug-drug interaction risks
- Polypharmacy safety studies

### Clinical Decision Support

- Informing prescribing decisions
- Patient-specific risk assessment
- Drug selection in special populations
- Safety monitoring in clinical practice

## Data Sources

**Primary Source**: FDA Adverse Event Reporting System (FAERS)

**Terminology Standards**:
- RxNorm (drug names)
- SNOMED-CT (clinical outcomes/adverse events)

## Integration

AEOLUS is registered as an information resource (infores:aeolus) in the NCATS Biomedical Data Translator ecosystem, enabling its use in integrated biomedical knowledge queries and reasoning systems.

## Advantages

- **Improved Data Quality**: Deduplication and standardization enhance reliability
- **Interoperability**: Standard terminologies enable integration with other biomedical resources
- **Computational Ready**: Pre-computed statistics facilitate large-scale analyses
- **Research Accessibility**: Processed format lowers barriers to FAERS data utilization
