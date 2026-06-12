---
reference_id: DOI:10.1186/s12859-020-3517-7
title: Broad-coverage biomedical relation extraction with SemRep
authors:
- Halil Kilicoglu
- Graciela Rosemblat
- Marcelo Fiszman
- Dongwook Shin
journal: BMC Bioinformatics
year: '2020'
doi: 10.1186/s12859-020-3517-7
content_type: abstract_only
---

# Broad-coverage biomedical relation extraction with SemRep
**Authors:** Halil Kilicoglu, Graciela Rosemblat, Marcelo Fiszman, Dongwook Shin
**Journal:** BMC Bioinformatics (2020)
**DOI:** [10.1186/s12859-020-3517-7](https://doi.org/10.1186/s12859-020-3517-7)

## Content

AbstractBackgroundIn the era of information overload, natural language processing (NLP) techniques are increasingly needed to support advanced biomedical information management and discovery applications. In this paper, we present an in-depth description of SemRep, an NLP system that extracts semantic relations from PubMed abstracts using linguistic principles and UMLS domain knowledge. We also evaluate SemRep on two datasets. In one evaluation, we use a manually annotated test collection and perform a comprehensive error analysis. In another evaluation, we assess SemRep’s performance on the CDR dataset, a standard benchmark corpus annotated with causal chemical-disease relationships.ResultsA strict evaluation of SemRep on our manually annotated dataset yields 0.55 precision, 0.34 recall, and 0.42 F1score. A relaxed evaluation, which more accurately characterizes SemRep performance, yields 0.69 precision, 0.42 recall, and 0.52 F1score. An error analysis reveals named entity recognition/normalization as the largest source of errors (26.9%), followed by argument identification (14%) and trigger detection errors (12.5%). The evaluation on the CDR corpus yields 0.90 precision, 0.24 recall, and 0.38 F1score. The recall and the F1score increase to 0.35 and 0.50, respectively, when the evaluation on this corpus is limited to sentence-bound relationships, which represents a fairer evaluation, as SemRep operates at the sentence level.ConclusionsSemRep is a broad-coverage, interpretable, strong baseline system for extracting semantic relations from biomedical text. It also underpins SemMedDB, a literature-scale knowledge graph based on semantic relations. Through SemMedDB, SemRep has had significant impact in the scientific community, supporting a variety of clinical and translational applications, including clinical decision making, medical diagnosis, drug repurposing, literature-based discovery and hypothesis generation, and contributing to improved health outcomes. In ongoing development, we are redesigning SemRep to increase its modularity and flexibility, and addressing weaknesses identified in the error analysis.