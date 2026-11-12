---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.genomicsengland.co.uk/panelapp
  - contact_type: github
    value: genomicsengland
  label: Genomics England
creation_date: '2026-11-12T00:00:00Z'
description: Genomics England PanelApp is a public knowledgebase and crowdsourcing
  tool for creating, reviewing and sharing virtual gene panels for human disorders.
  Each panel covers a clinical indication and lists genes, short tandem repeats and
  copy-number regions, each rated with a traffic-light confidence level (green for
  diagnostic grade, amber for borderline, red for insufficient evidence) agreed through
  expert review. The panels underpin genome interpretation in the NHS Genomic Medicine
  Service in England, where signed-off panels are approved for diagnostic testing.
  When checked on 2026-11-12, the PanelApp API listed 433 public panels, 296 of them
  signed off for the Genomic Medicine Service. Data are free to browse and download
  for non-commercial, non-diagnostic use under the PanelApp Terms of Use.
domains:
- biomedical
- genomics
- clinical
- rare disease
homepage_url: https://panelapp.genomicsengland.co.uk/
id: panelapp
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://panelapp.genomicsengland.co.uk/media/files/GEL_-_PanelApp_Terms_of_Use_December_2019.pdf
  label: PanelApp Terms of Use (non-commercial, non-diagnostic use; all rights reserved)
name: Genomics England PanelApp
products:
- category: GraphicalInterface
  description: PanelApp web site for browsing, searching and downloading gene panels,
    viewing gene, STR and region ratings and evidence, and submitting expert reviews.
  format: http
  id: panelapp.portal
  name: PanelApp Web Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  product_url: https://panelapp.genomicsengland.co.uk/
- category: ProgrammingInterface
  description: Public REST API (JSON, paginated) for panels, genes, STRs, regions,
    panel versions and the panels signed off for the NHS Genomic Medicine Service
    (/api/v1/panels/signedoff/).
  format: http
  id: panelapp.api
  is_public: true
  name: PanelApp REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  product_url: https://panelapp.genomicsengland.co.uk/api/docs/
- category: DocumentationProduct
  description: PanelApp Handbook (version 105) describing panel structure, the gene
    rating criteria, the review and sign-off process, and how to use the site.
  format: http
  id: panelapp.handbook
  name: PanelApp Handbook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panelapp
  product_url: https://panelapp.genomicsengland.co.uk/media/files/GUI-BIO-004_PanelApp_Handbook-v105.pdf
- category: ProcessProduct
  description: Source code of the PanelApp application (Python/Django). The GitHub
    mirror was last updated in 2019.
  format: python
  id: panelapp.software
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: PanelApp Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panelapp
  product_url: https://github.com/genomicsengland/panelapp
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mavedb
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: revel
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://sugi.bio/biobtree/api/
publications:
- authors:
  - Antonio Rueda Martin
  - Eleanor Williams
  - Rebecca E. Foulger
  - Sarah Leigh
  - Louise C. Daugherty
  - Olivia Niblock
  - Ivone U. S. Leong
  - Katherine R. Smith
  - Oleg Gerasimenko
  - Eik Haraldsdottir
  - Ellen Thomas
  - Richard H. Scott
  - Emma Baple
  - Arianna Tucci
  - Helen Brittain
  - Anna de Burca
  - Kristina Ibañez
  - Dalia Kasperaviciute
  - Damian Smedley
  - Mark Caulfield
  - Augusto Rendon
  - Ellen M. McDonagh
  doi: doi:10.1038/s41588-019-0528-2
  id: doi:10.1038/s41588-019-0528-2
  journal: Nature Genetics
  preferred: true
  title: PanelApp crowdsources expert knowledge to establish consensus diagnostic
    gene panels
  year: '2019'
- authors:
  - Zornitza Stark
  doi: doi:10.1016/j.ajhg.2021.06.020
  id: doi:10.1016/j.ajhg.2021.06.020
  journal: The American Journal of Human Genetics
  title: Scaling national and international improvement in virtual gene panel curation
    via a collaborative approach to discordance resolution
  year: '2021'
repository: https://github.com/genomicsengland/panelapp
---
# Genomics England PanelApp

Genomics England PanelApp is a public knowledgebase of virtual gene panels for
human disorders. Experts review and rate each gene, short tandem repeat and
copy-number region on a panel with a traffic-light system: green genes have
diagnostic-grade evidence, amber genes are borderline, and red genes lack enough
evidence. Signed-off panels are used for genome interpretation in the NHS Genomic
Medicine Service in England.

Panels can be browsed and downloaded on the web site or retrieved through a public
REST API. Use of PanelApp is governed by the Genomics England PanelApp Terms of
Use, which exclude commercial and diagnostic use without a separate agreement and
add conditions for OMIM- and Orphanet-derived content. A sister instance, PanelApp
Australia (https://panelapp-aus.org/), runs on the same software and is curated
by Australian Genomics.
