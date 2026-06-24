---
category: Product
description: Downloadable HPIDB host-pathogen interaction dataset in PSI-MITAB format.
format: psi_mi_mitab
id: hpidb.mitab
name: HPIDB PSI-MITAB Dataset
original_source:
- relation_type: prov:hadPrimarySource
  source: hpidb
product_url: https://hpidb.igbb.msstate.edu/
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: intact
- relation_type: prov:wasDerivedFrom
  source: mint
- relation_type: prov:wasDerivedFrom
  source: dip
- relation_type: prov:wasDerivedFrom
  source: biogrid
warnings:
- File was not able to be retrieved when checked on 2026-06-22_ Error connecting to
  URL_ HTTPSConnectionPool(host='hpidb.igbb.msstate.edu', port=443)_ Max retries exceeded
  with url_ / (Caused by NewConnectionError("HTTPSConnection(host='hpidb.igbb.msstate.edu',
  port=443)_ Failed to establish a new connection_ [Errno 111] Connection refused"))
- The HPIDB homepage failed to establish HTTP and HTTPS connections during curation
  on 2026-06-02.
- The historical AgBase HPI downloads URL redirected and then returned HTTP 403 during
  curation on 2026-06-02.
layout: product_detail
---
