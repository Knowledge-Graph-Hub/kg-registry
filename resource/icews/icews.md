---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://dataverse.harvard.edu/dataverse/icews
  label: Leidos, Inc.
- category: Individual
  contact_details:
  - contact_type: email
    value: GRACE.I.SCARBOROUGH@leidos.com
  label: Grace Scarborough
creation_date: '2026-11-12T00:00:00Z'
description: ICEWS (Integrated Crisis Early Warning System) is a body of machine-coded
  political event data, begun as a DARPA program and later produced by Lockheed Martin
  and Leidos. Each event records a cooperative or hostile interaction between socio-political
  actors (individuals, groups, sectors and nation states) as a triple of source actor,
  event type and target actor, with the event type drawn from the CAMEO event taxonomy.
  Events were extracted automatically from news articles by the BBN ACCENT event coder,
  together with geographic and temporal metadata, and cover 1995 to April 2023. The
  data were released on Harvard Dataverse as coded event files, actor/agent/sector
  dictionaries, monthly event aggregations and an Events of Interest ground truth
  data set; source story text and URLs are not provided because of licensing restrictions.
  ICEWS was discontinued on 11 April 2023 and succeeded by POLECAT (POLitical Event
  Classification, Attributes, and Types), a new, related dataset coded with the PLOVER
  ontology rather than CAMEO.
domains:
- other
homepage_url: https://dataverse.harvard.edu/dataverse/icews
id: icews
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: Integrated Crisis Early Warning System (ICEWS)
products:
- category: GraphicalInterface
  description: The ICEWS collection on Harvard Dataverse, gathering the coded event
    data, dictionaries, event aggregations and ground truth data set releases.
  format: http
  id: icews.dataverse
  name: ICEWS Dataverse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_url: https://dataverse.harvard.edu/dataverse/icews
- category: Product
  compression: zip
  description: ICEWS Coded Event Data (version 37, May 2023), tab-delimited files
    of machine-coded events (source actor, CAMEO event type, target actor, intensity,
    date and location), as yearly files for 1995-2022 and weekly files for January
    to April 2023, with read-me and coding documentation. Most files are zipped; some
    yearly files are plain tab-delimited text.
  format: tsv
  id: icews.coded-event-data
  name: ICEWS Coded Event Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_url: https://doi.org/10.7910/DVN/28075
  secondary_source:
  - relation_type: prov:used
    source: cameo
  warnings:
  - ICEWS was discontinued on 11 April 2023; no further event data will be added.
- category: Product
  description: ICEWS dictionaries of named actors and generic agents, with their aliases
    and time-dependent affiliations to other actors, countries and sectors, plus the
    sector list (tab-delimited and CSV files with read-me documentation).
  format: mixed
  id: icews.dictionaries
  name: ICEWS Dictionaries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_url: https://doi.org/10.7910/DVN/28118
- category: Product
  description: ICEWS event aggregations, time series (typically monthly) built from
    the coded event data by filtering events (for example by country or sector affiliation)
    and aggregating them (for example by count or average intensity), distributed
    as compressed archives and CSV files. No longer supported.
  format: mixed
  id: icews.event-aggregations
  name: ICEWS Event Aggregations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_url: https://doi.org/10.7910/DVN/28117
  secondary_source:
  - relation_type: prov:used
    source: cameo
- category: Product
  description: ICEWS Events of Interest Ground Truth Data Set, recording for each
    country and month (2001 to May 2014) whether macro-level Events of Interest such
    as domestic political crisis, rebellion, insurgency, ethnic/religious violence
    and international crisis occurred. No longer supported.
  format: csv
  id: icews.ground-truth
  name: ICEWS Events of Interest Ground Truth Data Set
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_file_size: 2282782
  product_url: https://dataverse.harvard.edu/api/access/datafile/2686391
- category: DocumentationProduct
  description: ICEWS Expanded CAMEO Annotation Guidelines, the document describing
    how ICEWS applies and extends the CAMEO event categories when coding events.
  format: pdf
  id: icews.cameo-annotation-guidelines
  name: ICEWS Expanded CAMEO Annotation Guidelines
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_file_size: 1606066
  product_url: https://dataverse.harvard.edu/api/access/datafile/2531993
  secondary_source:
  - relation_type: prov:used
    source: cameo
- category: DocumentationProduct
  description: Read-me document for the ICEWS Coded Event Data, describing the file
    layout and fields of the event records.
  format: pdf
  id: icews.readme
  name: ICEWS Coded Event Data Read Me
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icews
  product_file_size: 537367
  product_url: https://dataverse.harvard.edu/api/access/datafile/2548466
publications:
- authors:
  - Sean P. O’Brien
  doi: 10.1111/j.1468-2486.2009.00914.x
  id: doi:10.1111/j.1468-2486.2009.00914.x
  journal: International Studies Review
  preferred: true
  title: 'Crisis Early Warning and Decision Support: Contemporary Approaches and Thoughts
    on Future Research'
  year: '2010'
synonyms:
- ICEWS
- Integrated Crisis Early Warning System
version: '37'
---
# Integrated Crisis Early Warning System (ICEWS)

## Overview

ICEWS is a collection of machine-coded political event data. Each event is a coded
interaction between socio-political actors (individuals, groups, sectors and nation
states), recorded as a source actor, an event type and a target actor. Event types
follow the CAMEO (Conflict and Mediation Event Observations) taxonomy. Events were
extracted automatically from news articles by the BBN ACCENT event coder, which also
attached geographic and temporal metadata. The program began at DARPA, and the data
were later produced by Lockheed Martin and then Leidos.

## Data

The data were released through the ICEWS collection on Harvard Dataverse:

- **Coded Event Data**: yearly event files for 1995-2022 and weekly files for
  January to April 2023, with read-me, CAMEO codebook and annotation guidelines.
- **Dictionaries**: named actors, generic agents and sectors, with aliases and
  time-dependent affiliations.
- **Event Aggregations**: monthly time series derived from the event data (no longer
  supported).
- **Events of Interest Ground Truth Data Set**: country-month records of macro-level
  events such as domestic political crises and insurgencies, 2001 to May 2014 (no
  longer supported).

Source story text and article URLs are not distributed because of licensing restrictions.

## Status

ICEWS was discontinued on 11 April 2023. Its successor is POLECAT (POLitical Event
Classification, Attributes, and Types), a new but related event dataset on Harvard
Dataverse (https://doi.org/10.7910/DVN/AJGVIT), coded with the PLOVER ontology
rather than CAMEO.
