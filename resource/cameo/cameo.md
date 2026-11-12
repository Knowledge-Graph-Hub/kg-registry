---
activity_status: inactive
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: url
    value: https://parusanalytics.com/eventdata/data.dir/cameo.html
  label: Philip A. Schrodt
creation_date: '2026-10-21T00:00:00Z'
description: CAMEO (Conflict and Mediation Event Observations) is an event and actor
  coding scheme for political event data, developed from 2000 by Deborah Gerner, Philip
  Schrodt and Omur Yilmaz in the Kansas and later Penn State Event Data Projects as
  a successor to the WEIS framework. Its verb codebook arranges events in a hierarchy
  of 20 top-level categories (from making a public statement through cooperation,
  demands, protest and coercion to assault, fight and unconventional mass violence),
  with sub-categories tuned for the study of mediation and finer distinctions in the
  use of force. Its actor codebook gives hierarchical codes for states, sub-state
  roles, international organizations, and religious (CAMEORCS) and ethnic groups.
  CAMEO is the event taxonomy used by machine-coded event datasets such as GDELT and
  ICEWS.
domains:
- other
funding:
- National Science Foundation (NSF) (SES-0096086)
- National Science Foundation (NSF) (SES-0455158)
- National Science Foundation (NSF) (SES-0527564)
- National Science Foundation (NSF) (SES-1004414)
homepage_url: https://parusanalytics.com/eventdata/data.dir/cameo.html
id: cameo
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/3.0/
  label: CC BY-NC-SA 3.0
name: Conflict and Mediation Event Observations (CAMEO)
products:
- category: DataModelProduct
  description: CAMEO Event and Actor Codebook, version 1.1b3 (March 2012), the most
    recent version, covering the verb (event) codebook, actor codebook, the CAMEORCS
    religious coding scheme for about 1,500 religions, and the ethnic group taxonomy
    of about 650 codes.
  format: pdf
  id: cameo.codebook
  name: CAMEO Event and Actor Codebook (version 1.1b3)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cameo
  product_file_size: 791237
  product_url: https://parusanalytics.com/eventdata/cameo.dir/CAMEO.Manual.1.1b3.pdf
- category: DataModelProduct
  description: CAMEO codebook version 0.9b6 (July 2009), the version used in the CAMEO-based
    ICEWS research.
  format: pdf
  id: cameo.codebook-0.9b6
  name: CAMEO Codebook (version 0.9b6)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cameo
  product_file_size: 465600
  product_url: https://parusanalytics.com/eventdata/cameo.dir/CAMEO.09b6.pdf
- category: DataModelProduct
  compression: zip
  description: Documentation and an Excel file detailing the CAMEO ethnic group coding
    framework.
  format: mixed
  id: cameo.ethnic-groups
  name: CAMEO Ethnic Group Coding Framework
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cameo
  product_file_size: 240412
  product_url: https://parusanalytics.com/eventdata/cameo.dir/CAMEO.Ethnic.Groups.zip
- category: DataModelProduct
  description: Tab-delimited lookup table of CAMEO event codes and their descriptions
    (root, base and sub-category codes), as distributed by the GDELT Project for decoding
    its Event Database.
  format: tsv
  id: cameo.event-codes
  name: CAMEO Event Codes Lookup (GDELT)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cameo
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_file_size: 12157
  product_url: https://www.gdeltproject.org/data/lookups/CAMEO.eventcodes.txt
- category: DataModelProduct
  description: Tab-delimited lookup table assigning a Goldstein scale conflict-cooperation
    score to each CAMEO event code, as distributed by the GDELT Project.
  format: tsv
  id: cameo.goldstein-scale
  name: CAMEO Goldstein Scale Lookup (GDELT)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cameo
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_file_size: 3165
  product_url: https://www.gdeltproject.org/data/lookups/CAMEO.goldsteinscale.txt
- category: Product
  description: Master file list indexing every 15-minute GDELT 2.0 Event, Mentions,
    and Global Knowledge Graph update file (size, MD5, URL); the payload files are
    tab-delimited despite a .CSV extension.
  format: tsv
  id: gdelt.raw-data
  name: GDELT 2.0 Raw Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_file_size: 128756658
  product_url: https://data.gdeltproject.org/gdeltv2/masterfilelist.txt
  secondary_source:
  - relation_type: prov:used
    source: cameo
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
publications:
- authors:
  - Gerner DJ
  - Schrodt PA
  - Yilmaz O
  doi: 10.4324/9780203885130-25
  id: doi:10.4324/9780203885130-25
  journal: International Conflict Mediation
  preferred: true
  title: 'Conflict and Mediation Event Observations (CAMEO): an event data framework
    for a post-Cold War world'
  year: '2008'
synonyms:
- CAMEO
- Conflict and Mediation Event Observations
- CAMEO Event and Actor Codebook
version: 1.1b3
warnings:
- The most recent codebook version (1.1b3) dates from March 2012 and its project page
  notes it has not been fully implemented in the coding dictionaries; no newer release
  has been published on the project page.
---
# Conflict and Mediation Event Observations (CAMEO)

CAMEO is a coding scheme for political event data: a verb codebook that classifies who-did-what-to-whom events into a hierarchy of 20 top-level categories, and an actor codebook that gives hierarchical codes for states, sub-state roles, international organizations, and religious and ethnic groups. It was developed from 2000 by Deborah Gerner, Philip Schrodt and Omur Yilmaz at the Kansas Event Data Project (later the Penn State Event Data Project), with funding from the U.S. National Science Foundation, as a successor to WEIS that is optimized for the study of mediation and for machine coding of news reports.

The codebook (version 1.1b3, March 2012) is distributed as a PDF under a CC BY-NC-SA 3.0 license from the project page at https://parusanalytics.com/eventdata/data.dir/cameo.html. Version 0.9b6 (July 2009) is the version used in ICEWS research. CAMEO is also the event taxonomy of the GDELT Event Database, whose lookup tables for CAMEO event codes and Goldstein scale scores are listed here as products.
