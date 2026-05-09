---
activity_status: active
category: DataSource
creation_date: '2026-01-30T00:00:00Z'
description: A database of orthologous groups and functional annotations derived from comparative genomics, supporting cross-species gene function inference.
domains:
  - genomics
  - biological systems
homepage_url: https://eggnogdb.org/
id: eggnog
last_modified_date: '2026-02-15T00:00:00Z'
layout: resource_detail
name: eggNOG
products:
  - category: GraphicalInterface
    description: Main web interface for browsing orthologous groups and functional annotations.
    format: http
    id: eggnog.portal
    name: eggNOG Portal
    product_url: https://eggnogdb.org/
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Download interface for eggNOG annotation and orthology data releases.
    format: http
    id: eggnog.download
    name: eggNOG Downloads
    product_url: https://eggnogdb.org/downloads/
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: All protein sequences covered in eggNOG 7.
    format: fasta
    id: eggnog.download.e7.proteins
    name: eggNOG 7 Proteins
    product_file_size: 12753324465
    product_url: https://eggnogdb.org/public/eggnog7/e7.proteins.fa.gz
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Tar archive containing orthologous group FASTA sequence files.
    format: mixed
    id: eggnog.download.e7.og-fasta-sequences
    name: eggNOG 7 OG FASTA Sequences
    product_file_size: 28479795200
    product_url: https://eggnogdb.org/public/eggnog7/e7.og_fasta_sequences.tar
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: Orthologous group information table including KEGG and GO annotations.
    format: tsv
    id: eggnog.download.e7.og-info-kegg-go
    name: eggNOG 7 OG Info (KEGG/GO)
    product_file_size: 967458606
    product_url: https://eggnogdb.org/public/eggnog7/e7.og_info_kegg_go.tsv.gz
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: Protein family information table.
    format: tsv
    id: eggnog.download.e7.protein-families
    name: eggNOG 7 Protein Families
    product_file_size: 807966782
    product_url: https://eggnogdb.org/public/eggnog7/e7.protein_families.tsv.gz
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: Table listing orthologous groups per protein family.
    format: tsv
    id: eggnog.download.e7.clu2ogs
    name: eggNOG 7 Protein Family to OGs
    product_file_size: 15838901
    product_url: https://eggnogdb.org/public/eggnog7/e7.clu2ogs.tsv.gz
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: Taxonomic information table for genomes included in eggNOG 7.
    format: tsv
    id: eggnog.download.e7.taxid-info
    name: eggNOG 7 Taxonomic Information
    product_file_size: 1270490
    product_url: https://eggnogdb.org/public/eggnog7/e7.taxid_info.tsv.gz
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: Protein family phylogenetic trees table.
    format: tsv
    id: eggnog.download.e7.trees
    name: eggNOG 7 Protein Family Trees
    product_file_size: 2753498624
    product_url: https://eggnogdb.org/public/eggnog7/e7.trees.tsv.gz
    original_source:
      - source: eggnog
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    compression: gzip
    description: protein network data (full network, scored links between proteins)
    format: txt
    id: string.protein.links
    name: STRING Protein Links
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 138154280240
    product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: protein network data (full network, incl. subscores per channel)
    format: txt
    id: string.protein.links.detailed
    name: STRING Protein Links Detailed
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 203534412387
    product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: 'protein network data (full network, incl. distinction: direct vs. interologs)'
    format: txt
    id: string.protein.links.full
    name: STRING Protein Links Full
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 214269334954
    product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: protein network data (physical subnetwork, scored links between proteins)
    format: txt
    id: string.protein.physical.links
    name: STRING Protein Physical Links
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 11867396121
    product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: protein network data (physical subnetwork, incl. subscores per channel)
    format: txt
    id: string.protein.physical.links.detailed
    name: STRING Protein Physical Links Detailed
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 14859366689
    product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: 'protein network data (physical subnetwork, incl. distinction: direct vs. interologs)'
    format: txt
    id: string.protein.physical.links.full
    name: STRING Protein Physical Links Full
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 15528028374
    product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: association scores between orthologous groups
    format: txt
    id: string.cog.links
    name: STRING COG Links
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 185338269
    product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: association scores (incl. subscores per channel)
    format: txt
    id: string.cog.links.detailed
    name: STRING COG Links Detailed
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 250279091
    product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: 'full database, part II: the networks (nodes, edges, scores,...)'
    id: string.database
    name: STRING Database Network Schema
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 281505096430
    product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
synonyms:
  - eggNOG
  - 'Evolutionary Genealogy of Genes: Non-supervised Orthologous Groups'
---

# eggNOG

eggNOG is a resource of orthologous groups and functional annotations built from
large-scale comparative genomics across many taxa.
