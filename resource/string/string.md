---
activity_status: active
category: DataSource
collection:
  - ber
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://string-db.org/
    label: STRING Consortium
creation_date: '2025-06-04T00:00:00Z'
description: STRING is a database of known and predicted protein-protein interactions. The interactions include direct (physical) and indirect (functional) associations derived from computational prediction, knowledge transfer between organisms, and interactions aggregated from other primary databases.
domains:
  - genomics
  - biomedical
  - proteomics
homepage_url: https://string-db.org/
id: string
infores_id: string
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International (CC BY 4.0)
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: STRING
products:
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
    product_file_size: 250279091
    product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
  - category: Product
    compression: gzip
    description: list of STRING proteins incl. their display names and descriptions
    format: txt
    id: string.protein.info
    name: STRING Protein Info
    product_file_size: 1247927909
    product_url: https://stringdb-downloads.org/download/protein.info.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: sequences of the proteins in STRING (can be used as a BLAST db)
    format: fasta
    id: string.protein.sequences
    name: STRING Protein Sequences
    product_file_size: 13003020999
    product_url: https://stringdb-downloads.org/download/protein.sequences.v12.0.fa.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: 'aliases for STRING proteins: locus names, accessions, descriptions'
    format: txt
    id: string.protein.aliases
    name: STRING Protein Aliases
    product_file_size: 3469549093
    product_url: https://stringdb-downloads.org/download/protein.aliases.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: SW alignment scores between proteins within each STRING species
    format: txt
    id: string.protein.homology
    name: STRING Protein Homology
    product_file_size: 18695040184
    product_url: https://stringdb-downloads.org/download/protein.homology.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: list of terms associated with proteins used in the STRING enrichment
    format: txt
    id: string.protein.enrichment.terms
    name: STRING Protein Enrichment Terms
    product_file_size: 23627938784
    product_url: https://stringdb-downloads.org/download/protein.enrichment.terms.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: hierarchical STRING clusters and their proteins
    format: txt
    id: string.clusters.proteins
    name: STRING Clusters Proteins
    product_file_size: 14024645691
    product_url: https://stringdb-downloads.org/download/clusters.proteins.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: hierarchical STRING clusters annotations
    format: txt
    id: string.clusters.info
    name: STRING Clusters Info
    product_file_size: 217876761
    product_url: https://stringdb-downloads.org/download/clusters.info.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: hierarchical STRING clusters tree (represented as child-parent relationship)
    format: txt
    id: string.clusters.tree
    name: STRING Clusters Tree
    product_file_size: 57934238
    product_url: https://stringdb-downloads.org/download/clusters.tree.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    description: cross-species (aligned) eukaryotic protein network embeddings
    format: hdf5
    id: string.protein.network.embeddings
    name: STRING Protein Network Embeddings
    product_file_size: 19250141917
    product_url: https://stringdb-downloads.org/download/protein.network.embeddings.v12.0.h5
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    description: ProtT5 eukaryotic protein sequence embeddings
    format: hdf5
    id: string.protein.sequence.embeddings
    name: STRING Protein Sequence Embeddings
    product_file_size: 41108799687
    product_url: https://stringdb-downloads.org/download/protein.sequence.embeddings.v12.0.h5
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: hierarchical eggNOG orthologous groups and their proteins
    format: txt
    id: string.protein.orthology
    name: STRING Protein Orthology
    product_file_size: 2197752616
    product_url: https://stringdb-downloads.org/download/protein.orthology.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: LCA orthologous groups (COGs,NOGs,KOGs,...) and their proteins
    format: txt
    id: string.cog.mappings
    name: STRING COG Mappings
    product_file_size: 755326221
    product_url: https://stringdb-downloads.org/download/COG.mappings.v12.0.txt.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    description: organisms in STRING
    format: txt
    id: string.species
    name: STRING Species List
    product_file_size: 1023159
    product_url: https://stringdb-downloads.org/download/species.v12.0.txt
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    description: STRING tree of species
    format: txt
    id: string.species.tree
    name: STRING Species Tree
    product_file_size: 97357335
    product_url: https://stringdb-downloads.org/download/species.tree.v12.0.txt
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: STRING database schema
    format: pdf
    id: string.database.schema
    name: STRING Database Schema
    product_file_size: 52997
    product_url: https://stringdb-downloads.org/download/database.schema.v12.0.pdf
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: gzip
    description: 'full database, part I: the players (proteins, species, COGs,...)'
    id: string.database.items
    name: STRING Database Items Schema
    product_file_size: 45578053363
    product_url: https://stringdb-downloads.org/download/items_schema.v12.0.sql.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
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
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hprd
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
      - source: progenomes
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
      - source: string
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
    product_file_size: 281505096430
    product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
  - category: Product
    compression: gzip
    description: 'full database, part III: interaction evidence (excluding license-restricted data)'
    id: string.database.evidence
    name: STRING Database Evidence Schema
    product_file_size: 59513213030
    product_url: https://stringdb-downloads.org/download/evidence_schema.v12.0.sql.gz
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: ProgrammingInterface
    description: RESTful API for programmatic access to STRING data
    id: string.api
    name: STRING REST API
    product_url: https://string-db.org/cgi/help?subpage=api
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Web interface for searching, visualizing, and analyzing protein-protein interaction networks
    id: string.web
    name: STRING Web Interface
    product_url: https://string-db.org/
    original_source:
      - source: string
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: loinc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: obib
      - relation_type: prov:hadPrimarySource
        source: edam
      - relation_type: prov:hadPrimarySource
        source: hsapdv
      - relation_type: prov:hadPrimarySource
        source: sbo
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: pgo
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: hra
      - relation_type: prov:hadPrimarySource
        source: hubmap
      - relation_type: prov:hadPrimarySource
        source: sennet
      - relation_type: prov:hadPrimarySource
        source: stellar
      - relation_type: prov:hadPrimarySource
        source: dct
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: connectivitymap
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: msigdb
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 4dn
      - relation_type: prov:hadPrimarySource
        source: erccrbp
      - relation_type: prov:hadPrimarySource
        source: erccreg
      - relation_type: prov:hadPrimarySource
        source: faldo
      - relation_type: prov:hadPrimarySource
        source: glycordf
      - relation_type: prov:hadPrimarySource
        source: glycocoo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: kidsfirst
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: motrpac
      - relation_type: prov:hadPrimarySource
        source: mw
      - relation_type: prov:hadPrimarySource
        source: npo
      - relation_type: prov:hadPrimarySource
        source: sckan
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: biomarker
      - relation_type: prov:hadPrimarySource
        source: opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: ubkg
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: loinc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: obib
      - relation_type: prov:hadPrimarySource
        source: edam
      - relation_type: prov:hadPrimarySource
        source: hsapdv
      - relation_type: prov:hadPrimarySource
        source: sbo
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: pgo
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: hra
      - relation_type: prov:hadPrimarySource
        source: hubmap
      - relation_type: prov:hadPrimarySource
        source: sennet
      - relation_type: prov:hadPrimarySource
        source: stellar
      - relation_type: prov:hadPrimarySource
        source: dct
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: connectivitymap
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: msigdb
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 4dn
      - relation_type: prov:hadPrimarySource
        source: erccrbp
      - relation_type: prov:hadPrimarySource
        source: erccreg
      - relation_type: prov:hadPrimarySource
        source: faldo
      - relation_type: prov:hadPrimarySource
        source: glycordf
      - relation_type: prov:hadPrimarySource
        source: glycocoo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: kidsfirst
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: motrpac
      - relation_type: prov:hadPrimarySource
        source: mw
      - relation_type: prov:hadPrimarySource
        source: npo
      - relation_type: prov:hadPrimarySource
        source: sckan
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: biomarker
      - relation_type: prov:hadPrimarySource
        source: opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: ubkg
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
    id: spoke.graph
    name: SPOKE Graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: pid
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: lincs-l1000
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: civic
      - relation_type: prov:hadPrimarySource
        source: gdsc
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: metacyc
      - relation_type: prov:hadPrimarySource
        source: bv-brc
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: pathophenodb
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: interpro
      - relation_type: prov:hadPrimarySource
        source: protcid
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: spoke
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cosmic
      - relation_type: prov:hadPrimarySource
        source: achilles
      - relation_type: prov:hadPrimarySource
        source: depmap
      - relation_type: prov:hadPrimarySource
        source: ccle
      - relation_type: prov:hadPrimarySource
        source: gdsc
      - relation_type: prov:hadPrimarySource
        source: cellosaurus
      - relation_type: prov:hadPrimarySource
        source: clue
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: pharmacodb
      - relation_type: prov:hadPrimarySource
        source: prism
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: compartments
      - relation_type: prov:hadPrimarySource
        source: offsides
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: repohub
      - relation_type: prov:hadPrimarySource
        source: chemicalchecker
      - relation_type: prov:hadPrimarySource
        source: repodb
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: opentargets
      - relation_type: prov:hadPrimarySource
        source: creeds
      - relation_type: prov:hadPrimarySource
        source: interpro
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: dorothea
      - relation_type: prov:hadPrimarySource
        source: progeny
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: huri
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: omnipath
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: bto
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: bioteque
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: KGX Distribution of KG-Monarch
    edge_count: 15371045
    format: kgx
    id: kg-monarch.graph
    name: KGX Distribution of KG-Monarch
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 230877741
    product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: KGX JSON-Lines Distribution of KG-Monarch
    edge_count: 15371045
    format: kgx-jsonl
    id: kg-monarch.graph.jsonl
    name: KGX JSON-L Distribution of KG-Monarch
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 315667976
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: RDF Distribution of KG-Monarch
    edge_count: 15371045
    format: rdfxml
    id: kg-monarch.graph.rdf
    name: RDF Distribution of KG-Monarch
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 879238775
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: Neo4j Dump of KG-Monarch
    dump_format: neo4j
    edge_count: 15371045
    id: kg-monarch.graph.neo4j
    name: Neo4j Dump of KG-Monarch
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 1438250397
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
    warnings: []
  - category: GraphProduct
    description: DuckDB database of KG-Monarch
    edge_count: 15371045
    id: kg-monarch.graph.duckdb
    name: DuckDB database of KG-Monarch
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 6827814912
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: STRING-DB Automat
    format: kgx-jsonl
    id: automat.stringdb
    name: stringdb_automat
    original_source:
      - relation_type: prov:hadPrimarySource
        source: string
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/STRING-DB_Automat/4ca5a0ce557e2c18/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: automat
  - category: GraphProduct
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: pw
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: vo
      - relation_type: prov:hadPrimarySource
        source: bioportal
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: genemania
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: uniprot
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pheknowlator
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
  - category: GraphProduct
    description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
    edge_count: 15371045
    format: kgx-jsonl
    id: kg-monarch.graph.jsonl.edges
    name: KGX JSON-L Distribution of KG-Monarch Edges
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 15279494795
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.jsonl
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: KGX JSON-Lines Distribution of KG-Monarch (Nodes)
    edge_count: 15371045
    format: kgx-jsonl
    id: kg-monarch.graph.jsonl.nodes
    name: KGX JSON-L Distribution of KG-Monarch Nodes
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 1149505896
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.jsonl
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: Neo4j Dump of KG-Monarch Edges
    edge_count: 15371045
    format: neo4j
    id: kg-monarch.graph.neo4j.edges
    name: Neo4j Dump of KG-Monarch Edges
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 4386388748
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.neo4j.csv
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: Neo4j Dump of KG-Monarch Nodes
    edge_count: 15371045
    format: neo4j
    id: kg-monarch.graph.neo4j.nodes
    name: Neo4j Dump of KG-Monarch Nodes
    node_categories:
      - biolink:AnatomicalEntity
      - biolink:BiologicalProcess
      - biolink:Case
      - biolink:Cell
      - biolink:CellularComponent
      - biolink:ChemicalEntity
      - biolink:Disease
      - biolink:Gene
      - biolink:Genotype
      - biolink:LifeStage
      - biolink:MolecularActivity
      - biolink:MolecularEntity
      - biolink:NamedThing
      - biolink:OrganismTaxon
      - biolink:Pathway
      - biolink:PhenotypicFeature
      - biolink:Protein
      - biolink:SequenceVariant
    node_count: 1449211
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenio
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: zfin
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
      - biolink:has_mode_of_inheritance
      - biolink:has_participant
      - biolink:has_phenotype
      - biolink:has_sequence_variant
      - biolink:homologous_to
      - biolink:interacts_with
      - biolink:is_active_in
      - biolink:is_sequence_variant_of
      - biolink:located_in
      - biolink:model_of
      - biolink:orthologous_to
      - biolink:part_of
      - biolink:participates_in
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 349573789
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.neo4j.csv
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: Integrated graph knowledge base combining Mendelian randomization causal estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships (Neo4j backend)
    format: neo4j
    id: epigraphdb.graph
    name: EpiGraphDB Graph Database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epigraphdb
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
      - relation_type: prov:hadPrimarySource
        source: vectology
      - relation_type: prov:hadPrimarySource
        source: ukbiobank
      - relation_type: prov:hadPrimarySource
        source: prsatlas
      - relation_type: prov:hadPrimarySource
        source: eqtlgen
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: cpic
      - relation_type: prov:hadPrimarySource
        source: opentargets
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: semmeddb
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: mrbase
    product_url: https://docs.epigraphdb.org/graph-database/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: epigraphdb
  - category: Product
    description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB) to better characterize adverse outcomes of toxicological interest that are relevant to human health and the environment. Since its inception, the AOP-DB has been developed with the aim of integrating AOP molecular target information with other publicly available datasets to facilitate computational analyses of AOP information.
    id: aop-db.data
    name: AOP-DB Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: aop-wiki
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: toxcast
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 1000genomes
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
    product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: aop-db
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: cancer-genome-interpreter.clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: Product
    description: Protein interaction data aggregated from IntAct, STRING, BioGRID and other interaction databases
    format: http
    id: genecards.protein.interactions
    name: GeneCards Protein Interactions
    original_source:
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: biogrid
    product_url: https://www.genecards.org/
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 403 error when accessing file'
  - category: GraphProduct
    description: Core UniBioMap graph edges file.
    format: csv
    id: unibiomap.links
    name: UniBioMap Graph Links
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 1406201678
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
  - category: GraphProduct
    description: Auxiliary UniBioMap graph annotations and metadata.
    format: tsv
    id: unibiomap.auxs
    name: UniBioMap Graph Auxiliaries
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 591290539
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
  - category: GraphProduct
    description: Predicted UniBioMap graph edges with confidence scores.
    format: csv
    id: unibiomap.pred
    name: UniBioMap Predicted Graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 2484982268
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
  - category: GraphProduct
    description: Full unfiltered UniBioMap predicted graph edges file.
    format: csv
    id: unibiomap.pred.full
    name: UniBioMap Predicted Graph (Full)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 6303875907
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - Szklarczyk D
      - Kirsch R
      - Koutrouli M
      - Nastou K
      - Mehryary F
      - Hachilif R
      - Annika GL
      - Fang T
      - Doncheva NT
      - Pyysalo S
      - Bork P
      - Jensen LJ
      - von Mering C
    doi: doi:10.1093/nar/gkac1000
    id: https://doi.org/10.1093/nar/gkac1000
    journal: Nucleic Acids Research
    preferred: true
    title: The STRING database in 2023 - protein-protein association networks and functional enrichment analyses for any sequenced genome of interest
    year: '2023'
version: '12.0'
---

# STRING - Protein-Protein Interaction Networks

STRING (Search Tool for the Retrieval of Interacting Genes/Proteins) is a database of known and predicted protein-protein interactions. The database contains information from numerous sources, including experimental repositories, computational prediction methods, and public text collections.

## Overview

The STRING database currently covers:
- 59,309,604 proteins from 12,535 organisms
- Over 20 billion interactions
- Confidence scores for all protein interactions

## Data Sources

STRING integrates and scores interactions from five main sources:
1. **Genomic Context Predictions**: Interactions predicted from genome analysis
2. **High-throughput Lab Experiments**: Experimentally determined interactions
3. **(Conserved) Co-Expression**: Proteins that show similar expression patterns
4. **Automated Textmining**: Interactions extracted from scientific literature
5. **Previous Knowledge in Databases**: Curated interactions from existing databases

## Access and Usage

STRING data is available through multiple formats:
- Web interface for interactive visualization and analysis
- Downloadable datasets in various formats (TSV, SQL dumps)
- REST API for programmatic access
- Cytoscape plugin for network analysis

All data in STRING is freely available under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Citations

When using STRING, please cite:
- Szklarczyk D, et al. (2023) The STRING database in 2023 - protein-protein association networks and functional enrichment analyses for any sequenced genome of interest. Nucleic Acids Res. 51(D1):D638-646.
