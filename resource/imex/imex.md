---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/support/intact
  label: IntAct Team
creation_date: '2026-05-20T00:00:00Z'
description: IMEx Consortium is an international collaboration of public molecular
  interaction databases that shares deep-curation effort to produce a non-redundant,
  freely accessible set of experimentally supported molecular interaction records
  in PSI-MI standard formats.
domains:
- proteomics
- systems biology
- biological systems
homepage_url: https://www.imexconsortium.org/
id: imex
last_modified_date: '2026-05-22T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: IMEx Consortium
products:
- category: GraphicalInterface
  description: Search interface for the shared IMEx molecular interaction dataset.
  format: http
  id: imex.portal
  name: IMEx Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: intact
  product_url: https://www.imexconsortium.org/
- category: Product
  description: IMEx interaction downloads distributed through IntAct in PSI-MI XML
    and MITAB formats.
  format: psi_mi_mitab
  id: imex.downloads
  name: IMEx Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: intact
  product_url: https://www.ebi.ac.uk/intact/downloads
- category: GraphProduct
  description: IMEx complex nodes used in ProKN
  format: csv
  id: prokn.imex.complex.nodes
  name: ProKN IMEx Complex Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1381676
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Complex.nodes.csv
- category: GraphProduct
  description: IMEx protein interacts with protein edges
  format: csv
  id: prokn.imex.protein.interacts_with.protein.edges
  name: ProKN IMEx Protein Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 363360000
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Protein.INTERACTS_WITH.Protein.edges.csv
- category: GraphProduct
  description: IMEx protein participates in complex edges
  format: csv
  id: prokn.imex.protein.participates_in.complex.edges
  name: ProKN IMEx Protein Participates In Complex Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18774312
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Protein.PARTICIPATES_IN.Complex.edges.csv
publications:
- authors:
  - Porras P
  - Orchard S
  - Cesareni G
  - et al.
  id: https://doi.org/10.1038/s41467-020-19942-z
  journal: Nature Communications
  preferred: true
  title: Towards a unified open access dataset of molecular interactions
  year: '2020'
---

# IMEx Consortium

IMEx Consortium is a collaboration of major public molecular interaction data providers
that coordinate literature curation and direct submissions to avoid duplicated effort
and produce a shared, non-redundant interaction dataset. The consortium emphasizes
deep curation, common annotation rules, and distribution in PSI-MI standard formats.

Current IMEx data are centralized through IntAct at EMBL-EBI, while consortium member
databases curate or expose relevant subsets through their own portals. The public IMEx
website provides discovery and consortium context, and the IntAct download site is the
main distribution point for the current shared dataset.