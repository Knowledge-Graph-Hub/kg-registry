---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://tatonettilab.org/
  - contact_type: github
    value: tatonetti-lab
  label: Tatonetti Lab
- category: Individual
  contact_details:
  - contact_type: email
    value: nicholas.tatonetti@cshs.org
  label: Nicholas P. Tatonetti
creation_date: '2025-07-08T00:00:00Z'
description: OFFSIDES is a database of drug side effects that were found through data
  mining of FDA Adverse Event Reporting System (FAERS) but are not listed on the official
  FDA drug labels. Part of the nSIDES resource developed by Tatonetti Lab.
domains:
- pharmacology
- pharmacovigilance
homepage_url: http://tatonettilab.org/offsides/
id: offsides
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC-BY-NC-SA-4.0
name: OFFSIDES
products:
- category: DocumentationProduct
  description: Tatonetti Lab project page describing OffSIDES and related nSIDES resources.
  format: http
  id: offsides.docs
  name: OffSIDES Project Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: offsides
  product_url: http://tatonettilab.org/offsides/
- category: Product
  compression: gzip
  description: Gzipped OFFSIDES table of drug side effects mined from FAERS that are
    not listed on official FDA labels.
  format: csv
  id: offsides.data
  name: OFFSIDES Data Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: offsides
  product_file_size: 68762346
  product_url: https://tatonettilab-resources.s3.us-west-1.amazonaws.com/nsides/OFFSIDES.csv.gz
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- category: Product
  description: The 35 Drugmonizome drug set libraries, listed with metadata and per-library
    download links. Each library is downloadable as a GMT-like DMT file keyed by InChIKey
    or by drug name. Sources are DrugBank (targets, enzymes, carriers, transporters,
    ATC codes), DrugCentral targets, the Drug Repurposing Hub (targets and mechanisms
    of action), STITCH targets, KINOMEscan kinases, SIDER side effects and indications,
    PharmGKB variants and OFFSIDES side effects, PubChem and RDKit MACCS chemical
    fingerprints, Geneshot literature and predicted genes (including ARCHS4 coexpression
    and Enrichr co-occurrence), CREEDS signatures, and L1000FWD signatures, Enrichr
    GO and KEGG terms, and SEP-L1000 predicted side effects.
  format: json
  id: drugmonizome.libraries
  name: Drugmonizome Drug Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: repohub
  - relation_type: prov:wasDerivedFrom
    source: stitch
  - relation_type: prov:wasDerivedFrom
    source: kinomescan
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: geneshot
  - relation_type: prov:wasDerivedFrom
    source: archs4
  - relation_type: prov:wasDerivedFrom
    source: enrichr
  - relation_type: prov:wasDerivedFrom
    source: creeds
  - relation_type: prov:wasDerivedFrom
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: sep-l1000
  product_url: https://maayanlab.cloud/drugmonizome/metadata-api/libraries
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-20: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: Web portal for browsing and searching predicted and known drug-side
    effect connections by drug or side effect, with side effect-GO term and side effect-phenotype
    networks.
  format: http
  id: sep-l1000.portal
  name: SEP-L1000 Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_url: http://maayanlab.net/SEP-L1000/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: meddra
  - relation_type: prov:wasInformedBy
    source: drugbank
- category: Product
  compression: gzip
  description: Off-label drug-ADR matrix (684 drugs by 9,404 MedDRA preferred terms)
    from OFFSIDES, which processed FDA Adverse Event Reporting System (FAERS) reports
    with propensity score matching.
  format: csv
  id: sep-l1000.faers-offsides
  name: SEP-L1000 FAERS OFFSIDES Side Effect Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: faers
  product_file_size: 463065
  product_url: http://maayanlab.net/SEP-L1000/downloads/FAERS_offsides_PTs.csv.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: meddra
publications:
- authors:
  - Tatonetti NP
  - Ye PP
  - Daneshjou R
  - Altman RB
  doi: 10.1126/scitranslmed.3003377
  id: https://www.ncbi.nlm.nih.gov/pubmed/22422992
  journal: Sci Transl Med
  preferred: true
  title: Data-driven prediction of drug effects and interactions
  year: '2012'
repository: https://github.com/tatonetti-lab/nsides
synonyms:
- OffSIDES
---
# OFFSIDES

OFFSIDES is a Tatonetti Lab resource derived from mining the FDA Adverse Event
Reporting System (FAERS) for drug side effects that are not listed on official
FDA labels. It is part of the broader nSIDES family of adverse-event resources,
which also includes TwoSIDES for drug-drug-effect relationships.

In KG-Registry, the owned OFFSIDES products are the project page and the public
data export. The Bioteque embeddings entry is retained as a downstream derivative
that reuses OFFSIDES content in a larger integrated embedding resource.