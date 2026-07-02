---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://synlethdb.sist.shanghaitech.edu.cn/
  id: zhenglab
  label: Zheng Lab, School of Information Science and Technology, ShanghaiTech University
creation_date: '2026-07-01T00:00:00Z'
description: SynLethDB is a comprehensive database of synthetic lethality (SL) gene
  pairs and synthetic lethality-related interactions in human and other species. It
  aggregates SL and synthetic dosage lethality relationships assembled from biochemical
  and genetic screens, curated literature, other databases, and computational predictions,
  each annotated with supporting evidence and confidence scores. SynLethDB 2.0 further
  packages these relationships as a web-based knowledge graph (SynLethKG) that connects
  genes with compounds, diseases, pathways, and other biomedical entities to support
  anticancer drug-target discovery. It is the primary synthetic lethality data source
  underlying SynLethKG and downstream methods such as KG4SL.
domains:
- biomedical
- genomics
- drug discovery
homepage_url: https://synlethdb.sist.shanghaitech.edu.cn/
id: synlethdb
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: SynLethDB
products:
- category: Product
  description: Bulk downloads of SynLethDB synthetic lethality gene pairs, related
    interactions, and the SynLethKG knowledge graph, available in tabular and graph
    formats from the SynLethDB download page.
  format: http
  id: synlethdb.download
  name: SynLethDB Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: synlethdb
  product_url: https://synlethdb.sist.shanghaitech.edu.cn/#/download
- category: GraphicalInterface
  description: Web portal for browsing and searching synthetic lethality gene pairs,
    supporting evidence, and the SynLethKG knowledge graph.
  format: http
  id: synlethdb.portal
  name: SynLethDB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: synlethdb
  product_url: https://synlethdb.sist.shanghaitech.edu.cn/
- category: GraphProduct
  description: Data files for SynLethKG, the knowledge graph used by KG4SL and described
    as constructed from SynLethDB (v1.0/v2.0) and Hetionet.
  format: mixed
  id: kg4sl.synlethkg
  name: SynLethKG Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg4sl
  - relation_type: prov:hadPrimarySource
    source: synlethdb
  product_url: https://github.com/JieZheng-ShanghaiTech/KG4SL/tree/main/data
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
publications:
- authors:
  - Guo J
  - Liu H
  - Zheng J
  doi: 10.1093/nar/gkv1108
  id: https://www.ncbi.nlm.nih.gov/pubmed/26516187
  journal: Nucleic Acids Res
  title: 'SynLethDB: synthetic lethality database toward discovery of selective and
    sensitive anticancer drug targets'
  year: '2016'
- authors:
  - Wang J
  - Wu M
  - Huang X
  - Wang L
  - Zhang S
  - Liu H
  - Zheng J
  doi: 10.1093/database/baac030
  id: https://www.ncbi.nlm.nih.gov/pubmed/35562840
  journal: Database (Oxford)
  preferred: true
  title: 'SynLethDB 2.0: a web-based knowledge graph database on synthetic lethality
    for novel anticancer drug discovery'
  year: '2022'
taxon:
- NCBITaxon:9606
---
# SynLethDB

## Overview

SynLethDB is a comprehensive database of synthetic lethality (SL) gene pairs and related genetic interactions, developed by the Zheng Lab at ShanghaiTech University. It brings together synthetic lethality and synthetic dosage lethality relationships from genetic and biochemical screens, curated literature, other databases, and computational predictions, each annotated with supporting evidence and confidence scores.

## SynLethKG

SynLethDB 2.0 released SynLethKG, a knowledge graph that embeds the curated synthetic lethality relationships within a broader biomedical network linking genes to compounds, diseases, pathways, and other entities. SynLethKG is the structured graph used by the KG4SL synthetic lethality prediction method, which integrates SynLethDB relationships with additional biomedical relations from Hetionet.

## Access

- Web portal: browse and search SL gene pairs and the knowledge graph
- Bulk download: tabular SL data and graph files from the download page

## Terms and citation

Specific license terms are not stated on the SynLethDB site. Please cite the SynLethDB publications when using the resource.
</content>
</invoke>