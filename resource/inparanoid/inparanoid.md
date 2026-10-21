---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://inparanoidb.sbc.su.se/
  label: Sonnhammer group, Stockholm University (SciLifeLab / SBC)
creation_date: '2026-10-19T00:00:00Z'
description: InParanoid is an algorithm and database that detects orthologs and in-paralogs
  between two species by pairwise whole-proteome comparison, seeding ortholog clusters from
  reciprocal best sequence matches and then adding species-specific in-paralogs without multiple
  alignments or phylogenetic trees. The current release, InParanoiDB 9, uses the InParanoid-DIAMOND
  pipeline over 640 organisms (447 eukaryotic, 158 bacterial, and 35 archaeal proteomes) and
  provides ortholog groups for both full-length proteins and protein domains. It is developed
  by Erik Sonnhammer's group at Stockholm University (SciLifeLab / Stockholm Bioinformatics
  Centre).
domains:
- molecular evolution
- genomics
homepage_url: https://inparanoidb.sbc.su.se/
id: inparanoid
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: InParanoid
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
  description: Browse and search interface for ortholog groups and in-paralogs, for both full-length
    proteins and protein domains, across 640 organisms.
  format: http
  id: inparanoid.portal
  name: InParanoiDB 9 Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: inparanoid
  product_url: https://inparanoidb.sbc.su.se/
- category: Product
  description: Download area serving proteomes, species lists, and pairwise ortholog and domain
    files (as tab-delimited SQLtable text or OrthoXML), plus previous versions back to v2.0.
  format: http
  id: inparanoid.downloads
  name: InParanoiDB 9 Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: inparanoid
  product_url: https://inparanoidb.sbc.su.se/download
publications:
- authors:
  - Emma Persson
  - Erik L. L. Sonnhammer
  doi: 10.1016/j.jmb.2023.168001
  id: doi:10.1016/j.jmb.2023.168001
  journal: Journal of Molecular Biology
  preferred: true
  title: 'InParanoiDB 9: Ortholog Groups for Protein Domains and Full-Length Proteins'
  year: '2023'
- authors:
  - Maido Remm
  - Christian E. V. Storm
  - Erik L. L. Sonnhammer
  doi: 10.1006/jmbi.2000.5197
  id: doi:10.1006/jmbi.2000.5197
  journal: Journal of Molecular Biology
  title: Automatic clustering of orthologs and in-paralogs from pairwise species comparisons
  year: '2001'
rrid: SCR_006801
---

# InParanoid

## Overview

InParanoid detects orthologs and in-paralogs between two species from pairwise whole-proteome comparison, without multiple alignments or trees. The current web database, InParanoiDB 9, applies the InParanoid-DIAMOND pipeline over 640 organisms and offers ortholog groups for both full-length proteins and protein domains.

## Access

- Web portal: browse and search ortholog groups and in-paralogs.
- Bulk downloads: proteomes, pairwise ortholog and domain files (SQLtable text or OrthoXML), and previous versions.

Note: InParanoid version 8 (2013) remains available as a separate, frozen legacy site at inparanoid8.sbc.su.se and is the version used by HGNC's HCOP.

## Citation

Please cite: Persson E, Sonnhammer ELL. InParanoiDB 9: Ortholog Groups for Protein Domains and Full-Length Proteins. J Mol Biol. 2023;435(14):168001. doi:10.1016/j.jmb.2023.168001
