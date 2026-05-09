---
activity_status: active
category: DataSource
description: OFFSIDES is a database of drug side effects that were found through data mining of FDA Adverse Event Reporting System (FAERS) but are not listed on the official FDA drug labels. Part of the nSIDES resource developed by Tatonetti Lab.
domains:
  - pharmacology
id: "offsides"
layout: resource_detail
name: OFFSIDES
synonyms:
  - OffSIDES
homepage_url: http://tatonettilab.org/offsides/
last_modified_date: '2025-11-26T00:00:00Z'
products:
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: "bioteque.embeddings"
    name: Bioteque Embeddings
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: achilles
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ccle
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: cellosaurus
        relation_type: prov:hadPrimarySource
      - source: clue
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pharmacodb
        relation_type: prov:hadPrimarySource
      - source: prism
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: offsides
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: repohub
        relation_type: prov:hadPrimarySource
      - source: chemicalchecker
        relation_type: prov:hadPrimarySource
      - source: repodb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: creeds
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: dorothea
        relation_type: prov:hadPrimarySource
      - source: progeny
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: huri
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: omnipath
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - source: bioteque
        relation_type: prov:wasInfluencedBy
creation_date: '2025-07-08T00:00:00Z'
---

# OFFSIDES

OFFSIDES is a database of drug side effects discovered through data mining of the FDA Adverse Event Reporting System (FAERS) but not listed on official FDA drug labels. It is part of the nSIDES (Network-based Side Effect Database System) resource family developed by the Tatonetti Lab.
