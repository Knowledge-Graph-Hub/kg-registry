---
activity_status: inactive
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: xinchen@zju.edu.cn
  label: Xin Chen
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.cls.zju.edu.cn/dcdb/
  label: Department of Bioinformatics, College of Life Sciences, Zhejiang University
creation_date: '2026-06-18T00:00:00Z'
description: DCDB (Drug Combination Database) was a curated database of drug combinations
  developed at the College of Life Sciences, Zhejiang University. For each combination
  it recorded the components, indications, combined activity, possible pharmacodynamic
  and pharmacokinetic interactions between components, and development status; for
  each component drug, its chemical, pharmacological and pharmaceutical properties
  and known molecular targets. Version 1.0 (2009) held 499 combinations involving
  485 drugs; version 2.0 (2014) held 1363 combinations (including 237 unsuccessful
  ones) with 904 components, curated from ClinicalTrials.gov, the FDA Orange Book
  and PubMed, with component and target annotation from DrugBank, KEGG, PubChem, TTD
  and UniProt. Data were offered as tab-delimited text and Oracle dumps. DCDB was
  not updated after 2014, and the original host no longer serves the database or
  its downloads.
domains:
- pharmacology
- drug discovery
- clinical
- drug interactions
funding:
- Zhejiang Provincial Natural Science Foundation of China (R207609)
- National Basic Research Program of China (2012CB944900)
- National Natural Science Foundation of China (NSFC) (31071161)
- China Postdoctoral Science Foundation (2012M521164)
homepage_url: http://www.cls.zju.edu.cn/dcdb/
id: dcdb
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: Drug Combination Database
products:
- category: DocumentationProduct
  description: Original publication describing the Drug Combination Database (DCDB),
    its curated drug combinations, components, and targets. Retained as primary documentation
    because the original host site is no longer available.
  format: http
  id: dcdb.publication
  name: DCDB Publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dcdb
  product_url: https://doi.org/10.1093/bioinformatics/btp697
- category: GraphicalInterface
  description: Former DCDB web interface supporting browsing and query by individual
    drug, drug combination, usage and drug target, with wildcard text search.
  format: http
  id: dcdb.portal
  name: DCDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dcdb
  product_url: http://www.cls.zju.edu.cn/dcdb/
  warnings:
  - The host no longer serves DCDB (returned HTTP 403 when checked on 2026-11-12);
    archived copies of the pages are available from the Internet Archive Wayback Machine.
- category: Product
  compression: zip
  description: DCDB 2.0 data as tab-delimited plain text files (drug combinations,
    components, targets and their interactions), formerly offered on the DCDB download
    page alongside an Oracle 11.2 dump.
  format: tsv
  id: dcdb.plain_text_dump
  name: DCDB 2.0 Plain Text Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dcdb
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: http://www.cls.zju.edu.cn/dcdb/downloadfile/DCDB2_plaintxt.zip
  warnings:
  - File was not able to be retrieved when checked on 2026-11-12 (HTTP 404); no archived
    copy was found in the Internet Archive.
- category: GraphProduct
  description: Integrated pharmacological knowledge graph (PharmDB-K) of drugs, targets,
    diseases, and associations
  format: http
  id: pharmdb.graph
  name: PharmDB-K Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: dcdb
  - relation_type: prov:hadPrimarySource
    source: gad
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: t3db
  - relation_type: prov:hadPrimarySource
    source: wipo-tkp
publications:
- authors:
  - Liu Y
  - Hu B
  - Fu C
  - Chen X
  doi: 10.1093/bioinformatics/btp697
  id: doi:10.1093/bioinformatics/btp697
  journal: Bioinformatics
  title: 'DCDB: Drug combination database'
  year: '2010'
- authors:
  - Liu Y
  - Wei Q
  - Yu G
  - Gai W
  - Li Y
  - Chen X
  doi: 10.1093/database/bau124
  id: doi:10.1093/database/bau124
  journal: Database
  preferred: true
  title: 'DCDB 2.0: a major update of the drug combination database'
  year: '2014'
synonyms:
- DCDB
version: '2.0'
---
# Drug Combination Database

## Overview

DCDB (Drug Combination Database) was a curated resource developed at the Department
of Bioinformatics, College of Life Sciences, Zhejiang University. It collected drug
combinations together with their individual components, molecular targets,
mechanisms of action, and therapeutic indications, supporting research in
pharmacology, network pharmacology, and drug discovery. DCDB was used as an upstream
data source by downstream pharmacological knowledge graphs, including PharmDB.

Version 1.0 (2009) contained 499 drug combinations (178 approved and 321
investigational, including 40 unsuccessful ones) involving 485 individual drugs.
Version 2.0 (2014) expanded this to 1363 drug combinations, including 237 unsuccessful
ones, with 904 distinct components, curated from ClinicalTrials.gov, the FDA Orange
Book and PubMed. Component and target information came from DrugBank, KEGG, PubChem,
TTD and UniProt. The data were distributed as tab-delimited text files and as an
Oracle dump.

## Access

- Homepage (historical): http://www.cls.zju.edu.cn/dcdb/
- The original publications (Bioinformatics 2010; Database 2014) remain the most reliable
  documentation for the resource. None of the former download files can still be retrieved.

## Status

The resource is inactive. The historical host returns a content-management error page
("访问地址无效", i.e. "invalid access address") rather than the database, indicating the
DCDB section has been removed and the project is now defunct. Cite or consult the
original publication for details of the data model and contents.