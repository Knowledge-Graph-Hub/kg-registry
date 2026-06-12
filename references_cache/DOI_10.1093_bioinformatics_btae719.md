---
reference_id: DOI:10.1093/bioinformatics/btae719
title: PheWAS analysis on large-scale biobank data with PheTK
authors:
- Tam C Tran
- David J Schlueter
- Chenjie Zeng
- Huan Mo
- Robert J Carroll
- Joshua C Denny
journal: Bioinformatics
year: '2024'
doi: 10.1093/bioinformatics/btae719
content_type: abstract_only
---

# PheWAS analysis on large-scale biobank data with PheTK
**Authors:** Tam C Tran, David J Schlueter, Chenjie Zeng, Huan Mo, Robert J Carroll, Joshua C Denny
**Journal:** Bioinformatics (2024)
**DOI:** [10.1093/bioinformatics/btae719](https://doi.org/10.1093/bioinformatics/btae719)

## Content

Abstract

Summary
With the rapid growth of genetic data linked to electronic health record (EHR) data in huge cohorts, large-scale phenome-wide association study (PheWAS) have become powerful discovery tools in biomedical research. PheWAS is an analysis method to study phenotype associations utilizing longitudinal EHR data. Previous PheWAS packages were developed mostly with smaller datasets and with earlier PheWAS approaches. PheTK was designed to simplify analysis and efficiently handle biobank-scale data. PheTK uses multithreading and supports a full PheWAS workflow including extraction of data from OMOP databases and Hail matrix tables as well as PheWAS analysis for both phecode version 1.2 and phecodeX. Benchmarking results showed PheTK took 64% less time than the R PheWAS package to complete the same workflow. PheTK can be run locally or on cloud platforms such as the All of Us Researcher Workbench (All of Us) or the UK Biobank (UKB) Research Analysis Platform (RAP).


Availability and implementation
The PheTK package is freely available on the Python Package Index, on GitHub under GNU General Public License (GPL-3) at https://github.com/nhgritctran/PheTK, and on Zenodo, DOI 10.5281/zenodo.14217954, at https://doi.org/10.5281/zenodo.14217954. PheTK is implemented in Python and platform independent.