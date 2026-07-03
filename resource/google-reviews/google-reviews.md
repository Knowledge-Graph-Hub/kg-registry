---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.google.com/maps
  label: Google LLC
creation_date: '2026-07-03T00:00:00Z'
description: Google Reviews are user-contributed ratings and free-text reviews of
  places and organizations, surfaced through Google Maps and Google Business
  Profiles. Each review includes a review identifier, a star rating, review text,
  and author information associated with a named place or service.
domains:
- general
- public health
homepage_url: https://www.google.com/maps
id: google-reviews
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Google Reviews
products:
- category: GraphicalInterface
  description: User-contributed ratings and reviews of places and organizations,
    accessed through Google Maps.
  format: http
  id: google-reviews.site
  is_public: true
  name: Google Maps Reviews
  original_source:
  - relation_type: prov:hadPrimarySource
    source: google-reviews
  product_url: https://www.google.com/maps
---
# Google Reviews

Google Reviews are user-contributed ratings and written reviews of places and
organizations, surfaced through Google Maps and Google Business Profiles. Each
record carries a review identifier, a star rating, review text, and author
information tied to a named place.

DREAM-KG uses Google Reviews as a source of reputation signals for Philadelphia
social service providers, contributing rating and review triples to the
knowledge graph.
