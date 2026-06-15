---
reference_id: DOI:10.5281/zenodo.18962899
title: "BioBTree v2: Grounding LLM Responses with Large-Scale Structured Biomedical Data"
authors:
- "Gur, Tamer"
journal: Zenodo
year: '2026'
doi: 10.5281/zenodo.18962899
keywords:
- Bioinformatics
- "FOS: Computer and information sciences"
- Graph Database
- MCP
- LLM
content_type: abstract_only
supplementary_files:
  - filename: main.pdf
    download_url: "https://zenodo.org/api/records/18962899/files/main.pdf/content"
    size_bytes: 535417
    checksum: md5:93fa509f6b77caeba61bdeedf5f0d36f
  - filename: supplementary.pdf
    download_url: "https://zenodo.org/api/records/18962899/files/supplementary.pdf/content"
    size_bytes: 621188
    checksum: md5:f4a1552c8000d3726dac3a13de2be681
---

# BioBTree v2: Grounding LLM Responses with Large-Scale Structured Biomedical Data
**Authors:** Gur, Tamer
**Journal:** Zenodo (2026)
**DOI:** [10.5281/zenodo.18962899](https://doi.org/10.5281/zenodo.18962899)

## Content

Biological systems are inherently interconnected, and understanding their mechanisms often requires examining data from multiple angles—genomic, proteomic, chemical, clinical—yet these data reside in specialized databases with different identifiers, formats, and interfaces. We present BioBTree v2, a biomedical graph database that unifies more than fifty primary databases—across genes, proteins, chemical compounds, pathways, diseases, and clinical data, with complementary sources in key domains to maximize coverage—into a queryable graph with billions of connections. Users traverse this graph using an intuitive chain query syntax, replacing multi-step manual workflows with single-line queries. Through a Model Context Protocol (MCP) server, Large Language Models can directly query and reason over this graph, grounding their responses in structured database records. We evaluate this approach through four use cases comparing BioBTree-augmented LLM responses against three baseline LLMs (ChatGPT, Gemini, Claude) across drug safety, drug mechanism, clinical gene annotation, and transcription factor network analysis. Across all four use cases, BioBTree provided quantitative data, verified identifiers, and specialized database content, demonstrating that combining structured database access with LLM reasoning yields more comprehensive results for biomedical research. BioBTree v2 is open source (GPL-v3) and available at https://github.com/tamerh/biobtree. A publicly accessible instance with MCP and REST API endpoints is hosted at https://sugi.bio.