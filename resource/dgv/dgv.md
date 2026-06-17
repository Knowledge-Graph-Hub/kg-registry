---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://dgv.tcag.ca/dgv/app/contact
  label: The Centre for Applied Genomics, The Hospital for Sick Children
creation_date: '2026-06-17T00:00:00Z'
description: The Database of Genomic Variants (DGV) provides a curated catalogue of
  structural variation in the genomes of control individuals from healthy populations.
  It compiles copy-number variants, insertions, deletions, inversions, and other
  structural variants reported in the literature to provide a reference for studies
  of genomic disorders.
domains:
- genomics
- clinical
homepage_url: http://dgv.tcag.ca/dgv/app/home
id: dgv
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: Database of Genomic Variants
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching curated structural variants
    in the human genome.
  format: http
  id: dgv.site
  is_public: true
  name: DGV Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dgv
  product_url: http://dgv.tcag.ca/dgv/app/home
- category: Product
  description: Downloads of curated structural variant datasets by genome assembly.
  format: mixed
  id: dgv.downloads
  name: DGV Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dgv
  product_url: http://dgv.tcag.ca/dgv/app/downloads
publications:
- authors:
  - Jeffrey R. MacDonald
  - Robert Ziman
  - Ryan K. C. Yuen
  - Lars Feuk
  - Stephen W. Scherer
  doi: 10.1093/nar/gkt958
  id: https://doi.org/10.1093/nar/gkt958
  journal: Nucleic Acids Research
  preferred: true
  title: 'The Database of Genomic Variants: a curated collection of structural variation in the human genome'
  year: '2014'
---
# Database of Genomic Variants

The Database of Genomic Variants (DGV) is a curated collection of structural variation
identified in the genomes of control individuals from healthy populations. Maintained by
The Centre for Applied Genomics at The Hospital for Sick Children (Toronto), DGV serves
as a reference for the interpretation of structural variants in clinical and research
settings.

Content includes:

- Copy-number variants (CNVs), insertions, deletions, inversions and other structural
  variants curated from peer-reviewed studies
- Mapping of variants to multiple human genome assemblies
- Downloadable variant datasets for bulk analysis

GeneCards integrates structural variation data from DGV.
