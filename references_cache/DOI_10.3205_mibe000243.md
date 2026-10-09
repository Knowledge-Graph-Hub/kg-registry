---
reference_id: DOI:10.3205/mibe000243
title: A web-based pathway enrichment analysis module for the PharMeBINet database
authors:
- "Königs, Cassandra"
- "Dietrich, Theresa"
journal: German Medical Science GMS Publishing House
year: '2023'
doi: 10.3205/mibe000243
keywords:
- pathway enrichment analysis
- heterogeneous database
- Pathway-Enrichment-Analyse
- heterogene Datenbank
- Medicine and health
content_type: abstract_only
---

# A web-based pathway enrichment analysis module for the PharMeBINet database
**Authors:** Königs, Cassandra, Dietrich, Theresa
**Journal:** German Medical Science GMS Publishing House (2023)
**DOI:** [10.3205/mibe000243](https://doi.org/10.3205/mibe000243)

## Content

In modern molecular biology, the quantification of proteins, RNA, and DNA is a standard procedure. Resulting in the generation of large data, researchers need appropriate tools for interpretation. A common method for interpreting gene expression data is pathway enrichment analysis. The heterogeneous pharmacological medical biochemical network (PharMeBINet) is a Neo4j database in combination with a website for browsing and analysis available at [link:https://pharmebi.net*https://pharmebi.net]. Here we present a new analysis module for the website developed in JavaScript that applies enrichment analyses to gene expression data. The analysis has two methods for enrichment: Fisher’s exact test and modified Fisher’s exact test. The modified test considers the order of the gene expression data. Additionally, Bonferroni-correction, Dunn-Šidák correction, Holm-Bonferroni method, and Benjamin-Hochberg method are implemented to reduce the false positive pathways. The analysis was tested with the gene expression data of the first cluster described by the analysis of Shin et al. The result of Fisher’s exact test with corrected p-values (p&lt;0.01) was 68 pathways. In contrast, the result of the modified Fisher’s exact test was 104 different pathways. The pathway with the best p-value is “Generation of second messenger molecules”. The results are presented in multiple forms. The first is a table ordered by p-values. Secondly, a bar plot with the log10(p-value) for all pathways provides a general impression of the resulting pathways. Thirdly, a combination of heat map and bar plot for all pathway gene combinations shows an overview of how the genes are connected to the relevant pathways and with the p-values beside it. Further, the input data was analyzed. The results are presented as a pie chart and bar plot. The pie chart shows how many of the input genes have a connection to pathways and how many do not. The bar plot displays the number of enriched pathways the genes appear in. The resulting pathways are well-fitting results for the gene expression data. This analysis module returns similar results compared to other enrichment tools.