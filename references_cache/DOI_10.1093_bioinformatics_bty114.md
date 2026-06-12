---
reference_id: DOI:10.1093/bioinformatics/bty114
title: A global network of biomedical relationships derived from text
authors:
- Bethany Percha
- Russ B Altman
journal: Bioinformatics
year: '2018'
doi: 10.1093/bioinformatics/bty114
content_type: abstract_only
---

# A global network of biomedical relationships derived from text
**Authors:** Bethany Percha, Russ B Altman
**Journal:** Bioinformatics (2018)
**DOI:** [10.1093/bioinformatics/bty114](https://doi.org/10.1093/bioinformatics/bty114)

## Content

AbstractMotivationThe biomedical community’s collective understanding of how chemicals, genes and phenotypes interact is distributed across the text of over 24 million research articles. These interactions offer insights into the mechanisms behind higher order biochemical phenomena, such as drug-drug interactions and variations in drug response across individuals. To assist their curation at scale, we must understand what relationship types are possible and map unstructured natural language descriptions onto these structured classes. We used NCBI’s PubTator annotations to identify instances of chemical, gene and disease names in Medline abstracts and applied the Stanford dependency parser to find connecting dependency paths between pairs of entities in single sentences. We combined a published ensemble biclustering algorithm (EBC) with hierarchical clustering to group the dependency paths into semantically-related categories, which we annotated with labels, or ‘themes’ (‘inhibition’ and ‘activation’, for example). We evaluated our theme assignments against six human-curated databases: DrugBank, Reactome, SIDER, the Therapeutic Target Database, OMIM and PharmGKB.ResultsClustering revealed 10 broad themes for chemical-gene relationships, 7 for chemical-disease, 10 for gene-disease and 9 for gene–gene. In most cases, enriched themes corresponded directly to known database relationships. Our final dataset, represented as a network, contained 37 491 thematically-labeled chemical-gene edges, 2 021 192 chemical-disease edges, 136 206 gene-disease edges and 41 418 gene–gene edges, each representing a single-sentence description of an interaction from somewhere in the literature.Availability and implementationThe complete network is available on Zenodo (https://zenodo.org/record/1035500). We have also provided the full set of dependency paths connecting biomedical entities in Medline abstracts, with associated sentences, for future use by the biomedical research community.Supplementary informationSupplementary data are available at Bioinformatics online.