---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mediacloud.org/
  label: Media Cloud consortium (Media Ecosystems Analysis Group, UMass Amherst, Northeastern
    University)
creation_date: '2026-10-21T00:00:00Z'
description: Media Cloud is an open-source media research platform for studying the flow of
  online news and information worldwide. It maintains a database of over a billion news stories
  and a directory of more than 25,000 media sources, with open tools to search, aggregate,
  analyze, and visualize media coverage of topics. It is run as a consortium of the Media
  Ecosystems Analysis Group, the University of Massachusetts Amherst, and Northeastern University,
  and was originally incubated at Harvard University and MIT.
domains:
- natural language processing
- human populations
- literature
- organisms
homepage_url: https://www.mediacloud.org/
id: mediacloud
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0 (software; news content under Media Cloud Terms of Use)
name: Media Cloud
products:
- category: GraphicalInterface
  description: Web tool for retrieving online news stories and analyzing and visualizing how
    digital news covers a topic across the Online News Archive; free with an account.
  format: http
  id: mediacloud.search
  name: Media Cloud Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediacloud
  product_url: https://search.mediacloud.org/
- category: GraphicalInterface
  description: Searchable directory of the 25,000+ news media sources, collections, and feeds
    indexed by Media Cloud.
  format: http
  id: mediacloud.directory
  name: Media Cloud Directory
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediacloud
  product_url: https://search.mediacloud.org/directory
- category: Product
  description: Public Python client library (PyPI package `mediacloud`) for the Media Cloud
    API, to run searches and browse the source and collection directory.
  format: python
  id: mediacloud.api-client
  name: Media Cloud Python API Client
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediacloud
  product_url: https://github.com/mediacloud/api-client
  repository: https://github.com/mediacloud/api-client
publications:
- authors:
  - Hal Roberts
  - Rahul Bhargava
  - Linas Valiukas
  - Dennis Jen
  - Momin M. Malik
  - et al.
  doi: 10.1609/icwsm.v15i1.18127
  id: doi:10.1609/icwsm.v15i1.18127
  journal: Proceedings of the International AAAI Conference on Web and Social Media
  preferred: true
  title: 'Media Cloud: Massive Open Source Collection of Global News on the Open Web'
  year: '2021'
repository: https://github.com/mediacloud
---

# Media Cloud

## Overview

Media Cloud is an open-source platform for studying online news and information flow worldwide. It collects and indexes news stories from a large curated directory of media sources and provides tools to search, count, and analyze coverage over time, by language, and by source.

## Access

- Media Cloud Search: retrieve and analyze online news coverage (free account).
- Media Cloud Directory: the index of collections and media sources.
- Python API client (`mediacloud` on PyPI).

The Apache 2.0 license covers the web-search software; news content is accessed under Media Cloud's Terms of Use, not an open data license.

## Citation

Please cite: Roberts H, Bhargava R, Valiukas L, et al. Media Cloud: Massive Open Source Collection of Global News on the Open Web. Proc Int AAAI Conf Web Soc Media. 2021;15(1):1034–1045. doi:10.1609/icwsm.v15i1.18127
