---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://orthomcl.org/
  label: VEuPathDB
creation_date: '2026-10-19T00:00:00Z'
description: OrthoMCL is a genome-scale algorithm and database for grouping orthologous
  protein sequences across eukaryotic and prokaryotic proteomes. It computes all-against-all
  reciprocal best BLAST hits, normalizes the similarity scores, and clusters the resulting
  protein-pair graph with the Markov Cluster (MCL) algorithm to build ortholog groups.
  OrthoMCL DB is maintained by VEuPathDB; its OrthoMCL 7 content covers millions of
  proteins from hundreds of complete proteomes spanning the tree of life, clustered
  into hundreds of thousands of ortholog groups.
domains:
- molecular evolution
- genomics
homepage_url: https://orthomcl.org/
id: orthomcl
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: OrthoMCL DB
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
- category: GraphicalInterface
  description: Interactive VEuPathDB search and browse interface for OrthoMCL ortholog
    groups, proteins, and phyletic patterns.
  format: http
  id: orthomcl.portal
  name: OrthoMCL DB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthomcl
  product_url: https://orthomcl.org/orthomcl/
- category: Product
  description: Open directory index of bulk data files for the current OrthoMCL release.
  format: http
  id: orthomcl.downloads
  name: OrthoMCL DB Current Release Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthomcl
  product_url: https://orthomcl.org/common/downloads/Current_Release/
- category: Product
  compression: gzip
  description: Flat file listing each ortholog group and its member protein identifiers.
  format: txt
  id: orthomcl.groups
  name: OrthoMCL Ortholog Groups File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthomcl
  product_file_size: 51943340
  product_url: https://orthomcl.org/common/downloads/Current_Release/groups_OrthoMCL-8.2.txt.gz
- category: Product
  compression: gzip
  description: Amino-acid sequences for all proteins in the current OrthoMCL release.
  format: fasta
  id: orthomcl.protein-sequences
  name: OrthoMCL Protein Sequences (FASTA)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthomcl
  product_file_size: 2773509993
  product_url: https://orthomcl.org/common/downloads/Current_Release/aa_seqs_OrthoMCL-8.2.fasta.gz
publications:
- authors:
  - Feng Chen
  - Aaron J. Mackey
  - Christian J. Stoeckert Jr.
  - David S. Roos
  doi: 10.1093/nar/gkj123
  id: doi:10.1093/nar/gkj123
  journal: Nucleic Acids Research
  preferred: true
  title: 'OrthoMCL-DB: querying a comprehensive multi-species collection of ortholog
    groups'
  year: '2006'
- authors:
  - Li Li
  - Christian J. Stoeckert Jr.
  - David S. Roos
  doi: 10.1101/gr.1224503
  id: doi:10.1101/gr.1224503
  journal: Genome Research
  title: 'OrthoMCL: identification of ortholog groups for eukaryotic genomes'
  year: '2003'
rrid: SCR_007839
---
# OrthoMCL DB

## Overview

OrthoMCL groups orthologous protein sequences across eukaryotic and prokaryotic proteomes. It builds a graph of normalized reciprocal best BLAST hits and clusters it with the Markov Cluster (MCL) algorithm to form ortholog groups. OrthoMCL DB is now hosted by VEuPathDB.

## Access

- Web portal: search and browse ortholog groups, proteins, and phyletic patterns.
- Downloads: current-release ortholog group flat files and protein FASTA sequences.

## Citation

Please cite: Chen F, Mackey AJ, Stoeckert CJ Jr, Roos DS. OrthoMCL-DB: querying a comprehensive multi-species collection of ortholog groups. Nucleic Acids Res. 2006;34(Database issue):D363–D368. doi:10.1093/nar/gkj123