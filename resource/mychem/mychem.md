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
description: MyChem.info is a BioThings web service from the Su and Wu labs at Scripps
  Research that serves chemical and drug annotations aggregated from sources such
  as ChEMBL, DrugBank, DrugCentral, ChEBI, PubChem, UNII and GSRS, NDC, UMLS, PharmGKB,
  Guide to Pharmacology, UniChem, AEOLUS and SIDER. Records are keyed mainly by InChIKey
  and are served through a REST query API. The build of 2026-08-17 held about 198
  million chemical records.
domains:
- drug discovery
- pharmacology
- chemistry and biochemistry
homepage_url: https://mychem.info/
id: mychem
infores_id: mychem-info
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0
name: MyChem.info
products:
- category: ProgrammingInterface
  description: MyChem.info REST API (v1) for querying chemical and drug annotation
    records by keyword, field or identifier (InChIKey, ChEMBL, DrugBank, PubChem,
    ChEBI and UNII IDs), with batch queries over POST. Data in each record keep the
    license of their original source.
  format: json
  id: mychem.api
  infores_id: mychem-info
  name: MyChem.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: sider
  product_url: https://mychem.info/v1/query
- category: Product
  description: JSON metadata for the current MyChem.info build, listing each data
    source with its version, license and license URL, plus record counts.
  format: json
  id: mychem.metadata
  name: MyChem.info Build Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  product_url: https://mychem.info/v1/metadata
- category: DocumentationProduct
  description: MyChem.info documentation, covering the query syntax, the chem annotation
    endpoint, available fields and data sources.
  format: http
  id: mychem.docs
  name: MyChem.info Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  product_url: https://docs.mychem.info/
- category: Product
  description: biothings_client, the Python client package for the BioThings APIs,
    including MyChem.info.
  format: python
  id: mychem.python-client
  name: biothings_client Python Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  product_url: https://pypi.org/project/biothings-client/
  repository: https://github.com/biothings/biothings_client.py
- category: ProcessProduct
  description: Source code for the MyChem.info data parsers and web service, built
    with the BioThings SDK.
  format: python
  id: mychem.code
  name: MyChem.info Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  product_url: https://github.com/biothings/mychem.info
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
  - Chunlei Wu
  doi: 10.1093/bioinformatics/btac017
  id: doi:10.1093/bioinformatics/btac017
  journal: Bioinformatics
  preferred: true
  title: 'BioThings SDK: a toolkit for building high-performance data APIs in biomedical
    research'
  year: '2022'
repository: https://github.com/biothings/mychem.info
synonyms:
- MyChem
- mychem.info
---
# MyChem.info

MyChem.info is one of the BioThings APIs built by the Su and Wu labs at Scripps Research. It merges chemical and drug annotations from many sources into one JSON document per chemical, keyed mainly by InChIKey, and serves them through a REST API. It is one of the knowledge provider APIs of the NCATS Translator Service Provider team, exposed to Translator through BioThings Explorer.

## Data sources

The build of 2026-08-17 (`/v1/metadata`) lists DrugBank (open data subset), GSRS/ginas, ChEBI, DrugCentral, UMLS, the FDA NDC directory, ChEMBL, UNII, PharmGKB, Guide to Pharmacology, AEOLUS, UniChem, FDA orphan drug designations, PubChem and SIDER. Each source keeps its own license, which the metadata endpoint reports. Several are share-alike or non-commercial (for example DrugCentral, PharmGKB and Guide to Pharmacology under CC BY-SA 4.0, and SIDER under CC BY-NC-SA 3.0).

## Access

- Query: `https://mychem.info/v1/query?q=<term>`
- Annotation by ID: `https://mychem.info/v1/chem/<InChIKey>`
- Python: `biothings_client.get_client("chem")`

MyChem.info has no paper of its own. The BioThings SDK paper describes the framework it is built on.