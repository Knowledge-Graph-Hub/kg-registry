---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: ribeiro@ebi.ac.uk
  label: "Ant\xF3nio JM Ribeiro"
creation_date: '2025-03-17T00:00:00Z'
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
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: M-CSA
publications:
- authors:
  - Ribeiro AJM
  - Holliday GL
  - Furnham N
  - Tyzack JD
  - Ferris K
  - Thornton JM
  doi: 10.1093/nar/gkx1012
  id: https://www.ncbi.nlm.nih.gov/pubmed/29106569
  journal: Nucleic Acids Res
  preferred: true
  title: 'Mechanism and Catalytic Site Atlas (M-CSA): a database of enzyme reaction
    mechanisms and active sites'
  year: '2018'
products:
- category: GraphicalInterface
  description: Official M-CSA website for browsing curated enzyme mechanisms, catalytic
    sites, and related entry statistics.
  format: http
  id: m-csa.portal
  name: M-CSA Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: m-csa
  product_url: https://www.ebi.ac.uk/thornton-srv/m-csa/
- category: DocumentationProduct
  description: M-CSA download and API page describing export formats and programmatic
    access to the atlas.
  format: http
  id: m-csa.download
  name: M-CSA Download and API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: m-csa
  product_url: https://www.ebi.ac.uk/thornton-srv/m-csa/download/
- category: MappingProduct
  description: rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: m-csa
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
---
# M-CSA

The Mechanism and Catalytic Site Atlas (M-CSA) is an EMBL-EBI resource for
curated enzyme reaction mechanisms and catalytic sites. It combines the legacy
Catalytic Site Atlas and MACiE efforts into a single database that records
proteins, catalytic residues, cofactors, mechanistic steps, and literature-backed
annotations for experimentally characterized enzymes.

This registry page treats the live M-CSA site and its download/API page as the
owned entry points for the resource itself. The shared `rhea` SSSOM file remains
attached here as a propagated downstream mapping product because it integrates
M-CSA content with other reaction resources.