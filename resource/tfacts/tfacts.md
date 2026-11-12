---
activity_status: inactive
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jean-baptiste.demoulin@uclouvain.be
  label: Jean-Baptiste Demoulin
creation_date: '2026-06-18T00:00:00Z'
description: TFactS is a catalogue of literature-curated, signed transcription factor
  to target gene regulatory interactions, where each interaction records whether a
  transcription factor up-regulates or down-regulates its target. By comparing these
  curated "regulons" against differentially expressed genes, TFactS infers the activation
  or repression state of transcription factors from gene expression (microarray) data.
  The catalogue was compiled from the literature and from PAZAR, NFIregulomeDB, TRED
  and TRRD, and is offered as a sign-less version and a sign-sensitive version (version
  2, 2012). TFactS was developed at the de Duve Institute (Université catholique de
  Louvain) and served as a foundational upstream source for the DoRothEA regulon collection.
  The original web service at tfacts.org is no longer operational and the domain now
  redirects to unrelated content; the site and catalogue file survive as Internet Archive
  Wayback Machine snapshots.
domains:
- genomics
- systems biology
- pathways
- gene regulation
funding:
- Région Wallonne de Belgique, TransMaze project (415925 linked to 516207)
- Wallonie-Bruxelles International, Bourse d'Excellence IN.WBI
homepage_url: http://www.tfacts.org/
id: tfacts
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: TFactS
products:
- category: DocumentationProduct
  description: Peer-reviewed publication describing the TFactS method and the curated
    catalogue of signed transcription factor to target gene interactions. The original
    tfacts.org web server is defunct, so the paper serves as the authoritative reference
    for the resource.
  format: http
  id: tfacts.publication
  name: TFactS publication (Nucleic Acids Research, 2010)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  product_url: https://doi.org/10.1093/nar/gkq149
- category: Product
  description: TFactS catalogues (version 2) as a legacy Excel workbook, recovered
    from an Internet Archive Wayback Machine snapshot of tfacts.org. The workbook has
    a sign-less sheet of about 6,800 transcription factor to target gene pairs, with
    references, species and accessions, and a sign-sensitive sheet of about 3,250 pairs
    annotated as up- or down-regulation with PubMed references. Sources include TRED
    and PubMed literature.
  format: http
  id: tfacts.catalogues
  name: TFactS Catalogues (version 2, Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: pazar
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  - relation_type: prov:hadPrimarySource
    source: trrd
  product_url: https://web.archive.org/web/20220617202237/https://www.tfacts.org/TFactS-new/TFactS-v2/tfacts/data/Catalogues.xls
- category: GraphicalInterface
  description: Archived snapshot of the former TFactS web tool (version 2) in the Internet
    Archive Wayback Machine, preserved because the original site is defunct. The tool
    accepted lists of up- and down-regulated genes (simple or batch mode) and returned
    regulated, activated and repressed transcription factors.
  format: http
  id: tfacts.wayback
  name: TFactS web tool (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  product_url: https://web.archive.org/web/20221022054813/http://www.tfacts.org/TFactS-new/TFactS-v2/
- category: ProcessProduct
  description: TFactSR, a third-party R package on CRAN (by Atsushi Fukushima, GPL-3)
    that reimplements the TFactS enrichment approach and can import the original TFactS
    catalogue file as well as user-defined catalogues.
  format: r
  id: tfacts.tfactsr
  name: TFactSR R package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  product_url: https://cran.r-project.org/package=TFactSR
- category: GraphProduct
  description: Core TF–target regulon knowledge graph (multi-species) with confidence
    levels (A–E)
  format: r
  id: dorothea.graph
  name: DoRothEA Regulon Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  product_url: https://github.com/saezlab/dorothea/releases/tag/v1.0.0
publications:
- authors:
  - Essaghir A
  - Toffalini F
  - Knoops L
  - Kallin A
  - van Helden J
  - Demoulin JB
  doi: 10.1093/nar/gkq149
  id: doi:10.1093/nar/gkq149
  journal: Nucleic Acids Research
  preferred: true
  title: Transcription factor regulation can be accurately predicted from the presence
    of target gene signatures in microarray gene expression data
  year: '2010'
- authors:
  - Essaghir A
  - Demoulin JB
  doi: 10.1371/journal.pone.0039666
  id: doi:10.1371/journal.pone.0039666
  journal: PLoS ONE
  title: A Minimal Connected Network of Transcription Factors Regulated in Human Tumors
    and Its Application to the Quest for Universal Cancer Biomarkers
  year: '2012'
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
---
## Description

**TFactS** is a catalogue of literature-curated transcription factor to target
gene interactions, each annotated with a sign of regulation (up- or
down-regulation). Given a list of differentially expressed genes, TFactS scores
the over-representation of each transcription factor's curated target set to
infer which factors are activated or repressed in a given gene expression
(microarray) experiment.

The catalogue (version 2) combines literature curation with data from PAZAR,
NFIregulomeDB, TRED and TRRD, and comes in a sign-less and a sign-sensitive
form. Human genes are the main target, with mouse and rat genes supported via
orthology. TFactS was developed by Ahmed Essaghir and Jean-Baptiste Demoulin at
the de Duve Institute (Université catholique de Louvain, Brussels).

The resource is an upstream source of **DoRothEA**, the widely used regulon
collection. The original web service at tfacts.org is no longer operational; the
domain currently redirects to unrelated content, so the resource is marked
**inactive**. The tool and its catalogue workbook survive as Wayback Machine
snapshots, and the third-party CRAN package TFactSR reimplements the method.

## Products

- **TFactS publication (Nucleic Acids Research, 2010)** — the peer-reviewed
  paper describing the method and the curated catalogue of signed transcription
  factor to target gene interactions.
- **TFactS Catalogues (Wayback Machine archive)**: the version 2 sign-less and
  sign-sensitive catalogues as an Excel workbook.
- **TFactS web tool (Wayback Machine archive)**: snapshot of the former site.
- **TFactSR R package**: third-party CRAN reimplementation of the method.