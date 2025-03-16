---
layout: resource_detail
activity_status: active
id: reactome
name: Reactome
description: Reactome from Biopax
domain: biological systems
contacts:
- category: Individual
  orcid: 0000-0002-6601-2165
  github: cmungall
  email: cjmungall@lbl.gov
  label: Christopher J. Mungall
homepage_url: https://reactome.org
repository: ""
products:
- id: reactome.data.human
  name: Reactome Human from BioPAX, sqlite
  description: Conversion from BioPAX, human subset
  url: https://s3.amazonaws.com/bbop-sqlite/reactome-hs.db.gz
  category: Product
  original_source:
  - reactome
  secondary_source:
  - reactome
category: DataSource
---

REACTOME is an open-source, open access, manually curated and peer-reviewed pathway database.

This record includes alternative translatons:

- direct from BioPAX
- biopragmatics conversion

See also: [reacto](reacto.md)
