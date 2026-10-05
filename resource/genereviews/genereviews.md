---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/books/NBK1116/
  - contact_type: email
    value: cmahon3@uw.edu
  label: GeneReviews, University of Washington, Seattle
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/
  id: ncbi
  label: National Center for Biotechnology Information (NCBI) Bookshelf
creation_date: '2026-10-04T00:00:00Z'
description: GeneReviews is an expert-authored, peer-reviewed collection of disease
  descriptions for inherited conditions, covering diagnosis, management and genetic
  counseling. It is edited at the University of Washington, Seattle and published
  on the NCBI Bookshelf, with about 890 chapters as of 2026-10-04. NCBI also publishes
  weekly-updated mapping files linking each chapter to its NCBI Bookshelf id, PubMed
  id, genes, UniProt accessions and OMIM numbers.
domains:
- biomedical
- clinical
- genomics
- rare disease
homepage_url: https://www.ncbi.nlm.nih.gov/books/NBK1116/
id: genereviews
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/books/NBK138602/
  label: GeneReviews Copyright Notice and Usage Disclaimer (noncommercial research
    use with attribution)
name: GeneReviews
products:
- category: GraphicalInterface
  description: GeneReviews collection on the NCBI Bookshelf, with searchable expert-authored
    chapters on inherited conditions.
  format: http
  id: genereviews.portal
  name: GeneReviews on NCBI Bookshelf
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK1116/
- category: Product
  description: Tab-delimited list of GeneReviews chapters with short name, chapter
    title, NCBI Bookshelf (NBK) id and PubMed id, updated weekly.
  format: tsv
  id: genereviews.titles
  name: GeneReviews Titles
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 21527
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/GRtitle_shortname_NBKid.txt
- category: MappingProduct
  description: Tab-delimited mapping of GeneReviews chapters (NBK id and short name)
    to OMIM numbers, updated weekly.
  format: tsv
  id: genereviews.omim
  name: GeneReviews to OMIM Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 24971
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/NBKid_shortname_OMIM.txt
- category: MappingProduct
  description: Tab-delimited mapping of GeneReviews chapters (NBK id and short name)
    to HGNC gene symbols, updated weekly.
  format: tsv
  id: genereviews.genes
  name: GeneReviews to Gene Symbol Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_file_size: 17484
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/NBKid_shortname_genesymbol.txt
- category: MappingProduct
  description: Tab-delimited mapping of GeneReviews chapters to gene symbols and UniProt
    accessions, updated weekly.
  format: tsv
  id: genereviews.genes-uniprot
  name: GeneReviews to Gene Symbol and UniProt Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 24053
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/NBKid_shortname_genesymbol_UniProt.txt
- category: MappingProduct
  description: Pipe-delimited mapping of GeneReviews short names and NBK ids to gene
    symbols and disease names, without a header row, updated weekly.
  format: txt
  id: genereviews.genes-diseases
  name: GeneReviews Gene and Disease Name Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_file_size: 29333
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/GRshortname_NBKid_genesymbol_dzname.txt
- category: DocumentationProduct
  description: README for the GeneReviews data reports on the NCBI FTP site.
  format: http
  id: genereviews.readme
  name: GeneReviews Data README
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genereviews
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/README.html
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing concept names and source
    identifiers with gzip compression
  format: txt
  id: medgen.mgconso
  name: MGCONSO (Concept Names)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: genereviews
  product_file_size: 15816874
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGCONSO.RRF.gz
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing definitions and descriptions
    with gzip compression
  format: txt
  id: medgen.mgdef
  name: MGDEF (Definitions)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: genereviews
  product_file_size: 5305829
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGDEF.RRF.gz
synonyms:
- GeneReviews®
- GR
taxon:
- NCBITaxon:9606
---
# GeneReviews

GeneReviews is a collection of expert-authored, peer-reviewed chapters on inherited conditions. Each chapter covers diagnosis, management and genetic counseling for one condition or group of conditions. The collection is edited at the University of Washington, Seattle (first published in 1993) and is hosted on the [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1116/).

## Data Files

NCBI publishes five data reports at https://ftp.ncbi.nlm.nih.gov/pub/GeneReviews/, updated weekly:

- `GRtitle_shortname_NBKid.txt`: chapter short name, title, NBK id and PMID (tab-delimited).
- `NBKid_shortname_OMIM.txt`: chapter to OMIM number (tab-delimited).
- `NBKid_shortname_genesymbol.txt`: chapter to gene symbol (tab-delimited).
- `NBKid_shortname_genesymbol_UniProt.txt`: chapter to gene symbol and UniProt accession (tab-delimited).
- `GRshortname_NBKid_genesymbol_dzname.txt`: short name, NBK id, gene symbol and disease name (pipe-delimited, no header).

## License

GeneReviews chapters are owned by the University of Washington. The copyright notice permits reproduction, distribution and translation for noncommercial research purposes only, with credit to the source and copyright, a link to the original material, and compliance with the GeneReviews Copyright Notice and Usage Disclaimer. Excerpts for lab reports and clinic notes are a permitted use.

## Usage

MedGen draws concept names, gene-disease relationships and descriptions from GeneReviews.