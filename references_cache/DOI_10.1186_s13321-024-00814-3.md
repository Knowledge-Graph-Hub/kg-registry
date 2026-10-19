---
reference_id: DOI:10.1186/s13321-024-00814-3
title: Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling
authors:
- Kamel Mansouri
- José T. Moreira-Filho
- Charles N. Lowe
- Nathaniel Charest
- Todd Martin
- Valery Tkachenko
- Richard Judson
- Mike Conway
- Nicole C. Kleinstreuer
- Antony J. Williams
journal: Journal of Cheminformatics
year: '2024'
doi: 10.1186/s13321-024-00814-3
content_type: abstract_only
---

# Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling
**Authors:** Kamel Mansouri, José T. Moreira-Filho, Charles N. Lowe, Nathaniel Charest, Todd Martin, Valery Tkachenko, Richard Judson, Mike Conway, Nicole C. Kleinstreuer, Antony J. Williams
**Journal:** Journal of Cheminformatics (2024)
**DOI:** [10.1186/s13321-024-00814-3](https://doi.org/10.1186/s13321-024-00814-3)

## Content

Abstract

                    The rapid increase of publicly available chemical structures and associated experimental data presents a valuable opportunity to build robust QSAR models for applications in different fields. However, the common concern is the quality of both the chemical structure information and associated experimental data. This is especially true when those data are collected from multiple sources as chemical substance mappings can contain many duplicate structures and molecular inconsistencies. Such issues can impact the resulting molecular descriptors and their mappings to experimental data and, subsequently, the quality of the derived models in terms of accuracy, repeatability, and reliability. Herein we describe the development of an automated workflow to standardize chemical structures according to a set of standard rules and generate two and/or three-dimensional “QSAR-ready” forms prior to the calculation of molecular descriptors. The workflow was designed in the KNIME workflow environment and consists of three high-level steps. First, a structure encoding is read, and then the resulting in-memory representation is cross-referenced with any existing identifiers for consistency. Finally, the structure is standardized using a series of operations including desalting, stripping of stereochemistry (for two-dimensional structures), standardization of tautomers and nitro groups, valence correction, neutralization when possible, and then removal of duplicates. This workflow was initially developed to support collaborative modeling QSAR projects to ensure consistency of the results from the different participants. It was then updated and generalized for other modeling applications. This included modification of the “QSAR-ready” workflow to generate “MS-ready structures” to support the generation of substance mappings and searches for software applications related to non-targeted analysis mass spectrometry. Both QSAR and MS-ready workflows are freely available in KNIME, via standalone versions on GitHub, and as docker container resources for the scientific community.
                    Scientific contribution
                    : This work pioneers an automated workflow in KNIME, systematically standardizing chemical structures to ensure their readiness for QSAR modeling and broader scientific applications. By addressing data quality concerns through desalting, stereochemistry stripping, and normalization, it optimizes molecular descriptors' accuracy and reliability. The freely available resources in KNIME, GitHub, and docker containers democratize access, benefiting collaborative research and advancing diverse modeling endeavors in chemistry and mass spectrometry.