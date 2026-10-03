---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: literature@ebi.ac.uk
  - contact_type: url
    value: https://europepmc.org/
  - contact_type: github
    value: EuropePMC
  label: Europe PMC, EMBL-EBI
creation_date: '2026-10-03T00:00:00Z'
description: Europe PMC is an open life sciences literature database run by EMBL-EBI.
  It brings together PubMed abstracts, full-text articles from PubMed Central, author
  manuscripts, preprints, Agricola records, patents, theses and other sources under
  one search, and links publications to research grants, data citations and database
  records. Text-mined annotations of genes and proteins, organisms, diseases, chemicals,
  GO terms, accession numbers and other entity types are served through SciLite and
  the Annotations API. Data are available through the website, REST APIs and bulk
  FTP downloads.
domains:
- literature
- scholarly communication
- natural language processing
- biomedical
- research funding
homepage_url: https://europepmc.org/
id: europepmc
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: arrayexpress, biostudies. Not accounted for,
    no known license: pmc.'
  id: https://www.ebi.ac.uk/about/terms-of-use
  inferred_from:
  - arrayexpress
  - biostudies
  label: EMBL-EBI Terms of Use
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - pmc
name: Europe PMC
products:
- category: GraphicalInterface
  description: Europe PMC website for searching and reading life sciences literature,
    including abstracts, full text, preprints, patents and theses, with SciLite text-mined
    annotations and links to grants, data citations and database records.
  format: http
  id: europepmc.portal
  name: Europe PMC Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://europepmc.org/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  description: REST API for searching Europe PMC and retrieving article metadata,
    abstracts, open access full text (XML), references, citations and database cross-references.
  format: http
  id: europepmc.rest-api
  is_public: true
  name: Europe PMC Articles RESTful API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://www.ebi.ac.uk/europepmc/webservices/rest/
- category: ProgrammingInterface
  description: REST API serving text-mined entity annotations (genes and proteins,
    organisms, diseases, chemicals, GO terms, accession numbers and other types) for
    Europe PMC articles, produced by Europe PMC and community text-mining pipelines.
  format: http
  id: europepmc.annotations-api
  is_public: true
  name: Europe PMC Annotations API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  product_url: https://www.ebi.ac.uk/europepmc/annotations_api/
- category: ProgrammingInterface
  description: REST API (GRIST) for searching research grants from Europe PMC funders
    and the publications linked to them.
  format: http
  id: europepmc.grants-api
  is_public: true
  name: Europe PMC Grants API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  product_url: https://www.ebi.ac.uk/europepmc/GristAPI/rest/
- category: Product
  compression: gzip
  description: Bulk download of the Europe PMC open access full-text subset as gzipped
    JATS XML files grouped by PMCID range.
  format: xml
  id: europepmc.oa-fulltext
  name: Europe PMC Open Access Full Text
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://ftp.ebi.ac.uk/pub/databases/pmc/oa/
- category: MappingProduct
  description: CSV files, one per database, linking Europe PMC articles to accessions
    text-mined from their full text, covering ArrayExpress, BioStudies, ChEBI, Cellosaurus,
    AlphaFold DB, BioProject, BioSample, BRENDA, CATH and others.
  format: csv
  id: europepmc.textmined-terms
  name: Europe PMC Text-Mined Database Accession Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://ftp.ebi.ac.uk/pub/databases/pmc/TextMinedTerms/
- category: Product
  description: Europe PMC FTP root holding author manuscripts, preprints and preprint
    abstracts, PDFs, DOI mappings and lightweight metadata files alongside the open
    access and text-mined term downloads.
  format: mixed
  id: europepmc.ftp
  name: Europe PMC FTP Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  product_url: https://ftp.ebi.ac.uk/pub/databases/pmc/
- category: GraphProduct
  description: Every OnCo record in one JSON file, each with its plain-English summary,
    technical summary, dated facts, relationship fields and source links.
  format: json
  id: onco.all_json
  name: OnCo full corpus (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: onco
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: openalex
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 31490277
  product_url: https://onco.cc/api/v1/all.json
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/biostudies/api/v1/search
  description: REST API returning JSON for searching BioStudies, with per-collection
    search endpoints and per-study metadata and file listings. Covers all collections,
    including supplementary data imported from Europe PMC.
  format: http
  id: biostudies.api
  is_public: true
  name: BioStudies REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: europepmc
  product_url: https://www.ebi.ac.uk/biostudies/api/v1/search
- category: Product
  description: FTP/HTTPS archive of BioStudies study files, organized by accession
    prefix, including Europe PMC supplementary data and ArrayExpress experiment files.
  format: mixed
  id: biostudies.ftp
  name: BioStudies FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://ftp.ebi.ac.uk/pub/databases/biostudies/
publications:
- authors:
  - Summer Rosonovski
  - Maria Levchenko
  - Rajat Bhatnagar
  - Umamageswari Chandrasekaran
  - Lynne Faulk
  - Islam Hassan
  - Matt Jeffryes
  - Syed Irtaza Mubashar
  - Maaly Nassar
  - Madhumiethaa Jayaprabha Palanisamy
  - Michael Parkin
  - Jagadeeswararao Poluru
  - Frances Rogers
  - Shyamasree Saha
  - Mohamed Selim
  - Zunaira Shafique
  - Michele Ide-Smith
  - David Stephenson
  - Santosh Tirunagari
  - Aravind Venkatesan
  - Lijun Xing
  - Melissa Harrison
  doi: 10.1093/nar/gkad1085
  id: doi:10.1093/nar/gkad1085
  journal: Nucleic Acids Research
  preferred: true
  title: Europe PMC in 2023
  year: '2024'
- authors:
  - Christine Ferguson
  - Dayane Araújo
  - Lynne Faulk
  - Yuci Gou
  - Audrey Hamelers
  - Zhan Huang
  - Michele Ide-Smith
  - Maria Levchenko
  - Nikos Marinos
  - Rakesh Nambiar
  - Maaly Nassar
  - Michael Parkin
  - Xingjun Pi
  - Faisal Rahman
  - Frances Rogers
  - Yogmatee Roochun
  - Shyamasree Saha
  - Mohamed Selim
  - Zunaira Shafique
  - Shrey Sharma
  - David Stephenson
  - Francesco Talo'
  - Arthur Thouvenin
  - Santosh Tirunagari
  - Vid Vartak
  - Aravind Venkatesan
  - Xiao Yang
  - Johanna McEntyre
  doi: 10.1093/nar/gkaa994
  id: doi:10.1093/nar/gkaa994
  journal: Nucleic Acids Research
  title: Europe PMC in 2020
  year: '2021'
- authors:
  - Europe PMC Consortium
  doi: 10.1093/nar/gku1061
  id: doi:10.1093/nar/gku1061
  journal: Nucleic Acids Research
  title: 'Europe PMC: a full-text literature database for the life sciences and platform
    for innovation'
  year: '2015'
repository: https://github.com/EuropePMC
synonyms:
- Europe PubMed Central
- EuropePMC
---
# Europe PMC

Europe PMC is an open life sciences literature database run by EMBL-EBI. It brings
together PubMed abstracts, full-text articles from PubMed Central, author manuscripts,
preprints, Agricola records, patents, theses and other sources under one search, and
links publications to research grants, data citations and database records.

On 2026-10-02 its REST API reported 48,993,510 records, including 12,391,054 with full
text, 8,300,807 open access articles and 1,253,235 preprints.

## Text Mining

Text-mined annotations (genes and proteins, organisms, diseases, chemicals, GO terms,
accession numbers and other entity types) come from Europe PMC and community
text-mining pipelines. They are shown through SciLite in the web interface and served
through the Annotations API. Accession numbers mined from full text are also released
as per-database CSV link files on the FTP site.

## Access

- Website: https://europepmc.org/
- Articles REST API: https://www.ebi.ac.uk/europepmc/webservices/rest/
- Annotations API: https://www.ebi.ac.uk/europepmc/annotations_api/
- Grants API: https://www.ebi.ac.uk/europepmc/GristAPI/rest/
- Bulk FTP downloads: https://ftp.ebi.ac.uk/pub/databases/pmc/

## License

There is no single license. Open access articles carry their own licenses (mostly
Creative Commons), and other full text is free to read under publisher copyright.
