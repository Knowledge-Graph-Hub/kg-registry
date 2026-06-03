---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.mskcc.org/
    id: mskcc
    label: Memorial Sloan Kettering Cancer Center
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.utoronto.ca/
    id: utoronto
    label: University of Toronto
creation_date: '2026-06-02T00:00:00Z'
description: Pathway Commons is a centralized web resource that aggregates biological pathway and molecular interaction data into standardized BioPAX and related network formats for pathway analysis and systems biology.
domains:
  - pathways
  - systems biology
  - biomedical
homepage_url: https://www.pathwaycommons.org/
id: pathwaycommons
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0 (aggregated content)
name: Pathway Commons
products:
  - category: GraphicalInterface
    description: Pathway Commons web interface for browsing, searching, and visualizing integrated biological pathways and molecular interactions.
    format: http
    id: pathwaycommons.web
    is_public: true
    name: Pathway Commons Web Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
    product_url: https://www.pathwaycommons.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pathway-commons
  - category: ProgrammingInterface
    description: Pathway Commons REST API for querying integrated pathway and molecular interaction data.
    format: http
    id: pathwaycommons.api
    is_public: true
    name: Pathway Commons REST API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
    product_url: https://www.pathwaycommons.org/pc2/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pathway-commons
  - category: Product
    description: Pathway Commons downloadable pathway datasets in BioPAX, SIF, GMT, and related tabular formats.
    format: mixed
    id: pathwaycommons.downloads
    name: Pathway Commons Data Downloads
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
    product_url: https://download.baderlab.org/PathwayCommons/PC2/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pathway-commons
  - category: GraphProduct
    description: Downloadable GeneMANIA interaction network data organized by release and organism, with individual networks, combined default networks, metadata, and identifier mapping tables in plain tab-delimited text files
    format: txt
    id: genemania.networks
    latest_version: current
    name: GeneMANIA Interaction Network Archive
    original_source:
      - relation_type: prov:hadPrimarySource
        source: genemania
    product_url: https://genemania.org/data/current/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: geo
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: intact
      - relation_type: prov:wasDerivedFrom
        source: mint
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: hprd
publications:
  - authors:
      - Ethan G Cerami
      - Benjamin E Gross
      - Emek Demir
      - Igor Rodchenkov
      - Ozgun Babur
      - Nadia Anwar
    doi: 10.1093/nar/gkq1039
    id: doi:10.1093/nar/gkq1039
    journal: Nucleic Acids Research
    preferred: true
    title: Pathway Commons, a web resource for biological pathway data
    year: '2011'
synonyms:
  - Pathway Commons
warnings:
  - This is an unhyphenated legacy registry identifier for Pathway Commons. The canonical curated registry entry is pathway-commons.
---

# Pathway Commons

Pathway Commons aggregates biological pathway and molecular interaction data for
systems biology reuse. This unhyphenated registry page preserves provenance from
downstream resources that cite `pathwaycommons`; the canonical KG-Registry entry
is `pathway-commons`.
