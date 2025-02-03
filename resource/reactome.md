---
layout: resource_detail
activity_status: active
id: reactome
name: Reactome
description: Reactome from Biopax
domain: biological systems
contact:
  orcid: 0000-0002-6601-2165
  github: cmungall
  email: cjmungall@lbl.gov
  label: Christopher J. Mungall
url: https://reactome.org
tracker: https://github.com/biopragmatics/pyobo/issues
repository: https://github.com/biopragmatics/obo-db-ingest
products:
- id: reactome-hs-biopax.db.gz
  name: Reactome Human from BioPAX, sqlite
  description: Conversion from BioPAX, human subset
  url: https://s3.amazonaws.com/bbop-sqlite/reactome-hs.db.gz
  format: sqlite
- id: reactome-hs-biopragmatics.obo
  name: Reactome Human, Biopragmatics
  description: Biopragmatics provided conversion, human subset
  url: https://w3id.org/biopragmatics/resources/reactome/reactome.obo
  format: obo
uri_prefix: http://www.reactome.org/
category: DataGraph
---

REACTOME is an open-source, open access, manually curated and peer-reviewed pathway database.

This record includes alternative translatons:

- direct from BioPAX
- biopragmatics conversion

See also: [reacto](reacto.md)
