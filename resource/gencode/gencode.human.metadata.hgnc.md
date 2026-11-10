---
category: MappingProduct
compression: gzip
description: Mapping of GENCODE human transcripts to HGNC approved gene symbols, from
  the Ensembl xref pipeline. Companion metadata files in the same release map transcripts
  to NCBI Gene (Entrez) IDs, RefSeq, UniProtKB/Swiss-Prot and TrEMBL, PDB, and PubMed
  IDs.
format: tsv
id: gencode.human.metadata.hgnc
latest_version: '50'
name: GENCODE Human HGNC Metadata
original_source:
- relation_type: prov:hadPrimarySource
  source: gencode
- relation_type: prov:wasInformedBy
  source: hgnc
- relation_type: prov:wasInformedBy
  source: ncbigene
- relation_type: prov:wasInformedBy
  source: refseq
- relation_type: prov:wasInformedBy
  source: uniprot
- relation_type: prov:wasInformedBy
  source: pdb
- relation_type: prov:wasInformedBy
  source: pubmed
product_file_size: 2698457
product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.metadata.HGNC.gz
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: ensembl
layout: product_detail
---
