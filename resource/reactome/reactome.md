---
activity_status: active
category: DataSource
contacts:
- category: Individual
  email: cjmungall@lbl.gov
  github: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
description: Reactome from Biopax
domains:
- biological systems
homepage_url: https://reactome.org
id: reactome
layout: resource_detail
name: Reactome
products:
- category: Product
  description: Conversion from BioPAX, human subset
  id: reactome.data.human
  name: Reactome Human from BioPAX, sqlite
  original_source:
  - reactome
  product_url: https://s3.amazonaws.com/bbop-sqlite/reactome-hs.db.gz
  secondary_source:
  - reactome
- category: MappingProduct
  description: Rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: Rhea SSSOM
  original_source:
  - rhea
  - reactome
  - kegg
  - metacyc
  - m-csa
  - ecocyc
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: bigg.metabolite SSSOM
  format: sssom
  id: obo-db-ingest.bigg.metabolite.sssom.tsv
  license:
    id: http://bigg.ucsd.edu/license#license
    label: Custom
  name: bigg.metabolite SSSOM
  original_source:
  - chebi
  - bigg
  - biocyc
  - kegg
  - reactome
  product_url: https://w3id.org/biopragmatics/resources/bigg.metabolite/bigg.metabolite.sssom.tsv
  secondary_source:
  - obo-db-ingest
repository: ''
---
REACTOME is an open-source, open access, manually curated and peer-reviewed pathway database.

This record includes alternative translatons:

- direct from BioPAX
- biopragmatics conversion

See also: [reacto](reacto.md)