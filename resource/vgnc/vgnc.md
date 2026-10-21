---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://vertebrate.genenames.org/about/
  label: HUGO Gene Nomenclature Committee (HGNC)
creation_date: '2026-10-19T00:00:00Z'
description: The Vertebrate Gene Nomenclature Committee (VGNC) assigns standardized, HGNC-style
  approved gene symbols and names to genes in selected vertebrate species that lack a dedicated
  nomenclature committee, naming genes in line with their human homologs. A sister project
  of the HGNC, it began with chimpanzee and has expanded to species including rhesus macaque,
  dog, cat, horse, cattle, and pig. VGNC shares infrastructure with genenames.org and coordinates
  with the existing mouse, rat, chicken, Xenopus, and zebrafish nomenclature committees.
domains:
- genomics
- model organisms
- organisms
homepage_url: https://vertebrate.genenames.org/
id: vgnc
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: Creative Commons Public Domain Dedication (CC0 1.0)
name: Vertebrate Gene Nomenclature Committee (VGNC)
products:
- category: GraphicalInterface
  description: HCOP web search for orthologs of one or more genes (by symbol, name, Ensembl,
    NCBI Gene, or species database ID, with wildcards) between human and selected species,
    filterable by orthology source; supports direct-link URLs and tab-delimited export of
    results.
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
  description: All human ortholog assertions from HCOP for every ortholog species in one tab-delimited
    file (7 columns) with the ortholog species taxon ID, human and ortholog NCBI Gene and
    Ensembl gene IDs, and the assertion IDs.
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
  description: All human ortholog assertions from HCOP for every ortholog species in one tab-delimited
    file (16 columns), adding HGNC and species database IDs, approved symbols and names, chromosomal
    locations, and the list of supporting orthology sources to the 7-column file.
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
  description: HCOP bulk downloads page with pre-computed per-species files of human orthologs
    for each of the 19 ortholog species, as gzipped tab-delimited files in 6-column (raw assertions
    with Ensembl and NCBI Gene IDs) and 15-column (adding nomenclature, locations, and supporting
    sources) layouts, e.g. human_mouse_hcop_fifteen_column.txt.gz.
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
- category: GraphicalInterface
  description: Web tool to search and browse VGNC-approved vertebrate gene symbols, names,
    and records.
  format: http
  id: vgnc.search
  name: VGNC Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vgnc
  product_url: https://vertebrate.genenames.org/tools/search/
- category: Product
  description: Directory of downloadable, tab-delimited VGNC gene symbol report files and
    per-species nomenclature statistics.
  format: tsv
  id: vgnc.downloads
  name: VGNC Statistics and Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vgnc
  product_url: https://vertebrate.genenames.org/download/statistics-and-files/
- category: ProgrammingInterface
  description: Shared genenames.org REST service for programmatic retrieval of HGNC and VGNC
    gene nomenclature records.
  format: http
  id: vgnc.rest-api
  is_public: true
  name: genenames.org REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vgnc
  product_url: https://www.genenames.org/help/rest/
publications:
- authors:
  - Susan Tweedie
  - Bryony Braschi
  - Kristian Gray
  - Tamsin E. M. Jones
  - Ruth L. Seal
  - Elspeth A. Bruford
  doi: 10.1093/nar/gkaa980
  id: doi:10.1093/nar/gkaa980
  journal: Nucleic Acids Research
  preferred: true
  title: 'Genenames.org: the HGNC and VGNC resources in 2021'
  year: '2021'
rrid: SCR_017514
taxon:
- NCBITaxon:9598
- NCBITaxon:9544
- NCBITaxon:9615
- NCBITaxon:9685
- NCBITaxon:9796
- NCBITaxon:9913
- NCBITaxon:9823
---

# Vertebrate Gene Nomenclature Committee (VGNC)

## Overview

VGNC is HGNC's sister project, assigning standardized approved gene symbols and names to selected vertebrate species that have no nomenclature committee of their own, in line with their human homologs. It began with chimpanzee and has grown to include macaque, dog, cat, horse, cattle, pig, and others.

## Access

- Search: look up VGNC-approved vertebrate gene symbols and records.
- Statistics and downloads: tab-delimited gene symbol report files, updated regularly.
- REST API: programmatic access shared with genenames.org.

## Citation

Please cite: Tweedie S, Braschi B, Gray K, Jones TEM, Seal RL, Yates B, Bruford EA. Genenames.org: the HGNC and VGNC resources in 2021. Nucleic Acids Res. 2021;49(D1):D939–D946. doi:10.1093/nar/gkaa980
