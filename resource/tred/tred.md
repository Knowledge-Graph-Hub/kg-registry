---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: "TRED (Transcriptional Regulatory Element Database) was a curated database of cis-regulatory elements, with an emphasis on transcription factor (TF) binding sites, TF-promoter regulatory interactions, and promoter annotations for human, mouse, and rat genes. It combined computational promoter prediction with literature-based manual curation of regulatory interactions, and was originally developed and hosted at Cold Spring Harbor Laboratory. TRED served as an upstream primary source for downstream regulatory network resources such as DoRothEA. The resource is now legacy and effectively superseded; its original hosting sites are no longer serving content, and it was dropped from some downstream tools due to licensing constraints."
domains:
- genomics
- systems biology
- biological systems
homepage_url: https://rulai.cshl.edu/TRED/
id: tred
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: "Transcriptional Regulatory Element Database"
products:
- category: DocumentationProduct
  description: "Reference publication describing TRED's curated transcription factor binding sites, TF-promoter regulatory interactions, and promoter annotations. The original web database is no longer available, so the publication serves as the primary documentation of record."
  format: http
  id: tred.docs
  name: TRED Publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tred
  product_url: https://doi.org/10.1093/nar/gkl1041
publications:
- authors:
  - C. Jiang
  - Z. Xuan
  - F. Zhao
  - M. Q. Zhang
  doi: 10.1093/nar/gkl1041
  id: https://pubmed.ncbi.nlm.nih.gov/17202159/
  journal: Nucleic Acids Res
  preferred: true
  title: "TRED: a transcriptional regulatory element database, new entries and other development"
  year: '2007'
---
# Transcriptional Regulatory Element Database (TRED)

## Overview

TRED was a curated database of transcriptional regulatory elements focused on transcription factor (TF) binding sites, TF-promoter regulatory interactions, and promoter annotations for human, mouse, and rat. It paired computational promoter prediction with literature-based manual curation, and was originally developed at Cold Spring Harbor Laboratory.

## Status

TRED is legacy and effectively superseded. Its historical hosting URLs (rulai.cshl.edu/TRED and a cb.utdallas.edu/TRED mirror) no longer serve the database, and the resource was removed from some downstream tools owing to licensing constraints. It is recorded here primarily for provenance, as an upstream primary source for resources such as DoRothEA.

## Citation

Jiang C, Xuan Z, Zhao F, Zhang MQ. TRED: a transcriptional regulatory element database, new entries and other development. Nucleic Acids Res. 2007;35(Database issue):D137-D140. doi:10.1093/nar/gkl1041
