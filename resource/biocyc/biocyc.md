---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biocyc-support@sri.com
  label: BioCyc
creation_date: '2025-03-18T00:00:00Z'
description: BioCyc is a collection of 20,070 Pathway/Genome Databases (PGDBs) for
  model eukaryotes and for thousands of microbes, plus software tools for exploring
  them. BioCyc is an encyclopedic reference that contains curated data from 146,000
  publications.
domains:
- biological systems
homepage_url: https://biocyc.org/
id: biocyc
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://biocyc.org/download.shtml
  label: Varies
name: BioCyc
products:
- category: MappingProduct
  description: bigg.metabolite SSSOM
  format: sssom
  id: obo-db-ingest.bigg.metabolite.sssom.tsv
  license:
    id: http://bigg.ucsd.edu/license#license
    label: Custom
  name: bigg.metabolite SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  product_file_size: 400516
  product_url: https://w3id.org/biopragmatics/resources/bigg.metabolite/bigg.metabolite.sssom.tsv
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, scored links between proteins)
  format: txt
  id: string.protein.links
  name: STRING Protein Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 138154280240
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, incl. subscores per channel)
  format: txt
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
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
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 214269334954
  product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, scored links between proteins)
  format: txt
  id: string.protein.physical.links
  name: STRING Protein Physical Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 11867396121
  product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, incl. subscores per channel)
  format: txt
  id: string.protein.physical.links.detailed
  name: STRING Protein Physical Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
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
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 15528028374
  product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores between orthologous groups
  format: txt
  id: string.cog.links
  name: STRING COG Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 185338269
  product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores (incl. subscores per channel)
  format: txt
  id: string.cog.links.detailed
  name: STRING COG Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 250279091
  product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'full database, part II: the networks (nodes, edges, scores,...)'
  format: postgres
  id: string.database
  name: STRING Database Network Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 281505096430
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
- category: GraphicalInterface
  description: Interactive web interface for browsing and analyzing iModulons across
    15 prokaryotic organisms with 22 datasets, 1924 curated iModulons, and 9576 expression
    profiles. Includes organism-specific dataset pages, iModulon dashboards, gene
    search functionality, and project information pages displaying experimental conditions
    and publication abstracts.
  format: http
  id: imodulondb.browser
  name: iModulonDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imodulondb
  product_url: https://imodulondb.org/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: biocyc
  - relation_type: prov:wasInformedBy
    source: string
- category: Product
  description: Downloadable transcriptomic datasets and iModulon decompositions for
    15 organisms including E. coli, B. subtilis, S. aureus, M. tuberculosis, P. aeruginosa,
    P. putida, and others. Includes gene expression matrices, iModulon activity matrices,
    gene weights, and metadata for over 9500 expression profiles from 525 studies.
  format: mixed
  id: imodulondb.datasets
  name: iModulonDB Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imodulondb
  product_url: https://imodulondb.org/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: biocyc
  - relation_type: prov:wasDerivedFrom
    source: sra
  - relation_type: prov:wasInformedBy
    source: string
- category: GraphicalInterface
  description: Web interface for browsing and searching human metabolic pathways,
    genes, enzymes, reactions, and compounds within the BioCyc Pathway Tools environment.
  format: http
  id: humancyc.portal
  name: HumanCyc Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humancyc
  product_url: https://humancyc.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: biocyc
- category: Product
  description: Downloadable HumanCyc Pathway/Genome Database (PGDB) data, including
    pathways, reactions, enzymes, and compounds, available through the BioCyc download
    services.
  format: mixed
  id: humancyc.downloads
  name: HumanCyc Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humancyc
  product_url: https://biocyc.org/download.shtml
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: biocyc
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
- category: GraphProduct
  description: Current PSS model in Systems Biology Graphical Notation XML format
  format: sbgnml
  id: skm.pss.live.sbgn
  name: PSS Live Download (SBGN-ML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 3204548
  product_url: https://skm.nib.si/downloads/pss/public/sbgn
- category: GraphProduct
  description: Current PSS model in Systems Biology Markup Language XML format
  format: sbml
  id: skm.pss.live.sbml
  name: PSS Live Download (SBML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 548527
  product_url: https://skm.nib.si/downloads/pss/public/sbml
- category: GraphProduct
  description: PSS model (v1.0.0, October 2023) in DOT Language format compatible
    with Graphviz. The live/current DOT export endpoint was retired upstream; this
    points to the latest published versioned DOT export.
  format: dot
  id: skm.pss.live.dot
  name: PSS Download (DOT, v1.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 405988
  product_url: https://skm.nib.si/downloads/pss-version/v1.0.0/graphviz
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are represented as nodes (as in PSS Explorer and database schema).
  format: sif
  id: skm.pss.live.sif.original.graph
  name: PSS Live Download, original (SIF/LGL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 161651
  product_url: https://skm.nib.si/downloads/pss/public/sif-edges
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are represented as nodes (as in PSS Explorer and database schema). This
    file contains the node annotations.
  format: sif
  id: skm.pss.live.sif.original.annotations
  name: PSS Live Download, original (SIF/LGL), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 401897
  product_url: https://skm.nib.si/downloads/pss/public/sif-nodes
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges.
  format: sif
  id: skm.pss.live.sif.projection.graph
  name: PSS Live Download, projection (SIF/LGL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 253631
  product_url: https://skm.nib.si/downloads/pss/public/rxn-edges
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges. This file contains the node annotations.
  format: sif
  id: skm.pss.live.sif.projection.annotations
  name: PSS Live Download, projection (SIF/LGL), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 163587
  product_url: https://skm.nib.si/downloads/pss/public/rxn-nodes
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges, FunctionalClusters are expanded to arabidopsis
    identifiers.
  format: sif
  id: skm.pss.live.sif.dinar.graph
  name: PSS Live Download, DiNAR (SIF/LGL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 361747
  product_url: https://skm.nib.si/downloads/pss/public/dinar-edges
- category: GraphProduct
  description: Current PSS model in Boolean network format compatible with BoolDog
    and BoolNet
  format: boolnet
  id: skm.pss.live.boolnet.graph
  name: PSS Live Downloads (BoolNet)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 53198
  product_url: https://skm.nib.si/downloads/pss/public/boolnet
- category: GraphProduct
  description: Current PSS model in Boolean network format compatible with BoolDog
    and BoolNet. This file contains the node annotations.
  format: boolnet
  id: skm.pss.live.boolnet.annotations
  name: PSS Live Downloads (BoolNet), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 70946
  product_url: https://skm.nib.si/downloads/pss/public/boolnet-annot
- category: GraphProduct
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities
    and ~500,000 interactions
  edge_count: 500000
  format: sif
  id: skm.ckn.v2.graph
  name: CKN v2 (June 2023)
  node_count: 26234
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 2732107
  product_url: https://skm.nib.si/downloads/ckn/v2-2023.06/edges
- category: GraphProduct
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities
    and ~500,000 interactions. This file contains the node annotations.
  format: sif
  id: skm.ckn.v2.annotations
  name: CKN v2 (June 2023), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 885747
  product_url: https://skm.nib.si/downloads/ckn/v2-2023.06/nodes
- category: GraphProduct
  description: Comprehensive Knowledge Network v1 in SIF/LGL format
  format: sif
  id: skm.ckn.v1.graph
  name: CKN v1 (June 2018)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 318666
  product_url: https://skm.nib.si/downloads/ckn/v1-2018.06/edges
- category: GraphProduct
  description: Comprehensive Knowledge Network v1 in SIF/LGL format. This file contains
    the node annotations.
  format: sif
  id: skm.ckn.v1.annotations
  name: CKN v1 (June 2018), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 702407
  product_url: https://skm.nib.si/downloads/ckn/v1-2018.06/nodes
publications:
- authors:
  - Karp PD
  - Billington R
  - Caspi R
  - Fulcher CA
  - Latendresse M
  - Kothari A
  - Keseler IM
  - Krummenacker M
  - Midford PE
  - Ong Q
  - Ong WK
  - Paley SM
  - Subhraveti P
  doi: 10.1093/bib/bbx085
  id: https://www.ncbi.nlm.nih.gov/pubmed/29447345
  journal: Brief Bioinform
  preferred: true
  title: The BioCyc collection of microbial genomes and metabolic pathways
  year: '2019'
taxon:
- NCBITaxon:2759
---
BioCyc