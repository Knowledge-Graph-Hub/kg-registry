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
    value: https://mygene.info/about/
  label: Su and Wu Labs, Scripps Research
creation_date: '2026-10-04T00:00:00Z'
description: MyGene.info is a BioThings web service from the Su and Wu labs at Scripps
  Research that serves gene annotations aggregated from about 30 sources, including
  NCBI Gene, Ensembl, UniProt, RefSeq, Gene Ontology, Reactome, WikiPathways, KEGG,
  PANTHER, InterPro, ChEMBL, PharmGKB, ClinGen and the Alliance of Genome Resources,
  through a fast query and annotation API. The build of 2026-09-22 covered about 94
  million genes from about 54,000 species. It is one of the knowledge sources of the
  Translator Service Provider KP.
domains:
- genomics
- biomedical
homepage_url: https://mygene.info/
id: mygene
infores_id: mygene-info
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0
name: MyGene.info
products:
- category: ProgrammingInterface
  description: MyGene.info REST API (v3) for gene query and annotation retrieval by
    Entrez or Ensembl gene id, with batch POST queries and field filtering. Returns
    JSON documents merged from the integrated sources.
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
- category: Product
  description: JSON metadata for the current MyGene.info build, with build date and
    version, gene and species counts, and the version, license and download URL of
    each integrated source.
  format: json
  id: mygene.metadata
  name: MyGene.info Build Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  product_url: https://mygene.info/v3/metadata
- category: DocumentationProduct
  description: MyGene.info documentation, covering the gene query and annotation services,
    the available fields, data sources and client libraries.
  format: http
  id: mygene.docs
  name: MyGene.info Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  product_url: https://docs.mygene.info/en/latest/
- category: Product
  description: mygene, the Python client for the MyGene.info API, distributed on PyPI
    (version 3.2.2 when checked on 2026-10-04).
  format: python
  id: mygene.python
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: MyGene.info Python Client
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  product_url: https://pypi.org/project/mygene/
  repository: https://github.com/biothings/mygene.py
- category: ProcessProduct
  description: Source code of the MyGene.info web service and its data plugins, built
    with the BioThings SDK.
  format: python
  id: mygene.code
  name: MyGene.info Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:wasInfluencedBy
    source: biothings
  product_url: https://github.com/biothings/mygene.info
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
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: mychem
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
- authors:
  - Chunlei Wu
  - Ian MacLeod
  - Andrew I. Su
  doi: 10.1093/nar/gks1114
  id: doi:10.1093/nar/gks1114
  journal: Nucleic Acids Research
  title: 'BioGPS and MyGene.info: organizing online, gene-centric information'
  year: '2013'
repository: https://github.com/biothings/mygene.info
synonyms:
- MyGene
- mygene.info
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
- NCBITaxon:7227
- NCBITaxon:6239
- NCBITaxon:7955
- NCBITaxon:3702
- NCBITaxon:8364
- NCBITaxon:9823
---
# MyGene.info

MyGene.info is a gene annotation web service built with the [BioThings SDK](https://biothings.io/) by the Su and Wu labs at Scripps Research. It merges gene records from NCBI Gene, Ensembl, UniProt and about 30 other sources into one JSON document per gene, keyed by Entrez or Ensembl gene id.

## Access

- **Query service**: `https://mygene.info/v3/query?q=<term>` searches genes by symbol, name, id or annotation fields.
- **Annotation service**: `https://mygene.info/v3/gene/<id>` returns the merged record for one gene. Both accept batch POST requests.
- **Metadata**: `https://mygene.info/v3/metadata` lists the build version and each source's version.
- **Clients**: the `mygene` Python package and the `mygene` R/Bioconductor package.

The API is registered in [SmartAPI](https://smart-api.info/ui/59dce17363dce279d389100834e43648) and is served as part of the Translator Service Provider KP (`service-kp`) through BioThings Explorer.

## Coverage

The 2026-09-22 build listed about 94 million genes over about 54,000 species. Nine species have common names in the API (human, mouse, rat, fruit fly, nematode, zebrafish, thale cress, frog and pig).

## Licensing

The service code is Apache-2.0. Use of the website falls under the Scripps Research terms of use, and each integrated source keeps its own license, which the metadata endpoint reports where known (for example CC BY 4.0 for Alliance orthology and ODbL for ExAC).