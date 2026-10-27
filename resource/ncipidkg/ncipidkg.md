---
id: ncipidkg
name: NCI-PID 2.0 KG
description: The NCI-PID 2.0 Knowledge Graph converts NCI Pathway Interaction Database
  version 2.0 networks into RDF, capturing protein interactions, signaling pathways,
  and post-translational modifications enriched with INDRA evidence metadata.
activity_status: active
homepage_url: https://www.ndexbio.org/index.html#/networkset/7bc65b82-2a2f-11ed-ac45-0ac135e8bacf
contacts:
- category: Individual
  label: Cytoscape and NDEx Team
  contact_details:
  - contact_type: email
    value: support@ndexbio.org
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-09-23T00:00:00Z'
products:
- id: ncipidkg.graph.ttl
  name: NCI-PID 2.0 KG RDF graph
  description: RDF graph converting NCI Pathway Interaction Database version 2.0 networks
    into RDF, enriched with INDRA evidence metadata.
  category: GraphProduct
  format: ttl
  product_url: https://www.ndexbio.org/index.html#/networkset/7bc65b82-2a2f-11ed-ac45-0ac135e8bacf
  original_source:
  - source: ncipidkg
    relation_type: prov:hadPrimarySource
  - source: pid
    relation_type: prov:wasDerivedFrom
  secondary_source:
  - source: indra
    relation_type: prov:wasInfluencedBy
- id: ncipidkg.sparql
  name: NCI-PID 2.0 KG SPARQL
  description: SPARQL endpoint for NCI-PID 2.0 KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ncipidkg/sparql
  original_source:
  - source: ncipidkg
    relation_type: prov:hadPrimarySource
- id: ncipidkg.tpf
  name: NCI-PID 2.0 KG TPF
  description: Triple Pattern Fragments endpoint for NCI-PID 2.0 KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/ncipidkg
  original_source:
  - source: ncipidkg
    relation_type: prov:hadPrimarySource
- category: Product
  description: Downloadable Enrichr gene set libraries (more than 200 libraries across
    transcription, pathways, ontologies, diseases/drugs, cell types, crowd-contributed,
    and legacy categories), each retrievable as a GMT-style tab-delimited text file
    via the geneSetLibrary endpoint (e.g. geneSetLibrary?mode=text&libraryName=KEGG_2021_Human).
    Libraries are compiled from external databases including GO, KEGG, Reactome, WikiPathways,
    MSigDB, ChEA/ENCODE, GTEx, ARCHS4, LINCS L1000, GEO, DisGeNET, OMIM, GWAS Catalog,
    HPO, MGI, CellMarker, and others.
  format: txt
  id: enrichr.libraries
  name: Enrichr Gene Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: ncipidkg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://maayanlab.cloud/Enrichr/#libraries

domains:
- biomedical
- pathways
- signal transduction
---
NCI-PID 2.0 KG

## Description

The NCI-PID 2.0 Knowledge Graph converts NCI Pathway Interaction Database version 2.0 networks into RDF, capturing protein interactions, signaling pathways, and post-translational modifications enriched with INDRA evidence metadata.

The OKN registry entry notes that the graph is built by converting 196 NCI-PID 2.0 pathway networks from Cytoscape CX2 into RDF using standard biological ontologies including RO, GO, SIO, and UniProt identifiers.

Relationship assertions are reified so that evidence counts and source attribution can be attached directly to individual pathway statements, making the graph useful for provenance-aware pathway querying and downstream analysis.

*This resource was automatically synchronized from the FRINK OKN registry.*
