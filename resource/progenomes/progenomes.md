---
activity_status: active
category: DataSource
creation_date: '2026-01-30T00:00:00Z'
description: A large-scale microbial genome resource with consistent annotation, species
  clustering, and downloadable representative genome and protein datasets.
domains:
- genomics
- microbiology
- biological systems
homepage_url: https://progenomes.embl.de/
id: progenomes
last_modified_date: '2026-02-15T00:00:00Z'
layout: resource_detail
name: proGenomes
products:
- category: GraphicalInterface
  description: Main proGenomes web interface for exploring microbial genomes and clusters.
  format: http
  id: progenomes.portal
  name: proGenomes Portal
  product_url: https://progenomes.embl.de/
- category: Product
  compression: gzip
  description: NCBI taxonomy mapping table for proGenomes v4 entries.
  format: tsv
  id: progenomes.pg4.ncbi-taxonomy
  name: proGenomes v4 NCBI Taxonomy Table
  product_file_size: 6094365
  product_url: https://progenomes.embl.de/data/pg4_ncbi_taxonomy.tsv.gz
- category: Product
  compression: gzip
  description: Representative protein FASTA set for proGenomes v4.
  format: fasta
  id: progenomes.pg4.rep-proteins
  name: proGenomes v4 Representative Proteins
  product_file_size: 30345688548
  product_url: https://progenomes.embl.de/data/repGenomes/pg4_proteins_representatives.faa.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, scored links between proteins)
  format: txt
  id: string.protein.links
  name: STRING Protein Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 138154280240
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, incl. subscores per channel)
  format: txt
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 203534412387
  product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (full network, incl. distinction: direct vs.
    interologs)'
  format: txt
  id: string.protein.links.full
  name: STRING Protein Links Full
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 214269334954
  product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, scored links between proteins)
  format: txt
  id: string.protein.physical.links
  name: STRING Protein Physical Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 11867396121
  product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, incl. subscores per channel)
  format: txt
  id: string.protein.physical.links.detailed
  name: STRING Protein Physical Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 14859366689
  product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (physical subnetwork, incl. distinction: direct
    vs. interologs)'
  format: txt
  id: string.protein.physical.links.full
  name: STRING Protein Physical Links Full
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 15528028374
  product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores between orthologous groups
  format: txt
  id: string.cog.links
  name: STRING COG Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 185338269
  product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores (incl. subscores per channel)
  format: txt
  id: string.cog.links.detailed
  name: STRING COG Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 250279091
  product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'full database, part II: the networks (nodes, edges, scores,...)'
  id: string.database
  name: STRING Database Network Schema
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 281505096430
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
synonyms:
- proGenomes
- ProGenomes Database
---
# proGenomes

proGenomes is a large-scale microbial genome resource with consistent annotations,
quality controls, representative sets, and downloadable genome-derived datasets.
