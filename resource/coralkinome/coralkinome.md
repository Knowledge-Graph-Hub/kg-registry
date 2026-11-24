---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: dphansti
  label: Douglas H. Phanstiel
creation_date: '2025-11-05T00:00:00Z'
description: Coral is an interactive web application for visualizing quantitative and qualitative
  data in the context of the human kinome. It encodes data in node color, node size, and branch
  color, shows the kinome as the traditional tree or as radial or dynamic force networks, and
  exports vector graphics. Its annotation table gives kinase group, family, and subfamily assignments
  with UniProt, Ensembl, Entrez, and HGNC identifiers.
domains:
- proteomics
- chemistry and biochemistry
- enzymes
- pathways
- signal transduction
funding:
- National Human Genome Research Institute (R00HG008662)
- National Institute of General Medical Sciences (5T32GM007092, T32GM067553)
- National Institute of Diabetes and Digestive and Kidney Diseases (U24DK116204)
- National Cancer Institute (R01CA177993)
homepage_url: http://phanstiel-lab.med.unc.edu/CORAL/
id: coralkinome
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: Coral
products:
- category: GraphicalInterface
  description: Interactive Shiny web application for visualizing kinase data on the human kinome
    tree or as networks, with vector graphics export.
  format: http
  id: coralkinome.portal
  name: Coral Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: coralkinome
  product_url: http://phanstiel-lab.med.unc.edu/CORAL/
- category: Product
  description: Table of human kinases with Coral, UniProt, Ensembl, Entrez, and HGNC identifiers,
    kinase group, family, and subfamily, and drawing coordinates for the kinome tree.
  format: tsv
  id: coralkinome.kinase-table
  name: Coral Kinase Annotation Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: coralkinome
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_file_size: 853276
  product_url: https://raw.githubusercontent.com/dphansti/CORAL/master/Data/coral_dataframe.tsv
- category: ProcessProduct
  description: R/Shiny source code and data files for Coral.
  format: r
  id: coralkinome.code
  name: Coral Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: coralkinome
  product_url: https://github.com/dphansti/CORAL
- category: GraphicalInterface
  description: Interactive Shiny web interface for exploring and visualizing human
    kinase-substrate interactions
  format: http
  id: kinace.portal
  name: KiNet Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kinace
  product_url: https://kinet.kinametrix.com/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: coralkinome
  - relation_type: prov:wasDerivedFrom
    source: darkkinasekb
  - relation_type: prov:wasDerivedFrom
    source: epsd
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: kinhub
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: uniprot
publications:
- authors:
  - Kathleen S. Metz
  - Erika M. Deoudes
  - Matthew E. Berginski
  - Ivan Jimenez-Ruiz
  - Bulent Arman Aksoy
  - Jeff Hammerbacher
  - Shawn M. Gomez
  - Douglas H. Phanstiel
  doi: 10.1016/j.cels.2018.07.001
  id: doi:10.1016/j.cels.2018.07.001
  journal: Cell Systems
  preferred: true
  title: 'Coral: Clear and Customizable Visualization of Human Kinome Data'
  year: '2018'
repository: https://github.com/dphansti/CORAL
synonyms:
- CORAL
- CoralKinome
taxon:
- NCBITaxon:9606
---

# Coral

Coral is a web application for visualizing data on the human kinome, from the Phanstiel Lab at the
University of North Carolina. KiNet (KinAce) uses it as a source of kinase group membership.

This page was first created from a mention of "CORAL" in the KiNet documentation and wrongly described
a database of kinases from coral animals. The KiNet paper (doi:10.1038/s41540-024-00442-5) names
Coral, with KinHub, as a portal for phylogenetic classification of kinases. The identifier
`coralkinome` is kept so that existing references still resolve.
