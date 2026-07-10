---
activity_status: active
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: HOCOMOCO (HOmo sapiens COmprehensive MOdel COllection) is a curated database
  of transcription factor (TF) binding models, primarily position weight matrices
  (PWMs), for human and mouse. The models are derived from large-scale ChIP-Seq and
  HT-SELEX experiments and are manually curated, benchmarked, and annotated with quality
  ratings and recommended score thresholds. HOCOMOCO covers over a thousand human
  and mouse TFs, including secondary motif subtypes, and is a widely used upstream
  source for downstream regulatory resources such as DoRothEA.
domains:
- genomics
- systems biology
- proteomics
homepage_url: https://hocomoco.autosome.org
id: hocomoco
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: http://www.wtfpl.net/
  label: WTFPL
name: HOCOMOCO
products:
- category: Product
  description: HOCOMOCO v11 core collection human mononucleotide PWMs (flat text)
  format: txt
  id: hocomoco.core-pwms
  name: HOCOMOCO v11 Core Human Mononucleotide PWMs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  product_url: https://hocomoco11.autosome.org/final_bundle/hocomoco11/core/HUMAN/mono/HOCOMOCOv11_core_pwms_HUMAN_mono.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-03: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-07-10: No Content-Length
    header found'
- category: Product
  description: HOCOMOCO v11 full collection human mononucleotide PWMs (flat text),
    including secondary motif subtypes
  format: txt
  id: hocomoco.full-pwms
  name: HOCOMOCO v11 Full Human Mononucleotide PWMs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  product_url: https://hocomoco11.autosome.org/final_bundle/hocomoco11/full/HUMAN/mono/HOCOMOCOv11_full_pwms_HUMAN_mono.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-03: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-07-10: No Content-Length
    header found'
- category: Product
  description: HOCOMOCO download portal with PWM/PCM models for human and mouse in
    multiple formats (JASPAR, MEME, TRANSFAC, HOMER) plus annotations and thresholds
  format: http
  id: hocomoco.downloads
  name: HOCOMOCO Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  product_url: https://hocomoco14.autosome.org/downloads_v11
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
  - Ivan V. Kulakovskiy
  - Ilya E. Vorontsov
  - Ivan S. Yevshin
  - Ruslan N. Sharipov
  - Alla D. Fedorova
  - Eugene I. Rumynskiy
  - Yulia A. Medvedeva
  - Arturo Magana-Mora
  - Vladimir B. Bajic
  - Dmitry A. Papatsenko
  - Fedor A. Kolpakov
  - Vsevolod J. Makeev
  doi: 10.1093/nar/gkx1106
  id: https://www.ncbi.nlm.nih.gov/pubmed/29140464
  journal: Nucleic Acids Res
  preferred: true
  title: 'HOCOMOCO: towards a complete collection of transcription factor binding
    models for human and mouse via large-scale ChIP-Seq analysis'
  year: '2018'
---
# HOCOMOCO

## Overview

HOCOMOCO (HOmo sapiens COmprehensive MOdel COllection) is a manually curated collection of transcription factor (TF) binding models for human and mouse. The models are represented primarily as position weight matrices (PWMs) and position count matrices (PCMs), built from integrated ChIP-Seq and HT-SELEX data and benchmarked for quality.

## Contents

- PWM/PCM binding models for human and mouse TFs, including secondary motif subtypes
- Mononucleotide and dinucleotide models
- Model quality ratings, recommended score thresholds, and threshold-to-P-value maps
- Annotations mapping models to gene identifiers, sequence alignments, and sequence LOGOs

## Access

- Web portal at hocomoco.autosome.org (redirects to the current release)
- Direct download bundles in multiple formats (native, JASPAR, MEME, TRANSFAC, HOMER)

## Usage

HOCOMOCO models are used for motif scanning, regulatory sequence analysis, and as an upstream source of TF binding evidence for downstream resources such as DoRothEA.

## License

HOCOMOCO is distributed under the WTFPL; the authors note it may alternatively be treated as CC-BY.