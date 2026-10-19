---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: hgnc@genenames.org
  - contact_type: url
    value: https://www.genenames.org/contact/feedback/
  label: HUGO Gene Nomenclature Committee
creation_date: '2026-10-19T00:00:00Z'
description: HCOP (HGNC Comparison of Orthology Predictions) is an HGNC tool and dataset
  that integrates orthology assertions between human genes and genes of 19 other species
  (chimp, macaque, mouse, rat, dog, cat, horse, cattle, pig, opossum, platypus, chicken,
  anole lizard, Xenopus, zebrafish, C. elegans, Drosophila, S. cerevisiae, and S.
  pombe) from eggNOG, Ensembl Compara, HGNC, HomoloGene, Inparanoid, NCBI Gene orthology,
  OMA, OrthoDB, OrthoMCL, PANTHER, PhylomeDB, PomBase, TreeFam, and ZFIN. Each predicted
  ortholog pair lists the supporting sources, so the number of concurring databases
  indicates reliability, and gene data come from the relevant nomenclature and model
  organism databases. Data are updated weekly.
domains:
- genomics
- molecular evolution
- organisms
- model organisms
homepage_url: https://www.genenames.org/tools/hcop/
id: hcop
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: HCOP
products:
- category: GraphicalInterface
  description: HCOP web search for orthologs of one or more genes (by symbol, name,
    Ensembl, NCBI Gene, or species database ID, with wildcards) between human and
    selected species, filterable by orthology source; supports direct-link URLs and
    tab-delimited export of results.
  format: http
  id: hcop.web
  name: HCOP Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hcop
  product_url: https://www.genenames.org/tools/hcop/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: eggnog
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: homologene
  - relation_type: prov:wasDerivedFrom
    source: inparanoid
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ncbigene.gene_orthologs
  - relation_type: prov:wasDerivedFrom
    source: oma
  - relation_type: prov:wasDerivedFrom
    source: orthodb
  - relation_type: prov:wasDerivedFrom
    source: orthomcl
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: phylomedb
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: treefam
  - relation_type: prov:wasDerivedFrom
    source: zfin
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: rgd
  - relation_type: prov:wasDerivedFrom
    source: sgd
  - relation_type: prov:wasDerivedFrom
    source: vgnc
  - relation_type: prov:wasDerivedFrom
    source: wormbase
  - relation_type: prov:wasDerivedFrom
    source: xenbase
- category: MappingProduct
  compression: gzip
  description: All human ortholog assertions from HCOP for every ortholog species in
    one tab-delimited file (7 columns) with the ortholog species taxon ID, human and
    ortholog NCBI Gene and Ensembl gene IDs, and the assertion IDs.
  format: tsv
  id: hcop.all-seven-column
  name: HCOP All Species Orthologs (7 column)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hcop
  product_file_size: 26393603
  product_url: https://storage.googleapis.com/public-download-files/hcop/human_all_hcop_seven_column.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: eggnog
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: homologene
  - relation_type: prov:wasDerivedFrom
    source: inparanoid
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ncbigene.gene_orthologs
  - relation_type: prov:wasDerivedFrom
    source: oma
  - relation_type: prov:wasDerivedFrom
    source: orthodb
  - relation_type: prov:wasDerivedFrom
    source: orthomcl
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: phylomedb
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: treefam
  - relation_type: prov:wasDerivedFrom
    source: zfin
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: rgd
  - relation_type: prov:wasDerivedFrom
    source: sgd
  - relation_type: prov:wasDerivedFrom
    source: vgnc
  - relation_type: prov:wasDerivedFrom
    source: wormbase
  - relation_type: prov:wasDerivedFrom
    source: xenbase
- category: MappingProduct
  compression: gzip
  description: All human ortholog assertions from HCOP for every ortholog species in
    one tab-delimited file (16 columns), adding HGNC and species database IDs, approved
    symbols and names, chromosomal locations, and the list of supporting orthology
    sources to the 7-column file.
  format: tsv
  id: hcop.all-sixteen-column
  name: HCOP All Species Orthologs (16 column)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hcop
  product_file_size: 41825073
  product_url: https://storage.googleapis.com/public-download-files/hcop/human_all_hcop_sixteen_column.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: eggnog
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: homologene
  - relation_type: prov:wasDerivedFrom
    source: inparanoid
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ncbigene.gene_orthologs
  - relation_type: prov:wasDerivedFrom
    source: oma
  - relation_type: prov:wasDerivedFrom
    source: orthodb
  - relation_type: prov:wasDerivedFrom
    source: orthomcl
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: phylomedb
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: treefam
  - relation_type: prov:wasDerivedFrom
    source: zfin
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: rgd
  - relation_type: prov:wasDerivedFrom
    source: sgd
  - relation_type: prov:wasDerivedFrom
    source: vgnc
  - relation_type: prov:wasDerivedFrom
    source: wormbase
  - relation_type: prov:wasDerivedFrom
    source: xenbase
- category: Product
  description: HCOP bulk downloads page with pre-computed per-species files of human
    orthologs for each of the 19 ortholog species, as gzipped tab-delimited files in
    6-column (raw assertions with Ensembl and NCBI Gene IDs) and 15-column (adding
    nomenclature, locations, and supporting sources) layouts, e.g. human_mouse_hcop_fifteen_column.txt.gz.
  format: http
  id: hcop.species-downloads
  name: HCOP Per-species Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hcop
  product_url: https://www.genenames.org/download/hcop/tsv/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: eggnog
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: homologene
  - relation_type: prov:wasDerivedFrom
    source: inparanoid
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ncbigene.gene_orthologs
  - relation_type: prov:wasDerivedFrom
    source: oma
  - relation_type: prov:wasDerivedFrom
    source: orthodb
  - relation_type: prov:wasDerivedFrom
    source: orthomcl
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: phylomedb
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: treefam
  - relation_type: prov:wasDerivedFrom
    source: zfin
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: rgd
  - relation_type: prov:wasDerivedFrom
    source: sgd
  - relation_type: prov:wasDerivedFrom
    source: vgnc
  - relation_type: prov:wasDerivedFrom
    source: wormbase
  - relation_type: prov:wasDerivedFrom
    source: xenbase
- category: DocumentationProduct
  description: HCOP help page describing search usage, result fields, the orthology
    sources and versions used, species covered, link templates, and bulk download
    file layouts.
  format: http
  id: hcop.docs
  name: HCOP Help
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hcop
  product_url: https://www.genenames.org/help/hcop/
publications:
- authors:
  - Yates B
  - Gray KA
  - Jones TEM
  - Bruford EA
  doi: 10.1093/bib/bbab155
  id: PMID:33959747
  journal: Brief Bioinform
  preferred: true
  title: 'Updates to HCOP: the HGNC comparison of orthology predictions tool.'
  year: '2021'
- authors:
  - Eyre TA
  - Wright MW
  - Lush MJ
  - Bruford EA
  doi: 10.1093/bib/bbl030
  id: PMID:16951416
  journal: Brief Bioinform
  title: 'HCOP: a searchable database of human orthology predictions.'
  year: '2007'
- authors:
  - Wright MW
  - Eyre TA
  - Lush MJ
  - Povey S
  - Bruford EA
  doi: 10.1007/s00335-005-0103-2
  id: PMID:16284797
  journal: Mamm Genome
  title: 'HCOP: the HGNC comparison of orthology predictions search tool.'
  year: '2005'
synonyms:
- HGNC Comparison of Orthology Predictions
taxon:
- NCBITaxon:9606
- NCBITaxon:9598
- NCBITaxon:9544
- NCBITaxon:10090
- NCBITaxon:10116
- NCBITaxon:9615
- NCBITaxon:9685
- NCBITaxon:9796
- NCBITaxon:9913
- NCBITaxon:9823
- NCBITaxon:13616
- NCBITaxon:9258
- NCBITaxon:9031
- NCBITaxon:28377
- NCBITaxon:8364
- NCBITaxon:7955
- NCBITaxon:6239
- NCBITaxon:7227
- NCBITaxon:4932
- NCBITaxon:284812
---
# HCOP

## Overview

HCOP (HGNC Comparison of Orthology Predictions) is a tool from the HUGO Gene Nomenclature Committee (HGNC) that combines orthology predictions from many databases into one view. It was first built for human and mouse and now covers human plus 19 other species. For each predicted ortholog pair, HCOP lists the databases that support it, so the number of agreeing sources gives a measure of confidence.

## Data Content

Orthology assertions are imported from eggNOG, Ensembl Compara, HGNC, HomoloGene, Inparanoid, NCBI Gene orthology, OMA, OrthoDB, OrthoMCL, PANTHER, PhylomeDB (phylome 514), PomBase, TreeFam, and ZFIN. Not every source covers every species; the HCOP help page lists versions and species coverage for each source.

Gene symbols, names, locus types, and locations come from Ensembl, HGNC, MGI, NCBI Gene, PomBase, RGD, SGD, VGNC, WormBase, Xenbase, and ZFIN. For species without a nomenclature committee (chimp, macaque, dog, horse, cattle, pig, opossum, platypus) or without usable gene data (anole lizard), gene data are taken from NCBI Gene, or from Ensembl when no NCBI Gene ID can be mapped. A weekly pipeline checks each source for new data and updates HCOP.

## Access

- Web search at [genenames.org/tools/hcop](https://www.genenames.org/tools/hcop/), with linkable result URLs.
- Bulk downloads are gzipped tab-delimited files in the HGNC public Google Cloud Storage bucket (`https://storage.googleapis.com/public-download-files/hcop/`): per-species files (human vs. one species, 6 or 15 columns) and all-species files (7 or 16 columns).

## License

HGNC data, including HCOP, are released under the Creative Commons CC0 public domain dedication. Attribution is requested but not required.
