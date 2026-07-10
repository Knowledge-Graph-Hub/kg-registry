---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://dip.doe-mbi.ucla.edu/
  - contact_type: email
    value: dip@mbi.ucla.edu
  label: UCLA-DOE Institute for Genomics and Proteomics
- category: Individual
  contact_details:
  - contact_type: url
    value: https://www.chem.ucla.edu/~eisenberg/
  label: David Eisenberg
creation_date: '2025-11-10T00:00:00Z'
description: The Database of Interacting Proteins (DIP) is a curated biological database
  that catalogs experimentally determined interactions between proteins, developed
  and maintained by the research group of David Eisenberg at the University of California
  Los Angeles (UCLA). Established in 2002, DIP combines information from diverse sources
  to create a unified, consistent set of protein-protein interactions with both manual
  expert curation and automated computational approaches that leverage knowledge extracted
  from the most reliable core subset of the data. DIP serves as a member of the International
  Molecular Exchange (IMEx) Consortium, an international collaboration of major public
  providers of protein interaction data including IntAct, MINT, BioGRID, and others
  that work together to avoid duplication of curation efforts by collecting data from
  non-overlapping sources and sharing curated interaction data. The database enables
  searches through its web interface based on multiple criteria including interactions
  described in specific journal articles, interactions supported by particular types
  of experimental evidence, and protein identifiers or sequences. DIP data have been
  curated using both manual approaches by expert biologists and automated computational
  methods that utilize machine learning and network analysis of the high-confidence
  core interaction data. The IMEx consortium developed the HUPO Proteomics Standards
  Initiative Molecular Interaction (HUPO-PSI-MI) XML format, which has become widely
  implemented for standardizing molecular interaction data representation. All information
  within DIP is freely available under a Creative Commons Attribution-NoDerivatives
  3.0 license. DIP provides downloads of complete datasets and specialized subsets,
  supporting integration with other protein interaction databases and serving as a
  foundational resource for systems biology, network analysis, and protein function
  prediction studies.
domains:
- biological systems
homepage_url: https://dip.doe-mbi.ucla.edu/
id: dip
infores_id: dip
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://dip.doe-mbi.ucla.edu/dip/Download.cgi
  label: DIP Terms of Use
name: Database of Interacting Proteins
products:
- category: GraphicalInterface
  description: Web-based search interface for exploring protein-protein interactions
    by journal article, experimental evidence, or protein identifiers
  format: http
  id: dip.search
  name: DIP Search Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dip
  product_url: https://dip.doe-mbi.ucla.edu/dip/Search.cgi
- category: Product
  description: Complete DIP dataset and specialized subsets available for download
    in PSI-MI formats (registration required)
  format: psi_mi_mitab
  id: dip.downloads
  name: DIP Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dip
  product_url: https://dip.doe-mbi.ucla.edu/dip/Download.cgi
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='dip.doe-mbi.ucla.edu', port=443)_ Max retries
    exceeded with url_ /dip/Download.cgi (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='dip.doe-mbi.ucla.edu', port=443)_ Max retries
    exceeded with url_ /dip/Download.cgi (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='dip.doe-mbi.ucla.edu', port=443)_ Max retries
    exceeded with url_ /dip/Download.cgi (Caused by SSLError(SSLCertVerificationError(1,
    '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local
    issuer certificate (_ssl.c_1017)')))
- category: Product
  description: Historical consolidated protein interaction index in PSI-MITAB 2.5
    format aggregating data from BIND, BioGrid, DIP, HPRD, IntAct, MINT, MPact, MPPI
    and OPHID
  format: psi_mi_mitab
  id: irefindex.database
  name: iRefIndex Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bind
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: irefindex
  - relation_type: prov:hadPrimarySource
    source: mint
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
- category: Product
  description: Current HIPPIE v2.4 interaction dataset in the native HIPPIE tab-delimited
    format, last updated April 9, 2026
  format: tsv
  id: hippie.current.tab
  latest_version: v2.4
  name: HIPPIE Current TAB Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hippie
  product_file_size: 138719165
  product_url: https://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/hippie_current.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: hprd
- category: Product
  description: Current HIPPIE v2.4 interaction dataset in PSI-MI TAB 2.5 format, last
    updated April 9, 2026
  format: psi_mi_mitab
  id: hippie.current.mitab
  latest_version: v2.4
  name: HIPPIE Current PSI-MI TAB Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hippie
  product_file_size: 257038149
  product_url: https://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/HIPPIE-current.mitab.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: hprd
- category: Product
  description: Downloadable HPIDB host-pathogen interaction dataset in PSI-MITAB format.
  format: psi_mi_mitab
  id: hpidb.mitab
  name: HPIDB PSI-MITAB Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hpidb
  product_url: https://hpidb.igbb.msstate.edu/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  warnings:
  - The HPIDB homepage failed to establish HTTP and HTTPS connections during curation
    on 2026-06-02.
  - The historical AgBase HPI downloads URL redirected and then returned HTTP 403
    during curation on 2026-06-02.
  - 'File was not able to be retrieved when checked on 2026-07-03: Error connecting
    to URL: HTTPSConnectionPool(host=''hpidb.igbb.msstate.edu'', port=443): Max retries
    exceeded with url: / (Caused by NewConnectionError("HTTPSConnection(host=''hpidb.igbb.msstate.edu'',
    port=443): Failed to establish a new connection: [Errno 111] Connection refused"))'
  - 'File was not able to be retrieved when checked on 2026-07-10: Error connecting
    to URL: HTTPSConnectionPool(host=''hpidb.igbb.msstate.edu'', port=443): Max retries
    exceeded with url: / (Caused by NewConnectionError("HTTPSConnection(host=''hpidb.igbb.msstate.edu'',
    port=443): Failed to establish a new connection: [Errno 111] Connection refused"))'
- category: GraphProduct
  compression: gzip
  description: IID annotated human protein-protein interaction download.
  format: tsv
  id: iid.human_annotated_ppis
  name: IID Human Annotated PPIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iid
  product_file_size: 150992743
  product_url: https://iid.ophid.utoronto.ca/static/download/human_annotated_PPIs.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: GraphProduct
  compression: gzip
  description: IID annotated mouse protein-protein interaction download.
  format: tsv
  id: iid.mouse_annotated_ppis
  name: IID Mouse Annotated PPIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iid
  product_file_size: 40056241
  product_url: https://iid.ophid.utoronto.ca/static/download/mouse_annotated_PPIs.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: mint
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: Product
  compression: gzip
  description: PC v14 integrated BioPAX Level 3 unified model containing normalized
    pathway data, molecular interactions, cross-database entity mappings, and metadata-derived
    content from 26 datasource rows.
  format: biopax
  id: pathwaycommons.biopax
  name: Integrated BioPAX Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 1700903742
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-biopax.owl.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  description: Download directory for Pathway Commons PC v14 integrated pathway and
    molecular interaction datasets, including BioPAX, SIF, GMT, TXT, and JSON-LD products.
  format: mixed
  id: pathwaycommons.downloads
  name: Pathway Commons Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Simple Interaction Format network file representing binary pairwise
    molecular relationships integrated from Pathway Commons upstream datasource rows.
  format: sif
  id: pathwaycommons.sif
  name: SIF Network Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 9810179
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.sif.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Gene Matrix Transposed gene sets for pathway enrichment analysis,
    derived from the integrated Pathway Commons pathway archive.
  format: tsv
  id: pathwaycommons.gmt
  name: GMT Gene Set Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 262513
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.gmt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 tab-delimited extended SIF node and edge file using HGNC-oriented
    identifiers for integrated Pathway Commons interactions.
  format: txt
  id: pathwaycommons.txt
  name: Extended SIF TXT Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 115608500
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: GraphProduct
  description: Integrated pharmacological knowledge graph (PharmDB-K) of drugs, targets,
    diseases, and associations
  format: http
  id: pharmdb.graph
  name: PharmDB-K Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: dcdb
  - relation_type: prov:hadPrimarySource
    source: gad
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: t3db
  - relation_type: prov:hadPrimarySource
    source: wipo-tkp
publications:
- authors:
  - I. Xenarios
  doi: 10.1093/nar/30.1.303
  id: https://doi.org/10.1093/nar/30.1.303
  journal: Nucleic Acids Research
  title: 'DIP, the Database of Interacting Proteins: a research tool for studying
    cellular networks of protein interactions'
  year: '2002'
- authors:
  - L. Salwinski
  doi: 10.1093/nar/gkh086
  id: https://doi.org/10.1093/nar/gkh086
  journal: Nucleic Acids Research
  title: 'The Database of Interacting Proteins: 2004 update'
  year: '2004'
- authors:
  - Sandra Orchard
  - Samuel Kerrien
  - Sara Abbani
  - Bruno Aranda
  - Jignesh Bhate
  - Shelby Bidwell
  - Alan Bridge
  - Leonardo Briganti
  - Fiona S L Brinkman
  - Gianni Cesareni
  - Andrew Chatr-aryamontri
  - Emilie Chautard
  - Carol Chen
  - Marine Dumousseau
  - Johannes Goll
  - Robert E W Hancock
  - Linda I Hannick
  - Igor Jurisica
  - Jyoti Khadake
  - David J Lynn
  - Usha Mahadevan
  - Livia Perfetto
  - Arathi Raghunath
  - Sylvie Ricard-Blum
  - Bernd Roechert
  - Lukasz Salwinski
  - Volker Stümpflen
  - Mike Tyers
  - Peter Uetz
  - Ioannis Xenarios
  - Henning Hermjakob
  doi: 10.1038/nmeth.1931
  id: https://doi.org/10.1038/nmeth.1931
  journal: Nature Methods
  title: 'Protein interaction data curation: The International Molecular Exchange
    (IMEx) consortium'
  year: '2012'
synonyms:
- DIP
- Database of Interacting Proteins
---
# Database of Interacting Proteins

The Database of Interacting Proteins (DIP) is a curated resource for experimentally validated protein-protein interactions, maintained by UCLA as part of the IMEx consortium.