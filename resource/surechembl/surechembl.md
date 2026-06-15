---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: SureChEMBL is a freely available, large-scale resource of chemical compounds extracted from the patent literature through automated text- and image-mining. Hosted by EMBL-EBI, it links millions of annotated chemical structures to the patent documents in which they appear, enabling search and discovery of chemistry disclosed in patents. The resource is updated continuously and made available for both interactive search and bulk download.
domains:
  - drug discovery
  - chemistry and biochemistry
  - literature
homepage_url: https://www.surechembl.org/
id: surechembl
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: SureChEMBL
products:
  - category: Product
    description: Bulk download of the entire annotated SureChEMBL database as a set of core Parquet datasets, including chemical compounds (with SMILES, InChI, and molecular weight), patent metadata, compound-to-patent mappings, and extracted biomedical entities. A new complete version is released every two weeks via the EMBL-EBI FTP server.
    id: surechembl.bulk-data
    name: SureChEMBL Bulk Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: surechembl
    product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/SureChEMBL/bulk_data/
  - category: GraphicalInterface
    description: Web-based search interface for SureChEMBL providing combined chemical structure and keyword search across compounds mined from the patent literature, with links from compounds to the patent documents in which they were found.
    format: http
    id: surechembl.search
    name: SureChEMBL Web Search Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: surechembl
    product_url: https://www.surechembl.org/
  - category: DocumentationProduct
    description: Official SureChEMBL documentation describing the data sources, search capabilities, bulk data schema, and download options.
    format: http
    id: surechembl.docs
    name: SureChEMBL Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: surechembl
    product_url: https://chembl.gitbook.io/surechembl
publications:
  - authors:
      - George Papadatos
      - Mark Davies
      - Nathan Dedman
      - Jon Chambers
      - Anna Gaulton
      - James Siddle
      - Richard Koks
      - Sean A. Irvine
      - Joe Pettersson
      - Nicko Goncharoff
      - Anne Hersey
      - John P. Overington
    doi: doi:10.1093/nar/gkv1253
    id: doi:10.1093/nar/gkv1253
    journal: Nucleic Acids Research
    preferred: true
    title: 'SureChEMBL: a large-scale, chemically annotated patent document database'
    year: '2016'
---

# SureChEMBL

SureChEMBL is a freely available, large-scale resource of chemical compounds
extracted from the patent literature. Compounds are identified automatically
through text- and image-mining of patent documents, then chemically annotated
and linked back to the patents in which they appear. The resource is hosted and
maintained by EMBL-EBI.

In KG-Registry, the SureChEMBL products point to the live web search interface,
the bulk Parquet data distributed through the EMBL-EBI FTP server, and the
official documentation. The data are made available under a CC BY 4.0 license,
though individual compounds may carry additional restrictions imposed by the
original data owners.
