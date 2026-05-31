---
activity_status: active
category: DataSource
creation_date: '2025-07-08T00:00:00Z'
description: OFFSIDES is a database of drug side effects that were found through data
  mining of FDA Adverse Event Reporting System (FAERS) but are not listed on the official
  FDA drug labels. Part of the nSIDES resource developed by Tatonetti Lab.
domains:
- pharmacology
homepage_url: http://tatonettilab.org/offsides/
id: offsides
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
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