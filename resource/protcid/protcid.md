---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: qifang.xu@fccc.edu
  label: Qifang Xu
- category: Individual
  label: Roland L. Dunbrack Jr
- category: Organization
  label: Fox Chase Cancer Center
creation_date: '2025-05-28T00:00:00Z'
description: The Protein Common Interface Database (ProtCID) provides comprehensive,
  PDB-wide structural information on protein interactions, identifying and clustering
  interfaces observed in multiple crystal forms of homologous proteins.
domains:
- proteomics
- chemistry and biochemistry
- biological systems
homepage_url: http://dunbrack2.fccc.edu/protcid/
id: protcid
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://dunbrack2.fccc.edu/ProtCID/About.aspx
  label: Custom
name: ProtCID
products:
- category: Product
  description: Database containing protein-protein interfaces, domain-domain interfaces,
    protein-peptide interfaces, and protein-ligand interactions based on structural
    data from the PDB.
  format: http
  id: protcid.database
  name: ProtCID Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: protcid
  product_url: https://dunbrack2.fccc.edu/ProtCID/default.aspx
- category: GraphicalInterface
  description: Web interface for searching and visualizing protein interaction data
    from ProtCID.
  format: http
  id: protcid.site
  name: ProtCID Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: protcid
  product_url: https://dunbrack2.fccc.edu/ProtCID/Search/search.aspx
- category: DocumentationProduct
  description: ProtCID help and browsing pages for common-interface searches, Pfam-based
    browsing, and interpretation guidance.
  format: http
  id: protcid.docs
  name: ProtCID Help and Browse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: protcid
  product_url: https://dunbrack2.fccc.edu/ProtCID/Help/Help.aspx
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
publications:
- authors:
  - Qifang Xu
  - Roland L. Dunbrack
  doi: 10.1038/s41467-020-14301-4
  id: https://doi.org/10.1038/s41467-020-14301-4
  journal: Nature Communications
  preferred: true
  title: 'ProtCID: a data resource for structural information on protein interactions'
  year: '2020'
- authors:
  - Qifang Xu
  - Roland L. Dunbrack
  doi: 10.1093/nar/gkq1059
  id: https://doi.org/10.1093/nar/gkq1059
  journal: Nucleic Acids Research
  title: The protein common interface database (ProtCID) - a comprehensive database of interactions of homologous proteins in multiple crystal forms
  year: '2011'
- authors:
  - Qifang Xu
  - Adrian Canutescu
  - Zhenyu Wang
  - Mu Tian
  - Thomas Biesiada
  - Roland L. Dunbrack
  doi: 10.1016/j.jmb.2008.06.002
  id: https://doi.org/10.1016/j.jmb.2008.06.002
  journal: Journal of Molecular Biology
  title: Statistical Analysis of Interface Similarity in Crystals of Homologous Proteins
  year: '2008'
tags:
- core
version: '3.0'
---
# ProtCID

The Protein Common Interface Database (ProtCID) organizes PDB-wide structural
evidence about protein interfaces, domain-domain contacts, peptide interactions,
and ligand or nucleic-acid interactions. It clusters recurring interfaces across
homologous proteins so that structurally repeated contacts can be examined as
candidate biologically relevant interactions.

ProtCID supports search by PDB identifiers, Pfam terms, UniProt accessions, and
sequence input, and it also exposes browse and help pages for interpreting common
interface clusters. The `spoke` graph remains attached here as a propagated
downstream product because SPOKE incorporates ProtCID structural interaction data
as one upstream source among many.