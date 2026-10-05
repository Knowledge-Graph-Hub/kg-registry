---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://wordnet.princeton.edu/
  label: Princeton University
creation_date: '2026-10-04T00:00:00Z'
description: WordNet is Princeton University's lexical database of English. Nouns,
  verbs, adjectives and adverbs are grouped into synsets (sets of cognitive synonyms),
  each expressing a distinct concept, and synsets are linked by conceptual-semantic
  and lexical relations such as hypernymy, meronymy and antonymy. It is widely used
  in natural language processing and as a source for ontologies. Princeton states
  that WordNet is no longer developed; the last release is 3.1, and the community-maintained
  Open English WordNet continues the work.
domains:
- general
- literature
- natural language processing
homepage_url: https://wordnet.princeton.edu/
id: wordnet
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://wordnet.princeton.edu/license-and-commercial-use
  label: WordNet License
name: WordNet
products:
- category: Product
  compression: targz
  description: WordNet 3.1 database files only (the dict directory), without the browser
    or library code.
  format: txt
  id: wordnet.dict-3.1
  latest_version: '3.1'
  name: WordNet 3.1 Database Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wordnet
  product_file_size: 16358468
  product_url: https://wordnetcode.princeton.edu/wn3.1.dict.tar.gz
- category: Product
  compression: targz
  description: WordNet 3.0 release for Unix-like systems, with the database files,
    the wn command-line browser, the C library and the manual pages.
  format: mixed
  id: wordnet.release-3.0
  name: WordNet 3.0 Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wordnet
  product_file_size: 11537239
  product_url: https://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz
- category: GraphicalInterface
  description: WordNet Search 3.1, the online browser for looking up words and their
    synsets and relations.
  format: http
  id: wordnet.search
  name: WordNet Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wordnet
  product_url: http://wordnetweb.princeton.edu/perl/webwn
  warnings:
  - Returned HTTP 403 to automated requests when checked on 2026-10-04, probably bot
    blocking.
- category: DocumentationProduct
  description: WordNet download page listing the current and older versions, standoff
    files and related downloads.
  format: http
  id: wordnet.download-page
  name: WordNet Download Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wordnet
  product_url: https://wordnet.princeton.edu/download/current-version
  warnings:
  - Returned HTTP 403 to automated requests when checked on 2026-10-04, probably bot
    blocking. A Wayback Machine capture is available.
- category: DocumentationProduct
  description: PDF specification of PROTON 3.0 Beta, describing the System, Top, Extent
    and Knowledge Management modules and their classes and properties.
  format: pdf
  id: proton.ontology
  is_public: true
  name: PROTON 3.0 Beta Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  - relation_type: prov:wasInfluencedBy
    source: freebase
  - relation_type: prov:wasInfluencedBy
    source: wordnet
  - relation_type: prov:wasInfluencedBy
    source: dolce
  product_file_size: 725192
  product_url: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf
  warnings:
  - Could not be retrieved when checked on 2026-10-04 because the Ontotext site served
    a CAPTCHA page instead of the file.
- category: Product
  compression: gzip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives
    and adverbs only) in Global WordNet Association WN-LMF XML format.
  format: xml
  id: open-english-wordnet.lmf
  latest_version: '2025'
  name: Open English WordNet 2025 WN-LMF XML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 11363503
  product_url: https://en-word.net/static/english-wordnet-2025.xml.gz
- category: GraphProduct
  compression: gzip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives
    and adverbs only) as RDF in Turtle syntax, using the Lemon/OntoLex model.
  format: ttl
  id: open-english-wordnet.rdf
  latest_version: '2025'
  name: Open English WordNet 2025 RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 17760615
  product_url: https://en-word.net/static/english-wordnet-2025.ttl.gz
- category: Product
  compression: zip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives
    and adverbs only) as a set of JSON files.
  format: json
  id: open-english-wordnet.json
  latest_version: '2025'
  name: Open English WordNet 2025 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 9986555
  product_url: https://en-word.net/static/english-wordnet-2025-json.zip
- category: Product
  compression: zip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives
    and adverbs only) in the legacy Princeton WordNet database (WNDB) text file format,
    for older applications.
  format: txt
  id: open-english-wordnet.wndb
  latest_version: '2025'
  name: Open English WordNet 2025 WNDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 9618697
  product_url: https://en-word.net/static/english-wordnet-2025.zip
- category: Product
  compression: gzip
  description: 2025+ edition of Open English WordNet, which adds a manually validated
    selection of proper nouns from Open English Namenet (derived from Wikidata) in
    Global WordNet Association WN-LMF XML format.
  format: xml
  id: open-english-wordnet.lmf-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 WN-LMF XML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 12925887
  product_url: https://en-word.net/static/english-wordnet-2025-plus.xml.gz
- category: GraphProduct
  compression: gzip
  description: 2025+ edition of Open English WordNet, which adds a manually validated
    selection of proper nouns from Open English Namenet (derived from Wikidata) as
    RDF in Turtle syntax, using the Lemon/OntoLex model.
  format: ttl
  id: open-english-wordnet.rdf-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 20337343
  product_url: https://en-word.net/static/english-wordnet-2025-plus.ttl.gz
- category: Product
  compression: zip
  description: 2025+ edition of Open English WordNet, which adds a manually validated
    selection of proper nouns from Open English Namenet (derived from Wikidata) as
    a set of JSON files.
  format: json
  id: open-english-wordnet.json-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 11298794
  product_url: https://en-word.net/static/english-wordnet-2025-plus-json.zip
- category: Product
  compression: zip
  description: 2025+ edition of Open English WordNet, which adds a manually validated
    selection of proper nouns from Open English Namenet (derived from Wikidata) in
    the legacy Princeton WordNet database (WNDB) text file format, for older applications.
  format: txt
  id: open-english-wordnet.wndb-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 WNDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:wasDerivedFrom
    source: wordnet
  product_file_size: 10979359
  product_url: https://en-word.net/static/english-wordnet-2025-plus.zip
publications:
- authors:
  - George A. Miller
  doi: 10.1145/219717.219748
  id: doi:10.1145/219717.219748
  journal: Communications of the ACM
  preferred: true
  title: WordNet
  year: '1995'
synonyms:
- Princeton WordNet
- PWN
use_instead:
- open-english-wordnet
version: '3.1'
---
# WordNet

WordNet is a large lexical database of English developed at Princeton University, begun by George A. Miller in the 1980s. Nouns, verbs, adjectives and adverbs are grouped into synsets, sets of cognitive synonyms that each express a distinct concept. Synsets are linked by conceptual-semantic and lexical relations, such as hypernymy (is-a), meronymy (part-of) and antonymy, so the database forms a network of words and concepts.

WordNet is used in natural language processing for word sense disambiguation, semantic similarity and information retrieval, and as a source of upper-level and lexical concepts for ontologies and knowledge graphs. For example, the PROTON ontology's Person class definition cites WordNet 2.0.

## Status

The WordNet homepage (as captured on 2026-09-30) says: "Princeton WordNet is no longer developed, though the database and all tools are freely available on the download page." It points users to the community-led Open English WordNet (https://en-word.net/) and the Global Wordnet Association. The last Princeton release is WordNet 3.1, distributed as database files only; WordNet 3.0 is the last full release with the browser and library.

## Access

- WordNet 3.1 database files: https://wordnetcode.princeton.edu/wn3.1.dict.tar.gz
- WordNet 3.0 release: https://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz
- Online search: http://wordnetweb.princeton.edu/perl/webwn

On 2026-10-04 the wordnet.princeton.edu and wordnetweb.princeton.edu pages returned HTTP 403 to automated requests, while the wordnetcode.princeton.edu downloads returned HTTP 200. The W3C-style RDF service at wordnet-rdf.princeton.edu did not respond.

## License

WordNet is distributed under the WordNet License, a permissive BSD-style license: use, copying, modification and distribution are allowed for any purpose without fee, provided the copyright notice and disclaimer appear on all copies, and Princeton's name is not used in advertising.