---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://support.nlm.nih.gov/?pagename=guide%3ANONE%3AHomePage%3ANONE
  label: NCBI and NLM Support
creation_date: '2026-02-26T00:00:00Z'
description: The National Center for Biotechnology Information advances science and
  health by providing access to biomedical and genomic information, databases, tools,
  and services.
domains:
- biomedical
- genomics
- literature
homepage_url: https://www.ncbi.nlm.nih.gov/
id: ncbi
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain
name: National Center for Biotechnology Information
products:
- category: GraphicalInterface
  description: NCBI web portal with Entrez search across NCBI literature, sequence,
    gene, protein, genome, variation, taxonomy and chemical databases.
  format: http
  id: ncbi.portal
  name: NCBI Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/
- category: ProgrammingInterface
  connection_url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  description: Entrez Programming Utilities (E-utilities), a set of server-side programs
    (ESearch, EFetch, ESummary, ELink, EInfo and others) providing a URL-based API for
    searching and retrieving records from the Entrez databases. An API key raises the
    request rate limit.
  format: http
  id: ncbi.eutils
  is_public: true
  name: NCBI E-utilities
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- category: ProgrammingInterface
  connection_url: https://api.ncbi.nlm.nih.gov/datasets/v2/
  description: NCBI Datasets v2 REST API for programmatic access to genome, gene, taxonomy,
    virus, and BioSample data and metadata, with companion datasets and dataformat
    command-line tools.
  format: http
  id: ncbi.datasets-api
  is_public: true
  name: NCBI Datasets API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/rest-api/
- category: GraphicalInterface
  description: NCBI Datasets web interface for browsing and downloading genome assemblies,
    gene records and associated sequence, annotation and metadata packages.
  format: http
  id: ncbi.datasets
  name: NCBI Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/datasets/
- category: GraphicalInterface
  description: BLAST (Basic Local Alignment Search Tool) web service for comparing nucleotide
    or protein query sequences against NCBI sequence databases.
  format: http
  id: ncbi.blast
  name: NCBI BLAST
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://blast.ncbi.nlm.nih.gov/Blast.cgi
- category: Product
  description: NCBI FTP site providing bulk downloads for NCBI databases, including GenBank
    and RefSeq sequence releases, genome assemblies, the NCBI Taxonomy dump, gene data
    files, and the PubMed baseline and update files.
  format: mixed
  id: ncbi.ftp
  name: NCBI FTP Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: genbank
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: ncbitaxon
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  product_url: https://ftp.ncbi.nlm.nih.gov/
- category: DataModelProduct
  description: NCBI Genetic Codes tables summarizing translation tables used in GenBank
    and the NCBI taxonomy.
  format: http
  id: ncbi.gc
  name: NCBI Genetic Codes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
- category: Product
  description: Taxonomy crosswalk from GTDB release r220 to NCBI taxonomy (2025-07-28),
    with lineage context, genome counts, and majority-vote agreement fractions.
  format: tsv
  id: metatraits.gtdb2ncbi
  name: GTDB to NCBI Taxonomy Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 2937650
  product_url: https://www.bork.embl.de/~robbani/metatraits/GTDB2NCBI.tsv.gz
- category: Product
  description: Taxonomy crosswalk from NCBI taxonomy (2025-07-28) to GTDB release
    r220, with lineage context, genome counts, and majority-vote agreement fractions.
  format: tsv
  id: metatraits.ncbi2gtdb
  name: NCBI to GTDB Taxonomy Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 2895086
  product_url: https://www.bork.embl.de/~robbani/metatraits/NCBI2GTDB.tsv.gz
- category: Product
  description: Family-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.ncbi.family-summary
  name: metaTraits NCBI Family Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 913932
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_family_summary_no_predictions.tsv.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.ncbi.genus-summary
  name: metaTraits NCBI Genus Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 2431808
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_genus_summary_no_predictions.tsv.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.ncbi.species-summary
  name: metaTraits NCBI Species Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 6523019
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_species_summary_no_predictions.tsv.gz
- category: Product
  description: ncbi.gc Nodes TSV
  format: tsv
  id: obo-db-ingest.ncbi.gc.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 531
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.tsv
- category: Product
  description: ncbi.gc OBO
  format: obo
  id: obo-db-ingest.ncbi.gc.obo
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 1425
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.obo
- category: Product
  description: ncbi.gc OWL
  format: owl
  id: obo-db-ingest.ncbi.gc.owl
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 2223
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.owl
- category: Product
  description: ncbi.gc OBO Graph JSON
  format: json
  id: obo-db-ingest.ncbi.gc.json
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 1886
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.json
- category: MappingProduct
  description: ncbi.gc SSSOM
  format: sssom
  id: obo-db-ingest.ncbi.gc.sssom.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 191
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.sssom.tsv
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
- category: GraphicalInterface
  description: CNGBdb web portal for searching CNSA records and the integrated literature,
    gene, protein, sequence, organism, variation and other sub-databases, which include data
    from NCBI and EBI.
  format: http
  id: cngbdb.portal
  name: CNGBdb Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: ena
  product_url: https://db.cngb.org/
- category: GraphicalInterface
  description: Search interface for metadata across DDBJ, DRA, BioProject, BioSample and JGA
    (study, dataset and policy records), with entry pages linking related records.
  format: http
  id: ddbj.search
  name: DDBJ Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/search
- category: ProgrammingInterface
  connection_url: https://getentry.ddbj.nig.ac.jp/getentry/
  description: getentry, a web service and URL-based API for retrieving INSDC nucleotide entries,
    translated protein entries and related records by accession number, in flat file, FASTA
    and other formats.
  format: http
  id: ddbj.getentry
  is_public: true
  name: DDBJ getentry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://getentry.ddbj.nig.ac.jp/top-e.html
- category: GraphicalInterface
  description: ARSA (All-round Retrieval of Sequence and Annotation), a keyword and field
    search over INSDC nucleotide sequence records held at DDBJ.
  format: http
  id: ddbj.arsa
  name: DDBJ ARSA
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/arsa/
- category: Product
  compression: gzip
  description: Release flat files of the DDBJ nucleotide sequence database (division files
    such as ddbjbct*.seq.gz, accession indexes and file lists for release 143 at time of curation),
    plus TLS, TSA and WGS file lists.
  format: mixed
  id: ddbj.release
  name: DDBJ Release Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/ddbj/
- category: Product
  description: BioProject XML records (all INSDC projects and the DDBJ-registered subset)
    with a summary file and XML schema.
  format: xml
  id: ddbj.bioproject
  name: DDBJ BioProject
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/bioproject/
- category: Product
  compression: gzip
  description: BioSample XML records (all INSDC samples and the DDBJ-registered subset) with
    a summary file and XML schema.
  format: xml
  id: ddbj.biosample
  name: DDBJ BioSample
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/biosample/
- category: GraphicalInterface
  description: The SeqAPASS web application for cross-species comparison of chemical
    protein targets by primary amino acid sequence, functional domain, and individual
    amino acid residue similarity, with protein structure generation in version 8.
    A user account is required.
  format: http
  id: seqapass.app
  is_public: true
  name: SeqAPASS Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: seqapass
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  product_url: https://seqapass.epa.gov/seqapass/
publications:
- authors:
  - Sayers EW
  - Bolton EE
  - Fine AM
  - Kelly C
  - Kim S
  - Landrum M
  - Lathrop S
  - Malheiro A
  - Murphy TD
  - Phan L
  - Pujar S
  - Trawick BW
  - Schneider VA
  - Pruitt KD
  doi: 10.1093/nar/gkaf1060
  id: doi:10.1093/nar/gkaf1060
  journal: Nucleic Acids Research
  preferred: true
  title: Database resources of the National Center for Biotechnology Information in
    2026
  year: '2026'
repository: https://github.com/ncbi
rrid: SCR_006472
synonyms:
- NCBI
warnings:
- Some content served by NCBI, including PubMed Central articles, Bookshelf content,
  OMIM and parts of PubChem, may be protected by copyright held by third parties; NCBI
  places no restrictions on its molecular data, but submitters may claim rights to
  some records.
---
# National Center for Biotechnology Information

The National Center for Biotechnology Information (NCBI) is a division of the U.S. National Library of Medicine (NLM) at the National Institutes of Health. It was established by legislation on November 4, 1988, as a national resource for molecular biology information, and it builds and maintains public databases, conducts research in computational biology, and develops software tools for analyzing genomic and biomedical data.

## Databases and services

NCBI hosts several dozen interlinked databases searchable through the Entrez system. These cover literature (PubMed, PubMed Central, Bookshelf), nucleotide and protein sequences (GenBank, RefSeq), genomes and assemblies, genes (Gene), variation (dbSNP, dbVar, ClinVar), taxonomy (NCBI Taxonomy), sequencing reads (SRA), study and sample metadata (BioProject, BioSample), genotype-phenotype studies (dbGaP), and chemicals (PubChem). Analysis services include BLAST for sequence similarity search. NCBI also maintains reference tables such as the Genetic Codes used to assign translation tables to GenBank coding sequences.

## Access

- **Web**: the NCBI portal and per-database search pages.
- **APIs**: the Entrez Programming Utilities (E-utilities) for search and retrieval across Entrez databases, and the NCBI Datasets v2 REST API with the `datasets` and `dataformat` command-line tools for genome, gene, taxonomy and virus data.
- **Bulk downloads**: the NCBI FTP site (https://ftp.ncbi.nlm.nih.gov/) distributes full releases and dumps of many databases.

NCBI publishes an annual overview of its resources in the *Nucleic Acids Research* database issue. Source code for many NCBI tools is available from the NCBI GitHub organization.

## Usage terms

Information created by or for the U.S. government on NCBI web pages is in the public domain, and NCBI places no restrictions on the use or distribution of its molecular data. Some resources incorporate third-party copyrighted material (for example PMC, Bookshelf, OMIM and PubChem), and users are expected to follow the terms of the copyright holders.
