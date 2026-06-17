---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/UCDenver-ccp/CRAFT
  label: Center for Computational Pharmacology, University of Colorado Denver
creation_date: '2026-06-17T00:00:00Z'
description: The Colorado Richly Annotated Full-Text (CRAFT) Corpus is a manually
  annotated corpus of full-text biomedical journal articles. It provides concept
  annotations against multiple biomedical ontologies along with syntactic and
  coreference annotations, serving as a gold-standard resource for biomedical natural
  language processing.
domains:
- literature
- biomedical
homepage_url: https://github.com/UCDenver-ccp/CRAFT
id: craft
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Colorado Richly Annotated Full-Text Corpus
products:
- category: GraphicalInterface
  description: Repository providing the CRAFT corpus, annotations, and documentation.
  format: http
  id: craft.site
  is_public: true
  name: CRAFT Corpus Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: craft
  product_url: https://github.com/UCDenver-ccp/CRAFT
publications:
- authors:
  - Michael Bada
  - Miriam Eckert
  - Donald Evans
  - Kristin Garcia
  - Krista Shipley
  - Dmitry Sitnikov
  - William A Baumgartner
  - K Bretonnel Cohen
  - Karin Verspoor
  - Judith A Blake
  - Lawrence E Hunter
  doi: 10.1186/1471-2105-13-161
  id: https://doi.org/10.1186/1471-2105-13-161
  journal: BMC Bioinformatics
  preferred: true
  title: Concept annotation in the CRAFT corpus
  year: '2012'
repository: https://github.com/UCDenver-ccp/CRAFT
---
# Colorado Richly Annotated Full-Text Corpus

The Colorado Richly Annotated Full-Text (CRAFT) Corpus is a collection of full-text,
open-access biomedical journal articles that have been manually annotated for biomedical
concept mentions, syntax, and coreference. It is a widely used gold-standard resource for
developing and evaluating biomedical natural language processing systems.

Content includes:

- Full-text biomedical articles with concept annotations against multiple ontologies
  (including Gene Ontology, ChEBI, Cell Ontology, NCBI Taxonomy, and Entrez Gene)
- Syntactic (treebank) and coreference annotations
- Documentation and tooling distributed via the project repository

GeneCards links to concept annotations from the CRAFT corpus.
