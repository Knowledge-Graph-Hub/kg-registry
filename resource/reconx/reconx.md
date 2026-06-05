---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.vmh.life/
    label: Thiele/Palsson groups (Virtual Metabolic Human)
creation_date: '2026-06-03T00:00:00Z'
description: ReconX refers to the Recon series of genome-scale reconstructions of human metabolism, beginning with Recon 1 - the global reconstruction of the human metabolic network based on genomic and bibliomic data. These reconstructions account for thousands of metabolic reactions, metabolites, and gene-protein-reaction associations, providing a computable, constraint-based model of human metabolism. The reconstructions are reused by pathway aggregators and are maintained through the Virtual Metabolic Human (VMH) and BiGG Models resources.
domains:
  - pathways
  - chemistry and biochemistry
  - systems biology
  - genomics
homepage_url: https://www.vmh.life/
id: reconx
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ReconX
products:
  - category: GraphicalInterface
    description: Virtual Metabolic Human web portal for browsing and querying the Recon human metabolic reconstruction, including reactions, metabolites, genes, and associated microbiota and nutrition data.
    format: http
    id: reconx.vmh
    name: Virtual Metabolic Human Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: reconx
    product_url: https://www.vmh.life/
  - category: DataModelProduct
    description: Genome-scale human metabolic reconstruction model (Recon) distributed as a constraint-based model, available in SBML and related systems biology formats.
    format: sbml
    id: reconx.model
    name: Recon Human Metabolic Reconstruction
    original_source:
      - relation_type: prov:hadPrimarySource
        source: reconx
    product_url: https://www.vmh.life/#downloadview
publications:
  - id: https://doi.org/10.1073/pnas.0610772104
    journal: Proceedings of the National Academy of Sciences
    title: Global reconstruction of the human metabolic network based on genomic and bibliomic data
    year: '2007'
synonyms:
  - Recon
  - Recon 1
  - Recon X
taxon:
  - NCBITaxon:9606
---

# ReconX

## Overview

ReconX denotes the Recon series of community genome-scale reconstructions of human
metabolism. The foundational Recon 1 model provided a global reconstruction of the human
metabolic network built from genomic annotation and an extensive literature (bibliomic)
review, and later versions (Recon 2, Recon 3D) substantially expanded coverage. These
reconstructions form a computable, constraint-based representation of human metabolism
used for systems biology and metabolic modeling.

## Content

The Recon reconstructions account for thousands of biochemical reactions, metabolites,
and gene-protein-reaction associations spanning human metabolic pathways. They support
constraint-based modeling approaches such as flux balance analysis.

## Formats and Access

Recon models are distributed in SBML and related systems biology model formats and are
accessible through the Virtual Metabolic Human (VMH) portal and the BiGG Models database.
The reconstruction is also reused by pathway aggregators such as Pathway Commons.

## Development

The Recon reconstructions were developed by the Palsson group at UC San Diego and the
Thiele group, and are maintained through the Virtual Metabolic Human (VMH) resource.

## Citation

Duarte NC, Becker SA, Jamshidi N, et al. Global reconstruction of the human metabolic
network based on genomic and bibliomic data. PNAS (2007) 104(6):1777-1782.
doi:10.1073/pnas.0610772104
