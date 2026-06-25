---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: ORegAnno (the Open Regulatory Annotation database) is a community-driven,
  literature-curated resource of regulatory regions, transcription factor binding
  sites, regulatory polymorphisms, and regulatory interactions across multiple species.
  It served as an upstream primary source for regulatory annotation resources such
  as DoRothEA. The original standalone interactive site (oreganno.org) is no longer
  operational and now redirects to the UCSC Genome Browser; the curated ORegAnno 3.0
  data set lives on as a track and bulk download in the UCSC Genome Browser and is
  also distributed via Ensembl.
domains:
- genomics
- systems biology
homepage_url: https://genome.ucsc.edu/cgi-bin/hgTrackUi?org=Human&g=oreganno
id: oreganno
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: ORegAnno
products:
- category: DataProduct
  description: ORegAnno 3.0 regulatory annotation as a UCSC Genome Browser track and
    bulk download (human, hg38).
  format: gff
  id: oreganno.ucsc
  name: ORegAnno UCSC Track Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oreganno
  product_file_size: 20472081
  product_url: https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/oreganno.txt.gz
- category: GraphProduct
  description: Core TF–target regulon knowledge graph (multi-species) with confidence
    levels (A–E)
  id: dorothea.graph
  name: DoRothEA Regulon Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  product_url: https://github.com/saezlab/dorothea/releases/tag/v1.0.0
publications:
- authors:
  - Robert Lesurf
  - Kelsy C. Cotto
  - Grace Wang
  - Malachi Griffith
  - Katayoon Kasaian
  - Steven J. M. Jones
  - Stephen B. Montgomery
  - Obi L. Griffith
  doi: 10.1093/nar/gkv1203
  id: https://www.ncbi.nlm.nih.gov/pubmed/26578589
  journal: Nucleic Acids Res
  preferred: true
  title: 'ORegAnno 3.0: a community-driven resource for curated regulatory annotation'
  year: '2016'
---
# ORegAnno

## Overview

ORegAnno (the Open Regulatory Annotation database) is an open, community-curated
collection of regulatory annotation. It captures regulatory regions, transcription
factor binding sites, regulatory polymorphisms, and curated regulatory interactions,
each linked to supporting literature evidence and target genes across multiple species.

## Status

ORegAnno is largely a legacy resource. The original standalone site at oreganno.org
is no longer operational as an interactive database and now redirects to the UCSC
Genome Browser. The curated ORegAnno 3.0 data persists through the UCSC Genome Browser
(ORegAnno track and bulk downloads) and Ensembl, which is how the data remains
accessible today.

## Contents

- Curated regulatory regions and transcription factor binding sites
- Regulatory polymorphisms and regulatory interactions
- Literature-backed evidence linking regulatory features to target genes
- Multi-species coverage

## Access

- UCSC Genome Browser ORegAnno track and `goldenPath` bulk downloads
- Ensembl regulatory annotation

## Relationship to other resources

ORegAnno served as an upstream primary source for downstream regulatory resources,
including DoRothEA.

## Citation

Lesurf R, Cotto KC, Wang G, et al. "ORegAnno 3.0: a community-driven resource for
curated regulatory annotation." Nucleic Acids Res. 2016. doi:10.1093/nar/gkv1203