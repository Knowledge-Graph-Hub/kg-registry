---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://support.nlm.nih.gov/
  - contact_type: email
    value: custserv@nlm.nih.gov
  label: National Library of Medicine
creation_date: '2026-02-26T00:00:00Z'
description: The National Library of Medicine is the world's largest biomedical library
  and a national resource for health professionals, scientists, and the public.
domains:
- biomedical
- literature
homepage_url: https://www.nlm.nih.gov/
id: nlm
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/web_policies.html#copyright
  label: Public Domain
name: National Library of Medicine
products:
- category: DocumentationProduct
  description: NLM public homepage and organizational entry point for literature,
    terminology, clinical, and informatics resources.
  format: http
  id: nlm.portal
  name: NLM Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_url: https://www.nlm.nih.gov/
- category: DocumentationProduct
  description: NLM Data Distribution program page, the preferred access point for bulk
    downloads of MEDLINE/PubMed baseline and daily update citation files (XML), MeSH
    data, and NLM catalog record data, with the associated terms and conditions.
  format: http
  id: nlm.data-distribution
  name: NLM Data Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: mesh
  product_url: https://www.nlm.nih.gov/databases/download/data_distrib_main.html
- category: Product
  description: Bulk downloads of NLM bibliographic catalog records for books, journals
    and other materials in NLM's collections (CatfilePlus, Catfile and Serfile), as
    baseline and update files in NLMXML, MARCXML and MARC 21 formats.
  format: mixed
  id: nlm.catalog-records
  name: NLM Catalog Record Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_url: https://www.nlm.nih.gov/databases/download/catalog.html
- category: GraphicalInterface
  description: NLM Catalog, a search interface for bibliographic records of journals,
    books, audiovisuals and other materials in NLM's collections, including NLM Unique
    IDs and journal indexing status.
  format: http
  id: nlm.catalog
  name: NLM Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_url: https://www.ncbi.nlm.nih.gov/nlmcatalog/
- category: GraphicalInterface
  description: NLM Data Discovery, a catalog of NLM products and services with links to
    product information, data downloads, APIs and other programmatic interfaces.
  format: http
  id: nlm.data-discovery
  name: NLM Data Discovery
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_url: https://datadiscovery.nlm.nih.gov/
- category: Product
  description: nlm Nodes TSV
  format: tsv
  id: obo-db-ingest.nlm.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 1156325
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.tsv
- category: MappingProduct
  description: nlm.publisher SSSOM
  format: sssom
  id: obo-db-ingest.nlm.publisher.sssom.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 140
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.sssom.tsv
- category: Product
  description: nlm.publisher Nodes TSV
  format: tsv
  id: obo-db-ingest.nlm.publisher.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 8289
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.tsv
- category: Product
  description: nlm OBO
  format: obo
  id: obo-db-ingest.nlm.obo
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 2007193
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.obo
- category: Product
  description: nlm OWL
  format: owl
  id: obo-db-ingest.nlm.owl
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 2471988
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.owl
- category: Product
  description: nlm OBO Graph JSON
  format: json
  id: obo-db-ingest.nlm.json
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 2497051
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.json
- category: MappingProduct
  description: nlm SSSOM
  format: sssom
  id: obo-db-ingest.nlm.sssom.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 422890
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.sssom.tsv
- category: Product
  description: nlm.publisher OBO
  format: obo
  id: obo-db-ingest.nlm.publisher.obo
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 9570
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.obo
- category: Product
  description: nlm.publisher OWL
  format: owl
  id: obo-db-ingest.nlm.publisher.owl
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 12531
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.owl
- category: Product
  description: nlm.publisher OBO Graph JSON
  format: json
  id: obo-db-ingest.nlm.publisher.json
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 12675
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.json
rrid: SCR_011446
synonyms:
- NLM
warnings:
- NLM data include U.S. government works not protected by U.S. copyright, but also
  abstracts and other material that may be protected by copyright; bulk downloads are
  subject to the NLM Terms and Conditions, which require acknowledging NLM as the source.
---
# National Library of Medicine

The National Library of Medicine (NLM), on the campus of the National Institutes of Health in Bethesda, Maryland, has been a center of information innovation since its founding in 1836. It is the world's largest biomedical library, maintaining a large print collection and producing electronic information resources that are searched billions of times each year. NLM also supports and conducts research, development and training in biomedical informatics and health information technology, and coordinates the Network of the National Library of Medicine, with more than 8,000 members.

## Organization and resources

NLM is the home of the National Center for Biotechnology Information (NCBI), which runs PubMed, PubMed Central, GenBank and many other molecular and literature databases, and of the Lister Hill National Center for Biomedical Communications (LHNCBC). NLM produces or hosts widely used resources including PubMed/MEDLINE, Medical Subject Headings (MeSH), the Unified Medical Language System (UMLS), RxNorm, ClinicalTrials.gov, MedlinePlus, the NLM Catalog and Digital Collections.

## Data access

The NLM Data Distribution program is the preferred route for bulk downloads of MEDLINE/PubMed citation records (an annual XML baseline plus daily update files), MeSH, and catalog record data. Catalog data are also available through the NCBI E-utilities API and a Z39.50 endpoint. NLM Data Discovery lists NLM datasets, downloads and APIs. Some products, such as UMLS, require a UMLS Terminology Services (UTS) account and license agreement.

## Usage terms

NLM data include U.S. government works not protected by U.S. copyright, along with abstracts and other material that may be under copyright. No signed license is needed for the Data Distribution downloads, but users agree to the NLM Terms and Conditions, including acknowledging NLM as the source and not implying NLM endorsement.
