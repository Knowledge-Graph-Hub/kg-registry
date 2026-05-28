---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-05-21T00:00:00Z'
description: ARCHS4 is a Ma'ayan Lab resource for uniformly processed public RNA-seq
  data that provides gene and transcript count matrices, metadata search, and interactive
  exploration for large collections of human and mouse samples aggregated from GEO
  and SRA.
domains:
- biomedical
- genomics
homepage_url: https://archs4.org/
id: archs4
last_modified_date: '2026-05-21T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: ARCHS4
products:
- category: GraphicalInterface
  description: Web portal for metadata search, expression lookup, signature search,
    and interactive exploration of ARCHS4 sample and gene spaces
  format: http
  id: archs4.portal
  name: ARCHS4 Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: archs4
  product_url: https://archs4.org/
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
- category: GraphProduct
  description: Neo4j knowledge graph integrating transcription factor target libraries,
    coexpression networks, and benchmark datasets used by the ChEA3 resource
  dump_format: neo4j
  format: neo4j
  id: chea-kg.graph
  name: ChEA-KG Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries, benchmark
    datasets, and additional supporting libraries
  format: http
  id: chea-kg.libraries
  name: ChEA-KG Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries and
    benchmark datasets
  format: http
  id: chea.libraries
  name: ChEA Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
publications:
- authors:
  - Lachmann A
  - Torre D
  - Keenan AB
  - Jagodnik KM
  - Lee HJ
  - Wang L
  - Silverstein MC
  - Ma'ayan A
  id: doi:10.1038/s41467-018-03751-6
  journal: Nature Communications
  preferred: true
  title: Massive mining of publicly available RNA-seq data from human and mouse
  year: '2018'
repository: https://github.com/MaayanLab/archs4
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# ARCHS4

ARCHS4 is a large-scale expression resource that uniformly processes public RNA-seq experiments and exposes the resulting data through interactive web search, visualization, and bulk download interfaces. The current canonical homepage is [archs4.org](https://archs4.org/), while the original Ma'ayan Lab deployment remains available as a legacy site.

The public documentation states that ARCHS4 aggregates human and mouse RNA-seq experiments from GEO and SRA, aligns reads with kallisto in a cloud-based processing pipeline, and uses Ensembl annotations for gene and transcript quantification. The current site also notes an ARCHS4 Zoo section for additional species and links to companion client packages such as ARCHS4py and archs4r.

## Original Sources

- Gene Expression Omnibus (GEO)
- Sequence Read Archive (SRA)
- Ensembl reference annotations

## Access

- Main portal: [ARCHS4](https://archs4.org/)
- Human gene counts: [human_gene_v2.latest.h5](https://s3.dev.maayanlab.cloud/archs4/files/human_gene_v2.latest.h5)
- Mouse gene counts: [mouse_gene_v2.latest.h5](https://s3.dev.maayanlab.cloud/archs4/files/mouse_gene_v2.latest.h5)
- Human transcript counts: [human_transcript_v2.latest.h5](https://s3.dev.maayanlab.cloud/archs4/files/human_transcript_v2.latest.h5)
- Mouse transcript counts: [mouse_transcript_v2.latest.h5](https://s3.dev.maayanlab.cloud/archs4/files/mouse_transcript_v2.latest.h5)
- Additional-species downloads: [ARCHS4 Zoo](https://archs4.org/zoo)

## Automated Evaluation

- View the automated evaluation: [archs4 automated evaluation](archs4_eval_automated.html)