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
  - biomedical
  - pharmacovigilance
homepage_url: https://datadryad.org/dataset/doi:10.5061/dryad.8q0s4
id: aeolus
infores_id: aeolus
last_modified_date: '2026-09-23T00:00:00Z'
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
layout: resource_detail
name: Adverse Event Open Learning through Universal Standardization (AEOLUS)
products:
  - category: Product
    compression: zip
    description: Standardized and deduplicated version of FDA FAERS data with drug names mapped to RxNorm and adverse event outcomes mapped to SNOMED-CT, including pre-computed summary statistics for drug-outcome relationships.
    format: csv
    id: aeolus.standardized_data
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0 1.0
    name: AEOLUS Standardized FAERS Data
    original_source:
      - source: faers
        relation_type: prov:hadPrimarySource
      - source: aeolus
        relation_type: prov:hadPrimarySource
    product_url: https://datadryad.org/dataset/doi:10.5061/dryad.8q0s4
  - category: ProgrammingInterface
    description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
      querying the BioThings and other APIs registered to the team in SmartAPI.
    format: http
    id: service-kp.trapi
    is_public: true
    name: Service Provider TRAPI
    original_source:
    - relation_type: prov:hadPrimarySource
      source: service-kp
    - relation_type: prov:hadPrimarySource
      source: biothings
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: complexportal
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: litvar
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: ols
    - relation_type: prov:hadPrimarySource
      source: alliance
    - relation_type: prov:hadPrimarySource
      source: bindingdb
    - relation_type: prov:hadPrimarySource
      source: bioplanet
    - relation_type: prov:hadPrimarySource
      source: ddinter
    - relation_type: prov:hadPrimarySource
      source: dgidb
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: gene2phenotype
    - relation_type: prov:hadPrimarySource
      source: foodb
    - relation_type: prov:hadPrimarySource
      source: gtrx
    - relation_type: prov:hadPrimarySource
      source: hp
    - relation_type: prov:hadPrimarySource
      source: idisk
    - relation_type: prov:hadPrimarySource
      source: innatedb
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: pfocr
    - relation_type: prov:hadPrimarySource
      source: repodb
    - relation_type: prov:hadPrimarySource
      source: rhea
    - relation_type: prov:hadPrimarySource
      source: semmeddb
    - relation_type: prov:hadPrimarySource
      source: suppkg
    - relation_type: prov:hadPrimarySource
      source: ttd
    - relation_type: prov:hadPrimarySource
      source: uberon
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: clingen
    - relation_type: prov:hadPrimarySource
      source: cpdb
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: aeolus
    - relation_type: prov:hadPrimarySource
      source: chebi
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: mondo
    - relation_type: prov:hadPrimarySource
      source: civic
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: dbsnp
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:hadPrimarySource
      source: text-mining-kp
    - relation_type: prov:hadPrimarySource
      source: gdsc
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:wasInformedBy
      source: biothings-explorer
    product_url: https://bte.transltr.io/v1/team/Service%20Provider
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
taxon:
  - NCBITaxon:9606
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
