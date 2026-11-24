---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.lifemapsc.com/
  label: LifeMap Sciences
creation_date: '2026-11-24T00:00:00Z'
description: GeneCaRNA is a gene-centric database of human non-coding RNA genes in the GeneCards
  Suite. It integrates RNAcentral with the non-coding RNA entries of HGNC, Ensembl, and NCBI
  Gene. The 2021 publication describes 219,587 gene pages.
domains:
- genomics
- non-coding RNA
homepage_url: https://www.genecards.org/
id: genecarna
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://www.lifemapsc.com/genecards-suite-terms-of-use/
  label: Free for non-profit academic/hospital use; commercial license required (proprietary,
    LifeMap Sciences)
name: GeneCaRNA
products:
- category: GraphicalInterface
  description: Human non-coding RNA gene pages in the GeneCards web interface.
  format: http
  id: genecarna.portal
  name: GeneCaRNA in GeneCards
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecarna
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: genecards
  product_url: https://www.genecards.org/
  warnings:
  - genecards.org returns HTTP 403 to automated clients, so this URL was not confirmed by an
    automated check on 2026-11-24.
publications:
- authors:
  - Ruth Barshir
  - Simon Fishilevich
  - Tsippi Iny-Stein
  - Ofer Zelig
  - Yaron Mazor
  - Yaron Guan-Golan
  - Marilyn Safran
  - Doron Lancet
  doi: 10.1016/j.jmb.2021.166913
  id: doi:10.1016/j.jmb.2021.166913
  journal: Journal of Molecular Biology
  preferred: true
  title: 'GeneCaRNA: A Comprehensive Gene-centric Database of Human Non-coding RNAs in the GeneCards
    Suite'
  year: '2021'
taxon:
- NCBITaxon:9606
warnings:
- The GeneCards Suite terms of use prohibit automated scraping and prohibit use of the data
  for training AI models without written permission from LifeMap Sciences (read 2026-11-24).
---

# GeneCaRNA

GeneCaRNA is a member of the GeneCards Suite, for human non-coding RNA genes.
