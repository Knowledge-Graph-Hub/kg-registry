---
reference_id: DOI:10.1093/nar/gkad989
title: "CADD v1.7: using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide variant predictions"
authors:
- Max Schubach
- Thorben Maass
- Lusiné Nazaretyan
- Sebastian Röner
- Martin Kircher
journal: Nucleic Acids Research
year: '2024'
doi: 10.1093/nar/gkad989
content_type: abstract_only
---

# CADD v1.7: using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide variant predictions
**Authors:** Max Schubach, Thorben Maass, Lusiné Nazaretyan, Sebastian Röner, Martin Kircher
**Journal:** Nucleic Acids Research (2024)
**DOI:** [10.1093/nar/gkad989](https://doi.org/10.1093/nar/gkad989)

## Content

Abstract
Machine Learning-based scoring and classification of genetic variants aids the assessment of clinical findings and is employed to prioritize variants in diverse genetic studies and analyses. Combined Annotation-Dependent Depletion (CADD) is one of the first methods for the genome-wide prioritization of variants across different molecular functions and has been continuously developed and improved since its original publication. Here, we present our most recent release, CADD v1.7. We explored and integrated new annotation features, among them state-of-the-art protein language model scores (Meta ESM-1v), regulatory variant effect predictions (from sequence-based convolutional neural networks) and sequence conservation scores (Zoonomia). We evaluated the new version on data sets derived from ClinVar, ExAC/gnomAD and 1000 Genomes variants. For coding effects, we tested CADD on 31 Deep Mutational Scanning (DMS) data sets from ProteinGym and, for regulatory effect prediction, we used saturation mutagenesis reporter assay data of promoter and enhancer sequences. The inclusion of new features further improved the overall performance of CADD. As with previous releases, all data sets, genome-wide CADD v1.7 scores, scripts for on-site scoring and an easy-to-use webserver are readily provided via https://cadd.bihealth.org/ or https://cadd.gs.washington.edu/ to the community.