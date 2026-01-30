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
description: BioCyc is a collection of 20,070 Pathway/Genome Databases (PGDBs) for
  model eukaryotes and for thousands of microbes, plus software tools for exploring
  them. BioCyc is an encyclopedic reference that contains curated data from 146,000
  publications.
domains:
- biological systems
homepage_url: https://biocyc.org/
id: biocyc
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
  - chebi
  - bigg
  - biocyc
  - kegg
  - reactome
  product_file_size: 400516
  product_url: https://w3id.org/biopragmatics/resources/bigg.metabolite/bigg.metabolite.sssom.tsv
  secondary_source:
  - obo-db-ingest
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
taxon:
- NCBITaxon:2759
---
BioCyc