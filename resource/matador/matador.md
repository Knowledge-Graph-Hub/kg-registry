---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: MATADOR (Manually Annotated Targets and Drugs Online Resource) is a manually
  curated database of drug-target relationships developed at EMBL. Unlike resources
  limited to direct binding, MATADOR captures both direct (binding) and indirect (e.g.,
  metabolic or signaling) drug-target interactions for proteins and small molecules.
  It was distributed alongside SuperTarget and serves as an upstream source for downstream
  knowledge graphs such as PharmDB.
domains:
- pharmacology
- drug discovery
- chemistry and biochemistry
homepage_url: http://matador.embl.de/
id: matador
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: MATADOR
products:
- category: DocumentationProduct
  description: Publication describing SuperTarget and MATADOR resources for exploring
    drug-target relationships, the primary stable reference for the MATADOR dataset.
  format: http
  id: matador.publication
  name: SuperTarget and Matador Publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: matador
  product_url: https://doi.org/10.1093/nar/gkm862
- category: GraphProduct
  description: Integrated pharmacological knowledge graph (PharmDB-K) of drugs, targets,
    diseases, and associations
  format: http
  id: pharmdb.graph
  name: PharmDB-K Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: dcdb
  - relation_type: prov:hadPrimarySource
    source: gad
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: t3db
  - relation_type: prov:hadPrimarySource
    source: wipo-tkp
publications:
- authors:
  - S. Gunther
  - M. Kuhn
  - M. Dunkel
  - M. Campillos
  - C. Senger
  - E. Petsalaki
  - J. Ahmed
  - E. G. Urdiales
  - A. Gewiess
  - L. J. Jensen
  - R. Schneider
  - R. Skoblo
  - R. B. Russell
  - P. E. Bourne
  - P. Bork
  - R. Preissner
  doi: 10.1093/nar/gkm862
  id: https://pubmed.ncbi.nlm.nih.gov/17942422/
  journal: Nucleic Acids Res
  preferred: true
  title: 'SuperTarget and Matador: resources for exploring drug-target relationships'
  year: '2008'
---
# MATADOR

## Description

MATADOR (Manually Annotated Targets and Drugs Online Resource) is a manually curated
EMBL database of drug-target relationships. It distinguishes itself by recording both
direct (binding) and indirect (such as metabolic or signaling) interactions between
small molecules and protein targets. The resource was released together with
SuperTarget and is an upstream source for derived knowledge graphs including PharmDB.
The original site (matador.embl.de) is no longer reachable, so the dataset is
considered inactive and is best accessed through its associated publication and
archived copies.

## Products

- SuperTarget and Matador Publication: the primary stable reference describing the
  MATADOR dataset and its companion SuperTarget resource.