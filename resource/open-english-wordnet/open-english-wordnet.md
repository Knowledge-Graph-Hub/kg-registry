---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/globalwordnet/english-wordnet
  label: Global WordNet Association
- category: Individual
  contact_details:
  - contact_type: url
    value: https://github.com/jmccrae
  label: John P. McCrae
creation_date: '2026-10-05T00:00:00Z'
description: Open English WordNet (OEWN) is an open-source, community-maintained lexical
  database of English, forked from Princeton WordNet 3.1 and developed under the Global
  WordNet Association. It groups words into synsets linked by relations such as hypernymy,
  antonymy and meronymy, and is released yearly in WN-LMF XML, RDF, JSON and legacy
  WNDB formats.
domains:
- literature
- natural language processing
homepage_url: https://en-word.net/
id: open-english-wordnet
language: en
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Open English WordNet
products:
- category: GraphicalInterface
  description: Open English WordNet website, with a search and browsing interface for words, synsets and their relations, plus links to all releases.
  format: http
  id: open-english-wordnet.homepage
  name: Open English WordNet Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_url: https://en-word.net/
- category: ProgrammingInterface
  description: JSON API for programmatic lookup of lemmas, senses and synsets in Open English WordNet, documented at en-word.net.
  format: http
  id: open-english-wordnet.api
  name: Open English WordNet JSON API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_url: https://en-word.net/api/docs
- category: Product
  description: GitHub repository holding the Open English WordNet source data (one YAML file per lexicographer file), build scripts, issue tracker and versioned releases.
  format: http
  id: open-english-wordnet.repo
  name: Open English WordNet GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_url: https://github.com/globalwordnet/english-wordnet
- category: Product
  compression: gzip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives and adverbs only) in Global WordNet Association WN-LMF XML format.
  format: xml
  id: open-english-wordnet.lmf
  latest_version: '2025'
  name: Open English WordNet 2025 WN-LMF XML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_file_size: 11363503
  product_url: https://en-word.net/static/english-wordnet-2025.xml.gz
- category: GraphProduct
  compression: gzip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives and adverbs only) as RDF in Turtle syntax, using the Lemon/OntoLex model.
  format: ttl
  id: open-english-wordnet.rdf
  latest_version: '2025'
  name: Open English WordNet 2025 RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_file_size: 17760615
  product_url: https://en-word.net/static/english-wordnet-2025.ttl.gz
- category: Product
  compression: zip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives and adverbs only) as a set of JSON files.
  format: json
  id: open-english-wordnet.json
  latest_version: '2025'
  name: Open English WordNet 2025 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_file_size: 9986555
  product_url: https://en-word.net/static/english-wordnet-2025-json.zip
- category: Product
  compression: zip
  description: 2025 edition of Open English WordNet (common nouns, verbs, adjectives and adverbs only) in the legacy Princeton WordNet database (WNDB) text file format, for older applications.
  format: txt
  id: open-english-wordnet.wndb
  latest_version: '2025'
  name: Open English WordNet 2025 WNDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  product_file_size: 9618697
  product_url: https://en-word.net/static/english-wordnet-2025.zip
- category: Product
  compression: gzip
  description: 2025+ edition of Open English WordNet, which adds a manually validated selection of proper nouns from Open English Namenet (derived from Wikidata) in Global WordNet Association WN-LMF XML format.
  format: xml
  id: open-english-wordnet.lmf-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 WN-LMF XML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 12925887
  product_url: https://en-word.net/static/english-wordnet-2025-plus.xml.gz
- category: GraphProduct
  compression: gzip
  description: 2025+ edition of Open English WordNet, which adds a manually validated selection of proper nouns from Open English Namenet (derived from Wikidata) as RDF in Turtle syntax, using the Lemon/OntoLex model.
  format: ttl
  id: open-english-wordnet.rdf-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 20337343
  product_url: https://en-word.net/static/english-wordnet-2025-plus.ttl.gz
- category: Product
  compression: zip
  description: 2025+ edition of Open English WordNet, which adds a manually validated selection of proper nouns from Open English Namenet (derived from Wikidata) as a set of JSON files.
  format: json
  id: open-english-wordnet.json-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 11298794
  product_url: https://en-word.net/static/english-wordnet-2025-plus-json.zip
- category: Product
  compression: zip
  description: 2025+ edition of Open English WordNet, which adds a manually validated selection of proper nouns from Open English Namenet (derived from Wikidata) in the legacy Princeton WordNet database (WNDB) text file format, for older applications.
  format: txt
  id: open-english-wordnet.wndb-plus
  latest_version: '2025'
  name: Open English WordNet Plus 2025 WNDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-english-wordnet
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 10979359
  product_url: https://en-word.net/static/english-wordnet-2025-plus.zip
publications:
- authors:
  - John P. McCrae
  - Alexandre Rademaker
  - Francis Bond
  - Ewa Rudnicka
  - Christiane Fellbaum
  doi: 10.18653/v1/2019.gwc-1.31
  id: doi:10.18653/v1/2019.gwc-1.31
  journal: Proceedings of the 10th Global Wordnet Conference
  preferred: true
  title: English WordNet 2019 – An Open-Source WordNet for English
  year: '2019'
- authors:
  - John P. McCrae
  doi: 10.63317/4mit9o8vc2gw
  id: doi:10.63317/4mit9o8vc2gw
  journal: Proceedings of the Language Resources and Evaluation Conference
  title: 'Open English NameNet: Extending English Wordnet with Names'
  year: '2026'
repository: https://github.com/globalwordnet/english-wordnet
synonyms:
- OEWN
- English WordNet
- EWN
---
# Open English WordNet

Open English WordNet (OEWN) is a lexical network of the English language. Words are grouped into synsets (sets of synonyms sharing a sense), and synsets are linked by relations such as hypernymy, antonymy and meronymy. It is a fork of [Princeton WordNet](https://wordnet.princeton.edu/) 3.1, which is no longer updated, and is maintained on GitHub under the Global WordNet Association with an open-source contribution model. Correspondence to earlier WordNet versions and to wordnets in other languages is provided through the Collaborative Interlingual Index (CILI).

## Releases

New editions have appeared roughly yearly since 2019 (2019, 2020, 2021, 2022, 2023, 2024 and 2025). Files are served from `https://en-word.net/static/` and attached to GitHub releases; there is no version-independent "latest" link, so products here point to the 2025 edition files.

Since the 2025 edition, proper nouns have moved to a separate resource, Open English Namenet, built from Wikidata. Two flavours are released:

- **2025 edition**: common nouns, verbs, adjectives and adverbs (107,519 synsets).
- **2025+ edition**: also includes a manually validated selection of proper nouns from Open English Namenet (120,564 synsets, coverage similar to earlier OEWN releases).

Each flavour is available as WN-LMF XML, RDF (Turtle), JSON and legacy WNDB files.

## License

OEWN is derived from Princeton WordNet under the WordNet License and further developed under CC BY 4.0. Attribution is required to both Princeton WordNet and the Open English WordNet team.

## Publications

The 2019 Global Wordnet Conference paper describes the project's origins. A later paper, "English WordNet 2020: Improving and Extending a WordNet for English using an Open-Source Methodology" (McCrae et al., LREC 2020 Multimodal Wordnets workshop), was not found in Crossref and is not listed above.
