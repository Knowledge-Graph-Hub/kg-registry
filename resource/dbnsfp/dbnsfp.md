---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: xiaomingliu@usf.edu
  label: Xiaoming Liu
- category: Organization
  contact_details:
  - contact_type: email
    value: feedback@dbnsfp.org
  - contact_type: url
    value: https://www.dbnsfp.org/about-us
  label: Genos Bioinformatics LLC
creation_date: '2026-10-04T00:00:00Z'
description: dbNSFP is a database of functional predictions and annotations for all
  potential non-synonymous single-nucleotide variants (nsSNVs) and splice-site SNVs
  (ssSNVs) in the human genome. It compiles deleteriousness prediction scores from
  37 algorithms (including SIFT, PolyPhen-2, CADD, REVEL, AlphaMissense and its own
  ensemble scores MetaSVM, MetaLR and MetaRNN), evolutionary conservation scores,
  allele frequencies from population sequencing projects, ClinVar classifications
  and extensive gene-level annotations. Release 5.4 (August 2026) is based on GENCODE
  release 50 / Ensembl 116 and covers 86,701,498 nsSNVs and 2,582,202 ssSNVs. It is
  distributed in an academic branch (free for non-commercial use under CC BY-NC-ND
  4.0, with registration) and a commercial branch (paid license) that omits components
  whose authors restrict commercial use.
domains:
- biomedical
- genomics
- genetic variation
- precision medicine
homepage_url: https://www.dbnsfp.org/
id: dbnsfp
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.dbnsfp.org/license
  label: Academic branch CC BY-NC-ND 4.0; commercial branch under paid license
name: dbNSFP
products:
- category: GraphicalInterface
  description: dbNSFP Public Variant Browser, a free web interface for single-variant
    or small-batch lookups of dbNSFP annotations without downloading the database,
    with shareable permanent links to results.
  format: http
  id: dbnsfp.browser
  name: dbNSFP Public Variant Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  product_url: https://query.dbnsfp.org
- category: Product
  compression: zip
  description: Academic branch of dbNSFP (v5.4a at time of curation, about 50 GB),
    a ZIP of gzipped, tab-delimited per-chromosome variant tables, the gene table,
    column descriptions and the search_dbNSFP Java program. Variant tables are also
    offered as a single tabix-indexed BGZF file per genome build (GRCh37, GRCh38) for
    Ensembl VEP and SnpSift. Includes all upstream scores that are free for academic
    use. Free for academic and non-commercial users after registration with an institutional
    email; download links are issued on request.
  format: tsv
  id: dbnsfp.academic
  license:
    id: https://creativecommons.org/licenses/by-nc-nd/4.0/
    label: CC BY-NC-ND 4.0
  name: dbNSFP Academic Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/download
- category: Product
  compression: zip
  description: Commercial branch of dbNSFP (v5.4c at time of curation), in the same
    format as the academic branch but excluding CADD, VEST, M-CAP, MutScore, PolyPhen-2,
    PrimateAI and RGC Million Exome data, whose authors require separate commercial
    licenses. Available to subscribers under a paid license from Genos Bioinformatics.
  format: tsv
  id: dbnsfp.commercial
  license:
    id: https://www.dbnsfp.org/license
    label: Commercial license (Genos Bioinformatics LLC)
  name: dbNSFP Commercial Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/license
- category: GraphicalInterface
  description: Academic Portal for searching the full dbNSFP academic branch online,
    using the access code issued at academic registration.
  format: http
  id: dbnsfp.academic-portal
  name: dbNSFP Academic Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  product_url: https://query.genos.us
- category: DocumentationProduct
  description: README for dbNSFP v5.4a, listing the license terms, every upstream
    data source with version and URL, the distributed files and usage of the search_dbNSFP
    program.
  format: txt
  id: dbnsfp.readme
  name: dbNSFP v5.4a README
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  product_url: https://dist.genos.us/release/dbNSFP5.4a.readme.txt
- category: DocumentationProduct
  description: Column descriptions for the dbNSFP v5.4a variant table.
  format: txt
  id: dbnsfp.variant-columns
  name: dbNSFP v5.4a Variant Columns
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  product_url: https://dist.genos.us/release/dbNSFP5.4a_variant.columns.txt
- category: DocumentationProduct
  description: Legacy dbNSFP website documenting versions 1.x through 4.x (up to v4.9,
    August 2024), with release notes and download links for past releases.
  format: http
  id: dbnsfp.legacy
  name: dbNSFP Legacy Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  product_url: https://sites.google.com/site/jpopgen/dbNSFP
- category: Product
  compression: zip
  description: dbscSNV v1.1, a companion database of all potential human SNVs within
    splicing consensus regions (-3 to +8 at the 5' splice site and -12 to +2 at the
    3' splice site), with functional annotations and two ensemble scores (AdaBoost
    and random forest) predicting their potential to alter splicing, with hg19 and
    lifted-over hg38 positions. It can be attached to dbNSFP and queried with search_dbNSFP.
  format: tsv
  id: dbnsfp.dbscsnv
  name: dbscSNV v1.1
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  product_url: https://usf.box.com/shared/static/ffwlywsat3q5ijypvunno3rg6steqfs8
publications:
- authors:
  - Xiaoming Liu
  - Chang Li
  - Chengcheng Mou
  - Yibo Dong
  - Yicheng Tu
  doi: 10.1186/s13073-020-00803-9
  id: doi:10.1186/s13073-020-00803-9
  journal: Genome Medicine
  preferred: true
  title: 'dbNSFP v4: a comprehensive database of transcript-specific functional predictions
    and annotations for human nonsynonymous and splice-site SNVs'
  year: '2020'
- authors:
  - Xiaoming Liu
  - Xueqiu Jian
  - Eric Boerwinkle
  doi: 10.1002/humu.21517
  id: doi:10.1002/humu.21517
  journal: Human Mutation
  title: 'dbNSFP: A lightweight database of human nonsynonymous SNPs and their functional
    predictions'
  year: '2011'
- authors:
  - Xueqiu Jian
  - Eric Boerwinkle
  - Xiaoming Liu
  doi: 10.1093/nar/gku1206
  id: doi:10.1093/nar/gku1206
  journal: Nucleic Acids Research
  title: In silico prediction of splice-altering single nucleotide variants in the
    human genome
  year: '2014'
repository: https://www.dbnsfp.org/releases
synonyms:
- database of human non-synonymous SNVs and their functional predictions
taxon:
- NCBITaxon:9606
version: '5.4'
---
# dbNSFP

dbNSFP is a one-stop database of functional predictions and annotations for every possible non-synonymous and splice-site single-nucleotide variant in human protein-coding genes, including mitochondrial DNA. Xiaoming Liu created it in 2011, and it is now developed by Genos Bioinformatics LLC. New releases appear three to five times a year.

## Content

- **Prediction scores** from 37 algorithms, including SIFT, SIFT4G, PROVEAN, PolyPhen-2, MutationTaster 2021, CADD, VEST4, REVEL, AlphaMissense, ESM1b, popEVE, GPN-MSA and dbNSFP's own ensemble scores MetaSVM, MetaLR and MetaRNN.
- **Conservation scores**: PhyloP and phastCons (3 versions each), GERP++, GERP_92_mammals and bStatistic.
- **Allele frequencies** from the 1000 Genomes Project, gnomAD v4.1 and v2.1.1, TOPMed, All of Us, the RGC Million Exome and ALFA.
- **Variant annotations** from ClinVar, dbSNP, InterPro and MANE.
- **Gene-level annotations** from HGNC, UniProt, Gene Ontology, IntAct, GWAS Catalog, OMIM, Orphanet, HPO, GenCC, ClinGen, the Human Protein Atlas, ConsensusPathDB, KEGG, MGI, ZFIN and others.

## Access and Licensing

The academic branch ("a") includes every upstream resource that is free for academic use. It is distributed under CC BY-NC-ND 4.0 to registered users with an institutional email. The commercial branch ("c") is sold under a paid license and leaves out components whose authors restrict commercial use (CADD, VEST, M-CAP, MutScore, PolyPhen-2, PrimateAI and RGC Million Exome in v5.4c). Users of either branch must also comply with the licenses of the individual components, as listed in the README.

A free Public Variant Browser supports small lookups. dbNSFP data are also served through third-party tools such as Ensembl VEP, ANNOVAR, SnpSift, OpenCRAVAT, VarSome and the UCSC Genome Browser, often from older versions.

Versions 1.x to 4.x are documented on the legacy site, but its Amazon S3 download links for v4.9 returned HTTP 404 when checked on 2026-10-04. The companion splice-site database dbscSNV (v1.1, 2015) can be attached to dbNSFP and queried along with it.
