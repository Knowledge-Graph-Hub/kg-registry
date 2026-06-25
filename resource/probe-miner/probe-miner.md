---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.icr.ac.uk/
  label: Institute of Cancer Research
creation_date: '2026-06-18T00:00:00Z'
description: Probe Miner is a public resource for the objective, quantitative, and
  data-driven assessment of chemical probes for protein targets, developed at the
  Institute of Cancer Research. It integrates large-scale, publicly available medicinal
  chemistry and bioactivity data to score small molecules against six objective criteria,
  enabling researchers to evaluate the suitability of compounds as chemical probes
  for a given protein target. The resource helps reduce the misuse of poor-quality
  chemical probes in target validation and chemical biology by surfacing potency,
  selectivity, and cell-based activity evidence in a transparent, reproducible way.
domains:
- drug discovery
- chemistry and biochemistry
- pharmacology
homepage_url: https://probeminer.icr.ac.uk
id: probe-miner
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Probe Miner
products:
- category: GraphicalInterface
  description: Public web interface for searching and browsing objective, data-driven
    assessments of chemical probes for protein targets, with per-compound scores across
    six quantitative chemical probe quality criteria.
  format: http
  id: probe-miner.website
  name: Probe Miner Web Resource
  original_source:
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_url: https://probeminer.icr.ac.uk
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
publications:
- authors:
  - Antolin AA
  - Tym JE
  - Komianou A
  - Collins I
  - Workman P
  - Al-Lazikani B
  doi: 10.1016/j.chembiol.2017.11.004
  id: https://pubmed.ncbi.nlm.nih.gov/29249694/
  journal: Cell Chem Biol
  preferred: true
  title: Objective, Quantitative, Data-Driven Assessment of Chemical Probes
  year: '2018'
---
# Probe Miner

## Overview

Probe Miner is a public, data-driven resource developed at the Institute of Cancer Research that provides objective, quantitative assessments of chemical probes for protein targets. By mining large-scale public medicinal chemistry and bioactivity data, it scores small molecules against a set of objective criteria so that researchers can judge whether a compound is a suitable chemical probe for a given target.

## Scope & Content

- Objective, quantitative scoring of compounds across six chemical probe quality criteria
- Coverage of small-molecule potency, selectivity, and cell-based activity evidence
- Assessment of chemical probes across a broad space of human protein targets
- Transparent, reproducible evaluations derived from public bioactivity data

## Use Cases

- Selecting high-quality chemical probes for target validation
- Avoiding poor-quality or non-selective probes in chemical biology experiments
- Comparing candidate compounds for a protein target of interest
- Providing upstream probe-assessment data to integrative knowledge graphs (e.g., MolePro / molecular-data-kp)

## Access

The Probe Miner web resource is publicly available and can be searched and browsed by protein target or compound.

## Citation & Attribution

When using Probe Miner, cite Antolin et al. (2018), "Objective, Quantitative, Data-Driven Assessment of Chemical Probes," Cell Chemical Biology.

## Contact

General inquiries can be directed to the Institute of Cancer Research via its website.