---
reference_id: DOI:10.2196/17964
title: "Visualization Environment for Federated Knowledge Graphs: Development of an Interactive Biomedical Query Language and Web Application Interface"
authors:
- Steven Cox
- Stanley C Ahalt
- James Balhoff
- Chris Bizon
- Karamarie Fecho
- Yaphet Kebede
- Kenneth Morton
- Alexander Tropsha
- Patrick Wang
- Hao Xu
journal: JMIR Medical Informatics
year: '2020'
doi: 10.2196/17964
content_type: abstract_only
---

# Visualization Environment for Federated Knowledge Graphs: Development of an Interactive Biomedical Query Language and Web Application Interface
**Authors:** Steven Cox, Stanley C Ahalt, James Balhoff, Chris Bizon, Karamarie Fecho, Yaphet Kebede, Kenneth Morton, Alexander Tropsha, Patrick Wang, Hao Xu
**Journal:** JMIR Medical Informatics (2020)
**DOI:** [10.2196/17964](https://doi.org/10.2196/17964)

## Content

Background
Efforts are underway to semantically integrate large biomedical knowledge graphs using common upper-level ontologies to federate graph-oriented application programming interfaces (APIs) to the data. However, federation poses several challenges, including query routing to appropriate knowledge sources, generation and evaluation of answer subsets, semantic merger of those answer subsets, and visualization and exploration of results.


Objective
We aimed to develop an interactive environment for query, visualization, and deep exploration of federated knowledge graphs.


Methods
We developed a biomedical query language and web application interphase—termed as Translator Query Language (TranQL)—to query semantically federated knowledge graphs and explore query results. TranQL uses the Biolink data model as an upper-level biomedical ontology and an API standard that has been adopted by the Biomedical Data Translator Consortium to specify a protocol for expressing a query as a graph of Biolink data elements compiled from statements in the TranQL query language. Queries are mapped to federated knowledge sources, and answers are merged into a knowledge graph, with mappings between the knowledge graph and specific elements of the query. The TranQL interactive web application includes a user interface to support user exploration of the federated knowledge graph.


Results
We developed 2 real-world use cases to validate TranQL and address biomedical questions of relevance to translational science. The use cases posed questions that traversed 2 federated Translator API endpoints: Integrated Clinical and Environmental Exposures Service (ICEES) and Reasoning Over Biomedical Objects linked in Knowledge Oriented Pathways (ROBOKOP). ICEES provides open access to observational clinical and environmental data, and ROBOKOP provides access to linked biomedical entities, such as “gene,” “chemical substance,” and “disease,” that are derived largely from curated public data sources. We successfully posed queries to TranQL that traversed these endpoints and retrieved answers that we visualized and evaluated.


Conclusions
TranQL can be used to ask questions of relevance to translational science, rapidly obtain answers that require assertions from a federation of knowledge sources, and provide valuable insights for translational research and clinical practice.