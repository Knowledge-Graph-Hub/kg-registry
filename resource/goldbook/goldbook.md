---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://iupac.org/
  label: International Union of Pure and Applied Chemistry (IUPAC)
- category: Individual
  contact_details:
  - contact_type: email
    value: schalk@unf.edu
  - contact_type: github
    value: stuchalk
  label: Stuart Chalk
  orcid: 0000-0002-0703-7776
creation_date: '2026-10-04T00:00:00Z'
description: The IUPAC Compendium of Chemical Terminology, known as the Gold Book,
  collects authoritative definitions of chemical terms from IUPAC recommendations
  published in Pure and Applied Chemistry and the other IUPAC Colour Books, ratified
  by IUPAC's Interdivisional Committee on Terminology, Nomenclature and Symbols. Version
  5.0.0 (5th edition, 2025) holds 14,588 terms, each with a stable code and DOI, and
  the site offers an API for downloading single terms or the whole vocabulary as JSON
  or XML.
domains:
- chemistry and biochemistry
homepage_url: https://goldbook.iupac.org/
id: goldbook
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: IUPAC Gold Book
products:
- category: GraphicalInterface
  description: Gold Book website for browsing and searching term definitions, with
    alphabetical, division, organization and source indexes.
  format: http
  id: goldbook.portal
  name: IUPAC Gold Book Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_url: https://goldbook.iupac.org/
  warnings:
  - The site returned HTTP 403 to automated requests when checked on 2026-10-04, probably
    bot blocking.
- category: Product
  description: All Gold Book terms with definitions as a single JSON download, from
    the Gold Book API endpoint /terms/index/all/json/download.
  format: json
  id: goldbook.terms.json
  name: Gold Book Terms JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_url: https://goldbook.iupac.org/terms/index/all/json/download
  warnings:
  - The site returned HTTP 403 to automated requests when checked on 2026-10-04, probably
    bot blocking.
- category: Product
  description: All Gold Book terms with definitions as a single XML download, from
    the Gold Book API endpoint /terms/index/all/xml/download.
  format: xml
  id: goldbook.terms.xml
  name: Gold Book Terms XML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_url: https://goldbook.iupac.org/terms/index/all/xml/download
  warnings:
  - The site returned HTTP 403 to automated requests when checked on 2026-10-04, probably
    bot blocking.
- category: Product
  description: Index of the IUPAC recommendations and other source documents that
    Gold Book definitions cite, as a JSON download.
  format: json
  id: goldbook.sources.json
  name: Gold Book Sources JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_url: https://goldbook.iupac.org/sources/index/all/json/download
  warnings:
  - The site returned HTTP 403 to automated requests when checked on 2026-10-04, probably
    bot blocking.
- category: ProgrammingInterface
  description: Gold Book API (v1.1) for retrieving single terms or sources by code
    in HTML, XML or JSON, with an optional download flag.
  format: http
  id: goldbook.api
  name: Gold Book API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_url: https://goldbook.iupac.org/pages/api
  warnings:
  - The site returned HTTP 403 to automated requests when checked on 2026-10-04, probably
    bot blocking.
- category: Product
  description: IUPAC Gold Book (Compendium of Chemical Terminology) OBO
  format: obo
  id: obo-db-ingest.goldbook.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: goldbook OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_file_size: 1560100
  product_url: https://w3id.org/biopragmatics/resources/goldbook/goldbook.obo
- category: Product
  description: IUPAC Gold Book (Compendium of Chemical Terminology) OWL
  format: owl
  id: obo-db-ingest.goldbook.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: goldbook OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_file_size: 1783953
  product_url: https://w3id.org/biopragmatics/resources/goldbook/goldbook.owl
- category: Product
  description: IUPAC Gold Book (Compendium of Chemical Terminology) OBO Graph JSON
  format: json
  id: obo-db-ingest.goldbook.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: goldbook OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_file_size: 1802012
  product_url: https://w3id.org/biopragmatics/resources/goldbook/goldbook.json
- category: MappingProduct
  description: IUPAC Gold Book (Compendium of Chemical Terminology) SSSOM
  format: sssom
  id: obo-db-ingest.goldbook.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: goldbook SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_file_size: 231373
  product_url: https://w3id.org/biopragmatics/resources/goldbook/goldbook.sssom.tsv
- category: Product
  description: IUPAC Gold Book (Compendium of Chemical Terminology) Nodes TSV
  format: tsv
  id: obo-db-ingest.goldbook.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: goldbook Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: goldbook
  product_file_size: 977459
  product_url: https://w3id.org/biopragmatics/resources/goldbook/goldbook.tsv
publications:
- authors:
  - Victor Gold
  - Alan McNaught
  doi: 10.1351/goldbook
  id: doi:10.1351/goldbook
  preferred: true
  title: The IUPAC Compendium of Chemical Terminology
  year: '2025'
synonyms:
- Gold Book
- IUPAC Compendium of Chemical Terminology
- Compendium of Chemical Terminology
version: 5.0.0
---
# IUPAC Gold Book

The IUPAC Compendium of Chemical Terminology is called the Gold Book after Victor Gold, who started work on the first edition. It is one of IUPAC's Colour Books on chemical nomenclature, terminology, symbols and units. Its definitions come from IUPAC recommendations published in *Pure and Applied Chemistry* and the other Colour Books, supplemented by some definitions from ISO and the International Vocabulary of Metrology.

The online version 5.0.0 (5th edition, 2025) has 14,588 terms. Each term has a code (such as `A00001`) and a DOI under `10.1351/goldbook.`. Jan Kaiser is the content editor and Stuart Chalk the technical editor, for the Joint Subcommittee on the IUPAC Gold Book.

## Access

The Gold Book API (v1.1) is documented at <https://goldbook.iupac.org/pages/api>:

- `/terms/index/all/[xml|json]/download`: every term.
- `/terms/view/<code>/[xml|json]`: one term.
- `/sources/index/all/[xml|json]/download`: the cited source documents.

When checked on 2026-10-04 the site returned HTTP 403 to automated clients, so the URLs above were taken from an August 2026 Wayback Machine capture of the API page.

The biopragmatics `obo-db-ingest` project converts the Gold Book to OBO, OWL, OBO Graph JSON, SSSOM and other formats (see the `obo-db-ingest.goldbook.*` products).

## License

The Gold Book site and the `obo-db-ingest` export state CC BY-SA 4.0 for individual terms, and IUPAC asks parties wishing to reuse the entire Gold Book commercially to contact the Executive Director. The Crossref record for DOI 10.1351/goldbook lists CC BY-NC-ND 4.0 (from 2019), which was the license of earlier versions.