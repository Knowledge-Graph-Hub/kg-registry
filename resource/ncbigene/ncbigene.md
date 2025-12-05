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
description: NCBI Gene integrates information from a wide range of species. A record
  may include nomenclature, Reference Sequences (RefSeqs), maps, pathways, variations,
  phenotypes, and links to genome-, phenotype-, and locus-specific resources worldwide.
domains:
- biological systems
homepage_url: https://www.ncbi.nlm.nih.gov/gene/
id: ncbigene
infores_id: ncbi-gene
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
  - ensembl
  - ncbigene
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
  - go
  - ncbigene
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
  - pubmed
  - ncbigene
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
  - refseq
  - ncbigene
  product_file_size: 2027684801
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2refseq.gz
- category: Product
  compression: gzip
  description: Gene group information defining functional gene families and clusters
  format: tsv
  id: ncbigene.gene_group
  name: Gene Group Data
  original_source:
  - ncbigene
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
  - ncbigene
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
  - ncbigene
  product_file_size: 1354219182
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz
- category: Product
  compression: gzip
  description: Gene neighbor information showing genomic proximity relationships
  format: tsv
  id: ncbigene.gene_neighbors
  name: Gene Neighbors Data
  original_source:
  - ncbigene
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
  - ncbigene
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
  - refseq
  - ncbigene
  - uniprot
  product_file_size: 1182285769
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_refseq_uniprotkb_collab.gz
- category: Product
  compression: gzip
  description: Gene summary information providing brief descriptions of gene function
  format: tsv
  id: ncbigene.gene_summary
  name: Gene Summary Data
  original_source:
  - ncbigene
  product_file_size: 20880547
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
  product_file_size: 954971
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
  - pubmed
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
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
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
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
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
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
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
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
  - omim
  - ncbigene
  - ensembl
  - hgnc
  product_file_size: 974440
  product_url: https://www.omim.org/static/omim/data/mim2gene.txt
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  secondary_source:
  - rna-kg
- category: ProgrammingInterface
  description: TRAPI web API for querying MicrobiomeKG
  format: http
  id: microbiomekg.api
  name: MicrobiomeKG Plover API
  original_source:
  - biolink
  - chebi
  - ncbitaxon
  - ncbigene
  - mesh
  - pubchem
  - go
  - mondo
  - ncit
  - efo
  - uniprot
  - rhea
  - pr
  - uberon
  - panther
  - hgnc
  - drugbank
  - eupathdb
  product_url: https://multiomics.transltr.io/mbkp
  secondary_source:
  - microbiomekg
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - aop-wiki
  - ctd
  - toxcast
  - disgenet
  - ncbigene
  - string
  - 1000genomes
  - ensembl
  - gwascatalog
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
  secondary_source:
  - aop-db
- category: Product
  description: Integrated gene annotation data aggregated from HGNC, OMIM, Ensembl,
    NCBI Gene, UniProt and other genomic databases
  format: http
  id: genecards.gene.annotations
  name: GeneCards Gene Annotations
  original_source:
  - hgnc
  - omim
  - ensembl
  - ncbigene
  - uniprot
  - refseq
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-05: HTTP 403 error
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
