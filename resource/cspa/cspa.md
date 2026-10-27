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
description: The Cell Surface Protein Atlas (CSPA) is a mass spectrometry-derived
  resource mapping the cell surface glycoproteins (the surfaceome) of 41 human and
  31 mouse cell types and cell lines, generated with Cell Surface Capture technology
  by the Wollscheid Lab at ETH Zurich. The combined dataset covers 1,492 human and
  1,296 mouse cell surface N-glycoproteins. It is offered as a browsable database
  plus downloadable data matrices and targeting tools.
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
  description: The CSPA web portal for browsing the cell surface protein atlas and
    reaching all downloads (current host wollscheidlab.org/CSPA; the ETH wlab.ethz.ch/cspa
    URL redirects here).
  format: http
  id: cspa.portal
  name: CSPA Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cspa
  product_url: https://wollscheidlab.org/CSPA
- category: Product
  description: Excel workbook with the human (1,492 proteins) and mouse (1,296 proteins)
    detection matrices, per-cell-type protein counts, and log2-scaled relative quantities.
  format: xlsx
  id: cspa.detection-matrix
  name: CSPA Protein Detection Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cspa
  product_file_size: 2721208
  product_url: https://wollscheidlab.org/CSPA/data/S1_File.xlsx
- category: Product
  description: Annotated human and mouse surfaceome protein lists and the identified
    N-glycopeptides.
  format: xlsx
  id: cspa.validated-surfaceome
  name: CSPA Validated Surfaceome Proteins
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cspa
  product_file_size: 1430284
  product_url: https://wollscheidlab.org/CSPA/data/S2_File.xlsx
- category: GraphicalInterface
  description: Web interface for searching, browsing, and analyzing protein target
    information with advanced filtering, visualizations, and data export capabilities
    across the druggable genome
  format: http
  id: pharos.portal
  name: Pharos Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://pharos.nih.gov/
- category: Product
  description: Target Central Resource Database (TCRD) downloadable database files
    containing comprehensive protein target information including druggability classifications,
    expression data, disease associations, and chemical probe information
  format: http
  id: pharos.tcrd.download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://opendata.ncats.nih.gov/public/pharos/
  warnings:
  - The Pharos footer still links the historical Juniper TCRD download host, but the
    about page points Pharos data downloads to NCATS OpenData; the registry uses the
    NCATS OpenData URL.
- category: ProgrammingInterface
  connection_url: https://pharos-api.ncats.io/graphql
  description: GraphQL API for programmatic access to Pharos and TCRD data enabling
    custom queries and integrations. The pharos.nih.gov/graphql page is the in-browser
    explorer; queries are served by the pharos-api.ncats.io/graphql endpoint used
    by the Pharos frontend.
  format: graphql
  id: pharos.api
  name: Pharos GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://pharos.nih.gov/graphql
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