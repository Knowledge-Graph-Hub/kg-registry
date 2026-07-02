---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://hpap.pmacs.upenn.edu/
  label: Human Pancreas Analysis Program (HPAP)
creation_date: '2026-07-01T00:00:00Z'
description: The Human Pancreas Analysis Program (HPAP) is a program of the NIH/NIDDK
  Human Islet Research Network (HIRN) that generates deeply phenotyped, multi-omic
  datasets from human pancreata and isolated islets of organ donors across the spectrum
  of type 1 and type 2 diabetes. HPAP data, including single-cell RNA-seq and single-nucleus
  ATAC-seq of pancreatic islets, are distributed through the PANC-DB data portal.
domains:
- biomedical
- genomics
- immunology
- clinical
homepage_url: https://hpap.pmacs.upenn.edu/
id: hpap
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: Human Pancreas Analysis Program (HPAP)
products:
- category: DataSource
  description: PANC-DB data portal for browsing and downloading HPAP donor-derived
    pancreas and islet multi-omic datasets.
  format: http
  id: hpap.pancdb
  name: HPAP PANC-DB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hpap
  product_url: https://hpap.pmacs.upenn.edu/
- category: GraphProduct
  description: Pancreas-focused knowledge graph integrating genes, SNPs, pancreatic
    expression QTLs, and donor-derived islet datasets harmonized within PanKbase.
  format: http
  id: pankgraph.graph
  name: PanKgraph Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankgraph
  - relation_type: prov:wasDerivedFrom
    source: pankbase
  - relation_type: prov:hadPrimarySource
    source: hpap
  - relation_type: prov:hadPrimarySource
    source: iidp
  - relation_type: prov:hadPrimarySource
    source: prodo
  product_url: https://pankgraph.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
taxon:
- NCBITaxon:9606
---
Human Pancreas Analysis Program (HPAP)

## Description

The Human Pancreas Analysis Program (HPAP) is a component of the NIH/NIDDK Human Islet Research Network (HIRN). It produces standardized, deeply phenotyped multi-omic data from human organ donor pancreata and isolated islets spanning non-diabetic, type 1 diabetes, and type 2 diabetes states, distributed through the PANC-DB portal. HPAP is one of the primary upstream data sources integrated by PanKbase.