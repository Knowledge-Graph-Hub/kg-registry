---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@gpcrdb.org
  - contact_type: url
    value: https://docs.gpcrdb.org/contact.html
  label: GPCRdb team, Gloriam group, University of Copenhagen
creation_date: '2026-10-04T00:00:00Z'
description: GPCRdb is an information system for G protein-coupled receptors (GPCRs)
  that provides reference sequences and alignments with generic residue numbering,
  manually annotated experimental structures and state-specific structure models,
  ligands and bioactivities, receptor mutations, drugs and targets, signaling protein
  data, and web tools for structure, sequence and ligand analysis. It was started
  in 1993 and has been maintained by the David Gloriam group at the University of
  Copenhagen since 2013. Data are available through the web portal and a REST API
  under CC BY 4.0, and the source code is released under the Apache 2.0 license.
domains:
- pharmacology
- drug discovery
- proteomics
- protein structure
fairsharing_id: FAIRsharing.e4n3an
homepage_url: https://gpcrdb.org/
id: gpcrdb
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: GPCRdb
products:
- category: GraphicalInterface
  description: GPCRdb web portal for browsing and analyzing GPCR receptors, sequence
    alignments, structures and structure models, ligands and bioactivities, mutations,
    drugs and signaling proteins, with interactive diagrams such as snake plots and
    phylogenetic trees.
  format: http
  id: gpcrdb.portal
  name: GPCRdb Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpcrdb
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  product_url: https://gpcrdb.org/
- category: ProgrammingInterface
  description: REST API returning JSON for most GPCRdb data, including proteins, families,
    alignments, residues, structures, ligands, mutations and signaling proteins.
  format: http
  id: gpcrdb.api
  name: GPCRdb REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpcrdb
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  product_url: https://gpcrdb.org/services/reference/
- category: Product
  description: GitHub repository collecting the reference data used to build GPCRdb,
    including protein, structure, ligand, mutant, drug, G protein, arrestin and residue
    data files, plus a PDSP Ki data backup.
  format: mixed
  id: gpcrdb.data
  name: GPCRdb Reference Data Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpcrdb
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pdsp
  product_url: https://github.com/protwis/gpcrdb_data
  warnings:
  - The repository has no license file; the GPCRdb legal notice states that GPCRdb
    data are available under CC BY 4.0.
- category: ProcessProduct
  description: Protwis, the Django-based source code behind GPCRdb, including the
    database build pipeline and web tools.
  format: http
  id: gpcrdb.code
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache 2.0
  name: Protwis Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpcrdb
  product_url: https://github.com/protwis/protwis
- category: DocumentationProduct
  description: GPCRdb documentation covering receptors, structures, ligands, mutations,
    generic residue numbering, web services, local installation and the legal notice.
  format: http
  id: gpcrdb.docs
  name: GPCRdb Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpcrdb
  product_url: https://docs.gpcrdb.org/
publications:
- authors:
  - Gáspár Pándy-Szekeres
  - Jimmy Caroli
  - Alibek Mamyrbekov
  - Ali A Kermani
  - György M Keserű
  - Albert J Kooistra
  - David E Gloriam
  doi: 10.1093/nar/gkac1013
  id: doi:10.1093/nar/gkac1013
  journal: Nucleic Acids Research
  preferred: true
  title: 'GPCRdb in 2023: state-specific structure models using AlphaFold2 and new
    ligand resources'
  year: '2023'
- authors:
  - Albert J Kooistra
  - Stefan Mordalski
  - Gáspár Pándy-Szekeres
  - Mauricio Esguerra
  - Alibek Mamyrbekov
  - Christian Munk
  - György M Keserű
  - David E Gloriam
  doi: 10.1093/nar/gkaa1080
  id: doi:10.1093/nar/gkaa1080
  journal: Nucleic Acids Research
  title: 'GPCRdb in 2021: integrating GPCR sequence, structure and function'
  year: '2021'
- authors:
  - Gáspár Pándy-Szekeres
  - Christian Munk
  - Tsonko M Tsonkov
  - Stefan Mordalski
  - Kasper Harpsøe
  - Alexander S Hauser
  - Andrzej J Bojarski
  - David E Gloriam
  doi: 10.1093/nar/gkx1109
  id: doi:10.1093/nar/gkx1109
  journal: Nucleic Acids Research
  title: 'GPCRdb in 2018: adding GPCR structure models and ligands'
  year: '2018'
repository: https://github.com/protwis/protwis
synonyms:
- GPCR database
- GPCRDB
---
# GPCRdb

GPCRdb is a reference resource for G protein-coupled receptors, the largest family of drug targets. It was started in 1993 by Gert Vriend, Ad IJzerman, Bob Bywater and Friedrich Rippmann, and stewardship moved to the David Gloriam group at the University of Copenhagen in 2013.

## Content

- Reference receptor sequences and alignments using GPCRdb generic residue numbering
- Manually annotated experimental GPCR structures, plus state-specific structure models (built with AlphaFold2 since the 2023 release)
- Ligands and bioactivities drawn from ChEMBL, Guide to Pharmacology and PDSP Ki data
- Receptor mutations, natural variants, drugs and drug targets, and G protein and arrestin data
- Tools for structure comparison, sequence signatures, ligand target profiles and receptor diagrams

## Access

Data can be browsed on the web portal or retrieved as JSON from the REST API (see the [API reference](https://gpcrdb.org/services/reference/)). The reference data used to build the database are kept in the [gpcrdb_data](https://github.com/protwis/gpcrdb_data) repository, and the full source code is in [protwis](https://github.com/protwis/protwis).

## License

Per the GPCRdb legal notice, data are available under the Creative Commons Attribution 4.0 International license and the source code under the Apache 2.0 license.
