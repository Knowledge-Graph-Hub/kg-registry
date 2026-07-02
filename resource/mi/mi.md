---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: luana.licata@gmail.com
  - contact_type: github
    value: luanalicata
  label: Luana Licata
  orcid: 0000-0001-5084-9000
creation_date: '2025-06-04T00:00:00Z'
description: A structured controlled vocabulary for the annotation of experiments
  concerned with protein-protein interactions.
domains:
- biomedical
- general
homepage_url: https://github.com/HUPO-PSI/psi-mi-CV
id: mi
infores_id: mi
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Molecular Interactions Controlled Vocabulary
products:
- category: OntologyProduct
  description: Molecular Interactions Controlled Vocabulary in OWL format
  format: owl
  id: mi.owl
  name: mi.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mi
  product_file_size: 248742
  product_url: http://purl.obolibrary.org/obo/mi.owl
- category: OntologyProduct
  description: Molecular Interactions Controlled Vocabulary in OBO format
  format: obo
  id: mi.obo
  name: mi.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mi
  product_file_size: 169744
  product_url: http://purl.obolibrary.org/obo/mi.obo
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: clinicalkg
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Graph database dump and additional relationship files for the Clinical
    Knowledge Graph.
  format: neo4j
  id: ckg.graph
  latest_version: '1'
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: CKG Graph Database Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: ckg
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: Product
  description: Complete MINT dataset in PSI-MI MITAB 2.7 format accessible via PSICQUIC
    web service.
  format: psi_mi_mitab
  id: mint.mitab.all
  name: MINT MITAB Full Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mint
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/*
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: imex
  - relation_type: prov:wasInfluencedBy
    source: intact
  - relation_type: prov:used
    source: mi
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2026-03-08_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting
    to URL
- category: Product
  description: Human protein interactions from MINT in PSI-MI MITAB format for Homo
    sapiens (NCBITaxon 9606).
  format: psi_mi_mitab
  id: mint.mitab.human
  name: MINT Human Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mint
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/species:human
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: imex
  - relation_type: prov:wasInfluencedBy
    source: intact
  - relation_type: prov:used
    source: mi
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2026-03-08_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting
    to URL
- category: Product
  description: Mouse protein interactions from MINT in PSI-MI MITAB format for Mus
    musculus (NCBITaxon 10090).
  format: psi_mi_mitab
  id: mint.mitab.mouse
  name: MINT Mouse Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mint
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/species:mouse
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: imex
  - relation_type: prov:wasInfluencedBy
    source: intact
  - relation_type: prov:used
    source: mi
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2026-03-08_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-06_ Timeout connecting
    to URL
- category: Product
  description: Drosophila melanogaster protein interactions from MINT in PSI-MI MITAB
    format.
  format: psi_mi_mitab
  id: mint.mitab.drosophila
  name: MINT Drosophila Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mint
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/species:fruit%20fly
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: imex
  - relation_type: prov:wasInfluencedBy
    source: intact
  - relation_type: prov:used
    source: mi
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
  - PSICQUIC query endpoints may stream results without a stable Content-Length header.
- category: Product
  description: Saccharomyces cerevisiae protein interactions from MINT in PSI-MI MITAB
    format.
  format: psi_mi_mitab
  id: mint.mitab.yeast
  name: MINT Yeast Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mint
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query/species:yeast
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: imex
  - relation_type: prov:wasInfluencedBy
    source: intact
  - relation_type: prov:used
    source: mi
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
  - PSICQUIC query endpoints may stream results without a stable Content-Length header.
- category: ProgrammingInterface
  description: PSICQUIC SOAP and REST web services for programmatic access to MINT
    data using Molecular Interactions Query Language (MIQL).
  format: http
  id: mint.psicquic
  name: MINT PSICQUIC Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mint
  product_url: http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: imex
  - relation_type: prov:wasInfluencedBy
    source: intact
  - relation_type: prov:used
    source: mi
publications:
- authors:
  - Henning Hermjakob
  - Luisa Montecchi-Palazzi
  - Gary Bader
  - "J\xE9r\xF4me Wojcik"
  - Lukasz Salwinski
  - Arnaud Ceol
  - Susan Moore
  - Sandra Orchard
  - Ugis Sarkans
  - Christian von Mering
  - Bernd Roechert
  - Sylvain Poux
  - Eva Jung
  - Henning Mersch
  - Paul Kersey
  - Michael Lappe
  - Yixue Li
  - Rong Zeng
  - Debashis Rana
  - Macha Nikolski
  - Holger Husi
  - Christine Brun
  - K Shanker
  - Seth G N Grant
  - Chris Sander
  - Peer Bork
  - Weimin Zhu
  - Akhilesh Pandey
  - Alvis Brazma
  - Bernard Jacq
  - Marc Vidal
  - David Sherman
  - Pierre Legrain
  - Gianni Cesareni
  - Ioannis Xenarios
  - David Eisenberg
  - Boris Steipe
  - Chris Hogue
  - Rolf Apweiler
  doi: 10.1038/nbt926
  id: https://www.ncbi.nlm.nih.gov/pubmed/14755292
  journal: Nat Biotechnol
  preferred: true
  title: The HUPO PSI's molecular interaction format--a community standard for the
    representation of protein interaction data
  year: '2004'
repository: https://github.com/HUPO-PSI/psi-mi-CV
---
## Description

A structured controlled vocabulary for the annotation of experiments concerned with protein-protein interactions.

## Contacts

- Luana Licata (luana.licata@gmail.com) [ORCID: 0000-0001-5084-9000](https://orcid.org/0000-0001-5084-9000)

## Products

### mi.owl

Molecular Interactions Controlled Vocabulary in OWL format

**URL**: [http://purl.obolibrary.org/obo/mi.owl](http://purl.obolibrary.org/obo/mi.owl)

**Format**: owl

### mi.obo

Molecular Interactions Controlled Vocabulary in OBO format

**URL**: [http://purl.obolibrary.org/obo/mi.obo](http://purl.obolibrary.org/obo/mi.obo)

**Format**: obo

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*