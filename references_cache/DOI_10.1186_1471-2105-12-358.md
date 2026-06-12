---
reference_id: DOI:10.1186/1471-2105-12-358
title: "Clustering with position-specific constraints on variance: Applying redescending M-estimators to label-free LC-MS data analysis"
authors:
- Rudolf Frühwirth
- D R Mani
- Saumyadipta Pyne
journal: BMC Bioinformatics
year: '2011'
doi: 10.1186/1471-2105-12-358
content_type: abstract_only
---

# Clustering with position-specific constraints on variance: Applying redescending M-estimators to label-free LC-MS data analysis
**Authors:** Rudolf Frühwirth, D R Mani, Saumyadipta Pyne
**Journal:** BMC Bioinformatics (2011)
**DOI:** [10.1186/1471-2105-12-358](https://doi.org/10.1186/1471-2105-12-358)

## Content

AbstractBackgroundClustering is a widely applicable pattern recognition method for discovering groups of similar observations in data. While there are a large variety of clustering algorithms, very few of these can enforce constraints on the variation of attributes for data points included in a given cluster. In particular, a clustering algorithm that can limit variation within a cluster according to that cluster's position (centroid location) can produce effective and optimal results in many important applications ranging from clustering of silicon pixels or calorimeter cells in high-energy physics to label-free liquid chromatography based mass spectrometry (LC-MS) data analysis in proteomics and metabolomics.ResultsWe present MEDEA (M-Estimator with DEterministic Annealing), an M-estimator based, new unsupervised algorithm that is designed to enforce position-specific constraints on variance during the clustering process. The utility of MEDEA is demonstrated by applying it to the problem of "peak matching"--identifying the common LC-MS peaks across multiple samples--in proteomic biomarker discovery. Using real-life datasets, we show that MEDEA not only outperforms current state-of-the-art model-based clustering methods, but also results in an implementation that is significantly more efficient, and hence applicable to much larger LC-MS data sets.ConclusionsMEDEA is an effective and efficient solution to the problem of peak matching in label-free LC-MS data. The program implementing the MEDEA algorithm, including datasets, clustering results, and supplementary information is available from the author website athttp://www.hephy.at/user/fru/medea/.