---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pirmail@georgetown.edu
  - contact_type: url
    value: https://proteininformationresource.org/pirwww/support/contact.shtml
  label: Protein Information Resource
creation_date: '2026-05-20T00:00:00Z'
description: Protein Information Resource (PIR) is an integrated public bioinformatics
  resource that supports genomic, proteomic, and systems biology research through
  protein databases, annotation resources, search tools, and downloadable reference
  datasets.
domains:
- proteomics
- genomics
- systems biology
homepage_url: https://proteininformationresource.org/
id: pir
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://proteininformationresource.org/pirwww/about/linkpir.shtml
  label: PIR Terms of Use
name: Protein Information Resource
products:
- category: GraphicalInterface
  description: Main PIR web interface for navigating databases, search tools, and
    supporting resources.
  format: http
  id: pir.portal
  name: PIR Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  product_url: https://proteininformationresource.org/
- category: Product
  description: PIR download center linking to the anonymous FTP server, which holds releases
    of iProClass, PIRSF, and PRO along with ID mapping, Reference Proteome, and other PIR-maintained
    files. The FTP ontology/pro_obo directory is historical (last changed in 2020).
  format: http
  id: pir.downloads
  name: PIR Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: iproclass
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: pr
  product_url: https://proteininformationresource.org/pirwww/download/
- category: Product
  description: Anonymous FTP directory of PIR databases, including iproclass, pirsf, idmapping,
    rps (Reference Proteomes), iprolink, and ontology.
  format: mixed
  id: pir.ftp
  name: PIR FTP Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: iproclass
  - relation_type: prov:hadPrimarySource
    source: pirsf
  product_url: ftp://ftp.proteininformationresource.org/databases/
- category: MappingProduct
  compression: gzip
  description: Tab-delimited table mapping UniProtKB accessions to identifiers in other databases,
    including Entrez Gene, RefSeq, PDB, Pfam, GO, PIRSF, UniRef, UniParc, NCBI Taxonomy, OMIM,
    Ensembl, PubMed, and EMBL/GenBank/DDBJ. The file is dated 2024-05-29.
  format: tsv
  id: pir.idmapping
  name: PIR ID Mapping Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: uniref
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: ena
  product_file_size: 12465900679
  product_url: ftp://ftp.proteininformationresource.org/databases/idmapping/idmapping.tb.gz
- category: GraphicalInterface
  description: Web form for mapping a batch of identifiers between UniProtKB and other databases
    through iProClass.
  format: http
  id: pir.idmapping.web
  name: PIR ID Mapping Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: iproclass
  product_url: https://proteininformationresource.org/pirwww/search/idmapping.shtml
- category: Product
  description: Algorithmically determined Reference Proteomes (formerly Representative Proteomes),
    each chosen from a group of similar proteomes by co-membership in UniRef50 clusters. Group
    files (TXT) and sequence files (FASTA) are available at 75%, 55%, 35%, and 15% co-membership
    cutoffs, with browsing and BLAST search. The page lists release 2024_04 (2024-07-24).
  format: mixed
  id: pir.reference-proteomes
  latest_version: '2024_04'
  name: PIR Reference Proteomes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uniref
  product_url: https://proteininformationresource.org/rps/
- category: GraphicalInterface
  description: Web application and RESTful service for finding all occurrences of a query peptide
    in UniProtKB sequences, including isoforms.
  format: http
  id: pir.peptide-match
  name: Peptide Match
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://proteininformationresource.org/peptidematch/
  warnings:
  - The service returned HTTP 503 when checked on 2026-11-24.
- category: GraphProduct
  description: PIR compound exact match edges
  format: csv
  id: prokn.pir.compound.skos_exact_match.compound.edges
  name: ProKN PIR Compound Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 100170454
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Compound.SKOS_EXACT_MATCH.Compound.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impchumangene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4832630
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impc_gene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4832630
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: PIR IMPC human gene orthologous to protein edges
  format: csv
  id: prokn.pir.impchumangene.orthologous_to.protein.edges
  name: ProKN PIR Human Gene to Protein Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18025933
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.Protein.edges.csv
- category: GraphProduct
  description: PIR IMPC mouse gene has gene product protein edges
  format: csv
  id: prokn.pir.impcmousegene.has_gene_product.protein.edges
  name: ProKN PIR Mouse Gene Product Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 19465205
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcMouseGene.BIOLINK_HAS_GENE_PRODUCT.Protein.edges.csv
- category: ProgrammingInterface
  description: MyGene.info REST API (v3) for gene query and annotation retrieval by Entrez
    or Ensembl gene id, with batch POST queries and field filtering. Returns JSON documents
    merged from the integrated sources.
  format: http
  id: mygene.api
  infores_id: mygene-info
  name: MyGene.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://mygene.info/v3/api
- category: GraphicalInterface
  description: Entrez search interface for NCBI Protein sequence records, with links
    to Gene, Nucleotide, Structure, and Conserved Domains.
  format: http
  id: ncbi-protein.web
  name: NCBI Protein Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi-protein
  - relation_type: prov:hadPrimarySource
    source: genbank
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://www.ncbi.nlm.nih.gov/protein/
- category: GraphicalInterface
  description: Web interface for querying and downloading microRNA relations mined
    from Medline abstracts.
  format: http
  id: mirtex.portal
  name: miRTex Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtex
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://proteininformationresource.org/mirtex/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: pir
  warnings:
  - The site returned HTTP 503 when checked on 2026-11-24.
publications:
- authors:
  - Wu CH
  - Yeh LS
  - Huang H
  - Arminski L
  - Castro-Alvear J
  - Chen Y
  - Hu Z
  - Kourtesis P
  - Ledley RS
  - Suzek BE
  - Vinayaka CR
  - Zhang J
  - Barker WC
  doi: 10.1093/nar/gkg040
  id: https://www.ncbi.nlm.nih.gov/pubmed/12520019
  journal: Nucleic Acids Res
  preferred: true
  title: The Protein Information Resource
  year: '2003'
- authors:
  - Chuming Chen
  - Darren A. Natale
  - Robert D. Finn
  - Hongzhan Huang
  - Jian Zhang
  - Cathy H. Wu
  - Raja Mazumder
  doi: 10.1371/journal.pone.0018910
  id: doi:10.1371/journal.pone.0018910
  journal: PLoS ONE
  title: 'Representative Proteomes: A Stable, Scalable and Unbiased Proteome Set for Sequence
    Analysis and Functional Annotation'
  year: '2011'
- authors:
  - Chuming Chen
  - Zhiwen Li
  - Hongzhan Huang
  - Baris E. Suzek
  - Cathy H. Wu
  - UniProt Consortium
  doi: 10.1093/bioinformatics/btt484
  id: doi:10.1093/bioinformatics/btt484
  journal: Bioinformatics
  title: A fast Peptide Match service for UniProt Knowledgebase
  year: '2013'
rrid: SCR_002837
synonyms:
- PIR
- Protein Information Resource
---

# Protein Information Resource

PIR is a long-running public protein bioinformatics resource that historically contributed
core sequence and annotation infrastructure to UniProt and continues to maintain protein-centric
data integration and analysis resources. Its public site exposes databases, search tools,
downloads, and supporting documentation for protein annotation workflows.

The ProKN products on this page are derived graph views built from PIR-linked protein mappings
and cross-resource integration, including alignments to IMPC-derived gene and orthology data.

PIR was established in 1984 by the National Biomedical Research Foundation, following the Atlas of
Protein Sequence and Structure compiled under Margaret Dayhoff (1965-1978). It is now run from the
University of Delaware and Georgetown University Medical Center. PIR also hosts or links to
iPTMnet, the Protein Ontology (PRO), and the RLIMS-P and miRTex text mining systems, which have
their own entries here.
