---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://phylomedb.org/
  label: Comparative Genomics group, Barcelona Supercomputing Center
creation_date: '2026-10-19T00:00:00Z'
description: PhylomeDB is a public database of phylomes, the complete collections of annotated
  gene phylogenies (homologous sequences, their alignments, and reconstructed trees) for a
  set of species. The current release, version 5, provides 534 phylomes comprising more than
  8 million trees and covers homology relationships for genes across more than 6,000 species.
  From these trees PhylomeDB derives genome-wide orthology and paralogy predictions. It is
  maintained by the Comparative Genomics group at the Barcelona Supercomputing Center.
domains:
- molecular evolution
- genomics
homepage_url: https://phylomedb.org/
id: phylomedb
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: Creative Commons Attribution-NonCommercial 4.0 International
name: PhylomeDB
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
  description: PhylomeDB 5 web interface for browsing phylomes, gene trees, alignments, and
    orthology and paralogy predictions.
  format: http
  id: phylomedb.portal
  name: PhylomeDB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phylomedb
  product_url: https://phylomedb.org/
- category: Product
  description: 'Download page linking to per-phylome bulk data: gene trees (Newick/NHX), multiple
    sequence alignments, and orthology and paralogy prediction files.'
  format: http
  id: phylomedb.downloads
  name: PhylomeDB Download Area
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phylomedb
  product_url: https://phylomedb.org/download
publications:
- authors:
  - Diego Fuentes
  - Marina Molina
  - Uciel Chorostecki
  - Salvador Capella-Gutiérrez
  - Marina Marcet-Houben
  - Toni Gabaldón
  doi: 10.1093/nar/gkab966
  id: doi:10.1093/nar/gkab966
  journal: Nucleic Acids Research
  preferred: true
  title: 'PhylomeDB V5: an expanding repository for genome-wide catalogues of annotated gene
    phylogenies'
  year: '2022'
rrid: SCR_007850
---

# PhylomeDB

## Overview

PhylomeDB is a repository of phylomes — genome-wide collections of annotated gene phylogenies — together with the orthology and paralogy predictions derived from their trees. Release 5 holds 534 phylomes and over 8 million trees spanning more than 6,000 species.

## Access

- Web portal: browse phylomes, gene trees, and alignments.
- Download area: per-phylome trees (Newick/NHX), alignments, and orthology/paralogy predictions.

## Citation

Please cite: Fuentes D, Molina M, Chorostecki U, Capella-Gutiérrez S, Marcet-Houben M, Gabaldón T. PhylomeDB V5: an expanding repository for genome-wide catalogues of annotated gene phylogenies. Nucleic Acids Res. 2022;50(D1):D1062–D1068. doi:10.1093/nar/gkab966
