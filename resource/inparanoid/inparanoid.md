---
activity_status: active
category: DataSource
creation_date: '2026-10-19T00:00:00Z'
description: Stub Resource page for inparanoid. This page was automatically generated
  because it was referenced by other resources.
domains:
- stub
id: inparanoid
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
name: Inparanoid
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
  description: All human ortholog assertions from HCOP for every ortholog species
    in one tab-delimited file (7 columns) with the ortholog species taxon ID, human
    and ortholog NCBI Gene and Ensembl gene IDs, and the assertion IDs.
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
  description: All human ortholog assertions from HCOP for every ortholog species
    in one tab-delimited file (16 columns), adding HGNC and species database IDs,
    approved symbols and names, chromosomal locations, and the list of supporting
    orthology sources to the 7-column file.
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
    orthologs for each of the 19 ortholog species, as gzipped tab-delimited files
    in 6-column (raw assertions with Ensembl and NCBI Gene IDs) and 15-column (adding
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
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Inparanoid

This is an automatically generated stub page for inparanoid. Please update with proper information.