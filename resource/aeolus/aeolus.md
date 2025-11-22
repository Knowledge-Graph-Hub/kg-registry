---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: AEOLUS (Adverse Event Open Learning through Universal Standardization) is a standardized version of the FDA Adverse Event Reporting System (FAERS) that removes duplicate case records and applies standardized vocabularies, with drug names mapped to RxNorm concepts and outcomes mapped to SNOMED-CT concepts, providing pre-computed summary statistics about drug-outcome relationships.
domains:
  - clinical
  - pharmacology
  - drug discovery
  - health
  - biomedical
id: aeolus
infores_id: aeolus
last_modified_date: '2025-11-22T00:00:00Z'
layout: resource_detail
name: Adverse Event Open Learning through Universal Standardization (AEOLUS)
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/AEOLUS
synonyms:
  - AEOLUS
products:
- id: aeolus.standardized_data
  name: AEOLUS Standardized FAERS Data
  description: Standardized and deduplicated version of FDA FAERS data with drug names mapped to RxNorm and adverse event outcomes mapped to SNOMED-CT, including pre-computed summary statistics for drug-outcome relationships.
  category: DataProduct
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/AEOLUS
  original_source:
  - faers
  - aeolus
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

---

*Note: For current access information and specific data products, consult the NCATS Translator Knowledge Provider documentation.*

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:aeolus`

## Curation Status

- **Stub**: Yes - needs manual curation
- **Creation Date**: 2025-10-30
- **Original Source**: Translator Information Resource Registry

## What Needs to be Curated

1. **Activity Status**: Verify if this resource is active, inactive, or deprecated
2. **Category**: Confirm the resource category is correct
3. **Description**: Expand and improve the description
4. **Homepage URL**: Verify and update if needed
5. **Products**: Add specific data products/files/APIs offered by this resource
6. **Contacts**: Add contact information
7. **Publications**: Add relevant publications
8. **Domains**: Add relevant domain tags
9. **Repository**: Add code repository if applicable

## Additional Notes
