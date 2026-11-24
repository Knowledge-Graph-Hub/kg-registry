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
description: GeneHancer is a database of human enhancers and their inferred target genes, within
  the GeneCards Suite. The 2017 publication describes 285,000 candidate enhancers integrated
  from ENCODE, the Ensembl regulatory build, FANTOM, and the VISTA Enhancer Browser, linked
  to genes by expression correlation, expression quantitative trait loci, capture Hi-C, and
  genomic distance.
domains:
- genomics
- gene regulation
homepage_url: https://www.genecards.org/
id: genehancer
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://www.lifemapsc.com/genecards-suite-terms-of-use/
  label: Free for non-profit academic/hospital use; commercial license required (proprietary,
    LifeMap Sciences)
name: GeneHancer
products:
- category: GraphicalInterface
  description: GeneHancer enhancers and gene associations, shown on GeneCards gene pages.
  format: http
  id: genehancer.portal
  name: GeneHancer in GeneCards
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genehancer
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: vista
  product_url: https://www.genecards.org/
  warnings:
  - genecards.org returns HTTP 403 to automated clients, so this URL was not confirmed by an
    automated check on 2026-11-24.
publications:
- authors:
  - Simon Fishilevich
  - Ron Nudel
  - Noa Rappaport
  - Rotem Hadar
  - Inbar Plaschkes
  - Tsippi Iny Stein
  - Naomi Rosen
  - Asher Kohn
  - Michal Twik
  - Marilyn Safran
  - Doron Lancet
  - Dana Cohen
  doi: 10.1093/database/bax028
  id: doi:10.1093/database/bax028
  journal: Database
  preferred: true
  title: 'GeneHancer: genome-wide integration of enhancers and target genes in GeneCards'
  year: '2017'
rrid: SCR_023953
taxon:
- NCBITaxon:9606
warnings:
- The GeneCards Suite terms of use prohibit automated scraping and prohibit use of the data
  for training AI models without written permission from LifeMap Sciences (read 2026-11-24).
---

# GeneHancer

GeneHancer is a member of the GeneCards Suite. It merges enhancers reported by four genome-wide
databases, scores each one, and links it to likely target genes.
