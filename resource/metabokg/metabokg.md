---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: matthieu.feraud@univ-cotedazur.fr
  label: Matthieu Feraud
creation_date: '2026-06-02T00:00:00Z'
description: MetaboKG is an analysis-centric knowledge graph framework for untargeted
  metabolomics. It transforms public mass-spectrometry repository outputs, GNPS molecular-networking
  jobs, library annotations, confidence evidence, sample metadata, and environmental
  and taxonomic context into RDF knowledge graphs that preserve links between annotations
  and their analytical artifacts, samples, and studies.
domains:
- chemistry and biochemistry
- biomedical
- microbiome
- environment
homepage_url: https://github.com/HolobiomicsLab/MetaBoKG
id: metabokg
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: MetaboKG
products:
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
  id: metabokg.graph
  latest_version: arXiv v1 demonstration
  name: MetaboKG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://github.com/HolobiomicsLab/MetaBoKG
  secondary_source:
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: ncit
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: prov-o
  - relation_type: prov:used
    source: dcat
  - relation_type: prov:used
    source: afo
  warnings:
  - No static public graph release or hosted endpoint was available in the GitHub
    repository when curated on 2026-06-02; the repository documents local Turtle materialization
    and Virtuoso loading.
- category: ProcessProduct
  description: Source-code workflow that fetches PubMed and PMC context, extracts
    GNPS and MassIVE identifiers, downloads GNPS job archives, materializes RDF with
    RML mappings, loads Virtuoso, and runs competency-question SPARQL queries.
  format: http
  id: metabokg.workflow
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG Transformation Workflow
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_file_size: 1682
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/blob/main/main.py
  repository: https://github.com/HolobiomicsLab/MetaBoKG
- category: DataModelProduct
  description: Turtle schema files defining MetaBoKG classes, properties, and ReDU
    class hierarchies used by the generated knowledge graph.
  id: metabokg.schema
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG RDF Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/Schema
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ms
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: envo
  - relation_type: prov:wasInformedBy
    source: ncit
  - relation_type: prov:wasInformedBy
    source: uberon
  - relation_type: prov:wasInformedBy
    source: chmo
  - relation_type: prov:wasInformedBy
    source: sio
  - relation_type: prov:wasInformedBy
    source: prov-o
  - relation_type: prov:wasInformedBy
    source: dcat
  - relation_type: prov:wasInformedBy
    source: afo
- category: MappingProduct
  description: RML mappings and configuration templates used to transform GNPS, molecular
    networking, feature-based molecular networking, and ReDU data into RDF.
  format: http
  id: metabokg.rml_mappings
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG RML Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/mapping/rml
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gnps
  - relation_type: prov:wasInformedBy
    source: massive
  - relation_type: prov:wasInformedBy
    source: redu
publications:
- authors:
  - Matthieu Feraud
  - Dina Boukhajou
  - Fabien Gandon
  - Louis-Felix Nothias
  doi: 10.48550/arXiv.2605.24706
  id: arXiv:2605.24706
  journal: arXiv
  preferred: true
  title: 'MetaboKG: An Analysis-centric Knowledge Graph Framework for Untargeted Metabolomics'
  year: '2026'
repository: https://github.com/HolobiomicsLab/MetaBoKG
synonyms:
- MetaBoKG
warnings:
- The GitHub repository README states Apache License 2.0, but the repository did not
  expose a machine-readable GitHub license record when checked on 2026-06-02.
---
# MetaboKG

MetaboKG is an analysis-centric knowledge graph framework for untargeted metabolomics. It connects public repository metadata, GNPS molecular-networking results, spectral annotations, confidence evidence, sample context, and controlled vocabulary terms so that metabolomics annotations can be explored across analyses with SPARQL.

The public repository provides the transformation workflow, RDF schema files, RML mappings, Virtuoso loading scripts, and competency-question queries. The demonstrated graph materializes per-job Turtle files locally and loads them into named Virtuoso graphs; no static public graph archive or hosted endpoint was available at curation time.