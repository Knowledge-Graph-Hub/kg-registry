---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://form2.jst.go.jp/s/contact_nbdc
  label: National Bioscience Database Center (NBDC), Japan Science and Technology
    Agency
creation_date: '2026-10-05T00:00:00Z'
description: The Life Science Database Archive (LSDB Archive) is run by the National
  Bioscience Database Center (NBDC) of the Japan Science and Technology Agency. It
  preserves datasets from Japanese life science databases for the long term and distributes
  each one as a whole-database download, with database-level and data-item-level metadata
  in a common format, a DOI per archived database (prefix 10.18908/lsdba), and a license
  stated per database. About 90 databases are archived, including FANTOM5, ChIP-Atlas,
  KEGG MEDICUS, INOH, Open TG-GATEs, BodyParts3D and the NBDC Nikkaji RDF. Creative
  Commons licenses are the standard, but the version differs by database (for example
  CC BY 4.0, CC BY-SA 4.0 or CC BY-SA 2.1 Japan).
domains:
- biomedical
- metadata
- genomics
- organisms
- information technology
homepage_url: https://dbarchive.biosciencedbc.jp/
id: lsdb-archive
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: kegg.'
  id: https://www.kegg.jp/feedback/copyright.html
  inferred_from:
  - kegg
  label: By request
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
name: Life Science Database Archive
products:
- category: GraphicalInterface
  description: English web portal of the LSDB Archive for browsing archived databases,
    reading each database's description and license, and reaching its download page
    and TogoDB simple search.
  format: http
  id: lsdb-archive.portal
  name: LSDB Archive Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_url: https://dbarchive.biosciencedbc.jp/index-e.html
- category: GraphicalInterface
  description: Searchable list of data items (individual files and tables) across
    all archived databases, with item-level metadata.
  format: http
  id: lsdb-archive.data-list
  name: LSDB Archive Data List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_url: https://dbarchive.biosciencedbc.jp/datameta-list-e.html
- category: Product
  description: Machine-readable catalog of archived databases in JSON, with name,
    Integbio Database Catalog ID, DOI, creators, categories, organisms, description,
    original sites and download page for each database. Some records in the file are
    malformed duplicates.
  format: json
  id: lsdb-archive.database-catalog-json
  name: LSDB Archive Database Catalog (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_file_size: 0
  product_url: https://dbarchive.biosciencedbc.jp/en/databases.json
- category: Product
  description: Machine-readable catalog of archived databases in CSV, with the same
    fields as the JSON catalog.
  format: csv
  id: lsdb-archive.database-catalog-csv
  name: LSDB Archive Database Catalog (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_file_size: 0
  product_url: https://dbarchive.biosciencedbc.jp/en/databases.csv
- category: Product
  compression: zip
  description: ZIP bundle of the full English metadata export, containing database-level
    metadata (dbmeta_en.json) and data-item-level metadata (datameta_en.json) for
    all archived databases.
  format: json
  id: lsdb-archive.metadata-dump
  name: LSDB Archive Metadata Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_file_size: 0
  product_url: https://dbarchive.biosciencedbc.jp/en/databases/download.json
- category: Product
  description: Open directory of archived database files, with one folder per database
    and dated release subfolders plus a LATEST link. File formats vary by database.
  format: mixed
  id: lsdb-archive.downloads
  name: LSDB Archive Download Directory
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_url: https://dbarchive.biosciencedbc.jp/data/
- category: Product
  description: LSDB Archive copy of FANTOM5 data files, in dated releases (2015 to
    2019), licensed CC BY 4.0.
  format: mixed
  id: lsdb-archive.fantom5
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: FANTOM5 (LSDB Archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  - relation_type: prov:hadPrimarySource
    source: fantom5
  product_url: https://dbarchive.biosciencedbc.jp/data/fantom5/
- category: Product
  description: LSDB Archive copy of the INOH pathway database, in dated releases (2011
    to 2017), licensed CC BY-SA 2.1 Japan.
  format: mixed
  id: lsdb-archive.inoh
  license:
    id: https://creativecommons.org/licenses/by-sa/2.1/jp/
    label: CC BY-SA 2.1 JP
  name: INOH (LSDB Archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  - relation_type: prov:hadPrimarySource
    source: inoh
  product_url: https://dbarchive.biosciencedbc.jp/data/inoh/
- category: Product
  description: LSDB Archive copy of KEGG MEDICUS, the KEGG resource for drugs, diseases
    and drug labels, in dated releases (2014 to 2023), licensed CC BY-SA 4.0.
  format: mixed
  id: lsdb-archive.kegg-medicus
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: KEGG MEDICUS (LSDB Archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  - relation_type: prov:hadPrimarySource
    source: kegg
  product_url: https://dbarchive.biosciencedbc.jp/data/kegg-medicus/
- category: DocumentationProduct
  description: About page describing the purpose of the archive, its common metadata
    format and its use of Creative Commons licenses.
  format: http
  id: lsdb-archive.about
  name: About the LSDB Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_url: https://dbarchive.biosciencedbc.jp/contents-en/about/about.html
- category: DocumentationProduct
  description: NBDC terms of service for the LSDB Archive site, in English (PDF).
  format: pdf
  id: lsdb-archive.terms
  name: NBDC Terms of Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lsdb-archive
  product_file_size: 499210
  product_url: https://dbarchive.biosciencedbc.jp/files/nbdc_riyou_kiyaku_en.pdf
synonyms:
- LSDB Archive
- NBDC Life Science Database Archive
---
# Life Science Database Archive

The Life Science Database Archive (LSDB Archive) is the National Bioscience Database Center (NBDC) service for long-term preservation of databases produced by life scientists in Japan. Databases from projects overseen by Japan's Ministry of Education, Culture, Sports, Science and Technology are expected to be deposited here. The archive focuses on experimental data other than DNA sequences, protein structures and expression data, which already have international archives.

Each archived database has a description page, a download page, a license page and an update history. Most also have a DOI under the prefix `10.18908/lsdba` and an Integbio Database Catalog ID.

## Data access

- Whole-database downloads live in an open directory at `https://dbarchive.biosciencedbc.jp/data/`, with one folder per database and dated release subfolders plus `LATEST`.
- The database catalog comes as JSON and CSV, and a ZIP bundle holds both database-level and data-item-level metadata.
- Many databases can also be searched as tables through TogoDB.

## Licensing

There is no single license for the whole archive. Creative Commons is the standard, but each database states its own license and attribution text. When checked on 2026-10-05, for example, FANTOM5 and BodyParts3D were CC BY 4.0, ChIP-Atlas and KEGG MEDICUS were CC BY-SA 4.0, and INOH was CC BY-SA 2.1 Japan.