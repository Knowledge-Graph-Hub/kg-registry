---
activity_status: inactive
category: DataSource
creation_date: '2025-07-12T00:00:00Z'
description: PsyGeNET is a knowledge resource on psychiatric disorders and their associated genes, integrating expert-curated and text-mined data from the literature. It provides gene-disease associations for psychiatric disorders, supporting research in psychiatric genetics and genomics.
domains:
  - biomedical
  - genomics
homepage_url: http://www.psygenet.org/
id: psygenet
last_modified_date: '2025-07-12T00:00:00Z'
layout: resource_detail
name: PsyGeNET
products:
  - category: Product
    description: 'Gene-disease associations for psychiatric disorders, as described in "PsyGeNET: a knowledge platform on psychiatric disorders and their genes" (PMCID: PMC4565028). '
    format: tsv
    id: psygenet.genedisease
    name: PsyGeNET Gene-Disease Associations
    product_url: http://www.psygenet.org/
  - category: GraphProduct
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: disgenet.data
    name: DisGeNET Data
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: mgd
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: orphanet
        relation_type: prov:hadPrimarySource
      - source: psygenet
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: phewascat
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: finngen
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
    product_url: https://www.disgenet.com/
    secondary_source:
      - source: disgenet
        relation_type: prov:wasInfluencedBy
publications:
  - authors:
      - "Bravo À"
      - Pinero J
      - Queralt-Rosinach N
      - Rautschka M
      - Furlong LI
    id: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4565028/
    journal: Database (Oxford)
    preferred: true
    title: 'PsyGeNET: a knowledge platform on psychiatric disorders and their genes'
    year: '2015'
warnings:
  - The official PsyGeNET website (http://www.psygenet.org/) is currently inaccessible. Data may be unavailable or out of date.
taxon:
  - NCBITaxon:9606
---

# PsyGeNET
