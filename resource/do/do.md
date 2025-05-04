---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: lschriml@som.umaryland.edu
  - contact_type: github
    value: lschriml
  label: Lynn Schriml
description: A community-driven, community-accepted ontology of diseases for clinical
  research and medicine inclusive of genetic, environmental and infectious diseases.
domains:
- health
homepage_url: https://disease-ontology.org/
id: do
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Human Disease Ontology
products:
- category: DataModelProduct
  description: OWL release of DO (doid.owl). This file contains DO's is_a asserted
    hierarchy plus equivalent axioms to other OBO Foundry ontologies.
  format: owl
  id: do.owl
  name: Human Disease Ontology OWL release
  original_source:
  - do
  product_url: https://purl.obolibrary.org/obo/doid.owl
  secondary_source:
  - do
- category: DataModelProduct
  description: OBO release of DO (doid.obo). This file omits the equivalent axioms.
  format: obo
  id: do.obo
  name: Human Disease Ontology OBO release
  original_source:
  - do
  product_url: https://purl.obolibrary.org/obo/doid.obo
  secondary_source:
  - do
- category: ProcessProduct
  description: Utility code for supporting the operations of the Human Disease Ontology
  id: do.code.utils
  name: DO.utils
  original_source:
  - do
  product_url: https://github.com/DiseaseOntology/DO.utils
  secondary_source:
  - do
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.7
  format: kgx
  id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.7.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.7
  format: kgx
  id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.7.tsv
  secondary_source:
  - drug-approvals-kp
- category: MappingProduct
  description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
  format: sssom
  id: mondo.sssom
  name: MONDO SSSOM
  original_source:
  - do
  - hp
  - hgnc
  product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
  secondary_source:
  - mondo
- category: GraphProduct
  compression: zip
  description: Nodes from Human Disease Ontology
  format: csv
  id: biomarkerkg.nodes.condition
  name: BKG Condition Nodes
  original_source:
  - do
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Condition.nodes.zip
  secondary_source:
  - biomarkerkg
repository: https://github.com/DiseaseOntology/HumanDiseaseOntology
---
Human Disease Ontology