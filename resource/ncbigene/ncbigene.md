---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/gene
  label: NCBI Gene Database
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  label: NCBI Help Desk
description: >-
  NCBI Gene integrates information from a wide range of species. A record may
  include nomenclature, Reference Sequences (RefSeqs), maps, pathways, variations,
  phenotypes, and links to genome-, phenotype-, and locus-specific resources worldwide.
domains:
- biological systems
homepage_url: https://www.ncbi.nlm.nih.gov/gene/
id: ncbigene
infores_id: "ncbigene"
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: NCBI Gene
products:
- category: MappingProduct
  compression: gzip
  description: Gene to accession mapping data providing links between gene records
    and nucleotide/protein sequence accessions
  format: tsv
  id: ncbigene.gene2accession
  name: Gene to Accession Mapping
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2accession.gz
- category: MappingProduct
  compression: gzip
  description: Gene to Ensembl mapping data providing cross-references between NCBI
    Gene and Ensembl gene identifiers
  format: tsv
  id: ncbigene.gene2ensembl
  name: Gene to Ensembl Mapping
  original_source:
  - ensembl
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2ensembl.gz
- category: MappingProduct
  compression: gzip
  description: Gene to Gene Ontology mapping data providing functional annotations
    for genes
  format: tsv
  id: ncbigene.gene2go
  name: Gene to GO Mapping
  original_source:
  - go
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2go.gz
- category: MappingProduct
  compression: gzip
  description: Gene to PubMed mapping data providing literature references associated
    with genes
  format: tsv
  id: ncbigene.gene2pubmed
  name: Gene to PubMed Mapping
  original_source:
  - pubmed
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2pubmed.gz
- category: MappingProduct
  compression: gzip
  description: Gene to RefSeq mapping data providing links between gene records and
    RefSeq sequence identifiers
  format: tsv
  id: ncbigene.gene2refseq
  name: Gene to RefSeq Mapping
  original_source:
  - refseq
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2refseq.gz
- category: Product
  compression: gzip
  description: Gene group information defining functional gene families and clusters
  format: tsv
  id: ncbigene.gene_group
  name: Gene Group Data
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_group.gz
- category: Product
  compression: gzip
  description: Gene history data tracking changes and updates to gene records over
    time
  format: tsv
  id: ncbigene.gene_history
  name: Gene History Data
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_history.gz
- category: Product
  compression: gzip
  description: Comprehensive gene information including symbols, names, locations,
    and other metadata
  format: tsv
  id: ncbigene.gene_info
  name: Gene Information
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz
- category: Product
  compression: gzip
  description: Gene neighbor information showing genomic proximity relationships
  format: tsv
  id: ncbigene.gene_neighbors
  name: Gene Neighbors Data
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_neighbors.gz
- category: Product
  compression: gzip
  description: Gene ortholog information showing evolutionary relationships between
    genes across species
  format: tsv
  id: ncbigene.gene_orthologs
  name: Gene Orthologs Data
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_orthologs.gz
- category: MappingProduct
  compression: gzip
  description: Gene to RefSeq/UniProtKB collaboration data providing cross-references
    between gene records and protein databases
  format: tsv
  id: ncbigene.gene_refseq_uniprotkb_collab
  name: Gene RefSeq UniProtKB Collaboration Data
  original_source:
  - refseq
  - ncbigene
  - uniprot
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_refseq_uniprotkb_collab.gz
- category: Product
  compression: gzip
  description: Gene summary information providing brief descriptions of gene function
  format: tsv
  id: ncbigene.gene_summary
  name: Gene Summary Data
  original_source:
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_summary.gz
- category: MappingProduct
  description: MIM to Gene and MedGen mapping data connecting genetic disorders to
    genes
  format: tsv
  id: ncbigene.mim2gene_medgen
  name: MIM to Gene MedGen Mapping
  original_source:
  - ncbigene
  - medgen
  - omim
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/mim2gene_medgen
- category: GraphicalInterface
  description: Web-based search and browsing interface for the NCBI Gene database
  format: http
  id: ncbigene.search
  name: NCBI Gene Search Interface
  original_source:
  - ncbigene
  product_url: https://www.ncbi.nlm.nih.gov/gene/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  secondary_source:
  - spoke
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
  - Donna Maglott
  - Jim Ostell
  - Kim D. Pruitt
  - Tatiana Tatusova
  id: doi:10.1093/nar/gkq1237
  journal: Nucleic Acids Research
  preferred: true
  title: 'Entrez Gene: gene-centered information at NCBI'
  year: '2011'
---