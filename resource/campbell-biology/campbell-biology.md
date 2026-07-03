---
activity_status: active
category: DataSource
contacts: []
creation_date: '2026-07-03T00:00:00Z'
description: Campbell Biology (by Reece, Urry, Cain, Wasserman, Minorsky, and Jackson;
  published by Pearson) is a widely used undergraduate introductory biology textbook.
  It is the source text encoded by SRI International's AURA / Project Halo effort
  to produce the KB Bio 101 knowledge base.
domains:
- general
- biomedical
homepage_url: https://openlibrary.org/isbn/9780134093413
id: campbell-biology
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Campbell Biology
products:
- category: Product
  description: Bibliographic catalog record for the Campbell Biology textbook.
  format: http
  id: campbell-biology.openlibrary
  name: Campbell Biology (Open Library record)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: campbell-biology
  product_url: https://openlibrary.org/isbn/9780134093413
- category: Product
  description: The full KB Bio 101 knowledge base exported from SRI's AURA system.
    It is offered as a downloadable archive in five logic serializations (first-order
    predicate logic, TPTP FOF, Answer Set Programming, SILK rule language, and OWL2),
    available as single-file or per-concept file versions.
  format: owl
  id: bio101.exported-kb
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/3.0/
    label: CC BY-NC-SA 3.0
  name: KB Bio 101 Exported Knowledge Base
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bio101
  - relation_type: prov:wasDerivedFrom
    source: campbell-biology
  product_url: https://www.ai.sri.com/~halo/public/exported-kb/biokb.html
---
Campbell Biology

## Description

Campbell Biology is a comprehensive undergraduate introductory biology
textbook authored by Jane B. Reece, Lisa A. Urry, Michael L. Cain,
Steven A. Wasserman, Peter V. Minorsky, and Robert B. Jackson, and published
by Pearson. It is included in KG-Registry as the upstream source text for the
KB Bio 101 knowledge base, which encodes the textbook's content as formal
logic. The textbook is not itself a machine-readable data resource; this entry
exists to record the provenance of resources derived from it.