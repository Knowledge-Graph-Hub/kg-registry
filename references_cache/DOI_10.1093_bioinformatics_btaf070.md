---
reference_id: DOI:10.1093/bioinformatics/btaf070
title: "Associations on the Fly, a new feature aiming to facilitate exploration of the Open Targets Platform evidence"
authors:
- Carlos Cruz-Castillo
- Luca Fumis
- Chintan Mehta
- Ricardo Esteban Martinez-Osorio
- Juan Maria Roldan-Romero
- Helena Cornu
- Prashant Uniyal
- Antonio Solano-Roman
- Miguel Carmona
- David Ochoa
- Ellen Mary McDonagh
- Annalisa Buniello
journal: Bioinformatics
year: '2025'
doi: 10.1093/bioinformatics/btaf070
content_type: abstract_only
---

# Associations on the Fly, a new feature aiming to facilitate exploration of the Open Targets Platform evidence
**Authors:** Carlos Cruz-Castillo, Luca Fumis, Chintan Mehta, Ricardo Esteban Martinez-Osorio, Juan Maria Roldan-Romero, Helena Cornu, Prashant Uniyal, Antonio Solano-Roman, Miguel Carmona, David Ochoa, Ellen Mary McDonagh, Annalisa Buniello
**Journal:** Bioinformatics (2025)
**DOI:** [10.1093/bioinformatics/btaf070](https://doi.org/10.1093/bioinformatics/btaf070)

## Content

Abstract

Motivation
The Open Targets Platform (https://platform.opentargets.org) is a unique, comprehensive, open-source resource supporting systematic identification and prioritisation of targets for drug discovery. The Platform combines, harmonizes and integrates data from &gt;20 diverse sources to provide target–disease associations, covering evidence derived from genetic associations, somatic mutations, known drugs, differential expression, animal models, pathways and systems biology. An in-house target identification scoring framework weighs the evidence from each data source and type, contributing to an overall score for each of the 7.8M target–disease associations. However, the old infrastructure did not allow user-led dynamic adjustments in the contribution of different evidence types for target prioritisation, a limitation frequently raised by our user community. Furthermore, the previous Platform user interface did not support navigation and exploration of the underlying target–disease evidence on the same page, occasionally making the user journey counterintuitive.


Results
Here, we describe ‘Associations on the Fly’ (AOTF), a new Platform feature—developed with a user-centred vision—that enables the user to formulate more flexible therapeutic hypotheses through dynamic adjustment of the weight of contributing evidence from each source, altering the prioritisation of targets.


Availability and implementation
The codebases that power the Platform—including our pipelines, GraphQL API, and React UI—are all open source and licensed under the APACHE LICENSE, VERSION 2.0. You can find all of our code repositories on GitHub at https://github.com/opentargets and on Zenodo at https://zenodo.org/records/14392214. This tool was implemented using React v18 and its code is accessible here: (https://github.com/opentargets/ot-ui-apps). The tools are accessible through the Open Targets Platform web interface (https://platform.opentargets.org/) and GraphQL API (https://platform-docs.opentargets.org/data-access/graphql-api). Data is available for download here: (https://platform.opentargets.org/downloads) and from the EMBL-EBI FTP: (https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/).