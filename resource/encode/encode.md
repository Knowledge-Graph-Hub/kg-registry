---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: encode-help@lists.stanford.edu
  - contact_type: url
    value: https://www.encodeproject.org/
  label: ENCODE Data Coordination Center
creation_date: '2026-05-21T00:00:00Z'
description: The Encyclopedia of DNA Elements (ENCODE) is an NHGRI-funded international
  consortium and data resource that catalogs functional elements in the human genome
  and related model systems using large-scale functional genomics assays, standardized
  processing pipelines, and openly accessible metadata.
domains:
- genomics
homepage_url: https://www.encodeproject.org/
id: encode
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ENCODE
products:
- category: GraphicalInterface
  description: Main ENCODE portal for searching, browsing, and filtering released
    functional genomics experiments, biosamples, files, and annotations
  format: http
  id: encode.portal
  name: ENCODE Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: encode
  product_url: https://www.encodeproject.org/
- category: ProgrammingInterface
  connection_url: https://www.encodeproject.org/search/?type=Experiment&format=json
  description: REST API for retrieving ENCODE metadata and released objects in JSON
    format and performing structured search queries
  format: json
  id: encode.api
  is_public: true
  name: ENCODE REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: encode
  product_url: https://www.encodeproject.org/help/rest-api/
- category: GraphicalInterface
  description: Experiment matrix interface for browsing released ENCODE experiments
    across assays, biosamples, targets, and organisms
  format: http
  id: encode.experiment-matrix
  name: ENCODE Experiment Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: encode
  product_url: https://www.encodeproject.org/matrix/?type=Experiment
- category: GraphicalInterface
  description: Encyclopedia annotations view for released candidate cis-regulatory
    elements and other integrated ENCODE annotation products
  format: http
  id: encode.annotations
  name: ENCODE Encyclopedia Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: encode
  product_url: https://www.encodeproject.org/search/?type=Annotation&encyclopedia_version=current&annotation_type=candidate+Cis-Regulatory+Elements&annotation_type=chromatin+state&annotation_type=representative+DNase+hypersensitivity+sites&status=released
- category: GraphProduct
  description: Neo4j knowledge graph integrating transcription factor target libraries,
    coexpression networks, and benchmark datasets used by the ChEA3 resource
  dump_format: neo4j
  format: neo4j
  id: chea-kg.graph
  name: ChEA-KG Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries, benchmark
    datasets, and additional supporting libraries
  format: http
  id: chea-kg.libraries
  name: ChEA-KG Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries and
    benchmark datasets
  format: http
  id: chea.libraries
  name: ChEA Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
- category: GraphProduct
  description: Neo4j knowledge graph containing lncRNAs, protein-coding genes, regulatory
    interactions, and disease associations
  dump_format: neo4j
  format: neo4j
  id: lncrnalyzr.graph
  name: lncRNAlyzr Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lncrnalyzr
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: doid
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
publications:
- authors:
  - The ENCODE Project Consortium
  id: doi:10.1038/nature11247
  journal: Nature
  preferred: true
  title: An integrated encyclopedia of DNA elements in the human genome
  year: '2012'
repository: https://github.com/ENCODE-DCC/encoded
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# ENCODE

The Encyclopedia of DNA Elements (ENCODE) is an ongoing international consortium funded by NHGRI to identify and organize functional elements in the genome, including regulatory elements, protein-binding sites, chromatin features, and RNA-level signals. The ENCODE portal serves as the main public access point for consortium experiments, processed files, metadata, standards, and integrative annotations.

Current ENCODE portal documentation emphasizes standardized assays, shared experimental guidelines, uniform analysis pipelines, and explicit quality metrics across major assay classes such as ChIP-seq, ATAC-seq, DNase-seq, RNA-seq, eCLIP, methylation assays, chromatin conformation assays, and single-cell methods. The public REST API exposes released ENCODE objects in JSON and supports structured programmatic search over experiments, biosamples, files, publications, and annotations.

## Access

- Main portal: [ENCODE Portal](https://www.encodeproject.org/)
- REST API documentation: [ENCODE REST API](https://www.encodeproject.org/help/rest-api/)
- Experiment browser: [Experiment Matrix](https://www.encodeproject.org/matrix/?type=Experiment)
- Integrative annotations: [ENCODE Encyclopedia Annotations](https://www.encodeproject.org/search/?type=Annotation&encyclopedia_version=current&annotation_type=candidate+Cis-Regulatory+Elements&annotation_type=chromatin+state&annotation_type=representative+DNase+hypersensitivity+sites&status=released)

## Automated Evaluation

- View the automated evaluation: [encode automated evaluation](encode_eval_automated.html)