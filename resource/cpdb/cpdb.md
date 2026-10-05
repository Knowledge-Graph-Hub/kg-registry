---
activity_status: active
category: Aggregator
creation_date: '2025-11-19T00:00:00Z'
description: ConsensusPathDB integrates molecular interaction data from over 30 public
  databases, including protein-protein, genetic, metabolic, signaling, gene regulatory
  and drug-target interactions. It provides comprehensive pathway and functional analysis
  tools, allowing users to explore molecular networks and pathways from multiple sources
  through a unified interface. The frames-based site remains reachable and reports
  Release 35 for the human instance, dated June 5, 2021.
domains:
- pathways
- proteomics
- systems biology
- biomedical
- chemistry and biochemistry
- protein interactions
homepage_url: http://cpdb.molgen.mpg.de/
id: cpdb
infores_id: cpdb
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: http://cpdb.molgen.mpg.de/
  label: Free for academic use; commercial users must contact the developers (integrated
    interaction data inherits the license terms of the contributing source databases)
name: ConsensusPathDB
products:
- category: GraphicalInterface
  description: Web-based interface for integrated pathway and interaction analysis
    from multiple databases
  format: http
  id: cpdb.web
  name: ConsensusPathDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpdb
  product_url: http://cpdb.molgen.mpg.de/
- category: Product
  description: Download and access page for ConsensusPathDB data and service assets
  format: http
  id: cpdb.downloads
  name: ConsensusPathDB Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpdb
  product_url: http://cpdb.molgen.mpg.de/download
  warnings: []
- category: ProgrammingInterface
  description: SOAP web service description for ConsensusPathDB programmatic access
  format: xml
  id: cpdb.wsdl
  name: ConsensusPathDB SOAP WSDL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpdb
  product_url: http://cpdb.molgen.mpg.de/download/CPDB.wsdl
- category: GraphProduct
  description: Knowledge graph connecting rare diseases with genes, drugs, pathways,
    and medical images
  edge_count: 22293
  id: rdbridge.graph
  name: RDBridge Knowledge Graph
  node_count: 11704
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdbridge
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: cpdb
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
- category: ProgrammingInterface
  description: MyGene.info REST API (v3) for gene query and annotation retrieval by Entrez
    or Ensembl gene id, with batch POST queries and field filtering. Returns JSON documents
    merged from the integrated sources.
  format: http
  id: mygene.api
  infores_id: mygene-info
  name: MyGene.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://mygene.info/v3/api
- category: Product
  compression: zip
  description: Academic branch of dbNSFP (v5.4a at time of curation, about 50 GB), a ZIP of
    gzipped, tab-delimited per-chromosome variant tables, the gene table, column descriptions
    and the search_dbNSFP Java program. Variant tables are also offered as a single tabix-indexed
    BGZF file per genome build (GRCh37, GRCh38) for Ensembl VEP and SnpSift. Includes all
    upstream scores that are free for academic use. Free for academic and non-commercial users
    after registration with an institutional email; download links are issued on request.
  format: tsv
  id: dbnsfp.academic
  license:
    id: https://creativecommons.org/licenses/by-nc-nd/4.0/
    label: CC BY-NC-ND 4.0
  name: dbNSFP Academic Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/download
- category: Product
  compression: zip
  description: Commercial branch of dbNSFP (v5.4c at time of curation), in the same format
    as the academic branch but excluding CADD, VEST, M-CAP, MutScore, PolyPhen-2, PrimateAI
    and RGC Million Exome data, whose authors require separate commercial licenses. Available
    to subscribers under a paid license from Genos Bioinformatics.
  format: tsv
  id: dbnsfp.commercial
  license:
    id: https://www.dbnsfp.org/license
    label: Commercial license (Genos Bioinformatics LLC)
  name: dbNSFP Commercial Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/license
publications:
- authors:
  - Atanas Kamburov
  - Konstantin Pentchev
  - Hanna Galicka
  - Christoph Wierling
  - Hans Lehrach
  - Ralf Herwig
  doi: 10.1093/nar/gkq1156
  id: doi:10.1093/nar/gkq1156
  journal: Nucleic Acids Research
  preferred: true
  title: 'ConsensusPathDB: toward a more complete picture of cell biology'
  year: '2011'
- authors:
  - Atanas Kamburov
  - Christoph Wierling
  - Hans Lehrach
  - Ralf Herwig
  doi: 10.1093/nar/gkn698
  id: doi:10.1093/nar/gkn698
  journal: Nucleic Acids Research
  title: ConsensusPathDB--a database for integrating human functional interaction
    networks
  year: '2009'
synonyms:
- CPDB
- CPDB-human
- ConsensusPathDB-human
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:4932
---
# ConsensusPathDB

## Overview

ConsensusPathDB is an integrated molecular interaction database that consolidates data from over 30 public databases, including protein-protein interactions, genetic interactions, metabolic pathways, signaling pathways, gene regulatory interactions, and drug-target interactions. It provides a comprehensive platform for pathway and functional analysis of molecular networks.

The frames-based website remains reachable and reports Release 35 for the human instance, dated June 5, 2021. The site also links mouse and yeast instances. Historical `/CPDB/download` links are unavailable, but the root access page and SOAP WSDL remain reachable.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cpdb`