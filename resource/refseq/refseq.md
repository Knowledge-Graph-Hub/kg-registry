---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  - contact_type: github
    value: ncbi
  label: NCBI Help Desk
creation_date: '2025-07-17T00:00:00Z'
description: The NCBI Reference Sequence Database (RefSeq) provides a comprehensive,
  integrated, non-redundant, well-annotated set of reference sequences including genomic,
  transcript, and protein sequences for naturally occurring molecules of the central
  dogma.
domains:
- genomics
- biomedical
- biological systems
homepage_url: https://www.ncbi.nlm.nih.gov/refseq/
id: refseq
last_modified_date: '2025-08-07T00:00:00Z'
layout: resource_detail
name: RefSeq
products:
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
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - do
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
- doi: 10.1093/nar/gkv1189
  id: doi:10.1093/nar/gkv1189
  title: 'Reference sequence (RefSeq) database at NCBI: current status, taxonomic
    expansion, and functional annotation'
- doi: 10.1093/nar/gkl842
  id: doi:10.1093/nar/gkl842
  title: 'NCBI reference sequences (RefSeq): a curated non-redundant sequence database
    of genomes, transcripts and proteins'
repository: https://ftp.ncbi.nlm.nih.gov/refseq/
---
# RefSeq: NCBI Reference Sequence Database

The NCBI Reference Sequence Database (RefSeq) provides a comprehensive, integrated, non-redundant, well-annotated set of reference sequences including genomic, transcript, and protein sequences. RefSeq standards serve as a foundation for functional annotation of genomes and provide stable reference points for mutation analysis, gene expression studies, and polymorphism discovery.

## Overview

RefSeq provides reference sequence standards for naturally occurring molecules of the central dogma, from chromosomes to mRNAs to proteins. The database includes:

- **Genomic sequences**: Complete chromosomes and genomic regions
- **Transcript sequences**: mRNAs and non-coding RNAs  
- **Protein sequences**: Reference protein sequences
- **Cross-references**: Mappings between different sequence databases

## Scope and Content

### Current Statistics (Release 231)
- **Proteins**: 418,412,148 sequences
- **Transcripts**: 72,500,061 sequences  
- **Organisms**: 167,222 represented
- **Regular releases**: Updated periodically with comprehensive data

### Molecule Types and Accession Prefixes
- **Proteins**: NP_, XP_, AP_, YP_, WP_
- **RNA**: NM_, NR_, XM_, XR_
- **Genomic**: NC_, AC_, NG_, NT_, NW_, NZ_

## Key Features

### Data Organization
- **Taxonomic coverage**: Archaea, bacteria, fungi, invertebrates, plants, vertebrates, viruses
- **Sequence formats**: FASTA, GenBank flatfile, ASN.1
- **Update frequency**: Daily updates and periodic releases
- **Quality control**: Curated and computationally annotated sequences

### Special Collections
- **RefSeqGene**: Reference standards for well-characterized genes
- **Functional Elements**: Experimentally validated non-genic functional elements
- **MANE**: Matched Annotation from NCBI and EMBL-EBI
- **Targeted Loci**: rRNA sequences from type material

## Access Methods

### FTP Access
- **Main repository**: [ftp://ftp.ncbi.nlm.nih.gov/refseq/](ftp://ftp.ncbi.nlm.nih.gov/refseq/)
- **Genome sequences**: [ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/](ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/)
- **Daily updates**: Available for non-WGS and WGS sequences
- **Organism-specific**: Data for model organisms (human, mouse, etc.)

### Web Interfaces
- **RefSeq homepage**: [https://www.ncbi.nlm.nih.gov/refseq/](https://www.ncbi.nlm.nih.gov/refseq/)
- **NCBI Datasets**: Modern API and web interface
- **Genome Data Viewer**: Interactive genome browser

## Related Projects

- **CCDS**: Consensus CDS project for human and mouse
- **RefSeq Select**: High-confidence transcript sets
- **NCBI Virus**: Viral sequence collection
- **Prokaryotic Genome Annotation Pipeline**: Automated annotation system

## Citation

When using RefSeq data, please cite:
- O'Leary NA, et al. Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional annotation. Nucleic Acids Res. 2016;44(D1):D733-45.

## Contact Information

For questions, updates, or collaborations:
- **Help Desk**: info@ncbi.nlm.nih.gov
- **RefSeq Updates**: Subscribe to refseq-announce mailing list
- **GitHub**: [https://github.com/ncbi](https://github.com/ncbi)