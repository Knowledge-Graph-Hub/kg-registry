---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://wollscheidlab.org/CSPA
  label: Wollscheid Lab, ETH Zurich
creation_date: '2026-10-21T00:00:00Z'
description: The Cell Surface Protein Atlas (CSPA) is a mass spectrometry-derived resource
  mapping the cell surface glycoproteins (the surfaceome) of 41 human and 31 mouse cell types
  and cell lines, generated with Cell Surface Capture technology by the Wollscheid Lab at
  ETH Zurich. The combined dataset covers 1,492 human and 1,296 mouse cell surface N-glycoproteins.
  It is offered as a browsable database plus downloadable data matrices and targeting tools.
domains:
- proteomics
- cell biology
- biological systems
homepage_url: https://wlab.ethz.ch/cspa/
id: cspa
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: Cell Surface Protein Atlas (CSPA)
products:
- category: GraphicalInterface
  description: The CSPA web portal for browsing the cell surface protein atlas and reaching
    all downloads (current host wollscheidlab.org/CSPA; the ETH wlab.ethz.ch/cspa URL redirects
    here).
  format: http
  id: cspa.portal
  name: CSPA Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cspa
  product_url: https://wollscheidlab.org/CSPA
- category: Product
  description: Excel workbook with the human (1,492 proteins) and mouse (1,296 proteins) detection
    matrices, per-cell-type protein counts, and log2-scaled relative quantities.
  format: xlsx
  id: cspa.detection-matrix
  name: CSPA Protein Detection Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cspa
  product_url: https://wollscheidlab.org/CSPA/data/S1_File.xlsx
- category: Product
  description: Annotated human and mouse surfaceome protein lists and the identified N-glycopeptides.
  format: xlsx
  id: cspa.validated-surfaceome
  name: CSPA Validated Surfaceome Proteins
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cspa
  product_url: https://wollscheidlab.org/CSPA/data/S2_File.xlsx
publications:
- authors:
  - Damaris Bausch-Fluck
  - Andreas Hofmann
  - Thomas Bock
  - Andreas P. Frei
  - Ferdinando Cerciello
  - et al.
  doi: 10.1371/journal.pone.0121314
  id: doi:10.1371/journal.pone.0121314
  journal: PLoS ONE
  preferred: true
  title: A Mass Spectrometric-Derived Cell Surface Protein Atlas
  year: '2015'
synonyms:
- CSPA
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---

# Cell Surface Protein Atlas (CSPA)

## Overview

The Cell Surface Protein Atlas (CSPA) is a mass spectrometry-derived catalog of cell surface N-glycoproteins across 41 human and 31 mouse cell types and lines, produced with Cell Surface Capture by the Wollscheid Lab at ETH Zurich.

## Access

- Portal: browse the atlas (current host wollscheidlab.org/CSPA).
- Protein detection matrix (human and mouse), as an Excel workbook.
- Validated surfaceome protein lists and N-glycopeptides.

## Citation

Please cite: Bausch-Fluck D, Hofmann A, Bock T, et al. A Mass Spectrometric-Derived Cell Surface Protein Atlas. PLoS One. 2015;10(4):e0121314. doi:10.1371/journal.pone.0121314
