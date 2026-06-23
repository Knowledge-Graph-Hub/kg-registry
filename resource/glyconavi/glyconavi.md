---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://glyconavi.org/
    label: GlycoNAVI
creation_date: '2026-06-02T00:00:00Z'
description: GlycoNAVI is an integrated glycoscience portal that provides searchable glycan structures, glycoproteins, glycosylation sites, glycan-related genes, disease annotations, glycan tools, and GlyCosmos-linked data resources.
domains:
  - chemistry and biochemistry
  - biomedical
  - proteomics
homepage_url: https://glyconavi.org/
id: glyconavi
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: GlycoNAVI
products:
  - category: GraphicalInterface
    description: GlycoNAVI integrated portal for glycoscience research, including glycan structures, glycoproteins, glycosylation sites, glycan-related genes, diseases, and glycan analysis tools.
    id: glyconavi.portal
    name: GlycoNAVI Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: glyconavi
    product_url: https://glyconavi.org/
  - category: Product
    description: GlycoNAVI glycan structure table with GlyTouCan identifiers and WURCS strings, available through browser views and JSON, CSV, and TSV downloads.
    format: mixed
    id: glyconavi.glycans
    name: GlycoNAVI Glycans
    original_source:
      - relation_type: prov:hadPrimarySource
        source: glyconavi
    product_url: https://glyconavi.org/Glycans
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: glytoucan
  - category: Product
    description: Sample RDF data files demonstrating GlycoCoO usage with examples from UniCarbKB, GlyConnect, and GlycoNAVI
    format: http
    id: glycocoo.rdf-samples
    name: GlycoCoO RDF Sample Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: glycocoo
    product_url: https://github.com/glycoinfo/GlycoCoO/tree/master/RDF_Sample
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: glycordf
      - relation_type: prov:wasInformedBy
        source: unicarbkb
      - relation_type: prov:wasInformedBy
        source: glyconnect
      - relation_type: prov:wasInformedBy
        source: glyconavi
publications:
  - authors:
      - Tsuchiya S
      - Matsubara M
      - Aoki-Kinoshita KF
      - Yamada I
    doi: 10.3390/molecules26237149
    id: https://www.ncbi.nlm.nih.gov/pubmed/34885724
    journal: Molecules
    preferred: true
    title: 'SugarDrawer: A Web-Based Database Search Tool with Editing Glycan Structures'
    year: '2021'
synonyms:
  - Glyco-Database Information Search
---

# GlycoNAVI

GlycoNAVI is a glycoscience portal for searching glycan structures and related
biological annotations. Its glycan tables and portal views are also referenced
by GlycoCoO sample RDF materials.
