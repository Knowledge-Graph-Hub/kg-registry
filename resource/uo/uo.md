---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: g.gkoutos@gmail.com
  - contact_type: github
    value: gkoutos
  label: George Gkoutos
  orcid: 0000-0002-2061-091X
description: The Units Ontology (UO) provides a standardized vocabulary for units
  of measurement to facilitate consistent representation and integration of quantitative
  data in scientific research. It includes SI units, their derivatives, and commonly
  used units across scientific domains.
domains:
- upper
homepage_url: https://github.com/bio-ontology-research-group/unit-ontology
id: uo
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: Units of Measurement Ontology
products:
- category: DataModelProduct
  description: The latest release of UO in OWL format
  format: owl
  id: uo.owl
  name: UO OWL
  original_source:
  - uo
  product_url: http://purl.obolibrary.org/obo/uo.owl
- category: DataModelProduct
  description: The latest release of UO in OBO format
  format: obo
  id: uo.obo
  name: UO OBO
  original_source:
  - uo
  product_url: http://purl.obolibrary.org/obo/uo.obo
- category: DataModelProduct
  description: The latest release of UO in JSON format
  format: json
  id: uo.json
  name: UO JSON
  original_source:
  - uo
  product_url: http://purl.obolibrary.org/obo/uo.json
- category: GraphicalInterface
  description: Browse UO with Ontology Lookup Service (OLS)
  format: http
  id: uo.ols
  name: UO in OLS
  original_source:
  - uo
  product_url: https://www.ebi.ac.uk/ols/ontologies/uo
- category: GraphicalInterface
  description: Browse UO with OntoBee
  format: http
  id: uo.ontobee
  name: UO in OntoBee
  original_source:
  - uo
  product_url: https://ontobee.org/ontology/uo
- category: GraphicalInterface
  description: Browse UO with BioPortal
  format: http
  id: uo.bioportal
  name: UO in BioPortal
  original_source:
  - uo
  product_url: https://bioportal.bioontology.org/ontologies/UO
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
publications:
- authors:
  - Georgios V Gkoutos
  - Paul N Schofield
  - Robert Hoehndorf
  doi: 10.1093/database/bas033
  id: doi:10.1093/database/bas033
  journal: Database (Oxford)
  preferred: true
  title: The Units Ontology - a tool for integrating units of measurement in science
  year: '2012'
repository: https://github.com/bio-ontology-research-group/unit-ontology
---
# Units of Measurement Ontology

The Units Ontology (UO) is a controlled vocabulary for standardized units of measurement used in scientific research. It provides a comprehensive and systematic description of units, enabling consistent representation and integration of quantitative data across scientific disciplines.

UO was developed to address the need for integrating heterogeneous quantitative data in science, particularly in biomedical research. The ontology includes the International System of Units (SI), their derived units, and other commonly used units of measurement across scientific domains. It facilitates data exchange, integration, reproducibility, and semantic processing of quantitative measurements in databases and knowledge systems.

The ontology is structured to represent various aspects of units including:
- Base units (meter, kilogram, second, etc.)
- Derived units (newton, joule, pascal, etc.)
- Prefixed units (millimeter, kilogram, megahertz, etc.)
- Time units (second, minute, hour, day, etc.)
- Spatial units (meter, inch, foot, etc.)
- Mass units (gram, pound, dalton, etc.)
- Temperature units (kelvin, celsius, etc.)
- And many other domain-specific measurement units

UO is maintained by the Bio-Ontology Research Group and is part of the OBO Foundry collection of interoperable reference ontologies. It is widely used in conjunction with the Phenotype and Trait Ontology (PATO) and is integrated into numerous biological and biomedical data resources.

The ontology is provided under a CC-BY 3.0 license, making it freely available for both academic and commercial applications.