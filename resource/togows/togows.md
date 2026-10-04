---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://dbcls.rois.ac.jp/en/contact
  label: Database Center for Life Science (DBCLS)
- category: Individual
  contact_details:
  - contact_type: url
    value: http://togows.org/
  label: Toshiaki Katayama
creation_date: '2026-10-03T00:00:00Z'
description: TogoWS is a set of uniform REST web services from the Database Center
  for Life Science (DBCLS, Japan) for retrieving, searching and converting entries
  from major bioinformatics databases, including UniProt, ENA, DDBJ, NCBI Nucleotide,
  NCBI Gene, dbSNP, PubMed, PDB, OMIM and KEGG, plus a REST API over the UCSC Genome
  Browser databases. Entries are fetched from the upstream databases on request and
  returned in formats such as JSON, Turtle, XML, GFF and FASTA. It was originally
  built to unify the REST and SOAP services of NCBI, EBI, DDBJ, PDB and KEGG.
domains:
- genomics
- biomedical
- software
- information technology
homepage_url: http://togows.org/
id: togows
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: kegg. Not accounted for, no known license:
    ena, pdb.'
  id: https://www.kegg.jp/feedback/copyright.html
  inferred_from:
  - kegg
  label: By request
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - ena
  - pdb
name: TogoWS
products:
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
  product_url: http://togows.org/help/
  warnings:
  - On 2026-10-03 PDB entry retrieval returned empty results, PDB search returned
    HTTP 500 and dbSNP entry retrieval returned HTTP 404; the other databases tested
    (UniProt, ENA, DDBJ, NCBI Nucleotide, NCBI Gene, PubMed, KEGG, OMIM search) responded
    normally.
- category: ProgrammingInterface
  connection_url: http://togows.org/api/ucsc
  description: REST API over the public UCSC Genome Browser MySQL databases, for listing
    genome assemblies, tables and columns, querying table rows by column values, and
    retrieving genomic sequence ranges.
  format: http
  id: togows.ucsc-api
  is_public: true
  name: TogoWS UCSC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: togows
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: http://togows.org/help/
- category: ProgrammingInterface
  connection_url: http://togows.org/convert/
  description: REST service (HTTP POST) for converting between sequence, alignment
    and annotation formats such as GenBank, EMBL/ENA, DDBJ, FASTA, GFF and BLAST or
    HMMER output, and RDF serializations.
  format: http
  id: togows.convert
  is_public: true
  name: TogoWS Format Conversion
  original_source:
  - relation_type: prov:hadPrimarySource
    source: togows
  product_url: http://togows.org/help/
- category: GraphicalInterface
  description: KLOCD web interface for searching its drug, chemical, gene expression
    dataset, disease, toxicant, literature, patent and organ-on-chip model sub-databases,
    built from PubMed, PubChem, TogoWS, UniChem, DrugBank, ChEMBL, ClinicalTrials.gov,
    AACT, the European Medicines Agency, CTD, NCBI GEO, openFDA and Disease Ontology,
    among other public sources.
  format: http
  id: klocd.portal
  name: KLOCD Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: klocd
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: togows
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: ema
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: doid
  product_url: http://www.organchip.cn/
publications:
- authors:
  - Toshiaki Katayama
  - Mitsuteru Nakao
  - Toshihisa Takagi
  doi: 10.1093/nar/gkq386
  id: doi:10.1093/nar/gkq386
  journal: Nucleic Acids Research
  preferred: true
  title: 'TogoWS: integrated SOAP and REST APIs for interoperable bioinformatics Web
    services'
  year: '2010'
---
# TogoWS

TogoWS is a set of uniform REST web services from the Database Center for Life Science
(DBCLS, Japan) for retrieving, searching and converting entries from major
bioinformatics databases.

## Services

- **Entry** (`/entry/{database}/{id}[/field][.format]`): retrieves whole entries or
  single fields from UniProt, ENA, DDBJ, NCBI Nucleotide, NCBI Gene, dbSNP, PubMed,
  PDB and KEGG, returned as JSON, Turtle, XML, GFF or FASTA.
- **Search** (`/search/{database}/{query}[/offset,limit]`): searches UniProt, ENA,
  NCBI Nucleotide, dbSNP, PubMed, OMIM and PDB.
- **Convert** (`/convert/{source}.{format}`, HTTP POST): converts between sequence,
  alignment and annotation formats and RDF serializations.
- **UCSC API** (`/api/ucsc/...`): queries the public UCSC Genome Browser MySQL
  databases by assembly, table and column, and retrieves sequence ranges.

TogoWS was originally developed to provide uniform REST services over the public REST
and SOAP services of NCBI, EBI, DDBJ, PDB and KEGG. After most of those SOAP services
were discontinued in 2012, it focused on REST APIs, the UCSC genome databases and
Semantic Web support. The alias http://togows.dbcls.jp/ serves the same site.

## Status

Checked on 2026-10-03. The service responds, and entries are fetched live from the
upstream databases: a PubMed record first published in September 2026 was returned.
UniProt, ENA, DDBJ, NCBI Nucleotide, NCBI Gene, PubMed and KEGG entry retrieval,
UniProt, PubMed and OMIM search, format conversion and the UCSC API all worked. PDB
entry retrieval returned empty results, PDB search returned HTTP 500 and dbSNP entry
retrieval returned HTTP 404. An automated availability monitor
(http://togows.org/monitor/) has monthly reports through 2026-10, but the homepage
still carries a "Copyright 2008-2014" footer and a 2014 maintenance notice, so the
service may receive little active maintenance.

## Contact and License

The homepage directs comments to Toshiaki Katayama and links the DBCLS contact form.
No license is stated; the footer links the Life Science Database policy page
(http://lifesciencedb.jp/lsdb.cgi?lng=en&gg=policy). Data returned are subject to
each upstream database's own terms. No public source repository was found.
