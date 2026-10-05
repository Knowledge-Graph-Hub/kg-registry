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
    value: https://myvariant.info/
  label: Su and Wu Labs, Scripps Research
creation_date: '2026-10-04T00:00:00Z'
description: MyVariant.info is a BioThings web service from the Su and Wu labs at
  Scripps Research that serves human genetic variant annotations aggregated from about
  20 sources, including dbSNP, ClinVar, gnomAD, ExAC, dbNSFP, CADD, CIViC, COSMIC,
  DoCM, the Cancer Genome Interpreter, the GWAS Catalog and SnpEff predictions, through
  a fast query and annotation API keyed on HGVS identifiers. The build of 2025-06-24
  held about 1.51 billion variant documents. It is one of the knowledge sources of
  the Translator Service Provider KP.
domains:
- genomics
- genetic variation
- clinical
- biomedical
homepage_url: https://myvariant.info/
id: myvariant
infores_id: myvariant-info
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0
name: MyVariant.info
products:
- category: ProgrammingInterface
  description: MyVariant.info REST API (v1) for variant query and annotation retrieval
    by HGVS id or rsid, with batch POST queries and field filtering. Returns JSON
    documents merged from the integrated sources, on hg19 and hg38.
  format: http
  id: myvariant.api
  infores_id: myvariant-info
  name: MyVariant.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myvariant
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: docm
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snpeff
  product_url: https://myvariant.info/v1/query
- category: Product
  description: JSON metadata for the current MyVariant.info build, with build date
    and version, variant counts per assembly, and the version, license and URL of
    each integrated source.
  format: json
  id: myvariant.metadata
  name: MyVariant.info Build Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://myvariant.info/v1/metadata
- category: DocumentationProduct
  description: MyVariant.info documentation, covering the variant query and annotation
    services, HGVS identifiers, the available fields, data sources and client libraries.
  format: http
  id: myvariant.docs
  name: MyVariant.info Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://docs.myvariant.info/en/latest/
- category: Product
  description: myvariant, the Python client for the MyVariant.info API (version 1.0.0
    on PyPI), with helpers for querying variants and building HGVS ids from VCF files.
  format: python
  id: myvariant.python
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD
  name: myvariant Python Client
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://pypi.org/project/myvariant/
  repository: https://github.com/biothings/myvariant.py
- category: ProcessProduct
  description: Source code for the MyVariant.info service, including the BioThings
    data plugins and parsers that build the variant index.
  format: python
  id: myvariant.code
  name: MyVariant.info Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myvariant
  - relation_type: prov:wasInfluencedBy
    source: biothings
  product_url: https://github.com/biothings/myvariant.info
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
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
publications:
- authors:
  - Jiwen Xin
  - Adam Mark
  - Cyrus Afrasiabi
  - Ginger Tsueng
  - Moritz Juchler
  - Nikhil Gopal
  - Gregory S. Stupp
  - Timothy E. Putman
  - Benjamin J. Ainscough
  - Obi L. Griffith
  - Ali Torkamani
  - Patricia L. Whetzel
  - Christopher J. Mungall
  - Sean D. Mooney
  - Andrew I. Su
  - Chunlei Wu
  doi: 10.1186/s13059-016-0953-9
  id: doi:10.1186/s13059-016-0953-9
  journal: Genome Biology
  preferred: true
  title: High-performance web services for querying gene and variant annotation
  year: '2016'
repository: https://github.com/biothings/myvariant.info
synonyms:
- MyVariant
- myvariant-info
taxon:
- NCBITaxon:9606
---
# MyVariant.info

MyVariant.info is a BioThings API that merges human variant annotations from many sources into one JSON document per variant, keyed on its HGVS genomic id (for example `chr7:g.140453134T>C`). It supports full-text style queries, batch lookups by id or rsid, and both the hg19 and hg38 assemblies.

## Sources

The 2025-06-24 build metadata lists these sources: dbSNP (156), ClinVar (2025-05), gnomAD (2.1.1), ExAC (0.3.1), dbNSFP (4.8a), CADD, CIViC, COSMIC (68), DoCM, the Cancer Genome Interpreter, the GWAS Catalog, SnpEff (4.3k), the NHLBI Exome Variant Server, Geno2MP, EMVClass, GRASP, Wellderly, SNPedia and MutDB. Sources that have KG-Registry pages are cited on the API product. Each source keeps its own license (gnomAD and ExAC are ODbL, SNPedia is CC BY-NC-SA). The Apache-2.0 license on this page covers the service code only.

## Access

- API: `https://myvariant.info/v1/query` and `https://myvariant.info/v1/variant/<hgvs id>`
- Build metadata: `https://myvariant.info/v1/metadata`
- Python client: `pip install myvariant`

MyVariant.info is also exposed to the NCATS Biomedical Data Translator through the Service Provider KP's TRAPI endpoint.