---
reference_id: DOI:10.1093/database/baae133
title: A change language for ontologies and knowledge graphs
authors:
- Harshad Hegde
- Jennifer Vendetti
- Damien Goutte-Gattat
- J Harry Caufield
- John B Graybeal
- Nomi L Harris
- Naouel Karam
- Christian Kindermann
- Nicolas Matentzoglu
- James A Overton
- Mark A Musen
- Christopher J Mungall
journal: Database
year: '2025'
doi: 10.1093/database/baae133
content_type: abstract_only
---

# A change language for ontologies and knowledge graphs
**Authors:** Harshad Hegde, Jennifer Vendetti, Damien Goutte-Gattat, J Harry Caufield, John B Graybeal, Nomi L Harris, Naouel Karam, Christian Kindermann, Nicolas Matentzoglu, James A Overton, Mark A Musen, Christopher J Mungall
**Journal:** Database (2025)
**DOI:** [10.1093/database/baae133](https://doi.org/10.1093/database/baae133)

## Content

Abstract
Ontologies and knowledge graphs (KGs) are general-purpose computable representations of some domain, such as human anatomy, and are frequently a crucial part of modern information systems. Most of these structures change over time, incorporating new knowledge or information that was previously missing. Managing these changes is a challenge, both in terms of communicating changes to users and providing mechanisms to make it easier for multiple stakeholders to contribute. To fill that need, we have created KGCL, the Knowledge Graph Change Language (https://github.com/INCATools/kgcl), a standard data model for describing changes to KGs and ontologies at a high level, and an accompanying human-readable Controlled Natural Language (CNL). This language serves two purposes: a curator can use it to request desired changes, and it can also be used to describe changes that have already happened, corresponding to the concepts of “apply patch” and “diff” commonly used for managing changes in text documents and computer programs. Another key feature of KGCL is that descriptions are at a high enough level to be useful and understood by a variety of stakeholders—e.g. ontology edits can be specified by commands like “add synonym ‘arm’ to ‘forelimb’” or “move ‘Parkinson disease’ under ‘neurodegenerative disease’.” We have also built a suite of tools for managing ontology changes. These include an automated agent that integrates with and monitors GitHub ontology repositories and applies any requested changes and a new component in the BioPortal ontology resource that allows users to make change requests directly from within the BioPortal user interface. Overall, the KGCL data model, its CNL, and associated tooling allow for easier management and processing of changes associated with the development of ontologies and KGs.
Database URL: https://github.com/INCATools/kgcl