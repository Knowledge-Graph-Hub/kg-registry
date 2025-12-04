---
activity_status: active
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: "david.wishart@ualberta.ca"
    label: David Wishart
    orcid: 0000-0002-3207-2434
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://smpdb.ca/"
    label: The Metabolomics Innovation Centre (TMIC)
creation_date: '2025-12-03T00:00:00Z'
description: The Small Molecule Pathway Database (SMPDB) is an interactive, visual database containing more than 30,000 small molecule pathways found in humans. SMPDB provides detailed pathway diagrams for metabolic pathways, metabolic disease pathways, metabolite signaling pathways, and drug-action pathways. All pathways include information on relevant organs, subcellular compartments, cofactors, protein locations, metabolite locations, chemical structures, and protein quaternary structures. Each small molecule is hyperlinked to HMDB or DrugBank and each protein is hyperlinked to UniProt.
domains:
  - pathways
  - biological systems
  - drug discovery
  - chemistry and biochemistry
homepage_url: https://smpdb.ca/
id: "smpdb"
infores_id: smpdb
last_modified_date: '2025-12-03T00:00:00Z'
layout: resource_detail
name: Small Molecule Pathway Database
publications:
  - authors:
      - Wishart DS
      - Frolkis A
      - Knox C
      - et al.
    id: "https://doi.org/10.1093/nar/gkp1002"
    preferred: true
    title: 'SMPDB: The Small Molecule Pathway Database'
    year: "2010"
  - authors:
      - Jewison T
      - Su Y
      - Disfany FM
      - et al.
    id: "https://doi.org/10.1093/nar/gkt1067"
    title: 'SMPDB 2.0: Big Improvements to the Small Molecule Pathway Database'
    year: "2014"
synonyms:
  - SMPDB
taxon:
  - NCBITaxon:9606
products:
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: "clinicalkg.graph"
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - uniprot
      - tissues
      - string
      - stitch
      - smpdb
      - signor
      - sider
      - refseq
      - reactome
      - phosphositeplus
      - pfam
      - oncokb
      - mutationds
      - intact
      - hpa
      - hmdb
      - hgnc
      - gwascatalog
      - foodb
      - drugbank
      - disgenet
      - diseases
      - dgidb
      - corum
      - cancer-genome-interpreter
      - doid
      - bto
      - efo
      - go
      - hp
      - snomedct
      - mod
      - mi
      - ms
      - uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: "cancer-genome-interpreter.clinicalkg.graph"
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - uniprot
      - tissues
      - string
      - stitch
      - smpdb
      - signor
      - sider
      - refseq
      - reactome
      - phosphositeplus
      - pfam
      - oncokb
      - mutationds
      - intact
      - hpa
      - hmdb
      - hgnc
      - gwascatalog
      - foodb
      - drugbank
      - disgenet
      - diseases
      - dgidb
      - corum
      - cancer-genome-interpreter
      - doid
      - bto
      - efo
      - go
      - hp
      - snomedct
      - mod
      - mi
      - ms
      - uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
---

# Small Molecule Pathway Database

SMPDB is a comprehensive visual database of human small molecule pathways, providing detailed interactive pathway diagrams for metabolic, disease, signaling, and drug-action pathways with extensive molecular and structural annotations.
