---
activity_status: inactive
category: DataSource
creation_date: '2025-07-12T00:00:00Z'
description: PsyGeNET is a knowledge resource on psychiatric disorders and their associated
  genes, integrating expert-curated and text-mined data from the literature. It provides
  gene-disease associations for psychiatric disorders, supporting research in psychiatric
  genetics and genomics.
domains:
- biomedical
- genomics
homepage_url: https://www.psygenet.org/
id: psygenet
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
name: PsyGeNET
products:
- category: Product
  description: Gene-disease associations for psychiatric disorders; the PsyGeNET 2.0
    homepage reports 3,771 associations between 1,549 genes and 117 psychiatric disease
    concepts.
  format: tsv
  id: psygenet.genedisease
  name: PsyGeNET Gene-Disease Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: psygenet
  product_url: https://www.psygenet.org/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: disgenet
- category: ProcessProduct
  description: R/Bioconductor package for querying PsyGeNET and performing comorbidity
    studies with PsyGeNET data
  format: http
  id: psygenet.psygenet2r
  license:
    id: https://spdx.org/licenses/MIT.html
    label: MIT
  name: psygenet2r R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: psygenet
  product_url: https://bioconductor.org/packages/release/bioc/manuals/psygenet2r/man/psygenet2r.pdf
  repository: https://git.bioconductor.org/packages/psygenet2r
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-22: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-24: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  format: http
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: mgd
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: phewascat
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: finngen
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://www.disgenet.com/
publications:
- authors:
  - Alba Gutiérrez-Sacristán
  - Solène Grosdidier
  - Olga Valverde
  - Marta Torrens
  - Àlex Bravo
  - Janet Piñero
  - Ferran Sanz
  - Laura I. Furlong
  doi: 10.1093/bioinformatics/btv301
  id: doi:10.1093/bioinformatics/btv301
  journal: Bioinformatics
  preferred: true
  title: 'PsyGeNET: a knowledge platform on psychiatric disorders and their genes'
  year: '2015'
- authors:
  - Alba Gutierrez-Sacristan
  - Carles Hernandez-Ferrer
  - Juan R Gonzalez
  - Laura I Furlong
  doi: 10.1093/bioinformatics/btx506
  id: doi:10.1093/bioinformatics/btx506
  journal: Bioinformatics
  title: 'psygenet2r: a R/Bioconductor package for the analysis of psychiatric disease
    genes'
  year: '2017'
taxon:
- NCBITaxon:9606
version: '2.0'
warnings:
- The PsyGeNET homepage responded on 2026-06-02 but identifies itself as an incomplete
  Wayback Machine Downloader copy, so direct website functionality may be unavailable.
- Several PsyGeNET subpages checked on 2026-06-02 either returned 404 or redirected
  to unrelated content; use the site and downloads with caution.
---
# PsyGeNET

PsyGeNET is a psychiatric-disorder gene association resource combining literature text mining and expert curation. Its original web application is no longer reliably available, but the resource remains documented through its publications and the psygenet2r Bioconductor package.