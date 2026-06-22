---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: REDIportal is a specialized database of A-to-I RNA editing events, integrating ~16 million sites from GTEx and TCGA with links to Ensembl, RNAcentral, UniProt, and PRIDE. The portal supports search by genomic position, sample (GTEx/TCGA), dsRNA modules, and gene view, and reports AEI/REI indices and a deep-learning-based reliability score (REDInet).
domains:
  - genomics
  - biological systems
id: rediportal
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: REDIportal
products:
  - category: GraphicalInterface
    description: Web interface for browsing A-to-I RNA editing sites; supports Search Positions, Search Sample (GTEx/TCGA), Search dsRNA, and Gene View with integrated links to Ensembl, RNAcentral, UniProt, and PRIDE.
    format: http
    id: rediportal.portal
    name: REDIportal Web Portal
    product_url: http://srv00.recas.ba.infn.it/atlas/
    original_source:
      - source: rediportal
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Web portal for searching and browsing ncRNA sequences, structures, and annotations
    format: http
    id: rnacentral.portal
    name: RNAcentral Portal
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/
  - category: ProgrammingInterface
    description: REST API for programmatic access to RNAcentral data
    format: http
    id: rnacentral.api
    name: RNAcentral REST API
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/api
  - category: Product
    description: FTP archive with current and archived release files (sequences and annotations)
    format: http
    id: rnacentral.ftp
    name: RNAcentral FTP Archive
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
  - category: DataModelProduct
    description: Public PostgreSQL database for direct SQL access to RNAcentral data
    format: postgres
    id: rnacentral.public-db
    name: RNAcentral Public Postgres Database
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/help/public-database
publications:
- authors:
  - Pietro D'Addabbo
  - Roni Cohen-Fultheim
  - Itamar Twersky
  - Adriano Fonzino
  - Domenico Alessandro Silvestris
  - Ananth Prakash
  - Pietro Luca Mazzacuva
  - Juan Antonio Vizcaino
  - Andrew Green
  - Blake Sweeney
  doi: 10.1093/nar/gkae1083
  id: https://doi.org/10.1093/nar/gkae1083
  journal: Nucleic Acids Research
  preferred: true
  title: 'REDIportal: toward an integrated view of the A-to-I editing'
  year: '2025'
---

# REDIportal

REDIportal is a curated knowledgebase of A-to-I RNA editing sites. It integrates data from GTEx and TCGA, provides AEI and REI activity metrics, dsRNA modules, and deep-learning reliability scoring (REDInet), with rich cross-links to ELIXIR core resources. See the portal and the downloads page for access.
