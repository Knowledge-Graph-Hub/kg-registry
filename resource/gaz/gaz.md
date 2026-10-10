---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: lschriml@som.umaryland.edu
  - contact_type: github
    value: lschriml
  label: Lynn Schriml
  orcid: 0000-0001-8910-9851
creation_date: '2025-09-29T00:00:00Z'
description: A gazetteer constructed on ontological principles. The countries are
  actively maintained.
domains:
- environment
- geographic information systems
homepage_url: http://environmentontology.github.io/gaz/
id: gaz
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Gazetteer
products:
- category: OntologyProduct
  description: Gazetteer in OWL format
  format: owl
  id: gaz.owl
  name: gaz.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gaz
  product_file_size: 1308877129
  product_url: http://purl.obolibrary.org/obo/gaz.owl
- category: OntologyProduct
  description: Gazetteer in OBO format
  format: obo
  id: gaz.obo
  name: gaz.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gaz
  product_file_size: 189228723
  product_url: http://purl.obolibrary.org/obo/gaz.obo
- category: OntologyProduct
  description: A country specific subset of the GAZ.
  format: owl
  id: gaz.gaz-countries.owl
  name: GAZ countries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gaz
  product_file_size: 42847
  product_url: http://purl.obolibrary.org/obo/gaz/gaz-countries.owl
- category: ProgrammingInterface
  connection_url: https://pavs.phenomebrowser.net/sparql
  description: Public Virtuoso SPARQL endpoint for the PAVS knowledge graph, containing
    Saudi case records, gene annotations, HPO disease annotations, HPO information
    content values and literature phenopackets as RDF named graphs.
  format: http
  id: pavs-kg.sparql
  is_public: true
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: PAVS SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/sparql
- category: GraphicalInterface
  description: PAVS web portal with phenotype-based semantic similarity search, gene
    and variant browsers, and an HPO hierarchy explorer over the knowledge graph.
  format: http
  id: pavs-kg.portal
  name: PAVS Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/
- category: ProgrammingInterface
  description: FastAPI REST API backing the PAVS portal, with OpenAPI documentation,
    for case search and SPARQL-backed queries.
  format: http
  id: pavs-kg.api
  name: PAVS REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/api/docs
- category: Product
  description: Combined GA4GH Phenopackets v2 JSON file of all PAVS cases, with HPO
    phenotypes, variants, genes, zygosity, pathogenicity and disease diagnoses.
  format: json
  id: pavs-kg.phenopackets
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: PAVS Phenopackets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 1921927
  product_url: https://raw.githubusercontent.com/bio-ontology-research-group/pavs-knowledge-graph/master/data/PAVS_phenopackets.json
- category: OntologyProduct
  description: Sickle Cell Disease Ontology in OWL format
  format: owl
  id: scdo.owl
  name: scdo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scdo
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  - relation_type: prov:hadPrimarySource
    source: aro
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: cmo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dron
  - relation_type: prov:hadPrimarySource
    source: duo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eupath
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: ico
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: idomal
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: opmi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: symp
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 367519
  product_url: http://purl.obolibrary.org/obo/scdo.owl
- category: OntologyProduct
  description: Sickle Cell Disease Ontology in OBO format
  format: obo
  id: scdo.obo
  name: scdo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scdo
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  - relation_type: prov:hadPrimarySource
    source: aro
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: cmo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dron
  - relation_type: prov:hadPrimarySource
    source: duo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eupath
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: ico
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: idomal
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: opmi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: symp
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 324416
  product_url: http://purl.obolibrary.org/obo/scdo.obo
publications: []
repository: https://github.com/EnvironmentOntology/gaz
---
## Description

A gazetteer constructed on ontological principles. The countries are actively maintained.

## Contacts

- Lynn Schriml (lschriml@som.umaryland.edu) [ORCID: 0000-0001-8910-9851](https://orcid.org/0000-0001-8910-9851)

## Products

### gaz.owl

Gazetteer in OWL format

**URL**: [http://purl.obolibrary.org/obo/gaz.owl](http://purl.obolibrary.org/obo/gaz.owl)

**Format**: owl

### gaz.obo

Gazetteer in OBO format

**URL**: [http://purl.obolibrary.org/obo/gaz.obo](http://purl.obolibrary.org/obo/gaz.obo)

**Format**: obo

### GAZ countries

A country specific subset of the GAZ.

**URL**: [http://purl.obolibrary.org/obo/gaz/gaz-countries.owl](http://purl.obolibrary.org/obo/gaz/gaz-countries.owl)

**Format**: owl

**Domains**: environment

---

*This resource was automatically synchronized from the OBO Foundry registry.*