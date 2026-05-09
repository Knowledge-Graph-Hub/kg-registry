---
activity_status: active
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: david.wishart@ualberta.ca
    label: David Wishart
    orcid: 0000-0002-3207-2434
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://smpdb.ca/
    label: The Metabolomics Innovation Centre (TMIC)
creation_date: '2025-12-03T00:00:00Z'
description: The Small Molecule Pathway Database (SMPDB) is an interactive, visual database containing more than 30,000 small molecule pathways found in humans. SMPDB provides detailed pathway diagrams for metabolic pathways, metabolic disease pathways, metabolite signaling pathways, and drug-action pathways. All pathways include information on relevant organs, subcellular compartments, cofactors, protein locations, metabolite locations, chemical structures, and protein quaternary structures. Each small molecule is hyperlinked to HMDB or DrugBank and each protein is hyperlinked to UniProt.
domains:
  - pathways
  - biological systems
  - drug discovery
  - chemistry and biochemistry
homepage_url: https://smpdb.ca/
id: smpdb
infores_id: smpdb
last_modified_date: '2025-12-03T00:00:00Z'
layout: resource_detail
name: Small Molecule Pathway Database
products:
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: cancer-genome-interpreter.clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Core UniBioMap graph edges file.
    format: csv
    id: unibiomap.links
    name: UniBioMap Graph Links
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 1406201678
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
  - category: GraphProduct
    description: Auxiliary UniBioMap graph annotations and metadata.
    format: tsv
    id: unibiomap.auxs
    name: UniBioMap Graph Auxiliaries
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 591290539
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
  - category: GraphProduct
    description: Predicted UniBioMap graph edges with confidence scores.
    format: csv
    id: unibiomap.pred
    name: UniBioMap Predicted Graph
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 2484982268
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
  - category: GraphProduct
    description: Full unfiltered UniBioMap predicted graph edges file.
    format: csv
    id: unibiomap.pred.full
    name: UniBioMap Predicted Graph (Full)
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 6303875907
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - Wishart DS
      - Frolkis A
      - Knox C
      - et al.
    id: https://doi.org/10.1093/nar/gkp1002
    preferred: true
    title: 'SMPDB: The Small Molecule Pathway Database'
    year: '2010'
  - authors:
      - Jewison T
      - Su Y
      - Disfany FM
      - et al.
    id: https://doi.org/10.1093/nar/gkt1067
    title: 'SMPDB 2.0: Big Improvements to the Small Molecule Pathway Database'
    year: '2014'
synonyms:
  - SMPDB
taxon:
  - NCBITaxon:9606
---

# Small Molecule Pathway Database

SMPDB is a comprehensive visual database of human small molecule pathways, providing detailed interactive pathway diagrams for metabolic, disease, signaling, and drug-action pathways with extensive molecular and structural annotations.
