---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cwu@scripps.edu
  - contact_type: github
    value: newgene
  label: Chunlei Wu
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biothings.io/
  label: BioThings team, Su and Wu labs, Scripps Research
creation_date: '2026-10-04T00:00:00Z'
description: MyDisease.info is a BioThings web service from the Su and Wu labs at
  Scripps Research that serves disease annotations aggregated from Mondo, the Human
  Disease Ontology, HPO disease annotations, CTD and UMLS. Records are keyed mainly
  by Mondo identifiers and are served through a REST query API. The build of 2026-09-01
  held about 353,000 disease records.
domains:
- biomedical
- clinical
homepage_url: https://mydisease.info/
id: mydisease
infores_id: mydisease-info
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: ctd, umls.'
  id: https://ctdbase.org/about/legal.jsp
  inferred_from:
  - ctd
  - umls
  label: Custom
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
name: MyDisease.info
products:
- category: ProgrammingInterface
  description: MyDisease.info REST API (v1) for querying disease annotation records
    by keyword, field or identifier (Mondo, DOID, OMIM, Orphanet, MeSH and UMLS IDs),
    with batch queries over POST. Data in each record keep the license of their original
    source.
  format: json
  id: mydisease.api
  infores_id: mydisease-info
  name: MyDisease.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://mydisease.info/v1/query
- category: Product
  description: JSON metadata for the current MyDisease.info build, listing each data
    source with its version, license URL and record counts.
  format: json
  id: mydisease.metadata
  name: MyDisease.info Build Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mydisease
  product_url: https://mydisease.info/v1/metadata
- category: DocumentationProduct
  description: MyDisease.info documentation, covering the query syntax, the disease
    annotation endpoint, available fields and data sources.
  format: http
  id: mydisease.docs
  name: MyDisease.info Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mydisease
  product_url: https://docs.mydisease.info/
- category: ProcessProduct
  description: Source code for the MyDisease.info data parsers and web service, built
    with the BioThings SDK.
  format: python
  id: mydisease.code
  name: MyDisease.info Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:wasInfluencedBy
    source: biothings
  product_url: https://github.com/biothings/mydisease.info
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
publications:
- authors:
  - Sebastien Lelong
  - Xinghua Zhou
  - Cyrus Afrasiabi
  - Zhongchao Qian
  - Marco Alvarado Cano
  - Ginger Tsueng
  - Jiwen Xin
  - Julia Mullen
  - Yao Yao
  - Ricardo Avila
  - Greg Taylor
  - Andrew I Su
  - Chunlei Wu
  doi: 10.1093/bioinformatics/btac017
  id: doi:10.1093/bioinformatics/btac017
  journal: Bioinformatics
  preferred: true
  title: 'BioThings SDK: a toolkit for building high-performance data APIs in biomedical
    research'
  year: '2022'
repository: https://github.com/biothings/mydisease.info
synonyms:
- MyDisease
- mydisease.info
taxon:
- NCBITaxon:9606
---
# MyDisease.info

MyDisease.info is one of the BioThings APIs built and hosted by the Su and Wu labs at Scripps Research. It merges disease records from several sources into one JSON document per disease, keyed mainly by Mondo identifiers, and serves them through a REST API with full-text and fielded queries.

## Data Sources

The build of 2026-09-01 lists five sources in its metadata:

| Source | Version | Records |
|---|---|---|
| Mondo | 2026-09-01 | 36,015 |
| UMLS | 2026-05-04 | 337,047 |
| HPO disease annotations | 2026-06-23 | 12,918 |
| Human Disease Ontology | 2026-08-31 | 12,164 |
| CTD | 2026-08-28 | 6,522 |

Earlier builds also included DisGeNET, but the current metadata does not list it.

## Access

- API: `https://mydisease.info/v1/query` and `https://mydisease.info/v1/disease/<id>`.
- Metadata: `https://mydisease.info/v1/metadata`.
- Python access is through the shared `biothings_client` package.

MyDisease.info is also exposed to the NCATS Biomedical Data Translator through the Service Provider TRAPI endpoint.

## License

The repository declares no license. Data in each record keep the license of their original source, and the metadata links the UMLS and Disease Ontology license terms.