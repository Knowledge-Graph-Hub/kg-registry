---
activity_status: orphaned
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: http://www.netpath.org/
    label: Institute of Bioinformatics, Bangalore and Johns Hopkins University (Pandey lab)
creation_date: '2026-06-03T00:00:00Z'
description: NetPath is a public, manually curated resource of human signal transduction pathways. It provides detailed maps of immune and cancer signaling pathways, annotating thousands of reactions and transcriptionally regulated genes drawn from thousands of published articles. NetPath data is distributed in community standard formats including BioPAX, PSI-MI, and SBML, and is widely reused by pathway aggregators. The project is no longer actively maintained.
domains:
  - pathways
  - biological systems
  - immunology
  - systems biology
homepage_url: http://www.netpath.org/
id: netpath
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: http://www.netpath.org/
  label: Free for academic use
name: NetPath
products:
  - category: Product
    description: Manually curated human signal transduction pathway data, available in BioPAX, PSI-MI, and SBML community standard formats.
    format: biopax
    id: netpath.pathways
    name: NetPath Pathway Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: netpath
    product_url: http://www.netpath.org/
publications:
  - id: https://doi.org/10.1186/gb-2010-11-1-r3
    journal: Genome Biology
    title: 'NetPath: a public resource of curated signal transduction pathways'
    year: '2010'
synonyms:
  - NetPath
taxon:
  - NCBITaxon:9606
---

# NetPath

## Overview

NetPath is a public, manually curated resource of human signal transduction pathways.
It provides detailed pathway maps with extensive annotation of molecular reactions and
transcriptionally regulated genes, with a particular emphasis on immune and cancer
signaling pathways.

## Content

NetPath captures curated pathways comprising roughly 1,600 annotated reactions and more
than 2,800 instances of transcriptionally regulated genes, linked to over 5,500
published articles. Pathways include major immune signaling cascades and several
cancer-related signaling pathways.

## Formats and Access

NetPath pathway data is distributed in community standard formats including BioPAX,
PSI-MI, and SBML, making it readily reusable in pathway analysis tools and downstream
aggregators such as Pathway Commons.

## Status

The NetPath website is no longer reliably accessible and the project is not actively
maintained. Its curated pathway data remains available through downstream aggregators.

## Development

NetPath was developed jointly by the Institute of Bioinformatics, Bangalore, and the
Pandey laboratory at Johns Hopkins University.

## Citation

Kandasamy K, Mohan SS, Raju R, et al. NetPath: a public resource of curated signal
transduction pathways. Genome Biology (2010) 11:R3. doi:10.1186/gb-2010-11-1-r3
