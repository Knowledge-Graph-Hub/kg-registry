---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://enhancer.lbl.gov/vista/
  label: Lawrence Berkeley National Laboratory
creation_date: '2026-06-17T00:00:00Z'
description: The VISTA Enhancer Browser is a database of experimentally validated
  human and mouse noncoding fragments with gene enhancer activity as assessed in
  transgenic mice. Elements are tested in vivo and annotated with their tissue-specific
  enhancer activity patterns.
domains:
- genomics
- anatomy and development
homepage_url: https://enhancer.lbl.gov/vista/
id: vista
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: VISTA Enhancer Browser
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching experimentally validated
    tissue-specific enhancers.
  format: http
  id: vista.site
  is_public: true
  name: VISTA Enhancer Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vista
  product_url: https://enhancer.lbl.gov/vista/
- category: Product
  description: Downloadable datasets of validated enhancer elements and their activity
    annotations.
  format: mixed
  id: vista.data
  name: VISTA Enhancer Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vista
  product_url: https://enhancer.lbl.gov/vista/data
publications:
- authors:
  - A. Visel
  - S. Minovitsky
  - I. Dubchak
  - L. A. Pennacchio
  doi: 10.1093/nar/gkl822
  id: https://doi.org/10.1093/nar/gkl822
  journal: Nucleic Acids Research
  preferred: true
  title: VISTA Enhancer Browser--a database of tissue-specific human enhancers
  year: '2007'
---
# VISTA Enhancer Browser

The VISTA Enhancer Browser, developed at Lawrence Berkeley National Laboratory, is a
central resource for experimentally validated noncoding genomic elements with gene
enhancer activity. Candidate elements from the human and mouse genomes are tested in
transgenic mouse assays, and their tissue-specific activity patterns are documented.

Content includes:

- Human and mouse noncoding elements tested for enhancer activity in vivo
- Tissue-specific enhancer activity annotations from transgenic reporter assays
- Downloadable datasets of validated elements

GeneCards integrates validated enhancer annotations from the VISTA Enhancer Browser.
