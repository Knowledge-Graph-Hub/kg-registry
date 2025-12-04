---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "rgd.data@mcw.edu"
      - contact_type: url
        value: "https://rgd.mcw.edu/"
    label: Medical College of Wisconsin
creation_date: '2025-12-03T00:00:00Z'
description: The Rat Genome Database (RGD) curates and integrates rat genomic and phenotype data, and provides tools for genomics, physiology and functional genomics in rats. RGD contains comprehensive data on genes, QTLs, strains, and genomic elements for rat, human, mouse, chinchilla, dog, cat, pig, bonobo, squirrel, green monkey, and naked mole rat. The database includes extensive ontology annotations (RDO, CMO, ChEBI, EFO, GO, HP, MMO, MP, PW, RS, VT, XCO), variant information, pathway data, and disease relationships.
domains:
  - genomics
  - biological systems
  - organisms
homepage_url: https://rgd.mcw.edu/
id: "rgd"
infores_id: "rgd"
last_modified_date: '2025-12-03T00:00:00Z'
layout: resource_detail
name: Rat Genome Database
repository: https://github.com/rat-genome-database
synonyms:
  - RGD
taxon:
  - NCBITaxon:10116
products:
  - category: GraphProduct
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: "disgenet.data"
    name: DisGeNET Data
    original_source:
      - clingen
      - clinvar
      - mgd
      - rgd
      - orphanet
      - psygenet
      - uniprot
      - disgenet
      - hp
      - gwascatalog
      - phewascat
      - ukbiobank
      - finngen
      - clinicaltrialsgov
    product_url: https://www.disgenet.com/
    secondary_source:
      - disgenet
  - category: GraphicalInterface
    description: Web portal for searching and browsing ncRNA sequences, structures, and annotations
    format: http
    id: "rnacentral.portal"
    name: RNAcentral Portal
    original_source:
      - 5srrnadb
      - crd
      - dictybase
      - ena
      - ensembl
      - evlncrnas
      - expressionatlas
      - flybase
      - genecards
      - greengenes
      - gtrnadb
      - hgnc
      - intact
      - lncbase
      - lncbook
      - lncipedia
      - lncrnadb
      - malacards
      - mgnify
      - mirbase
      - mirgenedb
      - modomics
      - noncode
      - pdbe
      - pirbase
      - plncdb
      - pombase
      - rdp
      - rediportal
      - rfam
      - rgd
      - ribocentre
      - ribovision
      - sgd
      - silva
      - snodb
      - snopy
      - snornadatabase
      - srpdb
      - tair
      - tarbase
      - tmrnawebsite
      - zfin
      - zwd
      - rnacentral
    product_url: https://rnacentral.org/
  - category: ProgrammingInterface
    description: REST API for programmatic access to RNAcentral data
    format: http
    id: "rnacentral.api"
    name: RNAcentral REST API
    original_source:
      - 5srrnadb
      - crd
      - dictybase
      - ena
      - ensembl
      - evlncrnas
      - expressionatlas
      - flybase
      - genecards
      - greengenes
      - gtrnadb
      - hgnc
      - intact
      - lncbase
      - lncbook
      - lncipedia
      - lncrnadb
      - malacards
      - mgnify
      - mirbase
      - mirgenedb
      - modomics
      - noncode
      - pdbe
      - pirbase
      - plncdb
      - pombase
      - rdp
      - rediportal
      - rfam
      - rgd
      - ribocentre
      - ribovision
      - sgd
      - silva
      - snodb
      - snopy
      - snornadatabase
      - srpdb
      - tair
      - tarbase
      - tmrnawebsite
      - zfin
      - zwd
      - rnacentral
    product_url: https://rnacentral.org/api
  - category: Product
    description: FTP archive with current and archived release files (sequences and annotations)
    format: http
    id: "rnacentral.ftp"
    name: RNAcentral FTP Archive
    original_source:
      - 5srrnadb
      - crd
      - dictybase
      - ena
      - ensembl
      - evlncrnas
      - expressionatlas
      - flybase
      - genecards
      - greengenes
      - gtrnadb
      - hgnc
      - intact
      - lncbase
      - lncbook
      - lncipedia
      - lncrnadb
      - malacards
      - mgnify
      - mirbase
      - mirgenedb
      - modomics
      - noncode
      - pdbe
      - pirbase
      - plncdb
      - pombase
      - rdp
      - rediportal
      - rfam
      - rgd
      - ribocentre
      - ribovision
      - sgd
      - silva
      - snodb
      - snopy
      - snornadatabase
      - srpdb
      - tair
      - tarbase
      - tmrnawebsite
      - zfin
      - zwd
      - rnacentral
    product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
  - category: DataModelProduct
    description: Public PostgreSQL database for direct SQL access to RNAcentral data
    format: postgres
    id: "rnacentral.public-db"
    name: RNAcentral Public Postgres Database
    original_source:
      - 5srrnadb
      - crd
      - dictybase
      - ena
      - ensembl
      - evlncrnas
      - expressionatlas
      - flybase
      - genecards
      - greengenes
      - gtrnadb
      - hgnc
      - intact
      - lncbase
      - lncbook
      - lncipedia
      - lncrnadb
      - malacards
      - mgnify
      - mirbase
      - mirgenedb
      - modomics
      - noncode
      - pdbe
      - pirbase
      - plncdb
      - pombase
      - rdp
      - rediportal
      - rfam
      - rgd
      - ribocentre
      - ribovision
      - sgd
      - silva
      - snodb
      - snopy
      - snornadatabase
      - srpdb
      - tair
      - tarbase
      - tmrnawebsite
      - zfin
      - zwd
      - rnacentral
    product_url: https://rnacentral.org/help/public-database
---

# Rat Genome Database

RGD is a multispecies genomics and phenomics database, providing comprehensive data for rat and other model organisms including genes, QTLs, strains, variants, pathways, and disease associations with extensive ontological annotations.
