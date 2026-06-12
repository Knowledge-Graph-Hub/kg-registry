---
reference_id: DOI:10.1186/2041-1480-4-39
title: Introducing glycomics data into the Semantic Web
authors:
- Kiyoko F Aoki-Kinoshita
- Jerven Bolleman
- Matthew P Campbell
- Shin Kawano
- Jin-Dong Kim
- Thomas Lütteke
- Masaaki Matsubara
- Shujiro Okuda
- Rene Ranzinger
- Hiromichi Sawaki
- Toshihide Shikanai
- Daisuke Shinmachi
- Yoshinori Suzuki
- Philip Toukach
- Issaku Yamada
- Nicolle H Packer
- Hisashi Narimatsu
journal: Journal of Biomedical Semantics
year: '2013'
doi: 10.1186/2041-1480-4-39
content_type: abstract_only
---

# Introducing glycomics data into the Semantic Web
**Authors:** Kiyoko F Aoki-Kinoshita, Jerven Bolleman, Matthew P Campbell, Shin Kawano, Jin-Dong Kim, Thomas Lütteke, Masaaki Matsubara, Shujiro Okuda, Rene Ranzinger, Hiromichi Sawaki, Toshihide Shikanai, Daisuke Shinmachi, Yoshinori Suzuki, Philip Toukach, Issaku Yamada, Nicolle H Packer, Hisashi Narimatsu
**Journal:** Journal of Biomedical Semantics (2013)
**DOI:** [10.1186/2041-1480-4-39](https://doi.org/10.1186/2041-1480-4-39)

## Content

Abstract

Background
Glycoscience is a research field focusing on complex carbohydrates (otherwise known as glycans)a, which can, for example, serve as “switches” that toggle between different functions of a glycoprotein or glycolipid. Due to the advancement of glycomics technologies that are used to characterize glycan structures, many glycomics databases are now publicly available and provide useful information for glycoscience research. However, these databases have almost no link to other life science databases.


Results
In order to implement support for the Semantic Web most efficiently for glycomics research, the developers of major glycomics databases agreed on a minimal standard for representing glycan structure and annotation information using RDF (Resource Description Framework). Moreover, all of the participants implemented this standard prototype and generated preliminary RDF versions of their data. To test the utility of the converted data, all of the data sets were uploaded into a Virtuoso triple store, and several SPARQL queries were tested as “proofs-of-concept” to illustrate the utility of the Semantic Web in querying across databases which were originally difficult to implement.


Conclusions
We were able to successfully retrieve information by linking UniCarbKB, GlycomeDB and JCGGDB in a single SPARQL query to obtain our target information. We also tested queries linking UniProt with GlycoEpitope as well as lectin data with GlycomeDB through PDB. As a result, we have been able to link proteomics data with glycomics data through the implementation of Semantic Web technologies, allowing for more flexible queries across these domains.