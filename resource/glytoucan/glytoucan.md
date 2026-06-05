---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://glytoucan.org/
  label: GlyTouCan / GlySpace Project (Soka University, Japan)
creation_date: '2026-06-03T00:00:00Z'
description: GlyTouCan is the international glycan structure repository, assigning
  globally unique and persistent accession numbers to registered glycan structures.
  It accepts structures ranging in resolution from monosaccharide composition to fully
  defined structures, providing a freely available, uncurated registry that serves
  as a common reference for glycan identifiers across glycoscience resources.
domains:
- chemistry and biochemistry
- proteomics
- biological systems
homepage_url: https://glytoucan.org/
id: glytoucan
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: GlyTouCan
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing, and registering glycan structures
    and looking up GlyTouCan accession numbers.
  format: http
  id: glytoucan.portal
  name: GlyTouCan Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glytoucan
  product_url: https://glytoucan.org/
- category: ProgrammingInterface
  description: Public REST API (documented via Swagger UI) for programmatic access
    to GlyTouCan glycan structures and accession numbers.
  format: http
  id: glytoucan.api
  is_public: true
  name: GlyTouCan API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glytoucan
  product_url: https://api.glytoucan.org/
- category: ProgrammingInterface
  description: SPARQL endpoint providing RDF access to the GlyTouCan glycan structure
    repository and its semantic annotations.
  format: http
  id: glytoucan.sparql
  is_public: true
  name: GlyTouCan SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glytoucan
  product_url: https://ts.glytoucan.org/sparql
- category: Product
  description: GlycoNAVI glycan structure table with GlyTouCan identifiers and WURCS
    strings, available through browser views and JSON, CSV, and TSV downloads.
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
publications:
- id: https://doi.org/10.1093/nar/gkv1041
  journal: Nucleic Acids Research
  title: GlyTouCan 1.0 - The international glycan structure repository
  year: '2016'
synonyms:
- GlyTouCan
---
# GlyTouCan

## Overview

GlyTouCan is the international glycan structure repository. It assigns globally unique,
persistent accession numbers to glycan structures registered by the community, accepting
structures at any level of resolution from monosaccharide composition to fully defined
topology, linkage, and anomeric configuration. By providing a stable identifier space
for glycans, GlyTouCan acts as a common reference hub across glycoscience databases and
tools.

## Key Features

- **Persistent accessions**: Globally unique GlyTouCan IDs for registered glycan structures.
- **Variable resolution**: Accepts structures from composition-level to fully defined.
- **Open registry**: Freely available, uncurated repository accessible to all users.
- **Semantic access**: RDF data available through a public SPARQL endpoint.

## Access

- Web portal at [glytoucan.org](https://glytoucan.org/)
- Public REST API documented via Swagger UI
- SPARQL endpoint for RDF queries
- Documentation at [doc.glytoucan.org](https://doc.glytoucan.org/)

## Development and Funding

GlyTouCan is developed and maintained as part of the GlySpace Project, with leadership
from Soka University, Japan, and funding from MEXT and the Japan Science and Technology
Agency (JST).

## Citation

Tiemeyer M, Aoki K, Paulson J, et al. GlyTouCan 1.0 - The international glycan structure
repository. Nucleic Acids Research (2016) 44(D1):D1237-D1242. doi:10.1093/nar/gkv1041