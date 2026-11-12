---
reference_id: DOI:10.5281/zenodo.24144112
title: "BioBTree: An Integrated Biomedical Graph Database for Researchers and LLM Agents"
authors:
- "Gür, Tamer"
journal: Zenodo
year: '2026'
doi: 10.5281/zenodo.24144112
keywords:
- biomedical knowledge graph
- data integration
- Model Context Protocol
- large language models
- retrieval
- benchmark
content_type: abstract_only
supplementary_files:
  - filename: Gur_2026_BioBTree_preprint.pdf
    download_url: "https://zenodo.org/api/records/24144112/files/Gur_2026_BioBTree_preprint.pdf/content"
    size_bytes: 540301
    checksum: md5:18be4b50770b432b85873820c181bbe9
---

# BioBTree: An Integrated Biomedical Graph Database for Researchers and LLM Agents
**Authors:** Gür, Tamer
**Journal:** Zenodo (2026)
**DOI:** [10.5281/zenodo.24144112](https://doi.org/10.5281/zenodo.24144112)

## Content

Answering a biomedical question usually means combining several databases, each with its own identifiers. Large language models (LLMs) with search tools now retrieve individual facts reliably, but questions that need a complete set of records, a join across identifier systems or repeated retrieval at scale remain error-prone. We present BioBTree, a graph database that integrates more than 95 public biomedical sources into one cross-reference graph of 3.5 billion entries and 9.3 billion cross-references, each stored in both directions, complemented by 11.7 billion position-level variant scores. Multi-hop traversals are written as chain queries and served through a REST API and a Model Context Protocol (MCP) server, available publicly and for local deployment, so researchers, pipelines and LLM agents issue the same queries. We evaluated two LLMs using BioBTree as an MCP tool against the same LLMs without tools and with web search, on 900 GeneTuring and 160 LAB-Bench questions and three study-specific tasks. BioBTree raised accuracy from 379/900 to 833/900 on GeneTuring and from 72/160 to 157/160 on LAB-Bench. Compared with web search, accuracy was 12 points higher overall, similar on most single-record lookups and much higher where a complete set or a computed statistic was needed: 84/100 against 34/100 on transcription-factor regulation and 74/100 against 44/100 on gene ontology. A second LLM reproduced the overall difference (841/900 against 733/900). With BioBTree, the LLMs also needed fewer tool calls and answered 1.2 to 11 times faster. An integrated graph therefore complements LLM agents where completeness, cross-source joins or repetition matter. BioBTree is open source (AGPL-3.0) at https://github.com/tamerh/biobtree, with a public instance at https://sugi.bio.