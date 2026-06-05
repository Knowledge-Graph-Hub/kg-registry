---
activity_status: orphaned
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: http://www.inoh.org/
    label: Institute for Bioinformatics Research and Development (BIRD), Japan Science and Technology Agency (JST)
creation_date: '2026-06-03T00:00:00Z'
description: INOH (Integrating Network Objects with Hierarchies) is a highly structured, manually curated database of signal transduction and metabolic pathways. Pathways are annotated with custom event and molecule-role ontologies and span multiple organisms including mammals, Xenopus laevis, Drosophila melanogaster, and Caenorhabditis elegans. INOH data was distributed in INOH XML and BioPAX formats and is widely reused by pathway aggregators. The project appears to be no longer actively maintained.
domains:
  - pathways
  - biological systems
  - systems biology
homepage_url: http://www.inoh.org/
id: inoh
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/3.0/
  label: CC BY-NC 3.0
name: INOH
products:
  - category: Product
    description: Manually curated signal transduction and metabolic pathway data, distributed in INOH XML and BioPAX (Level 2 and Level 3) formats.
    format: biopax
    id: inoh.pathways
    name: INOH Pathway Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: inoh
    product_url: http://www.inoh.org/
publications:
  - id: https://doi.org/10.1093/database/bar052
    journal: Database (Oxford)
    title: 'INOH: ontology-based highly structured database of signal transduction pathways'
    year: '2011'
synonyms:
  - Integrating Network Objects with Hierarchies
---

# INOH

## Overview

INOH (Integrating Network Objects with Hierarchies) is a highly structured, manually
curated database of signal transduction pathways, with additional metabolic pathway
content. Each pathway is annotated using custom ontologies that capture event types
and molecular roles, enabling consistent representation of complex signaling logic
across organisms.

## Content

The database covers signal transduction and metabolic pathways for mammals, *Xenopus
laevis*, *Drosophila melanogaster*, *Caenorhabditis elegans*, and canonical pathways.
A representative release included 73 signal transduction diagrams and 29 metabolic
pathway diagrams encompassing hundreds of subpathways, thousands of interactions, and
thousands of protein entities.

## Formats and Access

INOH data was provided in INOH XML and BioPAX formats, with BioPAX Level 3 recommended
for signaling data because of its ability to represent molecular states and binding
topology. INOH is a recognized upstream source for pathway aggregators such as Pathway
Commons.

## Status

The INOH website (www.inoh.org) is not currently reachable, and the project appears to
be no longer actively maintained. Its data remains accessible through downstream
aggregators.

## Development

INOH was developed by the Institute for Bioinformatics Research and Development (BIRD)
under the Japan Science and Technology Agency (JST).

## Citation

Yamamoto S, Sakai N, Nakamura H, Fukagawa H, Fukuda K, Takagi T. INOH: ontology-based
highly structured database of signal transduction pathways. Database (Oxford) (2011)
2011:bar052. doi:10.1093/database/bar052
