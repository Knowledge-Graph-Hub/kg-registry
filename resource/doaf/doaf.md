---
activity_status: inactive
category: DataSource
contacts:
  - category: Individual
    label: Warren A. Kibbe
    orcid: 0000-0001-5622-7659
    contact_details:
      - contact_type: url
        value: https://orcid.org/0000-0001-5622-7659
creation_date: '2025-10-30T00:00:00Z'
description: The Disease Ontology Annotation Framework (DOAF) was an automated pipeline and web resource from Northwestern University that annotated human genes with Disease Ontology terms by text mining NCBI GeneRIF entries with the NCBO Annotator, producing gene-disease associations backed by PubMed evidence.
domains:
  - biomedical
  - clinical
  - genomics
id: doaf
infores_id: doaf
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
name: Disease Ontology Annotation Framework
homepage_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049686
synonyms:
  - DOAF
  - Disease Ontology Annotation Framework
publications:
  - id: doi:10.1371/journal.pone.0049686
    doi: 10.1371/journal.pone.0049686
    title: A Framework for Annotating Human Genome in Disease Context
    authors:
      - Wei Xu
      - Huisong Wang
      - Wenqing Cheng
      - Dong Fu
      - Tian Xia
      - Warren A. Kibbe
      - Simon M. Lin
    journal: PLoS ONE
    preferred: true
    year: '2012'
products:
  - category: DocumentationProduct
    description: PLOS ONE article describing the Disease Ontology Annotation Framework and its use for disease annotation.
    format: http
    id: doaf.framework-publication
    name: DOAF Framework Publication
    original_source:
      - source: doaf
        relation_type: prov:hadPrimarySource
    product_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049686
  - category: GraphicalInterface
    description: Archived snapshot of the DOAF web interface (doa.nubic.northwestern.edu), which supported gene-to-disease and disease-to-gene queries, batch queries, and download of the DO-gene mappings. The live site is offline.
    format: http
    id: doaf.web
    name: DOAF web interface (archived)
    original_source:
      - source: doaf
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:used
      - source: bioportal
        relation_type: prov:used
    product_url: https://web.archive.org/web/20160601045226/http://doa.nubic.northwestern.edu/pages/about.php
    warnings:
      - The original site at http://doa.nubic.northwestern.edu did not resolve when checked on 2026-11-10; the last Internet Archive captures date from 2016.
taxon:
  - NCBITaxon:9606
warnings:
  - The DOAF web site (http://doa.nubic.northwestern.edu) and its REST API are offline as of 2026-11-10; the last Internet Archive captures date from 2016. No downloadable DOAF data files are known to survive.
---

# Disease Ontology Annotation Framework

## Overview

The Disease Ontology Annotation Framework (DOAF) was an automated method and
web resource for annotating the human genome in a disease context. It was
developed by the Northwestern University Biomedical Informatics Center (NUBIC)
and the Huazhong University of Science and Technology. DOAF linked human genes
to Disease Ontology (DO) terms by submitting NCBI Gene Reference Into Function
(GeneRIF) text to the NCBO Annotator text-mining service, so that each
gene-disease association was supported by the PubMed article behind the GeneRIF.

## Method

DOAF had four core components: the Disease Ontology, GeneRIF, the NCBO
Annotator, and a search interface. The annotation pipeline:

- submitted GeneRIF text to the NCBO Annotator and mapped matched DO terms to
  the GeneRIF's gene;
- applied a rule-based, Java-implemented quality control step that removed
  uninformative mappings (e.g. the overly broad term "Disease") and incorrect
  ones (e.g. "Ca" for calcium mapped to cancer), with a repository of known
  mis-mappings;
- supported both full rebuilds and incremental updates as DO and GeneRIF
  changed, and was described as updated monthly.

At publication (2012), DOAF contained 8,686 DO terms and 152,357 disease-gene
association entries.

## Access (historical)

The web interface at http://doa.nubic.northwestern.edu allowed gene-to-disease
and disease-to-gene queries (with gene alias and synonym support), batch
queries, and download of the mapping results as an OBO file or as mapped
identifier tables (DOID, Gene ID, PubMed ID). The paper also describes a
programmatic API and HTTP REST service, which was used by the Genomic Regions
Enrichment of Annotations Tool (GREAT).

## Status

The site is no longer online; Internet Archive captures exist from 2013 to 2016.
No DOAF data files are known to be available today. For current
disease-gene annotations based on the Disease Ontology, see the
[Disease Ontology](https://disease-ontology.org/) itself.

## Information Resource ID

This resource has the Information Resource identifier: `infores:doaf`

## Reference

Xu W, Wang H, Cheng W, Fu D, Xia T, Kibbe WA, Lin SM (2012). A Framework for
Annotating Human Genome in Disease Context. PLoS ONE 7(12): e49686.
https://doi.org/10.1371/journal.pone.0049686
