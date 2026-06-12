---
reference_id: DOI:10.1186/s12859-022-04932-3
title: "RTX-KG2: a system for building a semantically standardized knowledge graph for translational biomedicine"
authors:
- E. C. Wood
- Amy K. Glen
- Lindsey G. Kvarfordt
- Finn Womack
- Liliana Acevedo
- Timothy S. Yoon
- Chunyu Ma
- Veronica Flores
- Meghamala Sinha
- Yodsawalai Chodpathumwan
- Arash Termehchy
- Jared C. Roach
- Luis Mendoza
- Andrew S. Hoffman
- Eric W. Deutsch
- David Koslicki
- Stephen A. Ramsey
journal: BMC Bioinformatics
year: '2022'
doi: 10.1186/s12859-022-04932-3
content_type: abstract_only
---

# RTX-KG2: a system for building a semantically standardized knowledge graph for translational biomedicine
**Authors:** E. C. Wood, Amy K. Glen, Lindsey G. Kvarfordt, Finn Womack, Liliana Acevedo, Timothy S. Yoon, Chunyu Ma, Veronica Flores, Meghamala Sinha, Yodsawalai Chodpathumwan, Arash Termehchy, Jared C. Roach, Luis Mendoza, Andrew S. Hoffman, Eric W. Deutsch, David Koslicki, Stephen A. Ramsey
**Journal:** BMC Bioinformatics (2022)
**DOI:** [10.1186/s12859-022-04932-3](https://doi.org/10.1186/s12859-022-04932-3)

## Content

Abstract


Background

Biomedical translational science is increasingly using computational reasoning on repositories of structured knowledge (such as UMLS, SemMedDB, ChEMBL, Reactome, DrugBank, and SMPDB in order to facilitate discovery of new therapeutic targets and modalities. The NCATS Biomedical Data Translator project is working to federate autonomous reasoning agents and knowledge providers within a distributed system for answering translational questions. Within that project and the broader field, there is a need for a framework that can efficiently and reproducibly build an integrated, standards-compliant, and comprehensive biomedical knowledge graph that can be downloaded in standard serialized form or queried via a public application programming interface (API).



Results


                      To create a
                      knowledge provider
                      system within the Translator project, we have developed RTX-KG2, an open-source software system for building—and hosting a web API for querying—a biomedical knowledge graph that uses an Extract-Transform-Load approach to integrate 70 knowledge sources (including the aforementioned core six sources) into a knowledge graph with provenance information including (where available) citations. The semantic layer and schema for RTX-KG2 follow the standard Biolink model to maximize interoperability. RTX-KG2 is currently being used by multiple Translator reasoning agents, both in its downloadable form and via its SmartAPI-registered interface. Serializations of RTX-KG2 are available for download in both the pre-canonicalized form and in canonicalized form (in which synonyms are merged). The current canonicalized version (KG2.7.3) of RTX-KG2 contains 6.4M nodes and 39.3M edges with a hierarchy of 77 relationship types from Biolink.
                    



Conclusion


                      RTX-KG2 is the first knowledge graph that integrates UMLS, SemMedDB, ChEMBL, DrugBank, Reactome, SMPDB, and 64 additional knowledge sources within a knowledge graph that conforms to the Biolink standard for its semantic layer and schema. RTX-KG2 is publicly available for querying via its API at
                      arax.rtx.ai/api/rtxkg2/v1.2/openapi.json
                      . The code to build RTX-KG2 is publicly available at
                      github:RTXteam/RTX-KG2
                      .