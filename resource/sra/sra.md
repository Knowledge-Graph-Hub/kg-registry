---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: sra@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/sra/docs/
  label: NCBI SRA
creation_date: '2026-05-21T00:00:00Z'
description: The Sequence Read Archive (SRA) is NCBI's public archive of high-throughput
  sequencing data and part of the International Nucleotide Sequence Database Collaboration,
  providing searchable access to raw sequence runs, metadata, cloud delivery, and
  download tooling.
domains:
- genomics
- biomedical
- organisms
homepage_url: https://www.ncbi.nlm.nih.gov/sra
id: sra
last_modified_date: '2026-05-22T00:00:00Z'
layout: resource_detail
name: Sequence Read Archive
products:
- category: GraphicalInterface
  description: Main SRA search and browse interface for studies, experiments, runs,
    and associated metadata.
  format: http
  id: sra.portal
  name: SRA Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://www.ncbi.nlm.nih.gov/sra
- category: DocumentationProduct
  description: Official SRA documentation covering submission, search, download, cloud
    usage, and archive behavior.
  format: http
  id: sra.docs
  name: SRA Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://www.ncbi.nlm.nih.gov/sra/docs/
- category: GraphicalInterface
  description: SRA Run Selector interface for exporting run-level metadata tables
    and filtering search results.
  format: http
  id: sra.run_selector
  name: SRA Run Selector
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://www.ncbi.nlm.nih.gov/Traces/study/
- category: Product
  description: Latest human gene-level ARCHS4 expression matrix in HDF5 format using
    Ensembl 107 annotations
  format: hdf5
  id: archs4.human.gene_counts
  name: ARCHS4 Human Gene Counts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  product_file_size: 61899310543
  product_url: https://s3.dev.maayanlab.cloud/archs4/files/human_gene_v2.latest.h5
- category: Product
  description: Latest mouse gene-level ARCHS4 expression matrix in HDF5 format using
    Ensembl 107 annotations
  format: hdf5
  id: archs4.mouse.gene_counts
  name: ARCHS4 Mouse Gene Counts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  product_file_size: 49065676268
  product_url: https://s3.dev.maayanlab.cloud/archs4/files/mouse_gene_v2.latest.h5
- category: Product
  description: Latest human transcript-level ARCHS4 expression matrix in HDF5 format
    using Ensembl 107 annotations
  format: hdf5
  id: archs4.human.transcript_counts
  name: ARCHS4 Human Transcript Counts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  product_file_size: 192013010374
  product_url: https://s3.dev.maayanlab.cloud/archs4/files/human_transcript_v2.latest.h5
- category: Product
  description: Latest mouse transcript-level ARCHS4 expression matrix in HDF5 format
    using Ensembl 107 annotations
  format: hdf5
  id: archs4.mouse.transcript_counts
  name: ARCHS4 Mouse Transcript Counts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  product_file_size: 113637723557
  product_url: https://s3.dev.maayanlab.cloud/archs4/files/mouse_transcript_v2.latest.h5
- category: Product
  description: Collection page for ARCHS4 Zoo downloads covering selected additional
    species beyond human and mouse
  format: hdf5
  id: archs4.zoo
  name: ARCHS4 Zoo Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  product_url: https://archs4.org/zoo
synonyms:
- SRA
- Sequence Read Archive
---

# Sequence Read Archive

SRA is the largest public repository of high-throughput sequencing data and serves as
NCBI's contribution to the INSDC sequence archive ecosystem. It supports archival storage,
search, metadata export, toolkit-based download, cloud access patterns, and controlled-access
handling for sensitive human data via dbGaP-linked workflows.

The ARCHS4 products listed here are downstream matrices built from SRA and GEO RNA-seq inputs.
They remain attached as derived products because SRA is a direct upstream source of the sequence
data used in those uniformly processed expression releases.