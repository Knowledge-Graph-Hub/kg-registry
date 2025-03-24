---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: ChEBI
description: "Chemical Entities of Biological Interest (ChEBI) is a freely available\
  \ dictionary of molecular entities focused on \u2018small\u2019 chemical compounds."
domain: chemistry and biochemistry
homepage_url: https://www.ebi.ac.uk/chebi/
id: chebi
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: ChEBI
products:
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
- category: Product
  description: ChEBI chemical structures and additional data in SDF format. This file contains only the chemical structure, ChEBI identifier and ChEBI Name.
  format: chebi_sdf
  id: chebi.structures.lite
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: ChEBI structures (lite)
  original_source:
  - chebi
  product_url: https://ftp.ebi.ac.uk/pub/databases/chebi/SDF/ChEBI_lite_3star.sdf.gz
  secondary_source:
  - chebi
  compression: gzip
- category: Product
  description: ChEBI chemical structures and additional data in SDF format. This file contains all the chemical structures and associated information. Note that it excludes any ontological information as ontological classes are not able to be represented as they do not contain a structure.
  format: chebi_sdf
  id: chebi.structures.complete
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: ChEBI structures (complete)
  original_source:
  - chebi
  product_url: https://ftp.ebi.ac.uk/pub/databases/chebi/SDF/ChEBI_complete_3star.sdf.gz
  secondary_source:
  - chebi
  compression: gzip
repository: https://github.com/ebi-chebi/ChEBI
---
ChEBI