---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/research/pubtator3/
  id: ncbi
  label: National Center for Biotechnology Information (NCBI)
description: PubTator 3.0 is an AI-powered biomedical literature resource that uses
  state-of-the-art AI techniques to provide semantic and relation searches for key
  biomedical entities like proteins, genetic variants, diseases and chemicals. It
  offers over one billion entity and relation annotations across approximately 36
  million PubMed abstracts and 6 million full-text articles from the PMC open access
  subset, updated weekly.
domains:
- literature
- biomedical
- health
- genomics
- pharmacology
homepage_url: https://www.ncbi.nlm.nih.gov/research/pubtator3/
id: pubtator
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain
name: PubTator
products:
- category: ProgrammingInterface
  description: PubTator 3.0 API for programmatic access to entity annotation, relation
    search, and other features
  id: pubtator.api
  is_public: true
  name: PubTator 3.0 API
  original_source:
  - pubtator
  product_url: https://www.ncbi.nlm.nih.gov/research/pubtator3-api/
  secondary_source:
  - pubtator
- category: Product
  description: Bulk downloads of annotated articles and extraction summaries for entities
    and relations
  id: pubtator.bulk
  name: PubTator 3.0 Bulk Downloads
  original_source:
  - pubtator
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator3
  secondary_source:
  - pubtator
- category: GraphicalInterface
  description: Web interface for exploring PubTator annotations with semantic and
    relation search capabilities
  id: pubtator.site
  is_public: true
  name: PubTator 3.0 Web Interface
  original_source:
  - pubtator
  product_url: https://www.ncbi.nlm.nih.gov/research/pubtator3/
  secondary_source:
  - pubtator
- category: GraphProduct
  description: Text-mined biomedical knowledge graph of gene–disease–drug relationships
    (semantic themes)
  id: gnbr.graph
  name: GNBR graph
  original_source:
  - pubtator
  product_url: https://zenodo.org/records/3459420
  secondary_source:
  - gnbr
publications:
- authors:
  - Wei CH
  - Allot A
  - Lai PT
  - Leaman R
  - Tian S
  - Luo L
  - Jin Q
  - Wang Z
  - Chen Q
  - Lu Z
  doi: 10.1093/nar/gkae235
  id: doi:10.1093/nar/gkae235
  journal: Nucleic Acids Research
  preferred: true
  title: 'PubTator 3.0: an AI-powered literature resource for unlocking biomedical
    knowledge'
  year: '2024'
repository: https://github.com/ncbi/AIONER
---

# PubTator 3.0

PubTator 3.0 is a comprehensive biomedical literature resource that leverages state-of-the-art AI techniques to annotate and make searchable over one billion entity and relation annotations across approximately 36 million PubMed abstracts and 6 million full-text articles from the PMC open access subset.

## Features

- Semantic search for six key biomedical entity types: genes, diseases, chemicals, genetic variants, species, and cell lines
- Relation search across 12 common relation types between entities
- Query auto-completion to enhance search accuracy
- Prioritized search results based on entity relationships
- Full-text search in both abstracts and open access articles
- Advanced filtering options
- Weekly updates to include new literature

## Technical Components

PubTator 3.0 is built on several advanced NLP components, all of which are available as open-source tools:

- **AIONER**: An all-in-one named entity recognizer for biomedical text
- **GNorm2**: A system for gene name normalization
- **tmVar3**: A tool for genetic variant normalization
- **BioREx**: A comprehensive biomedical relation extraction system

These components work together to provide highly accurate entity recognition and relation extraction, making PubTator 3.0 a valuable resource for biomedical researchers and data scientists.