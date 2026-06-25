---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://allenai.org/
  label: Allen Institute for AI (AI2)
creation_date: '2026-06-18T00:00:00Z'
description: 'CORD-19 (the COVID-19 Open Research Dataset) is a freely available corpus
  of tens of thousands of scholarly articles about COVID-19, SARS-CoV-2, and the broader
  coronavirus family, assembled by the Allen Institute for AI (AI2) in partnership
  with the White House Office of Science and Technology Policy (OSTP), the National
  Library of Medicine (NLM), Microsoft Research, the Chan Zuckerberg Initiative, and
  others. Each release packaged article metadata, machine-readable full text (parsed
  from PDFs and PubMed Central XML), and precomputed document embeddings, making the
  corpus a widely used resource for text mining, information retrieval, and natural
  language processing during the pandemic. It is an upstream literature source for
  KG-COVID-19. The dataset is no longer maintained; its final release was issued on
  2 June 2022 and AI2 has since sunset the project.'
domains:
- literature
- biomedical
- public health
- information technology
homepage_url: https://allenai.org/data/cord-19
id: cord-19
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: CORD-19 dataset license (per-article licenses; see dataset license agreement)
name: COVID-19 Open Research Dataset
products:
- category: Dataset
  description: The CORD-19 corpus, comprising article metadata, machine-readable full
    text, and precomputed document embeddings. Releases were distributed as compressed
    archives; historical releases (first 2020-03-13, final 2022-06-02) remain hosted
    on AWS S3 and are documented in the AI2 repository.
  format: json
  id: cord-19.corpus
  name: CORD-19 corpus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cord-19
  product_url: https://github.com/allenai/cord19
- category: DataProduct
  description: AI2 data landing page describing the CORD-19 corpus, its structure,
    and access to historical releases.
  format: http
  id: cord-19.landing
  name: CORD-19 download / landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cord-19
  product_url: https://allenai.org/data/cord-19
publications:
- authors:
  - Wang LL
  - Lo K
  - Chandrasekhar Y
  - Reas R
  - Yang J
  - Burdick D
  - Eide D
  - Funk K
  - Katsis Y
  - Kinney R
  - Li Y
  - Liu Z
  - Merrill W
  - Mooney P
  - Murdick D
  - Rishi D
  - Sheehan J
  - Shen Z
  - Stilson B
  - Wade A
  - Wang K
  - Wilhelm C
  - Xie B
  - Raymond D
  - Weld DS
  - Etzioni O
  - Kohlmeier S
  id: https://www.ncbi.nlm.nih.gov/pubmed/32510522
  journal: ArXiv
  preferred: true
  title: 'CORD-19: The COVID-19 Open Research Dataset'
  year: '2020'
repository: https://github.com/allenai/cord19
---

## Description

CORD-19, the COVID-19 Open Research Dataset, is a freely available corpus of tens
of thousands of scholarly articles about COVID-19, SARS-CoV-2, and related
coronaviruses. It was created by the Allen Institute for AI (AI2) together with the
White House OSTP, the National Library of Medicine, Microsoft Research, the Chan
Zuckerberg Initiative, and other partners. Each release bundled article metadata,
machine-readable full text, and precomputed document embeddings, and the corpus
became a heavily used substrate for text mining and NLP work during the pandemic.
CORD-19 is an upstream literature source for KG-COVID-19.

The dataset is **inactive**: its final release was issued on 2 June 2022, after
which AI2 sunset the project. Historical releases remain accessible for archival
and reproducibility purposes.

## Products

- **CORD-19 corpus** — article metadata, full text, and document embeddings;
  documented in the [allenai/cord19 repository](https://github.com/allenai/cord19),
  with historical releases on AWS S3.
- **CORD-19 download / landing page** — the [AI2 data page](https://allenai.org/data/cord-19)
  describing the corpus and access to past releases.
