---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: ribeiro@ebi.ac.uk
  label: "Ant\xF3nio JM Ribeiro"
description: The Mechanism and Catalytic Site Atlas (M-CSA) is a database of enzyme
  reaction mechanisms. It provides annotation on the protein, catalytic residues,
  cofactors, and the reaction mechanisms of hundreds of enzymes. There are two kinds
  of entries in M-CSA. 'Detailed mechanism' entries are more complete and show the
  individual chemical steps of the mechanism as schemes with electron flow arrows.
  'Catalytic Site' entries annotate the catalytic residues necessary for the reaction,
  but do not show the mechanism.
domains:
- biological systems
homepage_url: https://www.ebi.ac.uk/thornton-srv/m-csa/
id: m-csa
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: M-CSA
products:
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
---
M-CSA