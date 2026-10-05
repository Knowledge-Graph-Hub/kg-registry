---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ddbj.nig.ac.jp/contact-ddbj-e.html
  label: DDBJ Center, National Institute of Genetics
creation_date: '2026-10-05T00:00:00Z'
description: The DNA Data Bank of Japan (DDBJ), run by the Bioinformation and DDBJ
  Center (BioData Science Initiative) of the National Institute of Genetics in Mishima,
  Japan, is one of the three members of the International Nucleotide Sequence Database
  Collaboration (INSDC), together with NCBI GenBank and EMBL-EBI ENA. It collects,
  archives and exchanges annotated nucleotide sequences (DDBJ), raw sequencing reads
  (DDBJ Sequence Read Archive, DRA), BioProject and BioSample metadata, and controlled-access
  human genotype and phenotype data (Japanese Genotype-phenotype Archive, JGA).
domains:
- genomics
homepage_url: https://www.ddbj.nig.ac.jp/
id: ddbj
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ddbj.nig.ac.jp/policies-e.html
  label: DDBJ (NIG BioData Science Initiative) Terms of Use; INSDC data are unrestricted-access
    and may be freely used, redistributed and modified, while JGA data are controlled-access
    under the NBDC Human Data Sharing Guidelines
name: DNA Data Bank of Japan (DDBJ)
products:
- category: GraphicalInterface
  description: DDBJ web portal with news, submission guides and links to the DDBJ,
    DRA, BioProject, BioSample, JGA, GEA and MetaboBank services.
  format: http
  id: ddbj.portal
  name: DDBJ Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  product_url: https://www.ddbj.nig.ac.jp/
- category: GraphicalInterface
  description: Search interface for metadata across DDBJ, DRA, BioProject, BioSample
    and JGA (study, dataset and policy records), with entry pages linking related
    records.
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
  description: getentry, a web service and URL-based API for retrieving INSDC nucleotide
    entries, translated protein entries and related records by accession number, in
    flat file, FASTA and other formats.
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
  description: ARSA (All-round Retrieval of Sequence and Annotation), a keyword and
    field search over INSDC nucleotide sequence records held at DDBJ.
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
  description: Release flat files of the DDBJ nucleotide sequence database (division
    files such as ddbjbct*.seq.gz, accession indexes and file lists for release 143
    at time of curation), plus TLS, TSA and WGS file lists.
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
  description: DDBJ Sequence Read Archive (DRA) download area with FASTQ, SRA and
    SRA Lite files and run metadata for high-throughput sequencing submissions, exchanged
    with NCBI SRA and ENA.
  format: mixed
  id: ddbj.dra
  name: DDBJ Sequence Read Archive (DRA)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: ena
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/dra/
- category: Product
  description: BioProject XML records (all INSDC projects and the DDBJ-registered
    subset) with a summary file and XML schema.
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
  description: BioSample XML records (all INSDC samples and the DDBJ-registered subset)
    with a summary file and XML schema.
  format: xml
  id: ddbj.biosample
  name: DDBJ BioSample
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/biosample/
- category: Product
  description: Japanese Genotype-phenotype Archive (JGA), a controlled-access archive
    for individual-level human genotype and phenotype data. Data use requires an application
    reviewed by the Database Center for Life Science (DBCLS); study, dataset and policy
    summaries are public in DDBJ Search.
  format: http
  id: ddbj.jga
  is_public: false
  name: Japanese Genotype-phenotype Archive (JGA)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  product_url: https://www.ddbj.nig.ac.jp/jga/index-e.html
- category: GraphProduct
  compression: gzip
  description: DDBJ-LD, RDF (Turtle) versions of DDBJ nucleotide sequence releases
    and BioSample records, with current and archived releases, ontologies and a Virtuoso
    database dump.
  format: ttl
  id: ddbj.rdf
  name: DDBJ-LD RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  product_url: https://ddbj.nig.ac.jp/public/rdf/
- category: DocumentationProduct
  description: Index of DDBJ services with links to help pages for submission, search
    and retrieval tools.
  format: http
  id: ddbj.docs
  name: DDBJ Services and Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  product_url: https://www.ddbj.nig.ac.jp/services/index-e.html
- category: ProgrammingInterface
  connection_url: http://togows.org/
  description: REST API for retrieving entries, or individual fields of entries, from
    UniProt, ENA, DDBJ, NCBI Nucleotide, NCBI Gene, dbSNP, PubMed, PDB and KEGG (entry
    endpoint), and for searching UniProt, ENA, NCBI Nucleotide, dbSNP, PubMed, OMIM
    and PDB (search endpoint), with JSON, Turtle, XML, GFF or FASTA output.
  format: http
  id: togows.rest-api
  is_public: true
  name: TogoWS REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: togows
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: ddbj
  product_url: http://togows.org/help/
  warnings:
  - On 2026-10-03 PDB entry retrieval returned empty results, PDB search returned
    HTTP 500 and dbSNP entry retrieval returned HTTP 404; the other databases tested
    (UniProt, ENA, DDBJ, NCBI Nucleotide, NCBI Gene, PubMed, KEGG, OMIM search) responded
    normally.
- category: ProgrammingInterface
  description: SPARQL endpoint for the DDBJ RDF dataset.
  format: http
  id: rdf-portal.sparql.ddbj
  name: RDF Portal DDBJ SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: ddbj
  product_url: https://rdfportal.org/ddbj/sparql
publications:
- authors:
  - Takeshi Ara
  - Yuichi Kodama
  - Takatomo Fujisawa
  - Takehide Kosuge
  - Kyungbum Lee
  - Jun Mashima
  - Osamu Ogasawara
  - Yasuhiro Tanizawa
  - Tomoya Tanjo
  - Yasukazu Nakamura
  - Masanori Arita
  doi: 10.1093/nar/gkaf1273
  id: doi:10.1093/nar/gkaf1273
  journal: Nucleic Acids Research
  preferred: true
  title: 'DDBJ update in 2025: system integration for global data-sharing including
    pathogen surveillance'
  year: '2026'
- authors:
  - Yuichi Kodama
  - Takeshi Ara
  - Asami Fukuda
  - Toshiaki Tokimatsu
  - Jun Mashima
  - Takehide Kosuge
  - Yasuhiro Tanizawa
  - Tomoya Tanjo
  - Osamu Ogasawara
  - Takatomo Fujisawa
  - Yasukazu Nakamura
  - Masanori Arita
  doi: 10.1093/nar/gkae882
  id: doi:10.1093/nar/gkae882
  journal: Nucleic Acids Research
  title: 'DDBJ update in 2024: the DDBJ Group Cloud service for sharing pre-publication
    data'
  year: '2025'
synonyms:
- DDBJ
- DNA Data Bank of Japan
---
# DNA Data Bank of Japan (DDBJ)

DDBJ is the Japanese member of the International Nucleotide Sequence Database Collaboration (INSDC), operated by the National Institute of Genetics. Records submitted to DDBJ, NCBI GenBank and EMBL-EBI ENA are exchanged daily, so DDBJ releases cover the full INSDC nucleotide collection.

Services include the DDBJ nucleotide sequence database, the DDBJ Sequence Read Archive (DRA), BioProject, BioSample, and the controlled-access Japanese Genotype-phenotype Archive (JGA). Records can be searched through [DDBJ Search](https://ddbj.nig.ac.jp/search) and ARSA, retrieved by accession through getentry, and downloaded in bulk from the [public file area](https://ddbj.nig.ac.jp/public/), including RDF versions (DDBJ-LD).

## License

Under the [Terms of Use](https://www.ddbj.nig.ac.jp/policies-e.html), unrestricted-access data (including INSDC data) may be freely used, redistributed and modified, subject to any third-party rights the user must check. JGA data are controlled-access and must be used under the NBDC Human Data Sharing Guidelines. Website content is CC BY 4.0 unless stated otherwise.