---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://proteininformationresource.org/
  label: Protein Information Resource
creation_date: '2026-05-20T00:00:00Z'
description: Protein Information Resource (PIR) is an integrated public bioinformatics
  resource that supports genomic, proteomic, and systems biology research through
  protein databases, annotation resources, search tools, and downloadable reference
  datasets.
domains:
- proteomics
- genomics
- systems biology
homepage_url: https://proteininformationresource.org/
id: pir
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://proteininformationresource.org/pirwww/about/linkpir.shtml
  label: PIR Terms of Use
name: Protein Information Resource
products:
- category: GraphicalInterface
  description: Main PIR web interface for navigating databases, search tools, and
    supporting resources.
  format: http
  id: pir.portal
  name: PIR Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  product_url: https://proteininformationresource.org/
- category: Product
  description: PIR download center exposing FTP-accessible releases for iProClass,
    PIRSF, PRO, and related PIR-maintained datasets.
  format: http
  id: pir.downloads
  name: PIR Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  product_url: https://proteininformationresource.org/pirwww/download/
- category: GraphProduct
  description: PIR compound exact match edges
  format: csv
  id: prokn.pir.compound.skos_exact_match.compound.edges
  name: ProKN PIR Compound Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 100170454
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Compound.SKOS_EXACT_MATCH.Compound.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impchumangene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4832630
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impc_gene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4832630
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: PIR IMPC human gene orthologous to protein edges
  format: csv
  id: prokn.pir.impchumangene.orthologous_to.protein.edges
  name: ProKN PIR Human Gene to Protein Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18025933
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.Protein.edges.csv
- category: GraphProduct
  description: PIR IMPC mouse gene has gene product protein edges
  format: csv
  id: prokn.pir.impcmousegene.has_gene_product.protein.edges
  name: ProKN PIR Mouse Gene Product Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 19465205
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcMouseGene.BIOLINK_HAS_GENE_PRODUCT.Protein.edges.csv
publications:
- authors:
  - Wu CH
  - Yeh LS
  - Huang H
  - Arminski L
  - Castro-Alvear J
  - Chen Y
  - Hu Z
  - Kourtesis P
  - Ledley RS
  - Suzek BE
  - Vinayaka CR
  - Zhang J
  - Barker WC
  doi: 10.1093/nar/gkg040
  id: https://www.ncbi.nlm.nih.gov/pubmed/12520019
  journal: Nucleic Acids Res
  preferred: true
  title: The Protein Information Resource
  year: '2003'
synonyms:
- PIR
- Protein Information Resource
---

# Protein Information Resource

PIR is a long-running public protein bioinformatics resource that historically contributed
core sequence and annotation infrastructure to UniProt and continues to maintain protein-centric
data integration and analysis resources. Its public site exposes databases, search tools,
downloads, and supporting documentation for protein annotation workflows.

The ProKN products on this page are derived graph views built from PIR-linked protein mappings
and cross-resource integration, including alignments to IMPC-derived gene and orthology data.