---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: tarcisiocsf
  - contact_type: url
    value: https://www.sib.swiss
  label: Tarcisio Mendes de Farias
  orcid: 0000-0002-3175-5372
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.dbgi.org
  label: Digital Botanical Gardens Initiative
description: A knowledge graph version of the Earth Metabolome Initiative (EMI) Ontology, containing over 413 million triples derived from metabolomic datasets. It provides a structured representation of metabolomic data within a semantic framework.
domains:
- biological systems
- chemistry and biochemistry
homepage_url: https://github.com/digital-botanical-gardens-initiative/earth_metabolome_ontology
id: emikg
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: EMI KG
products:
- category: GraphProduct
  description: Graph version of the Earth Metabolome Initiative Ontology
  format: kgx
  id: emikg.kg
  name: EMI Knowledge Graph
  product_url: https://github.com/digital-botanical-gardens-initiative/earth_metabolome_ontology
  repository: https://github.com/digital-botanical-gardens-initiative/earth_metabolome_ontology
- category: ProgrammingInterface
  description: SPARQL endpoint for programmatic access to the EMI Knowledge Graph
  format: http
  id: emikg.sparql
  name: EMI KG SPARQL Endpoint
  product_url: https://biosoda.unil.ch/emi/sparql
- category: GraphicalInterface
  description: Web-based SPARQL query editor for the EMI Knowledge Graph
  id: emikg.web
  name: EMI KG SPARQL Query Editor
  product_url: https://sib-swiss.github.io/sparql-editor/dbgi
---