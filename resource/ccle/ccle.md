---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: CCLE
creation_date: '2025-03-18T00:00:00Z'
description: CCLE is the Cancer Cell Line Encyclopedia, a collaboration between the
  Broad Institute and the Novartis Institutes for Biomedical Research.
domains:
- health
homepage_url: https://sites.broadinstitute.org/ccle/
id: ccle
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: CCLE
products:
- category: DocumentationProduct
  description: CCLE project site describing the Cancer Cell Line Encyclopedia collaboration, motivations, and project phases.
  format: http
  id: ccle.docs
  name: CCLE Project Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  product_url: https://sites.broadinstitute.org/ccle/
- category: Product
  description: CCLE datasets page linking processed genetic, transcriptomic, proteomic, and metabolomic releases and related DepMap resources.
  format: http
  id: ccle.datasets
  name: CCLE Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  product_url: https://sites.broadinstitute.org/ccle/datasets
- category: Product
  description: ccle OBO
  format: obo
  id: obo-db-ingest.ccle.obo
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 19324
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.obo
- category: Product
  description: ccle OWL
  format: owl
  id: obo-db-ingest.ccle.owl
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 29770
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.owl
- category: Product
  description: ccle OBO Graph JSON
  format: json
  id: obo-db-ingest.ccle.json
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 23282
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.json
- category: MappingProduct
  description: ccle SSSOM
  format: sssom
  id: obo-db-ingest.ccle.sssom.tsv
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 14414
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.sssom.tsv
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: http
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
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: http
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: Product
  description: ccle Nodes TSV
  format: tsv
  id: obo-db-ingest.ccle.tsv
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL-1.0
  name: ccle Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 12188
  product_url: https://w3id.org/biopragmatics/resources/ccle/ccle.tsv
taxon:
- NCBITaxon:9606
---
# CCLE

The Cancer Cell Line Encyclopedia (CCLE) is a large-scale collaboration that
characterizes cancer cell lines across genomic, transcriptomic, proteomic,
epigenetic, metabolomic, and pharmacologic dimensions. It was established to make
well-annotated cancer cell models more useful for target discovery, biomarker
analysis, and drug-response modeling.

In KG-Registry, the owned products for CCLE point to the main project site and
datasets page, while the OBO-DB-Ingest, Bioteque, and INDRA-related entries are
retained as downstream derivative products built from or informed by CCLE data.