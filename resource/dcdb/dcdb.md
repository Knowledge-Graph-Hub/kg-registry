---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: DCDB (Drug Combination Database) was a curated database of drug combinations
  and their components, developed at Zhejiang University. It catalogued combinations
  along with their individual drugs, molecular targets, mechanisms, and therapeutic
  indications to support pharmacology and drug discovery research. The resource served
  as an upstream source for downstream pharmacological knowledge graphs such as PharmDB.
  The original host site no longer serves the database and the project is now defunct.
domains:
- pharmacology
- drug discovery
- clinical
homepage_url: http://www.cls.zju.edu.cn/dcdb/
id: dcdb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
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
  - Yanbin Liu
  - Bin Hu
  - Chengxin Fu
  - Xin Chen
  doi: 10.1093/bioinformatics/btp697
  id: https://pubmed.ncbi.nlm.nih.gov/20031966/
  journal: Bioinformatics
  preferred: true
  title: 'DCDB: drug combination database'
  year: '2010'
---
# Drug Combination Database

## Overview

DCDB (Drug Combination Database) was a curated resource developed at the Department
of Bioinformatics, College of Life Sciences, Zhejiang University. It collected drug
combinations together with their individual components, molecular targets,
mechanisms of action, and therapeutic indications, supporting research in
pharmacology, network pharmacology, and drug discovery. DCDB was used as an upstream
data source by downstream pharmacological knowledge graphs, including PharmDB.

## Access

- Homepage (historical): http://www.cls.zju.edu.cn/dcdb/
- The original publication remains the most reliable documentation for the resource.

## Status

The resource is inactive. The historical host returns a content-management error page
("访问地址无效", i.e. "invalid access address") rather than the database, indicating the
DCDB section has been removed and the project is now defunct. Cite or consult the
original publication for details of the data model and contents.