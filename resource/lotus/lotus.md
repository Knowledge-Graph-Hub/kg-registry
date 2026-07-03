---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://lotus.naturalproducts.net/
  label: LOTUS Initiative
creation_date: '2026-07-01T00:00:00Z'
description: LOTUS (naturaL prOducTs occUrrence databaSe) is an open knowledge base
  of referenced structure-organism pairs for natural products research. It harmonizes,
  curates, and validates hundreds of thousands of documented natural product occurrences,
  linking chemical structures to the organisms in which they were reported together
  with the supporting literature references. LOTUS data are disseminated openly and
  are hosted on Wikidata, mirrored at lotus.naturalproducts.net, and released as frozen
  tabular snapshots on Zenodo.
domains:
- chemistry and biochemistry
- biomedical
homepage_url: https://lotus.naturalproducts.net/
id: lotus
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
  label: CC0-1.0
name: LOTUS (naturaL prOducTs occUrrence databaSe)
products:
- category: GraphicalInterface
  description: LOTUS Natural Products Online (LNPN) web interface for structural search,
    taxonomy-oriented queries, and browsing of referenced structure-organism pairs.
  format: http
  id: lotus.portal
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    label: CC0-1.0
  name: LOTUS Natural Products Online Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lotus
  product_url: https://lotus.naturalproducts.net/
- category: Product
  description: Frozen (2021-12-20) tabular snapshot of the LOTUS structure-organism
    pair dataset with associated metadata, archived on Zenodo for reproducible bulk
    download.
  format: csv
  id: lotus.dataset
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    label: CC0-1.0
  name: LOTUS Frozen Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lotus
  product_url: https://doi.org/10.5281/zenodo.5794106
- category: GraphProduct
  description: RDF knowledge graph of the Experimental Natural Products Knowledge
    Graph, integrating experimental LC-MS/MS spectra and GNPS-based annotations, ISDB-LOTUS
    structural annotations, taxonomic and bioactivity metadata, cross-linked to Wikidata
    and served from the public GraphDB/SPARQL endpoint.
  format: ttl
  id: kg-enp.graph
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    label: CC0-1.0
  name: ENPKG RDF Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-enp
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: lotus
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://enpkg.commons-lab.org/graphdb
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: open-tree-of-life
  - relation_type: prov:wasInfluencedBy
    source: chembl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 406 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-07-03: HTTP 406 error
    when accessing file'
publications:
- authors:
  - Adriano Rutz
  - Maria Sorokina
  - Jakub Galgonek
  - Daniel Mietchen
  - Egon Willighagen
  - Arnaud Gaudry
  - James G Graham
  - Ralf Stephan
  - Roderic Page
  - Jiří Vondrášek
  - Christoph Steinbeck
  - Guido F Pauli
  - Jean-Luc Wolfender
  - Jonathan Bisson
  - Pierre-Marie Allard
  doi: 10.7554/eLife.70780
  id: doi:10.7554/eLife.70780
  journal: eLife
  preferred: true
  title: The LOTUS initiative for open knowledge management in natural products research
  year: '2022'
synonyms:
- LOTUS
- LNPN
- LOTUS Natural Products Online
- naturaL prOducTs occUrrence databaSe
---
# LOTUS (naturaL prOducTs occUrrence databaSe)

LOTUS is an open natural products knowledge base cataloguing referenced
structure-organism pairs: each entry links a chemical structure to an organism it
has been reported from, backed by a literature reference. The initiative harmonizes
and curates data from multiple natural product resources and disseminates it under a
CC0 license.

## Access

- **Wikidata**: primary, continuously maintained host of LOTUS data.
- **LNPN portal**: user-friendly interface at lotus.naturalproducts.net for
  structural and taxonomy-oriented search and flat-table/structure exports.
- **Zenodo**: frozen tabular snapshots for reproducible bulk download.

LOTUS is widely reused by downstream natural products tools and knowledge graphs,
including via the in silico spectral database ISDB-LOTUS.