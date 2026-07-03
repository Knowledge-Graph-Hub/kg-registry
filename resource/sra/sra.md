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
last_modified_date: '2026-06-18T00:00:00Z'
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
- category: Product
  description: Computational pipeline for gathering publicly available RNA-seq data,
    aligning reads, performing quality control, computing iModulons using independent
    component analysis, and formatting dashboard files. Enables users to generate
    their own iModulon decompositions from transcriptomic datasets.
  format: http
  id: imodulondb.imodulonminer
  name: iModulonMiner Pipeline
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imodulondb
  product_url: https://github.com/SBRG/iModulonMiner
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: sra
- category: Product
  description: Modulome workflow for scraping publicly available data for an organism,
    aligning reads, quality control, and computing iModulons. Used to expand iModulonDB
    across the prokaryotic evolutionary tree by processing data from the Sequence
    Read Archive.
  format: http
  id: imodulondb.modulome_workflow
  name: Modulome Workflow
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imodulondb
  product_url: https://github.com/avsastry/modulome-workflow
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: sra
- category: Product
  description: Downloadable transcriptomic datasets and iModulon decompositions for
    15 organisms including E. coli, B. subtilis, S. aureus, M. tuberculosis, P. aeruginosa,
    P. putida, and others. Includes gene expression matrices, iModulon activity matrices,
    gene weights, and metadata for over 9500 expression profiles from 525 studies.
  format: mixed
  id: imodulondb.datasets
  name: iModulonDB Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imodulondb
  product_url: https://imodulondb.org/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: biocyc
  - relation_type: prov:wasDerivedFrom
    source: sra
  - relation_type: prov:wasInformedBy
    source: string
- category: GraphProduct
  description: RDF (Turtle) knowledge graph of the NIAID Data Ecosystem, harmonizing
    dataset and computational-tool metadata harvested from NIAID-funded and globally-relevant
    infectious and immune-mediated disease repositories. Served through the Proto-OKN
    FRINK federated SPARQL platform.
  format: ttl
  id: nde.graph
  name: NIAID Data Ecosystem KG (graph)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nde
  - relation_type: prov:hadPrimarySource
    source: immport
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  product_url: https://frink.apps.renci.org/nde
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: omicsdi
  - relation_type: prov:wasInfluencedBy
    source: hubmap
  - relation_type: prov:wasInfluencedBy
    source: massive
  - relation_type: prov:wasInfluencedBy
    source: pdb
  - relation_type: prov:wasInfluencedBy
    source: lincs
publications:
- authors:
  - Katz K
  - Shutov O
  - Lapoint R
  - Kimelman M
  - Brister JR
  - O'Sullivan C
  doi: 10.1093/nar/gkab1053
  id: https://www.ncbi.nlm.nih.gov/pubmed/34850094
  journal: Nucleic Acids Res
  preferred: true
  title: 'The Sequence Read Archive: a decade more of explosive growth'
  year: '2022'
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