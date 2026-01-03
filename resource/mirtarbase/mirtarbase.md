---
activity_status: active
category: DataSource
creation_date: '2025-07-17T00:00:00Z'
description: miRTarBase is a comprehensive database of experimentally validated microRNA-target
  interactions (MTIs). It collects and curates miRNA-target interactions with experimental
  evidence from the literature, including data from reporter assays, western blot,
  qPCR, microarray, and high-throughput experiments such as CLIP-Seq.
domains:
- genomics
- biological systems
id: mirtarbase
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: miRTarBase
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing experimentally validated microRNA-target
    interactions across multiple species.
  format: http
  id: mirtarbase.portal
  name: miRTarBase Web Portal
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/index.php
- category: Product
  description: Complete dataset of microRNA-target interactions (MTI) in CSV format
    containing all experimentally validated interactions.
  format: csv
  id: mirtarbase.mti
  name: miRTarBase Complete MTI Dataset
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-22_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-11-25_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1017)'')))'
- category: Product
  description: Dataset of microRNA target sites with detailed binding site information
    in CSV format.
  format: csv
  id: mirtarbase.target_sites
  name: miRTarBase Target Sites Dataset
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-22_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-10-21_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1017)'')))'
- category: Product
  description: Species-specific microRNA-target interaction datasets in CSV format
    for human, mouse, rat, and 25+ other species.
  format: csv
  id: mirtarbase.species_mti
  name: miRTarBase Species-Specific MTI Files
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-22_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-12-15_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1017)'')))'
- category: Product
  description: Curated datasets filtered for strong experimental evidence including
    reporter assays, western blot, qPCR, and CLIP-Seq data.
  format: csv
  id: mirtarbase.strong_evidence
  name: miRTarBase Strong Evidence Datasets
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-22_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-12-07_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1017)'')))'
- category: Product
  description: Archive of previous miRTarBase releases for reproducibility and historical
    comparisons.
  format: http
  id: mirtarbase.archive
  name: miRTarBase Previous Releases Archive
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-22_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-12-13_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-03: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1017)'')))'
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - doid
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
publications:
- authors:
  - Cui S
  - Yu S
  - Huang HY
  - Lin YCD
  - Huang Y
  - Zhang B
  - Xiao J
  - Zuo H
  - Wang J
  - Li Z
  id: https://doi.org/10.1093/nar/gkae1072
  journal: Nucleic Acids Research
  preferred: true
  title: 'miRTarBase 2025: updates to the collection of experimentally validated microRNA-target
    interactions'
  year: '2024'
- authors:
  - Huang HY
  - Lin YCD
  - Cui S
  - Huang Y
  - Tang Y
  - Xu J
  - Bao J
  - Li Y
  - Wen J
  - Zuo H
  id: https://doi.org/10.1093/nar/gkab1079
  journal: Nucleic Acids Research
  preferred: false
  title: 'miRTarBase update 2022: an informative resource for experimentally validated
    miRNA-target interactions'
  year: '2022'
---
# miRTarBase

miRTarBase is a comprehensive database that curates experimentally validated microRNA-target interactions (MTIs) from published literature. Developed by the Warshel Institute for Computational Biology at The Chinese University of Hong Kong, Shenzhen, miRTarBase collects MTIs with experimental evidence from various methods including reporter assays, western blot, qPCR, microarray, and next-generation sequencing experiments such as CLIP-Seq and degradome sequencing. The database covers over 28 species and provides detailed information about target sites, experimental evidence, and validation methods. Users can browse and download complete datasets in CSV format, including species-specific files and subsets filtered by evidence strength. For more information, visit the [miRTarBase portal](https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/index.php).