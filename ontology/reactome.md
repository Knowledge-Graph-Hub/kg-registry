---
layout: ontology_detail
activity_status: active
id: reactome
title: Reactome
description: Reactome from Biopax
domain: biological systems
preferredPrefix: Reactome
contact:
  orcid: 0000-0002-6601-2165
  github: cmungall
  email: cjmungall@lbl.gov
  label: Christopher J. Mungall
homepage: https://reactome.org
tracker: https://github.com/biopragmatics/pyobo/issues
repository: https://github.com/biopragmatics/obo-db-ingest
products:
- id: reactome-hs-biopax.db.gz
  title: Reactome Human from BioPAX, sqlite
  description: Conversion from BioPAX, human subset
  ontology_purl: https://s3.amazonaws.com/bbop-sqlite/reactome-hs.db.gz
  format: sqlite
- id: reactome-hs-biopragmatics.obo
  title: Reactome Human, Biopragmatics
  description: Biopragmatics provided conversion, human subset
  ontology_purl: https://w3id.org/biopragmatics/resources/reactome/reactome.obo
  format: obo
uri_prefix: http://www.reactome.org/
---

REACTOME is an open-source, open access, manually curated and peer-reviewed pathway database.

This record includes alternative translatons:

- direct from BioPAX
- biopragmatics conversion

See also: [reacto](reacto.md)
