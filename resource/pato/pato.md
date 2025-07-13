---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: g.gkoutos@gmail.com
  - contact_type: url
    value: https://orcid.org/0000-0002-2061-091X
  - contact_type: github
    value: gkoutos
  label: George Gkoutos
creation_date: "2025-07-12T00:00:00Z"
description: Phenotype And Trait Ontology (PATO) is an ontology of phenotypic qualities
  (properties, attributes or characteristics). It is used in conjunction with other
  ontologies to refer to phenotypes, and is widely used for logical definitions of
  phenotypes in cross-species integration.
domains:
- phenotype
homepage_url: https://github.com/pato-ontology/pato/
id: pato
last_modified_date: "2025-07-12T00:00:00Z"
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: Phenotype And Trait Ontology
products:
- category: DataModelProduct
  description: The main OWL release of the Phenotype And Trait Ontology.
  format: owl
  id: pato.owl
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: PATO OWL
  product_url: http://purl.obolibrary.org/obo/pato.owl
- category: DataModelProduct
  description: The OBO format release of the Phenotype And Trait Ontology.
  format: obo
  id: pato.obo
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: PATO OBO
  product_url: http://purl.obolibrary.org/obo/pato.obo
- category: DataModelProduct
  description: The JSON format release of the Phenotype And Trait Ontology.
  format: json
  id: pato.json
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: PATO JSON
  product_url: http://purl.obolibrary.org/obo/pato.json
- category: DataModelProduct
  description: The base OWL file for PATO, includes axioms linking to other ontologies
    but no imports.
  format: owl
  id: pato-base.owl
  license:
    id: http://creativecommons.org/licenses/by/3.0/
    label: CC BY 3.0
  name: PATO Base OWL
  product_url: http://purl.obolibrary.org/obo/pato/pato-base.owl
- category: DataModelProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_url: https://www.ebi.ac.uk/efo/efo.owl
  secondary_source:
  - efo
- category: DataModelProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_url: https://www.ebi.ac.uk/efo/efo.obo
  secondary_source:
  - efo
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: DataModelProduct
  description: The latest release of Plant Trait Ontology in OWL format
  format: owl
  id: to.owl
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology OWL
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  product_url: http://purl.obolibrary.org/obo/to.owl
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
- category: DataModelProduct
  description: The latest release of Plant Trait Ontology in OBO format
  format: obo
  id: to.obo
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology OBO
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  product_url: http://purl.obolibrary.org/obo/to.obo
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
- category: DataModelProduct
  description: The Basic subset of the Plant Trait Ontology in OBO format
  format: obo
  id: to-basic.obo
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology Basic OBO
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  product_url: http://purl.obolibrary.org/obo/to/subsets/to-basic.obo
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
repository: https://github.com/pato-ontology/pato
---
# Pato