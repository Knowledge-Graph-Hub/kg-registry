---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: pnrobinson
  label: Peter Robinson
description: An ontology developed by the Monarch Initiative used to describe human
  phenotypic abnormalities seen in genetic disorders and clinical research. It provides
  a structured representation of abnormal characteristics associated with diseases.
  HPO helps researchers and clinicians share and integrate phenotypic data, making
  understanding and diagnosing genetic disorders easier. It uses a hierarchical organization
  and semantic relationships between terms and allows for annotation of genes and
  diseases. HPO is used in multiple diagnosis and variant prioritization tools, aiding
  healthcare professionals and researchers in identifying and classifying genetic
  conditions.
domains:
- phenotype
homepage_url: https://hpo.jax.org/
id: hp
layout: resource_detail
license:
  id: https://hpo.jax.org/license
  label: Custom
name: Human Phenotype Ontology
products:
- category: DataModelProduct
  description: OWL release of HP
  format: owl
  id: hp.owl
  name: Human Phenotype Ontology OWL release
  original_source:
  - hp
  product_url: http://purl.obolibrary.org/obo/hp.owl
  secondary_source:
  - hp
- category: DataModelProduct
  description: OBO release of HP
  format: obo
  id: hp.obo
  name: Human Phenotype Ontology OBO release
  original_source:
  - hp
  product_url: http://purl.obolibrary.org/obo/hp.obo
  secondary_source:
  - hp
- category: ProcessProduct
  description: Code for Human Phenotype Ontology
  id: hp.code
  name: HP Code
  original_source:
  - hp
  product_url: https://github.com/obophenotype/human-phenotype-ontology
  secondary_source:
  - hp
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
  description: Nodes for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Edges for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Edges
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_edges_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
repository: https://github.com/obophenotype/human-phenotype-ontology
---
Human Phenotype Ontology