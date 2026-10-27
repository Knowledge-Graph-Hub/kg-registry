---
reference_id: DOI:10.1093/bioinformatics/btad130
title: Prediction and curation of missing biomedical identifier mappings with Biomappings
authors:
- Charles Tapley Hoyt
- Amelia L Hoyt
- Benjamin M Gyori
journal: Bioinformatics
year: '2023'
doi: 10.1093/bioinformatics/btad130
content_type: abstract_only
---

# Prediction and curation of missing biomedical identifier mappings with Biomappings
**Authors:** Charles Tapley Hoyt, Amelia L Hoyt, Benjamin M Gyori
**Journal:** Bioinformatics (2023)
**DOI:** [10.1093/bioinformatics/btad130](https://doi.org/10.1093/bioinformatics/btad130)

## Content

Abstract

Motivation
Biomedical identifier resources (such as ontologies, taxonomies, and controlled vocabularies) commonly overlap in scope and contain equivalent entries under different identifiers. Maintaining mappings between these entries is crucial for interoperability and the integration of data and knowledge. However, there are substantial gaps in available mappings motivating their semi-automated curation.


Results
Biomappings implements a curation workflow for missing mappings which combines automated prediction with human-in-the-loop curation. It supports multiple prediction approaches and provides a web-based user interface for reviewing predicted mappings for correctness, combined with automated consistency checking. Predicted and curated mappings are made available in public, version-controlled resource files on GitHub. Biomappings currently makes available 9274 curated mappings and 40 691 predicted ones, providing previously missing mappings between widely used identifier resources covering small molecules, cell lines, diseases, and other concepts. We demonstrate the value of Biomappings on case studies involving predicting and curating missing mappings among cancer cell lines as well as small molecules tested in clinical trials. We also present how previously missing mappings curated using Biomappings were contributed back to multiple widely used community ontologies.


Availability and implementation
The data and code are available under the CC0 and MIT licenses at https://github.com/biopragmatics/biomappings.