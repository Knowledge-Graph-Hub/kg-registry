---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/gene
  id: ncbi
  label: NCBI Gene Database
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  id: ncbi
  label: NCBI Help Desk
creation_date: '2025-06-04T00:00:00Z'
description: NCBI Gene integrates information from a wide range of species. A record
  may include nomenclature, Reference Sequences (RefSeqs), maps, pathways, variations,
  phenotypes, and links to genome-, phenotype-, and locus-specific resources worldwide.
domains:
- biological systems
homepage_url: https://www.ncbi.nlm.nih.gov/gene/
id: ncbigene
infores_id: ncbi-gene
last_modified_date: '2026-02-20T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 3953177919
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2accession.gz
- category: MappingProduct
  compression: gzip
  description: Gene to Ensembl mapping data providing cross-references between NCBI
    Gene and Ensembl gene identifiers
  format: tsv
  id: ncbigene.gene2ensembl
  name: Gene to Ensembl Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 282824267
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2ensembl.gz
- category: MappingProduct
  compression: gzip
  description: Gene to Gene Ontology mapping data providing functional annotations
    for genes
  format: tsv
  id: ncbigene.gene2go
  name: Gene to GO Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 1223833668
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2go.gz
- category: MappingProduct
  compression: gzip
  description: Gene to PubMed mapping data providing literature references associated
    with genes
  format: tsv
  id: ncbigene.gene2pubmed
  name: Gene to PubMed Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 230242176
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2pubmed.gz
- category: MappingProduct
  compression: gzip
  description: Gene to RefSeq mapping data providing links between gene records and
    RefSeq sequence identifiers
  format: tsv
  id: ncbigene.gene2refseq
  name: Gene to RefSeq Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 2027684801
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2refseq.gz
- category: Product
  compression: gzip
  description: Gene group information defining functional gene families and clusters
  format: tsv
  id: ncbigene.gene_group
  name: Gene Group Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 295428
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_group.gz
- category: Product
  compression: gzip
  description: Gene history data tracking changes and updates to gene records over
    time
  format: tsv
  id: ncbigene.gene_history
  name: Gene History Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 153023757
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_history.gz
- category: Product
  compression: gzip
  description: Comprehensive gene information including symbols, names, locations,
    and other metadata
  format: tsv
  id: ncbigene.gene_info
  name: Gene Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 1354219182
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz
- category: Product
  compression: gzip
  description: Gene neighbor information showing genomic proximity relationships
  format: tsv
  id: ncbigene.gene_neighbors
  name: Gene Neighbors Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 1764403523
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_neighbors.gz
- category: Product
  compression: gzip
  description: Gene ortholog information showing evolutionary relationships between
    genes across species
  format: tsv
  id: ncbigene.gene_orthologs
  name: Gene Orthologs Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 108555140
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_orthologs.gz
- category: MappingProduct
  compression: gzip
  description: Gene to RefSeq/UniProtKB collaboration data providing cross-references
    between gene records and protein databases
  format: tsv
  id: ncbigene.gene_refseq_uniprotkb_collab
  name: Gene RefSeq UniProtKB Collaboration Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 1182285769
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_refseq_uniprotkb_collab.gz
- category: Product
  compression: gzip
  description: Gene summary information providing brief descriptions of gene function
  format: tsv
  id: ncbigene.gene_summary
  name: Gene Summary Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 20880547
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_summary.gz
- category: MappingProduct
  description: MIM to Gene and MedGen mapping data connecting genetic disorders to
    genes
  format: tsv
  id: ncbigene.mim2gene_medgen
  name: MIM to Gene MedGen Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 954971
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/mim2gene_medgen
- category: GraphicalInterface
  description: Web-based search and browsing interface for the NCBI Gene database
  format: http
  id: ncbigene.search
  name: NCBI Gene Search Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://www.ncbi.nlm.nih.gov/gene/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: humannet
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharmkg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://zenodo.org/record/4077338
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genemania
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vo
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
- category: MappingProduct
  description: Public mapping of MIM numbers to NCBI Gene IDs, Ensembl Gene IDs, and
    HGNC symbols
  format: tsv
  id: omim.mim2gene
  name: OMIM mim2gene.txt
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_file_size: 974440
  product_url: https://www.omim.org/static/omim/data/mim2gene.txt
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
- category: ProgrammingInterface
  description: TRAPI web API for querying MicrobiomeKG
  format: http
  id: microbiomekg.api
  name: MicrobiomeKG Plover API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: eupathdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: microbiomekg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://multiomics.transltr.io/mbkp
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
- category: Product
  description: Integrated gene annotation data aggregated from HGNC, OMIM, Ensembl,
    NCBI Gene, UniProt and other genomic databases
  format: http
  id: genecards.gene.annotations
  name: GeneCards Gene Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://www.genecards.org/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 403 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: MappingProduct
  compression: zip
  description: A single delimited text file format containing a list of mappings between
    different identifiers stored in BioGRID and the identifiers used in downloads.
  format: tsv
  id: biogrid.identifiers
  latest_version: 5.0.252
  name: BIOGRID-IDENTIFIERS-LATEST.tab.zip
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_url: https://downloads.thebiogrid.org/File/BioGRID/Latest-Release/BIOGRID-IDENTIFIERS-LATEST.tab.zip
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
    source: omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to Entrez Gene identifiers
  format: tsv
  id: oma.mapping.entrez
  name: OMA to Entrez Gene Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://omabrowser.org/All/oma-entrez.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 403 error
    when accessing file'
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
