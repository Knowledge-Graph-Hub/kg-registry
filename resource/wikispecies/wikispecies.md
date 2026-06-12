---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://wikimediafoundation.org/
    label: Wikimedia Foundation
creation_date: '2026-06-12T00:00:00Z'
description: Wikispecies is a free, collaboratively edited Wikimedia species directory containing taxonomic information, nomenclature, references, and related links for organisms.
domains:
  - organisms
  - general
homepage_url: https://species.wikimedia.org/wiki/Main_Page
id: wikispecies
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: Wikispecies
products:
  - category: GraphicalInterface
    description: Main Wikispecies web interface for browsing and editing taxonomic pages.
    format: http
    id: wikispecies.portal
    name: Wikispecies Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: wikispecies
    product_url: https://species.wikimedia.org/wiki/Main_Page
  - category: ProgrammingInterface
    description: Public MediaWiki Action API endpoint for Wikispecies content.
    format: http
    id: wikispecies.api
    is_public: true
    name: Wikispecies MediaWiki Action API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: wikispecies
    product_url: https://species.wikimedia.org/w/api.php
  - category: Product
    description: Latest Wikispecies XML dump directory from Wikimedia Downloads.
    format: xml
    id: wikispecies.dumps.latest
    name: Wikispecies Latest XML Dumps
    original_source:
      - relation_type: prov:hadPrimarySource
        source: wikispecies
    product_url: https://dumps.wikimedia.org/specieswiki/latest/
---

Wikispecies is a Wikimedia Foundation project that provides collaboratively curated
species and taxonomy pages through a public wiki, MediaWiki API, and Wikimedia dump
infrastructure.
