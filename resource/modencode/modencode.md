---
activity_status: orphaned
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://data.modencode.org/
  label: modENCODE Consortium
creation_date: '2026-10-19T00:00:00Z'
description: modENCODE (model organism ENCyclopedia Of DNA Elements) was an NHGRI-funded
  consortium, begun in 2007, created to systematically identify and annotate the functional
  genomic elements (genes, transcripts, and regulatory, chromatin, and replication
  elements) in the genomes of Drosophila melanogaster and Caenorhabditis elegans using
  high-throughput approaches including ChIP-seq and RNA-seq. The consortium generated
  hundreds of genome-wide datasets and concluded around 2012. Its original web portals
  were retired in 2023 after funding ended, and its data are now distributed through
  FlyBase, WormBase, and the ENCODE Data Coordination Center.
domains:
- genomics
- gene regulation
- model organisms
- organisms
homepage_url: http://data.modencode.org/
id: modencode
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: modENCODE
products:
- category: Product
  description: GTRD bulk download directory with plain-text results of uniform annotation
    and analysis, including experiment metadata, peak and meta-cluster intervals for
    ChIP-seq, ChIP-exo, DNase-seq, and MNase-seq, bigBed files, target gene lists,
    and genome browser track hubs. Raw data were obtained from GEO, SRA, ENCODE, and
    modENCODE.
  format: http
  id: gtrd.downloads
  name: GTRD Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:wasDerivedFrom
    source: gene-expression-omnibus
  - relation_type: prov:wasDerivedFrom
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: modencode
  product_url: https://gtrd.biouml.org/downloads/current/
- category: Product
  description: Per-species archives of transcription factor ChIP-seq peaks called
    with GEM, MACS2, PICS, and SISSRs on uniformly reprocessed ChIP-seq data from
    GEO, SRA, ENCODE, and modENCODE.
  format: http
  id: gtrd.chip-seq_peaks
  name: GTRD ChIP-seq Peaks
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:wasDerivedFrom
    source: gene-expression-omnibus
  - relation_type: prov:wasDerivedFrom
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: modencode
  product_url: http://gtrd.biouml.org:8888/downloads/current/intervals/chip-seq/
- category: GraphicalInterface
  description: Static landing page for the retired modENCODE project, linking to the
    successor data repositories (FlyBase, WormBase, and the ENCODE Portal) that now
    host the project's data.
  format: http
  id: modencode.portal
  name: modENCODE Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: modencode
  product_url: http://data.modencode.org/
- category: Product
  description: Tar archive of supplementary files from the Drosophila modENCODE 2010
    Science paper (PMID 21177974).
  format: txt
  compression: tar
  id: modencode.fly-suppl-2010
  name: modENCODE Drosophila 2010 Supplemental Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: modencode
  product_url: https://s3.us-west-2.amazonaws.com/data.modencode.org/modencode_Science-2010_fly_suppl_PMID21177974.tar
- category: GraphicalInterface
  description: ENCODE Data Coordination Center experiment matrix hosting released
    modENCODE (and modERN) datasets for Drosophila melanogaster and Caenorhabditis
    elegans.
  format: http
  id: modencode.encode-portal
  name: modENCODE Data at the ENCODE Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: modencode
  product_url: https://www.encodeproject.org/search/?type=Experiment&internal_tags=ENCORTEX
publications:
- authors:
  - Sushmita Roy
  - Jason Ernst
  - Peter V. Kharchenko
  - Pouya Kheradpour
  - modENCODE Consortium
  doi: 10.1126/science.1198374
  id: doi:10.1126/science.1198374
  journal: Science
  preferred: true
  title: Identification of functional elements and regulatory circuits by Drosophila
    modENCODE
  year: '2010'
- authors:
  - Mark B. Gerstein
  - Zhi John Lu
  - Eric L. Van Nostrand
  - Chao Cheng
  - Bradley I. Arshinoff
  doi: 10.1126/science.1196914
  id: doi:10.1126/science.1196914
  journal: Science
  title: Integrative analysis of the Caenorhabditis elegans genome by the modENCODE
    project
  year: '2010'
rrid: SCR_006206
taxon:
- NCBITaxon:7227
- NCBITaxon:6239
---
# modENCODE

## Overview

The modENCODE (model organism ENCyclopedia Of DNA Elements) project was an NHGRI-funded consortium that systematically annotated the functional elements of the Drosophila melanogaster and Caenorhabditis elegans genomes. Using high-throughput assays — ChIP-seq, RNA-seq, and others — its eleven primary projects produced hundreds of genome-wide datasets and greatly expanded the annotated portion of the fly genome.

## Access

- Data portal: a static landing page (data.modencode.org) pointing to the successor repositories.
- FlyBase hosts the Drosophila datasets; WormBase hosts the C. elegans datasets.
- The ENCODE Portal (encodeproject.org) hosts released modENCODE and modERN data.

The original modENCODE and modMine (InterMine) portals were retired in 2023 after funding ended, so this resource is recorded with an activity status of orphaned.

## Citation

Please cite the companion 2010 Science papers:

- modENCODE Consortium, Roy S, Ernst J, et al. Identification of functional elements and regulatory circuits by Drosophila modENCODE. Science. 2010;330(6012):1787–1797. doi:10.1126/science.1198374
- Gerstein MB, Lu ZJ, Van Nostrand EL, et al. Integrative analysis of the Caenorhabditis elegans genome by the modENCODE project. Science. 2010;330(6012):1775–1787. doi:10.1126/science.1196914
