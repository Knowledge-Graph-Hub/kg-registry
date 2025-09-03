---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.hmdb.ca/w/contact"
    label: Human Metabolome Database (HMDB)
creation_date: '2025-08-12T00:00:00Z'
description: The Human Metabolome Database (HMDB) is a comprehensive curated knowledgebase of small molecule metabolites found in the human body, integrating chemical, clinical, biochemical, spectral, and physiological data along with associated enzyme, transporter, and disease information to support metabolomics, biomarker discovery, systems biology, and precision medicine research.
domains: []
homepage_url: https://www.hmdb.ca/
id: "hmdb"
last_modified_date: '2025-09-03T00:00:00Z'
layout: resource_detail
license:
  id: "https://www.hmdb.ca/downloads"
  label: HMDB Data Use (non-commercial without permission)
name: Human Metabolome Database
products:
  - category: GraphicalInterface
    description: Web portal providing integrated search, metabolite pages (MetaboCards), spectra, pathways, and download access
    format: http
    id: "hmdb.portal"
    name: HMDB Web Portal
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/
  - category: Product
    description: All metabolite metabolizing enzyme protein sequences (FASTA)
    format: fasta
    id: "hmdb.fasta.enzymes"
    name: HMDB Enzyme Protein Sequences (FASTA)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#protein-gene-sequences
  - category: Product
    description: All metabolite metabolizing enzyme gene sequences (FASTA)
    format: fasta
    id: "hmdb.fasta.genes"
    name: HMDB Gene Sequences (FASTA)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#protein-gene-sequences
  - category: Product
    description: All metabolite structures (SDF)
    format: sdf
    id: "hmdb.structures.sdf"
    name: HMDB Metabolite Structures (SDF)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#structures
  - category: Product
    description: All metabolites dataset (XML)
    format: xml
    id: "hmdb.xml.metabolites"
    name: HMDB All Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: All proteins dataset (XML)
    format: xml
    id: "hmdb.xml.proteins"
    name: HMDB All Proteins (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Urine metabolites subset (XML)
    format: xml
    id: "hmdb.xml.metabolites.urine"
    name: HMDB Urine Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Serum metabolites subset (XML)
    format: xml
    id: "hmdb.xml.metabolites.serum"
    name: HMDB Serum Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Cerebrospinal fluid (CSF) metabolites subset (XML)
    format: xml
    id: "hmdb.xml.metabolites.csf"
    name: HMDB CSF Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Saliva metabolites subset (XML)
    format: xml
    id: "hmdb.xml.metabolites.saliva"
    name: HMDB Saliva Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Feces metabolites subset (XML)
    format: xml
    id: "hmdb.xml.metabolites.feces"
    name: HMDB Feces Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Sweat metabolites subset (XML)
    format: xml
    id: "hmdb.xml.metabolites.sweat"
    name: HMDB Sweat Metabolites (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#metabolite-protein-xml
  - category: Product
    description: Mass spectra image files archive
    compression: zip
    id: "hmdb.spectra.mass.images"
    name: HMDB Mass Spectra Images
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: NMR spectra FID files archive
    compression: zip
    id: "hmdb.spectra.nmr.fid"
    name: HMDB NMR Spectra FID Files
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Raw NMR peaklist text files archive
    format: txt
    id: "hmdb.spectra.nmr.peaklist"
    name: HMDB NMR Peaklists (TXT)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Predicted GC-MS spectra peaklist text files archive
    format: txt
    id: "hmdb.spectra.gc.predicted.txt"
    name: HMDB GC-MS Predicted Peaklists (TXT)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Predicted MS-MS spectra peaklist text files archive
    format: txt
    id: "hmdb.spectra.msms.predicted.txt"
    name: HMDB MS-MS Predicted Peaklists (TXT)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Experimental MS-MS spectra peaklist text files archive
    format: txt
    id: "hmdb.spectra.msms.experimental.txt"
    name: HMDB MS-MS Experimental Peaklists (TXT)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: All raw spectra peaklists (aggregated TXT archive)
    format: txt
    id: hmdb.spectra.all.peaklists
    name: HMDB All Raw Spectra Peaklists (TXT)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: NMR spectra collection (XML)
    format: xml
    id: "hmdb.spectra.nmr.xml"
    name: HMDB NMR Spectra (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Predicted GC-MS spectra collection (XML)
    format: xml
    id: "hmdb.spectra.gc.predicted.xml"
    name: HMDB GC-MS Predicted Spectra (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Experimental GC-MS spectra collection (XML)
    format: xml
    id: "hmdb.spectra.gc.experimental.xml"
    name: HMDB GC-MS Experimental Spectra (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Predicted MS-MS spectra collection (XML)
    format: xml
    id: "hmdb.spectra.msms.predicted.xml"
    name: HMDB MS-MS Predicted Spectra (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: Experimental MS-MS spectra collection (XML)
    format: xml
    id: "hmdb.spectra.msms.experimental.xml"
    name: HMDB MS-MS Experimental Spectra (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
  - category: Product
    description: All spectra files aggregate (XML)
    format: xml
    id: "hmdb.spectra.all.xml"
    name: HMDB All Spectra (XML)
    original_source:
      - hmdb
    product_url: https://www.hmdb.ca/downloads#spectra
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
      - do
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
    description: HMDB Automat
    format: kgx-jsonl
    id: "automat.hmdb"
    infores_id: "automat-hmdb"
    name: hmdb_automat
    original_source:
      - hmdb
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/HMDB_Automat/6715124699b6dbf0/
    secondary_source:
      - automat
---

## Overview

HMDB integrates chemical, clinical, biochemical, and spectral information for more than 200,000 human metabolites, linking each to rich metadata (biofluid concentrations, pathways, spectra, disease associations, enzymes, and transporters). Download packages provide structured XML, spectral collections, and sequence datasets. Use of large portions of HMDB requires proper citation and (for commercial reuse) permission.

## Citation

Please cite the core HMDB publications (HMDB 1.0–5.0) as listed on the website; for current analyses, the HMDB 5.0 paper (Nucleic Acids Research 2022, D622–D631) is recommended.

## Licensing & Use

HMDB data are freely available for academic/non-commercial research with appropriate citation. Commercial reuse requires explicit permission; see the downloads page for terms.

## Contact

Contact form available via the portal for inquiries and permissions.
