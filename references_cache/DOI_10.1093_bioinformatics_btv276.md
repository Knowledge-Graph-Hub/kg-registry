---
reference_id: DOI:10.1093/bioinformatics/btv276
title: "Phylesystem: a git-based data store for community-curated phylogenetic estimates"
authors:
- Emily Jane McTavish
- Cody E. Hinchliff
- James F. Allman
- Joseph W. Brown
- Karen A. Cranston
- Mark T. Holder
- Jonathan A. Rees
- Stephen A. Smith
journal: Bioinformatics
year: '2015'
doi: 10.1093/bioinformatics/btv276
content_type: abstract_only
---

# Phylesystem: a git-based data store for community-curated phylogenetic estimates
**Authors:** Emily Jane McTavish, Cody E. Hinchliff, James F. Allman, Joseph W. Brown, Karen A. Cranston, Mark T. Holder, Jonathan A. Rees, Stephen A. Smith
**Journal:** Bioinformatics (2015)
**DOI:** [10.1093/bioinformatics/btv276](https://doi.org/10.1093/bioinformatics/btv276)

## Content

Abstract
Motivation: Phylogenetic estimates from published studies can be archived using general platforms like Dryad (Vision, 2010) or TreeBASE (Sanderson et al., 1994). Such services fulfill a crucial role in ensuring transparency and reproducibility in phylogenetic research. However, digital tree data files often require some editing (e.g. rerooting) to improve the accuracy and reusability of the phylogenetic statements. Furthermore, establishing the mapping between tip labels used in a tree and taxa in a single common taxonomy dramatically improves the ability of other researchers to reuse phylogenetic estimates. As the process of curating a published phylogenetic estimate is not error-free, retaining a full record of the provenance of edits to a tree is crucial for openness, allowing editors to receive credit for their work and making errors introduced during curation easier to correct.
Results: Here, we report the development of software infrastructure to support the open curation of phylogenetic data by the community of biologists. The backend of the system provides an interface for the standard database operations of creating, reading, updating and deleting records by making commits to a git repository. The record of the history of edits to a tree is preserved by git’s version control features. Hosting this data store on GitHub (http://github.com/) provides open access to the data store using tools familiar to many developers. We have deployed a server running the ‘phylesystem-api’, which wraps the interactions with git and GitHub. The Open Tree of Life project has also developed and deployed a JavaScript application that uses the phylesystem-api and other web services to enable input and curation of published phylogenetic statements.
Availability and implementation: Source code for the web service layer is available at https://github.com/OpenTreeOfLife/phylesystem-api. The data store can be cloned from: https://github.com/OpenTreeOfLife/phylesystem. A web application that uses the phylesystem web services is deployed at http://tree.opentreeoflife.org/curator. Code for that tool is available from https://github.com/OpenTreeOfLife/opentree.
Contact: mtholder@gmail.com