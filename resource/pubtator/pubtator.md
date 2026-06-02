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
creation_date: '2025-05-15T00:00:00Z'
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
last_modified_date: '2025-12-13T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://www.ncbi.nlm.nih.gov/research/pubtator3-api/
- category: Product
  description: Bulk downloads of annotated articles and extraction summaries for entities
    and relations
  id: pubtator.bulk
  name: PubTator 3.0 Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator3
- category: GraphicalInterface
  description: Web interface for exploring PubTator annotations with semantic and
    relation search capabilities
  id: pubtator.site
  is_public: true
  name: PubTator 3.0 Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://www.ncbi.nlm.nih.gov/research/pubtator3/
- category: GraphProduct
  description: "Text-mined biomedical knowledge graph of gene\u2013disease\u2013drug\
    \ relationships (semantic themes)"
  id: gnbr.graph
  name: GNBR graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://zenodo.org/records/3459420
- category: GraphicalInterface
  description: Web interface for browsing eMIND text-mined variant-impact annotations
    in Alzheimer's disease and related dementia literature
  format: http
  id: emind.site
  name: eMIND Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emind
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  product_url: https://research.bioinformatics.udel.edu/itextmine/integrate/search/emind/medline/*
- category: Product
  description: Gzipped JSON export of the eMIND text-mined literature annotations
    for variant impacts in Alzheimer's disease and related dementias
  format: json
  id: emind.json
  name: eMIND JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emind
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  product_file_size: 941473
  product_url: https://hershey.dbi.udel.edu/textmining/export/emind/eMIND_iTextmine.json.gz
- category: GraphProduct
  description: Current iPTMnet PTM record table with PTM type, source, UniProt protein,
    organism, site, enzyme, relation identifiers, and publication evidence.
  format: tsv
  id: iptmnet.ptm
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet PTM Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 44116546
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/ptm.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dbptm
  - relation_type: prov:wasDerivedFrom
    source: dbsno
  - relation_type: prov:wasDerivedFrom
    source: efip
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: nextprot
  - relation_type: prov:wasDerivedFrom
    source: p3db
  - relation_type: prov:wasDerivedFrom
    source: phosphoelm
  - relation_type: prov:wasDerivedFrom
    source: phosphogrid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: phosphat
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  - relation_type: prov:wasDerivedFrom
    source: rlims-p
  - relation_type: prov:wasDerivedFrom
    source: signor
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: GraphicalInterface
  description: Web interface for searching and retrieving variant information from
    35+ million PubMed articles with autocomplete, filtering, and entity highlighting
  format: http
  id: litvar.web_interface
  name: LitVar Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: litvar
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clingen
  - relation_type: prov:wasInformedBy
    source: clinvar
  - relation_type: prov:wasInformedBy
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:used
    source: pubtator
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to variant summaries, publications,
    search, and gene-level variant queries
  format: http
  id: litvar.api
  name: LitVar API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: litvar
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2-api/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clingen
  - relation_type: prov:wasInformedBy
    source: clinvar
  - relation_type: prov:wasInformedBy
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:used
    source: pubtator
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
taxon:
- NCBITaxon:9606
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